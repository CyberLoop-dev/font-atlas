#!/usr/bin/env python3
"""Inspect local font metadata and build a self-contained specimen page."""
import argparse
import base64
import html
from pathlib import Path
from fontTools.ttLib import TTFont

def name_value(font, name_id):
    for record in font["name"].names:
        if record.nameID == name_id:
            try:
                return record.toUnicode()
            except UnicodeDecodeError:
                continue
    return "Unknown"

def inspect_font(path: Path):
    font = TTFont(str(path), lazy=True)
    try:
        cmap = font.getBestCmap() or {}
        return {
            "file": path.name,
            "family": name_value(font, 1),
            "style": name_value(font, 2),
            "full_name": name_value(font, 4),
            "version": name_value(font, 5),
            "postscript": name_value(font, 6),
            "glyphs": int(font["maxp"].numGlyphs),
            "unicode_points": len(cmap),
        }
    finally:
        font.close()

def build_html(font_paths):
    cards = []
    for index, path in enumerate(font_paths):
        info = inspect_font(path)
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        family = "Font" + str(index)
        fmt = "opentype" if path.suffix.lower() == ".otf" else "truetype"
        css = f"@font-face{{font-family:'{family}';src:url(data:font/{fmt};base64,{encoded}) format('{fmt}');}}"
        details = " · ".join(f"{html.escape(k)}: {html.escape(str(v))}" for k,v in info.items() if k != "file")
        cards.append(f"<style>{css}</style><article><h2>{html.escape(info['family'])} — {html.escape(info['style'])}</h2><p>{details}</p><div style=\"font-family:{family};font-size:34px\">Sphinx of black quartz, judge my vow.</div><small>{html.escape(path.name)}</small></article>")
    return "<!doctype html><meta charset='utf-8'><title>Font Atlas</title><style>body{font:16px system-ui;background:#0b1220;color:#e2e8f0;padding:32px}article{background:#172235;border:1px solid #2dd4bf55;border-radius:18px;padding:24px;margin:18px auto;max-width:900px}p,small{color:#94a3b8}</style><h1>Font Atlas</h1>" + "".join(cards)

def main():
    parser = argparse.ArgumentParser(description="Inspect TTF/OTF files and create a specimen HTML report.")
    parser.add_argument("path", type=Path, help="Font file or directory")
    parser.add_argument("--output", type=Path, default=Path("font-atlas.html"))
    args = parser.parse_args()
    paths = sorted(args.path.glob("*.ttf")) + sorted(args.path.glob("*.otf")) if args.path.is_dir() else [args.path]
    if not paths or any(not p.is_file() for p in paths):
        parser.error("No readable font files found.")
    try:
        report = build_html(paths)
    except Exception as exc:
        parser.error(str(exc))
    args.output.write_text(report, encoding="utf-8")
    print(f"Inspected {len(paths)} font(s): {args.output}")
if __name__ == "__main__":
    main()

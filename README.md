<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0d9488&height=170&section=header&text=Font%20Atlas&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%" alt="Font Atlas banner">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=21&pause=900&color=2DD4BF&center=true&vCenter=true&width=700&lines=Inspect%20local%20TTF%20and%20OTF%20font%20metadata%20and%20generate%20a%20self-contained%20specimen%20page." alt="Animated project title">
</p>
<p align="center">
<a href="https://github.com/CyberLoop-dev/font-atlas/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CyberLoop-dev/font-atlas?style=flat-square" alt="License"></a>
<img src="https://img.shields.io/badge/language-Python-0d9488?style=flat-square" alt="Python">
<a href="https://github.com/CyberLoop-dev/font-atlas/stargazers"><img src="https://img.shields.io/github/stars/CyberLoop-dev/font-atlas?style=flat-square" alt="Stars"></a>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/font-atlas?style=flat-square" alt="Last commit">
</p>
<p align="center"><img src="assets/icon.svg" width="520" alt="Font Atlas custom illustration"></p>

## 🧭 Overview
Inspect local TTF and OTF font metadata and generate a self-contained specimen page.. A small, local-first project designed to solve one focused problem with a simple workflow.

## ✨ Features
- 🔤 Read family, style, version, PostScript name, and glyph counts.
- 🧾 Generate a standalone HTML specimen for each selected font.
- 📎 Embed local font bytes in the report so it travels as one file.
- 🔒 All processing stays on your machine.

## 🖥️ Demo
~~~bash
python main.py examples --output font-atlas.html
~~~
The demo uses local sample input. No hosted service or external account is required.

## 🚀 Quick Start
~~~bash
git clone https://github.com/CyberLoop-dev/font-atlas.git
cd font-atlas
python main.py examples --output font-atlas.html
~~~

## 🧰 Tech Stack
- Python 3.10+
- fontTools (TTFont)
- HTML and base64 from the standard library

## 🗂️ Folder Structure
~~~text
font-atlas/\n├── assets/icon.svg\n├── examples/\n├── tests/test_main.py\n├── LICENSE\n├── README.md\n├── main.py\n└── requirements.txt
~~~

## 🗺️ Roadmap
- [ ] Add drag-and-drop folder selection in a small local web UI.
- [ ] Export a machine-readable JSON inventory.

## 🤝 Contributing
Bug reports and focused pull requests are welcome. Add or update tests when changing behavior, and keep the project easy to run locally.

## 📄 License
Released under the MIT License. See LICENSE.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d9488,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer"></p>

import unittest
from main import name_value

class FontAtlasTests(unittest.TestCase):
    def test_missing_name_is_safe(self):
        class EmptyName:
            names = []
        class FakeFont(dict):
            pass
        fake = FakeFont(name=EmptyName())
        self.assertEqual(name_value(fake, 1), "Unknown")

if __name__ == "__main__":
    unittest.main()

import re
import unittest
from pathlib import Path

class ReadmeLinksTest(unittest.TestCase):
    def test_animation_readme_relative_links_exist(self):
        readme = Path(__file__).resolve().parents[1] / "scripts" / "animation" / "README.md"
        self.assertTrue(readme.exists(), f"README not found at {readme}")
        for _, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", readme.read_text()):
            if target.startswith(("http://", "https://")) or not target.endswith(".md"):
                continue
            resolved = readme.parent / target
            self.assertTrue(resolved.exists(), f"README link points to missing file: {target} (resolved to {resolved})")

if __name__ == "__main__":
    unittest.main()

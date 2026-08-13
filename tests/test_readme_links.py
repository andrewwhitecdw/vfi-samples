import os
import re
import unittest


class TestReadmeLinks(unittest.TestCase):
    def test_animation_readme_links_exist(self):
        """Verify relative links in scripts/animation/README.md point to existing files."""
        readme_path = os.path.join(
            os.path.dirname(__file__), "..", "scripts", "animation", "README.md"
        )
        readme_dir = os.path.dirname(readme_path)
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        for match in re.finditer(r"\]\(([^)]+)\)", content):
            link = match.group(1)
            if link.startswith("http") or link.startswith("#") or "://" in link:
                continue
            target = os.path.normpath(os.path.join(readme_dir, link))
            self.assertTrue(
                os.path.exists(target),
                f"README link target does not exist: {link} -> {target}",
            )


if __name__ == "__main__":
    unittest.main()

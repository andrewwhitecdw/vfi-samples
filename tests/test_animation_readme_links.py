import re
import unittest
from pathlib import Path


class TestAnimationReadmeLinks(unittest.TestCase):
    def test_value_clip_links_are_relative_to_readme(self):
        repo_root = Path(__file__).resolve().parents[1]
        readme = repo_root / "scripts" / "animation" / "README.md"
        self.assertTrue(readme.exists(), f"README not found: {readme}")
        text = readme.read_text()
        for label, link in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text):
            if "VALUE_CLIP" in label or "VALUE_CLIP" in link:
                self.assertFalse(
                    link.startswith("scripts/animation/"),
                    f"Link {link!r} has redundant scripts/animation/ prefix",
                )
                target = readme.parent / link
                self.assertTrue(
                    target.exists(),
                    f"Target file for link {link!r} does not exist: {target}",
                )



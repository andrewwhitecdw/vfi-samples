import re
import unittest
from pathlib import Path


class TestReadmeNumbering(unittest.TestCase):
    def setUp(self):
        self.readme = Path(__file__).resolve().parents[1] / "scripts" / "animation" / "README.md"

    def test_usd_anim_asset_extractor_steps_are_sequential(self):
        text = self.readme.read_text(encoding="utf-8")
        section_match = re.search(
            r"### USD animation asset extractor.*?#### Applying the value clip",
            text,
            re.DOTALL,
        )
        self.assertIsNotNone(section_match, "Asset extractor section not found")
        section = section_match.group(0)

        # Find the 'To use:' numbered list inside this section
        list_match = re.search(
            r"To use:\s*\n((?:\d+\.\s+.*?\n)+)",
            section,
        )
        self.assertIsNotNone(list_match, "'To use:' list not found")
        steps = re.findall(r"^\d+\.", list_match.group(1), re.MULTILINE)
        expected = [f"{i}." for i in range(1, len(steps) + 1)]
        self.assertListEqual(steps, expected, f"Step numbering is not sequential: {steps}")


if __name__ == "__main__":
    unittest.main()

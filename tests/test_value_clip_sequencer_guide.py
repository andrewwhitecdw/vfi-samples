import unittest
from pathlib import Path


class ValueClipSequencerGuideTest(unittest.TestCase):
    def test_guide_references_existing_script(self):
        repo_root = Path(__file__).resolve().parents[1]
        guide_path = repo_root / "scripts" / "animation" / "VALUE_CLIP_SEQUENCER_GUIDE.md"
        script_path = repo_root / "scripts" / "animation" / "value_clip_sequencer.py"
        self.assertTrue(guide_path.exists(), "Guide file missing")
        self.assertTrue(script_path.exists(), "Script file missing")
        guide = guide_path.read_text(encoding="utf-8")
        self.assertNotIn("simple_clip_sequencer.py", guide, "Guide references old script name")
        self.assertIn("value_clip_sequencer.py", guide, "Guide does not reference current script name")

if __name__ == "__main__":

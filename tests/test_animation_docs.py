import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class AnimationDocsTest(unittest.TestCase):
    def test_value_clip_sequencer_guide_refers_to_correct_script(self):
        guide_path = os.path.join(
            REPO_ROOT, "scripts", "animation", "VALUE_CLIP_SEQUENCER_GUIDE.md"
        )
        self.assertTrue(os.path.exists(guide_path), "Guide file must exist")
        with open(guide_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("simple_clip_sequencer.py", content)

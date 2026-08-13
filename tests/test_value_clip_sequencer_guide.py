import re
from pathlib import Path

import pytest


def test_guide_references_correct_sequencer_script():
    """The Value Clip Sequencer guide must reference the script that is actually shipped."""
    guide = Path("scripts/animation/VALUE_CLIP_SEQUENCER_GUIDE.md")
    assert guide.exists(), "Value Clip Sequencer guide is missing"

    text = guide.read_text(encoding="utf-8")
    py_refs = re.findall(r"`(\w+\.py)`", text)
    assert "value_clip_sequencer.py" in py_refs, "Guide should reference value_clip_sequencer.py"

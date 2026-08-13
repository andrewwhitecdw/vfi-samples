import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
GUIDE = REPO_ROOT / "scripts" / "animation" / "VALUE_CLIP_SEQUENCER_GUIDE.md"
SCRIPT = REPO_ROOT / "scripts" / "animation" / "value_clip_sequencer.py"


def test_value_clip_sequencer_guide_references_correct_script():
    assert GUIDE.exists(), "Value Clip Sequencer guide is missing"
    text = GUIDE.read_text(encoding="utf-8")
    # The guide should tell users to run the actual script in the repo.
    assert "`value_clip_sequencer.py`" in text
    assert "`simple_clip_sequencer.py`" not in text


def test_value_clip_sequencer_script_exists():
    assert SCRIPT.exists(), (
        "The user guide references value_clip_sequencer.py, "
        "but the script file is missing"
    )
    assert SCRIPT.is_file()

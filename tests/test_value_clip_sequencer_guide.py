from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
GUIDE = REPO_ROOT / "scripts" / "animation" / "VALUE_CLIP_SEQUENCER_GUIDE.md"
SCRIPT = REPO_ROOT / "scripts" / "animation" / "value_clip_sequencer.py"


def test_guide_references_correct_script():
    content = GUIDE.read_text(encoding="utf-8")

    assert SCRIPT.exists(), "value_clip_sequencer.py must exist"
    assert "value_clip_sequencer.py" in content, "guide should reference value_clip_sequencer.py"
    assert "simple_clip_sequencer.py" not in content, "guide should not reference simple_clip_sequencer.py"

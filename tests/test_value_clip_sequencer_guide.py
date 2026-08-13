import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
GUIDE = REPO_ROOT / "scripts" / "animation" / "VALUE_CLIP_SEQUENCER_GUIDE.md"

def test_guide_uses_existing_sequencer_script():
    assert GUIDE.exists(), "VALUE_CLIP_SEQUENCER_GUIDE.md must exist"
    text = GUIDE.read_text()
    assert "simple_clip_sequencer.py" not in text, (
        "guide references non-existent simple_clip_sequencer.py"
    )
    assert "value_clip_sequencer.py" in text, (
        "guide should instruct users to run value_clip_sequencer.py"

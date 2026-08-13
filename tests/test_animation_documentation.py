import pathlib


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
GUIDE = REPO_ROOT / "scripts" / "animation" / "VALUE_CLIP_SEQUENCER_GUIDE.md"


def test_value_clip_sequencer_guide_references_real_script():
    assert GUIDE.exists(), f"Guide not found at {GUIDE}"
    text = GUIDE.read_text(encoding="utf-8")
    assert "simple_clip_sequencer.py" not in text, (
        "Guide references non-existent simple_clip_sequencer.py"
    )
    assert "value_clip_sequencer.py" in text, (
        "Guide should tell users to load value_clip_sequencer.py"

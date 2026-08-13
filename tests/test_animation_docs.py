from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
GUIDE = REPO_ROOT / "scripts" / "animation" / "VALUE_CLIP_SEQUENCER_GUIDE.md"
SCRIPT = REPO_ROOT / "scripts" / "animation" / "value_clip_sequencer.py"

def test_value_clip_sequencer_guide_references_real_script():
    assert GUIDE.exists(), "User guide is missing"
    assert SCRIPT.exists(), "Referenced sequencer script is missing"

    content = GUIDE.read_text(encoding="utf-8")
    assert "simple_clip_sequencer.py" not in content, (
        "User guide references outdated script name simple_clip_sequencer.py"

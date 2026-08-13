import pathlib


def test_value_clip_sequencer_guide_references_correct_script():
    repo_root = pathlib.Path(__file__).parent.parent
    guide_path = repo_root / "scripts" / "animation" / "VALUE_CLIP_SEQUENCER_GUIDE.md"
    script_path = repo_root / "scripts" / "animation" / "value_clip_sequencer.py"

    assert guide_path.exists(), "Value Clip Sequencer guide is missing"
    assert script_path.exists(), "value_clip_sequencer.py script is missing"

    guide_text = guide_path.read_text()
    assert "value_clip_sequencer.py" in guide_text, (
        "User guide should reference the shipped value_clip_sequencer.py script"
    )
    assert "simple_clip_sequencer.py" not in guide_text, (
        "User guide should not reference the old simple_clip_sequencer.py script"
    )

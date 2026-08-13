import pathlib
import re

README = pathlib.Path(__file__).parents[1] / "scripts" / "animation" / "README.md"


def test_usd_anim_asset_extractor_usage_steps_are_sequential():
    text = README.read_text(encoding="utf-8")
    section = text.split("### USD animation asset extractor")[1].split("###")[0]
    numbers = [
        int(match.group(1))
        for match in re.finditer(r"^(\d+)\.", section, re.MULTILINE)
    ]
    # The extractor section contains two numbered lists; both should be [1, 2, 3].
    assert numbers[:3] == [1, 2, 3], f"Expected [1, 2, 3], got {numbers[:3]}"
    assert numbers[3:] == [1, 2, 3], f"Expected [1, 2, 3], got {numbers[3:]}"

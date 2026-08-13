import re
from pathlib import Path


def test_convert_orient_readme_steps():
    readme_path = Path("scripts/animation/README.md")
    readme = readme_path.read_text(encoding="utf-8")
    match = re.search(
        r"### Convert Orient to Eulers.*?To use:\n\n(.*?)\n\nThe data has now been converted to Eulers\.",
        readme,
        re.DOTALL,
    )
    assert match, "Convert Orient usage section not found"
    steps = match.group(1)
    assert steps.startswith(
        "1. Copy the script to a location on your hard drive."
    ), "First step should be to copy the script"
    assert (
        "Select the prim that contains the hierarchy of timeSample animation and execute the script."
        not in steps

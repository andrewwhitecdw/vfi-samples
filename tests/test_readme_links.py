import re
from pathlib import Path


def test_animation_readme_links_are_sibling_paths():
    readme = Path(__file__).parent.parent / "scripts" / "animation" / "README.md"
    text = readme.read_text()
    link_targets = re.findall(r"\[([^\]]+)\]\(([^\)]+)\)", text)
    for label, target in link_targets:
        if target.endswith(".md") and not target.startswith(("http://", "https://", "#")):
            assert "scripts/animation/" not in target, (
                f"README link {label!r} uses nested path {target!r}; "
                "use a sibling filename since README is already in scripts/animation/"

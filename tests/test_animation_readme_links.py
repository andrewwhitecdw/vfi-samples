import re
from pathlib import Path


def _find_readme():
    start = Path(__file__).resolve().parent
    for parent in [start, *start.parents]:
        candidate = parent / "scripts" / "animation" / "README.md"
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Could not find scripts/animation/README.md")


def test_animation_readme_links_are_relative_to_sibling_files():
    readme_path = _find_readme()
    content = readme_path.read_text(encoding="utf-8")
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)

    broken = []
    missing = []
    for _text, href in links:
        if href.startswith("http") or href.startswith("#"):
            continue
        # README.md sits next to the guides, so a scripts/animation/ prefix
        # would resolve to a non-existent nested directory on GitHub.
        if "scripts/animation/" in href:
            broken.append(href)
            continue
        target = readme_path.parent / href
        if not target.exists():
            missing.append(str(target))

    assert not broken, f"README contains broken nested paths: {broken}"
    assert not missing, f"README links point to missing files: {missing}"



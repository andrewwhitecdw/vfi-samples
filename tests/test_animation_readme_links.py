import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
README = REPO_ROOT / "scripts" / "animation" / "README.md"

_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

def test_animation_readme_links_resolve():
    assert README.exists(), f"README not found at {README}"
    text = README.read_text(encoding="utf-8")
    links = _LINK_RE.findall(text)
    assert links, "No markdown links found in README"

    readme_dir = README.parent
    for label, href in links:
        if href.startswith("#") or "://" in href:
            continue
        target = readme_dir / href
        assert target.exists(), (
            f"README link {label!r} points to missing file: {href}"
        )

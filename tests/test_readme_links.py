import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "scripts" / "animation" / "README.md"

def test_animation_readme_links_are_not_nested():
    """Ensure relative .md links in scripts/animation/README.md do not repeat scripts/animation/."""
    content = README.read_text(encoding="utf-8")
    for label, url in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content):
        if url.endswith(".md"):
            assert "scripts/animation/" not in url, (
                f"Nested relative link found in {README}: [{label}]({url}) "
                "points to a non-existent scripts/animation/scripts/animation/... path."
            )

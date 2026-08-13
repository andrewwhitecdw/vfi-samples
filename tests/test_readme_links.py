import os
import re

def test_animation_readme_relative_links_resolve():
    """Verify that relative links in scripts/animation/README.md point to existing files."""
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(repo_root, "scripts", "animation", "README.md")
    assert os.path.exists(readme_path), f"README not found: {readme_path}"

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    for label, link in link_pattern.findall(content):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = os.path.normpath(os.path.join(os.path.dirname(readme_path), link))
        assert os.path.exists(target), f"Broken relative link in README: {link} -> {target}"

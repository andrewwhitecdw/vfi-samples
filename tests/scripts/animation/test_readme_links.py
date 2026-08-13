import os
import re


def test_readme_local_markdown_links_are_relative():
    readme_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts', 'animation', 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for text, url in links:
        if url.endswith('.md') and not url.startswith(('http://', 'https://', '#')):
            assert not url.startswith('scripts/animation/'), (
                f"Local markdown link {url!r} incorrectly includes scripts/animation/ prefix"

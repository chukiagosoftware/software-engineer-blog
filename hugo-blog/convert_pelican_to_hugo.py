#!/usr/bin/env python3
"""
Convert Pelican markdown files to Hugo format.
Changes:
1. Convert Pelican metadata format to Hugo YAML front matter
2. Change {attach}images/file.png to /images/file.png
3. Change {filename}file.md to {{< ref "file.md" >}}
"""

import re
import os
from pathlib import Path

PELICAN_CONTENT = Path('../content')
HUGO_CONTENT_POSTS = Path('./content/posts')
HUGO_CONTENT_PAGES = Path('./content')

# Create Hugo content directories
HUGO_CONTENT_POSTS.mkdir(parents=True, exist_ok=True)
HUGO_CONTENT_PAGES.mkdir(parents=True, exist_ok=True)

def convert_metadata_to_hugo(content):
    """Convert Pelican metadata to Hugo YAML front matter"""
    lines = content.split('\n')
    metadata = {}
    body_start = 0

    # Parse Pelican metadata
    for i, line in enumerate(lines):
        if not line.strip():
            body_start = i + 1
            break
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip().lower()] = value.strip()

    # Build Hugo front matter
    hugo_frontmatter = ['---']

    if 'title' in metadata:
        hugo_frontmatter.append(f'title: "{metadata["title"]}"')
    if 'date' in metadata:
        hugo_frontmatter.append(f'date: {metadata["date"]}')
    if 'category' in metadata:
        hugo_frontmatter.append(f'categories: ["{metadata["category"]}"]')
    if 'tags' in metadata:
        tags = [t.strip() for t in metadata['tags'].split(',')]
        hugo_frontmatter.append(f'tags: {tags}')
    if 'authors' in metadata:
        hugo_frontmatter.append(f'author: "{metadata["authors"]}"')
    if 'summary' in metadata:
        hugo_frontmatter.append(f'description: "{metadata["summary"]}"')

    hugo_frontmatter.append('draft: false')
    hugo_frontmatter.append('---')
    hugo_frontmatter.append('')

    # Get body content
    body = '\n'.join(lines[body_start:])

    # Convert {attach}images/file.png to /images/file.png
    body = re.sub(r'\{attach\}images/', '/images/', body)

    # Convert {filename}file.md to {{< ref "file.md" >}}
    body = re.sub(r'\{filename\}([^)]+\.md)', r'{{< ref "\1" >}}', body)

    return '\n'.join(hugo_frontmatter) + '\n' + body

def main():
    converted_posts = 0
    converted_pages = 0

    # Convert post markdown files
    for md_file in PELICAN_CONTENT.glob('*.md'):
        print(f'Converting post {md_file.name}...')

        content = md_file.read_text(encoding='utf-8')
        hugo_content = convert_metadata_to_hugo(content)

        # Write to Hugo posts directory
        output_file = HUGO_CONTENT_POSTS / md_file.name
        output_file.write_text(hugo_content, encoding='utf-8')
        print(f'  -> {output_file}')
        converted_posts += 1

    # Convert page markdown files
    pages_dir = PELICAN_CONTENT / 'pages'
    if pages_dir.exists():
        for md_file in pages_dir.glob('*.md'):
            print(f'Converting page {md_file.name}...')

            content = md_file.read_text(encoding='utf-8')
            hugo_content = convert_metadata_to_hugo(content)

            # Write to Hugo pages directory (content root)
            output_file = HUGO_CONTENT_PAGES / md_file.name
            output_file.write_text(hugo_content, encoding='utf-8')
            print(f'  -> {output_file}')
            converted_pages += 1

    print(f'\nConverted {converted_posts} posts and {converted_pages} pages')

if __name__ == '__main__':
    main()
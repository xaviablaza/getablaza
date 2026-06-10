#!/usr/bin/env python3
"""Create local Eleventy alias pages for source-site internal links that are referenced but not present.

The copied content graph contains many edge links to planned terms/concepts that are not
separate pages in the source sitemap. We still want every internal href to resolve on
getablaza, so this script crawls the built site and materializes lightweight local pages
for missing internal paths.
"""
from __future__ import annotations

import hashlib
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
OUT = ROOT / 'link-aliases'
HOSTS = {'getablaza.com', 'localhost'}

class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.assets: list[str] = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == 'a' and data.get('href'):
            self.hrefs.append(data['href'])
        if tag in {'img', 'script', 'source', 'link'}:
            for attr in ('src', 'href', 'srcset'):
                if data.get(attr):
                    self.assets.append(data[attr])

def file_for_path(path: str) -> Path:
    if not path or path == '/':
        return SITE / 'index.html'
    if path.endswith('/'):
        return SITE / path.lstrip('/') / 'index.html'
    candidate = SITE / path.lstrip('/')
    if not candidate.exists() and not Path(path).suffix:
        candidate = candidate / 'index.html'
    return candidate

def is_generated_alias_output(path: Path) -> bool:
    if not path.exists() or path.suffix != '.html':
        return False
    try:
        sample = path.read_text(encoding='utf-8', errors='ignore')[:20000]
    except OSError:
        return False
    return 'knowledge graph' in sample and 'home page' in sample

def resolve_internal(url: str, base: str) -> str | None:
    if url.startswith(('mailto:', 'tel:', 'data:', '#')):
        return None
    absolute = urljoin(base, url)
    parsed = urlparse(absolute)
    if parsed.scheme in {'http', 'https'} and parsed.netloc and parsed.netloc not in HOSTS:
        return None
    path = unquote(parsed.path)
    if not path.startswith('/'):
        path = '/' + path
    # Drop obvious markdown/math accidents that resolve as fragments of formulas.
    return path

def title_for(path: str) -> str:
    bits = [b for b in path.strip('/').split('/') if b]
    if not bits:
        return 'Home'
    return bits[-1].replace('-', ' ').replace('_', ' ').title()

def parent_for(path: str) -> str:
    bits = [b for b in path.strip('/').split('/') if b]
    if len(bits) <= 1:
        return '/'
    return '/' + '/'.join(bits[:-1]) + '/'

def yaml_quote(value: str) -> str:
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'

def collect_missing() -> set[str]:
    missing: set[str] = set()
    for html in SITE.rglob('*.html'):
        rel = '/' + str(html.relative_to(SITE)).replace('index.html', '').lstrip('/')
        base = 'https://getablaza.com' + rel
        parser = Parser()
        parser.feed(html.read_text(encoding='utf-8', errors='ignore'))
        for href in parser.hrefs:
            path = resolve_internal(href, base)
            if path:
                target = file_for_path(path)
                if not target.exists() or is_generated_alias_output(target):
                    missing.add(path)
        for asset in parser.assets:
            for item in asset.split(','):
                url = item.strip().split(' ')[0]
                path = resolve_internal(url, base)
                if path and not file_for_path(path).exists():
                    missing.add(path)
    return missing

def main() -> None:
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob('*.md'):
        old.unlink()
    missing = collect_missing()
    for path in sorted(missing):
        digest = hashlib.sha1(path.encode()).hexdigest()[:12]
        parent = parent_for(path)
        title = title_for(path)
        content = '\n'.join([
            '---',
            f'title: {yaml_quote(title)}',
            f'description: {yaml_quote("Navigation alias for " + path)}',
            'layout: layouts/post.njk',
            'templateEngineOverride: md',
            'eleventyExcludeFromCollections: true',
            'draft: false',
            f'permalink: {yaml_quote(path if path.endswith("/") else path + "/")}',
            '---',
            '',
            f'# {title}',
            '',
            'This node is part of the local knowledge graph. Continue from [the home page](/) while the full node is expanded.',
            '',
        ])
        (OUT / f'{digest}.md').write_text(content, encoding='utf-8')
    print(f'generated_aliases={len(missing)}')

if __name__ == '__main__':
    main()

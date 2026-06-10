#!/usr/bin/env python3
import datetime as dt
import hashlib
import html
import json
import mimetypes
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'posts' / 'coming-soon'
ASSET_ROOT = ROOT / 'img' / 'templeton'
PROFILE_OUT = ROOT / 'img' / 'xavi-linkedin-profile.jpg'
BASE = 'https://templeton.host'
SITEMAP = BASE + '/sitemap.xml'
LINKEDIN = 'https://www.linkedin.com/in/xaviablaza'
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125 Safari/537.36 getablaza-deep-copy/3.0'

# These are linked from the source homepage but are not currently listed in its sitemap.
EXTRA_URLS = [
    BASE + '/about/',
    BASE + '/answers/',
    BASE + '/business/',
    BASE + '/experiments/',
    BASE + '/frameworks/',
    BASE + '/frameworks/capital-allocation/',
    BASE + '/frameworks/deity-problem/',
    BASE + '/frameworks/demand-field/',
    BASE + '/frameworks/designed-convergence/',
    BASE + '/frameworks/knowledge-capital/',
    BASE + '/frameworks/performance-frontier/',
    BASE + '/frameworks/promotion-protocol/',
    BASE + '/frameworks/quality-hillclimb/',
    BASE + '/frameworks/verifier-capital/',
    BASE + '/graph/',
    BASE + '/lexicon/',
    BASE + '/money/',
    BASE + '/positions/',
    BASE + '/positions/allocator/',
    BASE + '/positions/operator/',
    BASE + '/positions/builder/',
    BASE + '/positions/scientist/',
    BASE + '/tech-tree/',
    BASE + '/thesis/',
    BASE + '/tools/',
]

OUT.mkdir(parents=True, exist_ok=True)
ASSET_ROOT.mkdir(parents=True, exist_ok=True)


def fetch_bytes(url, timeout=35):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en-US,en;q=0.9'})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read(), response.headers


def fetch_text(url, timeout=35):
    data, _headers = fetch_bytes(url, timeout=timeout)
    return data.decode('utf-8', errors='replace')


def source_to_target_text(value):
    if not isinstance(value, str):
        return value
    replacements = [
        ('Andrew Templeton', 'Xavi Ablaza'),
        ('Andrew\u00a0Templeton', 'Xavi Ablaza'),
        ('Andrew', 'Xavi'),
        ('Templeton Ratio', 'Ablaza Ratio'),
        ('Templeton', 'Ablaza'),
        ('the-andrew-templeton', 'xaviablaza'),
        ('admin@templeton.host', 'xavi@hostari.com'),
        ('templeton.host', 'getablaza.com'),
        ('https://www.linkedin.com/in/xaviablaza/', 'https://www.linkedin.com/in/xaviablaza/'),
        ('https://www.linkedin.com/in/xaviablaza', 'https://www.linkedin.com/in/xaviablaza'),
        ('https://getablaza.com', 'https://getablaza.com'),
        ('https://templeton.host', 'https://getablaza.com'),
    ]
    for old, new in replacements:
        value = value.replace(old, new)
    # Source pages occasionally serialize Unicode escapes as raw C0 controls (e.g. \x03bc).
    # Remove controls that break Eleventy JSON-LD output while preserving normal whitespace.
    value = ''.join(ch for ch in value if ch in '\n\r\t' or ord(ch) >= 32)
    return value


def transform_deep(obj):
    if isinstance(obj, dict):
        return {source_to_target_text(k): transform_deep(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [transform_deep(v) for v in obj]
    return source_to_target_text(obj)


def slugify(value):
    value = value.lower().strip('/ ')
    value = re.sub(r'https?://[^/]+/?', '', value)
    value = re.sub(r'[^a-z0-9]+', '-', value).strip('-')
    return value or 'home'


def category_from_url(url):
    path = urllib.parse.urlparse(url).path.strip('/')
    return path.split('/')[0] if path else 'home'


def title_from_url(url):
    path = urllib.parse.urlparse(url).path.strip('/')
    if not path:
        return 'P&L Engineering: Xavi Ablaza'
    return path.split('/')[-1].replace('-', ' ').title()


def strip_tags(value):
    soup = BeautifulSoup(value or '', 'html.parser')
    return re.sub(r'\s+', ' ', soup.get_text(' ', strip=True)).strip()


def meta(soup, key):
    tag = soup.find('meta', attrs={'name': key}) or soup.find('meta', attrs={'property': key})
    return html.unescape(tag.get('content', '')) if tag else ''


def local_asset_for(url):
    parsed = urllib.parse.urlparse(url)
    clean_path = parsed.path.lstrip('/') or hashlib.sha1(url.encode()).hexdigest()
    if clean_path.startswith('_next/image'):
        qs = urllib.parse.parse_qs(parsed.query)
        nested = qs.get('url', [''])[0]
        if nested:
            return local_asset_for(urllib.parse.urljoin(BASE, nested))
        clean_path = 'next-image-' + hashlib.sha1(url.encode()).hexdigest() + '.bin'
    if clean_path.startswith('images/'):
        clean_path = clean_path[len('images/'):]
    if clean_path.startswith('icons/'):
        clean_path = 'icons/' + clean_path[len('icons/'):]
    ext = Path(clean_path).suffix
    if not ext:
        clean_path += '.bin'
    return ASSET_ROOT / clean_path


def download_asset(url, page_url):
    if not url or url.startswith('data:'):
        return url
    if url.startswith('/img/templeton/') or url.startswith('/img/xavi-'):
        return url
    absolute = urllib.parse.urljoin(page_url, url)
    parsed = urllib.parse.urlparse(absolute)
    if parsed.scheme not in ('http', 'https'):
        return url
    # Only vendor local source media into the repository; leave unrelated outbound URLs alone.
    if parsed.netloc and parsed.netloc != 'templeton.host':
        return absolute
    dest = local_asset_for(absolute)
    public = '/' + str(dest.relative_to(ROOT)).replace('\\', '/')
    if dest.exists() and dest.stat().st_size > 0:
        return public
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        data, headers = fetch_bytes(absolute, timeout=45)
        if dest.suffix == '.bin':
            ctype = headers.get_content_type()
            ext = mimetypes.guess_extension(ctype) or '.bin'
            dest = dest.with_suffix(ext)
            public = '/' + str(dest.relative_to(ROOT)).replace('\\', '/')
        dest.write_bytes(data)
        return public
    except Exception as error:
        print(f'WARN asset failed {absolute}: {error}')
        return absolute


def rewrite_image_refs(markdown, page_url):
    def repl(match):
        alt = match.group(1)
        src = match.group(2).strip()
        return f'![{alt}]({download_asset(src, page_url)})'
    markdown = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', repl, markdown)
    return markdown


def rewrite_local_links(markdown):
    # Keep copied internal links on their canonical local path, not source absolute URLs.
    markdown = re.sub(r'\]\(https://templeton\.host(/[^)\s]*)\)', r'](\1)', markdown)
    markdown = re.sub(r'\]\(https://getablaza\.com(/[^)\s]*)\)', r'](\1)', markdown)
    markdown = markdown.replace('](mailto:xavi@hostari.com)', '](mailto:xavi@hostari.com)')
    markdown = markdown.replace('/lexicon/templeton-ratio/', '/lexicon/ablaza-ratio/')
    markdown = markdown.replace('https://github.com/andrew-templeton', 'https://github.com/xaviablaza')
    markdown = markdown.replace('https://www.linkedin.com/in/the-andrew-templeton', 'https://www.linkedin.com/in/xaviablaza')
    return markdown


def split_frontmatter(markdown):
    if markdown.startswith('---\n'):
        end = markdown.find('\n---', 4)
        if end != -1:
            raw = markdown[4:end]
            body = markdown[end + len('\n---'):].lstrip('\n')
            try:
                return yaml.safe_load(raw) or {}, body
            except Exception:
                return {}, markdown
    return {}, markdown


def markdown_url_for(page_url, soup):
    alt = soup.find('link', attrs={'rel': 'alternate', 'type': 'text/markdown'})
    if alt and alt.get('href'):
        return urllib.parse.urljoin(page_url, alt['href'])
    return None


def html_to_markdown(page_url, html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    title = strip_tags((soup.find('h1') or {}).get_text(' ', strip=True) if soup.find('h1') else '') or meta(soup, 'og:title') or title_from_url(page_url)
    description = meta(soup, 'description') or meta(soup, 'og:description')
    main = soup.find('main') or soup.body or soup
    for selector in ['script', 'style', 'nav', 'noscript']:
        for node in main.find_all(selector):
            node.decompose()
    for a in main.find_all('a'):
        href = a.get('href')
        if not href:
            continue
        href = source_to_target_text(href)
        if href.startswith('https://templeton.host/') or href.startswith('https://getablaza.com/'):
            href = urllib.parse.urlparse(href).path or '/'
        a['href'] = href
    for img in main.find_all('img'):
        src = img.get('src') or img.get('data-src')
        if src:
            img['src'] = download_asset(src, page_url)
        for attr in ['srcset', 'data-srcset']:
            if img.get(attr):
                # Prefer a concrete src; srcset widths do not survive markdown conversion well.
                del img[attr]
    body = md(str(main), heading_style='ATX', bullets='-', strip=['script', 'style']).strip()
    body = re.sub(r'\n{3,}', '\n\n', body)
    return {'title': title, 'summary': description}, body


def canonical_permalink(page_url):
    path = urllib.parse.urlparse(page_url).path or '/'
    if path == '/':
        return None
    return path if path.endswith('/') else path + '/'


def build_page(page_url, index):
    html_doc = fetch_text(page_url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    markdown_url = markdown_url_for(page_url, soup)
    source_format = 'html'
    if markdown_url:
        try:
            raw_md = fetch_text(markdown_url)
            source_fm, body = split_frontmatter(raw_md)
            source_format = 'markdown'
        except Exception as error:
            print(f'WARN markdown failed {markdown_url}: {error}; falling back to HTML')
            source_fm, body = html_to_markdown(page_url, html_doc)
    else:
        source_fm, body = html_to_markdown(page_url, html_doc)

    source_fm = transform_deep(source_fm)
    body = source_to_target_text(body)
    body = rewrite_image_refs(body, page_url)
    body = rewrite_local_links(body)

    title = source_fm.get('title') or title_from_url(page_url)
    title = source_to_target_text(str(title)).strip() or title_from_url(page_url)
    description = source_fm.get('summary') or source_fm.get('description') or meta(soup, 'description') or meta(soup, 'og:description') or title
    description = source_to_target_text(str(description)).strip()
    source_path = urllib.parse.urlparse(page_url).path or '/'
    category = category_from_url(page_url)
    source_date = source_fm.get('published_at') or source_fm.get('date') or source_fm.get('staged_at')
    date = '2026-07-01'
    if source_date:
        m = re.search(r'\d{4}-\d{2}-\d{2}', str(source_date))
        if m:
            date = m.group(0)
    scheduled = dt.date.today().isoformat()
    slug = slugify(source_path)
    filename = OUT / f'{index + 1:03d}-{slug}.md'

    fm = {
        'title': title,
        'description': description,
        'date': date,
        'scheduled': scheduled,
        'tags': ['p-and-l-engineering', 'coming-soon', category],
        'layout': 'layouts/post.njk',
        'templateEngineOverride': 'md',
        'image': '/img/xavi-linkedin-profile.jpg',
        'draft': False,
        'generated_by': 'templeton-deep-copy-import',
        'permalink': canonical_permalink(page_url),
    }
    if source_format != 'html':
        fm['source_format'] = source_format
    if source_fm:
        clean_source = {k: v for k, v in source_fm.items() if k not in fm and k not in ('title', 'description', 'summary', 'date')}
        if clean_source:
            fm['source_frontmatter'] = clean_source

    yaml_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000).strip()
    filename.write_text('---\n' + yaml_text + '\n---\n\n' + body.strip() + '\n', encoding='utf-8')
    return {'file': str(filename.relative_to(ROOT)), 'permalink': fm['permalink'], 'url': page_url, 'title': title, 'category': category, 'source_format': source_format}


def download_linkedin_photo():
    if PROFILE_OUT.exists() and PROFILE_OUT.stat().st_size > 0:
        return 'existing local profile photo'
    html_doc = fetch_text(LINKEDIN, timeout=45)
    soup = BeautifulSoup(html_doc, 'html.parser')
    image = meta(soup, 'og:image')
    if not image:
        raise RuntimeError('LinkedIn og:image not found')
    data, _headers = fetch_bytes(image, timeout=45)
    PROFILE_OUT.write_bytes(data)
    return image


def main():
    # Remove only previous generated imports.
    removed = 0
    for path in OUT.glob('*.md'):
        text = path.read_text(encoding='utf-8', errors='ignore')
        if ('generated_by: templeton-coming-soon-import' in text or
                'generated_by: templeton-deep-copy-import' in text or
                'permalink: /about/' in text or
                'permalink: /frameworks/' in text or
                'permalink: /tools/' in text or
                'permalink: /positions/' in text or
                'permalink: /writing/' in text or
                'permalink: /tech-tree/' in text or
                'permalink: /visualizations/' in text or
                'permalink: /money/' in text or
                'permalink: /business/' in text or
                'permalink: /lexicon/' in text or
                'permalink: /answers/' in text or
                'permalink: /graph/' in text):
            path.unlink()
            removed += 1

    try:
        profile_source = download_linkedin_photo()
    except Exception as error:
        profile_source = f'skipped: {error}'
        print(f'WARN profile photo skipped: {error}')

    xml = fetch_text(SITEMAP)
    root = ET.fromstring(xml)
    namespace = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [node.text.strip() for node in root.findall('.//sm:loc', namespace) if node.text]
    urls.extend(EXTRA_URLS)
    seen = set()
    urls = [url for url in urls if url.startswith(BASE) and not (url in seen or seen.add(url))]

    manifest = []
    failures = []
    # Do not generate pages that are already hand-owned by the existing codebase.
    hand_owned_paths = {'', '/'}
    for index, url in enumerate([u for u in urls if urllib.parse.urlparse(u).path not in hand_owned_paths]):
        try:
            manifest.append(build_page(url, index))
        except Exception as error:
            failures.append({'url': url, 'error': str(error)})
            print(f'ERROR page failed {url}: {error}')
        if (index + 1) % 50 == 0:
            print(f'Processed {index + 1}/{len(urls)}')
        time.sleep(0.03)

    manifest_doc = {
        'generated_at': dt.datetime.now(dt.UTC).isoformat(),
        'source': SITEMAP,
        'source_home_mapped_to': 'index.njk',
        'count': len(manifest),
        'failures': failures,
        'profile_photo_source': profile_source,
        'items': manifest,
    }
    (ROOT / 'posts' / 'coming-soon-manifest.json').write_text(json.dumps(manifest_doc, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Removed {removed} old generated drafts')
    print(f'Downloaded LinkedIn profile photo to {PROFILE_OUT}')
    print(f'Generated {len(manifest)} copied pages under {OUT}')
    print(f'Failures: {len(failures)}')


if __name__ == '__main__':
    main()

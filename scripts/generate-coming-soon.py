import datetime as dt
import html
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

ROOT = Path('/home/administrator/nvg_monorepo/getablaza')
OUT = ROOT / 'posts' / 'coming-soon'
OUT.mkdir(parents=True, exist_ok=True)
BASE = 'https://templeton.host'
SITEMAP = BASE + '/sitemap.xml'


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 getablaza-placeholder-generator/1.0'})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode('utf-8', errors='replace')


def strip_tags(value):
    value = re.sub(r'<script[\s\S]*?</script>', ' ', value, flags=re.I)
    value = re.sub(r'<style[\s\S]*?</style>', ' ', value, flags=re.I)
    value = re.sub(r'<[^>]+>', ' ', value)
    return re.sub(r'\s+', ' ', html.unescape(value)).strip()


def attr_meta(doc, value, attr='content'):
    pattern = re.compile(r'<meta\s+[^>]*(?:name|property)=["\']%s["\'][^>]*>' % re.escape(value), re.I)
    match = pattern.search(doc)
    if not match:
        return ''
    tag = match.group(0)
    content_match = re.search(r'%s=["\']([^"\']*)["\']' % re.escape(attr), tag, re.I)
    return html.unescape(content_match.group(1)) if content_match else ''


def page_info(url) -> dict[str, Any]:
    try:
        doc = fetch(url)
    except Exception as error:
        return {'fetch_error': str(error)}
    title = ''
    title_match = re.search(r'<title[^>]*>(.*?)</title>', doc, re.I | re.S)
    if title_match:
        title = strip_tags(title_match.group(1))
    h1 = ''
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', doc, re.I | re.S)
    if h1_match:
        h1 = strip_tags(h1_match.group(1))
    description = attr_meta(doc, 'description') or attr_meta(doc, 'og:description')
    images = []
    for tag in re.findall(r'<img\s+[^>]*>', doc, flags=re.I):
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', tag, re.I)
        src_match = re.search(r'src=["\']([^"\']*)["\']', tag, re.I)
        alt = html.unescape(alt_match.group(1)) if alt_match else ''
        src = html.unescape(src_match.group(1)) if src_match else ''
        if alt or src:
            images.append({'alt': alt[:220], 'src': src[:220]})
        if len(images) >= 5:
            break
    headings = []
    for heading in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', doc, flags=re.I | re.S):
        text = strip_tags(heading)
        if text and text not in headings:
            headings.append(text[:140])
        if len(headings) >= 6:
            break
    return {'title': title, 'h1': h1, 'description': description, 'images': images, 'headings': headings}


def slugify(value):
    value = value.lower().strip('/ ')
    value = re.sub(r'https?://[^/]+/?', '', value)
    value = re.sub(r'[^a-z0-9]+', '-', value).strip('-')
    return value or 'home'


def category_from_path(path):
    parts = [part for part in path.strip('/').split('/') if part]
    return parts[0] if parts else 'home'


def title_from_url(url):
    path = re.sub(r'^https?://[^/]+', '', url)
    if path in ('', '/'):
        return 'P&L Engineering Home'
    last = [part for part in path.strip('/').split('/') if part][-1]
    return last.replace('-', ' ').title()


def yaml_quote(value):
    return json.dumps(str(value), ensure_ascii=False)


brand_terms = {
    'frameworks': 'framework',
    'tools': 'tool',
    'lexicon': 'lexicon entry',
    'answers': 'problem note',
    'tech-tree': 'technical primitive',
    'business': 'business primitive',
    'money': 'capital note',
    'writing': 'essay',
    'positions': 'operator stance',
    'visualizations': 'visual model',
    'experiments': 'experiment',
    'about': 'about note',
    'home': 'thesis page',
}

xml = fetch(SITEMAP)
namespace = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
root = ET.fromstring(xml)
urls = [node.text.strip() for node in root.findall('.//sm:loc', namespace) if node.text]
seen = set()
urls = [url for url in urls if url.startswith(BASE) and not (url in seen or seen.add(url))]

for path in OUT.glob('*.md'):
    text = path.read_text(encoding='utf-8', errors='ignore')
    if 'generated_by: templeton-coming-soon-import' in text:
        path.unlink()

manifest = []
start_date = dt.date(2026, 7, 1)
for index, url in enumerate(urls):
    source_path = re.sub(r'^https?://[^/]+', '', url)
    category = category_from_path(source_path)
    info = page_info(url)
    raw_title = info.get('h1') or info.get('title') or title_from_url(url)
    raw_title = re.sub(r'\s*[-–|]\s*Andrew Templeton.*$', '', raw_title).strip() or title_from_url(url)
    title = raw_title.replace('Andrew Templeton', 'Xavi Ablaza').replace('Templeton Ratio', 'Operator Ratio').replace('Templeton', 'Operator')
    if category == 'home':
        title = 'P&L Engineering: Xavi Ablaza'
    description_source = info.get('description') or f'A coming-soon {brand_terms.get(category, "post")} for Xavi Ablaza on {raw_title}.'
    description_source = (
        description_source.replace('Andrew Templeton', 'Xavi Ablaza')
        .replace('Templeton Ratio', 'Operator Ratio')
        .replace('Templeton', 'Operator')
        .replace('Group CTO', 'operator')
    )
    description = f'Coming-soon draft for Xavi Ablaza: {description_source[:210]}'
    scheduled = start_date + dt.timedelta(days=index)
    slug = slugify(source_path)
    filename = OUT / f'{index + 1:03d}-{slug}.md'
    tags = ['p-and-l-engineering', 'coming-soon', category]
    inspiration_bits = []
    for heading in info.get('headings', [])[:4]:
        inspiration_bits.append(heading)
    images_info = info.get('images', [])
    if isinstance(images_info, list):
        for image in images_info[:3]:
            if isinstance(image, dict) and image.get('alt'):
                inspiration_bits.append('visual: ' + str(image['alt']))
    if not inspiration_bits:
        inspiration_bits = [raw_title, description_source[:120]]
    kind = brand_terms.get(category, 'post')
    article = 'an' if kind[0].lower() in 'aeiou' else 'a'
    body = []
    body.append('> Coming soon: this is placeholder copy for the Xavi Ablaza P&L Engineering canon. It uses source-route structure and visual cues as scaffolding, not final prose.')
    body.append('')
    body.append('## Operating thesis')
    body.append(f'Lorem ipsum for {article} {kind}: {title} becomes a way to explain how product, infrastructure, finance, and execution all meet inside the P&L. The future essay should translate abstract leverage into decisions an operator can price, sequence, and defend.')
    body.append('')
    body.append('In Xavi’s version, the unit of analysis is not a generic roadmap item. It is a capital instrument: a deployment pipeline, a support process, an incident class, a vendor contract, a model workflow, or a team habit that either compounds margin or consumes it.')
    body.append('')
    body.append('## Placeholder outline')
    body.append('- Map the operating surface: where revenue, cost, latency, trust, and attention move.')
    body.append('- Price the opportunity: expected upside, downside, reversibility, maintenance drag, and opportunity cost.')
    body.append('- Allocate effort like capital: compare this bet against every other engineering and organizational bet.')
    body.append('- Ship with gates: use verifiers, rollback paths, owner clarity, and measured promotion into autonomy.')
    body.append('- Compound the artifact: turn the work into runbooks, dashboards, tests, datasets, and decision language.')
    body.append('')
    body.append('## Visual / source-shape notes')
    for bit in inspiration_bits[:7]:
        clean = bit.replace('Andrew Templeton', 'Xavi Ablaza').replace('Templeton', 'Operator')
        body.append(f'- {clean}')
    body.append('')
    body.append('## Lorem ipsum direction')
    body.append('This placeholder should eventually read like field notes from a technical operator: concise, financially legible, and grounded in production. The diagram should make the P&L edge visible before the prose explains it. The conclusion should leave the reader with a decision rule, not just a metaphor.')
    content = '\n'.join([
        '---',
        f'title: {yaml_quote(title)}',
        f'description: {yaml_quote(description)}',
        f'date: {scheduled.isoformat()}',
        f'scheduled: {scheduled.isoformat()}',
        'tags:',
        *[f'  - {tag}' for tag in tags],
        'layout: layouts/post.njk',
        'image: /img/ablaza-fb-og.png',
        'draft: true',
        'generated_by: templeton-coming-soon-import',
        f'inspiration_url: {yaml_quote(url)}',
        f'inspiration_category: {yaml_quote(category)}',
        '---',
        '',
        '\n'.join(body),
        '',
    ])
    filename.write_text(content, encoding='utf-8')
    manifest.append({'file': str(filename.relative_to(ROOT)), 'url': url, 'title': title, 'category': category})

(ROOT / 'posts' / 'coming-soon-manifest.json').write_text(
    json.dumps({'generated_at': dt.datetime.now(dt.UTC).isoformat(), 'source': SITEMAP, 'count': len(manifest), 'items': manifest}, ensure_ascii=False, indent=2),
    encoding='utf-8',
)
print(f'Generated {len(manifest)} draft placeholder posts under {OUT}')

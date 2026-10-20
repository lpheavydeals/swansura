"""Rebuild the prototype's product images from the live store's full Shopify galleries.

The preview artifact allows at most 511 files and blocks images from other hosts, so
images are packed into sheets:
  prototype/cards/cN.webp    - frames 0 and 1 of 12 products (card + hover), 480x600 cells, 6x4 grid
  prototype/gallery/gN.webp  - every gallery frame, 720x900 cells, 5x4 grid (product page)
Each product in products.json gets ci (first card cell), gi (first gallery cell), frames, alts.

Usage: python3 tools/proto_gallery.py <workdir>
  <workdir>/js/<handle>.json  = https://www.swansura.com/products/<handle>.js
  <workdir>/p1..p3.json       = https://www.swansura.com/products.json?limit=250&page=N
Downloads go to <workdir>/raw/.
"""
import html, json, os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROTO = os.path.join(ROOT, 'prototype')
W = sys.argv[1]
RAW = os.path.join(W, 'raw'); os.makedirs(RAW, exist_ok=True)

CARD = (480, 600, 6, 4)      # cell w, h, cols, rows
GAL = (720, 900, 5, 4)
IVORY = (242, 237, 228)
FRAG_BRANDS = {'Tiziana Terenzi', 'Al Haramain', 'Hemel', "Signature D'orient", 'Fumeri', 'Gucci'}

# ---- catalogue: existing prototype data + live products not yet in it ----
live = [p for i in (1, 2, 3) for p in json.load(open(os.path.join(W, f'p{i}.json')))['products'] if p['title'] != 'Example product']
proto = json.load(open(os.path.join(PROTO, 'products.json')))
have = {q['id'] for q in proto}

def clean_text(h):
    if not h: return ''
    t = re.sub(r'(?i)<br\s*/?>', '\n', h); t = re.sub(r'(?i)</(p|li|h\d|div)>', '\n', t); t = re.sub(r'(?i)<li[^>]*>', '- ', t)
    t = html.unescape(re.sub(r'<[^>]+>', '', t)); t = re.sub(r'[ \t]+', ' ', t)
    return '\n'.join(l.strip() for l in t.split('\n') if l.strip() and not re.match(r'(?i)^(barcode|ean|upc)\b', l.strip()) and not re.match(r'^\d{8,}$', l.strip()))

def brand_of(p):
    if p['title'].startswith('Deyga'): return 'Deyga'
    if 'Vilvah' in p['title']: return 'Vilvah'
    if p['vendor'].lower().startswith('anatom'): return 'anatome'
    return p['vendor']

def cat_of(p, b):
    t = p['title']
    if b in FRAG_BRANDS or re.search(r'(?i)parfum|\bEDP\b|\bEDT\b|perfume|eau de|fragrance|cologne', t): return 'fragrance'
    if re.search(r'(?i)shampoo|conditioner|hair', t): return 'haircare'
    if re.search(r'(?i)body|soap|bath|butter|pillow|sleep|hand cream|foot', t): return 'bath-body'
    return 'skincare'

def tags_of(p, cat):
    t = p['title'] + ' ' + (p['body_html'] or ''); g = []
    if re.search(r'(?i)\b(kit|combo|set|duo|trio|bundle|gift)\b', p['title']): g.append('gift')
    if cat == 'fragrance':
        for k, r in [('oud', 'oud'), ('floral', 'floral|rose|jasmine'), ('woody', 'wood|cedar|sandal|vetiver|patchouli'), ('amber', 'amber|oriental|vanilla'), ('fresh', 'fresh|citrus|aquatic|bergamot')]:
            if re.search('(?i)' + r, t): g.append(k)
        g.append('men' if re.search(r"(?i)\bmen\b|men[’']s|homme|for him", p['title']) else 'women' if re.search(r"(?i)women|femme|for her", p['title']) else 'unisex')
    else:
        for k, r in [('acne', 'acne|pimple|charcoal|tea tree|oil control'), ('glow', r'pigment|dark spot|bright|vitamin c|glow|\btan\b'), ('hydration', 'dry skin|hydrat|moistur|hyaluronic|aloe'), ('hairfall', 'hair ?fall|hair growth|onion'), ('dandruff', 'dandruff'), ('sun', 'sunscreen|spf'), ('calm', 'sleep|relax|calm')]:
            if re.search('(?i)' + r, t): g.append(k)
        if re.search(r'(?i)\blip', p['title']): g.append('lips')
    return g

def short_title(t):
    return re.sub(r'\s+\|.*$', '', re.split(r'\s?[–|]\s', t)[0]).strip()

for p in live:
    if str(p['id']) in have: continue
    b = brand_of(p); c = cat_of(p, b); v = p['variants'][0]
    price, comp = float(v['price']), float(v['compare_at_price'] or 0)
    proto.append({'id': str(p['id']), 'title': short_title(p['title']), 'brand': b, 'cat': c, 'price': price,
                  'compare': comp if comp > price else None, 'available': any(x['available'] for x in p['variants']),
                  'tags': tags_of(p, c), 'desc': clean_text(p['body_html'])})

# ---- gallery per product from <handle>.js (media order + alt) ----
handle = {str(p['id']): p['handle'] for p in live}
gal = {}
for q in proto:
    d = json.load(open(os.path.join(W, 'js', handle[q['id']] + '.json')))
    gal[q['id']] = [(m['src'] if m['src'].startswith('http') else 'https:' + m['src'], (m.get('alt') or '').strip()) for m in d['media'] if m['media_type'] == 'image']

def raw_path(url): return os.path.join(RAW, re.sub(r'[^A-Za-z0-9._-]', '_', url.split('/files/')[-1].split('?')[0])[-150:])
def fetch(url):
    out = raw_path(url)
    if os.path.exists(out) and os.path.getsize(out) > 0: return
    for _ in range(4):
        try:
            data = urllib.request.urlopen(url + ('&' if '?' in url else '?') + 'width=1000', timeout=60).read()
            open(out, 'wb').write(data); return
        except Exception as e: err = e
    print('FAIL', url, err)
with ThreadPoolExecutor(16) as ex: list(ex.map(fetch, [u for g in gal.values() for u, _ in g]))

def frame(url, w, h):
    im = Image.open(raw_path(url)).convert('RGBA')
    bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im); im = bg.convert('RGB')
    s = min(w * .86 / im.width, h * .86 / im.height)
    im = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    # same warm ivory grade as the original build (white -> backdrop)
    r, g, b = im.split()
    r = r.point(lambda v: max(0, min(255, v * 0.949 * 1.04 - 5))); g = g.point(lambda v: max(0, min(255, v * 0.929 * 1.04 - 5))); b = b.point(lambda v: max(0, min(255, v * 0.894 * 1.04 - 5)))
    im = Image.merge('RGB', (r, g, b))
    c = Image.new('RGB', (w, h), IVORY); c.paste(im, ((w - im.width) // 2, (h - im.height) // 2)); return c

def sheets(cells, spec, folder, prefix, q):
    w, h, cols, rows = spec; per = cols * rows
    os.makedirs(os.path.join(PROTO, folder), exist_ok=True)
    for f in os.listdir(os.path.join(PROTO, folder)): os.remove(os.path.join(PROTO, folder, f))
    def one(n):
        sh = Image.new('RGB', (w * cols, h * rows), IVORY)
        for k, url in enumerate(cells[n * per:(n + 1) * per]):
            try: sh.paste(frame(url, w, h), ((k % cols) * w, (k // cols) * h))
            except Exception as e: print('BAD', url, e)
        sh.save(os.path.join(PROTO, folder, f'{prefix}{n}.webp'), 'WEBP', quality=q, method=6)
    with ThreadPoolExecutor(os.cpu_count() or 4) as ex: list(ex.map(one, range((len(cells) + per - 1) // per)))
    return (len(cells) + per - 1) // per

# group by category then brand so a listing needs few card sheets
order = {'skincare': 0, 'haircare': 1, 'bath-body': 2, 'fragrance': 3}
proto = [q for q in proto if gal[q['id']]] + [q for q in proto if not gal[q['id']]]
seq = sorted([q for q in proto if gal[q['id']]], key=lambda q: (order.get(q['cat'], 9), q['brand'].lower(), q['title'].lower()))
card_cells, gal_cells = [], []
for q in seq:
    g = gal[q['id']]
    q['frames'] = len(g); q['ci'] = len(card_cells); q['gi'] = len(gal_cells)
    q['alts'] = [a or f"{q['title']} – image {i + 1}" for i, (_, a) in enumerate(g)]
    card_cells += [u for u, _ in g[:2]]
    if len(g) == 1: card_cells.append(g[0][0])  # keep products on even cells
    gal_cells += [u for u, _ in g]
    q.pop('img', None)
for q in proto:
    if not gal[q['id']]: q.update(frames=0); q.pop('img', None)

nc = sheets(card_cells, CARD, 'cards', 'c', 80)
ng = sheets(gal_cells, GAL, 'gallery', 'g', 78)
json.dump(proto, open(os.path.join(PROTO, 'products.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print('products', len(proto), 'new', len(proto) - len(have), 'frames', len(gal_cells), 'card sheets', nc, 'gallery sheets', ng)

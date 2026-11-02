"""Put every product of the client's 2 Nov 2026 sheet live (user: "those 674 and 159 should be in the LIVE as well,
even without inventory"; chose 'All live now, sold out' with a photo placeholder).

Builds (no store writes; the session sends them):
  docs/seo/sheet_live_collections_2026-11-02.json  — collectionCreate inputs for brands without a brand page
  docs/seo/sheet_live_products_2026-11-02.json     — productSet inputs for the 207 products not in Shopify
     (201 perfumes from the merged SEO sheet, grouped into one product per H1 when only the size differs,
      + 6 Vilvah items), status ACTIVE, tracked stock 0, client-sheet prices.
Run: python3 tools/shopify/add_sheet_products.py
"""
import json, re, html, pathlib, collections, unicodedata
import openpyxl
ROOT = pathlib.Path(__file__).resolve().parents[2]
NEW = json.load(open(ROOT / 'docs/seo/fragrance_new_seo_2026-11-02.json'))
ALL = json.load(open(ROOT / 'docs/data/shopify_all_products_2026-11-02.json'))
TAKEN = {p['handle'] for p in ALL}
LOC = 'gid://shopify/Location/111879553411'
COLL = {}  # handle -> id (existing)
for line in open(ROOT / 'docs/seo/existing_collections_2026-11-02.tsv'):
    h, i = line.rstrip('\n').split('\t')
    COLL[h] = i

def handleize(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = s.replace('&', ' ').replace("'", '')
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s)).strip('-')

BRAND_NAME = {'Bois': 'Bois 1920'}
ARABIAN = {'Lattafa', 'Maison Alhambra', 'Afnan', 'Arabiyat Prestige', 'Rasasi', 'Swiss Arabian', 'Attar Collection', 'Armaf', 'Inaaya', 'Adi Guru'}
LINE = {'Guess': 'American fashion fragrances and body mists', 'Franck Olivier': 'French-style perfumes at everyday prices',
        'Maison Alhambra': 'Arabian-inspired eaux de parfum', 'Natural By Woods': 'Woody niche eaux de parfum',
        'Lattafa': 'Arabian perfume house', 'Armaf': 'Club de Nuit and Arabian-inspired perfumes', 'Afnan': 'Arabian perfume house',
        'Arabiyat Prestige': 'Arabian perfume house', 'Rasasi': 'Arabian perfume house', 'Swiss Arabian': 'Arabian perfume house',
        'Attar Collection': 'Arabian-inspired eaux de parfum', 'Inaaya': 'Arabian-inspired eaux de parfum', 'Adi Guru': 'Eaux de parfum',
        'Mercedes-Benz': 'Fragrances for men', 'Jaguar': 'Fragrances for men', 'Fomo': 'Niche extraits de parfum',
        'Unlimited': 'Eaux de parfum', 'Fun & Basics': 'Body mists and fragrances', 'David Beckham': 'Fragrances',
        'Tous': 'Spanish fashion fragrances', 'Vera Wang': 'Fragrances for women', 'Formula 1': 'Fragrances inspired by racing',
        'Armand Basi': 'Spanish fashion fragrances', 'Bois 1920': 'Italian niche perfumes', 'Notebook': 'Fragrances'}
OTHERS = [["anatomē", "/collections/anatome", "London apothecary for sleep and senses", "anatome"],
          ["Tiziana Terenzi", "/collections/tiziana-terenzi", "Italian niche extraits", "tiziana-terenzi"],
          ["Hemel", "/collections/hemel", "Modern luxury eaux de parfum", None],
          ["Fumeri", "/collections/fumeri", "Bold scents, everyday prices", None],
          ["Al Haramain", "/collections/al-haramain", "Arabian perfume house", "al-haramain"]]
GENDER = lambda cat: 'Men' if str(cat).startswith('Men') else 'Women' if str(cat).startswith('Women') else 'Unisex'
FAM = {'woody': 'woody', 'amber': 'amber', 'floral': 'floral', 'fresh': 'fresh', 'aquatic': 'fresh', 'gourmand': 'amber'}

def esc(s): return html.escape(str(s or '').strip(), quote=False)

def price_band(p):
    return 'price-0-15' if p < 15 else 'price-15-25' if p < 25 else 'price-25-50' if p < 50 else 'price-50-9999'

def notes_html(sc):
    if not sc:
        return ''
    parts = [x.strip() for x in str(sc).split('|') if x.strip()]
    li = ''.join(f'<li>{esc(p)}</li>' for p in parts)
    return f'<h3>Scent notes</h3><ul>{li}</ul>'

# ---------------------------------------------------------------- perfumes: group rows that differ only by size
groups = collections.OrderedDict()
for r in NEW:
    r['brand'] = BRAND_NAME.get(r['brand'], r['brand'])
    groups.setdefault(r['h1'], []).append(r)

brand_count = collections.Counter()
products = []
rank = 600
for h1, rows in groups.items():
    r0 = rows[0]
    brand = r0['brand']
    g = GENDER(r0['cat'])
    fam = FAM.get(str(r0['family'] or '').lower())
    gift = 'Gift Set' in str(r0['cat']) or ' set' in h1.lower()
    deo = 'Deodorant' in str(r0['cat']) or 'Deodorant' in str(r0['type'])
    multi = len(rows) > 1
    title = h1 if multi else f"{h1} {r0['size']}".strip()
    handle = handleize(title)
    if handle in TAKEN:
        handle += '-swansura'
    TAKEN.add(handle)
    prices = [float(x['price']) for x in rows]
    pmin = min(prices)
    desc = (f"<p>{esc(r0['client_desc'])}</p>" if r0['client_desc'] else '') + notes_html(r0['scent']) + \
        '<h3>Details</h3><ul>' + \
        f"<li>{esc(str(r0['type']).replace(' (EDP)', '').replace(' (EDT)', ''))}" + \
        (f", {esc(', '.join(x['size'] for x in rows))}" if any(x['size'] for x in rows) else '') + '</li>' + \
        f"<li>{'Made for men' if g == 'Men' else 'Made for women' if g == 'Women' else 'Unisex: for men and women'}</li>" + \
        f"<li>Brand: {esc(brand)}</li><li>100% authentic, dispatched from the UK</li></ul>"
    sizes_opt = [x['size'] or 'One size' for x in rows]
    variants = []
    for x, sz in zip(rows, sizes_opt):
        variants.append({'optionValues': [{'optionName': 'Size' if multi else 'Title', 'name': sz if multi else 'Default Title'}],
                         'price': f"{float(x['price']):.2f}", 'inventoryItem': {'tracked': True},
                         'inventoryQuantities': [{'locationId': LOC, 'name': 'available', 'quantity': 0}]})
    options = [{'name': 'Size', 'values': [{'name': s} for s in sizes_opt]}] if multi else [{'name': 'Title', 'values': [{'name': 'Default Title'}]}]
    colls = ['fragrance', handleize(brand), price_band(pmin)]
    if not deo:                                          # deodorants: brand + Deodorants only, not the perfume lists
        colls.append({'Men': 'perfume-for-men', 'Women': 'perfume-for-women', 'Unisex': 'unisex-perfume'}[g])
    if fam:
        colls.append('scent-' + fam)
    if re.search(r'\boud\b', h1, re.I):
        colls += ['oud-perfume', 'scent-oud']
    if brand in ARABIAN:
        colls.append('arabian-perfume')
    if gift:
        colls += ['perfume-gift-sets', 'sets-combos', 'christmas-gifts', {'Men': 'gifts-for-him', 'Women': 'gifts-for-her'}.get(g, 'gifts-for-her')]
        colls.append('gifts-under-25' if pmin < 25 else 'gifts-25-to-50' if pmin < 50 else 'gifts-over-50')
    if deo:
        colls.append('deodrants')
    if any(re.match(r'^\s*(\d+(\.\d+)?)\s*ml', x['size'] or '') and float(re.match(r'^\s*(\d+(\.\d+)?)', x['size']).group(1)) <= 15 for x in rows):
        colls.append('travel-size-minis')
    colls = list(dict.fromkeys(colls))
    type_word = {'Body Mist': 'Body Mist', 'Deodorant Spray': 'Deodorant'}.get(str(r0['type']), 'Eau de Parfum' if 'EDP' in str(r0['type']) else 'Eau de Toilette' if 'EDT' in str(r0['type']) else str(r0['type']).replace('Fragrance (type not specified)', 'Fragrance'))
    chips = ([fam.capitalize() + ' family'] if fam else []) + [{'Men': 'For men', 'Women': 'For women'}.get(g, 'Unisex'), type_word]
    notes = [x.strip() for x in str(r0['scent'] or '').split('|') if x.strip()]
    top = re.sub(r'^Top Notes:\s*', '', notes[0]) if notes else ''
    sw = {'t': {'Men': 'For him', 'Women': 'For her'}.get(g, 'Unisex'), 's': [], 'c': [], 'k': False, 'r': rank, 'f': fam, 'w': g, 'n': None,
          'a': [f"{'An' if (fam or 's')[0] in 'aeiou' else 'A'} {fam or 'signature'} fragrance{': ' + top if top else ''}."]}
    pdp = {'cat': 'fragrance', 'ben': '', 'more': False, 'chips': chips, 'how': [],
           'pair': ['deyga-chocolate-body-butter-100g', 'somali-frankincense-sleep-pillow-spray-overactive-mind-anatome'], 'sim': [],
           'kw': [[{'Men': 'Perfume for men', 'Women': 'Perfume for women'}.get(g, 'Unisex perfume'),
                   '/collections/' + {'Men': 'perfume-for-men', 'Women': 'perfume-for-women'}.get(g, 'unisex-perfume')]] +
                 ([['Perfume gift sets', '/collections/perfume-gift-sets']] if gift else [])}
    rank += 1
    brand_count[brand] += 1
    mf = lambda k, t, v: {'namespace': 'custom', 'key': k, 'type': t, 'value': v}
    products.append(dict(kind='perfume', rows=[x['id'] for x in rows], brand=brand, handle=handle, colls=colls, input={
        'title': title, 'handle': handle, 'status': 'ACTIVE', 'vendor': brand, 'productType': 'Fragrance',
        'tags': ['Fragrance', 'New 2026-11', 'Photo pending'] + (['Gift set'] if gift else []),
        'descriptionHtml': desc, 'seo': {'title': r0['title'], 'description': r0['desc']},
        'productOptions': options, 'variants': variants,
        'metafields': [mf('h1', 'single_line_text_field', h1), mf('sw', 'json', json.dumps(sw, ensure_ascii=False)),
                       mf('pdp', 'json', json.dumps(pdp, ensure_ascii=False))]}))
# similar products: up to 4 others of the same brand
by_brand = collections.defaultdict(list)
for p in products:
    by_brand[p['brand']].append(p['handle'])
for p in products:
    sim = [h for h in by_brand[p['brand']] if h != p['handle']][:4]
    for m in p['input']['metafields']:
        if m['key'] == 'pdp':
            d = json.loads(m['value']); d['sim'] = sim; m['value'] = json.dumps(d, ensure_ascii=False)

# ---------------------------------------------------------------- 6 Vilvah items not in Shopify
INCI = {}
try:
    for c in json.load(open(ROOT / 'docs/data/vilvah_inci_site_2026-10-30.json')).get('components', []):
        INCI[c.get('n', '').lower()] = c
except Exception:
    pass
VILVAH = [
    ('Vilvah Rose Milk Lip Balm 10g', 9.99, 'lip', 'A rose and milk lip balm from Vilvah for everyday lip care. Smooth a little over the lips as often as you like.'),
    ('Vilvah Filter Kaapi Lip Balm 10g', 9.99, 'lip', 'A coffee-scented lip balm from Vilvah, inspired by South Indian filter coffee. Smooth a little over the lips as often as you like.'),
    ('Vilvah Mango Shake Lip Balm 10g', 9.99, 'lip', 'A mango-scented lip balm from Vilvah (also part of the Vilvah Tinted Lip Balm Kit). Smooth a little over the lips as often as you like.'),
    ('Vilvah Cream Bun Lip Balm 10g', 9.99, 'lip', 'A cream-bun-scented lip balm from Vilvah (also part of the Vilvah Tinted Lip Balm Kit). Smooth a little over the lips as often as you like.'),
    ('Vilvah Budget Skincare Combo', 21.99, 'set', 'A Vilvah skincare combo chosen for everyday care. Message us on WhatsApp or Instagram for the items in this set.'),
    ('Vilvah x Annapoorna Gift Box', 20.99, 'set', 'A Vilvah gift box made with Annapoorna. Message us on WhatsApp or Instagram for the items in this box.'),
]
for title, price, kind, text in VILVAH:
    handle = handleize(title)
    if handle in TAKEN:
        handle += '-swansura'
    TAKEN.add(handle)
    lip = kind == 'lip'
    colls = ['vilvah', 'skincare', 'natural-skincare', price_band(price)] + (['lip-balm', 'concern-lips', 'lip-balm-for-dry-lips', 'vilvah-solo-products', 'stocking-fillers'] if lip else ['giftsets', 'sets-combos', 'skincare-tools-kits', 'gifts-under-25', 'christmas-gifts', 'gifts-for-her'])
    seo_t = f'{title} | Swansura UK'
    seo_d = f'Buy {title} for £{price:.2f} at Swansura UK. Official UK partner of Vilvah: 100% authentic, shipped from the UK, free delivery over £40.'
    assert len(seo_t) <= 60 and len(seo_d) <= 160, (seo_t, len(seo_d))
    desc = f'<p>{esc(text)}</p><h3>Details</h3><ul><li>Brand: Vilvah (official UK partner)</li><li>100% authentic, dispatched from the UK</li></ul>'
    sw = {'t': 'Lip care' if lip else 'Kits & routines', 's': [], 'c': ['lips'] if lip else [], 'k': False, 'r': rank, 'g': [],
          'a': ['A lip balm from Vilvah.' if lip else 'A Vilvah set.']}
    pdp = {'cat': 'skincare', 'ben': '', 'more': False, 'chips': ['Lip care', 'Natural formula'] if lip else ['Gift set', 'Natural formula'], 'how': [],
           'pair': [], 'sim': [], 'kw': [['Lip balm for dry lips', '/collections/lip-balm-for-dry-lips']] if lip else [['Vilvah sets', '/collections/giftsets']]}
    rank += 1
    mf = lambda k, t, v: {'namespace': 'custom', 'key': k, 'type': t, 'value': v}
    products.append(dict(kind='vilvah', rows=[title], brand='Vilvah', handle=handle, colls=list(dict.fromkeys(colls)), input={
        'title': title, 'handle': handle, 'status': 'ACTIVE', 'vendor': 'Vilvah', 'productType': 'Lip care' if lip else 'Gift set',
        'tags': ['Skincare', 'vilvah', 'New 2026-11', 'Photo pending'] + (['Sets & Combos'] if not lip else []),
        'descriptionHtml': desc, 'seo': {'title': seo_t, 'description': seo_d},
        'productOptions': [{'name': 'Title', 'values': [{'name': 'Default Title'}]}],
        'variants': [{'optionValues': [{'optionName': 'Title', 'name': 'Default Title'}], 'price': f'{price:.2f}', 'inventoryItem': {'tracked': True},
                      'inventoryQuantities': [{'locationId': LOC, 'name': 'available', 'quantity': 0}]}],
        'metafields': [mf('h1', 'single_line_text_field', title.replace(' 10g', '')), mf('sw', 'json', json.dumps(sw)), mf('pdp', 'json', json.dumps(pdp))]}))

# ---------------------------------------------------------------- brand collections that don't exist yet
newcolls = []
for brand, n in sorted(brand_count.items()):
    h = handleize(brand)
    if h in COLL and h != 'david-beckham':
        continue
    seo_t = f'{brand} Perfume | Shop at Swansura UK'
    seo_d = f'Shop {brand} perfume at Swansura: {n} product{"s" if n > 1 else ""}, 100% authentic and shipped from the UK. Free UK delivery over £40.'
    bj = {'name': brand, 'world': 'scent', 'partner': False, 'line': LINE.get(brand, 'Fragrances'),
          'story': f'{brand} at Swansura: {n} product{"s" if n > 1 else ""}, 100% authentic and shipped from the UK.', 'count': n, 'others': OTHERS}
    faq = [[f'Is {brand} at Swansura genuine?', f'Yes. Every {brand} product at Swansura is 100% authentic and ships from the UK.'],
           [f'How fast is {brand} delivery?', f'All {brand} orders ship from Swansura in the UK. UK delivery is free on orders over £40, and orders over £70 also get £5 off.']]
    mf = lambda k, t, v: {'namespace': 'custom', 'key': k, 'type': t, 'value': v}
    newcolls.append(dict(handle=h, existing=COLL.get(h), input={'title': brand, 'handle': h, 'sortOrder': 'MANUAL',
                     'seo': {'title': seo_t, 'description': seo_d},
                     'metafields': [mf('h1', 'single_line_text_field', f'{brand} Perfume'), mf('brand', 'json', json.dumps(bj, ensure_ascii=False)),
                                    mf('faq', 'json', json.dumps(faq, ensure_ascii=False))]}))
json.dump(newcolls, open(ROOT / 'docs/seo/sheet_live_collections_2026-11-02.json', 'w'), ensure_ascii=False, indent=1)
json.dump(products, open(ROOT / 'docs/seo/sheet_live_products_2026-11-02.json', 'w'), ensure_ascii=False, indent=1)
missing = sorted({c for p in products for c in p['colls'] if c not in COLL and c not in {x['handle'] for x in newcolls}})
print(len(products), 'products;', len(newcolls), 'brand collections;', 'unknown collection handles:', missing)

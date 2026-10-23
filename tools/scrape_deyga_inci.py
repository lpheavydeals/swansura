"""Full ingredient lists for the store's Deyga products, scraped from the brand's official site (deyga.in).

Source on each deyga.in product page: the 'Full Ingredients List' drawer (div.ingredients-drawer-body);
if that is empty, the 'Ingredients' section of the product description (products.json body_html).
Kits/combos get one list per product in the box (contents from deyga.in 'In the box' and our kit photos).

Usage: python3 tools/scrape_deyga_inci.py <workdir>
  Caches deyga.in products.json pages and product HTML in <workdir>.
Writes docs/data/deyga_inci_<date>.json (for theme metafields) and the `inci` field in prototype/products.json
(same shape as the Vilvah lists: [{n: product name, l: [[ingredient, 0], ...], g: {}}]).
"""
import html, json, os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = sys.argv[1]; os.makedirs(os.path.join(W, 'pages'), exist_ok=True)
DATE = '2026-10-23'

# store product id -> deyga.in handles (one per product in the box). Loofah has no ingredients.
MAP = {
    '15981319324035': ['mint-lip-scrub', 'beetroot-lip-balm'],                       # Soft Lip Combo
    '15981318832515': ['vitamin-c-foaming-facewash', 'vitamin-c-serum'],             # Vitamin C Daily Glow Combo
    '15981315031427': ['spirulina-matcha', 'tea-tree-facial-toner-100ml'],           # Acne Relief Combo
    '15981314539907': ['charcoal-bath-bar', 'tea-tree-facial-toner-100ml', 'aloe-vera-gel'],  # Acne Vanishing Combo
    '15981313753475': ['foot-soak', 'foot-scrub-100gm', 'foot-butter'],             # Mini Foot Spa Combo (3 jars in our photo)
    '15981312016771': ['chocolate-skin-nourished-100g'],
    '15981311623555': ['charcoal-detox-face-mask'],
    '15981310148995': ['charcoal-body-wash'],
    '15981305102723': ['body-scrub-100g'],
    '15981304611203': ['deep-moisturizing-face-cream'],
    '15981304152451': ['2-hyaluronic-serum-intense-hydration'],
    '15981299302787': ['orange-almond-face-pack-100g'],
    '15979363565955': ['pre-mature-greying-oil'],
    '15979358945667': ['rose-geranium-body-butter'],
    '15979354620291': ['rose-glow-serum-30ml'],
    '15979353276803': ['loose-setting-powder'],
    '15979352752515': ['light-moisturising-face-cream'],
    '15979351736707': ['foot-soak'],
    '15979334107523': ['vitamin-c-foaming-facewash'],
    '15979331191171': ['wild-berry-body-wash'],
    '15979325948291': ['neem-seed-oil-30ml'],
    '15979324113283': ['under-eye-mask'],
    '15979322442115': ['spirulina-matcha'],
    '15979320476035': ['tea-tree-facial-toner-100ml'],
    '15979313332611': ['cleansing-balm'],
    '15979080745347': ['foot-scrub-100gm'],
    '15979073765763': ['eyebrow-growth-oil-30ml'],
    '15979063378307': ['sunscreen-spf-50'],      # SPF 30 and SPF 50 lists are identical on deyga.in
    '15979054039427': ['skin-care-vanilla-lip-balm'],  # our listing is 8 g, deyga.in sells 10 g
    '15979046961539': ['spinach-cucumber-bath-bar'],
    '15979042439555': ['saffron-sheabutter-bath-bar'],
    '15979040539011': ['rose-pink-clay-bath-bar'],
    '15979031593347': ['neem-and-turmeric-bath-bar'],
    '15979028414851': ['mint-lip-scrub'],
    '15556043243907': ['aloe-vera-gel', 'beetroot-lip-balm'],                       # Daily Essential Kit
    '15556029251971': ['charcoal-bath-bar', 'aloe-vera-gel'],                       # Clear Skin Kit
    '15556025123203': ['charcoal-face-wash', 'beetroot-lip-balm'],                  # Best Selling Face Care Kit
    '15556017422723': ['hair-removal-powder', 'aloe-vera-gel'],                     # Instant Hair Removal Kit
    '15556010672515': ['hair-removal-powder', 'rose-water-toner-100ml', 'aloe-vera-gel'],  # ... with Toner (rose toner in photo)
    '15556006248835': ['rose-mulethi-skin-lightener-100g', 'rose-water-toner-100ml'],  # Healthy Glow Kit
    '15556004905347': ['aloe-vera-gel', 'hair-growth-oil'],                         # Hair Nourishment Kit
    '15556003299715': ['oat-milk-face-wash', 'aloe-vera-gel'],                      # Sensitive Skin Kit
    '15555987046787': ['hair-removal-powder'],
    '15555982721411': ['oat-milk-face-wash'],
    '15555979608451': ['almond-milk-body-lotion-100ml'],
    '15555970924931': ['rose-water-toner-100ml'],
    '15428515463555': ['strawberry-lip-scrub', 'beetroot-lip-balm'],                # Nourished Lip Care Kit
    '15428515529091': ['rice-water-shampoo', 'soy-milk-conditioner', 'hair-growth-oil'],  # Hair Care Kit
    '15428515561859': ['aloe-vera-gel', 'under-eye-cream-day-night'],               # Hydro Boosting Kit
    '15428515594627': ['aloe-vera-gel', 'beetroot-lip-balm', 'charcoal-bath-bar'],  # ABC Kit
    '15415430971779': ['charcoal-face-wash', 'aloe-vera-gel'],                      # Game Changer Kit
    '15415432544643': ['exfoliator', 'charcoal-bath-bar'],                          # De-Tan & Pigmentation Kit
    '15415435985283': ['rose-mulethi-skin-lightener-100g'],
    '15415432151427': ['charcoal-face-wash'],
    '15415430381955': ['strawberry-lip-scrub'],
    '15415435428227': ['aloe-vera-gel', 'beetroot-lip-balm'],                       # Double Hydration Kit
    '15415433855363': ['strawberry-lip-scrub', 'beetroot-lip-balm-stick'],          # Nourished Lips Stick Kit
    '15415430283651': ['beetroot-lip-balm'],
    '15415434477955': ['beetroot-lip-balm-stick'],
    '15415430021507': ['rice-water-shampoo', 'soy-milk-conditioner'],               # Daily Use Healthy Hair Kit
    '15415433036163': ['exfoliator'],
    '15415432511875': ['charcoal-bath-bar'],
    '15415430742403': ['foot-butter'],
    '15415430906243': ['under-eye-cream-day-night'],
    '15415431659907': ['aloe-vera-gel'],
    '15415431168387': ['deyga-100-plant-based-hair-color-black'],
    '15415430513027': ['anti-dandruff-shampoo-220ml'],
    '15415430939011': ['soy-milk-conditioner'],
    '15415432249731': ['hair-growth-oil'],
    '15415431725443': ['vitamin-c-serum'],
    '15415432774019': ['beautifying-serum-30ml'],
    '15415431135619': ['rice-water-shampoo'],
    '15979309138307': [],                                                            # Organic Loofah (no ingredients)
}

def get(url, path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        open(path, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read())
    return open(path, encoding='utf-8').read()

shop = {}
for n in range(1, 5):
    for p in json.loads(get(f'https://deyga.in/products.json?limit=250&page={n}', os.path.join(W, f'p{n}.json')))['products']:
        shop[p['handle']] = p
handles = sorted({h for hs in MAP.values() for h in hs})
with ThreadPoolExecutor(8) as ex:
    pages = dict(zip(handles, ex.map(lambda h: get(f'https://deyga.in/products/{h}', os.path.join(W, 'pages', h + '.html')), handles)))

def clean(s):
    s = html.unescape(re.sub(r'<[^>]+>', '', s)).replace('\xa0', ' ').replace('[', '(').replace(']', ')')
    s = re.sub(r'\(\s+', '(', re.sub(r'\s+\)', ')', re.sub(r'\s+', ' ', s))).strip(' ,')
    return s + ')' * (s.count('(') - s.count(')'))  # deyga.in drops some closing brackets

# typos on deyga.in (10% Vitamin C Serum list): merged lines, 'land)' for '(and)', a sign-off
SPLIT = [r'(?<=Fr\.Pf\.) (?=Citrus aurantium)', r'(?<=Fr\.Pr\.) (?=Fragrance)', r'(?<=\(Amisoft ECS 22\)) (?=Propandiol)']
FIX = [(r'\s+and LOVE\.?$', ''), (r'glutamate land\) water', 'glutamate (and) water')]

def scrape(h):
    m = re.search(r'(?s)<div class="ingredients-drawer-body">(.*?)</div>\s*</div>\s*</div>', pages[h])
    items = [clean(x) for x in re.findall(r'(?s)<li[^>]*>(.*?)</li>', m.group(1))] if m else []
    if not items and m and clean(m.group(1)):
        items = [clean(x) for x in re.split(r'<br\s*/?>|</p>|\n', m.group(1))]
    if not items:  # description fallback: text after the 'Ingredients' heading
        t = re.split(r'(?i)<h\d>\s*(?:<[^>]+>)*\s*ingredients\s*(?:<[^>]+>)*\s*</h\d>', shop[h]['body_html'] or '')
        if len(t) > 1:
            items = [clean(x) for x in re.split(r',(?![^()]*\))', re.split(r'(?i)<h\d', t[1])[0])]
    out = []
    for x in filter(None, items):  # 'Aqua, Rosmarinus …' arrives as one item on one page
        for a, b in FIX: x = re.sub(a, b, x)
        parts = [y.strip() for y in re.split(r',\s*(?![^()]*\))', x)] if x.lower().startswith('aqua,') else [x]
        for r in SPLIT: parts = [z for y in parts for z in re.split(r, y)]
        out += parts
    return [x for x in out if x]

def name(h):
    t = re.sub(r'(?i)\s*(mini\s*)?\d+(\.\d+)?\s*(ml|g|gm|gms)\b', '', shop[h]['title']).strip(' -–')
    return {'chocolate-skin-nourished-100g': 'Chocolate Body Butter', 'spirulina-matcha': 'Spirulina & Matcha Face Pack',
            'exfoliator': 'Face & Body Exfoliator', 'deyga-100-plant-based-hair-color-black': '100% Plant Based Hair Color (Black)'}.get(h, t)

lists, missing = {}, []
for h in handles:
    l = scrape(h)
    if not l: missing.append(h)
    if h == 'deyga-100-plant-based-hair-color-black':  # two-step dye: henna mix, then indigo mix
        parts, cur = [], None
        for x in l:
            if re.match(r'(?i)application \d', x): cur = {'n': '', 'l': []}; parts.append(cur)
            elif cur is not None and not cur['n']: cur['n'] = 'Step ' + str(len(parts)) + ': ' + re.sub(r'(?i)plant based hair colou?r\s*', '', x).strip('() ') + ' mix'
            elif cur is not None: cur['l'].append([x, 0])
        lists[h] = parts
    else:
        lists[h] = [{'n': name(h), 'l': [[x, 0] for x in l], 'g': {}}] if l else []

P = json.load(open(os.path.join(ROOT, 'prototype', 'products.json')))
byid = {p['id']: p for p in P}
out, n = {}, 0
for pid, hs in MAP.items():
    p = byid[pid]; inci = [c for h in hs for c in lists[h]]
    for c in inci: c.setdefault('g', {})
    if inci:
        p['inci'] = inci; n += 1
        out[pid] = {'title': p['title'], 'source': [f'https://deyga.in/products/{h}' for h in hs], 'inci': inci}
    else:
        p.pop('inci', None)
json.dump(out, open(os.path.join(ROOT, 'docs', 'data', f'deyga_inci_{DATE}.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(P, open(os.path.join(ROOT, 'prototype', 'products.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
deyga = [p for p in P if p['brand'] == 'Deyga']
print('Deyga products', len(deyga), 'mapped', len(MAP), 'with full list', n, '| deyga.in pages without a list:', missing,
      '| unmapped:', [p['title'] for p in deyga if p['id'] not in MAP])

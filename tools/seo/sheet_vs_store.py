"""Check every row of the client's 2 Nov 2026 sheet (674 fragrance + 159 Vilvah & Deyga) against all Shopify products.

Input : docs/data/Swansura_Fragrance_Data_2026-11-02.xlsx, docs/data/shopify_all_products_2026-11-02.json (admin export:
        id, title, handle, vendor, status, totalInventory, variant titles; 719 products).
Output: docs/seo/sheet_vs_store_2026-11-02.json  — per row: best Shopify product, status, size match, score.
"""
import json, re, pathlib, difflib, collections, sys
import openpyxl
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/seo'))
from merge_fragrance_sheet import toks, bnorm

P = json.load(open(ROOT / 'docs/data/shopify_all_products_2026-11-02.json'))
wb = openpyxl.load_workbook(ROOT / 'docs/data/Swansura_Fragrance_Data_2026-11-02.xlsx', data_only=True)
F = [r for r in wb['Fragrance Catalogue'].iter_rows(min_row=2, values_only=True) if r[6]]
V = [r for r in wb['Vilvah & Deyga'].iter_rows(min_row=2, values_only=True) if r[5]]

def sizes(s):
    s = str(s or '').lower()
    return set(re.findall(r'(\d+(?:\.\d+)?)\s*(?:ml|g|gm|gms)(?![a-z])', s)) | set(re.findall(r'(\d+(?:\.\d+)?)\s*(?:ml|g)(?=[a-z])', s))
VB = {'giorgia armani': 'giorgio armani', 'armaf club de nuit': 'armaf', 'swansura - the body studio': 'swansura selection'}
def brand(b): return bnorm(VB.get(str(b or '').lower().strip(), b))

def score(a, b):
    sa, sb = set(a), set(b)
    if not sa or not sb:
        return 0
    inter = len(sa & sb)
    return max(inter / len(sa | sb), inter / len(sa) * 0.9 if len(sa) <= len(sb) else 0,
               difflib.SequenceMatcher(None, ' '.join(a), ' '.join(b)).ratio() * 0.9)

store = []
for p in P:
    vt = [v['title'] for v in p['variants']['nodes']]
    store.append(dict(p=p, b=brand(p['vendor']), t=toks(p['title'], p['vendor']),
                      sz=sizes(p['title']) | set().union(*[sizes(x) for x in vt]) | {re.sub(r'[^0-9.]', '', x) for x in vt if re.fullmatch(r'\s*\d+(\.\d+)?\s*(ml|g)?\s*', x.lower())}))

def best(name, br, size, vd=False):
    b = brand(br); t = toks(name, br); s = sizes(size) or sizes(name)
    cands = []
    for c in store:
        if vd:
            if c['b'] not in (b, bnorm(br)):
                continue
        elif not (b and c['b'] and (b in c['b'] or c['b'] in b)):
            continue
        sc = score(t, c['t'])
        if sc >= 0.5:
            cands.append((sc + (0.15 if s and s & c['sz'] else 0), sc, bool(s & c['sz']) if s else None, c))
    if not cands or max(x[1] for x in cands) < 0.75:      # brand column wrong in the client sheet (e.g. Boucheron under 'antonio')
        t2 = toks(name, '')
        for c in store:
            sc = score(t2, toks(c['p']['title'], ''))
            if sc >= 0.75:
                cands.append((sc + (0.15 if s and s & c['sz'] else 0), sc, bool(s & c['sz']) if s else None, c))
    cands.sort(key=lambda x: (-x[0], {'ACTIVE': 0, 'DRAFT': 1}.get(x[3]['p']['status'], 2)))
    good = [x for x in cands if x[1] >= 0.75 and x[2] is not False]
    act = [x for x in good if x[3]['p']['status'] == 'ACTIVE']
    if act and good and good[0][3]['p']['status'] != 'ACTIVE':      # a live listing of the same perfume beats a hidden copy
        cands.remove(act[0]); cands.insert(0, act[0])
    return cands

out = []
for kind, rows in (('Fragrance', F), ('Vilvah & Deyga', V)):
    for i, r in enumerate(rows, 1):
        if kind == 'Fragrance':
            name, br, size, price = r[6], r[1], r[9], r[11]
        else:
            name, br, size, price = r[5], r[1], r[6], r[8]
        c = best(name, br, size, vd=kind != 'Fragrance')
        top = c[0] if c else None
        if top and top[1] >= 0.75 and top[2] is not False:
            st = top[3]['p']['status']
        elif top and top[1] >= 0.75:
            st = 'OTHER SIZE (' + top[3]['p']['status'] + ')'
        elif top:
            st = 'CHECK'
        else:
            st = 'NOT IN SHOPIFY'
        out.append(dict(kind=kind, row=i, brand=br, name=name, size=size, price=price, status=st,
                        score=round(top[1], 2) if top else 0, size_ok=top[2] if top else None,
                        shopify=dict(id=top[3]['p']['id'], title=top[3]['p']['title'], handle=top[3]['p']['handle'],
                                     status=top[3]['p']['status'], stock=top[3]['p']['totalInventory'],
                                     variants=[v['title'] for v in top[3]['p']['variants']['nodes']]) if top else None))
HAND = {  # (kind, name start) -> (status, live product title or note)
    ('Fragrance', 'Game Of Spades Opal'): ('ACTIVE', 'Game of Spades Opal Unisex Eau de Parfum 100ml'),
    ('Fragrance', 'Dolce & Gabbana Women'): ('ACTIVE', 'Dolce & Gabbana Women’s Miniature Fragrance Set'),
    ('Fragrance', 'Jimmy Choo Women’s Miniature'): ('ACTIVE', 'Jimmy Choo Women’s Miniature Fragrance Gift Set 5x4.5ml'),
    ('Fragrance', 'Marc Jacobs Perfect Eau de Toilette 10ml'): ('ACTIVE', 'Marc Jacobs Perfect Eau de Toilette 10ml Miniature (client size column says 75ml)'),
    ('Fragrance', 'Marc Jacobs Women’s Miniature'): ('ACTIVE', 'Marc Jacobs Women’s Miniature Fragrance Gift Set 2025'),
    ('Fragrance', 'Al Haramain Amber Oud Ruby Edition Eau de Parfum –'): ('SIZE MISSING', 'live product has 100/120/200ml; 60ml size not in Shopify'),
    ('Fragrance', 'Al Haramain Amber Oud Ruby Edition Eau de Parfum (EDP)'): ('ACTIVE', 'Al Haramain Amber Oud Ruby Edition (100/120/200ml options)'),
    ('Fragrance', 'Game Of Spades Bid For Men'): ('ACTIVE', 'Game of Spades Bid Eau de Parfum 100ml for Men (published 31 Oct)'),
    ('Fragrance', 'Game Of Spades Boston'): ('ACTIVE', 'Game of Spades Boston Eau de Parfum 100ml for Men (published 31 Oct)'),
    ('Fragrance', 'Game of Spades Diamond'): ('ACTIVE', 'Game of Spades Diamond Unisex Eau de Parfum 100ml (published 31 Oct)'),
    ('Fragrance', 'Game Of Spades Jackpot'): ('ACTIVE', 'Game of Spades Jackpot Unisex Eau de Parfum 100ml (published 31 Oct)'),
    ('Fragrance', 'Game Of Spades King'): ('ACTIVE', 'Game of Spades King Unisex Eau de Parfum 100ml (published 31 Oct)'),
    ('Fragrance', 'Game Of Spades Moon'): ('ACTIVE', 'Game Of Spades Moon Unisex Eau De Parfum 100ml'),
    ('Fragrance', 'Game Of Spades Blind-Bid'): ('ACTIVE', 'Jo Milano Unisex Blind Bid P 100 ml'),
    ('Fragrance', 'Game of Spades Rouge Unisex'): ('ACTIVE', 'Game of Spades Rouge Unisex Eau de Parfum 100ml'),
    ('Fragrance', 'Giorgio Armani Code EDT 125ml Refillable'): ('ACTIVE', 'Giorgio Armani Code Eau de Toilette 125ml Refillable'),
    ('Fragrance', 'Dolce & Gabbana Men'): ('ACTIVE', 'Dolce & Gabbana Men’s Miniature Fragrance Set'),
    ('Vilvah & Deyga', 'Skin finish Sunscreen'): ('ACTIVE', 'Vilvah Skin Finish Sunscreen SPF 50 PA+++'),
    ('Vilvah & Deyga', 'Milk Lip Balm SPF 30'): ('ACTIVE', 'Vilvah Milk Lip Balm SPF 30 PA+++'),
    ('Vilvah & Deyga', 'Milk Drops Brightening Serum'): ('ACTIVE', 'Vilvah Milk Drops Hydrating Serum (20 ml + 40 ml options)'),
    ('Vilvah & Deyga', 'Vilvah Store Frizz Free'): ('ACTIVE', 'Vilvah Frizz Free Hair Kit'),
    ('Vilvah & Deyga', 'Classic Rose Goatmilk'): ('ACTIVE', 'Classic Rose Goat Milk Soap Bar 125G (client sheet says 115 g)'),
    ('Vilvah & Deyga', 'Lip Balm - Grapefruit'): ('ACTIVE', 'Vilvah Grape Fruit Lip Balm 10g'),
    ('Vilvah & Deyga', "Men's Comb"): ('ACTIVE', "Vilvah Men's Neem Wood Comb"),
    ('Vilvah & Deyga', 'Under Eye Cream (Dark Circles'): ('ACTIVE', 'Vilvah Natural Under Eye Cream 20 ml'),
    ('Vilvah & Deyga', 'Rose Milk Lip Balm'): ('NOT IN SHOPIFY', ''),
    ('Vilvah & Deyga', 'Filter Kaapi Lip Balm'): ('NOT IN SHOPIFY', ''),
    ('Vilvah & Deyga', 'Mango Shake Lip Balm'): ('NOT IN SHOPIFY', 'only inside the Tinted Lip Balm Kit'),
    ('Vilvah & Deyga', 'Cream Bun Lip Balm'): ('NOT IN SHOPIFY', 'only inside the Tinted Lip Balm Kit'),
}
for o in out:
    for (k, start), (st, note) in HAND.items():
        if o['kind'] == k and str(o['name']).startswith(start):
            o['status'] = st; o['hand'] = note
            if st == 'NOT IN SHOPIFY':
                o['shopify'] = None
json.dump(out, open(ROOT / 'docs/seo/sheet_vs_store_2026-11-02.json', 'w'), ensure_ascii=False, indent=1)
for k in ('Fragrance', 'Vilvah & Deyga'):
    print(k, collections.Counter(o['status'] for o in out if o['kind'] == k))

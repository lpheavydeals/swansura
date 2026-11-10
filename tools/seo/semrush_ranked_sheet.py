"""Products ranked by Semrush UK search volume, one tab per group.

Usage: python3 tools/seo/semrush_ranked_sheet.py <live_products_dir>
  <live_products_dir> holds Admin product pages p*.json ({data:{products:{nodes:[...]}}})
  with title, vendor, handle, variants{price}; used for the 8 Nov fragrances and
  the 'Others' tab (products never checked in Semrush).
Source of volumes: seo/Swansura_Product_SEO_Merged_2026-11-02.xlsx 'Final SEO (merged)'
(546 products researched 18 Oct + 201 new perfumes checked 2 Nov).
Output: docs/seo/Swansura_Products_by_Search_Volume_2026-11-10.xlsx
"""
import sys, glob, json, re, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

SRC = 'seo/Swansura_Product_SEO_Merged_2026-11-02.xlsx'
OUT = 'docs/seo/Swansura_Products_by_Search_Volume_FINAL_2026-11-10.xlsx'
REMOVED = {'La Maison'}  # brand deleted from the store 6 Nov 2026
NOV8 = set(json.load(open('docs/seo/sheet_nov8_products_2026-11-08.json')) and
           [p['brand'] for p in json.load(open('docs/seo/sheet_nov8_products_2026-11-08.json'))])

ws = openpyxl.load_workbook(SRC, read_only=True)['Final SEO (merged)']
rows = list(ws.iter_rows(values_only=True))
H = rows[0]; ix = {h: i for i, h in enumerate(H)}
def g(r, k): return r[ix[k]]

tabs = {'Deyga': [], 'Vilvah': [], 'Fragrances': [], 'Others': []}
for r in rows[1:]:
    brand = g(r, 'Brand') or ''
    if brand in REMOVED: continue
    tab = brand if brand in ('Deyga', 'Vilvah') else 'Fragrances'
    kw = g(r, 'Primary keyword') or ''
    bw = re.sub(r'[^a-z]', '', brand.lower())[:5]
    ktype = 'Product / brand name' if bw and bw in re.sub(r'[^a-z]', '', kw.lower()) else 'General search term (shared with a collection page)'
    tabs[tab].append(dict(brand=brand, product=g(r, 'FINAL H1') or g(r, 'Product name (sheet)'), size=g(r, 'Size'),
        price=g(r, 'Price (£)'), kw=kw, vol=g(r, 'Primary vol.') or 0, kd=g(r, 'Primary KD'), ease=g(r, 'Ease'),
        kw2=g(r, 'Secondary keyword'), vol2=g(r, 'Secondary vol.') or 0, ktype=ktype, checked=True, added='Before 8 Nov'))

# 8 Nov fragrances: Semrush checked 10 Nov 2026 (screenshots)
NOVKW = {p['handle']: p for p in json.load(open('docs/seo/semrush_nov8_batches_2026-11-10.json'))['products']}
import csv as _csv
NOVRES = {r['keyword']: dict(v=int(r['volume_uk'] or 0), kd=int(r['kd']) if r['kd'] else None)
          for r in _csv.DictReader(open('docs/seo/semrush_nov8_results_2026-11-10.csv'))}
OTH = json.load(open('docs/seo/semrush_others_batches_2026-11-10.json'))['products']
OTHRES = {r['keyword']: dict(v=int(r['volume_uk'] or 0), kd=int(r['kd']) if r['kd'] else None)
          for r in _csv.DictReader(open('docs/seo/semrush_others_results_2026-11-10.csv'))}
def ease(v, kd):
    if not v: return 'No volume'
    return 'Easier' if (kd or 0) <= 29 else ('Medium' if kd <= 49 else 'Hard')
# live products never checked in Semrush
live = [p for f in sorted(glob.glob(sys.argv[1] + '/p*.json')) for p in json.load(open(f))['data']['products']['nodes']]
OTHER_V = {'Highborn London', 'Shiseido', 'Swansura - The Body Studio', 'anatomē', 'Coach', 'Acqua di Parma'}
NONFRAG = re.compile(r'face|serum|cleans|toner|moistur|balm|lip butter|scrub|body butter|eye gel|elixir$|night elixir|youth elixir|facial oil|gel|mask|bath|shower|sleep|pillow|deodorant stick|set$|pack$|collection$|four phase', re.I)
for p in live:
    v = p['vendor']; t = p['title']
    price = min(float(x['price']) for x in p['variants']['nodes'])
    row = dict(brand=v, product=t, size='', price=price, kw='', vol=None, kd=None, ease='', kw2='', vol2=None,
               ktype='', checked=False, added='8 Nov 2026' if v in NOV8 else 'Before 8 Nov', handle=p['handle'])
    if v in NOV8:
        m = NOVKW.get(p['handle'])
        if m:
            k1, k2 = m['primary'], m['secondary']
            r1, r2 = NOVRES.get(k1, {}), NOVRES.get(k2, {}) if k2 else {}
            bw = re.sub(r'[^a-z]', '', v.lower())[:5]
            row.update(kw=k1, vol=r1.get('v', 0), kd=r1.get('kd'), kw2=k2 or '', vol2=r2.get('v', 0) if k2 else None,
                       ease=ease(r1.get('v', 0), r1.get('kd')), checked=True, ktype='Product / brand name (checked 10 Nov 2026)')
        tabs['Fragrances'].append(row)
    elif v in OTHER_V and NONFRAG.search(t) and not re.search(r'eau de|parfum|edp|edt', t, re.I):
        # Others: Semrush checked 10 Nov 2026 (tools/keywords/others_prompts.py); main keyword = the busier of the two
        tok = lambda x: set(re.findall(r'[a-z0-9]+', x.lower()))
        m = next((o for o in OTH if tok(o['title']) <= tok(t)), None)
        if m:
            a, b = (m['primary'], OTHRES[m['primary']]), (m['secondary'], OTHRES[m['secondary']])
            if b[1]['v'] > a[1]['v']: a, b = b, a
            row.update(kw=a[0], vol=a[1]['v'], kd=a[1]['kd'], kw2=b[0], vol2=b[1]['v'], ease=ease(a[1]['v'], a[1]['kd']), checked=True,
                       ktype=('Product / brand name' if re.search(r'highborn|anatome|shiseido|coach|acqua|caviar serum 24k', a[0]) else 'General search term') + ' (checked 10 Nov 2026)')
        tabs['Others'].append(row)

wb = openpyxl.Workbook(); wb.remove(wb.active)
cols = ['Rank', 'Brand', 'Product', 'Size', 'Price £', 'Main keyword', 'UK searches / month', 'Keyword difficulty (KD)',
        'Ease', 'Second keyword', 'Second keyword searches / month', 'Keyword type', 'Added to store']
hdr = PatternFill('solid', fgColor='1B4D3E'); grey = PatternFill('solid', fgColor='EEEEEE'); newfill = PatternFill('solid', fgColor='E4EEE9')
tabs['New 8 Nov (129)'] = None
summary = []
tabs['New 8 Nov (129)'] = [dict(x) for x in tabs['Fragrances'] if x['added'] == '8 Nov 2026']
for name, items in tabs.items():
    items.sort(key=lambda x: (not x['checked'], -(x['vol'] or 0), -(x['vol2'] or 0), str(x['product']).lower()))
    sh = wb.create_sheet(name); sh.append(cols)
    for c in sh[1]:
        c.font = Font(bold=True, color='FFFFFF'); c.fill = hdr; c.alignment = Alignment(wrap_text=True, vertical='center')
    for n, x in enumerate(items, 1):
        if x['checked']:
            sh.append([n, x['brand'], x['product'], x['size'], x['price'], x['kw'], x['vol'], x['kd'], x['ease'],
                       x['kw2'], x['vol2'], x['ktype'], x['added']])
            if x['added'] == '8 Nov 2026':
                for c in sh[sh.max_row]: c.fill = newfill
        else:
            sh.append([n, x['brand'], x['product'], x['size'], x['price'], '', 'Not checked in Semrush', '', '', '', '', '', x['added']])
            for c in sh[sh.max_row]: c.fill = grey
    for i, w in enumerate([6, 18, 60, 10, 9, 38, 14, 12, 9, 30, 14, 34, 14], 1):
        sh.column_dimensions[get_column_letter(i)].width = w
    sh.freeze_panes = 'D2'; sh.auto_filter.ref = sh.dimensions
    chk = [x for x in items if x['checked']]
    summary.append((name, len(items), len(chk), sum(1 for x in chk if x['vol']), len(items) - len(chk)))
s = wb.create_sheet('Read me', 0)
lines = ['Swansura products ranked by Semrush UK search volume (10 Nov 2026)', '',
         'Tabs: 1 Deyga, 2 Vilvah, 3 Fragrances (the 129 added 8 Nov 2026 are in light green), 4 Others, 5 New 8 Nov (129) = those 129 ranked on their own. Rank 1 = most searched main keyword; ties ranked by the second keyword.',
         'Volumes: Semrush UK monthly searches, from the keyword research done for the website (18 Oct 2026) and the new perfumes (2 Nov 2026).',
         'Deyga and Vilvah: most products have no searches for their own name, so their main keyword is the general search the product page',
         'targets (e.g. "hair growth oil", "toner for dry skin"). The "Keyword type" column says which. Their second keyword is usually the brand name.',
         'The 129 fragrances added 8 Nov 2026 and the 39 "Others" (Highborn London, anatomē wellbeing, Shiseido skincare, Swansura Selection skincare, body care)', 
         'were checked in Semrush on 10 Nov 2026 (current live price shown). Others: main keyword = the busier of the brand + product term and a general product-type term. Prices are from the product sheet; La Maison is left out (removed from the store).', '']
for l in lines: s.append([l])
s.append(['Tab', 'Products', 'Checked in Semrush', 'With search volume', 'Not checked'])
for row in summary: s.append(list(row))
s['A1'].font = Font(bold=True, size=14, color='1B4D3E'); s.column_dimensions['A'].width = 24
for c in 'BCDE': s.column_dimensions[c].width = 18
wb.save(OUT)
for row in summary: print(row)

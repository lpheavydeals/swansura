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
OUT = 'docs/seo/Swansura_Products_by_Search_Volume_2026-11-10.xlsx'
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
        kw2=g(r, 'Secondary keyword'), vol2=g(r, 'Secondary vol.') or 0, ktype=ktype, checked=True))

# live products never checked in Semrush
live = [p for f in sorted(glob.glob(sys.argv[1] + '/p*.json')) for p in json.load(open(f))['data']['products']['nodes']]
OTHER_V = {'Highborn London', 'Shiseido', 'Swansura - The Body Studio', 'anatomē', 'Coach', 'Acqua di Parma'}
NONFRAG = re.compile(r'face|serum|cleans|toner|moistur|balm|lip butter|scrub|body butter|eye gel|elixir$|night elixir|youth elixir|facial oil|gel|mask|bath|shower|sleep|pillow|deodorant stick|set$|pack$|collection$|four phase', re.I)
for p in live:
    v = p['vendor']; t = p['title']
    price = min(float(x['price']) for x in p['variants']['nodes'])
    row = dict(brand=v, product=t, size='', price=price, kw='', vol=None, kd=None, ease='', kw2='', vol2=None,
               ktype='', checked=False)
    if v in NOV8:
        tabs['Fragrances'].append(row)
    elif v in OTHER_V and NONFRAG.search(t) and not re.search(r'eau de|parfum|edp|edt', t, re.I):
        tabs['Others'].append(row)

wb = openpyxl.Workbook(); wb.remove(wb.active)
cols = ['Rank', 'Brand', 'Product', 'Size', 'Price £', 'Main keyword', 'UK searches / month', 'Keyword difficulty (KD)',
        'Ease', 'Second keyword', 'Second keyword searches / month', 'Keyword type']
hdr = PatternFill('solid', fgColor='1B4D3E'); grey = PatternFill('solid', fgColor='EEEEEE')
summary = []
for name, items in tabs.items():
    items.sort(key=lambda x: (not x['checked'], -(x['vol'] or 0), -(x['vol2'] or 0), str(x['product']).lower()))
    sh = wb.create_sheet(name); sh.append(cols)
    for c in sh[1]:
        c.font = Font(bold=True, color='FFFFFF'); c.fill = hdr; c.alignment = Alignment(wrap_text=True, vertical='center')
    for n, x in enumerate(items, 1):
        if x['checked']:
            sh.append([n, x['brand'], x['product'], x['size'], x['price'], x['kw'], x['vol'], x['kd'], x['ease'],
                       x['kw2'], x['vol2'], x['ktype']])
        else:
            sh.append([n, x['brand'], x['product'], x['size'], x['price'], '', 'Not checked in Semrush', '', '', '', '', ''])
            for c in sh[sh.max_row]: c.fill = grey
    for i, w in enumerate([6, 18, 60, 10, 9, 38, 14, 12, 9, 30, 14, 34], 1):
        sh.column_dimensions[get_column_letter(i)].width = w
    sh.freeze_panes = 'D2'; sh.auto_filter.ref = sh.dimensions
    chk = [x for x in items if x['checked']]
    summary.append((name, len(items), len(chk), sum(1 for x in chk if x['vol']), len(items) - len(chk)))
s = wb.create_sheet('Read me', 0)
lines = ['Swansura products ranked by Semrush UK search volume (10 Nov 2026)', '',
         'Tabs: 1 Deyga, 2 Vilvah, 3 Fragrances, 4 Others. Rank 1 = most searched main keyword; ties ranked by the second keyword.',
         'Volumes: Semrush UK monthly searches, from the keyword research done for the website (18 Oct 2026) and the new perfumes (2 Nov 2026).',
         'Deyga and Vilvah: most products have no searches for their own name, so their main keyword is the general search the product page',
         'targets (e.g. "hair growth oil", "toner for dry skin"). The "Keyword type" column says which. Their second keyword is usually the brand name.',
         'Grey rows at the bottom were never checked in Semrush: the 8 Nov 2026 fragrances and the "Others" products (Highborn London, anatomē', 
         'wellbeing, Shiseido skincare, Swansura Selection skincare, body care). Prices are from the product sheet; La Maison is left out (removed from the store).', '']
for l in lines: s.append([l])
s.append(['Tab', 'Products', 'Checked in Semrush', 'With search volume', 'Not checked'])
for row in summary: s.append(list(row))
s['A1'].font = Font(bold=True, size=14, color='1B4D3E'); s.column_dimensions['A'].width = 24
for c in 'BCDE': s.column_dimensions[c].width = 18
wb.save(OUT)
for row in summary: print(row)

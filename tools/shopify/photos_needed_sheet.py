"""Client sheet: every photo we still need (user, 12 Nov 2026: 'Make a client sheet listing the photos needed').
Usage: python3 photos_needed_sheet.py <storefront products.json dump (list)>
Reasons come from docs/Swansura_Products_Without_Photos_2026-11-12.xlsx (Drive check of 12 Nov).
Writes docs/Swansura_Photos_Needed_2026-11-12.xlsx: Read me / Photos needed / Wrong photos / By brand.
"""
import json, sys, collections, pathlib, re
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
ROOT = pathlib.Path(__file__).resolve().parents[2]
P = json.load(open(sys.argv[1]))
old = {}
ws0 = load_workbook(ROOT / 'docs/Swansura_Products_Without_Photos_2026-11-12.xlsx')['No photos (58)']
for r in ws0.iter_rows(min_row=5, values_only=True):
    if r[0]: old[r[3]] = (r[8] or '', r[13] or '')
EM, GOLD, YEL = '1B4D3E', 'F4EADA', 'FFF2CC'
# products where the store name may be what is wrong: the client can confirm instead of sending photos
CONFIRM = {'Paco Rabanne Fame Parfum 10ml': 'Our Drive folder shows Fame EAU DE PARFUM 10ml. If that is the bottle you sell, tell us and we will rename the product and use those photos.',
           'Paco Rabanne Phantom Parfum Spray 15ml': 'Our Drive folder shows Phantom EAU DE TOILETTE 15ml. If that is the bottle you sell, tell us and we will rename the product and use those photos.',
           'Superdry Real Fragrance 02 Masculin Eau de Toilette 100ml': 'Our Drive folder shows 01 Masculin. If you sell 01, not 02, tell us and we will rename the product and use those photos.',
           'Superdry Real Fragrance 02 Feminin Eau de Toilette 100ml': 'Our Drive folder shows 01 Feminin (already on our 01 Feminin product). Please send 02 Feminin photos.'}
def why(title, brand):
    r, d = old.get(title, ('', ''))
    if r.startswith('Drive folder shows a different product'):
        return 'Drive folder has photos of a different product: ' + r.split(':', 1)[1].strip()
    if brand == 'Vilvah': return 'No photos yet (not in the Vilvah Drive we were given)'
    return 'No photos in the Drive for this product'
rows = []
for p in P:
    if p['images']: continue
    vs = p['variants']; brand = p['vendor']
    rows.append(dict(brand=brand, title=p['title'], sizes=', '.join(v['title'] for v in vs) if len(vs) > 1 else '',
                     price=' / '.join(f'£{x:.2f}' for x in sorted({float(v['price']) for v in vs})),
                     stock='In stock' if any(v['available'] for v in vs) else 'Sold out',
                     now=why(p['title'], brand), confirm=CONFIRM.get(p['title'], ''),
                     folder=f"{brand}/{re.sub('^' + re.escape(brand) + ' ', '', p['title'])}",
                     url='https://www.swansura.com/products/' + p['handle']))
rows.sort(key=lambda r: (r['stock'] != 'In stock', r['brand'], r['title']))
WRONG = [('Tom Ford', 'Tom Ford Oud Wood Eau de Parfum 50ml Unisex (second listing, sold out)', 'https://www.swansura.com/products/tom-ford-oud-wood-eau-de-parfum-50ml-unisex-1',
          'All 4 photos show Tom Ford VELVET ORCHID (purple bottle, name on box and label), not Oud Wood.',
          'Send Oud Wood 50ml photos, or tell us to retire this second listing (the main Oud Wood 30/50ml listing already has the right photos).'),
         ('anatomē', 'anatomē Focus Eau de Parfum Travel 10ml', 'https://www.swansura.com/products/focus-eau-de-parfum-travel-10ml',
          'One gallery photo shows the ORDER travel spray, not Focus.', 'Tell us if we should remove that photo (anatomē supplies these photos through Shopify Collective).'),
         ('Swansura Selection', '24K Gold Hydrating Face Mask', 'https://www.swansura.com/products/24k-gold-hydrating-face-mask',
          'The photos show a Blushing Beauty Gold Blackhead Face Mask pack, not a pack named 24K Gold Hydrating Face Mask.',
          'Send photos of the pack you sell, or confirm the product name.')]
wb = Workbook()
rd = wb.active; rd.title = 'Read me'
ins = sum(r['stock'] == 'In stock' for r in rows)
lines = [('Swansura – product photos we still need (12 Nov 2026)', True),
         ('', False),
         (f'{len(rows)} products on the website have no photo yet. {ins} of them are in stock and on sale now with a "Photo coming soon" card, so please start with those (they are at the top of the list).', False),
         (f'{len(WRONG)} more products show the wrong photos (tab "Wrong photos").', False),
         ('', False),
         ('What to send for each product', True),
         ('1. One clear front photo of the bottle or pack (the label must be readable). A photo with the box is a bonus.', False),
         ('2. If you have them: a photo of the box, the back label, and any other angle. 2–4 photos per product is ideal.', False),
         ('3. Plain or simple background, good light. We cut every photo out and place it on the website background, so props and scenery are not needed.', False),
         ('4. The photo must show exactly the product on the listing: same name, size and type (Parfum, Eau de Parfum or Eau de Toilette). A photo of a similar bottle cannot be used.', False),
         ('', False),
         ('How to send', True),
         ('Upload to the usual fragrance photo Drive folder, one folder per product, named like column I (e.g. "Maison Alhambra/Salvo Eau de Parfum 100ml"). Then mark column J "Yes".', False),
         ('If a product name on our site is wrong (the photo you have is the right bottle but our name is not), write it in column K and we will fix the name.', False),
         ('If you no longer sell a product, choose "Not stocking it" in column J and we will hide it.', False)]
for i, (t, b) in enumerate(lines, 1):
    c = rd.cell(i, 1, t); c.alignment = Alignment(wrap_text=True)
    if b: c.font = Font(bold=True, size=13 if i == 1 else 11, color=EM)
rd.column_dimensions['A'].width = 120
ws = wb.create_sheet(f'Photos needed ({len(rows)})')
HEAD = ['#', 'Brand', 'Product (as on the website)', 'Sizes', 'Price', 'Stock', 'What we have now', 'Or just confirm', 'Suggested Drive folder name', 'Photos sent?', 'Notes / correct name', 'Live page']
W = [5, 18, 58, 14, 14, 10, 52, 46, 52, 15, 34, 46]
for i, h in enumerate(HEAD, 1):
    c = ws.cell(1, i, h); c.font = Font(bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor=EM)
    c.alignment = Alignment(wrap_text=True, vertical='center'); ws.column_dimensions[c.column_letter].width = W[i - 1]
dv = DataValidation(type='list', formula1='"Yes,Not stocking it,Name confirmed"', allow_blank=True); ws.add_data_validation(dv)
for k, r in enumerate(rows, 1):
    vals = [k, r['brand'], r['title'], r['sizes'], r['price'], r['stock'], r['now'], r['confirm'], r['folder'], '', '', r['url']]
    for i, v in enumerate(vals, 1):
        c = ws.cell(k + 1, i, v); c.alignment = Alignment(wrap_text=True, vertical='top')
        if r['stock'] == 'In stock' and i == 6: c.font = Font(bold=True, color=EM)
    for col in (10, 11): ws.cell(k + 1, col).fill = PatternFill('solid', fgColor=YEL)
    dv.add(ws.cell(k + 1, 10)); ws.cell(k + 1, 12).hyperlink = r['url']
ws.freeze_panes = 'D2'; ws.auto_filter.ref = f'A1:L{len(rows) + 1}'
w2 = wb.create_sheet(f'Wrong photos ({len(WRONG)})')
H2 = ['#', 'Brand', 'Product', 'What is wrong', 'What we need', 'Your answer', 'Live page']
for i, h in enumerate(H2, 1):
    c = w2.cell(1, i, h); c.font = Font(bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor=EM)
    w2.column_dimensions[c.column_letter].width = [5, 18, 50, 60, 60, 30, 50][i - 1]
for k, (b, t, u, w, n) in enumerate(WRONG, 1):
    for i, v in enumerate([k, b, t, w, n, '', u], 1):
        c = w2.cell(k + 1, i, v); c.alignment = Alignment(wrap_text=True, vertical='top')
    w2.cell(k + 1, 6).fill = PatternFill('solid', fgColor=YEL); w2.cell(k + 1, 7).hyperlink = u
w3 = wb.create_sheet('By brand')
w3.append(['Brand', 'Products needing photos', 'Of which in stock']); [setattr(c, 'font', Font(bold=True)) for c in w3[1]]
cb = collections.Counter(r['brand'] for r in rows); ci = collections.Counter(r['brand'] for r in rows if r['stock'] == 'In stock')
for b, n in cb.most_common(): w3.append([b, n, ci.get(b, 0)])
w3.append(['Total', len(rows), ins]); w3.column_dimensions['A'].width = 22; w3.column_dimensions['B'].width = 26; w3.column_dimensions['C'].width = 20
out = ROOT / 'docs/Swansura_Photos_Needed_2026-11-12.xlsx'; wb.save(out)
print(out.name, len(rows), 'products,', ins, 'in stock;', dict(cb.most_common()))

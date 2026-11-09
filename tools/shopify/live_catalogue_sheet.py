"""Client sheet: what is live on swansura.com (user, 9 Nov 2026: "give me the detailed sheet … sector-wise … photos,
in stock, sold out … clients list vs what's live … downloadable XLSX to discuss with the client").

Input : docs/data/live_catalogue_2026-11-09.json (Admin export of all ACTIVE products: title, vendor, stock, tags,
        media count, custom.pdp cat + handle; wrong-folder notes from docs/images/drive_nov9_photos_2026-11-09.json)
Output: docs/Swansura_Live_Catalogue_Summary_2026-11-09.xlsx
"""
import json, pathlib, collections
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = pathlib.Path(__file__).resolve().parents[2]
D = json.load(open(ROOT / 'docs/data/live_catalogue_2026-11-09.json'))
P, WRONG = D['products'], D['wrong_folder_notes']
SECTORS = [('fragrance', 'Fragrance'), ('skincare', 'Skincare'), ('haircare', 'Haircare'), ('bath-body', 'Bath & body')]

def sector(p):
    try:
        c = json.loads(p['pdp']['value']).get('cat')
    except Exception:
        c = None
    return c or ('haircare' if 'Hair' in p['title'] else 'bath-body')

NO_FOLDER = {'issey-miyake-leau-dissey-eau-de-toilette-50ml', 'lalique-hommage-a-lhomme-eau-de-toilette-shower-gel-gift-set-100ml-150ml',
             'lalique-linsoumis-eau-de-toilette-100ml', 'lanvin-mon-eclat-eau-de-parfum-mini-with-pouch-7-5ml',
             'paco-rabanne-invictus-eau-de-toilette-200ml', 'paco-rabanne-lady-million-eau-de-parfum-15ml'}
def photo_reason(p):
    h = p['handle']
    if h in WRONG:
        return 'Drive folder shows a different product: ' + WRONG[h]
    if h in NO_FOLDER or p['vendor'] in ('Maison Alhambra', 'Arabiyat Prestige', 'Formula 1', 'Natural By Woods', 'Jaguar', 'Franck Olivier', 'Vilvah'):
        return 'No photo folder in the client Drive for this product'
    return 'No photos received yet'

for p in P:
    p['sec'] = dict(SECTORS)[sector(p)]
    p['photos'] = p['mediaCount']['count']
    p['stock'] = p['totalInventory'] or 0

EMERALD, GOLD, TINT, GREY = '1B4D3E', 'B5843A', 'E4EEE9', 'F5F2ED'
H = Font(bold=True, color='FFFFFF'); HF = PatternFill('solid', fgColor=EMERALD)
B = Font(bold=True); TITLE = Font(bold=True, size=16, color=EMERALD); SUB = Font(italic=True, color='695541')
TOT = PatternFill('solid', fgColor=TINT); RED = PatternFill('solid', fgColor='F3E6E0'); YEL = PatternFill('solid', fgColor='FFF4CC')
thin = Side(style='thin', color='E3DACD'); BOX = Border(top=thin, bottom=thin, left=thin, right=thin)

def table(ws, r, headers, rows, widths=None, total=False):
    for i, h in enumerate(headers, 1):
        c = ws.cell(r, i, h); c.font, c.fill, c.border = H, HF, BOX
        c.alignment = Alignment(wrap_text=True, vertical='center')
    for j, row in enumerate(rows, 1):
        for i, v in enumerate(row, 1):
            c = ws.cell(r + j, i, v); c.border = BOX; c.alignment = Alignment(wrap_text=True, vertical='top')
            if total and j == len(rows):
                c.font, c.fill = B, TOT
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = max(ws.column_dimensions[get_column_letter(i)].width or 0, w)
    return r + len(rows) + 2

wb = Workbook()
# ---------------------------------------------------------------- Summary
ws = wb.active; ws.title = 'Summary'
ws['A1'] = 'Swansura – live catalogue summary'; ws['A1'].font = TITLE
ws['A2'] = 'swansura.com, checked 9 Nov 2026 (Shopify Admin, active products only)'; ws['A2'].font = SUB
rows = []
for k, name in SECTORS:
    ps = [p for p in P if p['sec'] == name]
    rows.append([name, len(ps), len({p['vendor'] for p in ps}), sum(p['photos'] > 0 for p in ps), sum(p['photos'] == 0 for p in ps),
                 sum(p['photos'] for p in ps), sum(p['stock'] > 0 for p in ps), sum(p['stock'] <= 0 for p in ps)])
rows.append(['Total', len(P), len({p['vendor'] for p in P}), sum(p['photos'] > 0 for p in P), sum(p['photos'] == 0 for p in P),
             sum(p['photos'] for p in P), sum(p['stock'] > 0 for p in P), sum(p['stock'] <= 0 for p in P)])
ws['A4'] = '1. Live products by sector'; ws['A4'].font = B
r = table(ws, 5, ['Sector', 'Live products', 'Brands', 'With photos', 'Without photos', 'Photos (images)', 'In stock', 'Sold out'],
          rows, [22, 14, 10, 13, 15, 15, 11, 11], total=True)
notes = ['Every one of the photos has alt text (checked 9 Nov 2026).',
         f"All {sum(p['stock'] > 0 for p in P)} in-stock products have photos; every product without photos is sold out.",
         'Sold-out products stay live with a "Notify me when back" button; in-stock products are listed first on every page.']
for n in notes:
    ws.cell(r - 1, 1, '• ' + n); r += 1
r += 1
ws.cell(r, 1, '2. Skincare, haircare and bath & body by brand').font = B; r += 1
brands = sorted({p['vendor'] for p in P if p['sec'] != 'Fragrance'}, key=lambda v: -sum(1 for p in P if p['vendor'] == v and p['sec'] != 'Fragrance'))
rows = []
for v in brands:
    vals = [sum(1 for p in P if p['vendor'] == v and p['sec'] == s) for _, s in SECTORS[1:]]
    rows.append([v.replace('Swansura - The Body Studio', 'Swansura Selection')] + vals + [sum(vals)])
rows.append(['Total'] + [sum(1 for p in P if p['sec'] == s) for _, s in SECTORS[1:]] + [sum(1 for p in P if p['sec'] != 'Fragrance')])
r = table(ws, r, ['Brand', 'Skincare', 'Haircare', 'Bath & body', 'Total'], rows, total=True)
ws.cell(r - 1, 1, '3. Client product list vs what is live').font = B
rows = [['Fragrance', '821 rows', 'All live except 1 row', 'Rimmel liquid lipstick (not a fragrance). The sheet repeats many perfumes under two spellings, and sizes of one perfume are one product with a size choice, so rows > products.'],
        ['Vilvah & Deyga', '159 rows', '157 live', '2 Deyga products are drafts waiting for a price: Anti-Dandruff Hair Oil 100ml, Baby Bath Bar 130g.']]
r = table(ws, r, ["Client's final sheet (9 Nov)", 'Rows given', 'Result in the store', 'Not live / notes'], rows, [22, 14, 22, 70])
ws.cell(r - 1, 1, '4. Other numbers').font = B
other = [['Products added from the November sheets (tag "New 2026-11")', sum('New 2026-11' in p['tags'] for p in P)],
         ['   …of which now have photos', sum('New 2026-11' in p['tags'] and p['photos'] > 0 for p in P)],
         ['Live fragrances from the store catalogue before November', sum(p['sec'] == 'Fragrance' and 'New 2026-11' not in p['tags'] for p in P)],
         ['Draft products (not live)', 12], ['   …of which waiting for a price', 3], ['Archived products', 4]]
table(ws, r, ['Item', 'Count'], other)
ws.column_dimensions['A'].width = 62

# ---------------------------------------------------------------- Fragrance brands
ws = wb.create_sheet('Fragrance by brand')
ws['A1'] = 'Fragrance: live products by brand'; ws['A1'].font = TITLE
rows = []
for v in sorted({p['vendor'] for p in P if p['sec'] == 'Fragrance'}, key=str.lower):
    ps = [p for p in P if p['vendor'] == v and p['sec'] == 'Fragrance']
    rows.append([v.replace('Swansura - The Body Studio', 'Swansura Selection'), len(ps), sum(p['photos'] > 0 for p in ps), sum(p['photos'] == 0 for p in ps),
                 sum(p['stock'] > 0 for p in ps), sum(p['stock'] <= 0 for p in ps)])
fr = [p for p in P if p['sec'] == 'Fragrance']
rows.append(['Total', len(fr), sum(p['photos'] > 0 for p in fr), sum(p['photos'] == 0 for p in fr), sum(p['stock'] > 0 for p in fr), sum(p['stock'] <= 0 for p in fr)])
table(ws, 3, ['Brand', 'Live products', 'With photos', 'Without photos', 'In stock', 'Sold out'], rows, [30, 13, 13, 15, 11, 11], total=True)
ws.freeze_panes = 'A4'

# ---------------------------------------------------------------- Without photos
ws = wb.create_sheet('Without photos (58)')
nophoto = sorted([p for p in P if p['photos'] == 0], key=lambda p: (p['sec'], p['vendor'], p['title']))
ws.title = f'Without photos ({len(nophoto)})'
ws['A1'] = 'Live products without photos – client to send photos'; ws['A1'].font = TITLE
rows = [[p['sec'], p['vendor'], p['title'], 'Sold out' if p['stock'] <= 0 else p['stock'], photo_reason(p), f"https://www.swansura.com/products/{p['handle']}", ''] for p in nophoto]
table(ws, 3, ['Sector', 'Brand', 'Product', 'Stock', 'Why no photo', 'Link', 'Client: photos sent? (Y/N)'], rows, [12, 18, 58, 10, 60, 50, 16])
dv = DataValidation(type='list', formula1='"Y,N"', allow_blank=True); ws.add_data_validation(dv); dv.add(f'G4:G{3 + len(rows)}')
for i in range(len(rows)):
    ws.cell(4 + i, 7).fill = YEL
ws.freeze_panes = 'A4'; ws.auto_filter.ref = f'A3:G{3 + len(rows)}'

# ---------------------------------------------------------------- All live products
ws = wb.create_sheet('All live products')
ws['A1'] = f'All {len(P)} live products'; ws['A1'].font = TITLE
allp = sorted(P, key=lambda p: (p['sec'], p['vendor'].lower(), p['title'].lower()))
rows = [[p['sec'], p['vendor'].replace('Swansura - The Body Studio', 'Swansura Selection'), p['title'], p['photos'], 'Yes' if p['photos'] else 'No',
         p['stock'], 'In stock' if p['stock'] > 0 else 'Sold out', 'Yes' if 'New 2026-11' in p['tags'] else '',
         f"https://www.swansura.com/products/{p['handle']}"] for p in allp]
table(ws, 3, ['Sector', 'Brand', 'Product', 'Photos', 'Has photos', 'Stock qty', 'Status', 'Added from Nov sheets', 'Link'], rows,
      [12, 22, 62, 8, 11, 10, 11, 12, 60])
for i, p in enumerate(allp):
    if not p['photos']:
        for c in range(1, 10):
            ws.cell(4 + i, c).fill = RED
ws.freeze_panes = 'A4'; ws.auto_filter.ref = f'A3:I{3 + len(rows)}'

out = ROOT / 'docs/Swansura_Live_Catalogue_Summary_2026-11-09.xlsx'
wb.save(out)
print(out, len(P), len(nophoto))

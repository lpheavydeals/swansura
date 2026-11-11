"""Live list of every published product without a photo (user, 11 Nov 2026: Paco Rabanne perfumes without photos were
missing from the 3 Nov 'Products without photos' sheet, which predates the 8 Nov products).
Usage: python3 no_photo_sheet_live.py <storefront /products.json dump (list)>
Reasons per product come from the 9 Nov catalogue summary (tab 'Without photos (58)') when the title matches.
Writes docs/Swansura_Products_Without_Photos_2026-11-11.xlsx
"""
import json, sys, pathlib, re
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
ROOT = pathlib.Path(__file__).resolve().parents[2]
P = json.load(open(sys.argv[1]))
why = {}
ws = load_workbook(ROOT / 'docs/Swansura_Live_Catalogue_Summary_2026-11-09.xlsx', read_only=True)['Without photos (58)']
for r in ws.iter_rows(values_only=True):
    if r and isinstance(r[2], str) and isinstance(r[4], str): why[r[2]] = r[4]
ADMIN = 'https://admin.shopify.com/store/d2rqgy-5e/products/'
rows = []
for p in P:
    if p['images']: continue
    vs = p['variants']
    sizes = ', '.join(v['title'] for v in vs) if len(vs) > 1 else ''
    prices = sorted({float(v['price']) for v in vs})
    added = p['created_at'][:10]
    rows.append(dict(kind='Skincare' if p['vendor'] in ('Vilvah', 'Deyga') else 'Fragrance', brand=p['vendor'], title=p['title'], sizes=sizes,
                     price=' / '.join(f'£{x:.2f}' for x in prices), stock='In stock' if any(v['available'] for v in vs) else 'Sold out',
                     added=added, new8=added >= '2026-11-08', why=why.get(p['title'], 'No photo folder in the client Drive for this product'),
                     live='https://www.swansura.com/products/' + p['handle'], admin=ADMIN + str(p['id'])))
rows.sort(key=lambda r: (r['kind'] != 'Fragrance', r['brand'], r['title']))
HEAD = ['#', 'Type', 'Brand', 'Product (as on the website)', 'Sizes', 'Price', 'Stock', 'Added to store', 'Why there is no photo yet',
        'Live page', 'Shopify admin', 'Photos sent?', 'Notes']
W = [5, 11, 18, 62, 16, 14, 10, 13, 70, 44, 24, 13, 30]
em = '1B4D3E'
wb = Workbook(); ws = wb.active; ws.title = f'No photos ({len(rows)})'
n8 = sum(r['new8'] for r in rows)
ws['A1'] = f'Swansura – every live product without a photo (checked on the live site, 11 Nov 2026): {len(rows)} products'
ws['A1'].font = Font(bold=True, size=12, color=em)
ws['A2'] = (f'Replaces the 3 Nov sheet (40 products). {n8} products added on 8 Nov are new on this list (green rows). '
            'Please add 1 plain bottle or box photo + 2–3 more per product to the Drive, in a folder named after the product, then mark column L.')
for c in ('A1', 'A2'): ws.merge_cells(f'{c}:M{c[1]}')
ws['A2'].alignment = Alignment(wrap_text=True); ws.row_dimensions[2].height = 32
for i, h in enumerate(HEAD, 1):
    c = ws.cell(4, i, h); c.font = Font(bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor=em); c.alignment = Alignment(wrap_text=True, vertical='center')
    ws.column_dimensions[c.column_letter].width = W[i - 1]
dv = DataValidation(type='list', formula1='"Yes,No,Not stocking it"', allow_blank=True); ws.add_data_validation(dv)
for k, r in enumerate(rows, 1):
    vals = [k, r['kind'], r['brand'], r['title'], r['sizes'], r['price'], r['stock'], r['added'], r['why'], r['live'], r['admin'], '', '']
    for i, v in enumerate(vals, 1):
        c = ws.cell(4 + k, i, v); c.alignment = Alignment(wrap_text=True, vertical='top')
        if r['new8']: c.fill = PatternFill('solid', fgColor='E4EEE9')
    ws.cell(4 + k, 10).hyperlink = r['live']; ws.cell(4 + k, 11).hyperlink = r['admin']
    ws.cell(4 + k, 12).fill = PatternFill('solid', fgColor='FFF2CC'); dv.add(ws.cell(4 + k, 12))
ws.freeze_panes = 'E5'; ws.auto_filter.ref = f'A4:M{4 + len(rows)}'
s = wb.create_sheet('By brand')
s.append(['Brand', 'Products without a photo', 'Of which added 8 Nov']); [setattr(c, 'font', Font(bold=True)) for c in s[1]]
from collections import Counter
cb, c8 = Counter(r['brand'] for r in rows), Counter(r['brand'] for r in rows if r['new8'])
for b, n in cb.most_common(): s.append([b, n, c8.get(b, 0)])
s.append(['Total', len(rows), n8]); s.column_dimensions['A'].width = 22; s.column_dimensions['B'].width = 26; s.column_dimensions['C'].width = 22
out = ROOT / 'docs/Swansura_Products_Without_Photos_2026-11-11.xlsx'; wb.save(out)
print(out.name, len(rows), 'rows,', n8, 'added 8 Nov;', sum(r['stock'] == 'In stock' for r in rows), 'in stock')
for r in rows:
    if r['brand'] == 'Paco Rabanne': print(' ', r['title'], '|', r['stock'], '|', r['why'][:90])

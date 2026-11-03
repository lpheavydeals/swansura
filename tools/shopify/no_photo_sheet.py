"""Excel list of the new products that still have no photos (user, 3 Nov 2026: 'Sheet 1 – products that don't have pictures
in the drive, Sheet 2 – 34 missed'). Sheet 1 = all 40 new products with no Drive photos (tag 'Photo pending');
Sheet 2 = the 34 perfumes among them. Source: docs/seo/sheet_live_products_2026-11-02.json + photo results.
Writes docs/Swansura_Products_Without_Photos_2026-11-03.xlsx
"""
import json, pathlib, re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
ROOT = pathlib.Path(__file__).resolve().parents[2]
P = json.load(open(ROOT / 'docs/seo/sheet_live_products_2026-11-02.json'))
done = {r['handle'] for r in json.load(open(ROOT / 'docs/images/drive_nov_photos_2026-11-03.json')) if r['status'] == 'uploaded'}
HM = json.load(open(ROOT / 'docs/seo/title_fixes_2026-11-03.json'))['handle_map']
done |= {HM[h] for h in list(done) if h in HM}
ADMIN = 'https://admin.shopify.com/store/d2rqgy-5e/products/'
rows = []
for p in P:
    if p['handle'] in done:
        continue
    i = p['input']
    sizes = ', '.join(v['optionValues'][0]['name'] for v in i['variants']) if len(i['variants']) > 1 else (re.search(r'(\d+(\.\d+)?\s?(ml|g)( \+ \d+ml)?|\d+ x \d+ml)\s*$', i['title'], re.I) or [''])[0]
    prices = sorted({float(v['price']) for v in i['variants']})
    rows.append({'brand': p['brand'], 'title': i['title'], 'size': sizes,
                 'price': ' / '.join(f'£{x:.2f}' for x in prices), 'kind': 'Perfume' if p['kind'] == 'perfume' else 'Vilvah skincare',
                 'live': 'https://www.swansura.com/products/' + p['handle'], 'admin': ADMIN + p['id'].rsplit('/', 1)[1],
                 'folder': f"{p['brand']}/{re.sub(r'^' + re.escape(p['brand']) + ' ', '', i['title'])}"})
rows.sort(key=lambda r: (r['kind'] != 'Perfume', r['brand'], r['title']))
assert len(rows) == 40, len(rows)
HEAD = ['#', 'Brand', 'Product (as on the website)', 'Size', 'Price', 'Type', 'Suggested Drive folder name', 'Live page', 'Shopify admin', 'Photos sent?', 'Notes']
W = [5, 18, 58, 16, 12, 15, 46, 40, 22, 14, 30]
emerald, gold = '1B4D3E', 'F4EADA'

def sheet(ws, title, data, lead):
    ws.title = title
    ws['A1'] = lead
    ws['A1'].font = Font(bold=True, size=12, color=emerald)
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(HEAD))
    ws['A2'] = ('Please add 1 plain bottle (or box) photo on a white background + 2–3 more per product, in a Drive folder named '
                'like column G. AI-styled images are fine.')
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(HEAD))
    ws['A2'].alignment = Alignment(wrap_text=True)
    ws.row_dimensions[2].height = 30
    for c, h in enumerate(HEAD, 1):
        x = ws.cell(4, c, h)
        x.font = Font(bold=True, color='FFFFFF')
        x.fill = PatternFill('solid', fgColor=emerald)
        x.alignment = Alignment(vertical='center', wrap_text=True)
        ws.column_dimensions[x.column_letter].width = W[c - 1]
    dv = DataValidation(type='list', formula1='"Not yet,Sent,Not available"', allow_blank=True)
    ws.add_data_validation(dv)
    for n, r in enumerate(data, 1):
        vals = [n, r['brand'], r['title'], r['size'], r['price'], r['kind'], r['folder'], r['live'], 'Open in Shopify', 'Not yet', '']
        for c, v in enumerate(vals, 1):
            x = ws.cell(4 + n, c, v)
            x.alignment = Alignment(vertical='top', wrap_text=c in (3, 7, 11))
            if n % 2 == 0:
                x.fill = PatternFill('solid', fgColor='FBF8F3')
        ws.cell(4 + n, 8).hyperlink = r['live']; ws.cell(4 + n, 8).font = Font(color='0563C1', underline='single')
        ws.cell(4 + n, 9).hyperlink = r['admin']; ws.cell(4 + n, 9).font = Font(color='0563C1', underline='single')
        dv.add(ws.cell(4 + n, 10))
    ws.freeze_panes = 'C5'
    ws.auto_filter.ref = f'A4:{ws.cell(4, len(HEAD)).column_letter}{4 + len(data)}'

wb = Workbook()
sheet(wb.active, 'No photos (40)', rows,
      f'Swansura – 40 new products with no photos in the Drive folder (3 Nov 2026): {sum(r["kind"]=="Perfume" for r in rows)} perfumes + {sum(r["kind"]!="Perfume" for r in rows)} Vilvah items')
perf = [r for r in rows if r['kind'] == 'Perfume']
sheet(wb.create_sheet(), f'Perfumes missing ({len(perf)})', perf,
      f'Swansura – the {len(perf)} perfumes still missing photos (3 Nov 2026)')
out = ROOT / 'docs/Swansura_Products_Without_Photos_2026-11-03.xlsx'
wb.save(out)
from collections import Counter
print(out, len(rows), len(perf), Counter(r['brand'] for r in rows))

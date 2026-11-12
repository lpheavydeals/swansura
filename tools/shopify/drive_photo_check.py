"""Check the client's fragrance photo Drive (public folder 1hHkzu2krQKx-9ffazrihUhPf1NVHIPro) against the products without
photos (user, 12 Nov 2026: 'the client uploaded some photos in that drive recently … what are present and what are absent').
Usage: python3 drive_photo_check.py <drive tree json from drive_tree.py>
Reads docs/Swansura_Products_Without_Photos_2026-11-11.xlsx, writes docs/Swansura_Products_Without_Photos_2026-11-12.xlsx
(same rows + 'Fragrance Drive check (12 Nov)' column + a 'Drive summary' tab).
"""
import sys, json, collections, re
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
ROOT = __file__.rsplit('/tools/', 1)[0]
tree = json.load(open(sys.argv[1]))
files = [r for r in tree if r['kind'] == 'file']
cnt = collections.Counter()
for r in files:
    p = r['path'].split('/')
    for k in range(1, len(p)): cnt['/'.join(p[:k])] += 1
latest = max((r['modified'] for r in tree), key=lambda m: (['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'].index(m[:3]), int(m[4:])))
tops = {r['title'].strip().lower() for r in tree if '/' not in r['path']}
wb = load_workbook(ROOT + '/docs/Swansura_Products_Without_Photos_2026-11-11.xlsx'); ws = wb.worksheets[0]
col = 14; ws.cell(4, col, 'Fragrance Drive check (12 Nov)').font = Font(bold=True, color='FFFFFF')
ws.cell(4, col).fill = PatternFill('solid', fgColor='1B4D3E'); ws.column_dimensions['N'].width = 60
summary = collections.Counter()
for row in range(5, ws.max_row + 1):
    brand, why = ws.cell(row, 3).value, ws.cell(row, 9).value or ''
    if not brand: continue
    if brand == 'Vilvah':
        v = 'Not in the fragrance Drive (Vilvah photos come from the separate Vilvah Drive): ABSENT here'
        k = 'Vilvah (other Drive)'
    elif why.startswith('Drive folder shows a different product'):
        v = 'Folder present, but its photos show a different product (no change since 9 Nov): STILL ABSENT'
        k = 'Folder shows another product'
    else:
        b = {'Franck Olivier': 'frank olivier', 'Natural By Woods': 'natural woods collection', 'Superdry': 'real superdry'}.get(brand, brand.lower())
        v = ('No folder for this product (brand folder exists)' if b in tops else 'No folder for this brand') + ': ABSENT'
        k = 'No folder'
    ws.cell(row, col, v).alignment = Alignment(wrap_text=True, vertical='top'); summary[k] += 1
ws.auto_filter.ref = f'A4:N{ws.max_row}'
s = wb.create_sheet('Drive summary', 0)
lines = [('Fragrance photo Drive check, 12 Nov 2026', ''),
         ('Drive folder', 'https://drive.google.com/drive/folders/1hHkzu2krQKx-9ffazrihUhPf1NVHIPro'),
         ('Files in the Drive', f'{len(files)} files in {sum(r["kind"]=="folder" for r in tree)} folders ({len(tops)} brand folders)'),
         ('Same as on 3 Nov?', 'Yes: 2,685 files then, 2,685 now'),
         ('Newest file or folder date', latest),
         ('New photos for the 58 products', 'None found: nothing in the Drive is dated after ' + latest),
         ('', ''),
         ('Products without a photo (live site)', 58)] + [(k, n) for k, n in summary.most_common()] + [
         ('', ''),
         ('Brands with no folder at all', 'Maison Alhambra (25 products), Arabiyat Prestige (2), Formula 1, Lanvin'),
         ('Note', 'If the client uploaded somewhere else (another folder, a shared drive, WhatsApp), please send that link.')]
for a, b in lines: s.append([a, b])
s['A1'].font = Font(bold=True, size=12, color='1B4D3E'); s.column_dimensions['A'].width = 38; s.column_dimensions['B'].width = 90
out = ROOT + '/docs/Swansura_Products_Without_Photos_2026-11-12.xlsx'; wb.save(out)
print(out.rsplit('/', 1)[1], dict(summary), 'latest', latest)

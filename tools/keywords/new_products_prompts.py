"""Semrush prompts for the 201 new perfumes from the client's 2 Nov 2026 sheet (same format as the Tier 3 prompts).

Keywords = each new product's primary (brand + name) and secondary (+ concentration) keyword, plus one brand term per
new brand, minus anything already in the 'Semrush Data' tab. Batches of 100 (Semrush Keyword Overview bulk limit).
Exports are to be named New_Batch_N_UK_keywords.xlsx.
Run: python3 tools/keywords/new_products_prompts.py
"""
import json, pathlib, openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
ROOT = pathlib.Path(__file__).resolve().parents[2]
rows = json.load(open(ROOT / 'docs/seo/fragrance_new_seo_2026-11-02.json'))
kw = openpyxl.load_workbook(ROOT / 'seo/Swansura_Keyword_Research.xlsx', read_only=True)
done = {str(r[0]).strip().lower() for r in kw['Semrush Data'].iter_rows(min_row=2, values_only=True) if r[0]}
want, seen = [], set()
def add(k):
    k = ' '.join(str(k or '').lower().replace('–', ' ').split())
    if k and k not in seen and k not in done:
        seen.add(k); want.append(k)
BRANDKW = {'Bois': 'bois 1920 perfume', 'Fun & Basics': 'fun and basics perfume', 'Unlimited': None, 'Notebook': 'notebook perfume'}
for b in sorted({r['brand'] for r in rows}):
    k = BRANDKW.get(b, b + ' perfume')
    if k:
        add(k)
for r in rows:
    add(r['primary'])
    add(r['secondary'])
B = [want[i:i + 100] for i in range(0, len(want), 100)]
A = 'Arial'; F = Font(name=A, size=10)
wb = Workbook(); ix = wb.active; ix.title = 'Index'
ix['A1'] = 'Semrush prompts: new perfumes (client sheet, 2 Nov 2026)'; ix['A1'].font = Font(name=A, bold=True, size=13)
ix['A2'] = f'{len(want)} keywords in {len(B)} batches: the primary keyword (brand + perfume name) and the concentration variant of each of the 201 new perfumes, plus one "<brand> perfume" term per new brand. Keywords already checked earlier are left out.'
ix['A3'] = 'How to use: open a "New Prompt" tab, click the column A header, copy and paste into the Claude in Chrome side panel with Semrush open. One prompt at a time.'
ix['A4'] = 'Then upload the exports (New_Batch_N_UK_keywords.xlsx) to the Claude Code session.'
for c in ('A2', 'A3', 'A4'):
    ix[c].font = F; ix[c].alignment = Alignment(wrap_text=True)
for i, h in enumerate(['Prompt', 'Tab', 'Keywords', 'Status', 'Export file name', 'Keywords with data', 'Notes'], 1):
    ix.cell(row=6, column=i, value=h).font = Font(name=A, size=10, bold=True)
ix.column_dimensions['A'].width = 18; ix.column_dimensions['B'].width = 16; ix.column_dimensions['E'].width = 32
for bi, batch in enumerate(B, 1):
    ws = wb.create_sheet(f'New Prompt {bi}'); ws.column_dimensions['A'].width = 120
    lines = [f'Task: get UK search volumes for a keyword list in Semrush (New perfumes, Batch {bi} of {len(B)}).', None, 'Steps:',
             '1. In this Semrush tab, open SEO > Keyword Overview.',
             '2. Set the database to United Kingdom (UK flag) before analysing. Do not use any other country.',
             '3. Paste the keyword list below into the Keyword Overview box (bulk analysis, one keyword per line) and click Analyze / Search.',
             f'4. When the results table loads, use Export > Excel (.xlsx) to download the results for all keywords. Keep the default columns. Save it as New_Batch_{bi}_UK_keywords.xlsx.',
             '5. Tell me: the downloaded file name, how many keywords returned data, and any keywords Semrush rejected.', None, 'Rules:',
             '- Do not change account settings, buy anything, start a trial or upgrade the plan.',
             '- If Semrush shows a limit, captcha, login prompt or an "upgrade" message, stop and tell me instead of working around it.',
             '- Do not add, remove or edit keywords in the list.', None, f'Keywords (New perfumes, Batch {bi}):'] + batch
    for j, v in enumerate(lines, 1):
        ws.cell(row=j, column=1, value=v).font = F
    row = 6 + bi
    for i, val in enumerate([f'New Prompt {bi}', f'New Prompt {bi}', len(batch), 'To do', f'New_Batch_{bi}_UK_keywords.xlsx'], 1):
        ix.cell(row=row, column=i, value=val).font = F
    ix.cell(row=row, column=2).hyperlink = f"#'New Prompt {bi}'!A1"
    ix.cell(row=row, column=2).font = Font(name=A, size=10, color='0563C1', underline='single')
out = ROOT / 'seo/Semrush_NewPerfumes_Prompts_2026-11-02.xlsx'
wb.save(out)
json.dump(B, open(ROOT / 'docs/seo/semrush_new_perfumes_batches_2026-11-02.json', 'w'), indent=1)
print(out, len(want), 'keywords,', len(B), 'batches; skipped as already checked:', sum(1 for r in rows for k in (r['primary'], r['secondary']) if k and k.lower() in done))

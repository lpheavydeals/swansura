"""Semrush prompts for the 39 'Others' products in the ranked sheet (user, 10 Nov 2026: 'Do the Semrush prompts for the
39 Others products'): Highborn London, anatomē, Shiseido, Coach, Acqua di Parma body care and Swansura Selection skincare.
Per product a main keyword (brand + product name) and a second, general product-type keyword (the term a page could
target if the branded one has no volume), plus brand terms. Keywords already in 'Semrush Data' or the 2 Nov / 10 Nov
results are left out. Same Claude-in-Chrome prompt format as tools/keywords/nov8_products_prompts.py.
Exports: Others_Batch_N_UK_keywords.xlsx. Run: python3 tools/keywords/others_prompts.py
"""
import json, csv, pathlib, openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
ROOT = pathlib.Path(__file__).resolve().parents[2]
BRAND = ['highborn london', 'highborn london skincare', 'anatome', 'anatome sleep', 'shiseido', 'shiseido skincare',
         'coach perfume', 'acqua di parma', '24k gold face mask']
P = [  # (product as in the ranked sheet, brand, main keyword, second keyword)
 ('24K Gold Hydrating Face Mask', 'Swansura Selection', '24k gold hydrating face mask', 'gold face mask'),
 ('Acqua di Parma Colonia Essenza Deodorant Stick 75ml', 'Acqua di Parma', 'acqua di parma colonia essenza deodorant', 'acqua di parma deodorant stick'),
 ('Bakuchiol Youth Elixir', 'Highborn London', 'highborn bakuchiol youth elixir', 'bakuchiol serum'),
 ('Bath & Shower Oil Somali Frankincense', 'anatomē', 'anatome bath and shower oil', 'frankincense bath oil'),
 ('Bath & Shower Oil with Roman Chamomile & Cornish Lavender', 'anatomē', 'anatome chamomile bath oil', 'lavender bath oil'),
 ('Botanical Balm', 'anatomē', 'anatome botanical balm', 'botanical balm'),
 ('Caviar Serum with 24K Gold', 'Swansura Selection', 'caviar serum 24k gold', 'caviar serum'),
 ('Cleanse and Tone Pack', 'Highborn London', 'highborn cleanse and tone', 'cleanser and toner set'),
 ('Coach Green Shower Gel 100ml', 'Coach', 'coach green shower gel', 'coach green'),
 ('Crystal Cleanser (100ml)', 'Highborn London', 'highborn crystal cleanser', 'luxury face cleanser'),
 ('Diamond Toner (100ml)', 'Highborn London', 'highborn diamond toner', 'diamond toner'),
 ('Four Phase Day and Night', 'Highborn London', 'highborn four phase day and night', 'day and night skincare set'),
 ('GLOWGUARD SPF30 Anti-Ageing Moisturiser', 'Highborn London', 'highborn glowguard spf30', 'moisturiser with spf 30'),
 ('Illuminating Rose-hip, Grape Seed & Avocado Face Oil', 'anatomē', 'anatome face oil', 'rosehip face oil'),
 ('Imperial Eye Gel', 'Highborn London', 'highborn imperial eye gel', 'eye gel'),
 ('Imperial Moisturiser', 'Highborn London', 'highborn imperial moisturiser', 'luxury moisturiser'),
 ('MOISTUREBURST Hydrating Glow Ceramide Serum', 'Highborn London', 'highborn moistureburst serum', 'ceramide serum'),
 ('Natural Luminosity Body Butter', 'Highborn London', 'highborn luminosity body butter', 'luxury body butter'),
 ('Natural Luminosity Scrub', 'Highborn London', 'highborn luminosity scrub', 'natural body scrub'),
 ('Night Elixir', 'Highborn London', 'highborn night elixir', 'night elixir'),
 ('Organic Age-Defying Facial Oil', 'Highborn London', 'highborn age defying facial oil', 'organic facial oil'),
 ('Organic Hydration Gel', 'Highborn London', 'highborn organic hydration gel', 'hydrating gel moisturiser'),
 ('Pre-Eminent Beauty Serum', 'Highborn London', 'highborn pre eminent beauty serum', 'beauty serum'),
 ('Relax + Sleep Chamomile Bath Salts', 'anatomē', 'anatome bath salts', 'chamomile bath salts'),
 ('Revive and Defy Starter Set', 'Highborn London', 'highborn revive and defy', 'skincare starter set'),
 ('Scrub and Glow Luminosity Set', 'Highborn London', 'highborn scrub and glow set', 'body scrub gift set'),
 ('Seven Phase Collection', 'Highborn London', 'highborn seven phase collection', 'luxury skincare set'),
 ('Shiseido Complete Cleansing Microfoam 180ml', 'Shiseido', 'shiseido complete cleansing microfoam', 'shiseido cleanser'),
 ('Shiseido Ultimune Power Infusing Concentrate 30ml', 'Shiseido', 'shiseido ultimune', 'shiseido ultimune power infusing concentrate'),
 ('Sleep Oil for an Overactive Mind | Somali Frankincense', 'anatomē', 'anatome sleep oil', 'sleep oil'),
 ('Sleep Oil for Restless Sleep | Roman Chamomile & Cornish Lavender', 'anatomē', 'anatome sleep oil chamomile', 'lavender sleep oil'),
 ('Sleep Pillow Spray | Roman Chamomile', 'anatomē', 'anatome pillow spray', 'pillow spray'),
 ('Somali Frankincense Sleep Pillow Spray | Overactive Mind', 'anatomē', 'anatome frankincense pillow spray', 'sleep pillow spray'),
 ('Superior Lip Butter (15ml)', 'Highborn London', 'highborn superior lip butter', 'lip butter'),
 ('Superior Lip Butter (Large 50ml)', 'Highborn London', 'highborn lip butter', 'lip butter'),
 ('The Gift of Good Sleep | Somali Frankincense', 'anatomē', 'anatome gift of good sleep', 'sleep gift set'),
 ('The Little Gift of Good Sleep - Frankincense | Overactive Mind', 'anatomē', 'anatome little gift of good sleep', 'sleep gift'),
 ('Ultimate Day & Night Moisture Set', 'Highborn London', 'highborn ultimate day and night moisture set', 'moisturiser gift set'),
 ('YOUTHBOOST Anti-Ageing Peptide Serum', 'Highborn London', 'highborn youthboost serum', 'peptide serum'),
]
assert len(P) == 39
kw = openpyxl.load_workbook(ROOT / 'seo/Swansura_Keyword_Research.xlsx', read_only=True)
done = {str(r[0]).strip().lower() for r in kw['Semrush Data'].iter_rows(min_row=2, values_only=True) if r[0]}
for f in ('docs/seo/semrush_new_perfumes_results_2026-11-02.csv', 'docs/seo/semrush_nov8_results_2026-11-10.csv'):
    done |= {r['keyword'].strip().lower() for r in csv.DictReader(open(ROOT / f))}
want, seen, skipped = [], set(), []
def add(k):
    k = ' '.join(k.split()).lower()
    if k in done: skipped.append(k)
    elif k not in seen: seen.add(k); want.append(k)
for b in BRAND: add(b)
for _, _, a, b in P: add(a); add(b)
B = [want[i:i + 100] for i in range(0, len(want), 100)]
A = 'Arial'; F = Font(name=A, size=10)
wb = Workbook(); ix = wb.active; ix.title = 'Index'
ix['A1'] = 'Semrush prompts: the 39 Others products'; ix['A1'].font = Font(name=A, bold=True, size=13)
ix['A2'] = (f'{len(want)} keywords in {len(B)} batch(es) for the 39 products on the Others tab (Highborn London, anatomē, Shiseido, Coach, '
            'Acqua di Parma, Swansura Selection): a main keyword (brand + product) and a general product-type keyword per product, plus brand terms. '
            f'{len(skipped)} keywords already checked earlier are left out (their volumes are already known).')
ix['A3'] = 'How to use: open an "Others Prompt" tab, click the column A header, copy and paste into the Claude in Chrome side panel with Semrush open.'
ix['A4'] = 'Then upload the export (Others_Batch_N_UK_keywords.xlsx) or screenshots to the Claude Code session.'
for c in ('A2', 'A3', 'A4'):
    ix[c].font = F; ix[c].alignment = Alignment(wrap_text=True)
ix.column_dimensions['A'].width = 18; ix.column_dimensions['B'].width = 18; ix.column_dimensions['E'].width = 34
for i, h in enumerate(['Prompt', 'Tab', 'Keywords', 'Status', 'Export file name', 'Keywords with data', 'Notes'], 1):
    ix.cell(row=6, column=i, value=h).font = Font(name=A, size=10, bold=True)
for bi, batch in enumerate(B, 1):
    ws = wb.create_sheet(f'Others Prompt {bi}'); ws.column_dimensions['A'].width = 120
    lines = [f'Task: get UK search volumes for a keyword list in Semrush (Others products, Batch {bi} of {len(B)}).', None, 'Steps:',
             '1. In this Semrush tab, open SEO > Keyword Overview.',
             '2. Set the database to United Kingdom (UK flag) before analysing. Do not use any other country.',
             '3. Paste the keyword list below into the Keyword Overview box (bulk analysis, one keyword per line) and click Analyze / Search.',
             f'4. When the results table loads, use Export > Excel (.xlsx) to download the results for all keywords. Keep the default columns. Save it as Others_Batch_{bi}_UK_keywords.xlsx.',
             '5. Tell me: the downloaded file name, how many keywords returned data, and any keywords Semrush rejected.', None, 'Rules:',
             '- Do not change account settings, buy anything, start a trial or upgrade the plan.',
             '- If Semrush shows a limit, captcha, login prompt or an "upgrade" message, stop and tell me instead of working around it.',
             '- Do not add, remove or edit keywords in the list.', None, f'Keywords (Others products, Batch {bi}):'] + batch
    for j, v in enumerate(lines, 1):
        ws.cell(row=j, column=1, value=v).font = F
    row = 6 + bi
    for i, val in enumerate([f'Others Prompt {bi}', f'Others Prompt {bi}', len(batch), 'To do', f'Others_Batch_{bi}_UK_keywords.xlsx'], 1):
        ix.cell(row=row, column=i, value=val).font = F
    ix.cell(row=row, column=2).hyperlink = f"#'Others Prompt {bi}'!A1"
    ix.cell(row=row, column=2).font = Font(name=A, size=10, color='0563C1', underline='single')
km = wb.create_sheet('Keyword map'); km.append(['Product', 'Brand', 'Main keyword', 'Second keyword', 'Already checked'])
for t, b, a, s in P:
    km.append([t, b, a, s, ', '.join(k for k in (a, s) if k in done)])
for c, w in zip('ABCDE', [62, 20, 44, 40, 30]): km.column_dimensions[c].width = w
for r in km.iter_rows():
    for c in r: c.font = Font(name=A, size=10, bold=c.row == 1)
out = ROOT / 'seo/Semrush_Others_Prompts_2026-11-10.xlsx'; wb.save(out)
json.dump(dict(batches=B, brand_terms=BRAND, products=[dict(title=t, brand=b, primary=a, secondary=s) for t, b, a, s in P], already_checked=skipped),
          open(ROOT / 'docs/seo/semrush_others_batches_2026-11-10.json', 'w'), indent=1, ensure_ascii=False)
print(out, len(want), 'keywords,', len(B), 'batches; already checked:', skipped)

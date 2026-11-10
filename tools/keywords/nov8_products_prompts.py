"""Semrush prompts for the 129 fragrances added 8 Nov 2026 (same format as New/Tier 3 prompts).

Keywords per product: primary = brand + perfume name, secondary = primary + concentration
(gift/mini/travel sets: one 'gift set' / 'miniature set' term, no secondary), plus one
'<brand> perfume' term per brand. Anything already in 'Semrush Data' or the 2 Nov results is skipped.
Titles come from the live store (Admin product pages dir as argv[1]). Exports: Nov8_Batch_N_UK_keywords.xlsx
Run: python3 tools/keywords/nov8_products_prompts.py <dir with p*.json>
"""
import json, glob, re, sys, csv, unicodedata, pathlib, openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
ROOT = pathlib.Path(__file__).resolve().parents[2]
N = json.load(open(ROOT / 'docs/seo/sheet_nov8_products_2026-11-08.json'))
BR = {p['brand'] for p in N}
live = [p for f in sorted(glob.glob(sys.argv[1] + '/p*.json')) for p in json.load(open(f))['data']['products']['nodes'] if p['vendor'] in BR]
kw = openpyxl.load_workbook(ROOT / 'seo/Swansura_Keyword_Research.xlsx', read_only=True)
done = {str(r[0]).strip().lower() for r in kw['Semrush Data'].iter_rows(min_row=2, values_only=True) if r[0]}
done |= {r['keyword'].lower() for r in csv.DictReader(open(ROOT / 'docs/seo/semrush_new_perfumes_results_2026-11-02.csv'))} if 'keyword' in open(ROOT / 'docs/seo/semrush_new_perfumes_results_2026-11-02.csv').readline().lower() else set()

def asc(s): return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
CONC = [('elixir de parfum', 'elixir de parfum'), ('eau de parfum extrême', 'eau de parfum extreme'), ('eau de parfum intense', 'eau de parfum intense'),
        ('eau de parfum fraîche', 'eau de parfum fraiche'), ('eau de toilette intense', 'eau de toilette intense'),
        ('eau de parfum', 'eau de parfum'), ('eau de toilette', 'eau de toilette'), ('cologne intense', 'cologne intense'), ('parfum spray', 'parfum'), ('parfum', 'parfum')]
OVR = {  # title -> (primary, secondary) where the rule gives a poor search term
 'Mugler Cologne Blow It Up Eau de Toilette 10ml': ('mugler cologne blow it up', None),
 'Mugler Cologne Fly Away Eau de Toilette 10ml': ('mugler cologne fly away', None),
 'Mugler Cologne Heal Your Mind Eau de Toilette 10ml': ('mugler cologne heal your mind', None),
 'Mugler Cologne Love You All Eau de Toilette 10ml': ('mugler cologne love you all', None),
 'Lacoste L\'Homme Lacoste Deodorant Stick 70g': ("l'homme lacoste deodorant stick", "l'homme lacoste"),
 'Ralph Lauren Polo Cologne Intense 59ml': ('polo cologne intense', 'ralph lauren polo cologne intense'),
 'Superdry Real Fragrance 01 Feminin Eau de Toilette 100ml': ('superdry 01 feminin', None),
 'Superdry Real Fragrance 02 Feminin Eau de Toilette 100ml': ('superdry 02 feminin', None),
 'Superdry Real Fragrance 02 Masculin Eau de Toilette 100ml': ('superdry 02 masculin', None),
 'Roberto Cavalli Just Cavalli Eau de Toilette for Her 30ml': ('just cavalli for her', 'just cavalli eau de toilette'),
 'Thomas Kosmala No. 4 Après l\'Amour Parfum & Hair Mist Travel Kit 30ml + 30ml': ('thomas kosmala apres l\'amour', 'kosmala no 4 apres l\'amour'),
 'Paco Rabanne Miniature Eau de Parfum Set 8 x 2ml': ('paco rabanne miniature set', None),
 'Paco Rabanne Men\'s Miniature Eau de Toilette Set (1 Million, Invictus, Phantom) 3 x 4ml': ('paco rabanne mini set men', None),
 'Paco Rabanne Men\'s Miniature Set (Phantom, Invictus, 1 Million Elixir, 1 Million) 4 x 5ml': ('paco rabanne miniature set men', None),
 'Paco Rabanne Women\'s Miniature Eau de Parfum Gift Set (Lady Million, Olympéa) 4 x 10ml': ('paco rabanne miniature set women', None),
 'Paco Rabanne Women\'s Miniature Set (Lady Million, Olympéa, Fame) 5ml + 6ml + 4ml + 4ml': ('paco rabanne mini set women', None),
 'Lanvin Mon Éclat Eau de Parfum Mini with Pouch 7.5ml': ('lanvin mon eclat', 'lanvin mon eclat eau de parfum'),
}
BRANDKW = {'Salvatore Ferragamo': 'ferragamo perfume', 'Narciso Rodriguez': 'narciso rodriguez perfume', 'Thomas Kosmala': 'thomas kosmala perfume', 'Grès': 'gres perfume'}
def split(t):
    pr, se = _split(t)
    pr = pr.replace('no. ', 'no '); se = se.replace('no. ', 'no ') if se else se
    m = re.match(r'salvatore ferragamo tuscan creations (.+)', pr)
    if m: se = 'ferragamo ' + m.group(1)   # people search the short form
    return pr, se
def _split(t):
    if t in OVR: return OVR[t]
    a = asc(t)
    if re.search(r'gift set|travel set| set\b|travel kit', a):
        base = re.split(r' eau de| parfum|&| gift set| travel set| set', a)[0].strip()
        return (base + ' gift set', None)
    for c, cn in CONC:
        cc = asc(c)
        if cc in a:
            base = a.split(cc)[0].strip()
            base = re.sub(r'\b(miniature|mini|refillable|refillable star)\b', '', base).strip()
            return (base, base + ' ' + cn)
    return (re.sub(r'\s+\d+(\.\d+)?ml.*', '', a).strip(), None)

want, seen, prod = [], set(), []
def add(k):
    k = ' '.join(str(k or '').replace('–', ' ').split()).lower()
    if k and k not in seen and k not in done:
        seen.add(k); want.append(k)
for b in sorted(BR): add(BRANDKW.get(b, asc(b) + ' perfume'))
for p in sorted(live, key=lambda p: p['title']):
    pr, se = split(p['title']); prod.append(dict(title=p['title'], handle=p['handle'], brand=p['vendor'], primary=pr, secondary=se))
    add(pr); add(se)
B = [want[i:i + 100] for i in range(0, len(want), 100)]
A = 'Arial'; F = Font(name=A, size=10)
wb = Workbook(); ix = wb.active; ix.title = 'Index'
ix['A1'] = 'Semrush prompts: fragrances added 8 Nov 2026'; ix['A1'].font = Font(name=A, bold=True, size=13)
ix['A2'] = f'{len(want)} keywords in {len(B)} batches: the main keyword (brand + perfume name) and the concentration variant of each of the {len(prod)} fragrances added on 8 Nov 2026 (gift and miniature sets: one set keyword), plus one "<brand> perfume" term per brand. Keywords already checked earlier are left out.'
ix['A3'] = 'How to use: open a "Nov8 Prompt" tab, click the column A header, copy and paste into the Claude in Chrome side panel with Semrush open. One prompt at a time.'
ix['A4'] = 'Then upload the exports (Nov8_Batch_N_UK_keywords.xlsx) or screenshots to the Claude Code session.'
for c in ('A2', 'A3', 'A4'):
    ix[c].font = F; ix[c].alignment = Alignment(wrap_text=True)
for i, h in enumerate(['Prompt', 'Tab', 'Keywords', 'Status', 'Export file name', 'Keywords with data', 'Notes'], 1):
    ix.cell(row=6, column=i, value=h).font = Font(name=A, size=10, bold=True)
ix.column_dimensions['A'].width = 18; ix.column_dimensions['B'].width = 16; ix.column_dimensions['E'].width = 32
for bi, batch in enumerate(B, 1):
    ws = wb.create_sheet(f'Nov8 Prompt {bi}'); ws.column_dimensions['A'].width = 120
    lines = [f'Task: get UK search volumes for a keyword list in Semrush (8 Nov fragrances, Batch {bi} of {len(B)}).', None, 'Steps:',
             '1. In this Semrush tab, open SEO > Keyword Overview.',
             '2. Set the database to United Kingdom (UK flag) before analysing. Do not use any other country.',
             '3. Paste the keyword list below into the Keyword Overview box (bulk analysis, one keyword per line) and click Analyze / Search.',
             f'4. When the results table loads, use Export > Excel (.xlsx) to download the results for all keywords. Keep the default columns. Save it as Nov8_Batch_{bi}_UK_keywords.xlsx.',
             '5. Tell me: the downloaded file name, how many keywords returned data, and any keywords Semrush rejected.', None, 'Rules:',
             '- Do not change account settings, buy anything, start a trial or upgrade the plan.',
             '- If Semrush shows a limit, captcha, login prompt or an "upgrade" message, stop and tell me instead of working around it.',
             '- Do not add, remove or edit keywords in the list.', None, f'Keywords (8 Nov fragrances, Batch {bi}):'] + batch
    for j, v in enumerate(lines, 1):
        ws.cell(row=j, column=1, value=v).font = F
    row = 6 + bi
    for i, val in enumerate([f'Nov8 Prompt {bi}', f'Nov8 Prompt {bi}', len(batch), 'To do', f'Nov8_Batch_{bi}_UK_keywords.xlsx'], 1):
        ix.cell(row=row, column=i, value=val).font = F
    ix.cell(row=row, column=2).hyperlink = f"#'Nov8 Prompt {bi}'!A1"
    ix.cell(row=row, column=2).font = Font(name=A, size=10, color='0563C1', underline='single')
km = wb.create_sheet('Keyword map'); km.append(['Product', 'Brand', 'Main keyword', 'Second keyword'])
for p in prod: km.append([p['title'], p['brand'], p['primary'], p['secondary']])
for c, w in zip('ABCD', [70, 20, 45, 50]): km.column_dimensions[c].width = w
out = ROOT / 'seo/Semrush_Nov8_Prompts_2026-11-10.xlsx'
wb.save(out)
json.dump(dict(batches=B, products=prod), open(ROOT / 'docs/seo/semrush_nov8_batches_2026-11-10.json', 'w'), indent=1, ensure_ascii=False)
print(out, len(want), 'keywords,', len(B), 'batches')

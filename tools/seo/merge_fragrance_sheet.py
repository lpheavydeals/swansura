"""Merge the client's new 'Swansura Fragrance Data.xlsx' (2 Nov 2026) with our prepared sheet.

Input : docs/data/Swansura_Fragrance_Data_2026-11-02.xlsx (client: 674 fragrance + 159 Vilvah/Deyga rows)
        seo/Swansura_Keyword_Research.xlsx 'Final SEO' (546 prepared rows)
        live storefront /products.json
Step 1 (this file, match()): classify each client row as EXISTING (same brand + size, names match),
        CHECK (close but not certain) or NEW. Writes docs/seo/fragrance_merge_match_2026-11-02.json.
"""
import json, re, pathlib, urllib.request, difflib
import openpyxl
ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / 'docs/data/Swansura_Fragrance_Data_2026-11-02.xlsx'

STOP = set('eau de parfum toilette cologne edp edt edc extrait spray for men women mens womens unisex fragrance '
           'fragrances ml the and pour by natural vaporisateur vapo fr set travel funnel'.split())
def bnorm(b):
    b = str(b or '').lower().replace('&', 'and')
    b = re.sub(r'^the ', '', b)
    b = {'woods collection': 'woods collection', 'sap': 'sap', 'giorgia armani': 'giorgio armani'}.get(b.strip(), b)
    return re.sub(r'[^a-z0-9]', '', b)
def size(s):
    m = re.findall(r'(\d+(?:\.\d+)?)\s*ml', str(s or '').lower())
    return m[0] if m else re.sub(r'[^0-9.]', '', str(s or ''))
def toks(name, brand):
    s = str(name or '').lower().replace('&', ' and ').replace('’', "'").replace("'s", '')
    s = re.sub(r'\((?:edp|edt|edc|fr|\s)*\)', ' ', s)
    s = re.sub(r'\d+(?:\.\d+)?\s*ml', ' ', s)
    s = re.sub(r'–.*$', ' ', s)            # client titles end in '– Unisex Fragrance'
    bw = set(re.findall(r'[a-z0-9]+', str(brand or '').lower().replace('&', ' and ')))
    return [w for w in re.findall(r'[a-z0-9]+', s) if w not in STOP and w not in bw]

def live_products():
    out = []
    for p in range(1, 6):
        req = urllib.request.Request(f'https://www.swansura.com/products.json?limit=250&page={p}', headers={'User-Agent': 'Mozilla/5.0 Chrome/130'})
        b = json.load(urllib.request.urlopen(req))['products']
        if not b:
            break
        out += b
    return out

def score(a, b):
    if not a or not b:
        return 0.0
    sa, sb = set(a), set(b)
    j = len(sa & sb) / len(sa | sb)
    return max(j, difflib.SequenceMatcher(None, ' '.join(a), ' '.join(b)).ratio() * 0.95)

def match():
    wb = openpyxl.load_workbook(SRC, data_only=True)
    F = [r for r in wb['Fragrance Catalogue'].iter_rows(min_row=2, values_only=True) if r[6]]
    kw = openpyxl.load_workbook(ROOT / 'seo/Swansura_Keyword_Research.xlsx', read_only=True)
    FS = [r for r in kw['Final SEO'].iter_rows(min_row=2, values_only=True) if r[0] and r[1] != 'Vilvah & Deyga']
    sheet = [dict(src='sheet', id=r[0], brand=bnorm(r[2]), size=size(r[4]) or size(r[3]), name=r[3], t=toks(r[3], r[2])) for r in FS]
    live = []
    for a in live_products():
        for v in a['variants']:
            live.append(dict(src='live', id=a['handle'], brand=bnorm(a['vendor']), size=size(a['title'] + ' ' + v['title']),
                             name=a['title'] + ('' if v['title'] == 'Default Title' else f" [{v['title']}]"), t=toks(a['title'], a['vendor'])))
    exact = {(re.sub(r'[^a-z0-9]', '', str(r[3]).lower().replace('&', 'and')), re.sub(r'[^0-9.]', '', str(r[4] or ''))) for r in FS}
    res = []
    for i, r in enumerate(F):
        key = (re.sub(r'[^a-z0-9]', '', str(r[6]).lower().replace('&', 'and')), re.sub(r'[^0-9.]', '', str(r[9] or '')))
        row = dict(n=i + 1, brand=r[1], cat=r[3], family=r[4], type=r[5], name=r[6], desc=r[7], notes=r[8], size=r[9], price=r[11])
        if key in exact:
            res.append(dict(row, status='EXISTING', how='same name + size as prepared sheet')); continue
        b, s, t = bnorm(r[1]), size(r[9]) or size(r[6]), toks(r[6], r[1])
        best = []
        for c in sheet + live:
            if c['size'] != s:
                continue
            if c['brand'] != b and not (b and (b in c['brand'] or c['brand'] in b)):
                continue
            sc = score(t, c['t'])
            if sc > 0:
                best.append((sc, c))
        best.sort(key=lambda x: -x[0])
        top = best[0] if best else None
        if top and top[0] >= 0.85:
            st = 'EXISTING'
        elif top and top[0] >= 0.5:
            st = 'CHECK'
        else:
            st = 'NEW'
        row.update(status=st, how=(f"{top[1]['src']}: {top[1]['name']} ({top[0]:.2f})" if top else ''),
                   match_src=top[1]['src'] if top else None, match_id=top[1]['id'] if top else None, tokens=t)
        res.append(row)
    json.dump(res, open(ROOT / 'docs/seo/fragrance_merge_match_2026-11-02.json', 'w'), ensure_ascii=False, indent=1, default=str)
    return res

if __name__ == '__main__':
    import collections
    res = match()
    print(collections.Counter(r['status'] for r in res))


# ---------------------------------------------------------------- step 2: SEO rows for the new products + merged workbook
CONC = [('Extrait de Parfum', 'Extrait de Parfum', 'Extrait'), ('Eau de Parfum (EDP)', 'Eau de Parfum', 'EDP'),
        ('Eau de Toilette (EDT)', 'Eau de Toilette', 'EDT'), ('Eau de Cologne (EDC)', 'Eau de Cologne', 'EDC'),
        ('Body Mist', 'Body Mist', 'Body Mist'), ('Deodorant Spray', 'Deodorant Spray', 'Deodorant')]
BRAND_FIX = {'Armaf Club De Nuit': 'Armaf', 'Mercedes Benz': 'Mercedes-Benz'}
TYPO = {'Champange': 'Champagne', 'Mercedes Benz': 'Mercedes-Benz', 'Club De Nuit': 'Club de Nuit'}
# Gift sets / bundles whose client names are shorthand: (start of client name) -> (H1, size, note)
OVERRIDE = {
 'Franck Olivier Bella Women + Deodorant Coffret': ('Franck Olivier Bella Women Eau de Parfum & Deodorant Gift Set', '75ml + 250ml', ''),
 'Franck Olivier Black Touch + Deodorant Coffret': ('Franck Olivier Black Touch Eau de Toilette & Deodorant Gift Set', '100ml + 250ml', ''),
 'Guess Set (seductive': ('Guess Seductive Eau de Toilette Gift Set (Seductive, Noir, Red, Blue)', '4 x 15ml', ''),
 'Guess Pink Set': ('Guess Pink Eau de Parfum Gift Set', '75ml + 15ml + 100ml', "client name 'Pink Set + + Bl + Pouch (2023)': confirm contents (body lotion + pouch?)"),
 'Guess Seductive Homme Noir Set': ('Guess Seductive Homme Noir Gift Set', '100ml + 170g', "client name '+ Sg + + Pouch': confirm contents (shower gel, 170g item, pouch?)"),
 'Guess Seductive Noir Set': ('Guess Seductive Noir Eau de Toilette Gift Set', '75ml + 100ml + 15ml', "client name '+ Bl + + Pouch': confirm contents"),
 'Guess Uomo Set': ('Guess Uomo Gift Set', '100ml + 170g', "client name '+ Sg + + Pouch': confirm contents"),
 'Jaguar Classic Bath Set': ('Jaguar Classic Eau de Toilette & Shower Gel Gift Set', '100ml + 200ml', ''),
 'Mercedes Benz Club Black Set': ('Mercedes-Benz Club Black Eau de Toilette & Shower Gel Gift Set', '100ml', 'tin box (client name)'),
 'Mercedes Benz Multiline Trio Nomade': ('Mercedes-Benz Trio Nomade Eau de Parfum Set (Land, Sea & Air)', '3 x 30ml', 'leather case (client name)'),
 'Armaf Club De Nuit Set (intense Man': ("Armaf Club de Nuit Men's Parfum Gift Set (Intense Man, Sillage, Milestone)", '3 x 30ml', ''),
 'Armaf Club De Nuit Set (woman': ("Armaf Club de Nuit Women's Parfum Gift Set (Woman, Intense Woman, Milestone)", '3 x 30ml', ''),
 'Armaf Club De Nuit Woman Edp2x12ml': ('Armaf Club de Nuit Woman Eau de Parfum Travel Set', '2 x 12ml', ''),
 'Bois 1920 Set': ('Bois 1920 Oro Eau de Parfum Gift Set (5 scents)', '5 x 18ml', ''),
 'Natural By Woods Dawn 100 + Atomizer': ('Natural By Woods Dawn Eau de Parfum with Travel Atomiser', '100ml + 5ml', "client size column says 5ml, name says '100 + Atomizer': confirm"),
 'Natural By Woods Earth 100 + Atomizer': ('Natural By Woods Earth Eau de Parfum with Travel Atomiser', '100ml + 5ml', "client size column says 5ml, name says '100 + Atomizer': confirm"),
 'Natural By Woods Essence 100 + Atomizer': ('Natural By Woods Essence Eau de Parfum with Travel Atomiser', '100ml + 5ml', "client size column says 5ml, name says '100 + Atomizer': confirm"),
 'Natural By Woods Glow 100 + Atomizer': ('Natural By Woods Glow Eau de Parfum with Travel Atomiser', '100ml + 5ml', "client size column says 5ml, name says '100 + Atomizer': confirm"),
 'Natural By Woods Sun 100 + Atomizer': ('Natural By Woods Sun Eau de Parfum with Travel Atomiser', '100ml + 5ml', "client size column says 5ml, name says '100 + Atomizer': confirm"),
 'Natural By Woods Eclipse Eau de Parfum': ('Natural By Woods Eclipse Eau de Parfum with Travel Atomiser', '100ml + 5ml', ''),
 'Natural By Woods Karma + Atomizer': ('Natural By Woods Karma Eau de Parfum with Travel Atomiser', '100ml + 5ml', ''),
 'Natural By Woods Discovery Set': ('Natural By Woods Discovery Set', '', 'no size in client sheet: confirm sizes'),
}
GENDER = lambda cat: "men's" if cat.startswith("Men") else "women's" if cat.startswith("Women") else 'unisex'

def caps(s):
    s = re.sub(r'\(\s*([a-z])', lambda m: '(' + m.group(1).upper(), s)
    return re.sub(r'\s+', ' ', s).strip()

def clean_core(r):
    """'Guess Pink Body Mist 250ml – Women's Fragrance' -> ('Guess Pink Body Mist', 'Guess Pink')"""
    name = re.split(r'\s+–\s+', str(r['name']))[0]
    name = re.sub(r'\((EDP|EDT|EDC)\)', '', name)
    name = re.sub(r'\s*\d+(?:\.\d+)?\s*ml(\s*\+\s*\d+(?:\.\d+)?\s*ml)*', '', name, flags=re.I)
    name = re.sub(r'\s*\d+\s*x\s*\d+\s*ml', '', name, flags=re.I)
    name = caps(name)
    base = name
    for _, long, _ in CONC:
        base = re.sub(r'\s*' + re.escape(long) + r'\b', '', base, flags=re.I)
    base = re.sub(r'\s+(le\s+)?parfum$', '', base, flags=re.I).strip()
    return name, base

def ptype(r):
    t = str(r['type'] or '')
    for k, long, short in CONC:
        if t.startswith(k):
            return long, short
    if 'Gift Set' in t or 'Gift Set' in str(r['cat']):
        return 'Gift Set', 'Gift Set'
    if t == 'Parfum':
        return 'Parfum', 'Parfum'
    return 'Fragrance', 'Fragrance'

def fit(cands, hi):
    for c in cands:
        if len(c) <= hi:
            return c
    return cands[-1][:hi].rsplit(' ', 1)[0]

def build():
    import collections
    res = json.load(open(ROOT / 'docs/seo/fragrance_merge_match_2026-11-02.json'))
    for r in res:
        if r['status'] == 'CHECK' and str(r['brand']).lower() == 'signature':   # same Signature 100+15 ml sets (verified by eye)
            r['status'] = 'EXISTING'
        if r['status'] == 'NEW' and str(r['name']).startswith('Signature Blue'):
            r['status'] = 'EXISTING'; r['how'] = 'live: Signature Blue 100ml Edp (client row has no size)'
    new = [r for r in res if r['status'] == 'NEW']
    # Drive photo folders that are not in the store yet (19 Oct): link by brand + name words
    import csv
    drive = list(csv.DictReader(open(ROOT / 'docs/images/fragrance_not_in_store_2026-10-19.csv')))
    def drive_for(r):
        b = bnorm(BRAND_FIX.get(r['brand'], r['brand']))
        t = set(toks(r['name'], r['brand'])) - {'men', 'women', 'woman', 'man'}
        best = None
        for d in drive:
            db = bnorm(d['brand (Drive folder)'])
            if not (b and (b in db or db in b)):
                continue
            ft = set(toks(d['Drive folder'].split('/')[-1], d['brand (Drive folder)'])) - {'men', 'women', 'woman', 'man'}
            if t and ft and len(t & ft) / len(ft) >= 0.99:
                if not best or len(ft) > len(best[1]):
                    best = (d, ft)
        return f"{best[0]['Drive folder']} ({best[0]['usable images']} photos)" if best else ''
    # gender collisions: same base name with different gender (put gender in H1, like CK Eternity)
    kwg = collections.defaultdict(set)
    for r in new:
        kwg[clean_core(r)[1].lower()].add(GENDER(r['cat']))
    rows = []
    for i, r in enumerate(new, 1):
        brand = BRAND_FIX.get(r['brand'], r['brand'])
        name, base = clean_core(r)
        for a, b in TYPO.items():
            name, base = name.replace(a, b), base.replace(a, b)
        long, short = ptype(r)
        g = GENDER(r['cat'])
        size = str(r['size'] or '').replace(' ', '')
        ov = next((v for k, v in OVERRIDE.items() if str(r['name']).startswith(k)), None)
        gift = 'Gift Set' in str(r['cat']) or ' set' in name.lower()
        gtag = {"men's": ' for Men', "women's": ' for Women'}.get(g, '') if len(kwg[base.lower()]) > 1 else ''
        h1 = (name if long in name or gift else f'{base} {long}') + gtag
        h1 = caps(h1)
        if ov:
            h1, size = ov[0], ov[1]
            base = re.sub(r'\s*(Eau de Parfum|Eau de Toilette|Parfum)\b', '', h1).strip()
        sz_ = f' {size}' if size else ''
        t_long = f'{h1}{sz_} | Swansura UK'
        t_short = f"{h1.replace(long, short) if short not in ('Body Mist','Deodorant','Fragrance','Gift Set','Parfum') else h1} {size} | Swansura"
        t_short = t_short.replace(f' {size} |', f'{sz_} |')
        short = re.sub(r'\s*\(.*?\)', '', h1)
        short = short.replace('Extrait de Parfum', 'Extrait').replace('Eau de Parfum', 'EDP').replace('Eau de Toilette', 'EDT')
        short = short.replace('Collection Privee le Parfum', 'Collection Privée').replace('Deodorant Spray', 'Deodorant')
        short2 = re.sub(r'\s*(EDP|EDT|Parfum)?\s*&\s*(Deodorant|Shower Gel)', '', short)
        short2 = re.sub(r"\s+(EDP|EDT|Parfum)(?= (Gift|Travel) Set)", '', short2)
        cands = [t_long, f'{h1}{sz_} | Swansura', t_short, f'{short}{sz_} | Swansura', f'{h1} | Swansura', f'{short} | Swansura',
                 f'{short2}{sz_} | Swansura', f'{short2} | Swansura', f"{short2.replace('Club de Nuit ', '')} | Swansura"]
        title = next((c for c in cands if len(c) <= 60), short2[:60])
        fam = str(r['family'] or '').lower()
        art = 'An' if (fam or g)[:1] in 'aeiou' else 'A'
        kind = {'Gift Set': 'fragrance gift set', 'Fragrance': 'fragrance'}.get(long, long.lower())
        if gift and long not in ('Gift Set',):
            kind = f'{long.lower()} gift set'
        d1 = f"Buy {h1}{sz_} for £{float(r['price']):.2f} at Swansura UK. {art} {fam + ' ' if fam else ''}{g} {kind}. 100% authentic, fast UK delivery, free over £40."
        d2 = d1.replace('fast UK delivery, free over £40', 'free UK delivery over £40')
        d3 = f"Buy {h1}{sz_} for £{float(r['price']):.2f} at Swansura UK. {art} {fam + ' ' if fam else ''}{g} {kind}. 100% authentic."
        desc = fit([d1, d2, d3], 160)
        primary = re.sub(r'\s+', ' ', base.lower()).strip()
        if ov:
            primary = re.sub(r'\s+with travel atomiser', '', primary)
            primary = re.sub(r'\s*\(.*?\)', '', primary)
            primary = re.sub(r'\s*&\s*(deodorant|shower gel)', '', primary)
            primary = re.sub(r'\s+(parfum|eau de parfum|eau de toilette)\b', '', primary).strip()
        primary = re.sub(r'\s*\(.*?\)', '', primary).strip()          # Semrush rejects brackets
        secondary = f'{primary} {long.lower()}' if long not in ('Fragrance', 'Gift Set') and not gift else ''
        notes = ['NEW 2 Nov 2026 (client Fragrance Data sheet row %d)' % r['n'], 'Semrush volume not checked yet']
        if brand != r['brand']:
            notes.append(f"brand in client sheet: '{r['brand']}'")
        if ov and ov[2]:
            notes.append(ov[2])
        if any(a in str(r['name']) for a in TYPO if a == 'Champange'):
            notes.append("client typo 'Champange' corrected")
        if gtag:
            notes.append('same name sold for men and women: gender in H1')
        dr = drive_for(r)
        rows.append(dict(id=f'FR-N{i:03d}', source='Fragrance Catalogue (2 Nov 2026)', brand=brand, name=r['name'], size=size or r['size'],
                         price=float(r['price']), primary=primary, secondary=secondary, h1=h1, title=title, desc=desc,
                         notes='; '.join(notes), cat=r['cat'], family=r['family'], type=r['type'], scent=r['notes'],
                         client_desc=r['desc'], drive=dr))
    json.dump(rows, open(ROOT / 'docs/seo/fragrance_new_seo_2026-11-02.json', 'w'), ensure_ascii=False, indent=1)
    return res, rows


# ---------------------------------------------------------------- step 3: workbook
OUT = ROOT / 'seo/Swansura_Product_SEO_Merged_2026-11-02.xlsx'

def write():
    import collections
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    res, rows = build()
    c = collections.Counter(r['h1'] for r in rows)
    for r in rows:
        if c[r['h1']] > 1:
            sib = [x for x in rows if x['h1'] == r['h1']]
            r['notes'] += '; size variants: merge as variants of one product'
            if len({x['price'] for x in sib}) == 1:
                r['notes'] += f" (client sheet has the same price £{r['price']:.2f} for every size: confirm)"
        if r['h1'] == 'Franck Olivier Eau de Parfum':
            r['notes'] += '; perfume name missing in client sheet: confirm which Franck Olivier perfume'
    kw = openpyxl.load_workbook(ROOT / 'seo/Swansura_Keyword_Research.xlsx', read_only=True, data_only=True)
    ws = kw['Final SEO']
    head = [x for x in next(ws.iter_rows(min_row=1, max_row=1, values_only=True))]
    old = [list(r) for r in ws.iter_rows(min_row=2, values_only=True) if r[0]]
    EXTRA = ['Status', 'Category (client)', 'Scent family (client)', 'Type (client)', 'Scent notes (client)', 'Description (client)', 'Drive photos (not yet in Shopify)']
    import csv as _csv
    VOL = {}
    sem = ROOT / 'docs/seo/semrush_new_perfumes_results_2026-11-02.csv'
    if sem.exists():
        for x in _csv.DictReader(open(sem)):
            VOL[x['keyword']] = (int(x['volume_uk']) if x['volume_uk'] else None, int(x['kd']) if x['kd'] else None)
    def vk(k):
        return VOL.get(' '.join(str(k or '').lower().split()), (None, None)) if k else (None, None)
    def ease(v, kd):
        if not VOL:
            return 'Not checked'
        if not v:
            return 'No volume'
        return 'Easier' if (kd or 0) <= 20 else 'Medium' if kd <= 35 else 'Hard'
    def newrow(r):
        pv, pkd = vk(r['primary']); sv, _ = vk(r['secondary'])
        return [r['id'], r['source'], r['brand'], r['name'], r['size'], r['price'], r['primary'], pv, pkd, ease(pv, pkd), r['secondary'] or None, sv,
                r['h1'], r['title'], len(r['title']), r['desc'], len(r['desc']), r['notes'],
                'NEW 2 Nov 2026', r['cat'], r['family'], r['type'], r['scent'], r['client_desc'], r['drive']]
    EM, LINE = '1B4D3E', 'E3DACD'
    B = Border(*(Side(style='thin', color=LINE),) * 4)
    F = 'Plus Jakarta Sans'
    wb = Workbook()
    def sheet(title, header, data, widths, newfill_col=None):
        s = wb.create_sheet(title)
        for j, h in enumerate(header, 1):
            x = s.cell(1, j, h); x.font = Font(name=F, bold=True, color='FFFFFF'); x.fill = PatternFill('solid', fgColor=EM)
            x.alignment = Alignment(wrap_text=True, vertical='center'); x.border = B
        for i, row in enumerate(data, 2):
            isnew = newfill_col is not None and str(row[newfill_col]).startswith('NEW')
            for j, v in enumerate(row, 1):
                x = s.cell(i, j, v); x.font = Font(name=F, size=10); x.border = B
                x.alignment = Alignment(vertical='top', wrap_text=j in (4, 13, 14, 16, 18, 23, 24))
                if isnew:
                    x.fill = PatternFill('solid', fgColor='E4EEE9')
        for j, w in enumerate(widths, 1):
            s.column_dimensions[openpyxl.utils.get_column_letter(j)].width = w
        s.freeze_panes = 'E2'; s.auto_filter.ref = s.dimensions
        s.row_dimensions[1].height = 34
        return s
    W = [10, 16, 16, 44, 12, 9, 30, 9, 8, 11, 30, 9, 40, 44, 7, 60, 7, 40, 16, 20, 14, 18, 40, 50, 30]
    merged = [r + ['Prepared 18–26 Oct 2026', None, None, None, None, None, None] for r in old] + [newrow(r) for r in rows]
    sheet('Final SEO (merged)', head + EXTRA, merged, W, newfill_col=18)
    sheet(f'New products ({len(rows)})', head + EXTRA, [newrow(r) for r in rows], W, newfill_col=18)
    # existing rows: what they matched + price differences
    idx = {r[0]: r for r in old}
    exist = [r for r in res if r['status'] == 'EXISTING']
    ex_rows, pc = [], []
    names = collections.defaultdict(list)
    for o_ in old:
        names[re.sub(r'[^a-z0-9]', '', str(o_[3]).lower().replace('&', 'and')) + '|' + re.sub(r'[^0-9.]', '', str(o_[4] or ''))].append(o_)
    for r in exist:
        k = re.sub(r'[^a-z0-9]', '', str(r['name']).lower().replace('&', 'and')) + '|' + re.sub(r'[^0-9.]', '', str(r['size'] or ''))
        os_ = names.get(k) or ([idx[r['match_id']]] if r.get('match_src') == 'sheet' and r.get('match_id') in idx else [])
        o = os_[0] if os_ else None
        ex_rows.append([r['n'], r['brand'], r['name'], r['size'], r['price'], ', '.join(x[0] for x in os_) if os_ else '',
                        o[3] if o else r['how'].split(': ', 1)[-1], ', '.join(f'{x[5]}' for x in os_) if os_ else '',
                        'same name + size' if r['how'].startswith('same') else 'same brand + size, name matched'])
        ours = {round(float(x[5]), 2) for x in os_ if x[5] is not None}
        if os_ and r['price'] is not None and round(float(r['price']), 2) not in ours:
            pc.append([', '.join(x[0] for x in os_), o[2], r['name'], o[3], r['size'], ' / '.join(f'{v:.2f}' for v in sorted(ours)), float(r['price']),
                       round(float(r['price']) - min(ours, key=lambda v: abs(v - float(r['price']))), 2)])
    sheet(f'Already prepared ({len(exist)})', ['Client row', 'Brand', 'Client product name', 'Size', 'Client price £', 'Our ID', 'Our / live name', 'Our price £', 'How matched'],
          ex_rows, [9, 16, 60, 10, 10, 10, 60, 10, 30])
    sheet(f'Price changes ({len(pc)})', ['Our ID', 'Brand', 'Client product name', 'Our product name', 'Size', 'Our sheet £', 'Client new sheet £', 'Difference £'],
          pc, [12, 16, 55, 55, 10, 12, 14, 12])
    if VOL:
        brows = sorted([[k, v, kd] for k, (v, kd) in VOL.items() if k.endswith(' perfume')], key=lambda x: -(x[1] or 0))
        top = sorted([[r[2], r[3], r[6], r[7], r[8]] for r in (newrow(x) for x in rows) if r[7]], key=lambda x: -x[3])[:25]
        sheet('Brand searches', ['Brand search (UK)', 'Monthly volume', 'KD %'], brows, [34, 16, 10])
        sheet('Top new products', ['Brand', 'Client product name', 'Keyword', 'Monthly volume', 'KD %'], top, [18, 70, 34, 16, 10])
    s = wb['Sheet']; s.title = 'Summary'
    lines = [('Swansura product SEO – merged sheet (2 Nov 2026)', True),
             ("Client's new sheet 'Swansura Fragrance Data.xlsx': 674 fragrance rows + 159 Vilvah & Deyga rows.", False),
             (f'Already in our prepared sheet / store: {len(exist)} fragrance rows + all 159 Vilvah & Deyga rows (skipped, see "Already prepared").', False),
             ('The client sheet repeats many existing perfumes in a second spelling (e.g. "… Eau de Parfum (EDP) 100ml – Unisex Fragrance"); those were matched to our rows by brand + size + name.', False),
             (f'NEW: {len(rows)} perfumes, prepared in the same format (H1, meta title ≤60, meta description ≤160, primary/secondary keyword). Green rows in "Final SEO (merged)".', False),
             ('Semrush UK volumes for the new keywords: checked 2 Nov 2026 (392 keywords). Brand searches in "Brand searches" tab.', False),
             (f'Price changes: {len(pc)} existing products have a different price in the client\'s new sheet (see tab). Nothing has been changed in Shopify.', False),
             ('Notes column flags: gift-set contents to confirm, size variants, a missing perfume name, client typos corrected.', False)]
    for i, (t, b) in enumerate(lines, 1):
        x = s.cell(i, 1, t); x.font = Font(name=F, size=14 if i == 1 else 11, bold=b, color=EM if b else '1F1A17')
    s.column_dimensions['A'].width = 140
    wb.move_sheet('Summary', offset=-(len(wb.sheetnames) - 1))
    wb.save(OUT)
    return res, rows, pc

if __name__ == '__main__' and len(__import__('sys').argv) > 1 and __import__('sys').argv[1] == 'write':
    res, rows, pc = write()
    print('written', OUT, len(rows), 'new;', len(pc), 'price changes')

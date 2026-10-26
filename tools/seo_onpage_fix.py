"""On-page SEO fix (26 Oct 2026): product H1s, Vilvah/Deyga keyword corrections, long titles.

Reads prototype/products.json + seo/Swansura_Keyword_Research.xlsx ('Final SEO'), writes:
  - products.json: h1 (all products), st/sd corrected for Vilvah/Deyga rows whose keyword
    did not describe the product, kw (primary keyword used on the page)
  - docs/seo/onpage_changes_2026-10-26.csv: every change, for the theme / client
Run from the repo root:  python3 tools/seo_onpage_fix.py
"""
import json, re, csv, openpyxl, os

P = json.load(open('prototype/products.json'))
wb = openpyxl.load_workbook('seo/Swansura_Keyword_Research.xlsx', read_only=True, data_only=True)
rows = list(wb['Final SEO'].iter_rows(values_only=True)); H = rows[0]; ix = {h: i for i, h in enumerate(H)}
bd = {r[ix['FINAL meta description']].strip(): r for r in rows[1:] if r[ix['FINAL meta description']]}
bt = {r[ix['FINAL meta title']].strip(): r for r in rows[1:] if r[ix['FINAL meta title']]}

def norm(s): return re.sub(r'[^a-z0-9 ]+', ' ', s.lower().replace('é', 'e').replace('ē', 'e').replace('è', 'e').replace('à', 'a')).split()
STOP = {'the', 'and', 'of', 'for', 'a', 'to', 'in', 'with', 'uk', 'de'}
def has(t, k):
    T = set(norm(t)); T |= {w.rstrip('s') for w in T}
    return all(w in T or w.rstrip('s') in T for w in norm(k) if w not in STOP)
def fit(*parts, n=60):
    for i in range(len(parts), 0, -1):
        s = ' | '.join(parts[:i])
        if len(s) <= n: return s
    return parts[0][:n].rsplit(' ', 1)[0]

# Vilvah/Deyga rows: (keyword fits the product?) -> new H1 / keyword / type phrase for the description.
# Rows not listed keep their Final SEO H1 and keyword. FOR = append "for <x>" to the H1, DASH = "H1 – Keyword".
FIX = {
 # keyword fits: add it to the H1 (and title when missing)
 'Deyga Activated Charcoal Body Wash': ('Deyga Activated Charcoal Natural Body Wash', None, None),
 'Deyga Wild Berry Body Wash': ('Deyga Wild Berry Natural Body Wash', None, None),
 'Vilvah Goat Milk Body Wash': ('Vilvah Goat Milk Natural Body Wash', None, None),
 'Vilvah Goat Milk Shampoo': ('Vilvah Goat Milk Natural Shampoo', None, None),
 'Deyga Rice Water Shampoo': ('Deyga Rice Water Natural Shampoo', None, None),
 'Deyga Sunscreen': ('Deyga Natural Sunscreen', None, None),
 'Deyga Deep Moisturising Face Cream': ('FOR', None, None), 'Deyga Light Moisturising Face Cream': ('FOR', None, None),
 'Vilvah Ultra Moisturising Cream': ('FOR', None, None),
 'Deyga Vitamin C Foaming Face Wash': ('FOR', None, None), 'Deyga Charcoal Face Wash': ('FOR', None, None),
 'Vilvah Milk Powder Face Wash': ('FOR', None, None), 'Deyga Oat Milk Face Wash': ('FOR', None, None),
 'Vilvah Cream Face Wash (Fragrance Free)': ('Vilvah Cream Face Wash for Dry Skin (Fragrance Free)', None, None),
 'Deyga Tea Tree Facial Toner': ('FOR', None, None), 'Deyga Pure Rose Water Toner': ('FOR', None, None),
 'Vilvah Milk Face Toner': ('FOR', None, None), 'Vilvah Rosewater Facial Toner': ('FOR', None, None),
 'Deyga Almond Milk Body Lotion': ('FOR', None, None), 'Vilvah Milk Body Lotion': ('FOR', None, None),
 'Vilvah Anti-Frizz Hair Serum': ('Vilvah Anti-Frizz Hair Serum for Frizzy Hair', None, None),
 'Vilvah Goat Milk Hair Mask': ('FOR', None, None),
 'Deyga Beetroot Lip Balm Classic': ('FOR', None, None), 'Deyga Beetroot Lip Balm Stick': ('FOR', None, None),
 'Vilvah Lip Balm - Lemon': ('Vilvah Lemon Lip Balm for Dry Lips', None, None),
 'Deyga Soft Lip Combo': ('FOR', None, None), 'Deyga Nourished Lip Care Kit': ('FOR', None, None),
 'Deyga Nourished Lips Stick Kit': ('FOR', None, None), 'Vilvah Lip Nourishing Kit': ('FOR', None, None),
 'Vilvah Tinted Lip Balm Kit': ('FOR', None, None),
 'Vilvah Deo Shot - Lavender and Sage': ('Vilvah Deo Shot Natural Deodorant – Lavender and Sage', None, None),
 'Vilvah Deo Shot - Rose and Vanilla': ('Vilvah Deo Shot Natural Deodorant – Rose and Vanilla', None, None),
 'Deyga Foot Scrub': ('DASH', None, None), 'Vilvah Cookie N Cream Body Polish': ('DASH', None, None),
 'Deyga Foot Butter': ('DASH', None, None), 'Vilvah Milk Mud Mask': ('Vilvah Milk Mud Face Mask', None, None),
 'Deyga 2% Hyaluronic Acid Serum': ('DASH', None, None), 'Deyga Rose Glow Serum': ('DASH', None, None),
 'Deyga Beautifying Serum': ('DASH', None, None), 'Deyga Rose & Mulethi Skin Brightening Pack': ('DASH', None, None),
 'Vilvah Better Ageing Serum': ('Vilvah Better Ageing Face Serum', None, None),
 'Vilvah Skin Finish Sunscreen SPF 50': (None, 'sunscreen spf 50', None),
 'Deyga Under Eye Cream': (None, 'under eye cream', None),
 # kits: keyword is a fair description of the kit
 **{k: ('DASH', None, None) for k in ['Vilvah Skin Radiance Kit', 'Vilvah AM Brightening Kit', 'Vilvah AM PM Serum Kit',
    'Vilvah Skin Brightening Kit', 'Vilvah Face Brightening Kit', 'Vilvah Body Polishing Kit', 'Vilvah Face Lift Kit',
    'Vilvah Pore Minimising Kit', 'Deyga Sensitive Skin Kit', 'Vilvah Sensitive Skin Kit', 'Vilvah Night Repair Kit',
    'Vilvah Better Ageing Kit', 'Vilvah Lip Lightening Kit', 'Deyga Clear Skin Kit', 'Deyga Hydro Boosting Skin Care Kit',
    'Vilvah Milk Face Kit', 'Vilvah Skin Hydration Kit', 'Deyga Double Hydration Kit', 'Vilvah Milk Body Kit']},
 # keyword does NOT describe the product: keyword becomes the product name, description gets the right type
 'Deyga Vitamin C Daily Glow Combo': (None, 'NAME', 'vitamin C skincare combo'),
 'Deyga Acne Relief Combo': (None, 'NAME', 'face care combo'), 'Deyga Acne Vanishing Combo': (None, 'NAME', 'face care combo'),
 'Deyga Mini Foot Spa Combo': (None, 'NAME', 'foot care combo'),
 'Deyga Orange & Almond Face Pack Powder': (None, 'NAME', 'face pack'), 'Deyga Spirulina Matcha Face Pack': (None, 'NAME', 'face pack'),
 'Deyga Premature Greying Hair Oil': (None, 'NAME', 'hair oil'), 'Vilvah Anti-dandruff Hair Oil': (None, 'NAME', 'hair oil'),
 'Deyga Natural Loose Setting Powder': (None, 'NAME', 'loose setting powder'), 'Deyga Foot Soak Powder': (None, 'NAME', 'foot soak'),
 'Deyga Neem Seed Oil': (None, 'NAME', 'neem oil for skin and hair'), 'Deyga Under Eye Mask': (None, 'NAME', 'under eye mask'),
 'Deyga Tangerine Cleansing Balm for Makeup Removal': (None, 'NAME', 'cleansing balm'),
 'Deyga Organic Loofah for Body Exfoliation': (None, 'NAME', 'body loofah'), 'Deyga Eyebrow Growth Oil': (None, 'NAME', 'eyebrow oil'),
 **{k: (None, 'NAME', 'soap bar') for k in ['Deyga Spinach & Cucumber Bath Bar', 'Deyga Shea Saffron Bath Bar', 'Deyga Rose Pink Clay Bath Bar',
    'Deyga Neem & Turmeric Bath Bar', 'Deyga Charcoal Bath Bar', 'Vilvah Cucumber, Curd & Mint Soap']},
 'Vilvah Charcoal Goatmilk Soap': ('Vilvah Charcoal Goat Milk Soap', 'goat milk soap', 'goat milk soap'),
 'Vilvah Classic Goatmilk Soap': ('Vilvah Classic Goat Milk Soap', 'goat milk soap', 'goat milk soap'),
 **{k: (None, 'NAME', 'sun care kit') for k in ['Vilvah Tan Protection Kit', 'Vilvah Sun Protection Kit']},
 **{k: (None, 'NAME', 'skincare kit') for k in ['Vilvah Everyday Care Milk Kit', 'Vilvah Oil Control Kit', 'Deyga Daily Essential Kit',
    'Deyga Best Selling Face Care Kit', 'Deyga Healthy Glow Kit', 'Deyga ABC Kit', 'Deyga Game Changer Face Care Kit', 'Deyga De- Tan & Pigmentation Kit']},
 **{k: (None, 'NAME', 'hair care kit') for k in ['Vilvah Shampoo and Hair Serum Kit', 'Vilvah Goat Milk Hair Kit', 'Deyga Hair Care Kit',
    'Deyga Hair Nourishment Kit', 'Deyga Daily Use Healthy Hair Kit', 'Vilvah Bestseller Hair Kit', 'Vilvah Hairfall Control Kit',
    'Vilvah Hair Strengthening Kit']},
 **{k: (None, 'NAME', 'conditioner') for k in ['Vilvah Cream Conditioner', 'Deyga Soy Milk Conditioner']},
 'Deyga Instant Hair Removal Kit': (None, 'NAME', 'hair removal kit'), 'Deyga Instant Hair Removal Kit with Toner': (None, 'NAME', 'hair removal kit'),
 'Deyga Hair Removal Powder': (None, 'NAME', 'hair removal powder'), 'Deyga Face & Body Exfoliator Powder': (None, 'NAME', 'exfoliator powder'),
 'Vilvah Cookie N Cream Body Mask': (None, 'NAME', 'body mask'), 'Deyga Plant Based Hair Color': (None, 'NAME', 'plant-based hair colour'),
 'Vilvah Neem Wood Comb(Fine and Wide Tooth)': ('Vilvah Neem Wood Comb (Fine and Wide Tooth)', 'NAME', 'neem wood comb'),
 'Vilvah Neem Wood Comb (With Handle)': (None, 'NAME', 'neem wood comb'),
}
def tc(s): return ' '.join(w if w in ('for', 'and', 'with') else (w if w.isupper() else w[:1].upper() + w[1:]) for w in s.split())
def clean(t):  # store title without size/marketing tail
    return re.split(r' – | \| ', t)[0].strip()
log = []
for p in P:
    r = bd.get((p.get('sd') or '').strip()) or bt.get((p.get('st') or '').strip())
    old = dict(h1=None, st=p.get('st'), sd=p.get('sd'), kw=None)
    if r:
        h1 = r[ix['FINAL H1']].strip(); kw = r[ix['Primary keyword']] or h1.lower()
        if r[ix['Source']] == 'Vilvah & Deyga':
            f = FIX.get(h1)
            if f:
                newh1, newkw, typ = f
                if newh1 == 'FOR': newh1 = f"{h1} for {tc(kw.split(' for ')[1])}"
                elif newh1 == 'DASH': newh1 = f"{h1} – {tc(kw)}"
                if newkw == 'NAME': newkw = (newh1 or h1).lower()
                oldkw = kw
                h1 = newh1 or h1; kw = newkw or kw
                if typ:  # description named the wrong product type
                    p['sd'] = re.sub(r'(, |: )(a )?(natural )?' + re.escape(re.sub(r'^natural ', '', oldkw)) + ' from', lambda m: f"{m.group(1)}{'a natural ' if typ != 'neem wood comb' else 'a '}{typ} from", p['sd'])
                if typ and newh1: p['sd'] = p['sd'].replace(r[ix['FINAL H1']].strip(), h1)  # e.g. Goatmilk -> Goat Milk
                if (typ or newkw) and oldkw != kw and (oldkw.lower() in (p['st'] or '').lower() or newh1):
                    p['st'] = fit(h1, 'Swansura UK')
                elif not has(p['st'], kw):
                    base = r[ix['FINAL H1']].strip()
                    p['st'] = fit(h1, 'Swansura UK') if (typ or newkw) else fit(base, tc(kw)) if len(f"{base} | {tc(kw)}") <= 60 else fit(h1, 'Swansura')
        p['h1'] = h1; p['kw'] = kw
    else:
        t = clean(p['title']); h1 = t if t.lower().startswith(p['brand'].lower()) else f"{p['brand']} {t}"
        p['h1'] = h1; p['kw'] = None
    if not p.get('st') and len(h1) > 60 - len(' | Swansura UK'):
        short = re.sub(r'Eau de Parfum', 'EDP', re.sub(r'Eau de Toilette', 'EDT', h1))
        short = re.sub(r' Signature Collection', '', short) if len(short) > 60 else short
        p['st'] = fit(short, 'Swansura UK') if len(short) <= 60 else short[:60].rsplit(' ', 1)[0]
    if p.get('sd') and len(p['sd']) > 158:
        p['sd'] = p['sd'].replace('Official UK partner: 100% authentic, shipped from the UK, free delivery over £40.', 'Official UK partner, 100% authentic, free UK delivery over £40.')
    ch = {k: (old[k], p.get(k)) for k in ('st', 'sd') if old[k] != p.get(k)}
    log.append(dict(id=p['id'], handle=p.get('h'), h1=p['h1'], keyword=p['kw'] or '', meta_title=p.get('st') or '', meta_title_changed='yes' if 'st' in ch else '', meta_description_changed='yes' if 'sd' in ch else '', meta_description=p.get('sd') or ''))
# hand-fitted titles/descriptions where the automatic ones lost part of the keyword (<= 60 / <= 160 chars)
OVERRIDE = {
 '16373161525635': {'st': 'CK Eternity Aromatic Essence Parfum Intense Miniature Women'},
 '16373147271555': {'st': 'CK Eternity Aromatic Essence Parfum Intense Miniature Men'},
 '16368950706563': {'st': 'anatomē Bath & Shower Oil, Chamomile & Lavender | Swansura'},
 '15415435198851': {'st': 'Jo Milano Game of Spades Wildcard Parfum 100ml | Swansura'},
 '16376523489667': {'st': 'Elie Saab Le Parfum Lumière Gift Set EDP 90ml | Swansura'},
 '15415435985283': {'st': 'Deyga Rose & Mulethi Pack | Skincare for Dull Skin'},
 '15415430316419': {'sd': 'Buy Vilvah Sun Protection Kit, a natural sun care kit from Vilvah with SPF 50 face sunscreen. Official UK partner, 100% authentic, free UK delivery over £40.'},
}
for p in P:
    for k, v in OVERRIDE.get(p['id'], {}).items():
        p[k] = v
        row = next(l for l in log if l['id'] == p['id'])
        row['meta_title' if k == 'st' else 'meta_description'] = v; row['meta_title_changed' if k == 'st' else 'meta_description_changed'] = 'yes'
json.dump(P, open('prototype/products.json', 'w'), ensure_ascii=False, separators=(',', ':'))
os.makedirs('docs/seo', exist_ok=True)
with open('docs/seo/product_onpage_2026-10-26.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(log[0])); w.writeheader(); w.writerows(log)
print('products', len(P), 'title changes', sum(1 for l in log if l['meta_title_changed']), 'desc changes', sum(1 for l in log if l['meta_description_changed']))

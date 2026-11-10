"""Recount the FAQ answers on the 5 scent-family pages (user, 10 Nov 2026: 'Go ahead and recount the scent page FAQs').
The gender splits, mini/gift-set counts and price ranges dated from before the 8 Nov products. Same rules as
tools/shopify/stale_copy_fix.py fix_faq (scent part): gender split from perfume-for-women/men + unisex-perfume,
minis/sets = perfume-gift-sets + travel-size-minis, price range of the live members, examples kept unless one has left.
argv[1] = folder of storefront dumps <handle>.json ([{handle,title,vendor,avail,prices}]), argv[2] = Admin read
({data:{alias:{id,handle,faq:{value}}}}). Writes docs/seo/scent_faq_recount_2026-11-10.json (before/after = undo).
"""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
S = pathlib.Path(sys.argv[1])
L = lambda h: json.load(open(S / f'{h}.json'))
SC = ['scent-floral', 'scent-woody', 'scent-amber', 'scent-fresh', 'scent-oud']
GENDER = {'for her': {p['handle'] for p in L('perfume-for-women')}, 'for him': {p['handle'] for p in L('perfume-for-men')},
          'unisex': {p['handle'] for p in L('unisex-perfume')}}
MINI = {p['handle'] for p in L('perfume-gift-sets')} | {p['handle'] for p in L('travel-size-minis')}
CLAIMY = re.compile(r'acne|lighten|hairfall|hair fall|de- ?tan|pigment|anti-ageing|anti-aging|greying', re.I)


def short(p):
    t = p['title'].split(' – ')[0].split(' | ')[0]
    for v in (p['vendor'] + ' ',):
        if t.startswith(v):
            t = t[len(v):]
    return t.strip()


def examples(ps, k=3):
    ps = [p for p in ps if p['avail'] and not CLAIMY.search(p['title'])]
    names = [short(p) for p in ps[:k]]
    return ', '.join(names[:-1]) + ' and ' + names[-1]


def money(v):
    return f'£{v:.2f}'.replace('.00', '') if v == int(v) and v >= 20 else f'£{v:.2f}'


adm = {c['handle']: c for c in json.load(open(sys.argv[2]))['data'].values()}
out = []
for h in SC:
    ps = L(h); hs = {p['handle'] for p in ps}
    pr = [float(x) for p in ps for x in p['prices']]
    faq = json.loads(adm[h]['faq']['value']); new = []
    for q, a in faq:
        if re.fullmatch(r'Yes: [\d\w ,]+\.', a):
            parts = sorted(((len(hs & GENDER[g]), g) for g in GENDER if hs & GENDER[g]), reverse=True)
            a = 'Yes: ' + ', '.join(f'{c} {g}' for c, g in parts) + '.'
        elif re.match(r'Yes(, \d+)?: ', a) and 'miniatures or gift sets' in q:
            ms = [p for p in ps if p['handle'] in MINI]
            if h == 'scent-oud':  # Daisy Love sits in scent-oud but is not an oud
                ms = [p for p in ms if 'oud' in p['title'].lower()]
            ms = [p for p in ms if p['avail']] + [p for p in ms if not p['avail']]
            if len(ms) == 1:
                a = f"Yes: {ms[0]['vendor']} {short(ms[0])}."
            elif ms:
                names = [short(p) for p in ms[:3]]
                a = f'Yes, {len(ms)}: ' + ', '.join(names[:-1]) + ' and ' + names[-1] + (' and more.' if len(ms) > 3 else '.')
            else:
                a = 'Not at the moment.'
        elif re.fullmatch(r'From £[\d.]+ to £[\d.]+\.', a):
            a = f'From {money(min(pr))} to {money(max(pr))}.'
        elif m := re.match(r'(.*?Examples here include )(.*)\.$', a):
            titles = ' '.join(p['title'] for p in ps if p['avail'])
            if not all(nm in titles for nm in re.split(r', | and ', m.group(2))):
                a = m.group(1) + examples(ps) + '.'
        new.append([q, a])
    out.append({'id': adm[h]['id'], 'handle': h, 'live_products': len(ps), 'before': faq, 'after': new})
json.dump(out, open(ROOT / 'docs/seo/scent_faq_recount_2026-11-10.json', 'w'), ensure_ascii=False, indent=1)
for o in out:
    print('##', o['handle'], o['live_products'])
    for (q, a0), (_, a1) in zip(o['before'], o['after']):
        if a0 != a1: print('  -', a0, '\n  +', a1)

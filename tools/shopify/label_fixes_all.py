"""Gender + scent-family label fixes across all perfumes (user, 8 Nov 2026: "Fix the gender and family labels across
all products"). Follows the 8 Nov fixes of 19 products (docs/seo/label_fixes_2026-11-08.json).

Input (scratchpad dir given as argv[1]):
  products.json      Admin export of all active products (id, handle, title, descriptionHtml, sw, pdp)
  family_changes.json  reviewed family changes [{h, title, from, to}] (35, chosen by hand from the notes;
                       titles that name a family keep it; 'Oud' in the name keeps oud)
  avail.jsonl        storefront availability per handle (for the 'similar' lists)
  <collection>.txt   storefront handles of perfume-for-women/men, unisex-perfume, scent-* (current membership)
GENDER (below) = 12 reviewed gender changes (title says Lady/Miss/(W); description says feminine / for the modern man).

For each changed product: custom.sw (f / w / t, the generic family answer in 'a'), custom.pdp (family + gender chip,
gender 'kw' link, 'sim' rebuilt from in-stock same-family + same-gender perfumes), gender + scent-* collections.
Writes docs/seo/label_fixes_all_2026-11-08.json (before/after per product = undo list).
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
S = pathlib.Path(sys.argv[1])
P = {p['handle']: p for p in json.load(open(S / 'products.json'))}
FAM = {c['h']: c['to'] for c in json.load(open(S / 'family_changes.json'))}
GENDER = {  # handle substring -> new gender
    'korloff-lady-intense': 'Women', 'miss-korloff': 'Women', 'yvresse': 'Women', 'fumeri-gabriella': 'Women',
    'fumeri-flirt': 'Women', 'un-soir': 'Women', 'korloff-paris-discovery-set': 'Women', 'signature-rose': 'Women',
    'signature-aura': 'Women', 'trussardi-pure-jasmine-lifestyle': 'Women', 'aventure-blanche': 'Women',
    'korloff-in-white': 'Men'}
AV = {}
for l in open(S / 'avail.jsonl'):
    d = json.loads(l); AV[d['h']] = d
MEM = {c: set(open(S / f'{c}.txt').read().split()) for c in
       ['perfume-for-women', 'perfume-for-men', 'unisex-perfume', 'scent-floral', 'scent-woody', 'scent-amber',
        'scent-fresh', 'scent-oud']}
CID = {'perfume-for-women': 'gid://shopify/Collection/714070851971', 'perfume-for-men': 'gid://shopify/Collection/714070884739',
       'unisex-perfume': 'gid://shopify/Collection/714070950275', 'scent-floral': 'gid://shopify/Collection/714071703939',
       'scent-woody': 'gid://shopify/Collection/714071736707', 'scent-amber': 'gid://shopify/Collection/714071671171',
       'scent-fresh': 'gid://shopify/Collection/714071769475', 'scent-oud': 'gid://shopify/Collection/714071638403'}
GCOLL = {'Women': 'perfume-for-women', 'Men': 'perfume-for-men', 'Unisex': 'unisex-perfume'}
GSW = {'Women': 'For her', 'Men': 'For him', 'Unisex': 'Unisex'}
GCHIP = {'Women': 'For women', 'Men': 'For men', 'Unisex': 'Unisex'}
GKW = {'Women': ['Perfume for women', '/collections/perfume-for-women'], 'Men': ['Perfume for men', '/collections/perfume-for-men'],
       'Unisex': ['Unisex perfume', '/collections/unisex-perfume']}
FDESC = {'oud': 'smoky, resinous, regal', 'amber': 'warm, sweet, golden', 'floral': 'rose, jasmine, white flowers',
         'woody': 'sandalwood, cedar, patchouli', 'fresh': 'citrus, bergamot, air'}
NORM = {'For her': 'Women', 'Women': 'Women', 'For him': 'Men', 'Men': 'Men', 'Unisex': 'Unisex'}


def gender_of(s):
    return NORM.get(s.get('w')) or NORM.get(s.get('t')) or 'Unisex'


ghandles = {}
for h in P:
    for k, g in GENDER.items():
        if k in h:
            ghandles[h] = g
assert len(ghandles) == len(GENDER), (len(ghandles), sorted(ghandles))
todo = sorted(set(FAM) | set(ghandles))

# current label of every perfume, after the changes (for the similar lists)
LAB = {}
for h, p in P.items():
    if not p['sw']:
        continue
    s = json.loads(p['sw']['value'])
    if s.get('f'):
        LAB[h] = (FAM.get(h, s['f']), ghandles.get(h, gender_of(s)))

out = []
for h in todo:
    p = P[h]
    s = json.loads(p['sw']['value']); pdp = json.loads(p['pdp']['value']) if p['pdp'] else None
    before = {'sw': p['sw']['value'], 'pdp': p['pdp']['value'] if p['pdp'] else None}
    f_old, g_old = s['f'], gender_of(s)
    f_new, g_new = FAM.get(h, f_old), ghandles.get(h, g_old)
    s['f'] = f_new
    s['w'] = s['t'] = GSW[g_new]
    if s.get('a'):
        art = 'An' if f_new[0] in 'aeiou' else 'A'
        s['a'] = [(f"{art} {f_new} fragrance: {FDESC[f_new]}." if re.match(r'^An? \w+ fragrance: [a-z ,]+\.$', a)
                   else re.sub(r'^An? \w+ fragrance:', f'{art} {f_new} fragrance:', a)) for a in s['a']]
    if pdp:
        old_ch = pdp.get('chips', [])
        style = GSW if any(c in ('For her', 'For him') for c in old_ch) else GCHIP  # keep the wording the product used
        ch = [c for c in old_ch if not re.match(r'^\w+ family$', c) and c not in ('For women', 'For men', 'For her', 'For him', 'Unisex')]
        pdp['chips'] = [f_new.capitalize() + ' family', style[g_new]] + ch
        kw = [k for k in pdp.get('kw', []) if k[1] not in ('/collections/perfume-for-women', '/collections/perfume-for-men', '/collections/unisex-perfume')]
        pdp['kw'] = [GKW[g_new]] + kw
        sim = [x for x, (f, g) in LAB.items() if x != h and f == f_new and g == g_new and AV.get(x, {}).get('a') and AV.get(x, {}).get('img')]
        if len(sim) < 4:
            sim += [x for x, (f, g) in LAB.items() if x != h and x not in sim and f == f_new and AV.get(x, {}).get('a') and AV.get(x, {}).get('img')]
        old = [x for x in pdp.get('sim', []) if x in sim]
        pdp['sim'] = (old + [x for x in sim if x not in old])[:4]
    join, leave = [], []
    gc = GCOLL[g_new]
    in_g = [c for c in ('perfume-for-women', 'perfume-for-men', 'unisex-perfume') if h in MEM[c]]
    if in_g:  # deodorants / body mists that sit in no gender collection stay out of them
        if h not in MEM[gc]:
            join.append(CID[gc])
        for c in in_g:
            if c != gc:
                leave.append(CID[c])
    fc = 'scent-' + f_new
    if h not in MEM[fc]:
        join.append(CID[fc])
    for c in ('scent-floral', 'scent-woody', 'scent-amber', 'scent-fresh', 'scent-oud'):
        if c != fc and h in MEM[c]:
            leave.append(CID[c])
    mf = [{'namespace': 'custom', 'key': 'sw', 'type': 'json', 'value': json.dumps(s, ensure_ascii=False)}]
    if pdp:
        mf.append({'namespace': 'custom', 'key': 'pdp', 'type': 'json', 'value': json.dumps(pdp, ensure_ascii=False)})
    out.append({'id': p['id'], 'handle': h, 'title': p['title'], 'family': [f_old, f_new], 'gender': [g_old, g_new],
                'before': before, 'input': {'id': p['id'], 'metafields': mf, 'collectionsToJoin': join, 'collectionsToLeave': leave}})
json.dump(out, open(ROOT / 'docs/seo/label_fixes_all_2026-11-08.json', 'w'), ensure_ascii=False, indent=1)
for o in out:
    print(f"{o['family'][0]:6}->{o['family'][1]:6} {o['gender'][0]:6}->{o['gender'][1]:6} +{len(o['input']['collectionsToJoin'])} -{len(o['input']['collectionsToLeave'])} {o['title'][:60]}")
print(len(out), 'products')

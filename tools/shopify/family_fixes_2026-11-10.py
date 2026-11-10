"""Scent-family label fixes flagged by the 10 Nov description writers (user, 10 Nov 2026: 'Fix the scent-family
labels the writers flagged'). Uses the store's five families (floral, woody, amber, fresh, oud).
Input: argv[1] = Admin read of the 5 products (id, handle, title, sw, pdp, collections) as {alias: product}.
Changes custom.sw f + the family word in its 'a' answer, the pdp family chip, and the scent-* collection.
'sim' lists are same-brand lists from the 8 Nov generator: left alone.
Kept (label fits the 5-family scheme): Phantom Parfum 15ml amber (vanilla/tolu balsam base; every Phantom listing
is amber), Mugler Angel amber (gourmand sits in amber), Polo Red Parfum woody (cedar, opoponax base), Moschino
I Love Love fresh (citrus-led), Lalique Amethyst floral (fruity floral), Versace Eros EDT amber (vanilla base).
Writes docs/seo/family_fixes_2026-11-10.json (before/after per product = undo list).
"""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
CHANGE = {'paco-rabanne-1-million-eau-de-toilette-200ml': ('woody', 'amber', 'cinnamon, amber and leather read spicy amber'),
          'roberto-cavalli-paradiso-eau-de-parfum-100ml': ('floral', 'fresh', 'citrus over cypress, pine and laurel; jasmine is the only flower'),
          'michael-kors-pour-homme-eau-de-parfum-miniature-5ml': ('woody', 'fresh', 'bergamot, lavender, sea water and sage: aromatic aquatic'),
          'mugler-angel-elixir-eau-de-parfum-refillable-star': ('floral', 'amber', 'Bourbon vanilla + amber base: amber floral'),
          'versace-eros-pour-femme-eau-de-parfum-100ml': ('fresh', 'floral', 'jasmine sambac, peony, lemon flower; the 5ml miniature is already floral')}
CID = {'floral': 'gid://shopify/Collection/714071703939', 'woody': 'gid://shopify/Collection/714071736707',
       'amber': 'gid://shopify/Collection/714071671171', 'fresh': 'gid://shopify/Collection/714071769475'}
P = {p['handle']: p for p in json.load(open(sys.argv[1]))['data'].values()}
out = []
for h, (f0, f1, why) in CHANGE.items():
    p = P[h]; s = json.loads(p['sw']['value']); d = json.loads(p['pdp']['value'])
    assert s['f'] == f0, (h, s['f'])
    cols = [c['handle'] for c in p['collections']['nodes']]
    assert 'scent-' + f0 in cols and 'scent-' + f1 not in cols, (h, cols)
    s['f'] = f1
    art = 'An' if f1[0] in 'aeiou' else 'A'
    s['a'] = [re.sub(r'^An? \w+ fragrance:', f'{art} {f1} fragrance:', a) for a in s['a']]
    d['chips'] = [f1.capitalize() + ' family' if re.match(r'^\w+ family$', c) else c for c in d['chips']]
    mf = [{'namespace': 'custom', 'key': 'sw', 'type': 'json', 'value': json.dumps(s, ensure_ascii=False)},
          {'namespace': 'custom', 'key': 'pdp', 'type': 'json', 'value': json.dumps(d, ensure_ascii=False)}]
    out.append({'id': p['id'], 'handle': h, 'title': p['title'], 'family': [f0, f1], 'why': why,
                'before': {'sw': p['sw']['value'], 'pdp': p['pdp']['value'], 'scent': 'scent-' + f0},
                'input': {'id': p['id'], 'metafields': mf, 'collectionsToJoin': [CID[f1]], 'collectionsToLeave': [CID[f0]]}})
json.dump(out, open(ROOT / 'docs/seo/family_fixes_2026-11-10.json', 'w'), ensure_ascii=False, indent=1)
for o in out: print(o['family'], o['title'])

"""Plan: make every prototype listing a Shopify collection with the prototype's exact membership.

Input:  docs/data/prototype_export.json (tools/proto/extract_data.js), docs/backups/products_before_day4_2026-10-26.jsonl,
        docs/backups/collections_before_day4_2026-10-26.jsonl
Output: docs/data/proto_collections_plan.json
  - tags: product gid -> tags to add (client's own category tags 'Skincare', 'Haircare', 'Bodycare', 'Sets & Combos'
          fill the existing automated collections; price bands are automated by price; other new collections are manual with their products)
  - manual_add: existing manual collection handle -> product gids to add (fragrance + Day-4 keyword collections)
  - create: new automated collections (handle, title, tag rule, prototype order)
  - order: handle -> product gids in the prototype's ranked order (for collectionReorderProducts)
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
D = json.load(open(ROOT / 'docs/data/prototype_export.json'))
A = {r['r']: r for r in json.load(open(ROOT / 'docs/seo/prototype_seoaudit_2026-10-26.json'))}
PROD = {}
for l in open(ROOT / 'docs/backups/products_before_day4_2026-10-26.jsonl'):
    r = json.loads(l)
    if 'handle' in r: PROD[r['id'].split('/')[-1]] = r
COLL = {json.loads(l)['handle']: json.loads(l) for l in open(ROOT / 'docs/backups/collections_before_day4_2026-10-26.jsonl') if 'handle' in json.loads(l)}

# Existing collections that stand for a prototype listing (Day 4 mapping) and how they are filled.
EXISTING = {
    'c-skincare': ('skincare', 'tag', 'Skincare'), 'c-haircare': ('haircare', 'tag', 'Haircare'),
    'c-bath-body': ('bodycare', 'tag', 'Bodycare'), 'c-gifts': ('sets-combos', 'tag', 'Sets & Combos'),
    'c-fragrance': ('fragrance', 'manual', None),
    'k-face-serum': ('serum', 'manual', None), 'k-face-wash': ('cleanser', 'manual', None), 'k-moisturiser': ('moisturizers-gels', 'manual', None),
    'k-sunscreen': ('sunscreen', 'manual', None), 'k-toner': ('toner', 'manual', None), 'k-lip-balm': ('lip-balm', 'manual', None),
    'k-lip-scrub': ('lip-scrub', 'manual', None), 'k-shampoo': ('shampoo', 'manual', None), 'k-hair-oil': ('hair-oil', 'manual', None),
    'k-deodorant': ('deodrants', 'manual', None), 'k-face-mask': ('face-mask-pack', 'manual', None),
}
SKIP = {'c-all'}  # Shopify's built-in /collections/all
gid = lambda i: f'gid://shopify/Product/{i}'
tags, manual_add, create, order = {}, {}, [], {}
for route, L in D['listings'].items():
    if route in SKIP or not L['live']:
        continue
    ids = [i for i in L['ids'] if str(i) in PROD]
    if route in EXISTING:
        handle, how, tag = EXISTING[route]
        cur = COLL[handle]
        if how == 'tag':
            for i in ids:
                if tag not in PROD[str(i)]['tags']:
                    tags.setdefault(gid(i), []).append(tag)
        else:
            manual_add[handle] = [gid(i) for i in ids]
    else:
        handle = A[route]['canon'].split('/collections/')[-1]
        if L['kind'] == 'price':  # automated: product price band, like the prototype's inBand()
            lo, hi = L['key'].split('-')
            create.append({'route': route, 'handle': handle, 'title': L['title'], 'price': [lo, hi]})
        else:
            create.append({'route': route, 'handle': handle, 'title': L['title'], 'products': [gid(i) for i in ids]})
    order[handle] = [gid(i) for i in ids]
missing = sorted({str(i) for L in D['listings'].values() for i in L['ids'] if str(i) not in PROD})
json.dump({'tags': tags, 'manual_add': manual_add, 'create': create, 'order': order}, open(ROOT / 'docs/data/proto_collections_plan.json', 'w'), indent=0)
print(len(tags), 'products get tags;', sum(len(v) for v in tags.values()), 'tags;', len(create), 'new collections;',
      len(manual_add), 'manual collections to fill;', len(missing), 'prototype ids not in the backup:', missing[:5])

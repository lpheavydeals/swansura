"""Deyga Chocolate Body Butter £15.99 -> £13.99 (live price) in 2 Journal guides (16 Nov 2026).
Usage: python3 choc_butter_price_fix_2026-11-16.py <admin articles json>
Writes docs/seo/choc_butter_price_fix_2026-11-16.json (before/after = undo)."""
import json, sys
OLD = 'chocolate-body-butter-100g">Deyga Chocolate Body Butter</a> (£15.99, 100g)'
NEW = 'chocolate-body-butter-100g">Deyga Chocolate Body Butter</a> (£13.99, 100g)'
nodes = json.load(open(sys.argv[1]))['data']['articles']['nodes']
out = []
for a in nodes:
    if a['handle'] in ('how-to-use-body-butter', 'how-to-use-body-scrub'):
        assert a['body'].count(OLD) == 1, a['handle']
        out.append({'handle': a['handle'], 'id': a['id'], 'before': a['body'], 'after': a['body'].replace(OLD, NEW)})
assert len(out) == 2
json.dump(out, open('docs/seo/choc_butter_price_fix_2026-11-16.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({x['handle']: x['after'] for x in out}, ensure_ascii=False))

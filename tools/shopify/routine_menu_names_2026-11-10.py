"""Rename the two claim-style routine links in menu sw-main (user, 10 Nov 2026:
'Go ahead and rename both routines in a new draft'): Age-Defying Routine -> Mature Skin Routine,
Hair Fall Rescue -> Hair Care Routine. Input: an Admin read of sw-main (id title type url tags resourceId, 3 levels).
Output: docs/seo/routine_menu_names_2026-11-10.json = {before, menuUpdate variables}.
"""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
m = json.load(open(sys.argv[1]))['data']['a']
REN = {'Age-Defying Routine': 'Mature Skin Routine', 'Hair Fall Rescue': 'Hair Care Routine'}
hits = []
def conv(it):
    o = {k: it[k] for k in ('id', 'title', 'type', 'url', 'tags') if it.get(k) not in (None, [])}
    if it.get('resourceId'): o['resourceId'] = it['resourceId']
    if o['title'] in REN: hits.append(o['title']); o['title'] = REN[o['title']]
    if it.get('items'): o['items'] = [conv(x) for x in it['items']]
    return o
items = [conv(i) for i in m['items']]
assert sorted(hits) == sorted(REN), hits
var = {'id': m['id'], 'title': m['title'], 'handle': m['handle'], 'items': items}
json.dump({'before': m, 'variables': var}, open(ROOT / 'docs/seo/routine_menu_names_2026-11-10.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(var, ensure_ascii=False, separators=(',', ':')))

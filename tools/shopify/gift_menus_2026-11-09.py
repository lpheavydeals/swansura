"""Menu links for the 9 Nov gift pages (user, 9 Nov 2026: "Go ahead with the gift pages and collection alt text").
Builds menuUpdate inputs from docs/backups/gift_pages_before_2026-11-09.json (item ids kept).
- sw-main Gifts & Sets > Christmas 2026: + Christmas gifts, Black Friday
  > By recipient: + Perfume gift sets for her, Aftershave gift sets for him, Skincare gift sets (before Perfume gift sets)
  > By price & occasion: + Under £50 (after Under £25)
- sw-drawer Gifts & Sets > Christmas 2026: + Christmas gifts, Black Friday
  > By recipient & price: + Perfume gift sets for her, Aftershave gift sets for him, Skincare gift sets, Gifts under £50
Output: docs/seo/gift_menus_2026-11-09.json
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
M = {m["handle"]: m for m in json.load(open(ROOT / "docs/backups/gift_pages_before_2026-11-09.json"))["menus"]}

def conv(it):
    o = {k: it[k] for k in ("id", "title", "type", "url", "tags") if it.get(k) is not None}
    if it.get("resourceId"): o["resourceId"] = it["resourceId"]
    if it.get("items"): o["items"] = [conv(x) for x in it["items"]]
    return o
def new(t, h): return {"title": t, "type": "HTTP", "url": f"/collections/{h}"}
def find(items, title): return next(i for i in items if i["title"] == title)
def idx(items, title): return next(n for n, i in enumerate(items) if i["title"] == title)

HER, HIM, SKIN = new("Perfume gift sets for her", "perfume-gift-sets-for-her"), new("Aftershave gift sets for him", "aftershave-gift-sets-for-him"), new("Skincare gift sets", "skincare-gift-sets")
XMAS, BF = new("Christmas gifts", "christmas-gifts"), new("Black Friday", "black-friday")
out = {}
main = [conv(i) for i in M["sw-main"]["items"]]
g = find(main, "Gifts & Sets")["items"]
find(g, "Christmas 2026")["items"] += [dict(XMAS), dict(BF)]
rec = find(g, "By recipient")["items"]; n = idx(rec, "Perfume gift sets"); rec[n:n] = [dict(HER), dict(HIM), dict(SKIN)]
pr = find(g, "By price & occasion")["items"]; n = idx(pr, "Under £25") + 1; pr[n:n] = [new("Under £50", "gifts-under-50")]
out["sw-main"] = main
dr = [conv(i) for i in M["sw-drawer"]["items"]]
g = find(dr, "Gifts & Sets")["items"]
find(g, "Christmas 2026")["items"] += [dict(XMAS), dict(BF)]
rp = find(g, "By recipient & price")["items"]; n = idx(rp, "Gifts under £25"); rp[n:n] = [dict(HER), dict(HIM), dict(SKIN)]
n = idx(rp, "Gifts under £25") + 1; rp[n:n] = [new("Gifts under £50", "gifts-under-50")]
out["sw-drawer"] = dr
res = {h: {"id": M[h]["id"], "title": M[h]["title"], "handle": h, "items": v} for h, v in out.items()}
json.dump(res, open(ROOT / "docs/seo/gift_menus_2026-11-09.json", "w"), ensure_ascii=False, indent=1)
for h, v in res.items(): print(h, len(json.dumps(v, ensure_ascii=False)))

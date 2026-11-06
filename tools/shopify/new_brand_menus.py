"""Menu links for the 2 Nov brands (user OK 6 Nov 2026). Builds menuUpdate inputs from the before-state
(docs/backups/new_brand_copy_before_2026-11-06.json, item ids kept so existing items are updated, not recreated).
- sw-main Fragrance > Houses: + Lattafa, Guess (before 'All brands A–Z').
- sw-main Brands > More houses: Chloé, Marc Jacobs -> Guess, Franck Olivier; 'All 66 brands A–Z' -> 'All brands A–Z';
  new 4th column 'Arabian houses' (Lattafa, Armaf, Afnan, Maison Alhambra, Swiss Arabian, Rasasi, Arabiyat Prestige).
- sw-footer-brands: + Lattafa, Guess.   - sw-drawer Fragrance > Houses: + Lattafa, Armaf.
Output: docs/seo/new_brand_menus_2026-11-06.json
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
M = {m["handle"]: m for m in json.load(open(ROOT / "docs/backups/new_brand_copy_before_2026-11-06.json"))["menus"]}

def conv(it):
    o = {k: it[k] for k in ("id", "title", "type", "url", "tags") if it.get(k) is not None}
    if it.get("resourceId"): o["resourceId"] = it["resourceId"]
    if it.get("items"): o["items"] = [conv(x) for x in it["items"]]
    return o

def new(t, h): return {"title": t, "type": "HTTP", "url": f"/collections/{h}"}
def find(items, title): return next(i for i in items if i["title"] == title)

out = {}
main = [conv(i) for i in M["sw-main"]["items"]]
houses = find(find(main, "Fragrance")["items"], "Houses")["items"]
houses[-1:-1] = [new("Lattafa", "lattafa"), new("Guess", "guess")]
brands = find(main, "Brands")["items"]
more = find(brands, "More houses")["items"]
for i, it in enumerate(more):
    if it["title"] == "Chloé": more[i] = new("Guess", "guess")
    elif it["title"] == "Marc Jacobs": more[i] = new("Franck Olivier", "franck-olivier")
    elif it["title"].startswith("All 66"): it["title"] = "All brands A–Z"
brands.append({"title": "Arabian houses", "type": "HTTP", "url": "/collections/arabian-perfume", "items": [
    new(t, h) for t, h in [("Lattafa", "lattafa"), ("Armaf", "armaf"), ("Afnan", "afnan"), ("Maison Alhambra", "maison-alhambra"),
                           ("Swiss Arabian", "swiss-arabian"), ("Rasasi", "rasasi"), ("Arabiyat Prestige", "arabiyat-prestige")]]})
out["sw-main"] = main
foot = [conv(i) for i in M["sw-footer-brands"]["items"]] + [new("Lattafa", "lattafa"), new("Guess", "guess")]
out["sw-footer-brands"] = foot
dr = [conv(i) for i in M["sw-drawer"]["items"]]
find(find(dr, "Fragrance")["items"], "Houses")["items"] += [new("Lattafa", "lattafa"), new("Armaf", "armaf")]
out["sw-drawer"] = dr
res = {h: {"id": M[h]["id"], "title": M[h]["title"], "handle": h, "items": v} for h, v in out.items()}
json.dump(res, open(ROOT / "docs/seo/new_brand_menus_2026-11-06.json", "w"), ensure_ascii=False, indent=1)
for h, v in res.items(): print(h, len(json.dumps(v, ensure_ascii=False)))

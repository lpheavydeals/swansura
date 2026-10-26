"""Per-listing 'related' rows from the prototype's listing(): facet links (scent families on Fragrance,
concerns on skin categories), 'Popular searches' (up to 10 live keyword pages sharing products, most
overlap first) and 'Explore more' (other categories + the listing's top 12 brands by catalogue size).
Output: docs/seo/proto_related.json {collection handle: {facet_label, facet, chips, explore}} for the
custom.related (json) collection metafield, read by sections/sw-p-collection.liquid."""
import ast
import json
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from proto_menus import ROOT, link  # noqa: E402

X = json.load(open(ROOT / "docs/data/prototype_export.json"))
P = {str(p["id"]): p for p in json.load(open(ROOT / "prototype/products.json"))}
for f in json.load(open(ROOT / "docs/seo/brand_mixup_fix_2026-10-26.json"))["products"]:  # corrected brands
    P[f["id"].rsplit("/", 1)[1]]["brand"] = f["vendor"]
L = X["listings"]
ids = {r: (ast.literal_eval(v["ids"]) if isinstance(v["ids"], str) else v["ids"]) for r, v in L.items()}
BR = X["brands"]
count = {}
for p in P.values():
    count[p["brand"]] = count.get(p["brand"], 0) + 1


def slug(b):
    return (BR.get(b) or {}).get("slug") or re.sub(r"[^a-z0-9]+", "-", b.lower()).strip("-")


def u(route):
    return link("", route)["url"]


live_kw = [k for k in X["kw"] if len(ids.get("k-" + k["s"], [])) >= 2]
CATS = X["cats"]
out = {}
for r, v in L.items():
    lst = ids[r]
    s = set(lst)
    kind, key = v["kind"], v["key"]
    facet_label, facet = "", []
    if kind == "c" and key == "fragrance":
        facet_label = "Shop by scent family"
        facet = [[L["scent-" + k]["title"].replace(" fragrances", ""), u("scent-" + k)] for k in ("oud", "amber", "floral", "woody", "fresh")]
    elif kind == "c" and CATS[key]["world"] == "skin" and key != "all":
        facet_label = "Shop by concern"
        facet = [[L[c]["title"], u(c)] for c in L if c.startswith("concern-") and set(ids[c]) & s]
    ks = [k for k in live_kw if k["s"] != key and set(ids["k-" + k["s"]]) & s]
    ks.sort(key=lambda k: -len(set(ids["k-" + k["s"]]) & s))
    chips = [[k["k"], u("k-" + k["s"])] for k in ks[:10]]
    brands = list(dict.fromkeys(P[i]["brand"] for i in lst if i in P))
    brands.sort(key=lambda b: -count.get(b, 0))
    explore = [[c["name"], u("c-" + k)] for k, c in CATS.items() if not (kind == "c" and k == key)]
    explore += [[b, u("b-" + slug(b))] for b in brands[:12]]
    m = re.match(r"^/collections/([^/?]+)$", u(r))
    if m:
        out[m.group(1)] = {"facet_label": facet_label, "facet": facet, "chips": chips, "explore": explore}
json.dump(out, open(ROOT / "docs/seo/proto_related.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "collections;", sum(1 for v in out.values() if v["facet"]), "with facet links")
print(json.dumps(out.get("concern-acne"), ensure_ascii=False)[:900])

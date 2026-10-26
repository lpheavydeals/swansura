"""Per-product prototype data for the theme: custom.sw (json), one metafield per active product.

The theme rebuilds the prototype's product-page FAQ, filters and badges from it, so the store keeps
one compact record instead of the full FAQ text.

  t  product type (prototype subtype)        s  skin/hair types        c  concerns
  k  Studio pick (bool)                      f  scent family (fragrance)
  w  For him / For her / Unisex (fragrance)  n  notes {top, heart, base} (fragrance)
  g  key ingredient names (skincare)
  a  prototype FAQ answers that depend on the product:
     fragrance -> [what it smells like]; others -> [what it is, key ingredients, how to use, types]
  r  rank in the prototype's default order (lower first)

Inputs:  docs/data/prototype_export.json, prototype/products.json, product backup (active ids)
Outputs: docs/seo/proto_product_facets.jsonl (MetafieldsSetInput per product)
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
X = json.load(open(ROOT / "docs/data/prototype_export.json"))
P = json.load(open(ROOT / "prototype/products.json"))
ACTIVE = set()
for line in open(ROOT / "docs/backups/products_before_day4_2026-10-26.jsonl"):
    r = json.loads(line)
    if r.get("status") == "ACTIVE":
        ACTIVE.add(r["id"].rsplit("/", 1)[1])
ORDER = {str(i): n for n, i in enumerate(X["listings"]["c-all"]["ids"])}


def clean_notes(n):
    """Drop description text the prototype's note parser swept in ('Oakmoss - 1 x 75ml ...',
    'Sandalwood Focus opens with ...'): cut at ' - ' and stop at the first item longer than four words."""
    if not n:
        return n
    out = {}
    for k, s in n.items():
        items = []
        for it in (s or "").split(" - ")[0].split(" Set Includes")[0].split(","):
            it = it.strip()
            if len(it.split()) > 4:
                break
            if it:
                items.append(it)
        out[k] = ", ".join(items)
    return out

out = []
for p in P:
    pid = str(p["id"])
    v = X["products"].get(pid)
    if not v or pid not in ACTIVE:
        continue
    a = [x[1] for x in v["faq"]]
    d = {"t": v["sub"], "s": v["skin"], "c": v["concerns"], "k": v["pick"], "r": ORDER.get(pid, 9999)}
    if v["cat"] == "fragrance":
        n = clean_notes(v["notes"])
        if n != v["notes"]:  # rebuild the prototype's 'smells like' answer from the cleaned notes
            a[0] = f"It opens with {n['top']}, settles into {n['heart']}, and dries down to {n['base']}."
        d.update({"f": v["fam"], "w": v["for"], "n": n, "a": a[:1]})
    else:
        # A few descriptions open with a customer quote; don't present a review as the product answer.
        if a and a[0][:1] in "\"“":
            a[0] = f"Part of the {p['brand']} range. See the product details above for what it contains."
        d.update({"g": v["ings"], "a": a[:4]})
    out.append({"ownerId": f"gid://shopify/Product/{pid}", "namespace": "custom", "key": "sw", "type": "json",
                "value": json.dumps(d, ensure_ascii=False, separators=(",", ":"))})

with open(ROOT / "docs/seo/proto_product_facets.jsonl", "w") as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
print(len(out), "products;", sum(len(o["value"]) for o in out), "bytes")

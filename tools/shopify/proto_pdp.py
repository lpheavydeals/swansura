"""Per-product PDP data from the prototype -> custom.pdp (json), one metafield per active product.

Input: docs/data/prototype_pdp.json (tools/proto/export_pdp.js), product backup (active ids + handles).
  cat   skincare / haircare / bath-body / fragrance (breadcrumb + 'View all' link)
  ben   benefit line under the price; more = it was shortened ('Read more')
  chips benefit chips; how = how-to-use bullets
  pair  'Frequently bought together' / 'Complete the ritual' (handles)
  sim   'You may also like' (handles); "More from <brand>" comes from the brand collection (prototype order)
  kw    'Part of our … edits' + 'Shop related' chips: [label, live URL]
Output: docs/seo/proto_pdp.jsonl (MetafieldsSetInput per product)
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/shopify"))
from proto_menus import link  # noqa: E402  (route -> live URL)

D = json.load(open(ROOT / "docs/data/prototype_pdp.json"))
ACTIVE, HANDLE = set(), {}
for line in open(ROOT / "docs/backups/products_before_day4_2026-10-26.jsonl"):
    r = json.loads(line)
    pid = r["id"].rsplit("/", 1)[1]
    HANDLE[pid] = r["handle"]
    if r.get("status") == "ACTIVE":
        ACTIVE.add(pid)


def clean_ben(b):
    """Drop benefit lines the prototype's summary() mangled: cut at an abbreviation ('Elie Saab … No.', 'S.T.'),
    customer quotes used as product copy, and placeholder text."""
    b = (b or "").strip()
    if len(b) < 30 or b.endswith(" No.") or b[:1] in "\"“'‘" or "short product description" in b.lower():
        return ""
    return b


def handles(ids):
    return [HANDLE[i] for i in ids if i in ACTIVE]


out = []
for pid, v in D.items():
    if pid not in ACTIVE:
        continue
    d = {"cat": v["cat"], "ben": clean_ben(v["ben"]), "more": v["more"], "chips": v["chips"], "how": v["how"],
         "pair": handles(v["pair"]), "sim": handles(v["sim"]),
         "kw": [[k, link(k, "#" + r)["url"]] for k, r in v["kw"]]}
    out.append({"ownerId": f"gid://shopify/Product/{pid}", "namespace": "custom", "key": "pdp", "type": "json",
                "value": json.dumps(d, ensure_ascii=False, separators=(",", ":"))})

with open(ROOT / "docs/seo/proto_pdp.jsonl", "w") as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
print(len(out), "products;", sum(len(o["value"]) for o in out), "bytes")

# Structured ingredient lists (prototype p.inci: [{n: component, l: [[name, marker]], g: {marker: label}}]) for the
# PDP 'Ingredients' block that sw-proto.js renders like inciBlock() -> custom.inci_data (json)
P = json.load(open(ROOT / "prototype/products.json"))
inci = [{"ownerId": f"gid://shopify/Product/{p['id']}", "namespace": "custom", "key": "inci_data", "type": "json",
         "value": json.dumps(p["inci"], ensure_ascii=False, separators=(",", ":"))}
        for p in P if p.get("inci") and str(p["id"]) in ACTIVE]
with open(ROOT / "docs/seo/proto_inci.jsonl", "w") as f:
    for o in inci:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
print(len(inci), "ingredient lists;", sum(len(o["value"]) for o in inci), "bytes")

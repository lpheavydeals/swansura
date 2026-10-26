"""Prototype FAQs, eyebrows and copy for the collections that already existed (categories, product types,
brands), plus the three brand pages the store had no collection for.

Inputs:  same as proto_collections_create.py
Outputs: docs/seo/proto_collection_existing_updates.jsonl (CollectionUpdateInput: id + metafields [+ copy])
         docs/seo/proto_brand_creates.jsonl                (CollectionCreateInput for Highborn London, anatomē,
                                                            Swansura Selection)

Rules
- custom.faq = the prototype FAQ list. Brand FAQs whose product count differs from the live collection
  lose the number ("4 products, from £18.99 ..." -> "Products from £18.99 ...").
- Listing collections also get custom.eyebrow. The five big categories (skincare, haircare, bodycare,
  fragrance, sets-combos) now hold the prototype's products, so they get the prototype intro as the
  description plus the 'About this page' copy (left out on Day 4).
- Highborn London and anatomē are vendor-based smart collections; Swansura Selection is a manual list
  (the store-name vendor also carries the four demo products).
"""
import json
import re

from proto_collections_create import AUDIT, COPY, P, PLAN, ROOT, ROUTES, STORE, X, copy_html, faq, mf

LIVE = {}
for line in open(ROOT / "docs/backups/collection_membership_before_2026-10-26.jsonl"):
    r = json.loads(line)
    if "handle" in r:
        LIVE[r["handle"]] = r["id"]
COUNTS = {}
for line in open(ROOT / "docs/backups/collections_before_day4_2026-10-26.jsonl"):
    r = json.loads(line)
    if "handle" in r:
        COUNTS[r["handle"]] = r["productsCount"]["count"]
CATS = {"c-skincare", "c-haircare", "c-bath-body", "c-fragrance", "c-gifts"}
NEW_BRANDS = {"Highborn London": "vendor", "anatomē": "vendor", "Swansura Selection": "manual"}
made = {c["route"] for c in PLAN["create"]}


def jfaq(pairs):
    return mf("faq", "json", json.dumps(pairs, ensure_ascii=False))


updates, creates = [], []
for r, h in sorted(ROUTES.items()):
    if r in made or r == "c-all" or h not in LIVE:
        continue
    if r.startswith("b-"):
        name = next((n for n, b in X["brands"].items() if b["slug"] == r[2:]), None)
        if not name:
            continue
        b = X["brands"][name]
        pairs = [[q, a] for q, a in b["faq"]]
        if COUNTS.get(h) != b["count"]:
            pairs = [[q, re.sub(r"^\d+ products?, from", "Products from", a)] for q, a in pairs]
        updates.append({"id": LIVE[h], "metafields": [jfaq(pairs)]})
        continue
    l = X["listings"][r]
    mfs = [mf("eyebrow", "single_line_text_field", l["eyebrow"])]
    if faq(r):
        mfs.append(jfaq(faq(r)))
    upd = {"id": LIVE[h], "metafields": mfs}
    if r in CATS:
        upd["descriptionHtml"] = f"<p>{l['intro']}</p>"
        mfs += [mf("seo_heading", "single_line_text_field", COPY[r]["h2"]),
                mf("seo_copy", "multi_line_text_field", copy_html(r))]
    updates.append(upd)

for name, kind in NEW_BRANDS.items():
    b = X["brands"][name]
    r = "b-" + b["slug"]
    a = AUDIT[r]
    mfs = [mf("h1", "single_line_text_field", a["h1"][0]), jfaq([[q, x] for q, x in b["faq"]])]
    if r in COPY:
        mfs += [mf("seo_heading", "single_line_text_field", COPY[r]["h2"]),
                mf("seo_copy", "multi_line_text_field", copy_html(r))]
    if kind == "vendor":
        src = {"title": "Brand", "inclusion": {"matchType": "ALL", "conditions": [
            {"productVendor": {"matchType": "ANY", "relation": "EQUALS", "values": [name]}}]}}
    else:
        ids = [str(p["id"]) for p in P if p["brand"] == name and STORE.get(str(p["id"]), {}).get("status") == "ACTIVE"]
        src = {"title": "Brand", "inclusion": {"selections": [{"productId": f"gid://shopify/Product/{i}"} for i in ids]}}
    creates.append({"handle": b["slug"], "title": name, "sortOrder": "BEST_SELLING", "templateSuffix": "brand",
                    "descriptionHtml": f"<p>{b['story']}</p>",
                    "seo": {"title": a["title"], "description": a["desc"]}, "metafields": mfs, "sources": [src]})

if __name__ == "__main__":
    with open(ROOT / "docs/seo/proto_collection_existing_updates.jsonl", "w") as f:
        for u in updates:
            f.write(json.dumps(u, ensure_ascii=False) + "\n")
    with open(ROOT / "docs/seo/proto_brand_creates.jsonl", "w") as f:
        for c in creates:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(len(updates), "updates;", len(creates), "brand creates",
          [(c["handle"], len(c["sources"][0]["inclusion"].get("selections", []))) for c in creates])

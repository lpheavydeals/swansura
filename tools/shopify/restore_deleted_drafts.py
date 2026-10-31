"""Restore the 35 draft products deleted on 31 Oct 2026 (user: 'Reverse the Deleted Drafts Also').

Sources: docs/backups/old_drafts_deleted_2026-10-31.json (33), vilvah_aloe_pack2_draft_deleted_2026-10-31.json,
vilvah_melt_in_milk_draft_deleted_2026-10-31.json. Each comes back as a DRAFT with the same title, handle, vendor,
type, tags, description, SEO, price, compare-at price, SKU, barcode, stock (at 'Swansura - The Body Studio') and
collections. Photos cannot be restored from Shopify: deleting a product deleted its image files (CDN URLs 404).
Writes docs/seo/restore_drafts_2026-10-31.json: list of productSet inputs, in batches.
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
B = ROOT / "docs/backups"
P = json.load(open(B / "old_drafts_deleted_2026-10-31.json"))["products"]
P += [json.load(open(B / "vilvah_aloe_pack2_draft_deleted_2026-10-31.json"))["product"],
      json.load(open(B / "vilvah_melt_in_milk_draft_deleted_2026-10-31.json"))["product"]]
COLL = {"vilvah": "687767716227", "deyga": "687768011139", "jo-milano-paris-1": "689023713667", "sunscreen": "689292804483",
        "fragrance": "689527685507", "gift-sets": "689549148547", "acqua-di-parma": "711465107843",
        "giorgia-armani": "711857176963", "sets-combos": "713096921475", "juicy-couture": "713590473091"}
LOC = "gid://shopify/Location/111879553411"
out = []
for p in P:
    v = p["variants"]["nodes"][0]
    assert len(p["variants"]["nodes"]) == 1 and p["options"][0]["name"] == "Title"
    var = {"optionValues": [{"optionName": "Title", "name": "Default Title"}], "price": v["price"],
           "inventoryItem": {"tracked": True},
           "inventoryQuantities": [{"locationId": LOC, "name": "available", "quantity": max(v["inventoryQuantity"] or 0, 0)}]}
    if v.get("sku"):
        var["sku"] = v["sku"]
    if v.get("compareAtPrice"):
        var["compareAtPrice"] = v["compareAtPrice"]
    bc = [b["value"] for b in (v.get("barcodes") or {}).get("nodes", []) if b.get("value")]
    if bc:
        var["barcodes"] = [{"value": bc[0]}]
    inp = {"title": p["title"], "handle": p["handle"], "status": "DRAFT", "vendor": p["vendor"],
           "productType": p.get("productType") or "", "tags": p.get("tags") or [], "descriptionHtml": p["descriptionHtml"],
           "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}], "variants": [var],
           "collections": ["gid://shopify/Collection/" + COLL[c["handle"]] for c in p["collections"]["nodes"]]}
    seo = {k: val for k, val in (p.get("seo") or {}).items() if val}
    if seo:
        inp["seo"] = seo
    mfs = [m for m in (p.get("metafields") or {}).get("nodes", []) if m["namespace"] not in ("global",)]
    if mfs:
        inp["metafields"] = [{"namespace": m["namespace"], "key": m["key"], "type": m["type"], "value": m["value"]} for m in mfs]
    out.append({"old_id": p["id"], "title": p["title"], "photos_lost": len(p["media"]["nodes"]), "input": inp})
json.dump(out, open(ROOT / "docs/seo/restore_drafts_2026-10-31.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "products;", sum(o["photos_lost"] for o in out), "photos lost;",
      sum(o["input"]["variants"][0]["inventoryQuantities"][0]["quantity"] for o in out), "units")

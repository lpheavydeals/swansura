"""Turn docs/seo/new_brand_copy_2026-11-06.jsonl into store writes (user OK 6 Nov 2026).

- collectionUpdate seo {title (unchanged), description} for 30 collections (title is resent: a seo
  input with only one field can blank the other).
- metafieldsSet: custom.seo_heading + custom.seo_copy for all 30; custom.faq for the 28 brands
  (existing genuine/delivery answers kept, new answers added; Armaf's stale '1 product' and
  'no gift sets' answers dropped); custom.brand.others (+ Armaf story/count); hubs: custom.related
  explore pills + the price-range FAQ answer from live prices.
Before-state: docs/backups/new_brand_copy_before_2026-11-06.json.
Output: docs/seo/new_brand_copy_apply_2026-11-06.json (seo list + metafield batches of <= 25).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ROWS = [json.loads(l) for l in open(ROOT / "docs/seo/new_brand_copy_2026-11-06.jsonl")]
BEFORE = {c["handle"]: c for c in json.load(open(ROOT / "docs/backups/new_brand_copy_before_2026-11-06.json"))["collections"]}
CAT = json.load(open(ROOT / "docs/data/new_brand_catalogue_2026-11-06.json"))

seo, mfs = [], []
for r in ROWS:
    h = r["handle"]
    c = BEFORE[h]
    cid = c["id"]
    seo.append({"id": cid, "seo": {"title": c["seo"]["title"], "description": r["seo_description"]}})
    mf = lambda k, t, v: {"ownerId": cid, "namespace": "custom", "key": k, "type": t, "value": v}
    mfs += [mf("seo_heading", "single_line_text_field", r["seo_heading"]),
            mf("seo_copy", "multi_line_text_field", r["seo_copy"])]
    faq = json.loads(c["faq"]["value"])
    if "others" in r:  # brand page
        if h == "armaf":
            faq = [q for q in faq if not q[0].startswith(("Which Armaf products", "Does Armaf come"))]
        faq = faq[:1] + r["faq_add"] + faq[1:]  # genuine, new answers, delivery
        br = json.loads(c["br"]["value"])
        br["others"] = [o for o in r["others"] if o[1] != f"/collections/{h}"]
        if r.get("story"):
            br["story"] = r["story"]
        br["count"] = len(CAT[h])
        mfs += [mf("faq", "json", json.dumps(faq, ensure_ascii=False)), mf("brand", "json", json.dumps(br, ensure_ascii=False))]
    else:  # hub page
        prices = [float(p) for x in CAT[h] for p in x["prices"]]
        faq[0][1] = f"Prices run from £{min(prices):.2f} to £{max(prices):.2f}."
        rel = json.loads(c["rel"]["value"])
        have = {u for _, u in rel["explore"]}
        rel["explore"] += [e for e in r["explore_add"] if e[1] not in have]
        mfs += [mf("faq", "json", json.dumps(faq, ensure_ascii=False)), mf("related", "json", json.dumps(rel, ensure_ascii=False))]

batches = [mfs[i:i + 25] for i in range(0, len(mfs), 25)]
json.dump({"seo": seo, "metafield_batches": batches}, open(ROOT / "docs/seo/new_brand_copy_apply_2026-11-06.json", "w"),
          ensure_ascii=False, indent=1)
print(len(seo), "collections;", len(mfs), "metafields in", len(batches), "batches")

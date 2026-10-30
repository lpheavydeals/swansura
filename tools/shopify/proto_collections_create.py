"""Create the prototype's listing pages as store collections (concerns, price bands, keyword pages,
ranges, scent families) with SEO, keyword H1, 'About this page' copy and FAQs.

Inputs:  docs/data/proto_collections_plan.json   (tools/shopify/proto_collections_plan.py)
         docs/data/prototype_export.json         (tools/proto/extract_data.js: ranked ids, FAQs)
         docs/seo/prototype_seoaudit_2026-10-26.json, prototype/seocopy.js
         docs/backups/products_before_day4_2026-10-26.jsonl (which prototype ids exist in the store)
Outputs: docs/seo/proto_collection_creates.jsonl (CollectionCreateInput per collection)
         docs/seo/proto_collection_faq.jsonl      (custom.faq for the existing collections)

Rules
- Membership = the prototype listing in its ranked order (manual selections, sort MANUAL), price bands
  included, so every page shows exactly what the prototype shows.
- seo.title / seo.description / custom.h1 from the prototype audit; custom.seo_heading + custom.seo_copy
  from seocopy.js; custom.eyebrow + the intro (collection description) as
  the prototype page header renders them; custom.faq = the prototype's FAQ list ([[q, a], ...]) for the theme's FAQ band.
- Copy links point at the new collection handles where they exist.
"""
import html
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
PLAN = json.load(open(ROOT / "docs/data/proto_collections_plan.json"))
X = json.load(open(ROOT / "docs/data/prototype_export.json"))
AUDIT = {r["r"]: r for r in json.load(open(ROOT / "docs/seo/prototype_seoaudit_2026-10-26.json"))}
COPY = json.loads(subprocess.run(
    ["node", "-e", 'global.window={};require("vm").runInThisContext(require("fs").readFileSync("prototype/seocopy.js","utf8"));'
     'process.stdout.write(JSON.stringify(window.SW_COPY))'], cwd=ROOT, capture_output=True, text=True, check=True).stdout)
P = json.load(open(ROOT / "prototype/products.json"))
STORE = {}
for line in open(ROOT / "docs/backups/products_before_day4_2026-10-26.jsonl"):
    r = json.loads(line)
    if "handle" in r:
        STORE[r["id"].rsplit("/", 1)[1]] = r

# Existing collections (Day 4) + the new ones: prototype route -> store handle.
ROUTES = {
    "c-all": "all", "c-skincare": "skincare", "c-haircare": "haircare", "c-bath-body": "bodycare",
    "c-fragrance": "fragrance", "c-gifts": "sets-combos",
    "b-deyga": "deyga", "b-vilvah": "vilvah", "b-hemel": "hemel",
    "b-jo-milano": "jo-milano", "b-signature-d-orient": "signature-dorient", "b-tom-ford": "tom-ford",
    "b-yves-saint-laurent": "yves-saint-laurent", "b-philipp-plein": "philipp-plein", "b-antonio-banderas": "antonio-banderas",
    "b-jean-paul-gaultier": "jean-paul-gaultier", "b-joop": "joop",
    "k-face-serum": "serum", "k-face-wash": "cleanser", "k-moisturiser": "moisturizers-gels", "k-sunscreen": "sunscreen",
    "k-toner": "toner", "k-lip-balm": "lip-balm", "k-lip-scrub": "lip-scrub", "k-shampoo": "shampoo",
    "k-hair-oil": "hair-oil", "k-deodorant": "deodrants", "k-face-mask": "face-mask-pack",
}
for c in PLAN["create"]:
    ROUTES[c["route"]] = c["handle"]
for line in open(ROOT / "docs/backups/collections_before_day4_2026-10-26.jsonl"):
    r = json.loads(line)
    if "handle" in r and r["productsCount"]["count"] > 0:
        ROUTES.setdefault("b-" + r["handle"], r["handle"])
BY_ID = {str(p["id"]): p["h"] for p in P}


def url(route):
    if route in ROUTES:
        return f"/collections/{ROUTES[route]}"
    if route.startswith("p-"):
        h = BY_ID.get(route[2:])
        return f"/products/{h}" if h else "/collections/all"
    if route.startswith("journal-"):
        return "/blogs/journal/" + route[8:]
    return {"rituals": "/pages/rituals", "wishlist": "/pages/wishlist", "brands": "/collections", "journal": "/blogs/journal",
            "offers": "/pages/offers", "advent": "/pages/advent", "sitemap": "/pages/sitemap",
            "page-about": "/pages/about", "page-faq": "/pages/faq", "page-contact": "/pages/contact", "page-delivery": "/pages/shipping",
            "page-shipping": "/policies/shipping-policy", "page-refunds": "/policies/refund-policy",
            "page-privacy": "/policies/privacy-policy", "page-terms": "/policies/terms-of-service"}.get(
        route, "/search?type=product&q=" + re.sub(r"^[a-z]+-", "", route).replace("-", "+"))


def md(t):
    t = html.escape(t, quote=False)
    return re.sub(r"\[([^\]]+)\]\(#([^)]+)\)", lambda m: f'<a href="{url(m.group(2))}">{m.group(1)}</a>', t)


def copy_html(route):
    return "".join((f"<h3>{html.escape(b['h3'], quote=False)}</h3>" if b.get("h3") else "") + f"<p>{md(b['p'])}</p>"
                   for b in COPY[route]["blocks"])


def faq(route):
    l = X["listings"].get(route) or {}
    return [[q, a] for q, a in (l.get("faq") or [])]


def mf(key, typ, value):
    return {"namespace": "custom", "key": key, "type": typ, "value": value}


if __name__ == "__main__":
    out = []
    for c in PLAN["create"]:
        r, l, a = c["route"], X["listings"][c["route"]], AUDIT[c["route"]]
        gids = [f"gid://shopify/Product/{i}" for i in l["ids"] if i in STORE and STORE[i]["status"] == "ACTIVE"]
        assert len(a["title"]) <= 60 and len(a["desc"]) <= 160, r
        mfs = [mf("h1", "single_line_text_field", a["h1"][0]), mf("eyebrow", "single_line_text_field", l["eyebrow"])]
        if r in COPY:
            mfs += [mf("seo_heading", "single_line_text_field", COPY[r]["h2"]),
                    mf("seo_copy", "multi_line_text_field", copy_html(r))]
        if faq(r):
            mfs.append(mf("faq", "json", json.dumps(faq(r), ensure_ascii=False)))
        out.append({"handle": c["handle"], "title": l["title"], "sortOrder": "MANUAL",
                    "descriptionHtml": f"<p>{html.escape(l['intro'], quote=False)}</p>",
                    "seo": {"title": a["title"], "description": a["desc"]}, "metafields": mfs,
                    "sources": [{"source": {"title": "Prototype selection", "inclusion": {
                        "selections": [{"productId": g} for g in gids]}}}]})
    with open(ROOT / "docs/seo/proto_collection_creates.jsonl", "w") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    # FAQs for the collections that already exist.
    with open(ROOT / "docs/seo/proto_collection_faq.jsonl", "w") as f:
        made = {c["route"] for c in PLAN["create"]}
        for r, h in sorted(ROUTES.items()):
            if r not in made and r != "c-all" and faq(r):
                f.write(json.dumps({"handle": h, "route": r, "faq": faq(r)}, ensure_ascii=False) + "\n")
    print(len(out), "collections;", sum(len(o["sources"][0]["source"]["inclusion"]["selections"]) for o in out), "selections")

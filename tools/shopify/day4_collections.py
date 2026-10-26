"""Day 4 collection SEO (title/description, keyword H1, 'About this page' copy) for 79 store collections.

Inputs:  prototype/seocopy.js (window.SW_COPY: h2 + blocks per prototype route)
         docs/seo/prototype_seoaudit_2026-10-26.json (H1 / title / description per prototype route)
         docs/backups/collections_before_day4_2026-10-26.jsonl (collection ids, live values before the change)
         prototype/products.json (product handles for in-text links)
Outputs: docs/seo/day4_collection_updates.jsonl (collectionUpdate inputs)
         docs/seo/day4_collection_changes.csv  (old -> new; also the undo list)

Rules
- seo.title / seo.description and custom.h1 from the prototype audit for every mapped route.
- custom.seo_heading (H2) + custom.seo_copy (HTML) for brands, keyword pages and Gifts. The four big
  categories get no copy: their live collections hold far fewer products than the prototype pages
  (e.g. skincare 32 vs 109), so the copy's counts and examples would be wrong there.
- Product counts in the copy that differ from the live collection are reworded without a number.
- The Deyga/Vilvah collection descriptions ('sample Deyga' / 'sample vilvah') become a real intro.
- Links: [text](#route) -> /collections/<handle> for mapped routes, /products/<handle> for products,
  else a store search for the keyword.
"""
import csv
import html
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = json.load(open(ROOT / "prototype/products.json"))
AUDIT = {r["r"]: r for r in json.load(open(ROOT / "docs/seo/prototype_seoaudit_2026-10-26.json"))}
COPY = json.loads(subprocess.run(
    ["node", "-e", 'global.window={};require("vm").runInThisContext(require("fs").readFileSync("prototype/seocopy.js","utf8"));'
     'process.stdout.write(JSON.stringify(window.SW_COPY))'], cwd=ROOT, capture_output=True, text=True, check=True).stdout)
LIVE = {}
for line in open(ROOT / "docs/backups/collections_before_day4_2026-10-26.jsonl"):
    r = json.loads(line)
    if "handle" in r:
        LIVE[r["handle"]] = r

SPECIAL = {
    "c-skincare": "skincare", "c-haircare": "haircare", "c-bath-body": "bodycare", "c-fragrance": "fragrance",
    "c-gifts": "sets-combos",
    "b-deyga": "milk-drop-brightening-serum-1", "b-vilvah": "milk-drop-brightening-serum", "b-hemel": "hemel-h",
    "b-jo-milano": "luxury-collection-1", "b-signature-d-orient": "signature-sillage-dorient", "b-tom-ford": "tomford",
    "b-yves-saint-laurent": "ysl", "b-philipp-plein": "phillip-plein", "b-antonio-banderas": "antonio",
    "b-jean-paul-gaultier": "jean-paul", "b-joop": "joop-homme",
    "k-face-serum": "serum", "k-face-wash": "cleanser", "k-moisturiser": "moisturizers-gels", "k-sunscreen": "sunscreen",
    "k-toner": "toner", "k-lip-balm": "lip-balm", "k-lip-scrub": "lip-scrub", "k-shampoo": "shampoo",
    "k-hair-oil": "hair-oil", "k-deodorant": "deodrants", "k-face-mask": "face-mask-pack",
}
ROUTES = dict(SPECIAL)
for r in COPY:
    if r.startswith("b-") and r not in ROUTES and r[2:] in LIVE and LIVE[r[2:]]["productsCount"]["count"] > 0:
        ROUTES[r] = r[2:]
BIG = {"c-skincare", "c-haircare", "c-bath-body", "c-fragrance"}

# Copy counts that differ from the live collection: reworded without a number.
COUNT_FIX = {
    "b-antonio-banderas": [("Our edit includes four bottles", "Our edit includes bottles"),
                           (" The line-up is split evenly, with two fresh scents for men and two sweet ones for women, so you can buy a matching pair as presents.",
                            " The line-up has fresh scents for men and sweet ones for women, so you can buy a matching pair as presents."),
                           ("All four sit in our", "These sit in our")],
    "b-davidoff": [("brings four of them together", "brings several of them together")],
    "b-hermes": [("Our five pieces start at", "Our pieces start at")],
    "b-deyga": [("We stock 73 Deyga products", "We stock a wide range of Deyga products")],
    "b-vilvah": [("We stock 72 Vilvah products", "We stock a wide range of Vilvah products")],
    "k-face-wash": [("We stock nine face washes", "We stock face washes")],
    "k-face-serum": [("brings together 16 serums", "brings together serums")],
    "k-sunscreen": [("has four SPF products", "has SPF products")],
    "k-toner": [("We stock five toners", "We stock toners")],
    "k-lip-balm": [("has 17 balms", "has balms")],
    "k-shampoo": [("has seven natural shampoos", "has natural shampoos")],
    "k-deodorant": [("brings together six options", "brings together natural options")],
    "c-gifts": [("from our 116 gifts", "from our gift edit")],
}
# The four big categories: descriptions without the prototype's product counts.
BIG_DESC = {
    "c-skincare": "Shop natural skincare from Deyga and Vilvah, our official UK partner brands, and Highborn London. 100% authentic, free UK delivery over £40.",
    "c-haircare": "Find a natural shampoo, conditioner or hair oil from Vilvah and Deyga. 100% authentic, shipped from the UK, free UK delivery over £40.",
    "c-bath-body": "Pick up a body butter, scrub, bath bar or body wash from natural brands Deyga and Vilvah. 100% authentic, free UK delivery over £40.",
    "c-fragrance": "Niche and designer perfume in the UK, from minis to rare extraits, all shipped from our UK base. 100% authentic, free UK delivery over £40.",
}
INTRO = {  # replaces the placeholder descriptions shown as the collection intro
    "b-deyga": "<p>Deyga makes natural skin, hair and body care from plant-based ingredients, many grown on its own farm in India. Swansura is Deyga's official UK partner.</p>",
    "b-vilvah": "<p>Vilvah makes natural skin and hair care with goat milk, plant oils and botanicals, made in India. Swansura is Vilvah's official UK partner.</p>",
}

# Collection display names (breadcrumbs, FAQ, schema): brand spelling instead of legacy titles.
# Handles stay the same, so links and menus keep working.
TITLE_FIX = {
    "abercrombie-fitch": "Abercrombie & Fitch", "anna-sui": "Anna Sui", "antonio": "Antonio Banderas",
    "ariana-grande": "Ariana Grande", "calvin-klein": "Calvin Klein", "chloe": "Chloé",
    "milk-drop-brightening-serum-1": "Deyga", "hemel-h": "Hemel", "hermes": "Hermès",
    "jean-paul": "Jean Paul Gaultier", "john-varvatos": "John Varvatos", "joop-homme": "Joop!",
    "paloma": "Paloma Picasso", "phillip-plein": "Philipp Plein", "sap": "SAP",
    "signature-sillage-dorient": "Signature D'orient", "tomford": "Tom Ford",
    "milk-drop-brightening-serum": "Vilvah", "deodrants": "Deodorants",
    "shampoo": "Shampoo & Conditioner", "moisturizers-gels": "Moisturisers & Gels",
}

BY_HANDLE = {p["h"] for p in P}
BY_ID = {str(p["id"]): p["h"] for p in P}


def url(route):
    if route in ROUTES:
        return f"/collections/{ROUTES[route]}"
    if route.startswith("p-"):
        h = BY_ID.get(route[2:]) or (route[2:] if route[2:] in BY_HANDLE else None)
        return f"/products/{h}" if h else "/collections/all"
    m = re.match(r"price-(\d+)-(\d+)", route)
    if m:  # Dawn price filter on the all-products collection
        lo, hi = m.groups()
        return f"/collections/all?filter.v.price.gte={lo}" + (f"&amp;filter.v.price.lte={hi}" if hi != "9999" else "")
    m = re.match(r"(k|concern|scent|range|b|c)-(.+)", route)
    if m:
        return "/search?type=product&q=" + m.group(2).replace("-", "+")
    return {"rituals": "/collections/sets-combos", "brands": "/collections", "journal": "/blogs/news"}.get(route, "/")


def md(t):
    t = html.escape(t, quote=False)
    return re.sub(r"\[([^\]]+)\]\(#([^)]+)\)", lambda m: f'<a href="{url(m.group(2))}">{m.group(1)}</a>', t)


def copy_html(route):
    blocks = COPY[route]["blocks"]
    out = "".join((f"<h3>{html.escape(b['h3'], quote=False)}</h3>" if b.get("h3") else "") + f"<p>{md(b['p'])}</p>" for b in blocks)
    for old, new in COUNT_FIX.get(route, []):
        assert old in out, (route, old)
        out = out.replace(old, new)
    return out


lines, log = [], []
for route, handle in sorted(ROUTES.items()):
    c, a = LIVE[handle], AUDIT[route]
    h1 = a["h1"][0]
    desc = BIG_DESC.get(route, a["desc"])
    for old, new in COUNT_FIX.get(route, []):
        desc = desc.replace(old, new)
    title = a["title"]
    assert len(title) <= 60 and len(desc) <= 160, (route, title, desc)
    upd = {"id": c["id"], "seo": {"title": title, "description": desc}}
    mfs = [{"namespace": "custom", "key": "h1", "type": "single_line_text_field", "value": h1}]
    log += [(handle, route, "seo.title", c["seo"]["title"] or "", title),
            (handle, route, "seo.description", c["seo"]["description"] or "", desc),
            (handle, route, "custom.h1", "", h1)]
    if route not in BIG and route in COPY:
        body = copy_html(route)
        mfs += [{"namespace": "custom", "key": "seo_heading", "type": "single_line_text_field", "value": COPY[route]["h2"]},
                {"namespace": "custom", "key": "seo_copy", "type": "multi_line_text_field", "value": body}]
        log += [(handle, route, "custom.seo_heading", "", COPY[route]["h2"]),
                (handle, route, "custom.seo_copy", "", re.sub("<[^>]+>", "", body)[:100] + "…")]
    if handle in TITLE_FIX and TITLE_FIX[handle] != c["title"]:
        upd["title"] = TITLE_FIX[handle]
        log.append((handle, route, "title", c["title"], TITLE_FIX[handle]))
    if route in INTRO:
        upd["descriptionHtml"] = INTRO[route]
        log.append((handle, route, "descriptionHtml", c["descriptionHtml"], INTRO[route]))
    upd["metafields"] = mfs
    lines.append(upd)

with open(ROOT / "docs/seo/day4_collection_updates.jsonl", "w") as f:
    for l in lines:
        f.write(json.dumps(l, ensure_ascii=False) + "\n")
with open(ROOT / "docs/seo/day4_collection_changes.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["handle", "prototype_route", "field", "before", "after"])
    w.writerows(log)
print(len(lines), "collections;", sum(1 for l in lines if len(l["metafields"]) > 1), "with page copy")

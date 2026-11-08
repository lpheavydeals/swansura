"""Pick the next wave of products for longer descriptions and build the writers' fact file.

Usage:
  python3 tools/shopify/product_desc_facts.py select <scratch> <wave> [N]
      reads  <scratch>/sfall_live.json  (storefront /products.json, all pages, fetched by `fetch`)
             docs/seo/product_descriptions_*.json  (products already done: excluded)
             seo/Swansura_Product_SEO_Merged_2026-11-02.xlsx  ('Final SEO (merged)': keyword + volume)
      writes <scratch>/desc_<wave>_pick.json  (ids to read from Admin: h1, custom.sw, custom.pdp)
  python3 tools/shopify/product_desc_facts.py fetch <scratch>
      writes <scratch>/sfall_live.json
  python3 tools/shopify/product_desc_facts.py build <scratch> <wave>
      reads  <scratch>/desc_<wave>_admin.json  (Admin nodes: id handle h1 sw pdp descriptionHtml)
             <scratch>/sf2/{perfume-for-men,perfume-for-women,unisex-perfume,scent-*}.json  (fresh storefront dumps)
      writes docs/data/product_desc_facts_<wave>.json  (same shape as product_desc_facts_2026-11-08.json)

  Add --skin to select/build for Vilvah + Deyga skincare (no perfume filter; facts from custom.inci/sw/pdp;
  Admin query must also return inci: metafield(namespace:"custom", key:"inci")).

Rules (same as wave 1, 8 Nov 2026): in stock, has photos, current description under 80 words, a perfume,
one listing per scent, ranked by UK volume of the product keyword (then secondary volume).
"""
import html
import json
import pathlib
import re
import sys
import time
import unicodedata
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
UA = {"User-Agent": "swansura-seo-check"}
PERFUME = re.compile(r"parfum|toilette|cologne|extrait|perfume|fragrance|body mist|attar|\boud\b|edp|edt", re.I)
SKIN = re.compile(r"\b(serum|cream|lotion|shampoo|conditioner|soap|balm|scrub|face|hair|toner|gel|mask|butter|oil|wash|kit|comb|loofah)\b", re.I)
NOT_SKIN_BRANDS = {"vilvah", "deyga", "highborn london"}
DUP_SKIP = re.compile(r"full house|caput mundi|cyth[eè]re|rougue|game of spade rouge|wildcard for unisex", re.I)  # duplicate listings waiting for the client


def words(h):
    return len(re.sub(r"<[^>]+>", " ", html.unescape(h or "")).split())


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]+", " ", s)


def scent_key(t):
    t = norm(t.split(" – ")[0])
    t = re.sub(r"\b\d+(\.\d+)?\s*(ml|g)\b|\bminiature\b|\btravel\b|\bspray\b", " ", t)
    return " ".join(t.split())


def fetch(S):
    out, page = [], 1
    while True:
        u = f"https://www.swansura.com/products.json?limit=250&page={page}"
        r = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA)))["products"]
        if not r:
            break
        out += r
        page += 1
        time.sleep(1)
    json.dump(out, open(S / "sfall_live.json", "w"))
    print(len(out), "products")


def keywords():
    import openpyxl
    ws = openpyxl.load_workbook(ROOT / "seo/Swansura_Product_SEO_Merged_2026-11-02.xlsx", read_only=True)["Final SEO (merged)"]
    rows = list(ws.iter_rows(values_only=True))
    hd = rows[0]
    ix = {k: hd.index(k) for k in ("Brand", "Product name (sheet)", "Primary keyword", "Primary vol.", "Secondary keyword", "Secondary vol.", "FINAL H1")}
    return [{k: r[i] for k, i in ix.items()} for r in rows[1:] if r[ix["Primary keyword"]]]


def match_kw(title, kws):
    tt = set(norm(title).split())
    best, bs = None, 0
    for k in kws:
        h1 = set(norm(k["FINAL H1"] or "").split())
        if not h1:
            continue
        s = len(h1 & tt) / len(h1)
        if s > bs:
            best, bs = k, s
    return best if bs >= 0.85 else None


SKINCARE = {"vilvah", "deyga"}


def select(S, wave, n, skin=False):
    done = set()
    for f in (ROOT / "docs/seo").glob("product_descriptions_*.json"):
        done |= {r["handle"] for r in json.load(open(f))}
    kws = keywords()
    cand = []
    for p in json.load(open(S / "sfall_live.json")):
        if p["handle"] in done or not p["images"] or not any(v["available"] for v in p["variants"]):
            continue
        if words(p["body_html"]) >= 80 or DUP_SKIP.search(p["title"]):
            continue
        if skin:
            if p["vendor"].lower() not in SKINCARE:
                continue
        elif p["vendor"].lower() in NOT_SKIN_BRANDS or not PERFUME.search(p["title"]) or SKIN.search(p["title"].split(" – ")[0]):
            continue
        k = match_kw(p["title"], kws)
        cand.append((-(k["Primary vol."] or 0) if k else 0, -(k["Secondary vol."] or 0) if k else 0, p["title"], p, k))
    cand.sort(key=lambda x: x[:3])
    live = {p["handle"]: p for p in json.load(open(S / "sfall_live.json"))}
    seen, pick = {scent_key(live[h]["title"]) for h in done if h in live}, []  # one description per scent, across waves
    for *_, p, k in cand:
        sk = scent_key(p["title"])
        if sk in seen:
            continue
        seen.add(sk)
        pick.append({"id": f"gid://shopify/Product/{p['id']}", "handle": p["handle"], "title": p["title"], "vendor": p["vendor"],
                     "words": words(p["body_html"]), "kw": k})
        if len(pick) == n:
            break
    json.dump(pick, open(S / f"desc_{wave}_pick.json", "w"), ensure_ascii=False, default=str, indent=1)
    print(len(cand), "candidates;", len(pick), "picked;", sum(1 for x in pick if x["kw"] and x["kw"]["Primary vol."]), "with volume")


def build_skin(S, wave):
    """Vilvah/Deyga: facts from custom.inci / custom.sw / custom.pdp; 'similar' = the product's own pdp pair/sim lists, in stock."""
    pick = {p["id"]: p for p in json.load(open(S / f"desc_{wave}_pick.json"))}
    admin = json.load(open(S / f"desc_{wave}_admin.json"))
    live = {p["handle"]: p for p in json.load(open(S / "sfall_live.json"))}
    instock = {h: p for h, p in live.items() if any(v["available"] for v in p["variants"]) and p["images"]}
    out = []
    for a in admin:
        p, lp = pick[a["id"]], live[a["handle"]]
        sw = json.loads((a.get("sw") or {}).get("value") or "{}")
        pdp = json.loads((a.get("pdp") or {}).get("value") or "{}")
        k = p["kw"] or {}
        rel = []
        for h in (pdp.get("pair") or []) + (pdp.get("sim") or []):
            h = h if isinstance(h, str) else (h.get("h") or h.get("handle") or "")
            if h in instock and h != a["handle"] and h not in rel:
                rel.append(h)
        out.append({
            "id": a["id"], "handle": a["handle"], "title": lp["title"], "vendor": lp["vendor"],
            "h1": (a.get("h1") or {}).get("value") or lp["title"],
            "primary_keyword": k.get("Primary keyword") or (a.get("h1") or {}).get("value") or lp["title"],
            "volume": k.get("Primary vol.") or 0,
            "secondary_keyword": k.get("Secondary keyword") or "", "secondary_volume": k.get("Secondary vol.") or 0,
            "variants": [[v["title"], v["price"], v["available"]] for v in lp["variants"]],
            "current_description_html": a["descriptionHtml"],
            "current_text": " ".join(re.sub(r"<[^>]+>", " ", html.unescape(a["descriptionHtml"] or "")).split()),
            "inci": (a.get("inci") or {}).get("value") or "",
            "facets": {k2: sw.get(k2) for k2 in ("t", "s", "c", "g", "k")},
            "faq_answers": sw.get("a") or [], "pdp": {k2: pdp.get(k2) for k2 in ("cat", "ben", "chips", "how")},
            "similar_in_stock": [{"title": instock[h]["title"], "url": f"/products/{h}",
                                  "price": min(v["price"] for v in instock[h]["variants"])} for h in rel[:4]],
        })
    dst = ROOT / f"docs/data/product_desc_facts_{wave}.json"
    json.dump(out, open(dst, "w"), ensure_ascii=False, indent=1)
    print(len(out), "->", dst)


def build(S, wave):
    pick = {p["id"]: p for p in json.load(open(S / f"desc_{wave}_pick.json"))}
    admin = json.load(open(S / f"desc_{wave}_admin.json"))
    live = {p["handle"]: p for p in json.load(open(S / "sfall_live.json"))}
    coll = lambda h: {p["handle"] for p in json.load(open(S / f"sf2/{h}.json"))}
    G = {"For him": coll("perfume-for-men"), "For her": coll("perfume-for-women"), "Unisex": coll("unisex-perfume")}
    F = {f: coll(f"scent-{f}") for f in ("amber", "floral", "fresh", "oud", "woody")}
    instock = {h: p for h, p in live.items() if any(v["available"] for v in p["variants"]) and p["images"]}
    out = []
    for a in admin:
        p = pick[a["id"]]
        lp = live[a["handle"]]
        sw = json.loads((a.get("sw") or {}).get("value") or "{}")
        pdp = json.loads((a.get("pdp") or {}).get("value") or "{}")
        g = next((k for k, s in G.items() if a["handle"] in s), sw.get("w"))
        f = next((k for k, s in F.items() if a["handle"] in s), sw.get("f"))
        pool = [h for h in instock if h != a["handle"] and h not in {a["handle"]}
                and (f is None or h in F.get(f, set())) and (g is None or h in G.get(g, set()))]
        pool.sort(key=lambda h: (instock[h]["vendor"] != lp["vendor"], h))
        k = p["kw"] or {}
        out.append({
            "id": a["id"], "handle": a["handle"], "title": lp["title"], "vendor": lp["vendor"],
            "h1": (a.get("h1") or {}).get("value") or lp["title"],
            "primary_keyword": k.get("Primary keyword") or (a.get("h1") or {}).get("value") or lp["title"].split(" – ")[0],
            "volume": k.get("Primary vol.") or 0,
            "secondary_keyword": k.get("Secondary keyword") or "", "secondary_volume": k.get("Secondary vol.") or 0,
            "variants": [[v["title"], v["price"], v["available"]] for v in lp["variants"]],
            "current_description_html": a["descriptionHtml"],
            "current_text": " ".join(re.sub(r"<[^>]+>", " ", html.unescape(a["descriptionHtml"] or "")).split()),
            "facets": {"f": f, "w": g, "n": sw.get("n"), "t": sw.get("t")},
            "faq_answers": sw.get("a") or [], "pdp_chips": pdp.get("chips") or [],
            "similar_in_stock": [{"title": instock[h]["title"], "url": f"/products/{h}",
                                  "price": min(v["price"] for v in instock[h]["variants"])} for h in pool[:4]],
        })
    dst = ROOT / f"docs/data/product_desc_facts_{wave}.json"
    json.dump(out, open(dst, "w"), ensure_ascii=False, indent=1)
    print(len(out), "->", dst)


if __name__ == "__main__":
    S = pathlib.Path(sys.argv[2])
    skin = "--skin" in sys.argv
    args = [a for a in sys.argv if a != "--skin"]
    {"fetch": lambda: fetch(S), "select": lambda: select(S, args[3], int(args[4]) if len(args) > 4 else 50, skin),
     "build": lambda: (build_skin if skin else build)(S, args[3])}[args[1]]()

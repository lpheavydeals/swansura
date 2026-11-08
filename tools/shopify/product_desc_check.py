"""Check drafted product descriptions (8 Nov 2026) before they go to the store.

Usage: python3 tools/shopify/product_desc_check.py <drafts.json> <facts.json> <storefront_products_dir>
drafts: list of {id, handle, html, ...}; facts: docs/data/product_desc_facts_2026-11-08.json;
storefront dir: sfall_*.json dumps of /products.json (for in-stock link checks).
Fails a draft on: words outside 140-240, tags other than p/h3/ul/li/a, banned words, prices, em dashes,
exclamation marks, links that are not in-stock live products, primary keyword missing from the first sentence,
stored top/heart/base notes missing from the text.
"""
import glob, html, json, re, sys, unicodedata

drafts = json.load(open(sys.argv[1]))
facts = {f["handle"]: f for f in json.load(open(sys.argv[2]))}
def _load(f):
    d = json.load(open(f))
    return d["products"] if isinstance(d, dict) else d  # sfall_N.json = {"products": [...]}, sfall_live.json = [...]


SF = {p["handle"]: p for f in sorted(glob.glob(sys.argv[3] + "/sfall_*.json")) for p in _load(f)}  # later files win; sfall_live sorts last
BANNED = r"captivat|mesmeri|intoxicat|allur|unleash|elevat|indulg|exquisite|symphony|journey|embark|best.?sell|iconic|cult\b|award|no\.? ?1\b|limited edition|new formula|dupe|smells like|alternative to|hypoallergenic|sensitive skin|aphrodisiac|pheromone|mood|lasts all day|\bhours\b|free delivery|in stock|official (?:uk )?partner|launched|perfumer|\bnose\b"
ALLOWED = {"p", "h3", "ul", "li", "a"}
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", html.unescape(s).replace("’", "'")).encode("ascii", "ignore").decode().lower()).strip()
bad = 0
for d in drafts:
    f = facts[d["handle"]]; h = d["html"]; errs = []
    text = html.unescape(re.sub(r"<[^>]+>", " ", h)); words = len(text.split())
    if not 140 <= words <= 240: errs.append(f"{words} words")
    tags = set(t.lower() for t in re.findall(r"</?([a-zA-Z0-9]+)", h))
    if tags - ALLOWED: errs.append(f"tags {sorted(tags - ALLOWED)}")
    if re.search(r"\b(style|class)=", h): errs.append("style/class")
    m = re.findall(BANNED, text, re.I)
    # keep 'iconic' etc. only when the current text already uses it
    m = [x for x in m if x.lower() not in f["current_text"].lower()]
    if m: errs.append(f"banned {sorted(set(x.lower() for x in m))}")
    if "£" in text or re.search(r"\d+\.\d\d", text): errs.append("price")
    if "—" in text or "–" in re.sub(r"<a [^>]*>.*?</a>", "", h): errs.append("dash")
    if "!" in text.replace("Joop!", "Joop"): errs.append("exclamation")
    for url in re.findall(r'href="([^"]+)"', h):
        hd = url.rsplit("/", 1)[-1]
        p = SF.get(hd)
        if not url.startswith("/products/") or not p or not any(v["available"] for v in p["variants"]):
            errs.append(f"link {url}")
        if hd == d["handle"]: errs.append("self link")
    first = norm(re.split(r"(?<!\bNo\.)(?<!\bSt\.)(?<=[.?])\s", text.strip(), maxsplit=1)[0])  # 'No. 1' / 'St. Dupont' are not sentence ends
    kw = norm(f["primary_keyword"]).split()
    if not all(w in first.split() for w in kw): errs.append(f"keyword '{f['primary_keyword']}' not in first sentence")
    n = f["facets"].get("n")
    if isinstance(n, dict):
        for k, v in n.items():
            for note in [x.strip() for x in re.split(r",|\band\b", v) if x.strip()]:
                if norm(note) not in norm(text): errs.append(f"note missing: {note}")
    if errs:
        bad += 1
        print(f"FAIL {d['handle'][:60]}: " + "; ".join(errs))
print(f"{len(drafts)} drafts, {bad} failing")

"""Build theme/templates/index.json (homepage) from the prototype's rendered homepage.

Reads docs/data/prototype_home/*.html (captured with tools/proto/dump_sections.js from the prototype at
1366 px) and fills the sw-p-* sections with the same text, links, products and order. Prototype routes
become live URLs (tools/shopify/proto_menus.link), product ids become handles (prototype/products.json),
tile photos are matched to products by their alt text.

Run: python3 tools/theme/build_home_proto.py
"""
import html as H
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/shopify"))
from proto_menus import link  # noqa: E402

SRC = ROOT / "docs/data/prototype_home"
P = json.load(open(ROOT / "prototype/products.json"))
BY_ID = {str(p["id"]): p for p in P}
BY_ALT = {}
for p in P:
    for a in (p.get("alts") or []):
        BY_ALT.setdefault(H.unescape(a), p)


def part(prefix):
    f = sorted(SRC.glob(prefix + "*.html"))[0]
    return f.read_text()


def u(route):
    """Prototype href (#route) -> live URL."""
    return link("", route)["url"]


def coll(route):
    """Collection handle for a prototype route, or None (search / page links)."""
    m = re.match(r"^/collections/([^/?]+)$", u(route))
    return m.group(1) if m else None


def handle_of(pid):
    return BY_ID[pid]["h"]


def by_alt(alt):
    p = BY_ALT.get(H.unescape(alt))
    return p["h"] if p else None


def text(s):
    return H.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def tiles(html, item_re):
    out = []
    for m in re.finditer(item_re, html, re.S):
        out.append(m)
    return out


def sec_head(html):
    h = text(re.search(r"<h2[^>]*>(.*?)</h2>", html, re.S).group(1))
    m = re.search(r'<a class="link" href="#([^"]+)">(.*?)</a>', html)
    return h, (text(m.group(2)) if m else ""), (u(m.group(1)) if m else "")


sections, order = {}, []


def add(key, sec):
    sections[key] = sec
    order.append(key)


def tile_section(key, prefix, layout, item_re, fields):
    html = part(prefix)
    h, ll, lu = sec_head(html)
    blocks, bo = {}, []
    for i, m in enumerate(re.finditer(item_re, html, re.S)):
        d = m.groupdict()
        route = d["href"]
        st = {"title": text(d.get("title", "")), "line": text(d.get("line") or "")}
        c = coll(route)
        if c:
            st["collection"] = c
        if not c or u(route) != f"/collections/{c}":
            st["url"] = u(route)
        if d.get("alt"):
            hp = by_alt(d["alt"])
            if hp:
                st["product"] = hp
        if d.get("go"):
            st["go"] = text(d["go"]).rstrip(" →")
        if d.get("p"):
            st["partner"] = d["p"] == "p"
        st = {k: v for k, v in st.items() if v not in ("", None)}
        blocks[f"t{i}"] = {"type": "tile", "settings": st}
        bo.append(f"t{i}")
    settings = {"layout": layout, "heading": h, "link_label": ll, "link_url": lu}
    kc = re.search(r'<div class="kwchips"><span class="eyebrow">(.*?)</span><div>(.*?)</div></div>', html, re.S)
    if kc:
        settings["chips_label"] = text(kc.group(1))
        settings["chips"] = "\n".join(f"{text(t)}|{u(r)}" for r, t in re.findall(r'<a href="#([^"]+)">(.*?)</a>', kc.group(2)))
    if layout == "brands":
        more = re.findall(r'<div class="brandmore">(.*?)</div>', html, re.S)[0]
        settings["more_links"] = "\n".join(f"{text(t)}|{u(r)}" for r, t in re.findall(r'<a href="#([^"]+)"[^>]*>(.*?)</a>', more))
    add(key, {"type": "sw-p-tiles", "settings": {k: v for k, v in settings.items() if v != ""}, "blocks": blocks, "block_order": bo})


# 00 hero
html = part("00_")
skin = re.findall(r'<a class="slide" href="#p-(\d+)"[^>]*><div class="pic[^>]*></div><span class="tag">(.*?) <i>', re.search(r'class="arch".*?</div></div>', html, re.S).group(0))
scent = re.findall(r'<a class="slide" href="#p-(\d+)"[^>]*><div class="pic[^>]*></div><small>.*?</small><span>(.*?)</span>', re.search(r'class="float".*?</div></div>', html, re.S).group(0))
blocks = {f"pair{i}": {"type": "pair", "settings": {"skin": handle_of(a), "skin_label": text(al), "scent": handle_of(b), "scent_label": text(bl)}}
          for i, ((a, al), (b, bl)) in enumerate(zip(skin, scent))}
ctas = re.findall(r'<a class="btn [^"]*" href="#([^"]+)">(.*?)(?:<svg|</a>)', html)
add("hero", {"type": "sw-p-hero", "settings": {
    "eyebrow": text(re.search(r"<h1[^>]*>(.*?)</h1>", html).group(1)),
    "title": re.search(r'<p class="htitle[^>]*>(.*?)</p>', html).group(1),
    "lede": text(re.search(r'<p class="lede[^>]*>(.*?)</p>', html).group(1)),
    "btn1": text(ctas[0][1]), "btn1_url": u(ctas[0][0]), "btn2": text(ctas[1][1]), "btn2_url": u(ctas[1][0]),
    "brands_count": int(re.findall(r"<b>(\d+)</b><span>Brands", html)[0]), "delivery_min": 40},
    "blocks": blocks, "block_order": list(blocks)})

# 01 categories
tile_section("categories", "01_", "catrow",
             r'<a class="cat" href="#(?P<href>[^"]+)"><span class="ci"[^>]*><div class="pic[^"]*" role="img" aria-label="(?P<alt>[^"]*)"[^>]*></div></span><span>(?P<title>.*?)</span></a>', None)

# 02 studios
html = part("02_")
sblocks = {}
for i, m in enumerate(re.finditer(r'<div class="studio (\w+)"><span class="mark">(.*?)</span><h2>(.*?)</h2><p>(.*?)</p><div class="links">(.*?)</div></div>', html, re.S)):
    kind, mark, h2, p, links = m.groups()
    p = re.sub(r"^\d+ products", "[skin] products", text(p)) if kind == "skin" else re.sub(r"^\d+ fragrances", "[fragrance] fragrances", text(p))
    sblocks[kind] = {"type": "studio", "settings": {"kind": kind, "mark": text(mark), "heading": text(h2), "text": p,
                                                     "links": "\n".join(f"{text(t)}|{u(r)}" for r, t in re.findall(r'<a href="#([^"]+)">(.*?)</a>', links))}}
add("studios", {"type": "sw-p-studios", "settings": {"fragrance_collection": "fragrance"}, "blocks": sblocks, "block_order": list(sblocks)})

# 03 price bands
tile_section("price", "03_", "bands",
             r'<a class="band" href="#(?P<href>[^"]+)"><div class="pic[^"]*" role="img" aria-label="(?P<alt>[^"]*)"[^>]*></div><div><span class="n">(?P<title>.*?)</span><small>(?P<line>.*?)</small>', None)

# 04 bestsellers
html = part("04_")
h, ll, lu = sec_head(html)
tabs = re.findall(r'data-tab="(\w+)">(.*?)</button>', html)
def ids(tpl):
    return [handle_of(x) for x in dict.fromkeys(re.findall(r'<article class="card">.*?href="#p-(\d+)"', tpl, re.S))]
skin_t = re.search(r'<template id="best-skin">(.*?)</template>', html, re.S).group(1)
scent_t = re.search(r'<template id="best-scent">(.*?)</template>', html, re.S).group(1)
add("bestsellers", {"type": "sw-p-best", "settings": {"heading": h, "link_label": ll, "link_url": lu,
    "tab1": text(tabs[0][1]), "products1": ids(skin_t), "tab2": text(tabs[1][1]), "products2": ids(scent_t)}})

# 05 steps
tile_section("steps", "05_", "steps",
             r'<a class="step" href="#(?P<href>[^"]+)"[^>]*><span class="eyebrow">.*?</span><b>(?P<title>.*?)</b><small>(?P<line>.*?)</small><span class="si"><div class="pic[^"]*" role="img" aria-label="(?P<alt>[^"]*)"[^>]*></div></span><span class="go">(?P<go>.*?)</span></a>', None)

# 06 routines
html = part("06_")
rblocks = {}
for i, m in enumerate(re.finditer(r'<article class="ritual">.*?<div class="eyebrow">(.*?)</div><h3>(.*?)</h3><p[^>]*>(.*?)</p><ol>(.*?)</ol>', html, re.S)):
    grp, name, intro, ol = m.groups()
    st = {"group": text(grp), "name": text(name), "intro": text(intro)}
    for k, (step, pid) in enumerate(re.findall(r'<b[^>]*>(.*?)</b> · <a href="#p-(\d+)">', ol), 1):
        st[f"s{k}"] = text(step)
        st[f"p{k}"] = handle_of(pid)
    rblocks[f"r{i}"] = {"type": "ritual", "settings": st}
va = re.search(r'<div class="viewall"><a class="btn" href="#([^"]+)">(.*?)</a>', html)
add("routines", {"type": "sw-p-rituals", "settings": {"heading": sec_head(html)[0], "all_label": text(va.group(2)), "all_url": u(va.group(1)),
                                                      "discount_live": False, "save_pct": 5}, "blocks": rblocks, "block_order": list(rblocks)})

# 07 ranges
tile_section("ranges", "07_", "ingcards",
             r'<a class="ingcard" href="#(?P<href>[^"]+)"><b>(?P<title>.*?)</b><small>(?P<line>.*?)</small><span class="ii"[^>]*><div class="pic[^"]*" role="img" aria-label="(?P<alt>[^"]*)"', None)
# 08 concerns
tile_section("concerns", "08_", "concerns",
             r'<a class="concern" href="#(?P<href>[^"]+)"><div><b>(?P<title>.*?)</b><small>(?P<line>.*?)</small>.*?<div class="pic[^"]*" role="img" aria-label="(?P<alt>[^"]*)"', None)
# 09 scent families
tile_section("families", "09_", "families",
             r'<a class="family" href="#(?P<href>[^"]+)"><span class="n">(?P<title>.*?)</span><p>(?P<line>.*?)</p>', None)
# 10 brands
tile_section("brands", "10_", "brands",
             r'<a class="bcard" href="#(?P<href>[^"]+)"[^>]*><div><span class="bn">(?P<title>.*?)</span><small class="(?P<p>p?)">(?P<line>.*?)</small>.*?<div class="pic[^"]*" role="img" aria-label="(?P<alt>[^"]*)"', None)

# 11 advent cards
html = part("11_")
h, ll, lu = sec_head(html)
ablocks = {}
for m in re.finditer(r'<article class="advent (\w+)"><div class="advent-top"><div class="eyebrow">(.*?)</div><h2>(.*?)</h2><p>(.*?)</p>.*?<a class="btn light" href="#([^"]+)">.*?<div class="advent-strip">(.*?)</div></article>', html, re.S):
    kind, eb, h2, p, inside, strip = m.groups()
    ablocks[kind] = {"type": "advent", "settings": {"kind": kind, "eyebrow": text(eb), "heading": text(h2), "text": text(p), "inside_url": "/pages/advent#" + kind,
                                                    "strip": [x for x in (by_alt(a) for a in re.findall(r'aria-label="([^"]*)"', strip)) if x]}}
add("advent", {"type": "sw-p-advents", "settings": {"heading": h, "link_label": ll, "link_url": lu}, "blocks": ablocks, "block_order": list(ablocks)})

# 12 / 13 brand stories
def imgs_html(html):
    i = html.find('<div class="imgs">')
    j = html.find('<div class="copy">', i)
    return html[i:j if j > i else len(html)]



for key, prefix in (("story_deyga", "12_"), ("story_vilvah", "13_")):
    html = part(prefix)
    btns = re.findall(r'<a class="btn[^"]*" href="#([^"]+)">(.*?)</a>', html)
    n = re.search(r"Shop all (\d+)", btns[0][1])
    route0 = btns[0][0]
    add(key, {"type": "sw-p-story", "settings": {
        "reverse": "story rev" in html,
        "products": [x for x in (by_alt(a) for a in re.findall(r'aria-label="([^"]*)"', imgs_html(html))) if x],
        "eyebrow": text(re.search(r'<div class="eyebrow">(.*?)</div>', html).group(1)),
        "heading": text(re.search(r"<h2>(.*?)</h2>", html).group(1)),
        "text": text(re.search(r'<p class="lede">(.*?)</p>', html, re.S).group(1)),
        "btn1": text(btns[0][1]).replace(n.group(1), "[count]") if n else text(btns[0][1]), "btn1_url": u(route0),
        "count_collection": coll(route0) or "",
        "btn2": text(btns[1][1]), "btn2_url": u(btns[1][0])}})

# 14 Christmas band
html = part("14_")
add("xmas", {"type": "sw-p-xmas", "settings": {
    "heading": text(re.search(r"<h2>(.*?)</h2>", html).group(1)),
    "text": text(re.search(r'<div class="xmas-copy">.*?<p>(.*?)</p>', html, re.S).group(1)),
    "links": "\n".join(f"{text(t)}|{u(r)}" for r, t in re.findall(r'<a href="#([^"]+)">(.*?)</a>', re.search(r'<div class="xmas-links">(.*?)</div>', html, re.S).group(1))),
    "btn": text(re.search(r'<a class="btn gold" href="#[^"]+">(.*?)</a>', html).group(1)),
    "btn_url": u(re.search(r'<a class="btn gold" href="#([^"]+)">', html).group(1)),
    "products": [handle_of(x) for x in re.findall(r'<a class="xp xp\d" href="#p-(\d+)"', html)]}})

# 15 Journal
html = part("15_")
h, ll, lu = sec_head(html)
add("journal", {"type": "sw-p-journal", "settings": {"heading": h, "link_label": ll, "blog": "journal", "limit": 3}})

# 16 newsletter
html = part("16_")
add("newsletter", {"type": "sw-p-news", "settings": {
    "eyebrow": text(re.search(r'<div class="eyebrow"[^>]*>(.*?)</div>', html).group(1)),
    "heading": text(re.search(r"<h2>(.*?)</h2>", html).group(1)),
    "text": text(re.search(r"</h2>\s*<p>(.*?)</p>", html, re.S).group(1))}})

# 17 popular searches
html = part("17_")
gblocks = {}
for i, m in enumerate(re.finditer(r"<details[^>]*><summary><h3>(.*?)</h3></summary><div>(.*?)</div></details>", html, re.S)):
    gblocks[f"g{i}"] = {"type": "group", "settings": {"title": text(m.group(1)),
                                                     "links": "\n".join(f"{text(t)}|{u(r)}" for r, t in re.findall(r'<a href="#([^"]+)">(.*?)</a>', m.group(2)))}}
add("popular", {"type": "sw-p-searches", "settings": {"heading": sec_head(html)[0]}, "blocks": gblocks, "block_order": list(gblocks)})

# 18 about this page
html = part("18_")
body = re.search(r'<div class="txt">(.*?)</div></div></section>', html, re.S).group(1)
body = re.sub(r'href="#([^"]+)"', lambda m: f'href="{u(m.group(1))}"', body)
add("seo", {"type": "sw-p-seocopy", "settings": {"eyebrow": "About this page", "heading": text(re.search(r"<h2[^>]*>(.*?)</h2>", html).group(1)), "text": body}})

# 'Picking up where you left off' sits after the brand stories, before the Christmas banner (shown once there is history)
sections["seen"] = {"type": "sw-p-seen", "settings": {}}
order.insert(order.index("xmas"), "seen")
json.dump({"sections": sections, "order": order}, open(ROOT / "theme/templates/index.json", "w"), ensure_ascii=False, indent=1)

# header group: announcement bar + Swansura header (prototype markup); Dawn's header is no longer used
hg_path = ROOT / "theme/sections/header-group.json"
raw = hg_path.read_text()
hg = json.loads(raw[raw.index("{"):])
ann = hg["sections"]["sw-announcement"]
ann["settings"] = {}
hg["sections"] = {"sw-announcement": ann, "sw-header": {"type": "sw-header", "settings": {
    "menu": "sw-main", "drawer_menu": "sw-drawer",
    "feat_skin_item": "Skincare", "feat_skin": handle_of("15415435067779"),
    "feat_scent_item": "Fragrance", "feat_scent": handle_of("16274498945411"),
    "brands_url": "/collections", "wishlist_url": "/pages/wishlist",
    "whatsapp": "+44 7438 847453", "email": "info@swansura.com",
    "skin_url": "/collections/skincare", "scent_url": "/collections/fragrance",
    "extras_collection": "price-0-15", "delivery_min": 40, "bonus_min": 70, "bonus_off": 5}}}
hg["order"] = ["sw-announcement", "sw-header"]
hg_path.write_text(json.dumps(hg, ensure_ascii=False, indent=2))

# settings: the prototype bag replaces Dawn's cart drawer
sd_path = ROOT / "theme/config/settings_data.json"
sd = sd_path.read_text()
sd = sd.replace('"cart_type": "drawer"', '"cart_type": "page"', 1)
sd_path.write_text(sd)
missing = [(k, b) for k, s in sections.items() for b, v in s.get("blocks", {}).items() if s["type"] == "sw-p-tiles" and "product" not in v["settings"] and s["settings"]["layout"] not in ("families",)]
print("index.json:", len(order), "sections;", "tiles without a photo:", missing)

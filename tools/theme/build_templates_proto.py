"""JSON templates on the prototype markup (design port, 26 Oct 2026). Overwrites the Day-2/3 versions
written by build_templates.py for the page types already ported.
Order on listings (prototype): listing → 'About this page' → Studio Letter → FAQs → footer."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / "theme/templates"
NEWS = {"type": "sw-p-news", "settings": {}}
FAQ = {"type": "sw-auto-faq", "settings": {"eyebrow": "Good to know", "heading": "Questions about Swansura"}}


def write(name, sections, order):
    (T / name).write_text(json.dumps({"sections": sections, "order": order}, ensure_ascii=False, indent=1))
    print(name, order)


listing = {"main": {"type": "sw-p-collection", "settings": {"explore_menu": "sw-footer-shop"}},
           "seo": {"type": "sw-p-seocopy", "settings": {"eyebrow": "About this page"}},
           "newsletter": NEWS, "faq": FAQ}
for name in ("collection.json", "collection.fragrance.json"):
    write(name, listing, ["main", "seo", "newsletter", "faq"])

# Product page (productPage()): main → Studio Letter → FAQs → footer; the bundle template uses the same layout
product = {"main": {"type": "sw-p-product", "settings": {}}, "newsletter": NEWS, "faq": FAQ}
for name in ("product.json", "product.bundle.json"):
    write(name, product, ["main", "newsletter", "faq"])

# ---------------------------------------------------------------------------------------------
# Pages, Journal, Routines, Brands A–Z, 404 (journalPage / articlePage / infoPage / ritualsPage / brandsAZ / notFound)
import glob
import html as H
import re

D = ROOT / "docs/data/prototype_pages"
HANDLE = {}
for line in open(ROOT / "docs/backups/products_before_day4_2026-10-26.jsonl"):
    r = json.loads(line)
    HANDLE[r["id"].rsplit("/", 1)[1]] = r["handle"]
OLD_PAGE = json.loads((T / "page.faq.json").read_text()) if (T / "page.faq.json").exists() else {}
MAP = "fragrance:fragrance\nskincare:skincare\nhaircare:haircare\nbody-care:bodycare\nlipcare:lip-balm\ngift-set:sets-combos\nbest-sellers:best-sellers\ncleanser:cleanser\nmoisturiser:moisturizers-gels\ntoner:toner\nserum:serum\nunder-eye-cream:skincare\nfor-her:fragrance\nfor-him:fragrance\nlipbalm:lip-balm\nlib-scrub:lip-scrub\nshampoo:shampoo\nconditioner:shampoo\nhair-oil:hair-oil\nhair-serum:hair-styling-products\ncomb:haircare-tools-kits\nbody-lotion:body-cream-exfoliants\nbody-wash:body-cream-exfoliants\nbody-scrub-mask:body-cream-exfoliants\nfoot-cream:body-cream-exfoliants\nbody-butter:body-cream-exfoliants\nbody-scrub:body-cream-exfoliants\nbath-bar:body-cream-exfoliants\njo-milano:jo-milano\ndiamond-collection:diamond-collection\nmake-up-products:makeup-product"
# claims that need a Shopify discount that does not exist yet (routine / pack saving)
NO_SAVING = re.compile(r"\bsav(e|es|ing)\b.*\b\d+%|\b\d+%.*\bsav", re.I)


def dump(route, prefix):
    return open(glob.glob(str(D / route / prefix) + "*")[0]).read()


def faq_blocks(route, keep=lambda q, a: True):
    h = dump(route, "faqslot")
    out, head = {}, re.search(r"<h2[^>]*>(.*?)</h2>", h)
    for i, (q, a) in enumerate(re.findall(r"<details><summary>(.*?)</summary>(.*?)</details>", h, re.S)):
        q, a = H.unescape(q), re.sub(r'href="#([^"]+)"', lambda m: f'href="{route_url(m.group(1))}"', a)
        if keep(q, a):
            out[f"q{i}"] = {"type": "faq", "settings": {"q": q, "a": a}}
    return out, (H.unescape(head.group(1)) if head else "")


def route_url(r):
    sys.path.insert(0, str(ROOT / "tools/shopify"))
    from proto_menus import link
    if r.startswith("p-") and r[2:] in HANDLE:
        return "/products/" + HANDLE[r[2:]]
    return link("x", "#" + r)["url"]


import sys  # noqa: E402

no_saving = lambda q, a: not NO_SAVING.search(q + " " + a)  # noqa: E731


def seocopy(route):
    h = dump(route, "01_seocopy")
    head = H.unescape(re.search(r"<h2[^>]*>(.*?)</h2>", h).group(1))
    txt = re.search(r'<div class="txt">(.*)</div></div></section>', h, re.S).group(1)
    txt = re.sub(r'href="#([^"]+)"', lambda m: f'href="{route_url(m.group(1))}"', txt)
    return {"type": "sw-p-seocopy", "settings": {"eyebrow": "About this page", "heading": head, "text": txt}}


FAQ_PAGE = lambda heading, blocks: {"type": "sw-auto-faq", "settings": {"eyebrow": "Good to know", "heading": heading},  # noqa: E731
                                    "blocks": blocks, "block_order": list(blocks)}

# Journal + article
write("blog.json", {"main": {"type": "sw-p-blog", "settings": {}}, "newsletter": NEWS}, ["main", "newsletter"])
write("article.json", {"main": {"type": "sw-p-article", "settings": {}}, "newsletter": NEWS, "faq": FAQ},
      ["main", "newsletter", "faq"])

# Info pages: default, contact (form), about, shipping/offers use the default
chips = "Gifts for her|/collections/gifts-for-her\nGifts for him|/collections/gifts-for-him\nGifts under £25|/collections/gifts-under-25\nGifts £25 to £50|/collections/gifts-25-to-50\nLuxury gifts over £50|/collections/gifts-over-50\nDiwali gifts|/collections/diwali-gifts"
page = {"main": {"type": "sw-p-page", "settings": {"map": MAP, "chips": chips}}, "newsletter": NEWS}
write("page.json", page, ["main", "newsletter"])
write("page.about.json", page, ["main", "newsletter"])
write("page.contact.json", {"main": {"type": "sw-p-page", "settings": {"form": True, "chips": chips, "heading": "Contact us",
    "lede": "<p>Questions about an order, a product or a fragrance recommendation? Message us on <a href=\"https://wa.me/447438847453\">WhatsApp: +44 7438 847453</a> (messages only), email <a href=\"mailto:info@swansura.com\">info@swansura.com</a>, or use the form below.</p>"}}, "newsletter": NEWS},
      ["main", "newsletter"])
old_faq = OLD_PAGE.get("sections", {}).get("faq", {})
fb = {k: {"type": "faq", "settings": v["settings"]} for k, v in old_faq.get("blocks", {}).items()}
write("page.faq.json", {"main": {"type": "sw-p-page", "settings": {"show_content": False, "chips": chips,
                                                                  "lede": "<p>Delivery, returns, payment and orders: the quick answers.</p>"}},
                        "newsletter": NEWS, "faq": FAQ_PAGE("Questions about Swansura", fb)}, ["main", "newsletter", "faq"])
write("page.wishlist.json", {"main": {"type": "sw-p-wishlist", "settings": {"browse_url": "/collections/all"}}, "newsletter": NEWS},
      ["main", "newsletter"])

# Offers: tiles from the prototype; routine / pack tiles need the bundle discount
oh = dump("offers", "00_")
tiles = {}
for i, (eb, t, p, btn, href) in enumerate(re.findall(r'<article class="offer"><div class="eyebrow">(.*?)</div><h3>(.*?)</h3><p>(.*?)</p><a class="btn" href="#([^"]+)">(.*?)</a>', oh)
                                          and [(a, b, c, e, d) for a, b, c, d, e in re.findall(r'<article class="offer"><div class="eyebrow">(.*?)</div><h3>(.*?)</h3><p>(.*?)</p><a class="btn" href="#([^"]+)">(.*?)</a>', oh)]):
    tiles[f"o{i}"] = {"type": "offer", "settings": {"eyebrow": H.unescape(eb), "title": H.unescape(t), "text": H.unescape(p), "btn": H.unescape(btn),
                                                    "url": route_url(href), "needs_discount": bool(re.search(r"\d+%", t))}}
write("page.offers.json", {"main": {"type": "sw-p-offers", "blocks": tiles, "block_order": list(tiles), "settings": {
    "lede": "<p>Ways to save at Swansura today: free UK delivery over £40, and free delivery plus £5 off over £70.</p>"}},
    "newsletter": NEWS}, ["main", "newsletter"])

# Routines page: one routines section per group, kits grid, gift chips, SEO copy, FAQs
rh = re.sub(r'style="background-size[^"]*"', "", dump("rituals", "00_"))
sections, order = {"head": {"type": "sw-p-page", "settings": {
    "eyebrow": "Routines & sets", "heading": "Skincare Routines That Work Together", "share": True, "show_content": False,
    "share_text": "16 step-by-step skincare, hair, body and scent routines at Swansura",
    "lede": "<p>16 step-by-step routines built from products across our brands.</p>"}}}, ["head"]
for gi, (count, label, body) in enumerate(re.findall(r'<section style="padding-block:48px 8px"><div class="sec-head"><div><div class="eyebrow">(.*?)</div><h2>(.*?)</h2></div></div><div class="rituals">(.*?)</div></section>', rh, re.S)):
    blocks = {}
    for ri, (grp, name, intro, ol) in enumerate(re.findall(r'<article class="ritual">.*?<div class="eyebrow">(.*?)</div><h3>(.*?)</h3><p[^>]*>(.*?)</p><ol>(.*?)</ol>', body, re.S)):
        st = {"group": H.unescape(grp), "name": H.unescape(name), "intro": H.unescape(intro)}
        for k, (step, pid) in enumerate(re.findall(r'<b[^>]*>(.*?)</b> · <a href="#p-(\d+)"', ol), 1):
            st[f"s{k}"], st[f"p{k}"] = H.unescape(step), HANDLE.get(pid, "")
        blocks[f"r{ri}"] = {"type": "ritual", "settings": st}
    key = f"g{gi}"
    sections[key] = {"type": "sw-p-rituals", "settings": {"layout": "page", "heading": H.unescape(label), "all_label": ""},
                     "blocks": blocks, "block_order": list(blocks)}
    order.append(key)
sections["kits"] = {"type": "sw-p-grid", "settings": {"heading": "Ready-made kits", "collection": "sets-combos", "limit": 8, "link_label": "All gifts & sets"}}
chip_handles = ["gifts-under-25", "gifts-25-to-50", "gifts-over-50", "gifts-for-her", "gifts-for-him", "diwali-gifts", "ramadan-eid-gifts", "stocking-fillers"]
cb = {f"c{i}": {"type": "chip", "settings": {"collection": h}} for i, h in enumerate(chip_handles)}
sections["gifts"] = {"type": "sw-p-chips", "settings": {"heading": "Gifts by price", "unit": "gifts"}, "blocks": cb, "block_order": list(cb)}
sections["seo"] = seocopy("rituals")
sections["newsletter"] = NEWS
fq, fh = faq_blocks("rituals", no_saving)
sections["faq"] = FAQ_PAGE(fh, fq)
order += ["kits", "gifts", "seo", "newsletter", "faq"]
write("page.rituals.json", sections, order)

# Brands A–Z (/collections)
fq, fh = faq_blocks("brands")
write("list-collections.json", {"main": {"type": "sw-p-brands", "settings": {}}, "seo": seocopy("brands"), "newsletter": NEWS,
                                "faq": FAQ_PAGE(fh, fq)}, ["main", "seo", "newsletter", "faq"])

write("404.json", {"main": {"type": "sw-p-404", "settings": {}}, "newsletter": NEWS}, ["main", "newsletter"])

# Advent page (adventPage()): header, calendar cards + perks + doors, newsletter, FAQs.
# Prices / 'worth' only once a calendar product exists; FAQ answers avoid unconfirmed prices and stock claims.
home_adv = next(v for v in json.loads((T / "index.json").read_text())["sections"].values() if v["type"] == "sw-p-advents")
old_adv = json.loads((T / "page.advent.json").read_text())["sections"].get("advent", {}).get("blocks", {})
blocks = {}
for k, b in home_adv["blocks"].items():
    st = dict(b["settings"])
    st["inside_url"] = f"#{st['kind']}"
    contents = (old_adv.get(k) or old_adv.get(st["kind"]) or {}).get("settings", {}).get("contents")
    if contents:
        st["contents"] = contents
    blocks[k] = {"type": "advent", "settings": st}
adv_faq = {f"q{i}": {"type": "faq", "settings": {"q": q, "a": f"<p>{a}</p>"}} for i, (q, a) in enumerate([
    ("What is the difference between the two calendars?", "The Skin Studio Advent has 12 natural skin, lip and body products from Deyga and Vilvah. The Scent Studio Advent has 12 designer and niche fragrance miniatures."),
    ("Are the products full size?", "The Skin Studio Advent is mostly full-size lip, soap and skincare favourites. The Scent Studio Advent is fragrance miniatures."),
    ("Is it a good gift?", "Yes. Each calendar arrives gift-ready, and it is a good way to try a brand or fragrance before buying the full size."),
    ("When can I buy one?", "The calendars are coming soon for Christmas 2026. Sign up to the Studio Letter to hear when they launch."),
])}
write("page.advent.json", {
    "head": {"type": "sw-p-page", "settings": {"eyebrow": "Christmas 2026", "heading": "Two calendars. Twelve days of rituals.", "show_content": False,
                                               "share": True, "share_text": "Two advent calendars at Swansura: 12 days of natural skincare or 12 fragrance miniatures",
                                               "lede": "<p>Choose the Skin Studio for natural skin and body care, or the Scent Studio for fragrance miniatures.</p>"}},
    "advent": {"type": "sw-p-advents", "settings": {"layout": "page", "more_collection": "stocking-fillers"}, "blocks": blocks, "block_order": list(blocks)},
    "newsletter": NEWS, "faq": FAQ_PAGE("Advent calendar questions", adv_faq)}, ["head", "advent", "newsletter", "faq"])

# Sitemap (sitemapPage()): link columns from the prototype, Journal, brands with products
sm = dump("sitemap", "00_")
cols = {}
for i, (head, body) in enumerate(re.findall(r'<section class="smcol"><h2>(.*?)</h2>(.*?)</section>', sm, re.S)):
    head = H.unescape(head)
    if head == "Journal":
        continue
    links = [f"{H.unescape(re.sub(r'<small>.*?</small>', '', t)).strip()}|{route_url(h)}" for h, t in re.findall(r'<a href="#([^"]+)">(.*?)</a>', body)]
    cols[f"c{i}"] = {"type": "col", "settings": {"heading": head, "links": "\n".join(links), "counts": "<small>" in body}}
write("page.sitemap.json", {"main": {"type": "sw-p-sitemap", "settings": {"blog": "journal"}, "blocks": cols, "block_order": list(cols)},
                            "newsletter": NEWS}, ["main", "newsletter"])

# Bag page (the drawer inline) and search results
write("cart.json", {"main": {"type": "sw-p-cart", "settings": {}}}, ["main"])
write("search.json", {"main": {"type": "sw-p-search", "settings": {}}, "newsletter": NEWS}, ["main", "newsletter"])

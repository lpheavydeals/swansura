"""Store menus that mirror the prototype header mega menu and footer (rendered nav in
docs/data/prototype_nav.json, extracted with tools/proto/extract_nav.js).

New handles (sw-*) so the live theme's main-menu / footer menus stay as they are; the draft theme
points at these. Prototype 'By type' links (all '#c-skincare' in the prototype, a filter there) go to
the store's type collections. Output: docs/seo/proto_menus.json (MenuCreate arguments).
"""
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from proto_collections_create import ROOT, url  # noqa: E402

NAV = json.load(open(ROOT / "docs/data/prototype_nav.json"))
TYPES = {  # (category, prototype type label) -> store collection
    ("Skincare", "Serums"): "serum", ("Skincare", "Moisturisers"): "moisturizers-gels",
    ("Skincare", "Masks"): "face-mask-pack", ("Skincare", "Toners"): "toner", ("Skincare", "Cleansers"): "cleanser",
    ("Skincare", "Kits & routines"): "skincare-tools-kits", ("Skincare", "Sun care"): "sunscreen",
    ("Skincare", "Lip care"): "lip-balm",
    ("Haircare", "Hair oil"): "hair-oil", ("Haircare", "Kits & routines"): "haircare-tools-kits",
    ("Haircare", "Shampoo"): "shampoo", ("Haircare", "Moisturisers"): "hair-styling-products",
    ("Haircare", "Serums"): "hair-serum-for-frizzy-hair", ("Haircare", "Masks"): "hair-mask",
    ("Haircare", "Conditioner"): "conditioner",
}
FOR = {"For her": "perfume-for-women", "For him": "perfume-for-men", "Unisex": "unisex-perfume",
       "Minis & sets": "perfume-gift-sets"}
EXTRA = {"advent": "/pages/advent", "advent-skin": "/pages/advent#skin", "advent-scent": "/pages/advent#scent",
         "c-all": "/collections/all", "page-delivery": "/pages/shipping", "page-faq": "/pages/faq",
         "page-about": "/pages/about", "page-contact": "/pages/contact", "page-privacy": "/policies/privacy-policy",
         "page-terms": "/policies/terms-of-service", "page-refunds": "/policies/refund-policy",
         "page-shipping": "/pages/shipping", "sitemap": "/pages/sitemap", "offers": "/pages/offers"}


NEW_BRANDS = {"b-highborn-london": "highborn-london", "b-swansura-selection": "swansura-selection", "b-anatome": "anatome"}


def link(title, href, top=None, col=None):
    r = href.lstrip("#")
    if r in NEW_BRANDS:  # brand pages created after the route map
        u = "/collections/" + NEW_BRANDS[r]
    elif col == "By type" and (top, title) in TYPES:
        u = "/collections/" + TYPES[(top, title)]
    elif top == "Fragrance" and col == "For" and title in FOR:
        u = "/collections/" + FOR[title]
    else:
        u = EXTRA.get(r) or url(r)
    return {"title": title.replace(" →", ""), "type": "HTTP", "url": u}


main = []
for it in NAV["items"]:
    top = link(it["t"], it["h"])
    cols = []
    for c in it["cols"]:
        # Dawn's mega menu needs a heading per column; the unlabeled third brands column continues 'Scent Studio'
        head = c["h"] or "More houses"
        cols.append({"title": head, "type": "HTTP", "url": top["url"],
                     "items": [link(t, h, it["t"], c["h"]) for t, h in c["links"]]})
    if cols:
        top["items"] = cols
    main.append(top)

menus = [{"handle": "sw-main", "title": "Swansura main menu", "items": main}]
for f in NAV["foot"]:
    h = "sw-footer-" + f["h"].lower().replace(" ", "-")
    menus.append({"handle": h, "title": "Swansura footer – " + f["h"], "items": [link(t, x) for t, x in f["links"]]})
menus.append({"handle": "sw-legal", "title": "Swansura legal bar",
              "items": [link(t, x) for t, x in NAV["legal"] if t not in ("Sitemap", "Cookie settings")]})
json.dump(menus, open(ROOT / "docs/seo/proto_menus.json", "w"), ensure_ascii=False, indent=1)
for m in menus:
    n = sum(1 + sum(1 + len(c.get("items", [])) for c in i.get("items", [])) for i in m["items"])
    print(m["handle"], n, "links")

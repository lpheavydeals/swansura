"""Fix products filed under the wrong brand (store vendor and Day-4 SEO copied the prototype's mix-up):
5 Azzaro products under Bentley, 2 Boucheron under Antonio Banderas.

Writes docs/seo/brand_mixup_fix_2026-10-26.json: product updates (vendor, SEO title/description, custom.h1),
membership moves, the two new brand collections and corrected FAQs for Bentley / Antonio Banderas.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
FIX = [  # id, brand, H1, SEO title, price, style
    ("16367216984451", "Azzaro", "Azzaro The Most Wanted Parfum", "Azzaro The Most Wanted Parfum 100ml | Swansura UK",
     "Buy Azzaro The Most Wanted Parfum 100ml for £60.99 at Swansura UK. An amber men's parfum. 100% authentic, fast UK delivery, free over £40."),
    ("16367210561923", "Azzaro", "Azzaro The Most Wanted Eau de Toilette Intense Gift Set", "Azzaro The Most Wanted EDT Intense Gift Set | Swansura",
     "Buy Azzaro The Most Wanted Eau de Toilette Intense Gift Set 100ml for £68.99 at Swansura UK. A woody men's eau de toilette. Free UK delivery over £40."),
    ("16367198437763", "Azzaro", "Azzaro Pour Homme Deodorant Spray", "Azzaro Pour Homme Deodorant Spray 150ml | Swansura UK",
     "Buy Azzaro Pour Homme Deodorant Spray 150ml for £22.99 at Swansura UK. An aromatic men's fragrance. 100% authentic, fast UK delivery, free over £40."),
    ("16367171961219", "Azzaro", "Azzaro Chrome Legend Eau de Toilette 75ml", "Azzaro Chrome Legend 75ml EDT | Swansura UK",
     "Buy Azzaro Chrome Legend Eau de Toilette 75ml for £27.99 at Swansura UK. A fresh men's eau de toilette. 100% authentic, fast UK delivery, free over £40."),
    ("16367165276547", "Azzaro", "Azzaro Chrome Legend Eau de Toilette 125ml", "Azzaro Chrome Legend 125ml EDT | Swansura UK",
     "Buy Azzaro Chrome Legend Eau de Toilette 125ml for £33.99 at Swansura UK. A fresh men's eau de toilette. 100% authentic, fast UK delivery, free over £40."),
    ("16364242928003", "Boucheron", "Boucheron Rose d’Isparta Eau de Parfum 125ml", "Boucheron Rose d’Isparta EDP 125ml | Swansura UK",
     "Shop Boucheron Rose d’Isparta Eau de Parfum 125ml at Swansura UK. A unisex rose amber fragrance. 100% authentic, free UK delivery over £40."),
    ("16364237652355", "Boucheron", "Boucheron Patchouli d’Angkor Eau de Parfum 125ml", "Boucheron Patchouli d’Angkor EDP 125ml | Swansura UK",
     "Shop Boucheron Patchouli d’Angkor Eau de Parfum 125ml at Swansura UK. A unisex woody amber fragrance. 100% authentic, free UK delivery over £40."),
]
DELIV = "UK delivery is free on orders over £40, and orders over £70 also get £5 off. The cost for smaller orders is shown at checkout."


def brand_faq(b, n, lo, hi, split, picks, sets):
    return [[f"Is {b} at Swansura genuine?", f"Yes. Every {b} product at Swansura is 100% authentic and ships from the UK."],
            [f"Which {b} products do you stock?",
             f"{n} products, " + (f"both £{lo}" if lo == hi and n == 2 else f"from £{lo} to £{hi}") + f": {split}."],
            [f"Which {b} product should I start with?", f"Good places to start are {picks}."],
            [f"Does {b} come in miniatures or gift sets?", sets],
            [f"How fast is {b} delivery?", f"All {b} orders ship from Swansura in the UK. {DELIV}"]]


out = {
    "products": [{"id": f"gid://shopify/Product/{i}", "vendor": b, "seo": {"title": t, "description": d},
                  "metafields": [{"namespace": "custom", "key": "h1", "type": "single_line_text_field", "value": h}]}
                 for i, b, h, t, d in FIX],
    "remove": {"gid://shopify/Collection/713376792963": [f"gid://shopify/Product/{i}" for i, b, *_ in FIX if b == "Azzaro"],
               "gid://shopify/Collection/713303032195": [f"gid://shopify/Product/{i}" for i, b, *_ in FIX if b == "Boucheron"]},
    "faq": {
        "gid://shopify/Collection/713376792963": brand_faq(
            "Bentley", 6, "30.99", "40.99", "for him (6)",
            "Bentley Momentum Unlimited Eau de Toilette 100ml, Bentley Infinite Eau de Toilette 100ml and Bentley Become Eau de Parfum 100ml",
            "Not at the moment. Every Bentley product we stock is listed above."),
        "gid://shopify/Collection/713303032195": brand_faq(
            "Antonio Banderas", 4, "16.99", "20.99", "for her (2), for him (2)",
            "Power of Seduction Eau de Toilette 50ml, Her Secret Temptation Eau de Toilette 80ml and Diavolo Eau de Toilette",
            "Not at the moment. Every Antonio Banderas product we stock is listed above."),
    },
    "create": [],
}
for b, ids, lo, hi, split, picks, sets, h1, title, desc, intro in [
    ("Azzaro", [i for i, x, *_ in FIX if x == "Azzaro"], "22.99", "68.99", "for him (5)",
     "Azzaro The Most Wanted Parfum 100ml, Azzaro Chrome Legend Eau de Toilette 75ml and Azzaro Pour Homme Deodorant Spray 150ml",
     "Yes, 1: Azzaro The Most Wanted Eau de Toilette Intense Gift Set 100ml + 2x10ml.",
     "Azzaro Perfume for Men", "Azzaro Perfume for Men | The Most Wanted & Chrome | Swansura",
     "Shop Azzaro perfume for men in the UK: The Most Wanted Parfum, Chrome Legend and Pour Homme. 100% authentic, free UK delivery over £40.",
     "Azzaro fragrances for men, from The Most Wanted Parfum to Chrome Legend, 100% authentic and shipped from the UK."),
    ("Boucheron", [i for i, x, *_ in FIX if x == "Boucheron"], "63.99", "63.99", "unisex (2)",
     "Boucheron Rose d’Isparta Eau de Parfum 125ml and Boucheron Patchouli d’Angkor Eau de Parfum 125ml",
     "Not at the moment. Every Boucheron product we stock is listed above.",
     "Boucheron Perfume", "Boucheron Perfume | La Collection EDP 125ml | Swansura UK",
     "Shop Boucheron perfume in the UK: Rose d’Isparta and Patchouli d’Angkor eau de parfum, 125ml. 100% authentic, free UK delivery over £40.",
     "Boucheron's unisex eaux de parfum, Rose d’Isparta and Patchouli d’Angkor, 100% authentic and shipped from the UK."),
]:
    out["create"].append({
        "title": b, "handle": b.lower(), "templateSuffix": "brand", "sortOrder": "BEST_SELLING",
        "descriptionHtml": f"<p>{intro}</p>", "seo": {"title": title, "description": desc},
        "metafields": [
            {"namespace": "custom", "key": "h1", "type": "single_line_text_field", "value": h1},
            {"namespace": "custom", "key": "eyebrow", "type": "single_line_text_field", "value": "The brand"},
            {"namespace": "custom", "key": "faq", "type": "json",
             "value": json.dumps(brand_faq(b, len(ids), lo, hi, split, picks, sets), ensure_ascii=False)}],
        "products": [f"gid://shopify/Product/{i}" for i in ids]})
for p in out["products"]:
    assert len(p["seo"]["title"]) <= 60 and len(p["seo"]["description"]) <= 160, p
for c in out["create"]:
    assert len(c["seo"]["title"]) <= 60 and len(c["seo"]["description"]) <= 160, c["seo"]
json.dump(out, open(ROOT / "docs/seo/brand_mixup_fix_2026-10-26.json", "w"), ensure_ascii=False, indent=1)
print("ok", len(out["products"]), "products,", len(out["create"]), "new brand collections")

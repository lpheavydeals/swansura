"""Fix out-of-date counts and prices in the 'About this page' copy, FAQs and meta descriptions of the
collections listed in docs/seo/stale_copy_scan_2026-11-06.json (user, 7 Nov 2026: 'Fix the 40 pages with
outdated counts and prices'). armaf / oud-perfume / arabian-perfume were already rewritten on 6 Nov.

Causes: the 2 Nov additions (202 products), the 3 Nov price changes (69 products) and the 3 Nov
concern-collection rebuild (concern pages still named products that left them).

Inputs:  docs/backups/stale_copy_before_2026-11-07.json (live values = before-state)
         <scratch>/sf2/<handle>.json (storefront products per collection, snapshot 7 Nov)
         <scratch>/allproducts2.json (storefront /products.json)
Output:  docs/seo/stale_copy_fix_2026-11-07.json (per collection: seo description, seo_copy, faq; old + new)
         docs/seo/stale_copy_fix_2026-11-07.md (review: changed sentences / FAQ answers)

Counts updated 8 Nov 2026 after the Hemel duplicates and label fixes (unisex 299, floral 238, niche 72, gifts-over-50 142),
then after the site-wide gender + family fixes of both 8 Nov sessions (storefront: unisex 238, women 197, men 121).
WARNING (8 Nov 2026): scent-oud / scent-woody / scent-fresh / unisex copy, descriptions and FAQs were rewritten later by
tools/shopify/label_fixes_all.py (oud 'more than 30', woody 'more than 130', fresh 'more than 40 … from £9.99', unisex 230).
This script's E/DESC for those pages are older: diff against live and skip them, or update E/DESC first.
Rules: counts on big pages become 'more than N' (N = count rounded down to the ten below), so they stay
true as products are added; small pages keep exact numbers. Named-product prices = current lowest price.
Products that are no longer on a concern page are not named on it. FAQ price ranges, gender splits,
mini/set counts, 'including' / 'start with' examples are recomputed from live data. No claim-named products
(acne / lightening / hairfall / de-tan) are used as examples.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
S = pathlib.Path(sys.argv[1])
BEFORE = {n["handle"]: n for n in json.load(open(ROOT / "docs/backups/stale_copy_before_2026-11-07.json"))["collections"]}
SKIP = {"armaf", "oud-perfume", "arabian-perfume"}
P = {h: json.load(open(S / f"sf2/{h}.json")) for h in list(BEFORE) + ["perfume-gift-sets", "travel-size-minis"] if (S / f"sf2/{h}.json").exists()}
GENDER = {"for her": {p["handle"] for p in P["perfume-for-women"]}, "for him": {p["handle"] for p in P["perfume-for-men"]},
          "unisex": {p["handle"] for p in P["unisex-perfume"]}}
MINI = {p["handle"] for p in P["perfume-gift-sets"]} | {p["handle"] for p in P["travel-size-minis"]}
CLAIMY = re.compile(r"acne|lighten|hairfall|hair fall|de- ?tan|pigment|anti-ageing|anti-aging|greying", re.I)


def more_than(n):
    return f"more than {(n - 1) // 10 * 10}"


def short(p):
    t = p["title"].split(" – ")[0].split(" | ")[0]
    for v in (p["vendor"] + " ", "Deyga's ", "Deyga ", "Vilvah ", "Highborn London "):
        if t.startswith(v):
            t = t[len(v):]
    return t.strip()


def examples(h, k=3):
    ps = [p for p in P[h] if p["avail"] and not CLAIMY.search(p["title"])] or [p for p in P[h] if not CLAIMY.search(p["title"])]
    names = [short(p) for p in ps[:k]]
    if any(x != y and x in y for x in names for y in names):
        names = [p["title"].split(" – ")[0].split(" | ")[0] for p in ps[:k]]
    return ", ".join(names[:-1]) + " and " + names[-1] if len(names) > 1 else names[0]


BAND = {"gifts-25-to-50": (25, 50), "gifts-over-50": (50, 1e9), "gifts-under-25": (0, 25)}


def rng(h):
    lo_b, hi_b = BAND.get(h, (0, 1e9))
    pr = [float(x) for p in P[h] for x in p["prices"] if lo_b <= float(x) <= hi_b]
    f = lambda v: f"£{v:.2f}".replace(".00", "") if v == int(v) and v >= 20 else f"£{v:.2f}"
    return f(min(pr)), f(max(pr))


def vendors(h):
    m = {"Swansura - The Body Studio": "Swansura Selection"}
    c = {}
    for p in P[h]:
        v = m.get(p["vendor"], p["vendor"])
        c[v] = c.get(v, 0) + 1
    vs = [v for v, _ in sorted(c.items(), key=lambda x: -x[1])][:3]
    return ", ".join(vs[:-1]) + " and " + vs[-1] if len(vs) > 1 else vs[0]


# ---- copy edits: (old HTML substring, new) ------------------------------------------------------
E = {
 "deyga": [("Chocolate Body Butter 100G (£15.99)", "Chocolate Body Butter 100G (£13.99)"),
           ("The Mini Foot Spa Combo (£37.99)", "The Mini Foot Spa Combo (£35.99)")],
 "fumeri": [("from £23, with most at £23.95 or £37.95.", "from £23.95 to £40.99.")],
 "sap": [("each at £37.95,", "each at £43.99,")],
 "the-woods-collection": [("each in a 100ml bottle at £44.99.", "each in a 100ml bottle at £39.99 or £40.99."),
                          ("At £44.99 each, they also suit", "At £39.99 to £40.99 each, they also suit")],
 "signature-dorient": [("We stock 16 pieces, from £38.99 to £75.99.", "We stock 16 pieces, from £35.99 to £66.99."),
                       ("Black Pour Homme 100ml (£38.99)", "Black Pour Homme 100ml (£37.99)"),
                       ("Discovery Set 10x10ml (£75.99)", "Discovery Set 10x10ml (£65.99)"),
                       ("Musk, Onyx and Sapphire (£64.99 each)", "Musk, Onyx and Sapphire (£63.99 each)"),
                       ("Diamond, Jade and Opal are £64.99, and Rose is £44.99.", "Diamond is £65.99, Jade £66.99, and Opal and Rose £63.99."),
                       ("Santal and Ambre (£65.99)", "Santal and Ambre (£63.99)"),
                       ("Aura, Paradiso and Charm (£74.95)", "Aura, Paradiso and Charm (£63.99 to £66.99)"),
                       ("Le Femme Gold 100ml EDP Spray (£42.99)", "Le Femme Gold 100ml EDP Spray (£35.99)")],
 "al-haramain": [("Amber Oud Gold Edition (£29.99)", "Amber Oud Gold Edition (from £32.99)"),
                 ("Tobacco Edition 60ml (£34.99)", "Tobacco Edition 60ml (£32.99)"),
                 ("Ruby (£41.99) brings saffron and jasmine, Black (100ml, £41.99) is smoky with leather and resins, Bleu (£35.99) is fresh and aromatic, and Carbon (£34.99)",
                  "Ruby (from £41.99) brings saffron and jasmine, Black (100ml, £39.99) is smoky with leather and resins, Bleu (from £38.99) is fresh and aromatic, and Carbon (from £35.99)"),
                 ("Extreme Gold Edition Extrait de Parfum at £37.99.", "Extreme Gold Edition Extrait de Parfum from £36.99."),
                 ("fresher 100ml bottles from £24.99.", "fresher 100ml bottles from £29.99."),
                 ("The original L'Aventure (£27.99)", "The original L'Aventure (£29.99)"),
                 ("L'Aventure Intense (£30.99)", "L'Aventure Intense (£39.99)")],
 "skincare": [("brings together 109 face and lip products", "brings together more than 110 face and lip products")],
 "concern-lips": [("This edit gathers 17 lip care products", "This edit gathers 21 lip care products"),
                  ("Vilvah Grape Fruit Lip Balm gives a soft natural tint,", "Vilvah Grape Fruit Lip Balm gives a soft natural tint, Vilvah's Rose Milk, Filter Kaapi, Mango Shake and Cream Bun lip balms (£9.99 each) add new flavours,")],
 "price-0-15": [("This edit gathers 56 products,", "This edit gathers more than 70 products,")],
 "price-15-25": [("with over 100 products,", "with more than 200 products,"),
                 ("Armaf Hunter at £22.99.", "Armaf Hunter at £19.99."),
                 ("chocolate body butter at £15.99,", "chocolate body butter at £13.99,"),
                 ("Activated Charcoal Body Wash are £15.99 each.", "Activated Charcoal Body Wash are £13.99 each."),
                 ("Hermès Un Jardin 15ml miniatures, at £24.99,", "Hermès Un Jardin 15ml miniatures, from £24.99,")],
 "price-25-50": [("with 219 products from", "with more than 300 products from"),
                 ("Deyga Vitamin C Daily Glow Combo is £30.99.", "Deyga Vitamin C Daily Glow Combo is £26.99.")],
 "vitamin-c-serum": [("the Vitamin C Daily Glow Combo (£30.99)", "the Vitamin C Daily Glow Combo (£26.99)")],
 "hair-oil-for-dry-hair": [("Our edit has six oils, serums and kits", "Our edit has four oils, serums and kits"),
                           (" Deyga's Premature Greying Hair Oil 100ML (£18.99) adds coconut, castor and moringa oils with traditional herbs.", "")],
 "face-mask-for-oily-skin": [("Deyga's Charcoal Detox Face Mask (£15.99)", "Deyga's Charcoal Detox Face Mask (£13.99)")],
 "perfume-for-women": [("This edit brings together 67 eaux", "This edit brings together more than 190 eaux")],
 "perfume-for-men": [("This edit gathers 59 eaux", "This edit gathers more than 110 eaux"),
                     ("Armaf Hunter (£22.99)", "Armaf Hunter (£19.99)")],
 "unisex-perfume": [("more than 230 shareable fragrances", "more than 230 shareable fragrances"),
                    ("Montale Aoud Safran (£54.99)", "Montale Aoud Safran (£62.99)"),
                    ("Amber Oud Tobacco Edition (£34.99)", "Amber Oud Tobacco Edition (£32.99)")],
 "niche-perfume": [("This edit brings together 73 fragrances", "This edit brings together more than 70 fragrances"),
                   ("Montale Aoud Safran (£54.99)", "Montale Aoud Safran (£62.99)")],
 "gifts-for-him": [("This edit gathers 66 perfumes", "This edit gathers more than 70 perfumes")],
 "gifts-25-to-50": [("Hemel Gris and Dorado (£49.99 each)", "Hemel Gris (£53.99) and Dorado (£54.99)")],
 "gifts-over-50": [("over 130 fragrances and skincare collections", "over 140 fragrances and skincare collections")],
 "diwali-gifts": [("Amber Oud Gold Edition (£29.99)", "Amber Oud Gold Edition (from £32.99)"),
                  ("the Ruby Edition (£41.99)", "the Ruby Edition (from £41.99)"),
                  ("Tom Ford Oud Wood (£115.99)", "Tom Ford Oud Wood (from £115.99)"),
                  ("The Woods Collection Wild Roses (£44.99)", "The Woods Collection Wild Roses (£39.99)")],
 "ramadan-eid-gifts": [("L'Aventure (£27.99) is fresh and confident, L'Aventure Blanche (£24.99) is crisp and clean, and L'Aventure Gold (£28.99)",
                        "L'Aventure (£29.99) is fresh and confident, L'Aventure Blanche (£29.99) is crisp and clean, and L'Aventure Gold (£32.99)"),
                       ("Hemel Dorado (£49.99)", "Hemel Dorado (£54.99)")],
 "range-charcoal": [("gentle enough for daily use on all skin types, at £25.99.", "gentle enough for daily use on all skin types, from £12.99."),
                    ("Deyga Charcoal Detox Face Mask 100G at £15.99,", "Deyga Charcoal Detox Face Mask 100G at £13.99,"),
                    ("deep-cleansing feel, at £15.99.", "deep-cleansing feel, at £13.99.")],
 "range-vitamin-c": [("the Vitamin C Daily Glow Combo is £30.99.", "the Vitamin C Daily Glow Combo is £26.99.")],
 "range-oud": [("Our oud range gathers 27 fragrances, from £19.99,", "Our oud range gathers 26 fragrances, from £29.99,"),
               ("Fumeri Oud Saffron For Men, at £23.95,", "Fumeri Oud Saffron For Men, at £29.99,")],
 "scent-oud": [("Gold Edition at £29.99,", "Gold Edition from £32.99,")],
 "scent-amber": [("There are over 30 fragrances,", "There are more than 90 fragrances,"),
                 ("Swansura Selection Roll It 1 is a unisex Eau de Parfum at £99.99.", "Game of Spades Roll It 1 is a unisex Eau de Parfum at £99.99.")],
 "scent-floral": [("this floral perfume edit gathers 166 fragrances", "this floral perfume edit gathers more than 230 fragrances")],
 "scent-woody": [("This edit gathers 95 woody fragrances", "This edit gathers more than 140 woody fragrances")],
 "scent-fresh": [("gathers 25 bright, clean and easy-to-wear fragrances from £16.99,", "gathers more than 40 bright, clean and easy-to-wear fragrances from £9.99,"),
                 ("Fumeri Blue For Men offers a fresh men's option at £23.95.", "Fumeri Blue For Men offers a fresh men's option at £28.99."),
                 ("Antonio Banderas Power of Seduction, at £16.99, is the lowest-priced bottle here.", "Antonio Banderas Power of Seduction, at £16.99, is one of the lowest-priced bottles here.")],
 "swansura-selection": [("There are seven pieces, from £9.99.", "There are six pieces, from £9.99."),
                        ("<p>The selection also includes Roll It 1 Unisex Eau de Parfum 100ml from <a href=\"/collections/jo-milano\">Jo Milano</a>. Find more bars", "<p>Find more bars")],
}

# ---- concern pages: rewritten from their current products (3 Nov rebuild) -----------------------
NEW_COPY = {
 "concern-acne": """<p>If your skin runs shiny or breaks out easily, a face wash for oily skin is the first step. This edit gathers products for oily and blemish-prone skin from Deyga and Vilvah, from £9.99 to £34.99. Charcoal, neem and tea tree lead the ingredient list. Swansura is an official UK partner of both brands and ships from the UK.</p><h3>Cleanse and tone</h3><p>Deyga Charcoal Face Wash uses activated charcoal to lift dirt and excess oil, and is the charcoal face wash most people start with. After cleansing, Deyga Tea Tree Facial Toner is a toner for oily skin and combination skin. In the shower, Deyga Activated Charcoal Body Wash, Deyga Charcoal Bath Bar, Neem &amp; Turmeric Bath Bar and the Charcoal Goatmilk Soap Bar carry the same ingredients through to the body.</p><h3>Weekly masks</h3><p>Once or twice a week, use a face mask for oily skin: Deyga Spirulina Matcha Face Pack, Deyga Charcoal Detox Face Mask, Vilvah Charcoal Face Mask or Vilvah Milk Mud Mask. Deyga Face &amp; Body Exfoliator Powder adds a weekly polish for face and body.</p><h3>Kits and routines</h3><p>Kits such as Vilvah Oil Control Kit, Vilvah Pore Minimising Kit and Deyga Clear Skin Kit group matching steps. Our <a href="/collections/sets-combos">Clear Skin Routine</a> pairs a charcoal wash with a tea tree toner. For more, see <a href="/collections/oily-skin">skincare for oily and acne-prone skin</a> and our <a href="/collections/face-wash-for-oily-skin">face wash for oily skin guide</a>. Spend over £40 for free UK delivery.</p>""",
 "concern-glow": """<p>A good face serum for glowing skin is the heart of this edit, which gathers serums, masks and kits for dullness and uneven-looking tone, from £11.99 to £89. You will find Indian natural care from Deyga and Vilvah, luxury English skincare from Highborn London and a few Swansura Selection treats, all sent from the UK.</p><h3>Serums and cleansers</h3><p>Deyga Rose Glow Serum, Deyga 10% Vitamin C Face Serum and the Vitamin C Daily Glow Combo suit everyday use, and the Vilvah and Deyga Beautifying Serums are light everyday options. If you need a face serum for dull skin with a richer feel, Highborn London MOISTUREBURST Hydrating Glow Ceramide Serum is made for dry and dehydrated skin. Whichever face serum for glowing skin you choose, apply it after cleansing and before moisturiser. Start the routine with Deyga Vitamin C Foaming Face Wash, a vitamin c face wash at £15.99, or Vilvah Honey Face Wash.</p><h3>Masks and kits</h3><p>Skincare for dull skin often includes a weekly mask. Deyga Orange &amp; Almond Face Pack Powder and Spirulina Matcha Face Pack are mixed fresh, Vilvah Wild Rose Face Mask is ready to use, and the Swansura Selection 24K Gold Hydrating Face Mask adds a golden finishing touch. Vilvah's AM Brightening Kit, Face Brightening Kit and Skin Radiance Large Kit put serum and care steps together, and Deyga's Healthy Glow Kit is a smaller starter set.</p><h3>Finish and body</h3><p>Highborn London GLOWGUARD SPF30 Anti-Ageing Moisturiser adds daily SPF to the last step. For the body, Highborn London Natural Luminosity Scrub and the Scrub and Glow Luminosity Set leave skin feeling smoother. See our <a href="/collections/range-vitamin-c">Vitamin C range</a>, the <a href="/collections/sets-combos">Vitamin C Glow Routine</a> and <a href="/collections/dull-skin">skincare for dull skin</a> for more ideas. Free UK delivery starts at £40.</p>""",
 "concern-hydration": """<p>Finding the right moisturiser for dry skin is easier when everything sits in one place. This edit gathers products for dry, tight-feeling skin, from face creams and serums to body lotions and butters, from £9.99. Brands include Vilvah, Deyga and Highborn London, and every order is sent from the UK.</p><h3>Face care for dry skin</h3><p>Deyga Deep Moisturising Face Cream is a natural moisturiser made with plant-based oils, at £18.99, and Vilvah Ultra Moisturising Cream is a richer option. Highborn London Imperial Moisturiser offers rich moisture for dry, tight-feeling skin. Layer a serum underneath: Deyga 2% Hyaluronic Acid Serum, Vilvah Milk Drops Hydrating Serum or Highborn London MOISTUREBURST Hydrating Glow Ceramide Serum. In the evening, Highborn London Night Elixir works as a comforting night cream, and Four Phase Day and Night brings serum, eye gel, day cream and night cream together. For the eye area, Imperial Eye Gel is a lighter choice than a classic under eye cream.</p><h3>Cleanse and tone gently</h3><p>Deyga Oat Milk Face Wash, Vilvah Fragrance-Free Cream Face Wash and Vilvah Milk Powder Face Wash cleanse without a tight feel, and Deyga Pure Rose Water Toner, Vilvah Rosewater Facial Toner and Vilvah Milk Face Toner add a hydrating step.</p><h3>Body care</h3><p>Skincare for dry skin carries on below the neck. Deyga Chocolate Body Butter (£13.99) and Rose &amp; Geranium Body Butter (£15.99) are body butters for dry skin, and Highborn London Natural Luminosity Body Butter is the luxury pick. Deyga Almond Milk Body Lotion and Vilvah Milk Body Lotion are lighter, and Vilvah Foot Care Cream and Deyga Foot Butter look after dry feet.</p><p>Our <a href="/collections/sets-combos">Deep Hydration Routine</a> pairs Vilvah Honey Face Wash, the hyaluronic acid serum and the deep moisturising cream. For focused lists, see <a href="/collections/moisturiser-for-dry-skin">moisturiser for dry skin</a> and <a href="/collections/body-butter-for-dry-skin">body butter for dry skin</a>. Orders over £40 get free UK delivery.</p>""",
 "concern-hairfall": """<p>A weekly massage with a hair oil is a traditional Indian ritual, and this edit gathers hair oils and kits from Deyga and Vilvah, from £9.99 to £36.99. Swansura is an official UK partner of both brands and ships every order from the UK. These are cosmetic products to nourish your scalp and hair; if you are worried about sudden hair loss, speak to your GP.</p><h3>Oils for the scalp</h3><p>Deyga Hair Growth Oil 100 ml blends coconut, amla, hibiscus, castor and fenugreek, so it covers anyone searching for an amla hair oil or a hibiscus hair oil in one bottle, at £14.99. Vilvah Hair Growth Oil is alcohol-free, with pumpkin seed, kalonji, castor and grapeseed oils, from £9.99. People often look for a hair oil for hair loss; these oils are made to nourish the scalp and lengths.</p><h3>Kits</h3><p>Deyga Hair Care Kit pairs a rice water shampoo with soy milk conditioner, and Deyga Hair Nourishment Kit, Vilvah Hair Strengthening Kit and Vilvah Bestseller Hair Kit put oil, wash and care steps together. If you are searching for a shampoo for hair loss, our <a href="/collections/shampoo-for-hair-loss">shampoo for hair loss page</a> compares gentle cleansing options.</p><p>Our <a href="/collections/sets-combos">Hair Care Routine</a> brings oil, wash and condition together, and you can see the rest in <a href="/collections/haircare">Haircare</a>. Free UK delivery starts at £40.</p>""",
}
E["concern-sun"] = [
    ("This small edit gathers 9 sun care products from Vilvah, Deyga and Highborn London, with prices from £9.99.",
     "This small edit gathers six sun care products from Vilvah, Deyga and Highborn London, from £9.99 to £68."),
    (", and the Skin Brightening Kit adds a serum to the routine.", ", and the Vilvah Tan Protection Kit pairs the SPF 50 sunscreen with the Milk Mud Mask."),
]

DESC = {
 "the-woods-collection": "The Woods Collection perfume range is simple to shop: 11 unisex eaux de parfum, each in a 100ml bottle at £39.99 or £40.99.",
 "concern-glow": "A good face serum for glowing skin is the heart of this edit: serums, masks and kits from Deyga, Vilvah and Highborn London. Free UK delivery over £40.",
 "concern-hairfall": "A weekly massage with a hair oil is a traditional Indian ritual. Deyga and Vilvah hair oils and kits, 100% authentic, free UK delivery over £40.",
 "price-15-25": "Our £15 to £25 edit is full of gifts under £25, with more than 200 products from designer perfume minis to natural body care.",
 "price-25-50": "Our £25 to £50 edit is where you will find gifts under £50 that feel special, with more than 300 products from full-size perfumes to routines.",
 "range-oud": "Our oud range gathers 26 fragrances, from £29.99, and a good share of it is oud perfume for men, alongside many unisex bottles.",
 "scent-oud": "Our oud perfume edit gathers more than 40 fragrances built on smoky, resinous agarwood, from £17.99. 100% authentic, free UK delivery over £40.",
 "unisex-perfume": "A unisex perfume is made for anyone who loves it: more than 230 scents beyond the for him and for her labels. Free UK delivery over £40.",
 "scent-floral": "Floral is the biggest family on our shelf, and this floral perfume edit gathers more than 230 fragrances built around rose, jasmine and white flowers.",
}


def fix_faq(h, faq):
    n = len(P[h])
    lo, hi = rng(h)
    out = []
    for q, a in faq:
        a0 = a
        if re.fullmatch(r"Prices( in this edit)? run from £\d+(?:\.\d\d)? to £\d+(?:\.\d\d)?\.", a):
            a = re.sub(r"from £\d+(?:\.\d\d)? to £\d+(?:\.\d\d)?", f"from {lo} to {hi}", a)
        elif re.fullmatch(r"From £\d+(?:\.\d\d)? to £\d+(?:\.\d\d)?\.", a):
            a = f"From {lo} to {hi}."
        elif re.match(r"Products from £\d+(?:\.\d\d)? to £\d+(?:\.\d\d)?:", a):  # deyga: keep the type split
            a = re.sub(r"from £\d+(?:\.\d\d)? to £\d+(?:\.\d\d)?", f"from {lo} to {hi}", a)
        elif re.match(r"\d+ products?, from £\d+(?:\.\d\d)? to £\d+(?:\.\d\d)?: (unisex|for him|for her)", a):
            hs = {p["handle"] for p in P[h]}
            parts = sorted(((len(hs & GENDER[g]), g) for g in GENDER if hs & GENDER[g]), reverse=True)
            a = f"{n} product{'s' if n != 1 else ''}, from {lo} to {hi}: " + ", ".join(f"{g} ({c})" for c, g in parts) + "."
        elif h == "swansura-selection" and re.match(r"\d+ products, from", a):
            a = f"{n} products, from {lo} to {hi}: bath & soap (4), serums (1), masks (1)."
        elif re.match(r"\d+ products from .*, including ", a):  # concern pages
            a = f"{n} products from {vendors(h)}, including {examples(h)}."
        elif re.match(r"\d+ products: \d+ ", a):  # price bands
            a = f"{more_than(n).capitalize()} products across skincare, haircare, bath and body and fragrance, including {examples(h)}."
        elif m := re.match(r"(.*made with [\w ]+: )(\d+) fragrance products\.$", a):
            a = f"{m.group(1)}{n} fragrance products."
        elif re.fullmatch(r"Yes: [\d\w ,]+\.", a) and h.startswith("scent-"):
            hs = {p["handle"] for p in P[h]}
            parts = sorted(((len(hs & GENDER[g]), g) for g in GENDER if hs & GENDER[g]), reverse=True)
            a = "Yes: " + ", ".join(f"{c} {g}" for c, g in parts) + "."
        elif re.match(r"Yes, \d+: ", a) and h.startswith("scent-"):
            ms = [p for p in P[h] if p["handle"] in MINI]
            if h == "scent-oud":  # Daisy Love sits in scent-oud but is not an oud: keep it out of the answer
                ms = [p for p in ms if "oud" in p["title"].lower()]
            if len(ms) == 1:
                a = f"Yes: {ms[0]['vendor']} {short(ms[0])}."
            elif ms:
                names = [short(p) for p in ms[:3]]
                a = f"Yes, {len(ms)}: " + ", ".join(names[:-1]) + " and " + names[-1] + (" and more." if len(ms) > 3 else ".")
            else:
                a = "Not at the moment."
        elif m := re.match(r"(.*?(?:Examples here include|Good places to start are) )(.*)\.$", a):
            titles = " ".join(p["title"] for p in P[h])
            names = re.split(r", | and ", m.group(2))
            if not all(nm in titles for nm in names):
                a = m.group(1) + examples(h) + "."
        out.append([q, a])
    return out


rows, md = [], ["# Out-of-date counts and prices fixed (7 Nov 2026)\n"]
for h, n in BEFORE.items():
    if h in SKIP:
        continue
    cp_old = (n["cp"] or {}).get("value") or ""
    cp = NEW_COPY.get(h, cp_old)
    for old, new in E.get(h, []):
        assert cp.count(old) == 1, (h, old)
        cp = cp.replace(old, new)
    faq_old = json.loads(n["faq"]["value"]) if n["faq"] else []
    faq = fix_faq(h, faq_old)
    d_old = n["seo"]["description"] or ""
    d = DESC.get(h, d_old)
    assert d == d_old or len(d.replace("'", "&#39;")) <= 158, (h, len(d))
    rows.append({"handle": h, "id": n["id"], "seo_title": n["seo"]["title"], "desc_old": d_old, "desc": d,
                 "copy_old": cp_old, "copy": cp, "faq_old": faq_old, "faq": faq,
                 "changed": {"desc": d != d_old, "copy": cp != cp_old, "faq": faq != faq_old}})
    md.append(f"\n## /collections/{h} ({len(P[h])} products)\n")
    if d != d_old:
        md.append(f"- **Description:** {d_old}\n  → {d}\n")
    if h in NEW_COPY:
        md.append("- **Copy rewritten** from the current products (concern rebuild of 3 Nov).\n")
    for old, new in E.get(h, []):
        md.append(f"- {html.unescape(old) or '(added)'}\n  → {html.unescape(new) or '(removed)'}\n")
    for (q, a0), (_, a1) in zip(faq_old, faq):
        if a0 != a1:
            md.append(f"- FAQ *{q}* {a0}\n  → {a1}\n")

json.dump(rows, open(ROOT / "docs/seo/stale_copy_fix_2026-11-07.json", "w"), ensure_ascii=False, indent=1)
open(ROOT / "docs/seo/stale_copy_fix_2026-11-07.md", "w").write("".join(md))
print(len(rows), "collections;", sum(any(r["changed"].values()) for r in rows), "changed")

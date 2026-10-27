"""Publish the 3 priced Vilvah draft kits from the Drive photos (user, 27 Oct 2026: 'Go ahead with the 3 priced ones').

Writes docs/seo/priced_drafts_2026-10-27.json: per product the productUpdate input (description, SEO, tags,
status ACTIVE), metafields (custom.h1 / sw / pdp / inci / inci_data, same shapes as the live Vilvah kits) and the
collections to join (copied from the closest live sibling kit). Ingredient lists come from the client's Vilvah
catalogue (docs/data/vilvah_inci_2026-10-22.json). Copy is factual, no medical claims (ASA).
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
INCI = {}
for r in json.load(open(ROOT / "docs/data/vilvah_inci_2026-10-22.json")):
    for c in r["components"]:
        INCI.setdefault(c["n"], c)
def comps(*names):  # drop empty entries (the catalogue's Foot Care Cream list ends with one)
    return [dict(INCI[n], l=[i for i in INCI[n]["l"] if i[0].strip()]) for n in names]
def inci_text(cs): return "\n".join(f'{c["n"]}: ' + ", ".join(i[0] for i in c["l"]) for c in cs)
GIFT_KW = [["Natural skincare", "/collections/natural-skincare"], ["Gifts for her", "/collections/gifts-for-her"],
           ["Gifts £25 to £50", "/collections/gifts-25-to-50"], ["Christmas gifts", "/collections/christmas-gifts"]]
P = [
 {"id": "gid://shopify/Product/16396843581827", "title": "Vilvah Anti-Frizz Hair Kit",
  "html": "<p>A two-piece kit for smoother-looking, more manageable hair: Vilvah's Anti-Frizz Hair Serum 30ml and a neem wood comb with a handle.</p>"
          "<h3>In this kit</h3><ul><li><b>Anti-Frizz Hair Serum 30ml</b> – a silicone-free serum with black seed, curry leaf, hibiscus and arnica oils that helps tame frizz and flyaways and adds shine.</li>"
          "<li><b>Neem wood comb with handle</b> – a smooth wooden comb that glides through hair with less static than plastic.</li></ul>"
          "<h3>How to use</h3><p>Warm 2–3 drops of serum between your palms and smooth over the lengths and ends of damp or dry hair, then comb through with the neem comb. Patch test before first use.</p>",
  "seo_t": "Vilvah Anti-Frizz Hair Kit: Serum & Neem Comb | Swansura",
  "seo_d": "Buy the Vilvah Anti-Frizz Hair Kit: a silicone-free hair serum with black seed and curry leaf oils plus a neem wood comb. Free UK delivery over £40.",
  "h1": "Vilvah Anti-Frizz Hair Kit for Frizzy Hair", "tags": ["drive-photos", "vilvah", "Sets & Combos", "Haircare"],
  "comps": comps("Anti-Frizz Hair Serum"),
  "sw": {"t": "Kits & routines", "s": ["Dry", "Combination"], "c": ["hydration"], "k": False, "r": 62, "g": ["Kalonji", "Hibiscus"],
         "a": ["Anti-Frizz Hair Serum 30ml with black seed, curry leaf, hibiscus and arnica oils, plus a neem wood comb.",
               "Kalonji: black-seed oil for hair care. Hibiscus: conditioning flower for hair. The full ingredient list is printed on the pack.",
               "Smooth 2–3 drops of serum over damp or dry hair, then comb through. Patch test before first use.",
               "It suits dry and frizz-prone hair. If your skin is sensitive, patch test before first use."]},
  "pdp": {"cat": "haircare", "ben": "Silicone-free serum with black seed and curry leaf oils, plus a neem wood comb, for smoother-looking hair.", "more": False,
          "chips": ["Frizz control", "Natural formula"], "how": ["Warm 2–3 drops of serum in your palms, smooth over the lengths and ends, then comb through."],
          "pair": ["vilvah-frizz-free-hair-kit", "vilvah-shampoo-hair-serum-kit"],
          "sim": ["vilvah-frizz-free-hair-kit", "vilvah-shampoo-hair-serum-kit", "vilvah-goat-milk-hair-kit", "vilvah-bestseller-hair-kit-goat-milk-shampoo-200ml-cream-conditioner-200ml-nourishing-frizz-control-sulfate-free-hair-care-set"],
          "kw": [["Hair serum for frizzy hair", "/collections/hair-serum-for-frizzy-hair"]] + GIFT_KW},
  "colls": ["milk-drop-brightening-serum", "giftsets", "haircare-tools-kits", "haircare", "sets-combos", "concern-hydration", "price-25-50",
            "hair-serum-for-frizzy-hair", "natural-skincare", "gifts-for-her", "gifts-25-to-50", "diwali-gifts", "christmas-gifts"]},
 {"id": "gid://shopify/Product/16396843712899", "title": "Vilvah Face Brightening Kit Large",
  "html": "<p>The larger version of Vilvah's Face Brightening Kit: the Milk Powder Face Wash and the full-size Milk Drops Serum 40ml, for a simple cleanse-then-serum routine for dull-looking skin.</p>"
          "<h3>In this kit</h3><ul><li><b>Milk Powder Face Wash</b> – a powder-to-foam cleanser with a rice complex, hyaluronic acid and papain that lathers with water and leaves skin feeling clean and soft.</li>"
          "<li><b>Milk Drops Serum 40ml</b> – a lightweight serum with rice milk extract, aloe vera and hyaluronic acid for hydrated, radiant-looking skin.</li></ul>"
          "<h3>How to use</h3><p>Morning and evening: mix a little face wash powder with water in your palm, massage onto damp skin and rinse. Then pat 2–3 drops of serum onto clean skin. Patch test before first use.</p>",
  "seo_t": "Vilvah Face Brightening Kit Large | Dull Skin | Swansura",
  "seo_d": "Buy the Vilvah Face Brightening Kit Large: Milk Powder Face Wash and Milk Drops Serum 40ml for dull-looking skin. Official UK partner, free delivery over £40.",
  "h1": "Vilvah Face Brightening Kit Large – Skincare for Dull Skin", "tags": ["drive-photos", "vilvah", "Sets & Combos", "Skincare"],
  "comps": comps("Milk Powder Face Wash", "Milk Drops Serum"),
  "sw": {"t": "Kits & routines", "s": ["Oily", "Combination"], "c": ["glow", "hydration"], "k": False, "r": 83, "g": ["Hyaluronic acid", "Rice water"],
         "a": ["Milk Powder Face Wash and Milk Drops Serum 40ml: a cleanse-then-serum routine for dull-looking skin.",
               "Hyaluronic acid: draws in and holds moisture. Rice water: smoothing rice extract. The full ingredient list is printed on the pack.",
               "Use morning and evening: cleanse with the face wash, then apply 2–3 drops of serum. Patch test before first use.",
               "It suits normal, oily and combination skin. If your skin is sensitive, patch test before first use."]},
  "pdp": {"cat": "skincare", "ben": "Milk Powder Face Wash plus the full-size Milk Drops Serum 40ml for a cleanse-then-serum routine.", "more": False,
          "chips": ["Radiance", "Hydration"], "how": ["Cleanse with the face wash, then pat 2–3 drops of serum onto clean skin, morning and evening."],
          "pair": ["vilvah-tan-protection-kit", "vilvah-everyday-care-milk-kit"],
          "sim": ["vilvah-face-brightening-kit-milk-powder-face-wash-milk-drops-brightening-serum-duo-milky-cleanse-radiance-boost-evens-skin-tone-fades-dark-spots",
                  "pre-eminent-beauty-serum", "imperial-moisturiser", "cleanse-and-tone-pack"],
          "kw": [["Skincare for dull skin", "/collections/dull-skin"], ["Skincare for oily & acne-prone skin", "/collections/oily-skin"]] + GIFT_KW},
  "colls": ["milk-drop-brightening-serum", "giftsets", "skincare-tools-kits", "skincare", "sets-combos", "concern-glow", "concern-hydration", "price-25-50",
            "oily-skin", "dull-skin", "natural-skincare", "gifts-for-her", "gifts-25-to-50", "diwali-gifts", "christmas-gifts"]},
 {"id": "gid://shopify/Product/16396843811203", "title": "Vilvah Foot Cream & Body Lotion Kit",
  "html": "<p>A body-care pair for dry skin from head to toe: Vilvah's Foot Care Cream 100ml and Milk Body Lotion 250ml.</p>"
          "<h3>In this kit</h3><ul><li><b>Foot Care Cream 100ml</b> – a rich cream with shea, mango and avocado butters plus argan and kalonji oils that softens dry, rough-feeling feet.</li>"
          "<li><b>Milk Body Lotion 250ml</b> – a fast-absorbing lotion with oat milk, ceramide, olive squalane and jojoba oil for everyday hydration.</li></ul>"
          "<h3>How to use</h3><p>Smooth the body lotion over skin after a bath or shower. Massage the foot cream into clean, dry feet, ideally before bed. Patch test before first use.</p>",
  "seo_t": "Vilvah Foot Cream & Body Lotion Kit | Swansura",
  "seo_d": "Buy the Vilvah Foot Cream & Body Lotion Kit: Foot Care Cream 100ml with shea and avocado butters and oat milk Body Lotion 250ml. Free UK delivery over £40.",
  "h1": "Vilvah Foot Cream & Body Lotion Kit for Dry Skin", "tags": ["drive-photos", "vilvah", "Sets & Combos", "Bodycare"],
  "comps": comps("Foot Care Cream", "Milk Body Lotion"),
  "sw": {"t": "Kits & routines", "s": ["All", "Dry"], "c": ["hydration"], "k": False, "r": 108, "g": ["Shea butter", "Oat milk"],
         "a": ["Foot Care Cream 100ml and Milk Body Lotion 250ml: a body-care pair for dry skin.",
               "Shea butter: rich, cushioning nourishment. Oat milk: soothing, softening hydration. The full ingredient list is printed on the pack.",
               "Use the lotion after bathing and the foot cream on clean, dry feet, ideally before bed. Patch test before first use.",
               "It is made for all skin types. If your skin is sensitive, patch test before first use."]},
  "pdp": {"cat": "bath-body", "ben": "Foot Care Cream with shea and avocado butters plus an oat milk body lotion, for soft, hydrated skin.", "more": False,
          "chips": ["Hydration", "Natural formula"], "how": ["Lotion after bathing; foot cream on clean, dry feet before bed."],
          "pair": ["vilvah-milk-body-kit-goat-milk-body-wash-milk-body-lotion-deep-hydration-skin-softening-nourishment-oat-milk-olive-squalane-coconut-oil-vanilla-scent"],
          "sim": ["natural-luminosity-body-butter", "natural-luminosity-scrub", "coach-green-shower-gel-100ml-men-s-fresh-aromatic-body-wash", "superior-lip-butter-large-50ml"],
          "kw": [["Body lotion for dry skin", "/collections/body-lotion-for-dry-skin"], ["Skincare for dry skin", "/collections/dry-skin"]] + GIFT_KW},
  "colls": ["milk-drop-brightening-serum", "giftsets", "bodycare-kits", "bodycare", "sets-combos", "body-cream-exfoliants", "concern-hydration", "price-25-50",
            "body-lotion-for-dry-skin", "dry-skin", "natural-skincare", "gifts-for-her", "gifts-25-to-50", "diwali-gifts", "christmas-gifts"]},
]
out = []
for p in P:
    assert len(p["seo_t"]) <= 60, p["seo_t"]; assert len(p["seo_d"]) <= 160, (len(p["seo_d"]), p["seo_d"])
    mf = lambda k, t, v: {"namespace": "custom", "key": k, "type": t, "value": v}
    out.append({"id": p["id"], "title": p["title"], "collections": p["colls"],
                "input": {"id": p["id"], "descriptionHtml": p["html"], "seo": {"title": p["seo_t"], "description": p["seo_d"]}, "tags": p["tags"], "status": "ACTIVE"},
                "metafields": [mf("h1", "single_line_text_field", p["h1"]), mf("sw", "json", json.dumps(p["sw"], ensure_ascii=False)),
                               mf("pdp", "json", json.dumps(p["pdp"], ensure_ascii=False)), mf("inci", "multi_line_text_field", inci_text(p["comps"])),
                               mf("inci_data", "json", json.dumps(p["comps"], ensure_ascii=False))]})
    print(p["title"], len(p["seo_t"]), len(p["seo_d"]), [c["n"] for c in p["comps"]])
json.dump(out, open(ROOT / "docs/seo/priced_drafts_2026-10-27.json", "w"), ensure_ascii=False, indent=1)

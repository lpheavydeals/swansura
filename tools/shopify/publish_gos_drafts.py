"""Publish 6 Game of Spades (Jo Milano) draft perfumes (user, 31 Oct 2026: 'Go ahead with the 7 finish & publish ones').

The 7th row of the old-drafts sheet (Vilvah Aloe Vera Gel Pack of 2) is NOT published: the live
'Vilvah Aloe Vera Gel 100ml' already sells a '2' option (£18.99), so it would be a second listing.

Writes docs/seo/gos_drafts_2026-10-31.json: per product the productUpdate input (title, handle, vendor, description,
SEO, status ACTIVE), metafields (custom.h1 / sw / pdp, same shapes as the live Game of Spades listings), collections
to join, media alt text (written after viewing every photo) and the media order (plain bottle shot first).
Scent notes come from the client's own draft descriptions; no performance claims (ASA).
Drafts were never published, so handles are shortened without redirects.
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]

COLL = {"fragrance": "689527685507", "jo-milano": "689549017475", "diamond-collection": "689549083011",
        "price-50-9999": "714069311875", "perfume-for-men": "714070884739", "unisex-perfume": "714070950275",
        "niche-perfume": "714070983043", "gifts-over-50": "714071212419", "scent-amber": "714071671171",
        "scent-floral": "714071703939", "scent-woody": "714071736707"}
PAIR = ["deyga-chocolate-body-butter-100g", "somali-frankincense-sleep-pillow-spray-overactive-mind-anatome"]
GOS = {"royale": "game-of-spades-royale-eau-de-parfum-100ml-long-lasting-luxury-perfume-for-men-women",
       "ruby": "game-of-spades-ruby-eau-de-parfum-100ml-luxury-long-lasting-perfume-for-men-women-designer-unisex-fragrance",
       "emerald": "game-of-spades-emerald-edp-100ml-long-lasting-luxury-unisex-perfume-for-men-women",
       "sapphire": "game-of-spades-yellow-sapphire-eau-de-parfum-100ml-fresh-luxury-unisex-perfume-designer-fragrance",
       "highroller": "game-of-spades-high-roller-eau-de-parfum-100ml-luxury-unisex-fragrance-citrus-spice-patchouli-powerhouse",
       "wildcard": "game-of-spades-wildcard-eau-de-parfum-100ml-long-lasting-luxury-unisex-perfume-woody-amber-vanilla-fragrance-for-men-women"}
FAM = {"woody": "Woody family", "amber": "Amber family", "floral": "Floral family"}
HOW = ("Spray from 15–20 cm onto pulse points such as the neck, inner wrists and inner elbows. "
       "Don't rub your wrists together. Patch test before first use if your skin is sensitive.")

P = [
 dict(id="15415430119811", name="Bid", who="Men", fam="woody", price="84.99", r=446,
      handle="game-of-spades-bid-eau-de-parfum-100ml-men",
      title="Game of Spades Bid Eau de Parfum 100ml for Men",
      notes="a fresh citrus opening, a spicy-woody heart and a warm amber base",
      look="the green Game of Spades bottle with a gold spade and knurled gold cap",
      sim=["royale", "highroller", "wildcard", "emerald"],
      alts=["bottle with its green spade-pattern box", "bottle among orange flower petals",
            "bottle with violets, sandalwood and a leather swatch", "bottle on a marble table in a living room",
            "bottle with violets, cardamom, wood and leather", "where to apply perfume: chest, neck, wrists and more"],
      order=[1, 2, 3, 4, 5, 6]),
 dict(id="15415431496067", name="Boston", who="Men", fam="woody", price="89.99", r=447,
      handle="game-of-spades-boston-eau-de-parfum-100ml-men",
      title="Game of Spades Boston Eau de Parfum 100ml for Men",
      notes="a fresh citrus top, a spicy heart and a woody-amber base",
      look="the matte black Game of Spades bottle with a teal spade",
      sim=["royale", "highroller", "wildcard", "ruby"],
      alts=["bottle with pineapple, lime, berries and wood", "bottle on black satin",
            "bottle among blackcurrants", "bottle on dark pebbles", "matte black bottle with teal spade",
            "bottle with its black box", "where to apply perfume: chest, neck, wrists and more"],
      order=[5, 6, 1, 2, 3, 4, 7]),
 dict(id="15415432184195", name="Diamond", who="Unisex", fam=None, price="85.99", r=448,
      handle="game-of-spades-diamond-eau-de-parfum-100ml",
      title="Game of Spades Diamond Unisex Eau de Parfum 100ml",
      notes=None,
      look="the black Game of Spades bottle with a crystal-set silver spade and ribbed silver cap",
      sim=["ruby", "emerald", "sapphire", "royale"],
      alts=["black bottle with crystal-set silver spade", "bottle resting on black stones",
            "bottle with its black textured box", "bottle lying on its side in low light",
            "close-up of the silver spade emblem", "where to apply perfume: chest, neck, wrists and more"],
      order=[1, 3, 2, 4, 5, 6]),
 dict(id="15415431528835", name="Jackpot", who="Unisex", fam="woody", price="79.99", r=449,
      handle="game-of-spades-jackpot-eau-de-parfum-100ml",
      title="Game of Spades Jackpot Unisex Eau de Parfum 100ml",
      notes="a citrus top, a floral-spicy heart and a woody-amber base",
      look="the polished gold Game of Spades bottle with a black spade",
      sim=["royale", "wildcard", "highroller", "ruby"],
      alts=["bottle with citrus slices, vanilla pods and berries", "bottle on a gold pedestal with red curtains",
            "bottle on a marble shelf in a panelled room", "bottle on gold satin", "polished gold bottle",
            "bottle with its gold box", "where to apply perfume: chest, neck, wrists and more"],
      order=[5, 6, 1, 2, 3, 4, 7]),
 dict(id="15415431922051", name="King", who="Unisex", fam="amber", price="73.99", r=450,
      handle="game-of-spades-king-eau-de-parfum-100ml",
      title="Game of Spades King Unisex Eau de Parfum 100ml",
      notes="citrus top notes, a fruity heart and an amber-vanilla base",
      look="the golden Game of Spades bottle with a black spade and knurled gold cap",
      sim=["ruby", "wildcard", "royale", "sapphire"],
      alts=["bottle with orange peel, berries, flowers and amber", "bottle in a beam of golden light",
            "bottle on a marble table in a study", "golden bottle with black spade",
            "bottle with its black box", "where to apply perfume: chest, neck, wrists and more"],
      order=[4, 5, 1, 2, 3, 6]),
 dict(id="15415432970627", name="Opal", who="Unisex", fam="floral", price="109.99", r=451,
      handle="game-of-spades-opal-eau-de-parfum-100ml",
      title="Game of Spades Opal Unisex Eau de Parfum 100ml",
      notes=("bergamot, lemon, pear and raspberry on top, a heart of rose, jasmine and peony, "
             "and a base of amber, sandalwood, cedar and musk"),
      look="the white Game of Spades bottle with a crystal-set gold spade and gold cap",
      sim=["sapphire", "emerald", "ruby", "royale"],
      alts=["white bottle on white feathers", "bottle with roses, peony, citrus and amber",
            "bottle on a pedestal with gold satin", "bottle with its white box",
            "where to apply perfume: chest, neck, wrists and more"],
      order=[1, 4, 2, 3, 5]),
]

out = []
for p in P:
    short = f"Game of Spades {p['name']}"
    who_txt = "for men" if p["who"] == "Men" else "for men and women"
    gender_coll = "perfume-for-men" if p["who"] == "Men" else "unisex-perfume"
    notes_html = (f"<p>The scent has {p['notes']}.</p>" if p["notes"] else
                  "<p>Ask us for the scent notes before you buy: message us on WhatsApp or Instagram and we will help.</p>")
    html = (f"<p>{short} is an eau de parfum {who_txt} from Jo Milano's Game of Spades collection, in {p['look']}.</p>"
            + notes_html +
            "<h3>Details</h3><ul><li>Eau de parfum, 100ml spray</li>"
            f"<li>{'Made for men' if p['who'] == 'Men' else 'Unisex: for men and women'}</li>"
            "<li>Brand: Jo Milano (Game of Spades collection)</li>"
            "<li>100% authentic, dispatched from the UK</li></ul>"
            f"<h3>How to use</h3><p>{HOW}</p>")
    fam_word = {"woody": "woody", "amber": "warm amber", "floral": "floral"}.get(p["fam"])
    seo_t = f"{short} {'' if p['who'] == 'Men' else 'Unisex '}Eau de Parfum 100ml{' for Men' if p['who'] == 'Men' else ''} | Swansura"
    if len(seo_t) > 60:
        seo_t = f"{short} EDP 100ml{' for Men' if p['who'] == 'Men' else ''} | Swansura"
    seo_d = (f"Buy {short} Eau de Parfum 100ml, a {fam_word + ' ' if fam_word else ''}"
             f"{'men' + chr(39) + 's' if p['who'] == 'Men' else 'unisex'} perfume by Jo Milano, for £{p['price']}. "
             "100% authentic, free UK delivery over £40.")
    h1 = f"{short} {'Eau de Parfum for Men' if p['who'] == 'Men' else 'Unisex Eau de Parfum'}"
    fam_answer = {"woody": "A woody fragrance with citrus, spice and amber.",
                  "amber": "A warm amber fragrance with citrus, fruit and vanilla.",
                  "floral": "A floral fragrance with rose, jasmine and peony over amber and woods."}
    sw = {"t": "For him" if p["who"] == "Men" else "Unisex", "s": [], "c": [], "k": False, "r": p["r"],
          "f": p["fam"], "w": p["who"], "n": None,
          "a": [fam_answer[p["fam"]] if p["fam"] else "Message us for the scent notes of this perfume."]}
    chips = ([FAM[p["fam"]]] if p["fam"] else []) + ["For men" if p["who"] == "Men" else "Unisex", "Eau de Parfum"]
    kw = ([["Perfume for men", "/collections/perfume-for-men"]] if p["who"] == "Men" else [["Unisex perfume", "/collections/unisex-perfume"]]) + \
         [["Niche perfume", "/collections/niche-perfume"], ["Luxury gifts over £50", "/collections/gifts-over-50"]]
    pdp = {"cat": "fragrance", "ben": "", "more": False, "chips": chips, "how": [], "pair": PAIR,
           "sim": [GOS[s] for s in p["sim"]], "kw": kw}
    colls = ["fragrance", "jo-milano", "price-50-9999", gender_coll, "niche-perfume", "gifts-over-50"]
    if p["fam"]:
        colls.append("scent-" + p["fam"])
    if p["name"] in ("Diamond", "Opal"):
        colls.append("diamond-collection")
    assert len(seo_t) <= 60, seo_t
    assert len(seo_d) <= 160, (len(seo_d), seo_d)
    mf = lambda k, t, v: {"namespace": "custom", "key": k, "type": t, "value": v}
    out.append({"id": "gid://shopify/Product/" + p["id"], "title": p["title"],
                "collections": colls, "collection_ids": ["gid://shopify/Collection/" + COLL[c] for c in colls],
                "alts": [f"{short} – {a}" for a in p["alts"]], "order": p["order"],
                "input": {"id": "gid://shopify/Product/" + p["id"], "title": p["title"], "handle": p["handle"],
                          "vendor": "Jo Milano", "descriptionHtml": html,
                          "seo": {"title": seo_t, "description": seo_d}, "tags": ["Fragrance", "Game of Spades"],
                          "status": "ACTIVE"},
                "metafields": [mf("h1", "single_line_text_field", h1), mf("sw", "json", json.dumps(sw, ensure_ascii=False)),
                               mf("pdp", "json", json.dumps(pdp, ensure_ascii=False))]})
    print(p["title"], "|", seo_t, len(seo_t), "|", len(seo_d), "|", h1)
json.dump(out, open(ROOT / "docs/seo/gos_drafts_2026-10-31.json", "w"), ensure_ascii=False, indent=1)

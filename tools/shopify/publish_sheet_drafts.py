"""Publish the 19 fragrance drafts that are in the client's 2 Nov 2026 sheet (user: "those 674 and 159 should be in the
LIVE as well, even without inventory"; chose 'All live now, sold out').

13 Maison de Milan, 2 Chris Adams, Game of Spades Win + Rouge Extrait (Jo Milano), Rihanah Ajwaa Oud.
Prices = client sheet (same as the drafts). Titles cleaned ('… – Long Lasting Luxury Fragrance' dropped), vendor =
real brand (was 'Generic'), factual description from the notes in the client's own draft text (no longevity or
other claims), SEO in the 'Final SEO' format (family/gender corrected from the notes), custom.h1/sw/pdp, collections.
Drafts were never live, so handles are shortened without redirects. Photos: the drafts' own (1–8 each).
Writes docs/seo/sheet_drafts_publish_2026-11-02.json. Before-state: docs/backups/sheet_drafts_before_2026-11-02.json.
"""
import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
PAIR = ["deyga-chocolate-body-butter-100g", "somali-frankincense-sleep-pillow-spray-overactive-mind-anatome"]
HOW = ("Spray from 15–20 cm onto pulse points such as the neck, inner wrists and inner elbows. "
       "Don't rub your wrists together. Patch test before first use if your skin is sensitive.")

# id, brand, name, who (Men/Women/Unisex), type, family, price, notes sentence (None = ask us)
P = [
 ("15415436837251", "Chris Adams", "CA DX 77 Pour Homme", "Men", "Eau de Parfum", "woody", "14.50",
  "Top notes of citrus, bergamot, petitgrain, melon, apple, ginger and galbanum; a heart of vetiver, thyme, mint, lavender, "
  "geranium, nutmeg and clove; and a base of vetiver, sandalwood, cinnamon, amber and musk. Fragrance family: aromatic woods."),
 ("15415434674563", "Chris Adams", "Black Shadow Pour Homme", "Men", "Eau de Toilette", "woody", "11.94",
  "A chypre fragrance for men."),
 ("15415434805635", "Game of Spades", "Win", "Unisex", "Eau de Parfum", "floral", "79.99",
  "Top notes of litchi, cassis and mandarin orange, a floral heart, and a base of vanilla and musk."),
 ("15415434969475", "Maison de Milan", "Amalfi Bleu", "Men", "Eau de Parfum", "fresh", "17.99",
  "Mint and melon top notes, a heart of ginger, and a base of cedar and sandalwood."),
 ("15415435100547", "Maison de Milan", "Bliss Rouge", "Women", "Eau de Parfum", "amber", "17.99",
  "Top notes of blood orange with saffron and almond, a heart of cedar and ambergris, and a musk base."),
 ("15415437197699", "Maison de Milan", "Brave Lad", "Unisex", "Eau de Parfum", "amber", "17.99",
  "A blend of juicy fruits, florals and amber."),
 ("15415435166083", "Maison de Milan", "Delight Pour Femme", "Women", "Eau de Parfum", "floral", "17.99",
  "Citrus and peach with peony and freesia, finishing on sandalwood and musk."),
 ("15415433658755", "Maison de Milan", "Elegance Pour Femme", "Women", "Eau de Parfum", "floral", "17.99",
  "Bright citrus and rose over creamy sandalwood and soft musk."),
 ("15415435133315", "Maison de Milan", "Gossip Pour Femme", "Women", "Eau de Parfum", "floral", "17.99",
  "Citrus and pear, then violet and jasmine, ending on amber and musk."),
 ("15415437918595", "Maison de Milan", "Invincible", "Women", "Eau de Parfum", "floral", "17.99",
  "A blend of floral and woody notes."),
 ("15415437328771", "Maison de Milan", "L'Homme Suave", "Men", "Eau de Parfum", "woody", "17.99",
  "Bergamot with lavender and pepper over a base of cedarwood, patchouli and labdanum."),
 ("15415433757059", "Maison de Milan", "M", "Unisex", "Eau de Parfum", "floral", "17.99",
  "Bergamot and green apple, a heart of jasmine and iris, and a base of amber and sandalwood."),
 ("15415436444035", "Maison de Milan", "Milano Girl Black", "Women", "Eau de Parfum", "floral", "17.99",
  "Floral and woody notes."),
 ("15415433593219", "Maison de Milan", "Milano Girl Red", "Women", "Eau de Parfum", "floral", "19.99",
  "Floral, fruity and amber notes."),
 ("15415434412419", "Maison de Milan", "Milano Girl White", "Women", "Eau de Parfum", "floral", "19.99",
  "White florals and musk with warm undertones."),
 ("15415433691523", "Maison de Milan", "Opulent Gold", "Unisex", "Eau de Parfum", "woody", "17.99",
  "Floral top notes over a woody base."),
 ("15415434183043", "Maison de Milan", "Valiant Pour Homme", "Unisex", "Eau de Parfum", "woody", "17.99",
  "Citrus and spice top notes over warm woods and leather."),
 ("15415431889283", "Game of Spades", "Rouge", "Unisex", "Extrait de Parfum", "woody", "85.99", None),
 ("15415436345731", "Rihanah", "Ajwaa Oud", "Unisex", "Eau de Parfum", "oud", "17.99", None),
]
VENDOR = {"Game of Spades": "Jo Milano"}
BRAND_COLL = {"Maison de Milan": "maison-de-milan", "Chris Adams": "chris-adams", "Rihanah": "rihanah", "Game of Spades": "jo-milano"}
GOS_SIM = ["game-of-spades-king-eau-de-parfum-100ml", "game-of-spades-jackpot-eau-de-parfum-100ml",
           "game-of-spades-opal-eau-de-parfum-100ml", "game-of-spades-diamond-eau-de-parfum-100ml"]
FAMW = {"woody": "woody", "amber": "warm amber", "floral": "floral", "fresh": "fresh", "oud": "oud"}


def handleize(s):
    s = s.lower().replace("&", " ").replace("'", "")
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s)).strip("-")


def price_band(p):
    return "price-0-15" if p < 15 else "price-15-25" if p < 25 else "price-25-50" if p < 50 else "price-50-9999"


out, by_brand = [], {}
for pid, brand, name, who, typ, fam, price, notes in P:
    short = f"{brand} {name}"
    title = f"{short} {'Unisex ' if who == 'Unisex' else ''}{typ} 100ml{' for Men' if who == 'Men' else ' for Women' if who == 'Women' else ''}"
    handle = handleize(f"{short} {typ} 100ml")
    by_brand.setdefault(brand, []).append(handle)
    h1 = f"{short} {'Unisex ' if who == 'Unisex' else ''}{typ}{' for Men' if who == 'Men' else ' for Women' if who == 'Women' else ''}"
    whotxt = {"Men": "for men", "Women": "for women", "Unisex": "for men and women"}[who]
    by = f" from Jo Milano's Game of Spades collection" if brand == "Game of Spades" else ""
    html = (f"<p>{short} is an {typ.lower()} {whotxt}{by}, in a 100ml spray.</p>" if typ[0] in "EA" else
            f"<p>{short} is a {typ.lower()} {whotxt}{by}, in a 100ml spray.</p>")
    html = html.replace("is an extrait", "is an extrait")
    html += (f"<h3>Scent notes</h3><p>{notes}</p>" if notes else
             "<p>Ask us for the scent notes before you buy: message us on WhatsApp or Instagram and we will help.</p>")
    html += (f"<h3>Details</h3><ul><li>{typ}, 100ml spray</li>"
             f"<li>{'Made for men' if who == 'Men' else 'Made for women' if who == 'Women' else 'Unisex: for men and women'}</li>"
             f"<li>Brand: {VENDOR.get(brand, brand)}{' (Game of Spades collection)' if brand == 'Game of Spades' else ''}</li>"
             "<li>100% authentic, dispatched from the UK</li></ul>"
             f"<h3>How to use</h3><p>{HOW}</p>")
    g_word = {"Men": "men's", "Women": "women's", "Unisex": "unisex"}[who]
    abbr = {"Eau de Parfum": "EDP", "Eau de Toilette": "EDT", "Extrait de Parfum": "Extrait"}[typ]
    seo_t = f"{short} {typ} 100ml | Swansura UK"
    if len(seo_t) > 60:
        seo_t = f"{short} {abbr} 100ml | Swansura UK"
    if len(seo_t) > 60:
        seo_t = f"{short} 100ml | Swansura UK"
    art = "An" if FAMW[fam][0] in "aeiou" else "A"
    seo_d = (f"Buy {short} {typ} 100ml for £{price} at Swansura UK. {art} {FAMW[fam]} {g_word} {typ.lower()}. "
             "100% authentic, fast UK delivery, free over £40.")
    if len(seo_d) > 160:
        seo_d = seo_d.replace("fast UK delivery, free over £40", "free UK delivery over £40")
    if len(seo_d) > 160:
        seo_d = seo_d.replace(f" {typ} 100ml for", f" {abbr} 100ml for")
    assert len(seo_t) <= 60 and len(seo_d) <= 160, (seo_t, len(seo_d), seo_d)
    gender_coll = {"Men": "perfume-for-men", "Women": "perfume-for-women", "Unisex": "unisex-perfume"}[who]
    colls = ["fragrance", BRAND_COLL[brand], price_band(float(price)), gender_coll, "scent-" + fam]
    if brand == "Game of Spades":
        colls += ["niche-perfume", "gifts-over-50"]
    if fam == "oud":
        colls += ["oud-perfume", "arabian-perfume"]
    sw = {"t": {"Men": "For him", "Women": "For her"}.get(who, "Unisex"), "s": [], "c": [], "k": False, "r": 800 + len(out),
          "f": fam, "w": who, "n": None,
          "a": [notes if notes and notes.startswith("A ") else
                f"{art} {FAMW[fam]} fragrance: {notes.split(';')[0].rstrip('.')}." if notes else
                "Message us for the scent notes of this perfume."]}
    chips = [{"oud": "Oud"}.get(fam, fam.capitalize()) + " family", {"Men": "For men", "Women": "For women"}.get(who, "Unisex"), typ]
    kw = [[{"Men": "Perfume for men", "Women": "Perfume for women"}.get(who, "Unisex perfume"), "/collections/" + gender_coll]]
    pdp = {"cat": "fragrance", "ben": "", "more": False, "chips": chips, "how": [], "pair": PAIR, "sim": [], "kw": kw}
    mf = lambda k, t, v: {"namespace": "custom", "key": k, "type": t, "value": v}
    out.append({"id": "gid://shopify/Product/" + pid, "brand": brand, "collections": colls, "pdp": pdp,
                "input": {"id": "gid://shopify/Product/" + pid, "title": title, "handle": handle,
                          "vendor": VENDOR.get(brand, brand), "productType": "Fragrance", "descriptionHtml": html,
                          "seo": {"title": seo_t, "description": seo_d},
                          "tags": ["Fragrance"] + (["Game of Spades"] if brand == "Game of Spades" else []),
                          "status": "ACTIVE"},
                "metafields": [mf("h1", "single_line_text_field", h1), mf("sw", "json", json.dumps(sw, ensure_ascii=False))]})
for o in out:
    sim = GOS_SIM if o["brand"] == "Game of Spades" else [h for h in by_brand[o["brand"]] if h != o["input"]["handle"]][:4]
    o["pdp"]["sim"] = sim
    o["metafields"].append({"namespace": "custom", "key": "pdp", "type": "json", "value": json.dumps(o.pop("pdp"), ensure_ascii=False)})
    print(o["input"]["title"], "|", o["input"]["seo"]["title"], "|", len(o["input"]["seo"]["description"]))
json.dump(out, open(ROOT / "docs/seo/sheet_drafts_publish_2026-11-02.json", "w"), ensure_ascii=False, indent=1)

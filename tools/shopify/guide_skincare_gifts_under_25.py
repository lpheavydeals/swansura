"""Journal guide 'Skincare gifts under £25: Vilvah and Deyga kits, lip sets and soaps'
(user, 28 Nov 2026: 'Go ahead with the two guides', after gift sets under £30 / women's perfume under £50).

Every product below was in stock at £25 or less on the storefront on 28 Nov 2026. Facts = each product's
own description ('What's in the kit' lists, ingredients). Claim-named kits (Lip Lightening, Rose & Mulethi
'Skin Brightening' pack) left out; Deyga Natural Hair Care Kit left out (contents unknown).
NO PRICES in the text (only the £25 band and £40 delivery).

Usage: python3 tools/shopify/guide_skincare_gifts_under_25.py <storefront products dump dir>
Output: docs/seo/guide_skincare_gifts_under_25_2026-11-28.jsonl
"""
import glob
import json
import sys

from journal_lib import build

A = {
    "title": "Skincare gifts under £25: Vilvah and Deyga kits, lip sets and soaps",
    "handle": "skincare-gifts-under-25",
    "tag": "Gift guide",
    "summary": "Natural skincare gifts for £25 or less: Vilvah and Deyga lip sets, hair and face kits, solid deodorants, goat milk soaps and bath bars, with what is in each one.",
    "mt": "Skincare Gifts Under £25: Vilvah & Deyga Kits | Swansura",
    "md": "Natural skincare gifts under £25 in the UK: Vilvah and Deyga lip sets, hair and face kits, solid deodorants, goat milk soaps and bath bars, with contents.",
    "pick": {
        "lipnour": "vilvah-lip-nourishing-kit-grapefruit-lip-balm-lip-scrub-exfoliates-hydrates-softens-natural-tint-shea-butter-graperfruit-avocado-oil",
        "softlip": "deyga-soft-lip-combo",
        "tinted": "vilvah-tinted-lip-balm-kit",
        "anna": "vilvah-x-annapoorna-gift-box",
        "lipspf": "vilvah-milk-lip-balm-spf-30-pa-natural-uv-protection-hydrating-lip-care-for-all-skin-types",
        "glow": "deyga-healthy-glow-kit",
        "sun": "vilvah-sun-protection-kit-spf-50-face-sunscreen-spf-30-lip-balm-lightweight-hydrating-sun-care-soy-milk-nourishing-oils",
        "mask": "vilvah-wild-rose-face-mask-100ml-natural-brightening-clay-mask-for-even-skin-tone-deep-hydration",
        "hair": "daily-use-healthy-hair-combo-deygas-natural-hair-care-set-with-shampoo-conditioner-nourishing-and-strengthening-routine",
        "comb": "neem-wood-comb-set-of-3-fine-tooth-wide-tooth-handle-comb-natural-wooden-combs-for-hair-scalp-health-value-saver-pack",
        "deo": "vilvah-deo-shot-kit-pocket-size-solid-deodorant-bundle-rose-vanilla-lavender-sage-natural-butters-essential-oils-for-day-to-night-freshness",
        "rosesoap": "classic-rose-goat-milk-soap-bar-125g",
        "soap": "classic-goatmilk-soap-bar-115g",
        "saffron": "deyga-shea-saffron-bath-bar-100g",
        "pinkclay": "deyga-rose-pink-clay-bath-bar-100g",
        "foot": "foot-butter-40-g-deygas-deep-moisture-butter-for-dry-cracked-heels-rough-feet",
    },
    "titles": {},
    "shop": ["lipnour", "softlip", "anna", "glow", "hair", "deo", "rosesoap", "sun"],
    "body": """<p><strong>A good skincare gift does not need a big budget.</strong> Everything below was £25 or less at Swansura at the time of writing, from Vilvah and Deyga, the two natural skincare brands we are official UK partners of. Most are small ready-made kits, so the gift is already put together; we list what is in each one so you can match it to the person.</p>
<h2>Lip care sets</h2>
<p>The easiest skincare gift: everyone uses lip balm, especially in winter.</p>
<ul>
<li>[[lipnour|Vilvah Lip Nourishing Kit]]: a sugar lip scrub and a tinted grapefruit lip balm, both made with organic shea butter, avocado oil and almond oil.</li>
<li>[[softlip|Deyga Soft Lip Combo]]: a mint lip scrub and the Classic Beetroot Lip Balm, made with plant oils, shea butter and beetroot extract.</li>
<li>[[tinted|Vilvah Tinted Lip Balm Kit]]: two tinted lip balms for a hint of everyday colour.</li>
<li>[[anna|Vilvah x Annapoorna Gift Box]]: Filter Kaapi and Rose Milk lip balms with Annapoorna coffee beans, a limited-edition box for coffee lovers.</li>
<li>[[lipspf|Vilvah Milk Lip Balm SPF 30 PA+++]]: a single balm with mineral filters and shea, soy and kokum butters, for winter walks and ski trips.</li>
</ul>
<p>Our <a href="/blogs/journal/lip-balm-guide">lip balm guide</a> compares SPF, tinted and natural balms, and our <a href="/blogs/journal/how-to-use-lip-scrub">lip scrub guide</a> explains how to use the scrubs.</p>
<h2>Face kits</h2>
<ul>
<li>[[glow|Deyga Healthy Glow Kit]]: a Rose &amp; Mulethi face pack powder (rose petals, liquorice root and oatmeal) and a Pure Rose Water Toner, a simple two-step rose routine.</li>
<li>[[sun|Vilvah Sun Protection Kit]]: an SPF 50 face sunscreen and the Milk Lip Balm SPF 30 PA+++, so face and lips are covered in one step. A thoughtful gift for someone who walks, cycles or skis.</li>
<li>[[mask|Vilvah Wild Rose Face Mask]]: three ingredients, aloe vera, French pink clay and rose hydrosol, for a 15-minute weekend mask.</li>
</ul>
<p>Our <a href="/blogs/journal/face-mask-guide">face mask guide</a> and <a href="/blogs/journal/toner-for-dry-skin">toner guide</a> explain how each step fits a routine.</p>
<h2>Hair gifts</h2>
<ul>
<li>[[hair|Deyga Daily Use Healthy Hair Kit]]: Rice Water Shampoo and Soy Milk Conditioner, made with coconut-derived cleansers, soybean extract, argan oil and provitamin B5. The smaller 50ml set fits a stocking.</li>
<li>[[comb|Vilvah Neem Wood Comb Set of 3]]: a fine-tooth comb, a wide-tooth comb and a wide-tooth handle comb, all in neem wood.</li>
</ul>
<p>More in our <a href="/blogs/journal/natural-shampoo-guide">natural shampoo guide</a>.</p>
<h2>Body and bath</h2>
<ul>
<li>[[deo|Vilvah Deo Shot Kit]]: two pocket-size solid deodorants, Rose &amp; Vanilla and Lavender &amp; Sage, made with shea butter, coconut oil, jojoba oil and cocoa butter.</li>
<li>[[rosesoap|Vilvah Classic Rose Goat Milk Soap]] and [[soap|Vilvah Classic Goat Milk Soap]]: handmade bars, one with rose petals and pink clay, one with lavender essential oil. Our <a href="/blogs/journal/goat-milk-soap-guide">goat milk soap guide</a> explains how they are made.</li>
<li>[[saffron|Deyga Shea Saffron Bath Bar]] and [[pinkclay|Deyga Rose Pink Clay Bath Bar]]: made with raw shea butter and coconut and olive oils.</li>
<li>[[foot|Deyga Foot Butter]]: coconut oil, olive oil and beeswax with a soft vanilla scent. More in our <a href="/blogs/journal/foot-cream-guide">foot cream guide</a>.</li>
</ul>
<h2>How to choose</h2>
<ul>
<li><strong>For anyone:</strong> a lip set, such as the Vilvah Lip Nourishing Kit or Deyga Soft Lip Combo.</li>
<li><strong>For someone who loves a pamper night:</strong> the Deyga Healthy Glow Kit or Vilvah Wild Rose Face Mask.</li>
<li><strong>For a stocking:</strong> a goat milk soap, a single lip balm or the 50ml hair kit.</li>
<li><strong>For a coffee lover:</strong> the Vilvah x Annapoorna Gift Box.</li>
</ul>
<h2>Good to know</h2>
<p>Patch test new skincare before first use, especially products with essential oils. Every product is 100% authentic and ships from the UK, and UK delivery is free on orders over £40, so two or three small gifts in one order usually ship free. For bigger kits, see our <a href="/blogs/journal/skincare-gift-sets-guide">skincare gift sets guide</a>; for perfume, our <a href="/blogs/journal/perfume-gift-sets-under-30">perfume gift sets under £30 guide</a>. Browse every <a href="/collections/skincare-gift-sets">skincare gift set</a> and <a href="/collections/gifts-under-25">gift under £25</a>.</p>""",
    "faq": [
        ["What is a good skincare gift under £25?",
         "A lip set is the safest choice, such as the Vilvah Lip Nourishing Kit or the Deyga Soft Lip Combo. For a pamper night, the Deyga Healthy Glow Kit pairs a rose face pack with rose water toner."],
        ["What is in the Vilvah x Annapoorna Gift Box?",
         "A Filter Kaapi lip balm and a Rose Milk lip balm from Vilvah, with Annapoorna coffee beans, in a limited-edition box."],
        ["Are these skincare gifts vegan?",
         "Not all of them. The goat milk soaps contain goat milk, and several lip balms and the deodorants contain beeswax. Each product page lists the full ingredients."],
        ["Are Vilvah and Deyga products authentic?",
         "Yes. Swansura is an official UK partner of Vilvah and Deyga, and every product ships from the UK."],
    ],
}

if __name__ == "__main__":
    ALL = {}
    for f in glob.glob(sys.argv[1] + "/*.json"):
        d = json.load(open(f))
        if isinstance(d, dict) and "products" in d:
            for p in d["products"]:
                ALL[p["handle"]] = p
    build(A, ALL, "guide_skincare_gifts_under_25_2026-11-28.jsonl")

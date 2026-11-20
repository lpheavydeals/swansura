"""Journal guide 'Skincare gift sets for Christmas: Vilvah and Deyga kits, and what is in each'
(user, 19-20 Nov 2026: 'Write and Publish All').

Semrush UK: skincare gift set 3,600, hair care gift set 880. All picks in stock with photos on 20 Nov
(allp_map_1120.json, skincare-gift-sets collection). Kit contents from each kit's stored custom.inci component names and
description (Admin read 20 Nov). Claim-named kits (Tan Protection, Oil Control, Brightening, Face Lift, Pore Minimising,
Better Ageing, Night Repair, Lip Lightening, De-tan) left out. No order-by dates (client has not confirmed them).
Vilvah/Deyga first (best margin); one Highborn London set as the premium pick.

Usage: python3 tools/shopify/guide_skincare_gift_sets.py <allp_map.json>
Output: docs/seo/guide_skincare_gift_sets_2026-11-20.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Skincare gift sets for Christmas: Vilvah and Deyga kits, and what is in each",
    "handle": "skincare-gift-sets-guide",
    "tag": "Gift guide",
    "summary": "Skincare and hair care gift sets from Vilvah, Deyga and Highborn London, sorted by who they suit, with exactly what is in each kit and the prices.",
    "mt": "Skincare Gift Sets UK: Vilvah & Deyga Kits | Swansura",
    "md": "Skincare and hair care gift sets for Christmas: Vilvah and Deyga kits for face, lips, body and hair, what is in each one and gifts under £20.",
    "pick": {
        "hydration": "vilvah-skin-hydration-kit-milk-face-toner-milk-drops-brightening-serum-hydrate-minimize-pores-brighten-skin-naturally",
        "everyday": "vilvah-everyday-care-milk-kit",
        "milkface": "vilvah-milk-face-kit-milk-mud-mask-milk-drops-brightening-serum-de-tans-brightens-clears-skin-oatmilk-saffron-rice-milk-extracts",
        "glow": "deyga-healthy-glow-kit",
        "bodykit": "vilvah-milk-body-kit-goat-milk-body-wash-milk-body-lotion-deep-hydration-skin-softening-nourishment-oat-milk-olive-squalane-coconut-oil-vanilla-scent",
        "footkit": "vilvah-foot-cream-body-lotion-kit",
        "deo": "vilvah-deo-shot-kit-pocket-size-solid-deodorant-bundle-rose-vanilla-lavender-sage-natural-butters-essential-oils-for-day-to-night-freshness",
        "lipdeyga": "nourished-lip-care-kit-deygas-strawberry-lip-scrub-beetroot-lip-balm-set-for-soft-smooth-hydrated-lips",
        "lipstick": "deygas-beetroot-lip-balm-stick-strawberry-lip-scrub-combo-natural-tinted-lip-care-duo-for-soft-smooth-lips",
        "tinted": "vilvah-tinted-lip-balm-kit",
        "annapoorna": "vilvah-x-annapoorna-gift-box",
        "hairvilvah": "vilvah-bestseller-hair-kit-goat-milk-shampoo-200ml-cream-conditioner-200ml-nourishing-frizz-control-sulfate-free-hair-care-set",
        "hairmask": "vilvah-goat-milk-hair-kit",
        "hairdeyga": "daily-use-healthy-hair-combo-deygas-natural-hair-care-set-with-shampoo-conditioner-nourishing-and-strengthening-routine",
        "highborn": "ultimate-day-night-moisture-set",
    },
    "titles": {},
    "shop": ["bodykit", "hydration", "everyday", "glow", "hairvilvah", "lipdeyga", "tinted", "footkit"],
    "body": """<p>A skincare gift set takes the guesswork out of buying for someone else: the products are chosen to be used together, and the box is ready to give. Here are the <strong>skincare gift sets</strong> and hair care sets we stock from Vilvah and Deyga, sorted by who they suit, with exactly what is inside each one. Swansura is an official UK partner of both brands, and every kit ships from the UK.</p>
<h2>Face care gift sets</h2>
<ul>
<li>[[hydration|Vilvah Skin Hydration Kit]] ({{hydration}}): Milk Face Toner (earth marine water, glycerine, rice milk extract and glycolic acid) and Milk Drops Serum (aloe vera juice, betaine and hyaluronic acid). A simple two-step routine for after cleansing.</li>
<li>[[everyday|Vilvah Everyday Care Milk Kit]] ({{everyday}}): the same toner and serum plus Melt-in-Milk Sunscreen SPF 50, so it covers a full morning routine.</li>
<li>[[milkface|Vilvah Milk Face Kit]] ({{milkface}}): Milk Mud Mask (kaolin, oat milk, saffron and liquorice root extracts) and Milk Drops Serum. A weekly mask and a daily serum.</li>
<li>[[glow|Deyga Healthy Glow Kit]] ({{glow}}): a Rose &amp; Mulethi face pack (dried rose petals, mulethi root and oatmeal, mixed with water or toner) and Rose Water Toner. The most affordable face set, and a good one for someone who likes traditional ingredients.</li>
</ul>
<p>The Milk Face Toner contains glycolic acid, so it suits someone who already uses a toner; patch test first and wear SPF in the day. For more on the serum, see our <a href="/blogs/journal/vilvah-milk-drops-serum">Vilvah Milk Drops guide</a>.</p>
<h2>Body care gift sets</h2>
<ul>
<li>[[bodykit|Vilvah Milk Body Kit]] ({{bodykit}}): Goat Milk Body Wash (goat milk, coconut-derived cleansers, glycerine and acai oil, scented with vanilla and white lily) and Milk Body Lotion (oat milk, ceramide NP, olive squalane, jojoba and coconut oils). A complete shower-to-moisturiser gift.</li>
<li>[[footkit|Vilvah Foot Cream &amp; Body Lotion Kit]] ({{footkit}}): Foot Care Cream 100ml (shea, mango and avocado butters with argan and kalonji oils) and Milk Body Lotion 250ml. Ideal for someone with dry skin in winter.</li>
<li>[[deo|Vilvah Deo Shot Kit]] ({{deo}}): two pocket-size solid deodorant balms, Rose &amp; Vanilla and Lavender &amp; Sage, with kaolin clay and vitamin E.</li>
</ul>
<h2>Lip care gift sets</h2>
<ul>
<li>[[lipdeyga|Deyga Nourished Lip Care Kit]] ({{lipdeyga}}): Strawberry Lip Scrub (sugar in plant oils and shea butter) and the classic Beetroot Lip Balm pot.</li>
<li>[[lipstick|Deyga Beetroot Lip Balm Stick &amp; Strawberry Lip Scrub combo]] ({{lipstick}}): the same scrub with the tinted beetroot stick.</li>
<li>[[tinted|Vilvah Tinted Lip Balm Kit]] ({{tinted}}): the Cream Bun and Mango Milkshake lip balms, each with a hint of colour.</li>
<li>[[annapoorna|Vilvah x Annapoorna Gift Box]] ({{annapoorna}}): Filter Kaapi and Rose Milk lip balms with Annapoorna coffee beans: two Coimbatore names in one box.</li>
</ul>
<p>Our <a href="/blogs/journal/lip-balm-guide">lip balm guide</a> and <a href="/blogs/journal/deyga-beetroot-lip-balm-stick-or-pot">beetroot lip balm guide</a> compare them in more detail.</p>
<h2>Hair care gift sets</h2>
<ul>
<li>[[hairvilvah|Vilvah Bestseller Hair Kit]] ({{hairvilvah}}): Goat Milk Shampoo (goat milk, jasmine flower water and hydrolysed pea protein) and Cream Conditioner (tucuma butter, broccoli seed oil and aloe vera).</li>
<li>[[hairmask|Vilvah Goat Milk Hair Kit]] ({{hairmask}}): Goat Milk Shampoo with the Goat Milk Hair Mask, for a weekly treat.</li>
<li>[[hairdeyga|Deyga Daily Use Healthy Hair Combo]] ({{hairdeyga}}): Rice Water Shampoo and Soy Milk Conditioner (soybean extract, argan oil, panthenol and vitamin E). The best value hair set we stock.</li>
</ul>
<p>See our <a href="/blogs/journal/natural-shampoo-guide">natural shampoo guide</a> for how they compare.</p>
<h2>Skincare gifts under £20</h2>
<p>For stockings and Secret Santa: the Deyga hair combo ({{hairdeyga}}), Vilvah Tinted Lip Balm Kit ({{tinted}}), Deo Shot Kit ({{deo}}) and Deyga Healthy Glow Kit ({{glow}}). The Annapoorna box is just over, at {{annapoorna}}. Our <a href="/blogs/journal/stocking-fillers-for-her-under-25">stocking fillers guide</a> has more ideas.</p>
<h2>A premium pick</h2>
<p>The [[highborn|Highborn London Ultimate Day &amp; Night Moisture Set]] ({{highborn}}) holds the Imperial Moisturiser and Night Elixir, both in 50ml jars.</p>
<h2>How to choose</h2>
<ul>
<li><strong>Not sure of their skin type?</strong> Body, lip and hair sets are the safest choice.</li>
<li><strong>Check the ingredients:</strong> the Deyga beetroot lip balms contain almond oil and beeswax, and the Vilvah goat milk products are not vegan. Every product page has the full ingredient list.</li>
<li><strong>Spend £40 or more</strong> for free UK delivery: the Deyga Nourished Lip Care Kit and the Vilvah Tinted Lip Balm Kit together come to just over.</li>
<li><strong>Delivery before Christmas:</strong> see our <a href="/pages/shipping">delivery page</a> for dispatch times and rates.</li>
</ul>
<p>Shop every <a href="/collections/skincare-gift-sets">skincare gift set</a>, or browse <a href="/collections/vilvah">Vilvah</a> and <a href="/collections/deyga">Deyga</a>. Buying perfume too? See our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a>.</p>""",
    "faq": [
        ["What is in the Vilvah Milk Body Kit?",
         "Goat Milk Body Wash (goat milk, coconut-derived cleansers, glycerine and acai oil) and Milk Body Lotion (oat milk, ceramide NP, olive squalane, jojoba oil and coconut oil)."],
        ["Which skincare gift set is best if I do not know their skin type?",
         "A body, lip or hair set is the safest choice, for example the Vilvah Milk Body Kit, the Deyga Nourished Lip Care Kit or the Vilvah Bestseller Hair Kit. Face sets suit someone whose routine you already know."],
        ["Do you have skincare gift sets under £20?",
         "Yes: the Deyga Daily Use Healthy Hair Combo, Vilvah Tinted Lip Balm Kit, Vilvah Deo Shot Kit and Deyga Healthy Glow Kit. The Vilvah x Annapoorna Gift Box is just over £20."],
        ["Are the Vilvah and Deyga gift sets vegan?",
         "Not all of them. The Vilvah goat milk products contain goat milk, and the Deyga beetroot lip balms contain beeswax and almond oil. Every product page lists the full ingredients, so check there before buying for someone vegan or with a nut allergy."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_skincare_gift_sets_2026-11-20.jsonl")

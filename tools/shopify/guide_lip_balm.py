"""Journal guide 'Lip balm for dry lips: SPF, tinted or natural?' (user, 15 Nov 2026: 'Write the next 2 Journal guides').

Semrush UK: spf lip balm 4,400 (KD 30), tinted lip balm 2,900 (KD 21), natural lip balm 1,300 (KD 10), lip butter 1,300
(KD 18), lip balm for dry lips 1,000 (KD 41). The existing how-to-use-lip-scrub guide targets lip scrub and only touches
balms; this guide is about choosing a balm and links back to it. 11 balms in stock on 15 Nov (Vilvah Cream Bun sold out:
not used). Facts = stored custom.inci + the descriptions rewritten 8 Nov (Admin read 15 Nov 2026). Tint colours for the
new Vilvah Rose Milk / Filter Kaapi / Mango Shake balms come from their own descriptions.
Left out (ASA / unprovable): lightening, pigmentation, 'even-looking lip tone', heals / repairs, protects against
chapping, 'vegan' (the Vilvah Lemon balm's old text says vegan but its INCI lists beeswax), 'chemical-free',
'100% natural'. SPF: only the labelled SPF 30 PA+++ rating and its mineral filters; reapply advice. Cracked or sore lips
that do not settle → pharmacist / GP. Prices are written into the text: re-run the generator and update the body if
prices change.

Usage: python3 tools/shopify/guide_lip_balm.py <allp_map.json>   (handle -> storefront product)
Output: docs/seo/guide_lip_balm_2026-11-15.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Lip balm for dry lips: SPF, tinted or natural, and how to choose",
    "handle": "lip-balm-guide",
    "tag": "Skin Studio",
    "summary": "SPF, tinted or natural lip balm: what is inside each type, which suits dry winter lips, and the balms we stock from Vilvah, Deyga and Highborn London.",
    "mt": "Lip Balm for Dry Lips: SPF, Tinted or Natural | Swansura",
    "md": "How to choose a lip balm for dry lips: SPF lip balm, tinted lip balm or a natural balm, with the ingredients in each and how to use them.",
    "pick": {
        "spf": "vilvah-milk-lip-balm-spf-30-pa-natural-uv-protection-hydrating-lip-care-for-all-skin-types",
        "beetpot": "deygas-beetroot-lip-balm-classic-10-g-100-natural-no-harsh-chemicals",
        "beetstick": "beetroot-lip-balm-stick-natural-tinted-balm-for-dry-lips-100-organic-ingredients-plant-based-cruelty-free-5-5-g",
        "rosemilk": "vilvah-rose-milk-lip-balm-10g",
        "mango": "vilvah-mango-shake-lip-balm-10g",
        "kaapi": "vilvah-filter-kaapi-lip-balm-10g",
        "grapefruit": "vilvah-grape-fruit-lip-balm-10g",
        "lemon": "vilvah-natural-lemon-lip-balm-10g-deep-hydration-pigmentation-reduction-with-shea-butter-avocado-oil-vitamin-e",
        "shea": "deyga-natural-vanilla-lip-balm-8g",
        "tintkit": "vilvah-tinted-lip-balm-kit",
        "lipbutter": "superior-lip-butter-15ml",
    },
    "titles": {},
    "shop": ["spf", "beetpot", "rosemilk", "mango", "kaapi", "shea", "beetstick", "grapefruit"],
    "body": """<p>Cold wind, central heating and hot drinks all leave lips dry in winter, and a good <strong>lip balm</strong> is the simplest fix. But balms are not all the same: some carry an SPF, some add a sheer tint, and some are just a few plant oils, butters and wax. Here is how to choose a <strong>lip balm for dry lips</strong>, what is inside each type and how to get the most from it.</p>
<h2>What a lip balm does</h2>
<p>Lips have a very thin outer layer and no oil glands of their own, so they dry out faster than the rest of the face. A balm puts a soft layer of oils, butters and wax over them, which keeps them feeling comfortable for longer. Most balms are built from the same few things: plant oils such as almond, avocado or jojoba; butters such as shea, mango or kokum; and a wax, often beeswax, that holds it all together.</p>
<h2>SPF lip balm</h2>
<p>Lips burn too, on bright winter days, ski trips and holidays as much as in summer. [[spf|Vilvah Milk Lip Balm SPF 30 PA+++]] ({{spf}}) uses mineral filters, zinc oxide and titanium dioxide, in a base of coconut oil, shea butter, soy butter, kokum butter and soy milk extract, with a soft vanilla note. Apply it before going outside, and reapply often, especially after eating, drinking or swimming. It works on its own or under lipstick.</p>
<h2>Tinted lip balm</h2>
<p>A <strong>tinted lip balm</strong> adds a sheer wash of colour as well as moisture, so it can stand in for a lipstick on busy days.</p>
<ul>
<li>[[beetpot|Deyga Beetroot Lip Balm Classic]] ({{beetpot}}, 10g pot) takes its rosy tint from beetroot extract, in almond, avocado and jojoba oils with shea butter and beeswax. The same balm comes as a twist-up [[beetstick|Beetroot Lip Balm Stick]] ({{beetstick}}, 5.5g) for your pocket.</li>
<li>[[rosemilk|Vilvah Rose Milk Lip Balm]] ({{rosemilk}}) gives a soft pink tint, with paneer rose extract, olive squalane, avocado butter, shea butter and vitamin E.</li>
<li>[[mango|Vilvah Mango Shake Lip Balm]] ({{mango}}) leaves a reddish-orange tint, with Alphonso mango pulp extract, mango butter, coconut milk and olive squalane.</li>
<li>[[kaapi|Vilvah Filter Kaapi Lip Balm]] ({{kaapi}}) has a subtle brown tint inspired by South Indian filter coffee, with coffee oil, coffee extract, shea butter, coconut milk and almond oil.</li>
<li>[[grapefruit|Vilvah Grape Fruit Lip Balm]] ({{grapefruit}}) has just six ingredients, with a little red iron oxide for a sheer tint and grapefruit essential oil for a zesty scent.</li>
</ul>
<p>Can't choose? The [[tintkit|Vilvah Tinted Lip Balm Kit]] ({{tintkit}}) puts two tinted balms in one box.</p>
<h2>Natural lip balm with a short ingredient list</h2>
<p>If you prefer a plain balm with nothing extra, look for a short list of oils, butter and wax.</p>
<ul>
<li>[[shea|Deyga Shea Butter Lip Balm]] ({{shea}}, 8g): almond oil, jojoba oil, beeswax, shea butter, vanilla extract and vitamin E, in a vanilla or shea version.</li>
<li>[[lemon|Vilvah Natural Lemon Lip Balm]] ({{lemon}}): organic shea butter, avocado oil, almond oil, unrefined beeswax and lemon essential oil.</li>
</ul>
<p>For a rich, jar-style <strong>lip butter</strong>, [[lipbutter|Highborn London Superior Lip Butter]] ({{lipbutter}}, 15ml, or a 50ml jar) is made with organic palm oil certified by the RSPO.</p>
<h2>How to use a lip balm</h2>
<ol>
<li><strong>Start with clean, dry lips.</strong></li>
<li><strong>Apply a thin layer</strong> with the stick or a clean fingertip, and reapply whenever lips feel dry.</li>
<li><strong>At night, use a thicker layer</strong> so it can sit on your lips while you sleep.</li>
<li><strong>Once or twice a week, use a lip scrub first.</strong> A balm spreads more evenly on smooth lips; our <a href="/blogs/journal/how-to-use-lip-scrub">lip scrub guide</a> explains how.</li>
<li><strong>In the sun, choose an SPF balm</strong> and reapply often.</li>
</ol>
<h2>Good to know</h2>
<ul>
<li><strong>Try not to lick your lips:</strong> saliva dries quickly and leaves them drier than before.</li>
<li><strong>Many balms contain beeswax.</strong> If you avoid it, check the Ingredients tab on each product before you buy.</li>
<li><strong>Patch test</strong> balms with essential oils, such as the lemon and grapefruit balms, before first use.</li>
<li><strong>Cracked or sore lips</strong> that do not settle after a week or two are worth showing to a pharmacist or your GP.</li>
<li><strong>Lip balms make easy stocking fillers:</strong> see our <a href="/blogs/journal/stocking-fillers-for-her-under-25">stocking fillers guide</a>.</li>
</ul>
<p>Shop every <a href="/collections/lip-balm">lip balm and lip care</a> product and our <a href="/collections/lip-scrub">lip scrubs</a>, all dispatched from the UK with free UK delivery over £40.</p>""",
    "faq": [
        ["What is the best lip balm for dry lips?",
         "One with plant butters and oils that sits on the lips for a while, such as shea butter, almond oil and beeswax. Apply a thin layer through the day and a thicker one at night, and use a gentle lip scrub once or twice a week so the balm spreads evenly."],
        ["Do I need an SPF lip balm in winter?",
         "Lips can burn on bright winter days, on ski trips and on holiday, so an SPF balm is worth carrying. The Vilvah Milk Lip Balm SPF 30 PA+++ uses zinc oxide and titanium dioxide. Reapply often, especially after eating or drinking."],
        ["What is the difference between a tinted lip balm and a lipstick?",
         "A tinted lip balm is a moisturising balm with a sheer wash of colour, so it feels like a balm and gives a soft, natural look. A lipstick gives stronger colour. Our tinted balms take their colour from beetroot extract, fruit extracts or mineral pigments."],
        ["How often should I apply lip balm?",
         "Whenever your lips feel dry, and always before bed. In cold or windy weather you may need it several times a day. If you are outdoors in the sun, use an SPF lip balm and reapply often."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_lip_balm_2026-11-15.jsonl")

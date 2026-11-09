"""Journal guide 'Goat milk soap: what it is, how to use it, and which bar to choose' (user, 9 Nov 2026: "Go ahead with
the goat milk soap guide"; plan item 5 of docs/seo/SEO_Orders_Audit_2026-11-09.md).

Target keywords (Semrush UK, competitor_research_2026-11-09.md): goat milk soap 880/mo (KD 15), goat milk shampoo 110
(KD 4), goat milk body lotion 110 (KD 5). Facts = stored custom.inci (Classic, Classic Rose, shampoo, hair mask) and the
products' own descriptions (Charcoal has no stored INCI: only goat milk + activated charcoal are named). Honest notes:
Cucumber, Curd & Mint Soap has no goat milk (curd); Vilvah Milk Body Lotion is oat milk (the goat milk is in the body
wash). Left out (ASA): eczema / psoriasis / acne, lactic acid 'exfoliates', pH claims, 'chemical-free', 'sulphate-free'
(the shampoo lists disodium laureth sulfosuccinate), hair repair / strengthening. No longevity numbers for the bars.
Prices are written into the text: re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_goat_milk_soap.py <allp.json>   (handle -> storefront product)
Output: docs/seo/guide_goat_milk_soap_2026-11-09.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Goat milk soap: what it is, how to use it, and which bar to choose",
    "handle": "goat-milk-soap-guide",
    "tag": "Skin Studio",
    "summary": "What goat milk soap is, how it is made, how to use a bar on face and body, and how the Vilvah goat milk soaps, shampoo and body care compare.",
    "mt": "Goat Milk Soap UK: How to Use It & Which Bar | Swansura",
    "md": "Goat milk soap explained: how it is made, how to use a bar on face and body, and the Vilvah goat milk soaps, shampoo and body wash, from the UK.",
    "pick": {
        "classic": "classic-goatmilk-soap-bar-115g",
        "rose": "classic-rose-goat-milk-soap-bar-125g",
        "charcoal": "charcoal-goatmilk-soap-bar-115g",
        "mint": "cucumber-curd-mint-soap-bar-115g",
        "saffron": "deyga-shea-saffron-bath-bar-100g",
        "pinkclay": "deyga-rose-pink-clay-bath-bar-100g",
        "shampoo": "vilvah-goat-milk-shampoo-250ml",
        "mask": "vilvah-goat-milk-hair-mask-200g-deep-conditioning-treatment-for-frizz-flyaway-control-curl-definition-moisture-repair-mask",
        "hairkit": "vilvah-goat-milk-hair-kit",
        "bestkit": "vilvah-bestseller-hair-kit-goat-milk-shampoo-200ml-cream-conditioner-200ml-nourishing-frizz-control-sulfate-free-hair-care-set",
        "bodykit": "vilvah-milk-body-kit-goat-milk-body-wash-milk-body-lotion-deep-hydration-skin-softening-nourishment-oat-milk-olive-squalane-coconut-oil-vanilla-scent",
        "lotion": "vilvah-milk-body-lotion-250ml-vegan-paraben-free-with-oat-milk-ceramides-olive-squalane-deep-moisturizing-for-dry-sensitive-skin-non-greasy-fast-absorbing-formula",
    },
    "shop": ["classic", "rose", "charcoal", "bodykit", "shampoo", "mask", "hairkit", "saffron"],
    "body": """<p>Goat milk soap is a bar soap made with goat milk in its recipe. It gives a creamy lather and leaves skin feeling soft rather than tight, which is why many people keep a bar by the bath or basin. This guide explains how goat milk soap is made, how to use it on your face and body, and how to choose between the goat milk soaps from Vilvah, one of the two Indian natural brands Swansura is an official UK partner of.</p>
<h2>What is goat milk soap?</h2>
<p>Every true bar soap is made by mixing oils or butters with lye (sodium hydroxide). The two react together to form soap, a process called saponification. In goat milk soap, fresh goat milk goes into the recipe, which gives the bar a creamy lather. You will see sodium hydroxide at the end of the ingredient lists below: that is how all bar soap is made.</p>
<p>Vilvah makes its goat milk bars by hand with farm-fresh goat milk and a base of plant oils such as extra virgin olive, coconut and castor oil. Coconut oil gives the bubbly lather, olive oil a gentle feel and castor oil a cushioned foam.</p>
<h2>The Vilvah goat milk soaps</h2>
<ul>
<li>[[classic|Classic Goat Milk Soap]] ({{classic}}, 115g): goat milk, olive, coconut and castor oils, lightly scented with lavender essential oil. Six ingredients in all, and listed as suiting dry and sensitive skin.</li>
<li>[[rose|Classic Rose Goat Milk Soap]] ({{rose}}, 125g): goat milk with rose petals, rose hydrosol, French pink clay, shea butter and rice bran oil, scented with rose and geranium essential oils.</li>
<li>[[charcoal|Charcoal Goat Milk Soap]] ({{charcoal}}, 115g): activated charcoal with goat milk, for a clean-feeling daily wash. The charcoal gives the bar its colour.</li>
</ul>
<p>All three are in our <a href="/collections/goat-milk-soap">goat milk soap</a> collection. One bar that looks similar is not a goat milk soap: Vilvah’s [[mint|Cucumber, Curd &amp; Mint Soap]] ({{mint}}) is made with cucumber juice, curd and mint leaves, for a cool, zesty morning wash.</p>
<h2>Which bar should you choose?</h2>
<ul>
<li><strong>A soft, simple scent:</strong> the Classic bar, with lavender.</li>
<li><strong>A floral scent:</strong> Classic Rose.</li>
<li><strong>A clean-feeling wash:</strong> Charcoal.</li>
<li><strong>Something fresh and minty:</strong> Cucumber, Curd &amp; Mint.</li>
<li><strong>A bar without milk:</strong> Deyga’s [[saffron|Shea Saffron Bath Bar]] ({{saffron}}) and [[pinkclay|Rose Pink Clay Bath Bar]] ({{pinkclay}}) are made with raw shea butter and coconut and olive oils.</li>
</ul>
<h2>How to use goat milk soap</h2>
<ol>
<li>Wet your skin and the bar, then work up a lather between your hands.</li>
<li>Massage the foam over damp face or body, keeping it away from your eyes.</li>
<li>Rinse well with warm water and pat dry.</li>
<li>Follow with a moisturiser or body lotion if your skin tends to feel dry.</li>
<li>Keep the bar on a draining soap dish between uses. A handmade bar left sitting in water softens quickly.</li>
</ol>
<p>The Classic, Classic Rose and Cucumber bars contain essential oils, so patch test before first use.</p>
<h2>Goat milk shampoo and hair care</h2>
<p>Goat milk is not only for soap. [[shampoo|Vilvah Goat Milk Shampoo]] ({{shampoo}}, 250ml) is a creamy shampoo with goat milk, jasmine flower water and hydrolysed pea protein, with a light jasmine and citrus scent. [[mask|Vilvah Goat Milk Hair Mask]] ({{mask}}) pairs goat milk with ceramides and argan oil to condition dry, frizzy lengths. Buy them together in the [[hairkit|Goat Milk Hair Kit]] ({{hairkit}}), or try the shampoo with Vilvah’s Cream Conditioner in the [[bestkit|Bestseller Hair Kit]] ({{bestkit}}). Our <a href="/blogs/journal/natural-shampoo-guide">natural shampoo guide</a> covers how to choose a shampoo for dry hair.</p>
<h2>Goat milk for the body</h2>
<p>The [[bodykit|Vilvah Milk Body Kit]] ({{bodykit}}) pairs a Goat Milk Body Wash, made with goat milk, chamomile water and coconut oil and scented with vanilla, with a Milk Body Lotion. If you were looking for a goat milk body lotion, note that the [[lotion|Milk Body Lotion]] ({{lotion}}) is made with oat milk, ceramide NP and olive squalane: the goat milk in this kit is in the body wash. For richer body care after a soap, read our <a href="/blogs/journal/how-to-use-body-butter">body butter guide</a>.</p>
<h2>Good to know</h2>
<ul>
<li>Goat milk soap is not vegan, because it contains goat milk.</li>
<li>Every skin is different. If you have a skin condition, ask a pharmacist or GP before trying a new soap.</li>
<li>A goat milk bar wrapped in tissue makes an easy gift: see our <a href="/collections/stocking-fillers">stocking fillers</a>.</li>
<li>Everything is 100% authentic and shipped from the UK. Browse the whole <a href="/collections/range-goat-milk">goat milk range</a>; UK delivery is free on orders over £40.</li>
</ul>""",
    "faq": [
        ["What is goat milk soap?",
         "A bar soap made with goat milk in its recipe, alongside oils such as olive, coconut and castor oil. It gives a creamy lather and leaves skin feeling soft. Vilvah makes three goat milk bars: Classic, Classic Rose and Charcoal."],
        ["Can I use goat milk soap on my face?",
         "Vilvah’s Classic and Classic Rose bars are made for face and body. Keep the lather away from your eyes, rinse well and patch test first, as both contain essential oils."],
        ["Is goat milk soap good for sensitive skin?",
         "The Classic bar is listed as suiting dry and sensitive skin, and Classic Rose sensitive skin. Every skin is different, so patch test first, and ask a pharmacist or GP if you have a skin condition."],
        ["Does goat milk soap contain lye?",
         "All true bar soap is made with lye (sodium hydroxide), which reacts with the oils to form soap. That is why it appears on the ingredient list."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_goat_milk_soap_2026-11-09.jsonl")

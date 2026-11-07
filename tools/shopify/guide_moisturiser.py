"""Journal guide 'Moisturiser for your skin type: dry, oily, sensitive and combination' (user, 7 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): night cream 3,600/mo (KD 18),
moisturiser for dry skin 2,900 (KD 29), moisturiser for oily skin 1,900 (KD 22), moisturiser for sensitive skin
1,300 (KD 18), moisturiser for combination skin 1,000 (KD 26), natural moisturiser 1,000 (KD 24), natural
moisturiser uk 140. Facts = product descriptions + stored custom.inci (7 Nov 2026). Left out (ASA / unprovable):
'up to 7-8 hours', boosts collagen, reduces pigmentation / fine lines / wrinkles, cell regeneration, oil control,
non-comedogenic, 'anti-ageing benefits' (the Highborn product NAME contains Anti-Ageing and is kept as a name),
customer quotes. Prices are written into the text: re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_moisturiser.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_moisturiser_2026-11-07.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Moisturiser for your skin type: dry, oily, sensitive and combination",
    "handle": "moisturiser-for-your-skin-type",
    "tag": "Skin Studio",
    "summary": "How to choose a moisturiser for dry, oily, sensitive or combination skin, when to add a serum or night cream, and how to apply it.",
    "mt": "Moisturiser for Dry, Oily & Sensitive Skin: Guide | Swansura",
    "md": "How to choose a moisturiser for dry, oily, sensitive or combination skin, plus night creams, SPF moisturisers, hydrating serums and how to apply them.",
    "pick": {
        "deep": "deyga-deep-moisturising-face-cream-30g",
        "light": "deyga-light-moisturising-face-cream-30g",
        "ultra": "vilvah-ultra-moisturising-cream-anti-aging-hydration-for-fine-lines-wrinkles-50ml",
        "imperial": "imperial-moisturiser",
        "night": "night-elixir",
        "set": "ultimate-day-night-moisture-set",
        "glow": "glowguard-spf30-anti-ageing-moisturiser",
        "ha": "deyga-2-hyaluronic-acid-serum-20ml",
        "drops": "milk-drops-brightening-serum-40-ml-rice-milk-alpha-arbutin-skin-brightening-treatment-for-dark-spots-uneven-skin-tone",
    },
    "titles": {},
    "shop": ["deep", "light", "ultra", "imperial", "night", "glow", "ha", "drops"],
    "body": """<p>A good <strong>moisturiser</strong> is the step that holds the rest of your routine together. It softens skin, helps it feel comfortable all day and gives make-up or sunscreen a smooth base. But the right texture depends on your skin: a rich cream that rescues dry skin can feel heavy on oily skin, and a light lotion may not be enough in winter. Here is how to choose a moisturiser for your skin type.</p>
<h2>Cream, lotion or gel: what is the difference?</h2>
<p>Most moisturisers mix water with oils and butters. The more oil and butter, the richer the texture:</p>
<ul>
<li><strong>Rich creams</strong> hold more butters and oils, such as shea butter and almond oil. They suit dry and very dry skin, and cold weather.</li>
<li><strong>Light creams and lotions</strong> have more water and lighter oils. They suit normal, oily and combination skin.</li>
<li><strong>Gels and serums</strong> are mostly water with moisture-loving ingredients such as glycerine and hyaluronic acid. They work on their own for oily skin, or under a cream.</li>
</ul>
<h2>Moisturiser for dry skin</h2>
<p>Dry skin feels tight, may flake and drinks a light lotion straight in. Look for a cream with butters and oils.</p>
<p>[[deep|Deyga Deep Moisturising Face Cream]] ({{deep}}, 30g) blends shea butter with marula and almond oils, centella asiatica (gotu kola) and cardamom, and Deyga makes it without artificial fragrance. [[imperial|Highborn London Imperial Moisturiser]] ({{imperial}}, 50ml) is a richer, nourishing cream made in England for dry, tight-feeling skin. See more <a href="/collections/moisturiser-for-dry-skin">moisturisers for dry skin</a>.</p>
<h2>Moisturiser for oily skin</h2>
<p>Oily skin still needs moisture: skipping it can leave skin feeling tight while it still looks shiny. Choose a light, fast-absorbing texture.</p>
<p>[[light|Deyga Light Moisturising Face Cream]] ({{light}}, 30g) is made for oily and normal skin, with rosehip, almond and avocado oils, shea butter, centella asiatica and ectoin, and a hint of vanilla essential oil. On very oily days, a serum such as [[ha|Deyga 2% Hyaluronic Acid Serum]] ({{ha}}, 20ml) can be enough on its own. More ideas for <a href="/collections/oily-skin">oily skin</a>.</p>
<h2>Moisturiser for sensitive skin</h2>
<p>Sensitive skin does best with a short ingredient list and no added fragrance. Of the creams above, the Deyga Deep Moisturising Face Cream is made without artificial fragrance; the Light cream contains vanilla essential oil, so patch test it first. Introduce one new product at a time, and see more for <a href="/collections/sensitive-skin">sensitive skin</a>.</p>
<h2>Moisturiser for combination skin</h2>
<p>Combination skin is oily through the centre and normal or dry on the cheeks. Use a light moisturiser all over and add a little richer cream only where skin feels dry. [[ultra|Vilvah Ultra Moisturising Cream]] ({{ultra}}, 50ml) is a good middle ground: olive squalane, glycerine and plant extracts in a non-greasy cream that Vilvah makes for all skin types, with white lily essential oil.</p>
<h2>Add a hydrating serum underneath</h2>
<p>Serums are light and watery, so they go on before your moisturiser. A hyaluronic acid serum such as the Deyga 2% Hyaluronic Acid Serum (sodium hyaluronate, panthenol, aloe and centella) or [[drops|Vilvah Milk Drops Hydrating Serum]] ({{drops}}), with aloe vera juice, hyaluronic acid and rice milk extract, adds a layer of moisture that the cream then seals in. Aloe vera gel works in a similar way; read <a href="/blogs/journal/how-to-use-aloe-vera-gel">how to use aloe vera gel</a>. Browse every <a href="/collections/serum">serum</a>.</p>
<h2>Day cream or night cream?</h2>
<p>By day, your moisturiser sits under sunscreen and make-up, so a lighter texture often works best. Finish with SPF, or use a moisturiser with SPF built in, such as [[glow|Highborn London GLOWGUARD SPF30 Moisturiser]] ({{glow}}), which uses non-nano zinc oxide.</p>
<p>At night there is no sunscreen or make-up to layer, so many people like something richer. A <strong>night cream</strong> such as [[night|Highborn London Night Elixir]] ({{night}}) is a comforting cream made for the last step of an evening routine. The [[set|Ultimate Day &amp; Night Moisture Set]] ({{set}}) pairs it with the Imperial Moisturiser.</p>
<h2>How to apply moisturiser</h2>
<ol>
<li><strong>Cleanse</strong> with a face wash that suits your skin: see <a href="/blogs/journal/face-wash-for-your-skin-type">face wash for your skin type</a>.</li>
<li><strong>Apply serum,</strong> if you use one, to slightly damp skin.</li>
<li><strong>Warm a pea-sized amount</strong> of moisturiser between your fingertips.</li>
<li><strong>Press and smooth</strong> it over your face and neck with upward strokes, avoiding the eyes.</li>
<li><strong>In the morning, finish with sunscreen</strong> unless your moisturiser has SPF.</li>
</ol>
<h2>What makes a moisturiser "natural"?</h2>
<p>There is no legal definition of "natural" in the UK, so read the ingredient list rather than the label. In the creams above you will find plant butters and oils (shea, marula, rosehip, avocado, almond, olive squalane) alongside glycerine, water and an emulsifier that keeps them blended. Full ingredient lists are on every product page.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test</strong> a new moisturiser on your jaw or inner arm for 24 hours.</li>
<li><strong>Your skin changes with the seasons:</strong> many people switch to a richer cream in winter and a lighter one in summer.</li>
<li><strong>Dryness, redness or itching that lasts</strong> is worth showing to a pharmacist or your GP.</li>
</ul>
<p>Explore every product for <a href="/collections/concern-hydration">hydration</a>, our <a href="/collections/highborn-london">Highborn London</a> range and the full <a href="/collections/skincare">skincare</a> shelf, all dispatched from the UK.</p>""",
    "faq": [
        ["What is the best moisturiser for dry skin?",
         "A cream with butters and oils, such as shea butter, almond or marula oil. The Deyga Deep Moisturising Face Cream and the Highborn London Imperial Moisturiser are both made for dry skin. Apply to slightly damp skin."],
        ["Do I need a moisturiser if my skin is oily?",
         "Yes. Choose a light, fast-absorbing texture such as the Deyga Light Moisturising Face Cream, or a hydrating serum on its own on very oily days."],
        ["What is the difference between a day cream and a night cream?",
         "A day cream is usually lighter so it sits well under sunscreen and make-up, or it has SPF built in. A night cream is often richer, because there is nothing to layer on top."],
        ["Should I use a serum before or after moisturiser?",
         "Before. Apply a light serum such as a hyaluronic acid serum to slightly damp skin, then seal it in with your moisturiser."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_moisturiser_2026-11-07.jsonl")

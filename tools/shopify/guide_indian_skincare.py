"""Journal guide 'Indian skincare in the UK: the key ingredients, Vilvah and Deyga, and how to start' (user, 10 Nov 2026:
"Go ahead with the Indian skincare UK guide"; plan item 5 of docs/seo/SEO_Orders_Audit_2026-11-09.md).

Targets: indian skincare uk (no Semrush volume yet; Google results are editorial lists, no shop owns it, see
competitor_research_2026-11-09.md), natural skincare uk 480 (KD 59), ayurvedic hair oil 390 (KD 12), ayurvedic skincare
uk 20, multani mitti face pack 140. Facts = stored custom.inci of each product (Admin read 10 Nov). Ingredients are
described as traditional / culinary-cultural use only, never as having an effect. Not repeated: the brand comparison in
/blogs/journal/deyga-or-vilvah (linked instead). Claim-named products (Hair Growth Oil) are named once, never
explained. Left out (ASA): brightening, tan, pigmentation, acne, anti-inflammatory / antibacterial, hair growth,
'chemical-free', 'Ayurvedic medicine'. Prices are written into the text: re-run and update if prices change.

Usage: python3 tools/shopify/guide_indian_skincare.py <allp.json>   (handle -> storefront product)
Output: docs/seo/guide_indian_skincare_2026-11-10.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Indian skincare in the UK: the key ingredients, Vilvah and Deyga, and how to start",
    "handle": "indian-skincare-uk-guide",
    "tag": "Skin Studio",
    "summary": "Turmeric, neem, saffron, rose water, amla and bhringraj: the ingredients behind Indian skincare, which Vilvah and Deyga products use them, and how to buy them in the UK.",
    "mt": "Indian Skincare UK: Ingredients, Vilvah & Deyga | Swansura",
    "md": "Indian skincare explained: turmeric, neem, saffron, rose water and amla, the Vilvah and Deyga products that use them, and how to buy them in the UK.",
    "pick": {
        "neembar": "deyga-neem-turmeric-bath-bar-100g",
        "orange": "deyga-orange-almond-face-pack-powder-100g",
        "spirulina": "deyga-spirulina-matcha-face-pack-150g",
        "neemoil": "deyga-neem-seed-oil-30ml",
        "roseglow": "deyga-rose-glow-serum-30ml",
        "saffronbar": "deyga-shea-saffron-bath-bar-100g",
        "mudmask": "vilvah-milk-mud-mask-50ml-de-tan-brightening-face-mask-with-oat-milk-saffron-kaolin-clay-natural-tan-removal-oil-control-radiant-glow-for-all-skin-types",
        "rosewater": "deyga-pure-rose-water-toner-100-ml",
        "hairoil": "deygas-hair-growth-oil-100-ml-natural-blend-of-coconut-amla-hibiscus-stronger-hair",
        "herbal": "vilvah-herbal-shampoo-250ml",
        "serum": "vilvah-anti-frizz-hair-serum-30ml-silicone-free-hair-serum-with-black-seed-curry-leaf-oil-for-frizz-control-split-end-prevention-and-heat-protection",
        "beet": "deygas-beetroot-lip-balm-classic-10-g-100-natural-no-harsh-chemicals",
    },
    "shop": ["neembar", "orange", "roseglow", "rosewater", "mudmask", "hairoil", "herbal", "beet"],
    "body": """<p>Indian skincare grows out of ingredients found in Indian kitchens and gardens: turmeric, neem, saffron, rose water, amla and coconut oil. Many people in the UK grew up with them through family routines, and many more are discovering them now. This guide explains the key ingredients, shows which products from <a href="/collections/vilvah">Vilvah</a> and <a href="/collections/deyga">Deyga</a> actually contain them (checked against each full ingredient list), and covers how to buy Indian skincare in the UK without waiting for a parcel from India.</p>
<h2>What makes Indian skincare different?</h2>
<p>Two things stand out. First, the ingredients: many come from Ayurveda, India’s traditional system of wellbeing, and from everyday cooking, so the labels read like a spice rack. Deyga even lists many ingredients with their Sanskrit names, such as Haridra for turmeric, Nimba for neem, Kumkuma for saffron and Satapatrika for rose. Second, the formats: powder face packs you mix with water, oils massaged into the scalp before washing, and handmade bars. These are cosmetic products, not Ayurvedic medicines, and we describe them that way.</p>
<h2>The key ingredients, and where to find them</h2>
<h3>Turmeric (haldi)</h3>
<p>Turmeric is part of the Indian haldi ceremony before a wedding, when a turmeric paste is spread on the bride and groom. You will find it in the [[neembar|Deyga Neem &amp; Turmeric Bath Bar]] ({{neembar}}), made with coconut oil, neem hydrosol, turmeric and shea butter, and in the [[orange|Deyga Orange &amp; Almond Face Pack]] ({{orange}}), a three-ingredient powder of sun-dried orange pulp and zest, almond meal and turmeric. Turmeric can colour towels and nails, so rinse well.</p>
<h3>Neem</h3>
<p>Neem is a tree grown across India, and its leaves and seeds are used in hair and skin care. [[neemoil|Deyga Neem Seed Oil]] ({{neemoil}}) has one ingredient: neem seed oil, with a strong, earthy scent. The [[spirulina|Deyga Spirulina Matcha Face Pack]] ({{spirulina}}) mixes neem leaf with spirulina, matcha, moringa and aloe vera powder.</p>
<h3>Saffron (kesar or kumkuma)</h3>
<p>Saffron is one of the most prized spices in Indian cooking and a long-standing beauty ingredient. The [[roseglow|Deyga Rose Glow Serum]] ({{roseglow}}) is a face oil of native rose and saffron in virgin coconut, pomegranate seed, rosehip, almond and jojoba oils. The [[saffronbar|Deyga Shea Saffron Bath Bar]] ({{saffronbar}}) pairs saffron with raw shea butter, and the [[mudmask|Vilvah Milk Mud Mask]] ({{mudmask}}) combines kaolin clay, licorice root, oat milk and saffron extract.</p>
<h3>Rose water (gulab jal)</h3>
<p>Rose water is a staple of Indian dressing tables, used to refresh the face or mix face packs. [[rosewater|Deyga Pure Rose Water Toner]] ({{rosewater}}) has two ingredients: rose and distilled water. It is also the classic liquid for mixing a powder face pack.</p>
<h3>Clay and multani mitti</h3>
<p>Multani mitti, or fuller’s earth, is the traditional Indian clay for face packs. Our clay products use kaolin and French pink clay instead, such as the Milk Mud Mask above. Our <a href="/blogs/journal/face-mask-guide">face mask guide</a> explains how to use clay masks and powder packs.</p>
<h3>Amla, bhringraj and hibiscus for hair</h3>
<p>Oiling the hair before washing is one of the best-known Indian routines. [[hairoil|Deyga’s Hair Growth Oil]] ({{hairoil}}) is a coconut, almond and castor oil base with amla, bhringraj, hibiscus, fenugreek, curry leaves and vetiver: a classic Indian herbal hair oil. [[serum|Vilvah Anti-Frizz Hair Serum]] ({{serum}}) is a lighter, leave-in option with black seed oil, curry leaf oil, hibiscus oil and amla extract, and [[herbal|Vilvah Herbal Shampoo]] ({{herbal}}, 250ml) includes neem leaf, amla and basil leaf water. Read our <a href="/blogs/journal/hair-oil-guide">hair oil guide</a> for how to oil your hair.</p>
<h3>Beetroot and goat milk</h3>
<p>Two newer favourites: the [[beet|Deyga Beetroot Lip Balm]] ({{beet}}) is made with beetroot extract, almond, avocado and jojoba oils and shea butter, and Vilvah builds much of its range on goat milk (see <a href="/collections/goat-milk-soap">goat milk soap</a>).</p>
<h2>A simple way to start</h2>
<ol>
<li><strong>Cleanse:</strong> a handmade bar such as the Neem &amp; Turmeric bar for the body, or a gentle face wash.</li>
<li><strong>Refresh:</strong> pat on rose water with clean hands or a cotton pad.</li>
<li><strong>Nourish:</strong> a few drops of a face oil such as the Rose Glow Serum in the evening.</li>
<li><strong>Once a week:</strong> a powder face pack mixed with rose water, or a clay mask.</li>
<li><strong>Hair:</strong> oil the scalp and lengths an hour or more before washing, then shampoo.</li>
</ol>
<p>Many of these products contain essential oils or strongly scented plant ingredients, so patch test anything you leave on the skin, and keep powders and oils away from the eyes. For which brand suits your skin type, read <a href="/blogs/journal/deyga-or-vilvah">Deyga or Vilvah</a>; for adding a serum, see our <a href="/blogs/journal/face-serum-guide">face serum guide</a>.</p>
<h2>Buying Indian skincare in the UK</h2>
<ul>
<li><strong>Official UK partner:</strong> Swansura is an official UK partner of both Deyga and Vilvah, so every product is genuine.</li>
<li><strong>Shipped from the UK:</strong> orders leave our UK stock, so there is no wait for a parcel from India and no import charge at your door.</li>
<li><strong>Full ingredient lists:</strong> almost every product page has the full ingredient list on its Ingredients tab, so you can check before you buy.</li>
<li><strong>Delivery:</strong> UK delivery is free on orders over £40, and unopened items can be returned within 14 days.</li>
</ul>
<p>Browse all our <a href="/collections/natural-skincare">natural skincare</a>, or shop by brand: <a href="/collections/vilvah">Vilvah</a> and <a href="/collections/deyga">Deyga</a>.</p>""",
    "faq": [
        ["What is Indian skincare?",
         "Skincare built around ingredients long used in India, such as turmeric, neem, saffron, rose water, amla and coconut oil, often in formats like powder face packs, hair oils and handmade bars. Vilvah and Deyga are two Indian brands that make it."],
        ["Where can I buy Vilvah and Deyga in the UK?",
         "At Swansura. We are an official UK partner of both brands, and every order ships from our UK stock, so there is no import charge at your door."],
        ["Are Vilvah and Deyga Ayurvedic?",
         "Both use ingredients from Ayurvedic tradition, and Deyga lists many by their Sanskrit names, such as Haridra for turmeric. They are cosmetic products, not Ayurvedic medicines."],
        ["How do I check the ingredients?",
         "Almost every Vilvah and Deyga product page has the full ingredient list on its Ingredients tab. Patch test anything you leave on the skin, especially products with essential oils."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_indian_skincare_2026-11-10.jsonl")

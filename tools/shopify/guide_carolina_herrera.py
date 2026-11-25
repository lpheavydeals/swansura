"""Journal guide 'Carolina Herrera perfume: Bad Boy, Bad Boy Extreme and 212 compared'
(user, 25 Nov 2026: 'Write and Publish All').

Semrush UK: carolina herrera perfume 9,900. Trends: steepest seasonal rise of the topics checked (peaks 21-27 Dec).
5 Carolina Herrera in stock with photos, all men's (allp_map 25 Nov); Bad Boy Extreme only the 10ml option in stock.
Very Good Girl Glam + 212 VIP Rose sold out: text links only. 3 more cards = men's scents in a similar mood
(Azzaro The Most Wanted Parfum, Joop! Homme Le Parfum, Dunhill Desire Black), named as different perfumes.
Facts = stored custom.sw notes + descriptions (Admin read 25 Nov). NO PRICES in the text.

Usage: python3 tools/shopify/guide_carolina_herrera.py <allp_map.json>
Output: docs/seo/guide_carolina_herrera_2026-11-25.jsonl
"""
import json
import sys

from journal_lib import build

C = "carolina-herrera-"
A = {
    "title": "Carolina Herrera perfume: Bad Boy, Bad Boy Extreme and 212 compared",
    "handle": "carolina-herrera-perfume-guide",
    "tag": "Scent Studio",
    "summary": "The Carolina Herrera fragrances we stock: Bad Boy Le Parfum, Bad Boy Extreme, 212 VIP Men and 212 Sexy Men, with the notes, the differences and who each suits.",
    "mt": "Carolina Herrera Perfume: Bad Boy & 212 Compared | Swansura",
    "md": "Carolina Herrera Bad Boy Le Parfum vs Bad Boy Extreme, and 212 VIP Men vs 212 Sexy Men: the notes, sizes and which one to choose.",
    "pick": {
        "bb150": C + "bad-boy-le-parfum-eau-de-parfum-150ml-men-s-woody-aromatic-fragrance",
        "bb10": C + "bad-boy-le-parfum-eau-de-parfum-10ml-men-s-woody-aromatic-fragrance",
        "extreme": C + "bad-boy-extreme-eau-de-parfum-men-s-warm-spicy-amber-fragrance",
        "vip": C + "212-vip-men-eau-de-toilette-100ml-men-s-aromatic-woody-fragrance",
        "sexy": C + "212-sexy-men-eau-de-toilette-100ml-men-s-warm-spicy-fragrance",
        "glam": C + "very-good-girl-glam-parfum-50ml-women-s-floral-fruity-gourmand-fragrance",
        "rose": C + "212-vip-rose-eau-de-parfum-125ml-women-s-floral-fruity-fragrance",
        "azzaro": "azzaro-the-most-wanted-parfum-100ml-men-s-warm-spicy-amber-fragrance",
        "joop": "joop-homme-le-parfum-75ml-men-s-warm-spicy-amber-fragrance",
        "dunhill": "dunhill-desire-black-eau-de-toilette-100ml-men-s-spicy-woody-fragrance",
    },
    "titles": {},
    "soldout": ["glam", "rose"],
    "shop": ["bb150", "extreme", "vip", "sexy", "bb10", "azzaro", "joop", "dunhill"],
    "body": """<p><strong>Carolina Herrera perfume</strong> for men comes in two families we stock: Bad Boy, in its lightning-bolt bottle, and 212, the house's city-inspired line. Here is every Carolina Herrera fragrance we have, what is in each one, and how to choose between them.</p>
<h2>Bad Boy Le Parfum</h2>
<p>Bad Boy Le Parfum is an aromatic, leathery eau de parfum for men, in a [[bb150|150ml bottle]] or a [[bb10|10ml size]] for travel. Grapefruit and hemp open it, black pepper and geranium add spice and a green warmth, and leather with vetiver gives a dark, dry base. It starts sharp and citrusy, then turns smoky as the pepper and leather come through.</p>
<h2>Bad Boy Extreme</h2>
<p>[[extreme|Bad Boy Extreme Eau de Parfum]], in stock in the 10ml size, is the sweeter, warmer version: ginger and bergamot, then cacao and vetiver, over patchouli and tonka bean. The cacao and tonka make it dark and sweet-spiced, so it suits evenings and nights out.</p>
<p><strong>Le Parfum or Extreme?</strong> Choose Le Parfum for a dry, leathery scent with pepper; choose Extreme if you like cocoa and tonka sweetness.</p>
<h2>212 VIP Men</h2>
<p>[[vip|212 VIP Men Eau de Toilette]] (100ml) is the bright, playful one. Lime, passion fruit, pepper and ginger open it, a cocktail heart of vodka, gin, mint and spices follows, and amber, leather and woody notes give it a warm base. Fresh and lively, it is made for parties and weekends.</p>
<h2>212 Sexy Men</h2>
<p>[[sexy|212 Sexy Men Eau de Toilette]] (100ml) is warmer and softer: mandarin orange, bergamot and green notes, then cardamom, pepper and flowers, over vanilla, sandalwood, guaiac wood, musk and amber. A smooth, spiced scent for evenings and cooler months.</p>
<h2>Which Carolina Herrera perfume should you choose?</h2>
<ul>
<li><strong>Dry, smoky and leathery:</strong> Bad Boy Le Parfum.</li>
<li><strong>Sweet, with cocoa and tonka:</strong> Bad Boy Extreme.</li>
<li><strong>Fresh and fun:</strong> 212 VIP Men.</li>
<li><strong>Soft, warm and spiced:</strong> 212 Sexy Men.</li>
<li><strong>To try before a big bottle:</strong> the 10ml Bad Boy Le Parfum or Bad Boy Extreme.</li>
</ul>
<h2>Carolina Herrera for women</h2>
<p>The women's bottles we list, [[glam|Very Good Girl Glam]] and [[rose|212 VIP Rose]], are sold out at the moment. For women's gift ideas, see our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</p>
<h2>Other men's scents in a similar mood</h2>
<p>These are different perfumes, not copies:</p>
<ul>
<li>If you like Bad Boy Extreme's sweetness: [[azzaro|Azzaro The Most Wanted Parfum]] (100ml), with ginger, woody notes and bourbon vanilla.</li>
<li>If you like 212 Sexy Men's warm spice: [[joop|Joop! Homme Le Parfum]] (75ml), with lavender and cinnamon, orange blossom and tonka bean, over vanilla, amber and woods.</li>
<li>If you like Bad Boy Le Parfum's pepper: [[dunhill|Dunhill Desire Black Eau de Toilette]] (100ml), with black pepper, bergamot and grapefruit, cypress, saffron and rose, over vetiver, olibanum and amber.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum or eau de toilette?</strong> Bad Boy Le Parfum and Extreme are eau de parfums; the 212 scents are eau de toilettes. Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying for him?</strong> See <a href="/collections/aftershave-gift-sets-for-him">aftershave gift sets for him</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/carolina-herrera">Carolina Herrera</a> fragrance, or browse <a href="/collections/perfume-for-men">perfume for men</a>.</p>""",
    "faq": [
        ["What does Carolina Herrera Bad Boy Le Parfum smell like?",
         "Bad Boy Le Parfum opens with grapefruit and hemp, has black pepper and geranium in the heart, and dries down to leather and vetiver. It is aromatic, peppery and leathery."],
        ["What is the difference between Bad Boy Le Parfum and Bad Boy Extreme?",
         "Le Parfum is dry and leathery, with pepper and vetiver. Bad Boy Extreme is sweeter: ginger and bergamot, then cacao and vetiver, over patchouli and tonka bean."],
        ["Which is fresher, 212 VIP Men or 212 Sexy Men?",
         "212 VIP Men is the fresher one, with lime, passion fruit, ginger and a vodka, gin and mint heart. 212 Sexy Men is warmer, with cardamom and pepper over vanilla and sandalwood."],
        ["Do you sell Carolina Herrera perfume for women?",
         "We list Very Good Girl Glam and 212 VIP Rose, but both are sold out at the moment. The Carolina Herrera fragrances in stock now are for men."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_carolina_herrera_2026-11-25.jsonl")

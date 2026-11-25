"""Journal guide 'Guerlain perfume: Habit Rouge, Samsara, L'Instant, La Petite Robe Noire and more compared'
(user, 25 Nov 2026: topics checked against Semrush, Search Console and Google Trends, then 'Write and Publish All').

Semrush UK: guerlain perfume 12,100, guerlain oud essentiel 590, habit rouge 480, samsara 480. GSC 4-10 Nov: Mon
Guerlain set pos 8 (11 impr), L'Instant / Samsara / Petite Robe Noire showing. Trends: rising, peaks 21-27 Dec.
7 Guerlain in stock with photos (allp_map 25 Nov) + Chopard Amber Malaki as 'a different perfume'. Musc Noble sold
out: text link only. Facts = stored custom.sw notes + descriptions (Admin read 25 Nov). NO PRICES in the text.

Usage: python3 tools/shopify/guide_guerlain.py <allp_map.json>
Output: docs/seo/guide_guerlain_2026-11-25.jsonl
"""
import json
import sys

from journal_lib import build

G = "guerlain-"
A = {
    "title": "Guerlain perfume: Habit Rouge, Samsara, L'Instant, La Petite Robe Noire and more compared",
    "handle": "guerlain-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Guerlain fragrance we stock, from Habit Rouge and Samsara to L'Instant, La Petite Robe Noire, Oud Essentiel, Épices Exquises and the Mon Guerlain miniature set, with the notes and who each suits.",
    "mt": "Guerlain Perfume: Habit Rouge, Samsara & More | Swansura",
    "md": "Guerlain perfume compared: Habit Rouge, Samsara, L’Instant, La Petite Robe Noire, Oud Essentiel, Épices Exquises and the Mon Guerlain mini set.",
    "pick": {
        "habit": G + "habit-rouge-eau-de-parfum-100ml-luxury-men-s-amber-woody-fragrance",
        "samsara": G + "samsara-eau-de-parfum-75ml-luxury-women-s-floral-woody-fragrance",
        "instant": G + "l-instant-de-guerlain-eau-de-parfum-75ml-luxury-women-s-floral-amber-fragrance",
        "robe": G + "la-petite-robe-noire-ma-robe-cocktail-eau-de-toilette-100ml-women-s-fruity-floral-fragrance",
        "mon": G + "mon-guerlain-miniature-perfume-gift-set-4x5ml-women-s-fragrance-collection",
        "oud": G + "oud-essentiel-eau-de-parfum-125ml-luxury-unisex-oud-woody-fragrance",
        "epices": G + "epices-exquises-eau-de-parfum-125ml-luxury-unisex-spicy-woody-fragrance",
        "musc": G + "musc-noble-eau-de-parfum-125ml-luxury-unisex-musky-woody-fragrance",
        "amber": "chopard-amber-malaki-eau-de-parfum-80ml-luxury-unisex-amber-fragrance",
    },
    "titles": {},
    "soldout": ["musc"],
    "shop": ["habit", "samsara", "instant", "mon", "robe", "oud", "epices", "amber"],
    "body": """<p><strong>Guerlain perfume</strong> runs from classic bottles such as Habit Rouge and Samsara to the modern Mon Guerlain and the richer, unisex fragrances of its niche line. Here is every Guerlain fragrance we stock, what is in each one, and who it suits.</p>
<h2>Guerlain Habit Rouge</h2>
<p>[[habit|Guerlain Habit Rouge Eau de Parfum]] (100ml) is the men's classic of the house. Four citrus notes, lemon, bergamot, orange and lime, open it; rose, jasmine, cinnamon and patchouli warm the heart; and leather, vanilla, amber, benzoin and labdanum make a smooth base. Bright at first, then warm and polished, it suits the office as well as evenings.</p>
<h2>Guerlain Samsara</h2>
<p>[[samsara|Guerlain Samsara Eau de Parfum]] (75ml) is a warm floral built on sandalwood. Bergamot, peach and ylang-ylang lead into jasmine, rose, narcissus and orris, and the base is sandalwood, vanilla, amber, tonka bean and musk. Smooth rather than sharp, it is a good choice for someone who likes rich, creamy florals.</p>
<h2>L'Instant de Guerlain</h2>
<p>[[instant|L'Instant de Guerlain Eau de Parfum]] (75ml) is a honeyed floral. Mandarin orange, bergamot and red apple open it; magnolia, jasmine, ylang-ylang and iris form the heart; and honey, vanilla, amber, benzoin and musk settle on the skin. It sits between Samsara's depth and the lightness of La Petite Robe Noire.</p>
<h2>La Petite Robe Noire Ma Robe Cocktail</h2>
<p>[[robe|La Petite Robe Noire Ma Robe Cocktail Eau de Toilette]] (100ml) is the lightest Guerlain we stock: bergamot, lemon, orange and red berries, then rose, jasmine and cherry, over white amber, musk and patchouli. Fruity, playful and easy to wear every day.</p>
<h2>The Mon Guerlain miniature set</h2>
<p>The [[mon|Mon Guerlain Miniature Perfume Gift Set]] holds four 5ml bottles, 20ml in all:</p>
<ul>
<li><strong>Mon Guerlain Eau de Parfum</strong> (2 x 5ml): lavender, bergamot, jasmine sambac, iris, Tahitian vanilla and sandalwood.</li>
<li><strong>Mon Guerlain Florale Eau de Parfum</strong> (5ml): lavender, jasmine sambac, peony, neroli, vanilla and sandalwood.</li>
<li><strong>Mon Guerlain Bloom of Rose Eau de Toilette</strong> (5ml): Bulgarian and Turkish rose, lavender, neroli, vanilla and sandalwood.</li>
</ul>
<p>Lavender and vanilla run through all three, so it is an easy way to find the Mon Guerlain that suits you, and a ready-made gift.</p>
<h2>The richer unisex scents: Oud Essentiel and Épices Exquises</h2>
<p>[[oud|Guerlain Oud Essentiel Eau de Parfum]] (125ml) frames oud with saffron and pelargonium at the top, rose and cedarwood in the heart, and leather, frankincense and guaiac wood in the base. For more oud scents, see our <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a>.</p>
<p>[[epices|Guerlain Épices Exquises Eau de Parfum]] (125ml) is built on spice and coffee: cardamom, pink pepper and angelica, then black pepper and coffee, over sandalwood, oud and patchouli. [[musc|Guerlain Musc Noble]], from the same line, is sold out at the moment.</p>
<h2>Which Guerlain perfume should you choose?</h2>
<ul>
<li><strong>For him, a classic:</strong> Habit Rouge.</li>
<li><strong>A rich, creamy floral:</strong> Samsara.</li>
<li><strong>A honeyed floral:</strong> L'Instant de Guerlain.</li>
<li><strong>Light and fruity:</strong> La Petite Robe Noire Ma Robe Cocktail.</li>
<li><strong>To try several, or as a gift:</strong> the Mon Guerlain miniature set.</li>
<li><strong>Deep, smoky and unisex:</strong> Oud Essentiel or Épices Exquises.</li>
</ul>
<h2>Another warm scent in a similar mood</h2>
<p>If you like the amber and vanilla in Habit Rouge or Samsara, try [[amber|Chopard Amber Malaki Eau de Parfum]] (80ml): orange blossom and frankincense, then amber and papyrus, over labdanum and bourbon vanilla. It is a different perfume, not a copy.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum or eau de toilette?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> See our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> and <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/guerlain">Guerlain</a> fragrance, or browse <a href="/collections/perfume-for-women">perfume for women</a> and <a href="/collections/perfume-for-men">perfume for men</a>.</p>""",
    "faq": [
        ["What does Guerlain Habit Rouge smell like?",
         "Habit Rouge Eau de Parfum opens with lemon, bergamot, orange and lime, has rose, jasmine, cinnamon and patchouli in the heart, and settles on leather, vanilla, amber, benzoin and labdanum."],
        ["What is the difference between Samsara and L'Instant de Guerlain?",
         "Samsara is a creamy floral built on sandalwood, with jasmine, rose, narcissus and orris. L'Instant de Guerlain is a honeyed floral, with magnolia, jasmine, ylang-ylang and iris over honey, vanilla and amber."],
        ["What is in the Mon Guerlain miniature set?",
         "Four 5ml bottles: two Mon Guerlain Eau de Parfum, one Mon Guerlain Florale Eau de Parfum and one Mon Guerlain Bloom of Rose Eau de Toilette, 20ml in all."],
        ["Which Guerlain perfumes are unisex?",
         "Of the Guerlain fragrances we stock, Oud Essentiel and Épices Exquises are unisex. Habit Rouge is made for men, and Samsara, L'Instant, La Petite Robe Noire and Mon Guerlain for women."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_guerlain_2026-11-25.jsonl")

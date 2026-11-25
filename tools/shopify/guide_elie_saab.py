"""Journal guide 'Elie Saab perfume: Le Parfum, Intense, Elixir, Nuit Noor and the Essences compared'
(user, 25 Nov 2026: 'Write and Publish All').

Semrush UK: elie saab perfume 5,400, elie saab elixir 480. GSC 4-10 Nov: 'elie saab perfume gift set' / 'gift set'
pos 30-48, No. 1 Rose page pos 7 (1 click). Trends: small, rising into Christmas. 9 Elie Saab in stock with photos
(allp_map 25 Nov); Girl of Now Lovely set sold out: text link only. Facts = stored custom.sw notes + descriptions
(Admin read 25 Nov). The Essences have no stored top notes: 'key note' used, as on their pages. NO PRICES.

Usage: python3 tools/shopify/guide_elie_saab.py <allp_map.json>
Output: docs/seo/guide_elie_saab_2026-11-25.jsonl
"""
import json
import sys

from journal_lib import build

E = "elie-saab-"
A = {
    "title": "Elie Saab perfume: Le Parfum, Intense, Elixir, Nuit Noor and the Essences compared",
    "handle": "elie-saab-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Elie Saab fragrance we stock: Le Parfum, Le Parfum Intense, Bridal, Elixir, Nuit Noor, the two Le Parfum gift sets and La Collection des Essences, with the notes and who each suits.",
    "mt": "Elie Saab Perfume: Le Parfum, Elixir & Gift Sets | Swansura",
    "md": "Elie Saab perfume compared: Le Parfum, Intense, Bridal, Elixir, Nuit Noor, No. 1 Rose and No. 4 Oud, plus the Le Parfum gift sets.",
    "pick": {
        "lp50": E + "le-parfum-eau-de-parfum-50ml-women-s-floral-amber-fragrance",
        "intense": E + "le-parfum-eau-de-parfum-intense-90ml-women-s-floral-amber-fragrance",
        "bridal": E + "le-parfum-bridal-eau-de-parfum-90ml-women-s-floral-amber-fragrance",
        "elixir": E + "elixir-eau-de-parfum-50ml-women-s-floral-amber-fragrance",
        "noor": E + "nuit-noor-eau-de-parfum-90ml-women-s-amber-floral-fragrance",
        "setlp": E + "le-parfum-eau-de-parfum-gift-set-90ml-body-lotion-75ml-shower-gel-75ml-women-s-fragrance-set",
        "setlum": E + "le-parfum-lumiere-eau-de-parfum-gift-set-90ml-10ml-body-lotion-75ml-women-s-fragrance-set",
        "rose": E + "la-collection-des-essences-no-1-rose-eau-de-parfum-100ml-luxury-unisex-rose-fragrance",
        "oud": E + "la-collection-des-essences-no-4-oud-eau-de-parfum-100ml-luxury-unisex-oud-fragrance",
        "gon": E + "girl-of-now-lovely-eau-de-parfum-gift-set-50ml-body-lotion-75ml-new-pack-women-s-fragrance-set",
    },
    "titles": {},
    "soldout": ["gon"],
    "shop": ["lp50", "setlum", "intense", "elixir", "noor", "bridal", "setlp", "rose"],
    "body": """<p><strong>Elie Saab perfume</strong> is built around white flowers, honey and amber, from the bright Le Parfum to the darker Nuit Noor. Here is every Elie Saab fragrance we stock, what is in each one, and which to choose, for yourself or as a gift.</p>
<h2>Elie Saab Le Parfum</h2>
<p>[[lp50|Elie Saab Le Parfum Eau de Parfum]] (50ml) is where to start: orange blossom, then two kinds of jasmine, over cedarwood, patchouli, honey and rose. Bright white flowers with a soft, woody sweetness, it suits daytime and the office.</p>
<h2>Le Parfum Intense and Le Parfum Bridal</h2>
<p>[[intense|Le Parfum Eau de Parfum Intense]] (90ml) is richer and warmer: orange blossom, then ylang-ylang and rose, over honey, amber and patchouli. [[bridal|Le Parfum Bridal]] (90ml) is creamier: orange blossom, neroli and mandarin orange, then gardenia, ylang-ylang and vanilla, over musk, amber and benzoin.</p>
<h2>Elie Saab Elixir</h2>
<p>[[elixir|Elie Saab Elixir Eau de Parfum]] (50ml) pairs mandarin and neroli with rose and powdery iris, over amber, vanilla, musk and woods. Polished by day, warmer as the vanilla and amber come through.</p>
<h2>Elie Saab Nuit Noor</h2>
<p>[[noor|Elie Saab Nuit Noor Eau de Parfum]] (90ml) is the evening scent of the range: black pepper and spices, then rose, jasmine and incense, over patchouli, amber, musk and woods.</p>
<h2>Elie Saab gift sets</h2>
<ul>
<li>[[setlum|Le Parfum Lumière Gift Set]]: a 90ml eau de parfum, a 10ml travel spray and a 75ml body lotion. Mandarin orange, orange blossom and ylang-ylang, then jasmine and tuberose, over patchouli, amber and musk.</li>
<li>[[setlp|Le Parfum Gift Set]]: a 90ml Le Parfum eau de parfum with a 75ml body lotion and a 75ml shower gel.</li>
</ul>
<p>The [[gon|Girl of Now Lovely gift set]] is sold out at the moment. More boxed ideas are in our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</p>
<h2>La Collection des Essences: No. 1 Rose and No. 4 Oud</h2>
<p>These two are unisex and built around a single key note. [[rose|No. 1 Rose]] (100ml) puts rose at the centre, with floral accords over amber, woods and musk. [[oud|No. 4 Oud]] (100ml) is built around oud, with woody accords and spices over amber, resins and musk. For more oud scents, see our <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a>.</p>
<h2>Which Elie Saab perfume should you choose?</h2>
<ul>
<li><strong>Bright white flowers for every day:</strong> Le Parfum.</li>
<li><strong>Richer, with honey and amber:</strong> Le Parfum Intense.</li>
<li><strong>Creamy, with gardenia and vanilla:</strong> Le Parfum Bridal.</li>
<li><strong>Rose and iris:</strong> Elixir.</li>
<li><strong>Dark and spicy, for evenings:</strong> Nuit Noor.</li>
<li><strong>Unisex:</strong> No. 1 Rose or No. 4 Oud.</li>
<li><strong>A gift:</strong> the Le Parfum Lumière or Le Parfum gift set.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>What the labels mean:</strong> read <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a>.</li>
<li><strong>More gifts for her:</strong> see <a href="/collections/perfume-gift-sets-for-her">perfume gift sets for her</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/elie-saab">Elie Saab</a> fragrance, or browse <a href="/collections/perfume-for-women">perfume for women</a>.</p>""",
    "faq": [
        ["What does Elie Saab Le Parfum smell like?",
         "Le Parfum Eau de Parfum opens with orange blossom, has jasmine and grandiflorum jasmine in the heart, and settles on cedarwood, patchouli, honey and rose."],
        ["What is the difference between Le Parfum and Le Parfum Intense?",
         "Le Parfum is brighter, built on orange blossom and jasmine. Le Parfum Intense is warmer, with ylang-ylang and rose over honey, amber and patchouli."],
        ["What is in the Elie Saab gift sets?",
         "The Le Parfum Lumière set holds a 90ml eau de parfum, a 10ml travel spray and a 75ml body lotion. The Le Parfum set holds a 90ml eau de parfum, a 75ml body lotion and a 75ml shower gel."],
        ["Are any Elie Saab perfumes unisex?",
         "Yes: La Collection des Essences No. 1 Rose and No. 4 Oud are unisex. The other Elie Saab fragrances we stock are made for women."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_elie_saab_2026-11-25.jsonl")

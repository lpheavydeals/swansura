"""Journal guide "Issey Miyake L'Eau d'Issey: the original and its newer versions compared"
(user, 17-18 Nov 2026: 'Write and Publish All').

Semrush UK (10 Nov): issey miyake 9,900, l'eau d'issey 8,100. 5 of 8 Issey listings in stock with photos on 18 Nov
(allp_map_1118.json): the original L'Eau d'Issey EDT 50ml (no photo, sold out), Pour Homme EDT (sold out) and Wood & Wood
(no photo, sold out) are named in the text and not linked. Facts = stored notes (custom.sw + description, Admin read
18 Nov). 'Shop the story' filled with 3 in-stock fresh florals (Versace Yellow Diamond, Davidoff Cool Water Reborn
Intense, Versace Eros Pour Femme EDT 5ml). No longevity / 'dupe' / 'iconic' wording, no launch dates.

Usage: python3 tools/shopify/guide_issey.py <allp_map.json>
Output: docs/seo/guide_issey_2026-11-18.jsonl
"""
import json
import sys

from journal_lib import build

I = "issey-miyake-"
A = {
    "title": "Issey Miyake L'Eau d'Issey: the original and its newer versions compared",
    "handle": "issey-miyake-leau-dissey-guide",
    "tag": "Scent Studio",
    "summary": "L'Eau d'Issey and the Issey Miyake fragrances we stock: Eau & Magnolia, Rose & Rose, Pure Pétale de Nectar, A Drop d'Issey and Le Sel d'Issey.",
    "mt": "Issey Miyake L'Eau d'Issey: Versions Compared | Swansura",
    "md": "Issey Miyake L’Eau d’Issey explained: the original notes, Eau and Magnolia, Rose and Rose, Pure Pétale de Nectar and A Drop d’Issey compared.",
    "pick": {
        "magnolia": I + "leau-dissey-eau-magnolia-eau-de-toilette-intense",
        "rose": I + "leau-dissey-rose-rose-eau-de-parfum-intense-90ml",
        "nectar": I + "leau-dissey-pure-petale-de-nectar-eau-de-toilette-90ml",
        "drop": I + "a-drop-dissey-eau-de-parfum-fraiche-90ml",
        "sel": I + "le-sel-dissey-eau-de-toilette-10ml",
        "yellow": "versace-yellow-diamond-eau-de-toilette-90ml",
        "coolwater": "davidoff-cool-water-reborn-intense-eau-de-parfum-50ml-women-s-fresh-floral-fragrance",
        "erosfemme": "versace-eros-pour-femme-eau-de-toilette-miniature-5ml",
    },
    "titles": {},
    "shop": ["magnolia", "rose", "nectar", "drop", "sel", "yellow", "coolwater", "erosfemme"],
    "body": """<p><strong>L'Eau d'Issey</strong> is Issey Miyake's watery floral for women, and over the years it has grown into a whole family: a magnolia version, a rose version, a sweeter nectar version, and the rain-scented A Drop d'Issey. Here is what the original smells like, how each newer version differs, and which Issey Miyake fragrance to choose.</p>
<h2>What does the original L'Eau d'Issey smell like?</h2>
<p>The original L'Eau d'Issey Eau de Toilette is built around water and flowers. Its listed notes open with lotus, rose, freesia, cyclamen, melon and calone (a fresh, watery note), move to lily of the valley, lily, water peony and carnation, and settle on musk, tuberose, woods, osmanthus, cedar, sandalwood and amber. The result is clean and airy rather than sweet. We list the 50ml eau de toilette, which is not available to buy at present; the newer versions below are in stock.</p>
<h2>The newer L'Eau d'Issey versions</h2>
<h3>Eau &amp; Magnolia</h3>
<p>[[magnolia|L'Eau d'Issey Eau &amp; Magnolia Eau de Toilette Intense]] ({{magnolia}}, 50ml or 100ml) is the simplest: bergamot, then magnolia and rose, over sandalwood and musk. A soft, creamy floral that stays close to the original's clean feel.</p>
<h3>Rose &amp; Rose</h3>
<p>[[rose|L'Eau d'Issey Rose &amp; Rose Eau de Parfum Intense]] ({{rose}}, 90ml) is the richest of the family. Raspberry, pear and pink pepper open it; Bulgarian rose, rose and osmanthus fill the heart; and cashmere wood, amber and patchouli make the base. Fruity at first, then a deep, warm rose.</p>
<h3>Pure Pétale de Nectar</h3>
<p>[[nectar|L'Eau d'Issey Pure Pétale de Nectar Eau de Toilette]] ({{nectar}}, 90ml) is the sweetest: pear and honey, then rose and peony, over cashmeran, white musk and sandalwood. A soft, honeyed floral for anyone who finds the original too watery.</p>
<h2>A Drop d'Issey</h2>
<p>[[drop|A Drop d'Issey Eau de Parfum Fraiche]] ({{drop}}, 90ml) opens on a rain accord, like the air after a shower, with lilac and Damask rose in the heart and sandalwood and musk underneath. It keeps the brand's focus on water but with a lighter, cooler feel, and suits spring, summer and the office.</p>
<h2>For him: Le Sel d'Issey</h2>
<p>[[sel|Le Sel d'Issey Eau de Toilette]] ({{sel}}, 10ml) is a fresh men's scent built on sea salt and ginger, with vetiver and sand vetiver in the heart and cedarwood and oakmoss in the base: dry, mineral and slightly spicy. The 10ml size is an easy way to try it. We also list L'Eau d'Issey Pour Homme and Pour Homme Wood &amp; Wood, which are not available at present.</p>
<h2>Which Issey Miyake fragrance should you choose?</h2>
<ul>
<li><strong>Clean and close to the original:</strong> Eau &amp; Magnolia.</li>
<li><strong>A deeper, warmer rose:</strong> Rose &amp; Rose.</li>
<li><strong>Something sweeter and honeyed:</strong> Pure Pétale de Nectar.</li>
<li><strong>Light, cool and fresh:</strong> A Drop d'Issey.</li>
<li><strong>For him:</strong> Le Sel d'Issey.</li>
</ul>
<h2>Other fresh florals to try</h2>
<p>If you like L'Eau d'Issey's watery, airy style, these are different perfumes in a similar mood:</p>
<ul>
<li>[[yellow|Versace Yellow Diamond Eau de Toilette]] ({{yellow}}, 90ml): citron, pear sorbet, neroli and bergamot, then water lily, freesia and mimosa.</li>
<li>[[coolwater|Davidoff Cool Water Reborn Intense Eau de Parfum]] ({{coolwater}}, 50ml): bergamot and green notes, a rose heart, then vetiver, woods and musk.</li>
<li>[[erosfemme|Versace Eros Pour Femme Eau de Toilette Miniature]] ({{erosfemme}}, 5ml): lemon, mandarin, raspberry sorbet and white currant, then freesia, magnolia and jasmine.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de toilette or eau de parfum?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> See our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/issey-miyake">Issey Miyake</a> fragrance, or browse <a href="/collections/scent-floral">floral fragrances</a> and <a href="/collections/perfume-for-women">perfume for women</a>.</p>""",
    "faq": [
        ["What does L'Eau d'Issey smell like?",
         "The original L'Eau d'Issey Eau de Toilette is a watery floral: lotus, rose, freesia, cyclamen, melon and calone at the top, lily of the valley, lily, water peony and carnation in the heart, and musk, tuberose, osmanthus, cedar, sandalwood and amber in the base. It is clean and airy rather than sweet."],
        ["What is the difference between L'Eau d'Issey and Eau & Magnolia?",
         "Eau & Magnolia is a simpler, creamier version: bergamot, then magnolia and rose, over sandalwood and musk. The original has many more notes, including lotus, melon and a watery calone note."],
        ["Which L'Eau d'Issey is the sweetest?",
         "Pure Pétale de Nectar, with pear and honey at the top, rose and peony in the heart and cashmeran, white musk and sandalwood in the base. Rose & Rose is fruity too, with raspberry and pear, but turns into a deeper, warmer rose."],
        ["Is there an Issey Miyake fragrance for men?",
         "Yes. We stock Le Sel d'Issey Eau de Toilette 10ml, a fresh scent with sea salt and ginger, vetiver, cedarwood and oakmoss. We also list L'Eau d'Issey Pour Homme and Wood & Wood, which are not available at present."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_issey_2026-11-18.jsonl")

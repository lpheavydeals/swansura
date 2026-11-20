"""Journal guide 'Acqua di Parma: Colonia, Blu Mediterraneo and the 20ml eau de parfums compared'
(user, 20 Nov 2026: 'Write and Publish All').

Semrush UK: acqua di parma 27,100, acqua di parma perfume 1,000, zafferano 720, sandalo 480, sakura 390, rosa nobile 320.
8 of 9 listings in stock with photos on 20 Nov (allp_map_1120b.json); Oud Spice sold out (text link only). Facts =
stored notes (custom.sw + descriptions, Admin read 20 Nov); the two discovery sets name their scents only (no notes
stored), so they are described by name and the set's own short line. Deodorant: notes only, no effect claims.
NO PRICES in the text (user's 19 Nov decision). No longevity / 'iconic' wording, no launch dates.

Usage: python3 tools/shopify/guide_acqua_di_parma.py <allp_map.json>
Output: docs/seo/guide_acqua_di_parma_2026-11-20.jsonl
"""
import json
import sys

from journal_lib import build

Q = "acqua-di-parma-"
A = {
    "title": "Acqua di Parma: Colonia, Blu Mediterraneo and the 20ml eau de parfums compared",
    "handle": "acqua-di-parma-guide",
    "tag": "Scent Studio",
    "summary": "The Acqua di Parma fragrances we stock: Colonia Pura, Zafferano, Sandalo, Sakura and Rosa Nobile in 20ml, the Blu Mediterraneo and Holiday discovery sets, and the Colonia Essenza deodorant stick.",
    "mt": "Acqua di Parma: Colonia, Zafferano, Sandalo | Swansura",
    "md": "Acqua di Parma Colonia Pura, Zafferano, Sandalo, Sakura, Rosa Nobile, the Blu Mediterraneo and Holiday discovery sets compared: notes and sizes.",
    "pick": {
        "pura": Q + "colonia-pura-eau-de-cologne-20ml-unisex",
        "zaff": Q + "zafferano-edp-20ml-unisex",
        "sandalo": Q + "sandalo-edp-20ml-unisex",
        "sakura": Q + "sakura-edp-20ml-unisex",
        "rosa": Q + "rosa-nobile-edp-20ml-for-women",
        "blu": Q + "blu-mediterraneo-discovery-set-3x12ml",
        "holiday": Q + "holiday-discovery-set-edp-3x12ml",
        "deo": Q + "colonia-essenza-deodorant-stick-75ml",
        "oud": Q + "oud-spice-edp-20ml-for-men",
    },
    "titles": {},
    "soldout": ["oud"],
    "shop": ["pura", "zaff", "sandalo", "sakura", "rosa", "blu", "holiday", "deo"],
    "body": """<p>Acqua di Parma is an Italian house known for its colognes: bright citrus, Italian bergamot and clean, sunny florals. Its range has grown to include warmer eau de parfums and the Mediterranean-inspired Blu Mediterraneo line. Most of what we stock comes in 20ml bottles and 12ml discovery sets, which makes the range easy to try. Here is every <strong>Acqua di Parma</strong> fragrance we stock, with its notes.</p>
<h2>Colonia Pura</h2>
<p>[[pura|Acqua di Parma Colonia Pura Eau de Cologne]] (20ml) is the brand's classic cologne style: Italian bergamot, orange and petitgrain, then jasmine sambac, narcissus and coriander, over musk, cedarwood and patchouli. Fresh and clean, for warm days, the office and anyone who likes a light, citrus scent.</p>
<h2>The 20ml eau de parfums</h2>
<ul>
<li>[[zaff|Zafferano Eau de Parfum]] (20ml, unisex): bergamot, bitter orange, coriander and mandarin, then geranium, jasmine sambac, orange blossom, rose and saffron, over tonka bean, vanilla and woods. Warm, spiced and floral.</li>
<li>[[sandalo|Sandalo Eau de Parfum]] (20ml, unisex): Calabrian bergamot, lemon, orange and petitgrain, then cardamom and lavender, over sandalwood, amber and tonka bean. Citrus over a creamy, woody base.</li>
<li>[[sakura|Sakura Eau de Parfum]] (20ml, unisex): Calabrian bergamot, yellow mandarin and pink pepper, then cherry blossom and jasmine sambac, over musk. Light and floral.</li>
<li>[[rosa|Rosa Nobile Eau de Parfum]] (20ml, for women): bergamot, mandarin and pepper, then Italian rose, lily of the valley, peony and violet, over ambergris and Virginia cedarwood. A fresh, airy rose.</li>
</ul>
<p>[[oud|Oud Spice Eau de Parfum]] (bergamot, raspberry and rose; cinnamon, cloves and pink pepper; agarwood, labdanum and patchouli) is out of stock at present: use Notify me on the page. For more oud scents, see our <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a>.</p>
<h2>The discovery sets</h2>
<ul>
<li>[[blu|Blu Mediterraneo Discovery Set]] (3 x 12ml): Mirto di Panarea (woody aromatic), Arancia di Capri (bright citrus aromatic) and Fico di Amalfi (fresh floral fruity), three takes on the Mediterranean.</li>
<li>[[holiday|Holiday Discovery Set]] (3 x 12ml eau de parfum): Osmanthus, Yuzu and Lily of the Valley, a warm floral, a tart citrus and a green floral.</li>
</ul>
<h2>Colonia Essenza deodorant stick</h2>
<p>The [[deo|Colonia Essenza Deodorant Stick]] (75ml) carries the Colonia Essenza scent: lemon, orange, bergamot, grapefruit, mandarin and petitgrain, then rosemary, rose, jasmine, lily of the valley and clove, over patchouli, white musk and amber. A good add-on for someone who already wears the cologne.</p>
<h2>Which Acqua di Parma should you choose?</h2>
<ul>
<li><strong>A classic fresh cologne:</strong> Colonia Pura.</li>
<li><strong>Warm and spiced:</strong> Zafferano.</li>
<li><strong>Citrus over creamy wood:</strong> Sandalo.</li>
<li><strong>Light and floral:</strong> Sakura, or Rosa Nobile for a fresh rose.</li>
<li><strong>Not sure yet:</strong> one of the 3 x 12ml discovery sets.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Cologne, eau de toilette or eau de parfum?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> See our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> and <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/acqua-di-parma">Acqua di Parma</a> fragrance, or browse <a href="/collections/unisex-perfume">unisex perfume</a> and <a href="/collections/scent-fresh">fresh fragrances</a>.</p>""",
    "faq": [
        ["What does Acqua di Parma Colonia Pura smell like?",
         "Colonia Pura opens with Italian bergamot, orange and petitgrain, has jasmine sambac, narcissus and coriander in the heart, and dries down to musk, cedarwood and patchouli. It is fresh and clean."],
        ["What does Acqua di Parma Zafferano smell like?",
         "Zafferano Eau de Parfum opens with bergamot, bitter orange, coriander and mandarin, has geranium, jasmine, orange blossom, rose and saffron in the heart, and dries down to tonka bean, vanilla and woods. It is warm and spiced."],
        ["Which Acqua di Parma is best for women?",
         "Rosa Nobile is made for women: bergamot, mandarin and pepper, then Italian rose, lily of the valley, peony and violet, over ambergris and cedarwood. Sakura and the other 20ml eau de parfums are unisex."],
        ["Is there an Acqua di Parma discovery set?",
         "Yes, two: the Blu Mediterraneo Discovery Set (Mirto di Panarea, Arancia di Capri and Fico di Amalfi) and the Holiday Discovery Set (Osmanthus, Yuzu and Lily of the Valley), each 3 x 12ml."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_acqua_di_parma_2026-11-20.jsonl")

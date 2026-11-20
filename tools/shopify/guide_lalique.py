"""Journal guide 'Lalique perfume: Amethyst, White, Satine, L'Amour and more compared'
(user, 19-20 Nov 2026: 'Write and Publish All').

Semrush UK: lalique perfume 1,000 (KD 23), lalique amethyst 210, lalique white 170, lalique le parfum 170,
lalique l'amour 50, lalique satine 40. 7 of 12 Lalique listings in stock with photos on 20 Nov (allp_map_1120.json):
Le Parfum + de Lalique sold out (text links only); Lion, L'Insoumis, Hommage set have no photos (named, not linked).
Facts = stored notes in the descriptions (Admin read 20 Nov). 8th card: Miss Armaf Chic (berries + peony), named as a
different perfume. No longevity / 'dupe' / 'iconic' wording, no launch dates.

Usage: python3 tools/shopify/guide_lalique.py <allp_map.json>
Output: docs/seo/guide_lalique_2026-11-20.jsonl
"""
import json
import sys

from journal_lib import build

L = "lalique-"
A = {
    "title": "Lalique perfume: Amethyst, White, Satine, L'Amour and more compared",
    "handle": "lalique-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Lalique fragrance we stock, side by side: Amethyst and Amethyst Éclat, L'Amour, Perles, Satine, White and Noir Premier 1888, with the notes and who each suits.",
    "mt": "Lalique Perfume: Amethyst, White, Satine & More | Swansura",
    "md": "Lalique Amethyst, Amethyst Eclat, L’Amour, Perles, Satine, Le Parfum, White and Noir Premier 1888 compared: the notes and which to choose.",
    "pick": {
        "amethyst": L + "amethyst-eau-de-parfum-100ml",
        "eclat": L + "amethyst-eclat-eau-de-parfum-100ml",
        "amour": L + "lamour-eau-de-parfum-100ml",
        "perles": L + "perles-eau-de-parfum-100ml",
        "satine": L + "satine-eau-de-parfum-100ml",
        "leparfum": L + "le-parfum-eau-de-parfum-100ml",
        "delalique": L + "de-lalique-eau-de-parfum-100ml",
        "white": L + "white-eau-de-toilette-125ml",
        "noir": L + "noir-premier-or-intemporel-1888-eau-de-parfum-100ml",
        "chic": "armaf-miss-armaf-chic-eau-de-parfum-100ml",
    },
    "titles": {},
    "soldout": ["leparfum", "delalique"],
    "shop": ["amethyst", "eclat", "amour", "perles", "satine", "white", "noir", "chic"],
    "body": """<p>Lalique is a French crystal house, and its perfumes come in bottles that carry that heritage. The scents themselves cover a wide range: berry florals, white flowers, warm vanilla ambers and fresh, spicy scents for men. Every <strong>Lalique perfume</strong> we stock is a 100ml or 125ml bottle at around £30. Here they are with their notes and who each one suits.</p>
<h2>Lalique Amethyst and Amethyst Éclat</h2>
<ul>
<li>[[amethyst|Lalique Amethyst Eau de Parfum]] ({{amethyst}}, 100ml) is a berry floral: blackcurrant, blackberry, blueberry, mulberry and strawberry at the top, peony, pepper, ylang-ylang and rose in the heart, and musk, woody notes and Bourbon vanilla in the base. Juicy at first, then a soft, warm rose.</li>
<li>[[eclat|Lalique Amethyst Éclat Eau de Parfum]] ({{eclat}}, 100ml) is the lighter version: raspberry, blackcurrant and pear, then peony, rose and magnolia, over blackberry, musk and violet woodsorrel. Fresher and more floral, with less vanilla.</li>
</ul>
<h2>White flowers: L'Amour</h2>
<p>[[amour|Lalique L'Amour Eau de Parfum]] ({{amour}}, 100ml) opens with bergamot, neroli and rosebuds, centres on gardenia, tuberose and jasmine, and settles on musk, cedarwood and sandalwood. A bright white-flower bouquet, good for spring, summer and weddings.</p>
<h2>Warm and powdery: Perles, Satine and Le Parfum</h2>
<ul>
<li>[[perles|Lalique Perles Eau de Parfum]] ({{perles}}, 100ml): Bulgarian rose and orris, then Bourbon pepper and patchouli, over cashmere wood and tonka bean. A soft, powdery rose.</li>
<li>[[satine|Lalique Satine Eau de Parfum]] ({{satine}}, 100ml): jasmine, gardenia and heliotrope, then vanilla, tonka bean and pink peppercorn, over patchouli, sandalwood and vetiver. Creamy and warm, an evening and winter scent.</li>
<li>[[leparfum|Lalique Le Parfum Eau de Parfum]] (100ml): bay leaf, bergamot and pink peppercorn, then heliotrope and jasmine, over sandalwood, vanilla, patchouli and tonka bean. Out of stock at present: use Notify me on the page.</li>
</ul>
<p>[[delalique|Lalique de Lalique Eau de Parfum]] (jasmine, rose, clove flower and orris; blackberry, pear and blackcurrant leaves; sandalwood, vanilla and white musk) is also out of stock at present.</p>
<h2>For him: Lalique White</h2>
<p>[[white|Lalique White Eau de Toilette]] ({{white}}, 125ml) is a fresh, spicy men's scent: lemon tree leaves, bergamot and mandarin, then white pepper, nutmeg, cardamom and violet, over white cedar, white amber, moss and musk. Crisp for the working week, smart enough for evenings. We also list Lalique Lion, L'Insoumis and the Hommage à l'Homme set, which are not available at present.</p>
<h2>For anyone: Noir Premier Or Intemporel 1888</h2>
<p>[[noir|Lalique Noir Premier Or Intemporel 1888 Eau de Parfum]] ({{noir}}, 100ml) is a unisex amber: bergamot, black pepper and cardamom, then coffee, tobacco and violet, over patchouli, tolu balsam and vanilla. Dark, spiced and warm, for autumn and winter evenings.</p>
<h2>Which Lalique perfume should you choose?</h2>
<ul>
<li><strong>A fruity floral:</strong> Amethyst, or Amethyst Éclat for a lighter take.</li>
<li><strong>A white-flower bouquet:</strong> L'Amour.</li>
<li><strong>A soft, powdery rose:</strong> Perles.</li>
<li><strong>A creamy vanilla scent:</strong> Satine.</li>
<li><strong>For him:</strong> White.</li>
<li><strong>Coffee and tobacco, for anyone:</strong> Noir Premier 1888.</li>
</ul>
<p>If you like Amethyst Éclat's berries and peony, [[chic|Miss Armaf Chic Eau de Parfum]] ({{chic}}, 100ml) pairs raspberry, strawberry, pear and citrus with jasmine, peony and orange blossom over patchouli, cedarwood, musk and vanilla. It is a different perfume, sweeter and juicier.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum or eau de toilette?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> Every Lalique bottle we stock costs under £35: see <a href="/collections/gifts-under-50">gifts under £50</a> and our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/lalique">Lalique</a> fragrance, or browse <a href="/collections/perfume-for-women">perfume for women</a> and <a href="/collections/scent-floral">floral fragrances</a>.</p>""",
    "faq": [
        ["What does Lalique Amethyst smell like?",
         "Lalique Amethyst Eau de Parfum is a berry floral: blackcurrant, blackberry, blueberry, mulberry and strawberry at the top, peony, pepper, ylang-ylang and rose in the heart, and musk, woods and Bourbon vanilla in the base."],
        ["What is the difference between Amethyst and Amethyst Éclat?",
         "Amethyst Éclat is lighter and more floral: raspberry, blackcurrant and pear, then peony, rose and magnolia, over blackberry, musk and violet woodsorrel. The original Amethyst has more berries and a warm Bourbon vanilla base."],
        ["Is there a Lalique perfume for men?",
         "Yes. We stock Lalique White Eau de Toilette 125ml, a fresh, spicy scent with lemon tree leaves, bergamot, white pepper, nutmeg and cardamom over white cedar, white amber, moss and musk. Noir Premier 1888 is unisex."],
        ["Which Lalique perfume is warm and sweet?",
         "Satine, with jasmine, gardenia and heliotrope over vanilla, tonka bean and pink peppercorn and a patchouli, sandalwood and vetiver base. Perles is a softer, powdery rose with tonka bean, and Noir Premier 1888 adds coffee and tobacco."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_lalique_2026-11-20.jsonl")

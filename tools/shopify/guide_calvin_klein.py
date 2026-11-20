"""Journal guide 'Calvin Klein perfume: Defy, Eternity, Euphoria and the 10ml minis compared'
(user, 20 Nov 2026: 'Write and Publish All').

Semrush UK: calvin klein perfume 9,900, calvin klein defy 1,000, calvin klein perfume for men 590, for women 480.
9 of 10 CK listings in stock with photos on 20 Nov (allp_map_1120b.json); the women's 4 x 15ml set (Obsession,
Eternity, CK One) is sold out (text link only), so CK One and Obsession are named there, not sold separately. Eternity
is covered in its own guide (linked, not repeated). Facts = stored notes (custom.sw + descriptions, Admin read 20 Nov).
NO PRICES in the text (user's 19 Nov decision). No longevity / 'iconic' wording.

Usage: python3 tools/shopify/guide_calvin_klein.py <allp_map.json>
Output: docs/seo/guide_calvin_klein_2026-11-20.jsonl
"""
import json
import sys

from journal_lib import build

C = "calvin-klein-"
A = {
    "title": "Calvin Klein perfume: Defy, Eternity, Euphoria and the 10ml minis compared",
    "handle": "calvin-klein-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Calvin Klein fragrance we stock: Defy in three versions, Eternity for women and men, Eternity Aromatic Essence, My Euphoria and the 10ml miniatures.",
    "mt": "Calvin Klein Perfume: Defy, Eternity & Euphoria | Swansura",
    "md": "Calvin Klein Defy Parfum vs Defy EDP, Eternity for women and men, Eternity Aromatic Essence and My Euphoria compared: the notes and sizes.",
    "pick": {
        "defyp": C + "defy-parfum-men-s-warm-woody-fragrance",
        "defyp10": C + "defy-parfum-10ml-miniature-men-s-warm-woody-fragrance",
        "defye10": C + "defy-eau-de-parfum-10ml-miniature-men-s-fresh-woody-fragrance",
        "eterw": C + "eternity-eau-de-parfum-women-s-classic-floral-fragrance",
        "eterm": C + "eternity-for-men-eau-de-toilette-100ml-men-s-fresh-aromatic-fragrance",
        "eterparf": C + "eternity-parfum-10ml-miniature-men-s-warm-aromatic-fragrance",
        "aromw": C + "eternity-aromatic-essence-parfum-intense-10ml-miniature-women-s-aromatic-floral-fragrance",
        "aromm": C + "eternity-aromatic-essence-parfum-intense-10ml-miniature-men-s-aromatic-woody-fragrance",
        "euph": C + "my-euphoria-eau-de-parfum-10ml-miniature-women-s-floral-gourmand-fragrance",
        "set": C + "women-s-miniature-fragrance-set-4x15ml-obsession-eternity-ck-one",
    },
    "titles": {},
    "soldout": ["set"],
    "shop": ["defyp", "eterw", "eterm", "euph", "defye10", "eterparf", "aromw", "aromm"],
    "body": """<p>Calvin Klein fragrances are clean and wearable: lavender and woods for men, fresh florals for women, with a few warmer, sweeter choices. We stock Defy, Eternity, Eternity Aromatic Essence and My Euphoria, many as 10ml miniatures that make easy stocking fillers. Here is every <strong>Calvin Klein perfume</strong> we stock, with its notes.</p>
<h2>Calvin Klein Defy: three versions</h2>
<ul>
<li>[[defyp|Calvin Klein Defy Parfum]] (200ml; the 50ml is out of stock at present): mandarin and pink pepper, then lavender and a suede accord, over vetiver, amber and woods. Warm and smooth.</li>
<li>[[defyp10|Defy Parfum 10ml Miniature]]: the same Parfum in a travel spray.</li>
<li>[[defye10|Defy Eau de Parfum 10ml Miniature]]: mandarin and black pepper, then lavender and leather, over vetiver and amber. Fresher and a little sharper than the Parfum.</li>
</ul>
<p><strong>Defy Parfum or Defy Eau de Parfum?</strong> The Parfum has pink pepper and soft suede; the eau de parfum has black pepper and leather. A parfum holds a higher share of fragrance oils; our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</p>
<h2>Calvin Klein Eternity</h2>
<ul>
<li>[[eterw|Eternity Eau de Parfum]] (30ml or 100ml, for women): freesia, mandarin and sage, then lily, carnation, violet, jasmine and rose, over sandalwood, amber and musk. A clean, classic floral.</li>
<li>[[eterm|Eternity for Men Eau de Toilette]] (100ml): mandarin, lavender, bergamot and lemon, then sage, juniper, basil and geranium, over sandalwood, vetiver and musk. Fresh and aromatic.</li>
<li>[[eterparf|Eternity Parfum 10ml Miniature]] (for men): lavender and rum, warm spices, over vanilla, woods and amber. Warmer and sweeter.</li>
</ul>
<p>Our guide to <a href="/blogs/journal/calvin-klein-eternity-for-women-vs-for-men">Calvin Klein Eternity for women vs for men</a> compares them in detail.</p>
<h2>Eternity Aromatic Essence</h2>
<p>Two 10ml Parfum Intense miniatures with a coconut twist:</p>
<ul>
<li>[[aromw|Eternity Aromatic Essence for women]]: lavender and fresh aromatic notes, then a floral accord and coconut, over amber, woods and musk.</li>
<li>[[aromm|Eternity Aromatic Essence for men]]: juniper berry and fresh aromatic notes, then lavender and a coconut accord, over cardamom, woods and amber.</li>
</ul>
<h2>My Euphoria</h2>
<p>[[euph|Calvin Klein My Euphoria Eau de Parfum 10ml Miniature]] is the sweetest Calvin Klein we stock: blackcurrant and pink pepper, then orchid, rose and jasmine, over vanilla, amber and woods. A warm floral for evenings.</p>
<p>CK One and Obsession come in the [[set|Calvin Klein Women's Miniature Fragrance Set]] (4 x 15ml), which is out of stock at present: use Notify me on the page.</p>
<h2>Which Calvin Klein perfume should you choose?</h2>
<ul>
<li><strong>A warm, smooth scent for him:</strong> Defy Parfum.</li>
<li><strong>Fresh and aromatic for him:</strong> Eternity for Men.</li>
<li><strong>A clean, classic floral for her:</strong> Eternity Eau de Parfum.</li>
<li><strong>Something sweeter for her:</strong> My Euphoria.</li>
<li><strong>Not sure yet:</strong> one of the 10ml miniatures.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>The 10ml miniatures</strong> make easy stocking fillers: see our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> and <a href="/blogs/journal/stocking-fillers-for-her-under-25">stocking fillers guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/calvin-klein">Calvin Klein</a> fragrance, or browse <a href="/collections/perfume-for-men">perfume for men</a> and <a href="/collections/perfume-for-women">perfume for women</a>.</p>""",
    "faq": [
        ["What does Calvin Klein Defy smell like?",
         "Defy Parfum opens with mandarin and pink pepper, has lavender and a suede accord in the heart, and dries down to vetiver, amber and woods. Defy Eau de Parfum swaps in black pepper and leather and feels fresher."],
        ["Is Calvin Klein Eternity for men or women?",
         "Both, as different perfumes. Eternity Eau de Parfum for women is a clean floral with freesia, lily, jasmine and rose. Eternity for Men Eau de Toilette is fresh and aromatic, with lavender, sage, juniper and basil."],
        ["What does Calvin Klein My Euphoria smell like?",
         "My Euphoria Eau de Parfum opens with blackcurrant and pink pepper, has orchid, rose and jasmine in the heart, and dries down to vanilla, amber and woods. It is warm and sweet."],
        ["Do you sell CK One?",
         "CK One Eau de Toilette is in our Calvin Klein Women's Miniature Fragrance Set (4 x 15ml) with Obsession and Eternity, which is out of stock at present. We do not stock a full bottle of CK One."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_calvin_klein_2026-11-20.jsonl")

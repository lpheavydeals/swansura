"""Journal guide 'Narciso Rodriguez perfume: For Her, Musc Noir, All of Me and Bleu Noir compared'
(user, 17-18 Nov 2026: 'Write and Publish All').

Semrush UK (10 Nov): narciso rodriguez for her 14,800 (KD 26), narciso rodriguez perfume 2,400 (KD 32),
narciso rodriguez for him bleu noir 260, pure musc for her 210, musc noir for her 40.
7 of 9 Narciso listings in stock with photos on 18 Nov (allp_map_1118.json): the For Her EDP is sold out (linked in the
text only) and the For Her EDT has no photo (named, not linked). Facts = stored notes (custom.sw + description, Admin
read 18 Nov). 8th 'Shop the story' product: Attar Collection Floral Musk (white musk in its stored notes).
No longevity / 'dupe' / 'iconic' wording. Prices are written into the text: re-run and update if prices change.

Usage: python3 tools/shopify/guide_narciso.py <allp_map.json>
Output: docs/seo/guide_narciso_2026-11-18.jsonl
"""
import json
import sys

from journal_lib import build

N = "narciso-rodriguez-"
A = {
    "title": "Narciso Rodriguez perfume: For Her, Musc Noir, All of Me and Bleu Noir compared",
    "handle": "narciso-rodriguez-perfume-guide",
    "tag": "Scent Studio",
    "summary": "The Narciso Rodriguez fragrances we stock, side by side: For Her, Pure Musc, Musc Noir and Musc Noir Rose, Narciso Cristal and Ambree, All of Me and For Him Bleu Noir.",
    "mt": "Narciso Rodriguez For Her, Musc Noir & More | Swansura",
    "md": "Narciso Rodriguez For Her, Pure Musc, Musc Noir, All of Me, Cristal, Ambree and Bleu Noir compared: the notes, sizes and which to choose.",
    "pick": {
        "forher": N + "for-her-eau-de-parfum",
        "pure": N + "pure-musc-for-her-eau-de-parfum-10ml",
        "noir": N + "musc-noir-for-her-eau-de-parfum",
        "noirrose": N + "musc-noir-rose-for-her-eau-de-parfum-10ml",
        "cristal": N + "narciso-cristal-eau-de-parfum-10ml",
        "ambree": N + "narciso-ambree-eau-de-parfum-10ml",
        "allofme": N + "all-of-me-eau-de-parfum-90ml",
        "bleunoir": N + "for-him-bleu-noir-eau-de-toilette-50ml",
        "attar": "attar-collection-floral-musk-eau-de-parfum-100ml",
    },
    "titles": {},
    "soldout": ["forher"],
    "shop": ["allofme", "noir", "pure", "noirrose", "cristal", "ambree", "bleunoir", "attar"],
    "body": """<p>Narciso Rodriguez fragrances are built around one note above all: musk. Each line wraps it in something different, from peach and rose to plum and suede or white flowers. Here is every <strong>Narciso Rodriguez perfume</strong> we stock, with its notes, the sizes on offer and who each one suits.</p>
<h2>Narciso Rodriguez For Her</h2>
<p><strong>Narciso Rodriguez For Her</strong> is the one most people search for, and it comes in two versions with different notes:</p>
<ul>
<li>[[forher|For Her Eau de Parfum]] ({{forher}}, 10ml or 50ml): rose and peach, then musk and amber, over patchouli and sandalwood. Soft, warm and rosy. Currently out of stock: use Notify me on the page and we will email you when it is back.</li>
<li><strong>For Her Eau de Toilette</strong> (50ml or 100ml): African orange flower, osmanthus and bergamot, then musk and amber, over vetiver, vanilla and patchouli. Brighter and more floral at the start. Not available to buy at present.</li>
</ul>
<h2>The musk family: Pure Musc, Musc Noir and Musc Noir Rose</h2>
<ul>
<li>[[pure|Pure Musc For Her Eau de Parfum]] ({{pure}}, 10ml): jasmine and orange blossom, then musk, over cashmeran. The cleanest and simplest of the line, a gentle, skin-like musk for every day.</li>
<li>[[noir|Musc Noir For Her Eau de Parfum]] ({{noir}}, 10ml or 50ml): plum, then musk and heliotrope, over suede. Darker and more velvety, a good autumn and winter choice.</li>
<li>[[noirrose|Musc Noir Rose For Her Eau de Parfum]] ({{noirrose}}, 10ml): bergamot and pink peppercorn, then musk and tuberose, over vanilla, patchouli and suede leather. A floral, slightly spicy take on Musc Noir.</li>
</ul>
<h2>Narciso Cristal and Narciso Ambree</h2>
<p>Both are 10ml eau de parfums at {{cristal}}:</p>
<ul>
<li>[[cristal|Narciso Cristal]]: freesia, orange blossom and bergamot, then rose, jasmine and musk, over cashmeran, cedar, benzoin and amber. Bright and floral.</li>
<li>[[ambree|Narciso Ambree]]: frangipani, ylang-ylang and white flowers, then musk and amber, over cashmeran, cedar and vanilla. Warmer and creamier.</li>
</ul>
<h2>Narciso Rodriguez All of Me</h2>
<p>[[allofme|All of Me Eau de Parfum]] ({{allofme}}, 90ml) opens on magnolia, with rose and Bourbon geranium in the heart and musk and sandalwood in the base. Geranium gives the rose a fresh, slightly green lift, so it reads clean and polished rather than sweet. An easy everyday signature for any season.</p>
<h2>For Him Bleu Noir</h2>
<p>[[bleunoir|For Him Bleu Noir Eau de Toilette]] ({{bleunoir}}, 50ml) is the Narciso for men: cardamom and nutmeg, then musk, over vetiver, cedarwood, ebony wood and amber. Spiced and woody, it works at the office and through the cooler months.</p>
<h2>Which Narciso Rodriguez perfume should you choose?</h2>
<ul>
<li><strong>A soft, rosy musk:</strong> For Her Eau de Parfum.</li>
<li><strong>The cleanest musk:</strong> Pure Musc For Her.</li>
<li><strong>A darker, velvety musk for winter:</strong> Musc Noir, or Musc Noir Rose for a floral version.</li>
<li><strong>A fresh, polished floral:</strong> All of Me.</li>
<li><strong>A creamy white-flower scent:</strong> Narciso Ambree.</li>
<li><strong>For him:</strong> For Him Bleu Noir.</li>
<li><strong>Not sure yet:</strong> the 10ml sizes at {{pure}} let you try one before a bigger bottle, and make easy stocking fillers.</li>
</ul>
<p>If musk is what you love, [[attar|Attar Collection Floral Musk Eau de Parfum]] ({{attar}}, 100ml, unisex) pairs tagetes and jasmine with amber, caramel and white musk over sandalwood and myrrh. It is a different perfume, warmer and sweeter than the Narciso musks.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum or eau de toilette?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> See our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> and <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/narciso-rodriguez">Narciso Rodriguez</a> fragrance, or browse <a href="/collections/perfume-for-women">perfume for women</a>.</p>""",
    "faq": [
        ["What does Narciso Rodriguez For Her smell like?",
         "The For Her Eau de Parfum opens with rose and peach, has musk and amber in the heart, and dries down to patchouli and sandalwood. The eau de toilette is brighter, with African orange flower, osmanthus and bergamot over musk, amber, vetiver, vanilla and patchouli."],
        ["What is the difference between Pure Musc and Musc Noir?",
         "Pure Musc For Her is the cleanest: jasmine and orange blossom over musk and cashmeran. Musc Noir For Her is darker, with plum, musk and heliotrope over suede. Musc Noir Rose adds bergamot, pink peppercorn and tuberose over vanilla, patchouli and suede leather."],
        ["Which Narciso Rodriguez perfume is best for everyday wear?",
         "All of Me and Pure Musc For Her are the easiest for every day. All of Me is a fresh, polished floral with magnolia, rose and geranium over musk and sandalwood; Pure Musc is a soft, clean musk with jasmine and orange blossom."],
        ["Is there a Narciso Rodriguez perfume for men?",
         "Yes. We stock Narciso Rodriguez For Him Bleu Noir Eau de Toilette 50ml: cardamom and nutmeg, then musk, over vetiver, cedarwood, ebony wood and amber."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_narciso_2026-11-18.jsonl")

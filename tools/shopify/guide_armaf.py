"""Journal guide 'Armaf Club de Nuit: Intense, Precieux and the Private Key extraits compared'
(user, 19-20 Nov 2026: 'Write and Publish All').

Semrush UK: armaf club de nuit precieux 590 (KD 16), armaf club de nuit intense 480 (KD 12), Private Key line ~20 each.
8 of 9 Club de Nuit listings in stock with photos on 20 Nov (allp_map_1120.json); the men's gift set is sold out
(text link only). Our 'Club de Nuit Intense Eau de Parfum 105ml' listing carries the Intense Woman notes (same as the
Intense Woman in the women's gift set) and is labelled for women: said plainly (client still to confirm the bottle).
Facts = stored notes in the descriptions (Admin read 20 Nov). No longevity / projection / 'dupe' / 'clone' wording.

Usage: python3 tools/shopify/guide_armaf.py <allp_map.json>
Output: docs/seo/guide_armaf_2026-11-20.jsonl
"""
import json
import sys

from journal_lib import build

C = "armaf-club-de-nuit-"
A = {
    "title": "Armaf Club de Nuit: Intense, Precieux and the Private Key extraits compared",
    "handle": "armaf-club-de-nuit-guide",
    "tag": "Scent Studio",
    "summary": "The Armaf Club de Nuit fragrances we stock, side by side: Club de Nuit Intense, Precieux, Woman, the five Private Key extraits and the gift sets.",
    "mt": "Armaf Club de Nuit Intense, Precieux, Private Key | Swansura",
    "md": "Armaf Club de Nuit Intense, Precieux, Woman and the five Private Key extraits compared: the notes, sizes, gift sets and which to choose.",
    "pick": {
        "intense": C + "intense-eau-de-parfum-105ml",
        "precieux": C + "precieux-extrait-de-parfum-55ml",
        "success": C + "private-key-to-my-success-extrait-de-parfum-100ml",
        "dreams": C + "private-key-to-my-dreams-extrait-de-parfum-100ml",
        "love": C + "private-key-to-my-love-extrait-de-parfum-100ml",
        "life": C + "private-key-to-my-life-extrait-de-parfum-100ml",
        "soul": C + "private-key-to-my-soul-extrait-de-parfum-100ml",
        "woman": C + "woman-eau-de-parfum-travel-set-2-x-12ml",
        "wset": C + "womens-parfum-gift-set-woman-intense-woman-milestone-3-x-30ml",
        "mset": C + "mens-parfum-gift-set-intense-man-sillage-milestone-3-x-30ml",
    },
    "titles": {},
    "soldout": ["mset"],
    "shop": ["intense", "precieux", "success", "dreams", "love", "life", "soul", "woman"],
    "body": """<p>Armaf is a fragrance house from the United Arab Emirates, and Club de Nuit is its best-known line. It now covers far more than one bottle: the Intense scents for men and women, the Woman eau de parfum, the Precieux extrait and the five Private Key extraits. Here is every <strong>Armaf Club de Nuit</strong> fragrance we stock, with its notes, the sizes on offer and who each one suits.</p>
<h2>Club de Nuit Intense: which one do we stock?</h2>
<p>There are two Club de Nuit Intense scents, one for men and one for women, with very different notes. The [[intense|Armaf Club de Nuit Intense Eau de Parfum]] ({{intense}}, 105ml) we stock is the women's version: rose, saffron and geranium at the top, nutmeg, pepper, violet and caraway in the heart, and patchouli, agarwood (oud), vanilla and amber in the base. Spiced rose over a warm, resinous base, for evenings and the colder months. Its notes are the same as the Intense Woman in the women's gift set below.</p>
<p>The men's Club de Nuit Intense Man (lemon, pineapple, bergamot, blackcurrant and apple; birch, jasmine and rose; musk, ambergris, patchouli and vanilla) is in the [[mset|Club de Nuit Men's Parfum Gift Set]], which is out of stock at present: use Notify me on the page and we will email you when it is back.</p>
<h2>Club de Nuit Precieux</h2>
<p>[[precieux|Armaf Club de Nuit Precieux Extrait de Parfum]] ({{precieux}}, 55ml) is unisex and the sweetest of the line: pineapple, caramel, pear, pink pepper, bergamot and lemon at the top, oakmoss, white wood, jasmine, anise and lily of the valley in the heart, and ambergris, vanilla, leather, cedar, patchouli and white musk in the base. Fruity and gourmand at first, then smooth and leathery.</p>
<h2>The Private Key extraits</h2>
<p>The five Private Key scents are unisex extraits de parfum in 100ml bottles at {{success}} each. An extrait holds a higher share of fragrance oils than an eau de parfum; our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</p>
<ul>
<li>[[success|Private Key To My Success]]: ginger, bergamot and red chilli pepper, then spices and lavender, over akigalawood and vetiver. Spicy and woody.</li>
<li>[[dreams|Private Key To My Dreams]]: pink pepper, cardamom, pineapple leaf and black pepper, then lavender, orange blossom, Bourbon geranium and apple, over leather, vanilla absolute, cedarwood, patchouli and vetiver. Spiced leather and vanilla.</li>
<li>[[love|Private Key To My Love]]: peach, pear, passionfruit and cassis, then lily of the valley, white wood and amberwood, over musk, sandalwood, patchouli and vanilla. Fruity and soft.</li>
<li>[[life|Private Key To My Life]]: a long citrus and fruit opening (pink pepper, grapefruit, bergamot, lemon, lime, melon, pineapple, plum), then white flowers, lily of the valley, freesia, rose, jasmine and magnolia, over white musk, woods, patchouli, amber and leather. Bright and floral.</li>
<li>[[soul|Private Key To My Soul]]: grapefruit and mandarin, then sage and lavender, over vanilla. The simplest of the five: fresh herbs and vanilla.</li>
</ul>
<h2>Club de Nuit Woman and the gift sets</h2>
<ul>
<li>[[woman|Club de Nuit Woman Eau de Parfum Travel Set]] ({{woman}}, 2 x 12ml): bergamot, grapefruit, peach and orange, then geranium, jasmine, litchi and rose, over musk, patchouli, vanilla and vetiver. A fruity rose, in two handbag sprays.</li>
<li>[[wset|Club de Nuit Women's Parfum Gift Set]] ({{wset}}, 3 x 30ml): Club de Nuit Woman, Intense Woman and Milestone (sea notes, red fruits and bergamot; violet, white woods and sandalwood; ambroxan, musk and vetiver).</li>
</ul>
<h2>Which Club de Nuit should you choose?</h2>
<ul>
<li><strong>A spiced rose with oud, for her:</strong> Club de Nuit Intense (the women's version we stock).</li>
<li><strong>Sweet, fruity and leathery, for anyone:</strong> Precieux.</li>
<li><strong>Spicy and woody:</strong> Private Key To My Success.</li>
<li><strong>Leather and vanilla:</strong> Private Key To My Dreams.</li>
<li><strong>Soft and fruity:</strong> Private Key To My Love.</li>
<li><strong>Fresh herbs and vanilla:</strong> Private Key To My Soul.</li>
<li><strong>A gift, or not sure yet:</strong> the women's 3 x 30ml set or the 2 x 12ml travel set.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>More Arabian perfume:</strong> see our <a href="/blogs/journal/lattafa-khamrah-qahwa-arabian-perfume">Arabian perfume guide</a> and <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a>.</li>
<li><strong>Buying a gift?</strong> Our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a> has more ideas.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/armaf">Armaf</a> fragrance, or browse <a href="/collections/arabian-perfume">Arabian perfume</a> and <a href="/collections/unisex-perfume">unisex perfume</a>.</p>""",
    "faq": [
        ["What does Armaf Club de Nuit Intense smell like?",
         "There are two. The women's Intense, which we stock in 105ml, has rose, saffron and geranium, then nutmeg, pepper, violet and caraway, over patchouli, agarwood (oud), vanilla and amber. The men's Intense Man has lemon, pineapple, bergamot, blackcurrant and apple over birch, musk, ambergris, patchouli and vanilla."],
        ["What does Armaf Club de Nuit Precieux smell like?",
         "Precieux Extrait de Parfum opens with pineapple, caramel, pear, pink pepper, bergamot and lemon, has oakmoss, white wood, jasmine, anise and lily of the valley in the heart, and dries down to ambergris, vanilla, leather, cedar, patchouli and white musk."],
        ["What are the Armaf Private Key perfumes?",
         "Five unisex extraits de parfum in 100ml: To My Success (spicy and woody), To My Dreams (leather and vanilla), To My Love (fruity and soft), To My Life (bright citrus and florals) and To My Soul (grapefruit, sage, lavender and vanilla)."],
        ["Is Armaf Club de Nuit for men or women?",
         "Both. The line has men's scents (Intense Man), women's scents (Woman and Intense Woman) and unisex extraits (Precieux and the Private Key range). The Club de Nuit Intense we stock in 105ml is the women's version."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_armaf_2026-11-20.jsonl")

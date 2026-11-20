"""Journal guide 'Dolce & Gabbana perfume: The One, Devotion, Q, K and Light Blue compared'
(user, 19-20 Nov 2026: 'Write and Publish All').

Semrush UK: dolce & gabbana perfume 1,300, dolce & gabbana the one 720, the one for men 480, the one edp 390,
devotion 260. 10 of 12 D&G listings in stock with photos on 20 Nov (allp_map_1120.json): The One for Women set and
L'Imperatrice sold out (text links only). Light Blue is only in the two miniature sets (said plainly). Facts = stored
notes (custom.sw + descriptions, Admin read 20 Nov). No longevity / 'dupe' / 'iconic' wording, no launch dates.

Usage: python3 tools/shopify/guide_dolce_gabbana.py <allp_map.json>
Output: docs/seo/guide_dolce_gabbana_2026-11-20.jsonl
"""
import json
import sys

from journal_lib import build

D = "dolce-gabbana-"
A = {
    "title": "Dolce & Gabbana perfume: The One, Devotion, Q, K and Light Blue compared",
    "handle": "dolce-gabbana-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Dolce & Gabbana fragrance we stock, side by side: The One for Men in three versions, K, Devotion, Q and the miniature sets with Light Blue.",
    "mt": "Dolce & Gabbana Perfume: The One, Devotion, Q | Swansura",
    "md": "Dolce & Gabbana The One for Men EDP, Intense and Gold, K, Devotion, Q and Light Blue in the mini sets compared: notes, sizes and which to choose.",
    "pick": {
        "one": D + "the-one-for-men-eau-de-parfum-100ml-luxury-men-s-fragrance",
        "one150": D + "the-one-for-men-eau-de-parfum-150ml-luxury-men-s-fragrance",
        "intense": D + "the-one-for-men-eau-de-parfum-intense-100ml-luxury-men-s-fragrance",
        "gold": D + "the-one-gold-for-men-eau-de-parfum-intense-100ml-luxury-men-s-fragrance",
        "k": D + "k-eau-de-parfum-gift-set-50ml-5ml-men-s-fragrance-set",
        "devotion": D + "devotion-eau-de-parfum-100ml-luxury-women-s-gourmand-fragrance",
        "devset": D + "devotion-eau-de-parfum-gift-set-50ml-10ml-women-s-fragrance-set",
        "q": D + "q-eau-de-parfum-100ml-luxury-women-s-fruity-floral-fragrance",
        "onewomen": D + "the-one-for-women-eau-de-parfum-gift-set-50ml-50ml-luxury-women-s-fragrance-set",
        "imperatrice": D + "l-imperatrice-eau-de-toilette-100ml-women-s-fruity-floral-fragrance",
        "miniw": D + "women-s-miniature-fragrance-set-devotion-q-blue-jasmine-the-one-light-blue",
        "minim": D + "men-s-miniature-fragrance-set-devotion-k-edt-k-edp-the-one-light-blue-pour-homme",
    },
    "titles": {},
    "soldout": ["onewomen", "imperatrice"],
    "shop": ["one", "intense", "gold", "k", "devotion", "q", "miniw", "minim"],
    "body": """<p>Dolce &amp; Gabbana fragrances lean warm and Mediterranean: Sicilian citrus, orange blossom and spice over tobacco, amber and woods. The One is the line most people search for, but the house also makes the fresh, herbal K for men and the sweet Devotion and fruity Q for women. Here is every <strong>Dolce &amp; Gabbana perfume</strong> we stock, with its notes, the sizes on offer and who each one suits.</p>
<h2>The One for Men: three versions</h2>
<p>The One for Men comes in three strengths with different notes, so it is worth knowing which is which:</p>
<ul>
<li>[[one|The One for Men Eau de Parfum]] ({{one}}, 100ml, or [[one150|150ml]] at {{one150}}): grapefruit, coriander and basil, then cardamom, ginger and orange blossom, over tobacco, amber and cedarwood. Spicy and warm, with a smooth tobacco base.</li>
<li>[[intense|The One for Men Eau de Parfum Intense]] ({{intense}}, 100ml): neroli, cardamom and cypress, then cashmeran, benzoin and clary sage, over leather, labdanum and patchouli. Darker and more resinous, with leather in place of tobacco.</li>
<li>[[gold|The One Gold for Men Eau de Parfum Intense]] ({{gold}}, 100ml): blood orange, Sicilian bergamot and ginger, then clary sage, cardamom and geranium, over amberwood, patchouli and vetiver. Brighter at the start and woodier at the end.</li>
</ul>
<p><strong>Which The One for him?</strong> The eau de parfum for a warm, tobacco-spice scent; the Intense for something darker with leather; The One Gold for a citrus start and a woody finish. All three suit evenings and the colder months.</p>
<h2>K by Dolce &amp; Gabbana</h2>
<p>The [[k|K Eau de Parfum Gift Set]] ({{k}}, 50ml plus a 5ml travel spray) is the fresher choice for men: blood orange, Sicilian lemon and juniper berries, then clary sage, geranium, lavender and fig nectar, over cedarwood, vetiver, patchouli and nagarmotha. Herbal and citrusy, it works for the office and the daytime.</p>
<h2>Devotion</h2>
<p>[[devotion|Devotion Eau de Parfum]] ({{devotion}}, 100ml) is a gourmand for women with a short, clear list: candied citrus at the top, orange blossom in the heart and Madagascar vanilla in the base. Sweet, warm and creamy. The [[devset|Devotion Eau de Parfum Gift Set]] ({{devset}}) pairs a 50ml bottle with a 10ml travel spray.</p>
<h2>Q by Dolce &amp; Gabbana</h2>
<p>[[q|Q Eau de Parfum]] ({{q}}, 100ml) is a fruity floral: Sicilian lemon, blood orange and jasmine, then cherry and heliotrope, over cedarwood and musk. Bright and juicy at first, softer and powdery later.</p>
<h2>The One for Women and L'Imperatrice</h2>
<p>[[onewomen|The One for Women Eau de Parfum Gift Set]] (peach, lychee, mandarin and bergamot; lily, plum and jasmine; vanilla, amber, musk and vetiver) and [[imperatrice|L'Imperatrice Eau de Toilette]] (kiwi, rhubarb and pink pepper; watermelon, cyclamen and jasmine; musk, sandalwood and lemon tree) are out of stock at present: use Notify me on the page and we will email you when they are back.</p>
<h2>Light Blue and the miniature sets</h2>
<p>We do not stock a full bottle of Light Blue at present, but it is in both miniature sets, which are also the easiest way to try the range:</p>
<ul>
<li>[[miniw|Women's Miniature Fragrance Set]] ({{miniw}}): Devotion, Q, Blue Jasmine (fig, jasmine sambac, cedarwood) and The One in 5ml, plus Light Blue Eau de Toilette 4.5ml (Sicilian lemon, apple, jasmine, cedarwood, musk).</li>
<li>[[minim|Men's Miniature Fragrance Set]] ({{minim}}): Devotion, K Eau de Toilette, K Eau de Parfum and The One in 5ml, plus Light Blue Pour Homme Eau de Toilette (citrus, juniper, rosemary, musk, woods).</li>
</ul>
<h2>Which Dolce &amp; Gabbana perfume should you choose?</h2>
<ul>
<li><strong>A warm, spicy scent for him:</strong> The One for Men Eau de Parfum.</li>
<li><strong>Darker, with leather:</strong> The One for Men Intense.</li>
<li><strong>Fresh and herbal for him:</strong> K.</li>
<li><strong>A sweet vanilla scent for her:</strong> Devotion.</li>
<li><strong>A fruity floral for her:</strong> Q.</li>
<li><strong>Light Blue, or not sure yet:</strong> one of the miniature sets.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum, intense or eau de toilette?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> See our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> and <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/dolce-gabbana">Dolce &amp; Gabbana</a> fragrance, or browse <a href="/collections/perfume-for-men">perfume for men</a> and <a href="/collections/perfume-for-women">perfume for women</a>.</p>""",
    "faq": [
        ["What does Dolce & Gabbana The One for Men smell like?",
         "The eau de parfum opens with grapefruit, coriander and basil, has cardamom, ginger and orange blossom in the heart, and dries down to tobacco, amber and cedarwood. It is warm and spicy."],
        ["What is the difference between The One for Men EDP and Intense?",
         "The eau de parfum has a tobacco, amber and cedarwood base. The Intense is darker: neroli, cardamom and cypress, then cashmeran, benzoin and clary sage, over leather, labdanum and patchouli. The One Gold is a third version, with blood orange and ginger over amberwood, patchouli and vetiver."],
        ["What does Dolce & Gabbana Devotion smell like?",
         "Devotion Eau de Parfum is a sweet gourmand: candied citrus at the top, orange blossom in the heart and Madagascar vanilla in the base."],
        ["Do you sell Dolce & Gabbana Light Blue?",
         "Not as a full bottle at present. Light Blue Eau de Toilette 4.5ml is in the women's miniature set, and Light Blue Pour Homme is in the men's miniature set."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_dolce_gabbana_2026-11-20.jsonl")

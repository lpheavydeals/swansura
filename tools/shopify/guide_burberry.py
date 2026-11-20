"""Journal guide 'Burberry perfume: My Burberry, My Burberry Black and the Her mini set compared'
(user, 20 Nov 2026: 'Write and Publish All').

Semrush UK: burberry perfume 14,800, burberry perfume for women 880. All 5 Burberry listings in stock with photos on
20 Nov (allp_map_1120b.json). Facts = stored notes (custom.sw + descriptions, Admin read 20 Nov); Her, Her EDT and
Her London Dream only in the mini set (notes from its text). 3 more cards = women's scents in a similar mood
(Chloe Rose Naturelle Intense, Lalique Perles, D&G Devotion), named as different perfumes.
NO PRICES in the text (user's 19 Nov decision). No longevity / 'iconic' wording.

Usage: python3 tools/shopify/guide_burberry.py <allp_map.json>
Output: docs/seo/guide_burberry_2026-11-20.jsonl
"""
import json
import sys

from journal_lib import build

B = "burberry-"
A = {
    "title": "Burberry perfume: My Burberry, My Burberry Black and the Her mini set compared",
    "handle": "burberry-perfume-guide",
    "tag": "Scent Studio",
    "summary": "The Burberry fragrances we stock: My Burberry Eau de Parfum, My Burberry Black Parfum and the Burberry Her miniature set, with the notes and who each suits.",
    "mt": "Burberry Perfume: My Burberry, Black & Her | Swansura",
    "md": "My Burberry Eau de Parfum vs My Burberry Black Parfum, and the Burberry Her miniature set with Her London Dream: the notes, sizes and gifts.",
    "pick": {
        "my50": B + "my-burberry-eau-de-parfum-50ml-women-s-floral-fragrance",
        "my90": B + "my-burberry-eau-de-parfum-90ml-women-s-floral-fragrance",
        "black50": B + "my-burberry-black-parfum-50ml-women-s-rich-floral-amber-fragrance",
        "black90": B + "my-burberry-black-parfum-90ml-women-s-rich-floral-amber-fragrance",
        "her": B + "women-s-miniature-perfume-set-4x5ml-her-london-dream-her-edt-her-edp",
        "rose": "chloe-rose-naturelle-intense-eau-de-parfum-50ml-women-s-floral-woody-fragrance",
        "perles": "lalique-perles-eau-de-parfum-100ml",
        "devotion": "dolce-gabbana-devotion-eau-de-parfum-100ml-luxury-women-s-gourmand-fragrance",
    },
    "titles": {},
    "shop": ["my90", "black90", "her", "my50", "black50", "rose", "perles", "devotion"],
    "body": """<p>Burberry's women's fragrances come in two families we stock: My Burberry, a soft, green floral, and Burberry Her, a fruity, berry-led line. My Burberry also has a richer sister, My Burberry Black. Here is every <strong>Burberry perfume</strong> we stock, with its notes and who each one suits.</p>
<h2>My Burberry Eau de Parfum</h2>
<p>My Burberry Eau de Parfum, in [[my50|50ml]] or [[my90|90ml]], opens with sweet pea and bergamot, has geranium leaf, golden quince and freesia in the heart, and settles on patchouli with Damask and centifolia rose. Fresh, green and floral, an easy everyday scent for spring and autumn.</p>
<h2>My Burberry Black Parfum</h2>
<p>My Burberry Black Parfum, in [[black50|50ml]] or [[black90|90ml]], is the richer, warmer version: jasmine, then peach nectar and candied rose, over amber and patchouli. Sweeter and deeper, it suits evenings and the colder months.</p>
<p><strong>My Burberry or My Burberry Black?</strong> Choose the eau de parfum for a light, green floral; choose Black for a warm, sweet rose with amber.</p>
<h2>The Burberry Her miniature set</h2>
<p>The [[her|Burberry Women's Miniature Perfume Set]] holds four 5ml bottles from the Her family, 20ml in all:</p>
<ul>
<li><strong>Her Eau de Parfum</strong> (2 x 5ml): red berries and blackcurrant, jasmine and violet, over amber, musk and woods.</li>
<li><strong>Her Eau de Toilette</strong> (5ml): green pear, strawberry and blackcurrant, peony and lily of the valley, over musk and cedarwood. Lighter and fresher.</li>
<li><strong>Her London Dream Eau de Parfum</strong> (5ml): lemon and ginger, rose and peony, over musk and amber.</li>
</ul>
<p>It is a good gift for someone who likes fruity florals, and an easy way to try the Her family.</p>
<h2>Which Burberry perfume should you choose?</h2>
<ul>
<li><strong>A fresh, green floral:</strong> My Burberry Eau de Parfum.</li>
<li><strong>A warm rose with amber:</strong> My Burberry Black Parfum.</li>
<li><strong>Fruity and berry-led:</strong> the Her miniature set.</li>
<li><strong>A first bottle:</strong> the 50ml size of either My Burberry.</li>
</ul>
<h2>Other women's scents in a similar mood</h2>
<p>These are different perfumes, not copies:</p>
<ul>
<li>[[rose|Chloé Rose Naturelle Intense Eau de Parfum]] (50ml): bergamot and neroli, rose and oakwood, over sandalwood and vanilla. Our <a href="/blogs/journal/chloe-perfume-guide">Chloé perfume guide</a> has more.</li>
<li>[[perles|Lalique Perles Eau de Parfum]] (100ml): Bulgarian rose and orris over cashmere wood and tonka bean.</li>
<li>[[devotion|Dolce &amp; Gabbana Devotion Eau de Parfum]] (100ml): candied citrus, orange blossom and Madagascar vanilla, for anyone who likes the sweetness of My Burberry Black.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Parfum or eau de parfum?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> See our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> and <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/burberry">Burberry</a> fragrance, or browse <a href="/collections/perfume-for-women">perfume for women</a>.</p>""",
    "faq": [
        ["What does My Burberry smell like?",
         "My Burberry Eau de Parfum opens with sweet pea and bergamot, has geranium leaf, golden quince and freesia in the heart, and dries down to patchouli with Damask and centifolia rose. It is a fresh, green floral."],
        ["What is the difference between My Burberry and My Burberry Black?",
         "My Burberry is a light, green floral. My Burberry Black Parfum is warmer and sweeter: jasmine, then peach nectar and candied rose, over amber and patchouli."],
        ["What is in the Burberry Her mini set?",
         "Four 5ml bottles: two Burberry Her Eau de Parfum, one Her Eau de Toilette and one Her London Dream Eau de Parfum, 20ml in all."],
        ["Which sizes of My Burberry do you sell?",
         "My Burberry Eau de Parfum and My Burberry Black Parfum both come in 50ml and 90ml."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_burberry_2026-11-20.jsonl")

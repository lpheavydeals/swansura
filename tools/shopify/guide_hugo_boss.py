"""Journal guide 'Hugo Boss perfume: Bottled, HUGO Man, The Scent and Alive compared'
(user, 20 Nov 2026: 'Write and Publish All').

Semrush UK: hugo boss perfume 14,800, hugo boss bottled 4,400, hugo man 1,300, alive 720, for men / for women 720.
4 of 5 listings in stock with photos on 20 Nov (allp_map_1120b.json); The Collection Confident Oud sold out (text link).
BOSS The Scent is listed as a tester (said plainly). Facts = stored notes (custom.sw + descriptions, Admin read 20 Nov;
the stored Hugo Boss notes are short accords, written as they are). 4 more cards = men's scents in a similar mood
(Versace Eros EDT, D&G The One EDP, CK Defy Parfum, Paco Invictus EDT), named as different perfumes.
NO PRICES in the text (user's 19 Nov decision). No longevity / 'dupe' / 'clone' wording.

Usage: python3 tools/shopify/guide_hugo_boss.py <allp_map.json>
Output: docs/seo/guide_hugo_boss_2026-11-20.jsonl
"""
import json
import sys

from journal_lib import build

H = "hugo-boss-"
A = {
    "title": "Hugo Boss perfume: Bottled, HUGO Man, The Scent and Alive compared",
    "handle": "hugo-boss-perfume-guide",
    "tag": "Scent Studio",
    "summary": "The Hugo Boss fragrances we stock: BOSS Bottled Eau de Parfum, HUGO Man, BOSS The Scent and the Alive gift set for women, with the notes and who each suits.",
    "mt": "Hugo Boss Perfume: Bottled, HUGO Man & The Scent | Swansura",
    "md": "Hugo Boss Bottled Eau de Parfum, HUGO Man, BOSS The Scent and the Alive gift set compared: the notes, sizes and which to choose.",
    "pick": {
        "bottled": H + "bottled-eau-de-parfum-200ml-for-men",
        "hugo": H + "hugo-man-eau-de-toilette-125ml-for-men",
        "scent": H + "boss-the-scent-eau-de-toilette-100ml-tester-men-s-warm-spicy-fragrance",
        "alive": H + "alive-eau-de-parfum-80ml-body-lotion-75ml-gift-set-for-women",
        "oud": H + "the-collection-confident-oud-eau-de-parfum-intense-100ml-for-men",
        "eros": "versace-eros-eau-de-toilette-200ml",
        "theone": "dolce-gabbana-the-one-for-men-eau-de-parfum-100ml-luxury-men-s-fragrance",
        "defy": "calvin-klein-defy-parfum-men-s-warm-woody-fragrance",
        "invictus": "paco-rabanne-invictus-eau-de-toilette-200ml",
    },
    "titles": {},
    "soldout": ["oud"],
    "shop": ["bottled", "hugo", "scent", "alive", "eros", "theone", "defy", "invictus"],
    "body": """<p>Hugo Boss runs two fragrance lines: BOSS, polished and grown-up, and HUGO, younger and fresher. Most of the range is made for men, with Alive as the women's line. Here is every <strong>Hugo Boss perfume</strong> we stock, with its notes and who each one suits.</p>
<h2>BOSS Bottled Eau de Parfum</h2>
<p>[[bottled|Hugo Boss Bottled Eau de Parfum]] (200ml, for men) opens with apple and a citrus accord, has warm spices in the heart, and settles on woody notes and an earthy accord. Fresh at the start and warm underneath, it is an easy scent for work and evenings, and the large 200ml bottle suits someone who wears it every day.</p>
<h2>HUGO Man</h2>
<p>[[hugo|HUGO Man Eau de Toilette]] (125ml) is the fresher, younger choice: green apple and a citrus accord, then herbal notes, over woody notes. Crisp and green, good for daytime, the gym bag and warmer weather.</p>
<h2>BOSS The Scent</h2>
<p>[[scent|BOSS The Scent Eau de Toilette]] (100ml) opens with ginger, mandarin and bergamot, has maninka fruit and lavender in the heart, and finishes on leather. Warm, spicy and smooth, an evening scent. Our listing is a tester.</p>
<h2>Alive, for women</h2>
<p>The [[alive|Hugo Boss Alive Eau de Parfum and Body Lotion Gift Set]] pairs an 80ml eau de parfum with a 75ml body lotion. Alive is built on fruity accords, then floral notes, over woody notes and vanilla accords: a warm, fruity floral, and a ready-made gift.</p>
<p>[[oud|BOSS The Collection Confident Oud Eau de Parfum Intense]] (warm spices, an oud accord, amber and woods) is out of stock at present: use Notify me on the page.</p>
<h2>Which Hugo Boss perfume should you choose?</h2>
<ul>
<li><strong>A warm, versatile scent for him:</strong> BOSS Bottled Eau de Parfum.</li>
<li><strong>Fresh and green:</strong> HUGO Man.</li>
<li><strong>Spicy and leathery for evenings:</strong> BOSS The Scent.</li>
<li><strong>A gift for her:</strong> the Alive gift set.</li>
</ul>
<h2>Other men's scents in a similar mood</h2>
<p>These are different perfumes, not copies, for anyone who likes the Hugo Boss style:</p>
<ul>
<li>[[eros|Versace Eros Eau de Toilette]] (200ml): mint, lemon and candied apple over cedarwood, vetiver and vanilla. Like Bottled, it starts with apple. Our <a href="/blogs/journal/versace-perfume-guide">Versace perfume guide</a> has more.</li>
<li>[[theone|Dolce &amp; Gabbana The One for Men Eau de Parfum]] (100ml): grapefruit, coriander and basil, then cardamom and ginger, over tobacco, amber and cedarwood. See our <a href="/blogs/journal/dolce-gabbana-perfume-guide">Dolce &amp; Gabbana perfume guide</a>.</li>
<li>[[defy|Calvin Klein Defy Parfum]]: mandarin and pink pepper, lavender and a suede accord, over vetiver, amber and woods.</li>
<li>[[invictus|Paco Rabanne Invictus Eau de Toilette]] (200ml): sea notes and grapefruit over guaiac wood and patchouli. See our <a href="/blogs/journal/paco-rabanne-perfume-guide">Paco Rabanne perfume guide</a>.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum or eau de toilette?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> See our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/hugo-boss">Hugo Boss</a> fragrance, or browse <a href="/collections/perfume-for-men">perfume for men</a>.</p>""",
    "faq": [
        ["What does Hugo Boss Bottled smell like?",
         "BOSS Bottled Eau de Parfum opens with apple and a citrus accord, has warm spices in the heart, and dries down to woody notes and an earthy accord. It starts fresh and turns warm."],
        ["What is the difference between BOSS Bottled and HUGO Man?",
         "Bottled is the warmer, more grown-up scent, with apple, warm spices and woods. HUGO Man is fresher and greener: green apple and citrus, then herbal notes, over woods."],
        ["What does BOSS The Scent smell like?",
         "BOSS The Scent Eau de Toilette opens with ginger, mandarin and bergamot, has maninka fruit and lavender in the heart, and finishes on leather. It is warm and spicy. Our listing is a tester."],
        ["Is there a Hugo Boss perfume for women?",
         "Yes. We stock the Hugo Boss Alive Eau de Parfum and Body Lotion Gift Set: an 80ml eau de parfum with fruity accords, floral notes, woods and vanilla, and a 75ml body lotion."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_hugo_boss_2026-11-20.jsonl")

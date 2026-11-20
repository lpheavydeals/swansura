"""Journal guide 'Marc Jacobs perfume: Perfect, Daisy, Honey and the mini set compared'
(user, 20 Nov 2026: 'What's the topic of the next 5 Journals' -> 'Write and Publish All').

Semrush UK: marc jacobs perfume 27,100, marc jacobs perfect 6,600, honey 2,400, perfect perfume 1,900.
All 7 Marc Jacobs listings in stock with photos on 20 Nov (allp_map_1120b.json). Facts = stored notes (custom.sw +
descriptions, Admin read 20 Nov); Daisy, Daisy Eau So Fresh and Daisy Wild only in the 2025 mini set (notes from its
text). 8th card: Lalique Amethyst Eclat, named as a different perfume. NO PRICES in the text (user's 19 Nov decision to
remove prices from the articles; the product cards show live prices). No longevity / 'dupe' / 'iconic' wording.

Usage: python3 tools/shopify/guide_marc_jacobs.py <allp_map.json>
Output: docs/seo/guide_marc_jacobs_2026-11-20.jsonl
"""
import json
import sys

from journal_lib import build

M = "marc-jacobs-"
A = {
    "title": "Marc Jacobs perfume: Perfect, Daisy, Honey and the mini set compared",
    "handle": "marc-jacobs-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Marc Jacobs fragrance we stock, side by side: Perfect in three strengths, Daisy Love, Daisy Love Glow, Honey and the 2025 miniature set.",
    "mt": "Marc Jacobs Perfume: Perfect, Daisy & Honey | Swansura",
    "md": "Marc Jacobs Perfect EDP, EDT and Elixir, Daisy Love, Daisy Love Glow, Honey and the Daisy mini set compared: the notes and which to choose.",
    "pick": {
        "perfect": M + "perfect-eau-de-parfum-50ml-women-s-floral-fragrance",
        "perfectedt": M + "perfect-eau-de-toilette-10ml-miniature-women-s-floral-fragrance",
        "elixir": M + "perfect-elixir-eau-de-parfum-10ml-miniature-women-s-floral-gourmand-fragrance",
        "honey": M + "honey-eau-de-parfum-100ml-women-s-floral-fruity-fragrance",
        "love": M + "daisy-love-eau-de-toilette-10ml-miniature-women-s-floral-fruity-fragrance",
        "glow": M + "daisy-love-glow-limited-edition-eau-de-toilette-50ml-women-s-floral-fragrance",
        "set": M + "women-s-miniature-fragrance-gift-set-2025-daisy-daisy-eau-so-fresh-perfect-daisy-wild",
        "eclat": "lalique-amethyst-eclat-eau-de-parfum-100ml",
    },
    "titles": {},
    "shop": ["perfect", "honey", "glow", "set", "elixir", "perfectedt", "love", "eclat"],
    "body": """<p>Marc Jacobs fragrances are playful and easy to wear: fruity tops, soft florals and gentle, musky or woody bases. The house's two big families are Perfect and Daisy, with Honey as a warmer, sweeter choice. Here is every <strong>Marc Jacobs perfume</strong> we stock, with its notes and who each one suits.</p>
<h2>Marc Jacobs Perfect: three strengths</h2>
<p>Perfect is built around rhubarb and narcissus, and each version takes it in a different direction:</p>
<ul>
<li>[[perfect|Marc Jacobs Perfect Eau de Parfum]] (50ml): rhubarb and narcissus, then almond milk, over cedarwood and cashmeran. Soft, creamy and a little nutty, an easy everyday scent.</li>
<li>[[perfectedt|Perfect Eau de Toilette]] (10ml miniature): rhubarb and pink pepper, then narcissus, over cedarwood. Lighter and brighter, with no almond milk.</li>
<li>[[elixir|Perfect Elixir Eau de Parfum]] (10ml miniature): plum and rhubarb, then a floral accord, over vanilla, amber and woods. The warmest of the three, for evenings and winter.</li>
</ul>
<p><strong>Which Perfect?</strong> The eau de parfum for a soft, creamy floral; the eau de toilette for something fresher; the Elixir for a sweeter, ambery version.</p>
<h2>Daisy Love and Daisy Love Glow</h2>
<ul>
<li>[[love|Daisy Love Eau de Toilette]] (10ml miniature): cloudberry, then daisy, over cashmere musk and driftwood. Light, fruity and clean, a daytime scent.</li>
<li>[[glow|Daisy Love Glow Limited Edition Eau de Toilette]] (50ml): lemon essential oil, cloudberry and bergamot, then clove essential oil, jasmine and lemon blossom, over cashmere musk and patchouli oil. Brighter at the top and a touch spicier in the heart.</li>
</ul>
<h2>Marc Jacobs Honey</h2>
<p>[[honey|Marc Jacobs Honey Eau de Parfum]] (100ml) is the sweetest Marc Jacobs we stock: pear, mandarin and a punch accord, then honeysuckle, orange blossom and peach, over honey, vanilla and woods. Warm and fruity, a good choice for anyone who finds Daisy too light.</p>
<h2>The Marc Jacobs miniature set</h2>
<p>The [[set|Marc Jacobs Women's Miniature Fragrance Gift Set 2025]] is the easiest way to try the Daisy family:</p>
<ul>
<li><strong>Daisy Eau de Toilette</strong> (4ml): strawberry, violet leaf and grapefruit; violet, gardenia and jasmine; musk, white woods and vanilla.</li>
<li><strong>Daisy Eau So Fresh</strong> (4ml): raspberry, grapefruit and pear; violet, rose and apple blossom; musk, cedar and plum.</li>
<li><strong>Daisy Wild Eau de Parfum</strong> (4ml): banana blossom; jasmine and macadamia; vetiver and sandalwood.</li>
<li><strong>Perfect Eau de Parfum</strong> (5ml).</li>
</ul>
<h2>Which Marc Jacobs perfume should you choose?</h2>
<ul>
<li><strong>A soft, creamy everyday floral:</strong> Perfect Eau de Parfum.</li>
<li><strong>Something warmer for evenings:</strong> Perfect Elixir.</li>
<li><strong>Light and fruity:</strong> Daisy Love.</li>
<li><strong>Bright with a little spice:</strong> Daisy Love Glow.</li>
<li><strong>Sweet and warm:</strong> Honey.</li>
<li><strong>Not sure yet:</strong> the miniature set, or one of the 10ml sprays.</li>
</ul>
<p>If you like Daisy's fruity florals, [[eclat|Lalique Amethyst Éclat Eau de Parfum]] (100ml) pairs raspberry, blackcurrant and pear with peony, rose and magnolia over blackberry, musk and violet woodsorrel. It is a different perfume, with more berries.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum or eau de toilette?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Buying a gift?</strong> See our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> and <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/marc-jacobs">Marc Jacobs</a> fragrance, or browse <a href="/collections/perfume-for-women">perfume for women</a> and <a href="/collections/travel-size-minis">travel-size minis</a>.</p>""",
    "faq": [
        ["What does Marc Jacobs Perfect smell like?",
         "Marc Jacobs Perfect Eau de Parfum opens with rhubarb and narcissus, has almond milk in the heart, and dries down to cedarwood and cashmeran. It is soft and creamy. The eau de toilette is lighter, and Perfect Elixir adds plum, vanilla and amber."],
        ["What is the difference between Daisy Love and Daisy Love Glow?",
         "Daisy Love is cloudberry and daisy over cashmere musk and driftwood. Daisy Love Glow adds lemon, bergamot, clove, jasmine and lemon blossom, over cashmere musk and patchouli, so it is brighter and a little spicier."],
        ["What does Marc Jacobs Honey smell like?",
         "Honey Eau de Parfum opens with pear, mandarin and a punch accord, has honeysuckle, orange blossom and peach in the heart, and dries down to honey, vanilla and woods. It is the sweetest Marc Jacobs we stock."],
        ["Is there a Marc Jacobs mini set?",
         "Yes. The 2025 Women's Miniature Fragrance Gift Set holds Daisy, Daisy Eau So Fresh and Daisy Wild in 4ml each, plus Perfect Eau de Parfum in 5ml."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_marc_jacobs_2026-11-20.jsonl")

"""Journal guide 'Versace perfume: Eros, Eros Pour Femme, Dylan Blue and Yellow Diamond compared'
(user, 17-18 Nov 2026: 'Whats the topic of Next 5 Journals' -> 'Write and Publish All').

Semrush UK (10 Nov): versace eros 27,100 (KD 22), versace perfume 27,100 (KD 17), versace yellow diamond 1,900,
versace eros eau de toilette 1,000, versace man eau fraiche 1,000, versace eros pour femme 880, versace eros parfum 880.
All 7 Versace listings in stock with photos on 18 Nov (storefront dump allp_map_1118.json).
Facts = each product's stored notes (custom.sw + description, Admin read 18 Nov 2026). No longevity / projection /
'dupe' / 'iconic' wording, no launch dates. Prices are written into the text: re-run and update if prices change.

Usage: python3 tools/shopify/guide_versace.py <allp_map.json>
Output: docs/seo/guide_versace_2026-11-18.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Versace perfume: Eros, Eros Pour Femme, Dylan Blue and Yellow Diamond compared",
    "handle": "versace-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Versace fragrance we stock, side by side: Versace Eros eau de toilette and parfum, Eros Pour Femme, Dylan Blue, Man Eau Fraîche and Yellow Diamond.",
    "mt": "Versace Perfume: Eros, Dylan Blue, Yellow Diamond | Swansura",
    "md": "Versace Eros EDT vs Eros Parfum, Eros Pour Femme, Dylan Blue, Man Eau Fraiche and Yellow Diamond: the notes, sizes and which to choose.",
    "pick": {
        "erosedt": "versace-eros-eau-de-toilette-200ml",
        "erosparfum": "versace-eros-parfum",
        "femmeedp": "versace-eros-pour-femme-eau-de-parfum-100ml",
        "femmeedt": "versace-eros-pour-femme-eau-de-toilette-miniature-5ml",
        "dylan": "versace-dylan-blue-pour-homme-eau-de-toilette-miniature-5ml",
        "fraiche": "versace-man-eau-fraiche-eau-de-toilette-miniature-5ml",
        "yellow": "versace-yellow-diamond-eau-de-toilette-90ml",
        "invictus": "paco-rabanne-invictus-eau-de-toilette-200ml",
    },
    "titles": {},
    "shop": ["erosedt", "erosparfum", "femmeedp", "yellow", "dylan", "fraiche", "femmeedt", "invictus"],
    "body": """<p>Versace's fragrances split neatly in two: the Eros family, warm and sweet for him and bright and floral for her, and a set of fresher scents built on citrus, water and woods. Here is every <strong>Versace perfume</strong> we stock, with its notes, the sizes on offer and who each one suits.</p>
<h2>Versace Eros: mint, apple and vanilla</h2>
<p>[[erosedt|Versace Eros Eau de Toilette]] ({{erosedt}}, 200ml) is a men's fragrance built on contrast. Mint, Italian lemon, mandarin and candied apple open it; geranium, clary sage and an amber note sit in the heart; and two cedarwoods, vetiver, patchouli, sandalwood and vanilla make the base. It starts cool and sweet, then settles warm and woody. A natural pick for nights out, parties and the colder months.</p>
<h3>Versace Eros Parfum</h3>
<p>[[erosparfum|Versace Eros Parfum]] ({{erosparfum}}, 100ml or 200ml) is the darker, more resinous version. Italian lemon, mandarin, litsea cubeba, elemi and black pepper open it; pomarose, Egyptian geranium, lavender and clary sage form the heart; and benzoin, cashmeran, patchouli, vanilla and vetiver sit underneath. Where the eau de toilette leans on mint and apple, the parfum leans on pepper, lavender and resin.</p>
<p><strong>Eros eau de toilette or Eros Parfum?</strong> Choose the eau de toilette if you like the minty, sweet apple opening; choose the parfum for a spicier, deeper scent. A parfum holds a higher share of fragrance oils than an eau de toilette, so it feels richer and sits closer to the skin. Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</p>
<h2>Versace Eros Pour Femme</h2>
<p>Eros Pour Femme is a different perfume from the men's Eros, not a softer version of it. It comes in two strengths with different notes:</p>
<ul>
<li>[[femmeedp|Eros Pour Femme Eau de Parfum]] ({{femmeedp}}, 100ml): Sicilian lemon, Calabrian bergamot and pomegranate, then lemon flower, jasmine sambac and peony, over sandalwood, amber and musk. Bright at first, then floral and polished.</li>
<li>[[femmeedt|Eros Pour Femme Eau de Toilette Miniature]] ({{femmeedt}}, 5ml): Sicilian lemon, mandarin, raspberry sorbet and white currant, then freesia, magnolia, jasmine petals and orange blossom, over ambrox, white patchouli and musk. Juicier and lighter, an easy daytime scent.</li>
</ul>
<h2>Versace Dylan Blue Pour Homme</h2>
<p>[[dylan|Versace Dylan Blue Pour Homme Eau de Toilette Miniature]] ({{dylan}}, 5ml) opens with water notes, fig leaves, bergamot and grapefruit. Violet leaves, patchouli, papyrus, black pepper and ambroxan sit in the heart, with musk, tonka bean, saffron and frankincense underneath. It starts fresh and aquatic and dries down darker and woodier, so it works for the day and for evenings.</p>
<h2>Versace Man Eau Fraîche</h2>
<p>[[fraiche|Versace Man Eau Fraîche Eau de Toilette Miniature]] ({{fraiche}}, 5ml) is the crispest Versace for men: white lemon, rosewood and star fruit, then tarragon, cedar leaves and clary sage, over musk, amber and sycamore wood. Clean and airy, it suits hot days, holidays and the gym bag.</p>
<h2>Versace Yellow Diamond</h2>
<p>[[yellow|Versace Yellow Diamond Eau de Toilette]] ({{yellow}}, 90ml) is a sunny floral for women. Citron, pear sorbet, neroli and bergamot open it; water lily, freesia, orange blossom and mimosa form a soft heart; and amber wood, palo santo and musk sit quietly underneath. Light, fruity and slightly powdery, it is a spring and summer scent, and an easy one for the office.</p>
<h2>Which Versace perfume should you choose?</h2>
<ul>
<li><strong>A sweet, warm scent for him:</strong> Versace Eros Eau de Toilette.</li>
<li><strong>A deeper, spicier version:</strong> Versace Eros Parfum.</li>
<li><strong>A fresh scent that turns woody:</strong> Dylan Blue Pour Homme.</li>
<li><strong>Something light and citrusy for him:</strong> Man Eau Fraîche.</li>
<li><strong>A bright floral for her:</strong> Eros Pour Femme Eau de Parfum, or the eau de toilette for a fruitier, lighter take.</li>
<li><strong>A soft, sunny floral for her:</strong> Yellow Diamond.</li>
<li><strong>Not sure yet:</strong> start with a 5ml miniature at {{dylan}}.</li>
</ul>
<p>If you like the fresh, marine side of Dylan Blue, [[invictus|Paco Rabanne Invictus Eau de Toilette]] ({{invictus}}, 200ml) has sea notes and grapefruit over guaiac wood and patchouli. It is a different perfume, not a copy; our <a href="/blogs/journal/paco-rabanne-perfume-guide">Paco Rabanne guide</a> compares the whole range.</p>
<h2>Good to know</h2>
<ul>
<li><strong>The 5ml miniatures</strong> make easy stocking fillers: see our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> for more.</li>
<li><strong>Buying a gift?</strong> Our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a> has more Christmas ideas.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/versace">Versace</a> fragrance, or browse <a href="/collections/perfume-for-men">perfume for men</a> and <a href="/collections/perfume-for-women">perfume for women</a>.</p>""",
    "faq": [
        ["What does Versace Eros smell like?",
         "Versace Eros Eau de Toilette opens with mint, Italian lemon, mandarin and candied apple, has geranium and clary sage in the heart, and dries down to cedarwood, vetiver, patchouli, sandalwood and vanilla. It starts cool and sweet, then turns warm and woody."],
        ["What is the difference between Versace Eros EDT and Eros Parfum?",
         "The eau de toilette is built on mint, apple and vanilla. Eros Parfum is spicier and more resinous, with black pepper, elemi, lavender and geranium over benzoin, cashmeran, patchouli and vanilla. As a parfum it holds a higher share of fragrance oils, so it feels richer and sits closer to the skin."],
        ["Is Versace Eros Pour Femme the same as Eros?",
         "No. Eros Pour Femme is a separate perfume for women. The eau de parfum opens with Sicilian lemon, bergamot and pomegranate, with jasmine and peony in the heart over sandalwood, amber and musk. The eau de toilette is fruitier, with raspberry sorbet and white currant."],
        ["Which Versace perfume is fresh?",
         "Versace Man Eau Fraiche (white lemon, star fruit, tarragon and cedar leaves) is the freshest for men, and Dylan Blue Pour Homme opens with water notes, fig leaves and grapefruit before turning woody. For women, Yellow Diamond is a light, sunny floral with citron, pear and water lily."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_versace_2026-11-18.jsonl")

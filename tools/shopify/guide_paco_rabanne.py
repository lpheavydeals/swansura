"""Journal guide 'Paco Rabanne perfume: 1 Million, Invictus, Phantom, Fame and Lady Million' (user, 15 Nov 2026: 'Write the next 2 Journal guides').

Semrush UK: paco rabanne 1 million 14,800 (KD 22), invictus 9,900 (KD 11), phantom 9,900 (KD 13), fame 6,600 (KD 24),
paco rabanne perfume 2,900, lady million 2,900, ultraviolet 1,600, invictus victory 1,000, phantom parfum 880, fame parfum
590, phantom gift set 480, invictus gift set 390, olympea flora 170, xs black 170. No Paco Rabanne guide yet; 18 of the 23
listings in stock on 15 Nov (storefront dump allp_map_1115.json).
Facts = each product's stored notes (custom.sw + description, Admin read 15 Nov 2026; the 1 Million Elixir, Phantom EDT and
Olympea notes come from the miniature sets' stored note lists). Products without photos (Phantom Parfum 15ml, Lady Million
15ml / Royal 30ml, Fame Parfum 10ml / Intense 30ml, XS Black, Invictus EDT & Deodorant set) are linked in the text only,
never in 'Shop the story'. No longevity / projection / 'dupe' / 'most popular' / 'iconic' wording, no launch dates or
bottle-design history (not in our data). Prices are written into the text: re-run the generator and update the body if
prices change.

Usage: python3 tools/shopify/guide_paco_rabanne.py <allp_map.json>   (handle -> storefront product)
Output: docs/seo/guide_paco_rabanne_2026-11-15.jsonl
"""
import json
import sys

from journal_lib import build

P = "paco-rabanne-"
A = {
    "title": "Paco Rabanne perfume: 1 Million, Invictus, Phantom, Fame and Lady Million compared",
    "handle": "paco-rabanne-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Every Paco Rabanne line we stock, side by side: 1 Million, Invictus and Phantom for him, Fame, Lady Million, Olympéa and Ultraviolet for her, plus the gift and miniature sets.",
    "mt": "Paco Rabanne Perfume: 1 Million, Invictus, Fame | Swansura",
    "md": "Paco Rabanne 1 Million, Invictus, Phantom, Fame and Lady Million compared: the notes, the versions and which one to choose, plus gift sets and minis.",
    "pick": {
        "million": P + "1-million-eau-de-toilette-200ml",
        "invictus": P + "invictus-eau-de-toilette-200ml",
        "invset": P + "invictus-eau-de-toilette-gift-set-200ml-10ml",
        "invdeo": P + "invictus-eau-de-toilette-deodorant-gift-set-100ml-150ml-10ml",
        "victory": P + "invictus-victory-eau-de-parfum-extreme-100ml",
        "phparfum": P + "phantom-parfum-spray-15ml",
        "xs": P + "xs-black-eau-de-toilette-100ml",
        "menmini4": P + "mens-miniature-set-phantom-invictus-1-million-elixir-1-million-4-x-5ml",
        "menmini3": P + "mens-miniature-eau-de-toilette-set-1-million-invictus-phantom-3-x-4ml",
        "fame80": P + "fame-eau-de-parfum-refillable-80ml",
        "fameset": P + "fame-eau-de-parfum-gift-set-50ml-10ml",
        "famemini": P + "fame-eau-de-parfum-parfum-mini-set-4ml-4ml",
        "fameparfum": P + "fame-parfum-10ml",
        "fameint": P + "fame-eau-de-parfum-intense-30ml",
        "lady": P + "lady-million-eau-de-parfum-15ml",
        "royal": P + "lady-million-royal-eau-de-parfum-30ml",
        "flora": P + "olympea-flora-eau-de-parfum-intense-80ml",
        "uv": P + "ultraviolet-eau-de-parfum-80ml",
        "womenmini": P + "womens-miniature-set-lady-million-olympea-fame-5ml-6ml-4ml-4ml",
    },
    "titles": {},
    "shop": ["million", "invset", "victory", "menmini4", "fame80", "flora", "uv", "womenmini"],
    "body": """<p>Paco Rabanne's fragrance names can be confusing: 1 Million, Invictus and Phantom for men, Fame, Lady Million and Olympéa for women, each in several versions. Here is every <strong>Paco Rabanne perfume</strong> line we stock, with its notes, the versions on offer and who each one suits.</p>
<h2>Paco Rabanne for him</h2>
<h3>1 Million: warm and spicy</h3>
<p>[[million|Paco Rabanne 1 Million Eau de Toilette]] ({{million}}, 200ml) opens with blood mandarin, grapefruit and mint, moves to cinnamon, rose and spice, and settles on amber, leather, woody notes and Indian patchouli. It is sweet, spiced and confident, a natural choice for nights out and colder weather. The 1 Million Elixir, which you will find in the [[menmini4|men's miniature set]] ({{menmini4}}, 4 x 5ml), takes a different route: apple and davana, then Damask rose, osmanthus and cedar, over vanilla absolute, tonka bean and patchouli.</p>
<h3>Invictus: fresh and marine</h3>
<p>[[invictus|Paco Rabanne Invictus Eau de Toilette]] ({{invictus}}, 200ml) is the fresh one: sea notes, grapefruit and mandarin orange, then bay leaf and jasmine, over ambergris, guaiac wood, oakmoss and patchouli. It suits everyday wear, the office and warmer days. For a present, the [[invset|Invictus Eau de Toilette Gift Set]] ({{invset}}) adds a 10ml spray to the 200ml bottle, and the [[invdeo|Invictus Eau de Toilette &amp; Deodorant Gift Set]] ({{invdeo}}) pairs a 100ml bottle with a deodorant spray and a 10ml spray.</p>
<p>[[victory|Invictus Victory Eau de Parfum Extrême]] ({{victory}}, 100ml) is the warmer sister: pink pepper and lemon, then olibanum and lavender, over vanilla, tonka bean and amber. Choose it for evenings and winter; choose the original Invictus for daytime and summer.</p>
<h3>Phantom: aromatic lavender</h3>
<p>Phantom is built around lavender. The eau de toilette, found in both men's miniature sets, opens with lavender, lemon zest and Amalfi lemon, adds apple and a smoky, earthy heart, and dries down to vanilla, lavender and vetiver. The [[phparfum|Phantom Parfum Spray]] ({{phparfum}}, 15ml) is richer: cardamom, bergamot, lemon and rhubarb, then lavender, geranium, patchouli and cedar, over vanilla, tolu balsam and vetiver. Its small size is a good way to try the parfum before a bigger bottle.</p>
<h3>XS Black: woody and herbal</h3>
<p>[[xs|Paco Rabanne XS Black Eau de Toilette]] ({{xs}}, 100ml) mixes mint, bergamot and lemon with juniper berries, coriander and geranium, over oakmoss, sandalwood and rosemary. It is the most herbal and woody of the men's range.</p>
<h2>Paco Rabanne for her</h2>
<h3>Fame: mango, jasmine and incense</h3>
<p>The [[fame80|Fame Eau de Parfum]] ({{fame80}}, 80ml refillable) opens on mango and bergamot, moves to jasmine and olibanum, and ends on vanilla and sandalwood: fruity at first, then smooth and softly resinous. It also comes as the [[fameset|Fame Eau de Parfum Gift Set]] ({{fameset}}, 50ml + 10ml).</p>
<ul>
<li><strong>Fame Parfum</strong> ([[fameparfum|10ml]], {{fameparfum}}) adds pink pepper, patchouli and frankincense, over benzoin, sandalwood and musk: deeper and more resinous.</li>
<li><strong>Fame Eau de Parfum Intense</strong> ([[fameint|30ml]], {{fameint}}) swaps the mango for coconut water, pink pepper and bergamot, with jasmine, incense and ylang-ylang over sandalwood, cedarwood and musk.</li>
<li>Not sure which? The [[famemini|Fame Eau de Parfum &amp; Parfum Mini Set]] ({{famemini}}, 4ml + 4ml) lets you try the eau de parfum and the parfum side by side.</li>
</ul>
<h3>Lady Million: honeyed and floral</h3>
<p>[[lady|Lady Million Eau de Parfum]] ({{lady}}, 15ml) opens with raspberry, neroli and Amalfi lemon, blooms into jasmine, African orange flower and gardenia, and finishes on white honey, patchouli and amber. It is bright and golden, made for parties and celebrations. [[royal|Lady Million Royal]] ({{royal}}, 30ml) is simpler, with just three notes: pomegranate, white flowers and cashmeran.</p>
<h3>Olympéa and Ultraviolet</h3>
<ul>
<li><strong>Olympéa</strong> pairs water jasmine, green mandarin and ginger flower with vanilla and a touch of salt, over ambergris, cashmere wood and sandalwood (in the [[womenmini|women's miniature set]], {{womenmini}}). [[flora|Olympéa Flora Eau de Parfum Intense]] ({{flora}}, 80ml) is fruitier: black currant, sorbet and pink pepper, then rose and peony, over patchouli, cashmere wood, vanilla and salt.</li>
<li>[[uv|Ultraviolet Eau de Parfum]] ({{uv}}, 80ml) is the spiciest of the women's range: pepper, pimento, coriander, apricot and almond, then violet, osmanthus, rose and jasmine, over amber, vanilla, patchouli and cedar. A warm pick for autumn and winter.</li>
</ul>
<h2>Which Paco Rabanne should you choose?</h2>
<ul>
<li><strong>Sweet and spicy for him:</strong> 1 Million, or Invictus Victory for vanilla and amber.</li>
<li><strong>Fresh and easy for him:</strong> Invictus.</li>
<li><strong>Lavender and clean:</strong> Phantom.</li>
<li><strong>Fruity floral for her:</strong> Fame or Olympéa Flora.</li>
<li><strong>Honeyed and celebratory:</strong> Lady Million.</li>
<li><strong>Warm and spicy for her:</strong> Ultraviolet.</li>
</ul>
<h2>Gift sets and miniatures</h2>
<p>Miniature sets are the easiest way to try several scents before choosing a full bottle. The [[menmini3|men's miniature eau de toilette set]] ({{menmini3}}, 3 x 4ml) holds 1 Million, Invictus and Phantom; the 4 x 5ml set adds 1 Million Elixir. For her, the [[womenmini|women's miniature set]] ({{womenmini}}) holds Lady Million, Olympéa, Fame eau de parfum and Fame parfum. Our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> compares minis from other houses, and the <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a> has more ideas for Christmas.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de toilette, eau de parfum or parfum?</strong> The names tell you how concentrated the fragrance is; our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>Start small:</strong> a spray or two on the neck and wrists is enough for these scents.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/paco-rabanne">Paco Rabanne</a> fragrance, or browse <a href="/collections/perfume-for-men">perfume for men</a>, <a href="/collections/perfume-for-women">perfume for women</a> and <a href="/collections/aftershave-gift-sets-for-him">aftershave gift sets for him</a>.</p>""",
    "faq": [
        ["What is the difference between Paco Rabanne 1 Million and Invictus?",
         "1 Million is warm and spicy: blood mandarin and mint, then cinnamon and rose, over amber, leather and patchouli. Invictus is fresh and marine: sea notes, grapefruit and mandarin, then bay leaf and jasmine, over ambergris, guaiac wood and oakmoss. 1 Million suits evenings and colder weather; Invictus suits daytime and warmer days."],
        ["What does Paco Rabanne Phantom smell like?",
         "Phantom is built around lavender. The eau de toilette has lavender and lemon, apple and a smoky, earthy heart, over vanilla and vetiver. The parfum adds cardamom, rhubarb, geranium, patchouli and cedar, over vanilla, tolu balsam and vetiver."],
        ["What is the difference between Fame Eau de Parfum and Fame Parfum?",
         "Both open with mango and bergamot and have jasmine at the heart. The eau de parfum dries down to vanilla and sandalwood; the parfum adds pink pepper, patchouli and frankincense and ends on benzoin, sandalwood and musk, so it feels deeper. The Fame mini set has 4ml of each."],
        ["Do you sell Paco Rabanne miniature sets?",
         "Yes: a men's set with 1 Million, Invictus and Phantom (3 x 4ml), a men's set that adds 1 Million Elixir (4 x 5ml), and a women's set with Lady Million, Olympéa and Fame (5ml, 6ml and 2 x 4ml)."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_paco_rabanne_2026-11-15.jsonl")

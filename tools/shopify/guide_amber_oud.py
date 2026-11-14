"""Journal guide 'Al Haramain Amber Oud: every edition compared, from Gold to Tobacco' (user, 14 Nov 2026: 'Write the next 2 Journal guides').

Semrush UK: al haramain amber oud 2,400 (KD 16), amber oud gold edition 590 (KD 12), tobacco edition 480 (KD 15), ruby
edition 140 (KD 10), bleu edition 110, carbon edition 110. Search Console (4-10 Nov 2026): 'al haramain amber oud gold
edition' already at position 7, 'al haramain amber musk' at 3. All ten Amber Oud listings + Amber Musk in stock on 14 Nov.
Facts = each product's stored custom.sw notes + description (Admin read 14 Nov 2026). None of the stored note lists names
oud: the guide says so plainly and sends oud-led perfumes to the oud guide (same honesty line as oud-perfume-guide).
The original Amber Oud and the Gold Edition carry the same note list in our listings: stated as that, no claim that they
are the same perfume. Extreme Gold = extrait de parfum (title), same listed notes. No longevity / projection / 'dupe' /
'inspired by' wording; no 'most popular'. Prices (per size) are written into the text: re-run the generator and update the
body if prices change.

Usage: python3 tools/shopify/guide_amber_oud.py <allp_map.json>   (handle -> storefront product)
Output: docs/seo/guide_amber_oud_2026-11-14.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Al Haramain Amber Oud: every edition compared, from Gold to Tobacco",
    "handle": "al-haramain-amber-oud-editions",
    "tag": "Scent Studio",
    "summary": "The Al Haramain Amber Oud editions side by side: Gold, Ruby, Tobacco, Black, Bleu, Carbon and White, with their notes, sizes and who each one suits.",
    "mt": "Al Haramain Amber Oud: Every Edition Compared | Swansura",
    "md": "Al Haramain Amber Oud Gold, Ruby, Tobacco, Black, Bleu, Carbon and White compared: the notes, sizes and prices, and which edition to choose.",
    "pick": {
        "gold": "al-haramain-amber-oud-gold-edition-eau-de-parfum-luxury-unisex-fruity-amber-fragrance",
        "orig": "al-haramain-amber-oud-eau-de-parfum-60ml-luxury-unisex-amber-woody-fragrance",
        "xgold": "al-haramain-amber-oud-extreme-gold-edition-extrait-de-parfum-luxury-unisex-fruity-amber-fragrance",
        "ruby": "al-haramain-amber-oud-ruby-edition-eau-de-parfum-luxury-unisex-amber-floral-fragrance",
        "tobacco": "al-haramain-amber-oud-tobacco-edition-eau-de-parfum-60ml-luxury-unisex-spicy-tobacco-fragrance",
        "black": "al-haramain-amber-oud-black-edition-eau-de-parfum-100ml-luxury-unisex-woody-amber-fragrance",
        "bleu": "al-haramain-amber-oud-bleu-edition-eau-de-parfum-60ml-luxury-unisex-fresh-woody-fragrance",
        "carbon": "al-haramain-amber-oud-carbon-edition-eau-de-parfum-men-s-fresh-woody-fragrance",
        "white": "al-haramain-amber-oud-white-edition-eau-de-parfum-luxury-women-s-floral-oriental-fragrance",
        "musk": "al-haramain-amber-musk-eau-de-parfum-100ml-luxury-unisex-amber-musk-fragrance",
    },
    "titles": {},
    "shop": ["gold", "ruby", "tobacco", "black", "bleu", "carbon", "white", "orig"],
    "body": """<p>Al Haramain's <strong>Amber Oud</strong> is a family of eau de parfums rather than a single scent. Each edition has its own colour and its own character, from the sweet, fruity Gold to the spiced Tobacco and the fresh, herbal Carbon. Here is every <strong>Al Haramain Amber Oud</strong> edition we stock, side by side, with its notes, sizes and the kind of person it suits.</p>
<h2>Is there oud in Amber Oud?</h2>
<p>Amber Oud is the name of the line. The note lists we hold for these editions do not name oud: they are built on amber, woods, musk, vanilla and resins, with fruit, flowers, spice or herbs on top depending on the edition. If you want a perfume that puts oud at the centre, read our <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a>. If you want a warm, amber-led scent with an Arabian feel, read on.</p>
<h2>Sweet and fruity: the original and the Gold Edition</h2>
<p>[[gold|Al Haramain Amber Oud Gold Edition]] ({{gold}}, 60ml, 100ml or 200ml) opens with bergamot and green notes, moves into melon, pineapple, amber and sweet notes, and dries down to vanilla, musk and woods. It is the edition to choose if you like sweet, golden, fruity scents.</p>
<p>The [[orig|original Al Haramain Amber Oud]] ({{orig}}, 60ml) carries the same note list in our listings: bergamot and green notes, then amber, melon, pineapple and sweet notes, then vanilla, musk and woods. The brand sells them as separate editions, so expect them to be close relatives.</p>
<p>For a stronger version, [[xgold|Amber Oud Extreme Gold Edition]] ({{xgold}}, 60ml or 100ml) is an extrait de parfum with the same listed notes. An extrait has a higher concentration of fragrance oils than an eau de parfum; our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</p>
<h2>Warm and spiced: Ruby, Tobacco and Black</h2>
<ul>
<li>[[ruby|Amber Oud Ruby Edition]] ({{ruby}}, 100ml, 120ml or 200ml): saffron and bitter almond, then jasmine and cedarwood, over ambergris, woods and musk. Spiced, nutty and floral, a smooth choice for evenings.</li>
<li>[[tobacco|Amber Oud Tobacco Edition]] ({{tobacco}}, 60ml): tobacco leaf, cinnamon, black pepper and ginger, then vanilla, clove, star anise, cacao and tonka bean, over tobacco, dried fruits and woods. The richest and sweetest of the spiced editions, made for winter nights.</li>
<li>[[black|Amber Oud Black Edition]] ({{black}}, 100ml): cardamom, grapefruit and lavender, then leather, amber and orange blossom, over benzoin, ambergris and vetiver. Darker and drier, with a leather heart.</li>
</ul>
<h2>Fresh and woody: Bleu and Carbon</h2>
<ul>
<li>[[bleu|Amber Oud Bleu Edition]] ({{bleu}}, 60ml, 100ml or 200ml): grapefruit, lemon, mint and pink pepper, then ginger, nutmeg and jasmine, over incense, vetiver, cedar, sandalwood, patchouli, labdanum and white musk. Crisp at the start and woody underneath, easy to wear all year.</li>
<li>[[carbon|Amber Oud Carbon Edition]] ({{carbon}}, 60ml, 100ml or 200ml): lavender, rosemary and bergamot, then sage, cedarwood and geranium, over vetiver, musk, amber and moss. A clean, herbal scent sold as a men's fragrance, good for the office.</li>
</ul>
<h2>Floral: the White Edition</h2>
<p>[[white|Amber Oud White Edition]] ({{white}}, 60ml, 100ml or 200ml) is sold as a women's fragrance: bergamot and orange, then jasmine, rose and freesia, over musk, vanilla and patchouli. It is the lightest and most floral of the family, an easy pick for daytime.</p>
<h2>Which Amber Oud edition should you choose?</h2>
<ul>
<li><strong>You like sweet, fruity scents:</strong> Gold Edition, or Extreme Gold for a richer version.</li>
<li><strong>You want something warm for winter:</strong> Tobacco Edition or Ruby Edition.</li>
<li><strong>You like leather and dry woods:</strong> Black Edition.</li>
<li><strong>You want a fresh everyday scent:</strong> Bleu Edition, or Carbon for a herbal, barbershop style.</li>
<li><strong>You prefer florals:</strong> White Edition.</li>
</ul>
<p>Most editions are unisex; Carbon is sold for men and White for women, but wear whichever you like. Prefer amber without the fruit? The sister scent [[musk|Al Haramain Amber Musk]] ({{musk}}, 100ml) is amber and floral notes over musk, woods, vanilla and resins.</p>
<h2>How to wear it</h2>
<p>These are full, warm eau de parfums, so start with a spray or two on the neck and wrists rather than a cloud. They sit well on moisturised skin; our guide to <a href="/blogs/journal/layer-oud-with-body-butter">layering oud with body butter</a> shows how. For the wider family of Arabian scents, see our <a href="/blogs/journal/lattafa-khamrah-qahwa-arabian-perfume">Arabian perfume guide</a>.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Sizes vary by edition:</strong> Gold, Bleu, Carbon and White come in 60ml, 100ml and 200ml; check each listing for the size you want.</li>
<li><strong>As a gift:</strong> the warmer editions make a generous Christmas present. See our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a> for more ideas.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/al-haramain">Al Haramain</a> fragrance, browse <a href="/collections/arabian-perfume">Arabian perfume</a> and <a href="/collections/oud-perfume">oud perfume</a>, or see our <a href="/collections/scent-amber">amber fragrances</a>.</p>""",
    "faq": [
        ["Is there oud in Al Haramain Amber Oud?",
         "Amber Oud is the name of the line. The note lists we hold for these editions do not name oud; they are built on amber, woods, musk, vanilla and resins. For oud-led perfumes, see our oud perfume guide."],
        ["What is the difference between Al Haramain Amber Oud and the Gold Edition?",
         "In our listings both carry the same notes: bergamot and green notes, then melon, pineapple and amber, over vanilla, musk and woods. The brand sells them as two editions, so expect them to be close. The Gold Edition comes in 60ml, 100ml and 200ml."],
        ["Which Amber Oud edition is best for winter?",
         "The warm, spiced editions: Tobacco (tobacco, cinnamon, vanilla, cacao and tonka bean), Ruby (saffron, bitter almond and jasmine over ambergris) and Black (leather, amber and orange blossom over benzoin and vetiver)."],
        ["Is Al Haramain Amber Oud Carbon for men?",
         "It is sold as a men's fragrance: lavender, rosemary and bergamot, then sage, cedarwood and geranium, over vetiver, musk, amber and moss. Anyone who likes a fresh, herbal scent can wear it."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_amber_oud_2026-11-14.jsonl")

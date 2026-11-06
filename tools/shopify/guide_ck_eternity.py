"""Journal guide 'Calvin Klein Eternity for women vs for men: the difference explained' (user, 6 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): calvin klein eternity 4,400/mo
(KD 21), calvin klein eternity for women 2,900 (KD 16), calvin klein eternity for men 2,400 (KD 17), calvin klein
eternity eau de parfum 210. Facts = the scent notes and contents in our product descriptions. No 'long-lasting'
promises (the Eternity Parfum mini description says 'long-lasting finish': not repeated). Concentration ranges
described as typical. Prices are written into the text: re-run if prices change.

Usage: python3 tools/shopify/guide_ck_eternity.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_ck_eternity_2026-11-06.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Calvin Klein Eternity for women vs for men: the difference explained",
    "handle": "calvin-klein-eternity-for-women-vs-for-men",
    "tag": "Scent Studio",
    "summary": "Calvin Klein Eternity for women and Eternity for men compared: the notes, the strengths, the minis and how to choose.",
    "mt": "Calvin Klein Eternity for Women vs for Men | Swansura",
    "md": "Calvin Klein Eternity for women vs Eternity for men: the notes compared, eau de parfum vs eau de toilette, the Parfum and Aromatic Essence minis.",
    "pick": {
        "women": "calvin-klein-eternity-eau-de-parfum-women-s-classic-floral-fragrance",
        "men": "calvin-klein-eternity-for-men-eau-de-toilette-100ml-men-s-fresh-aromatic-fragrance",
        "parfum": "calvin-klein-eternity-parfum-10ml-miniature-men-s-warm-aromatic-fragrance",
        "ae-men": "calvin-klein-eternity-aromatic-essence-parfum-intense-10ml-miniature-men-s-aromatic-woody-fragrance",
        "ae-women": "calvin-klein-eternity-aromatic-essence-parfum-intense-10ml-miniature-women-s-aromatic-floral-fragrance",
        "set": "calvin-klein-women-s-miniature-fragrance-set-4x15ml-obsession-eternity-ck-one",
        "defy": "calvin-klein-defy-parfum-men-s-warm-woody-fragrance",
        "euphoria": "calvin-klein-my-euphoria-eau-de-parfum-10ml-miniature-women-s-floral-gourmand-fragrance",
    },
    "titles": {},
    "shop": ["women", "men", "parfum", "ae-women", "ae-men", "set", "defy", "euphoria"],
    "body": """<p><strong>Calvin Klein Eternity</strong> is a name shared by two classic fragrances: Eternity for women and Eternity for men. They sit side by side on the shelf, in similar clean, simple bottles, but they smell quite different. Here is what is in each one, how the strengths compare, and how to choose, whether for yourself or as a gift.</p>
<h2>Calvin Klein Eternity for women</h2>
<p>[[women|Calvin Klein Eternity Eau de Parfum]] ({{women}}, 30ml or 100ml) is a classic floral: fresh citrus at the start, a big bouquet of white and spring flowers in the middle, and a soft woody base.</p>
<ul>
<li><strong>Top:</strong> freesia, mandarin orange, sage and citrus.</li>
<li><strong>Heart:</strong> lily, carnation, violet, jasmine, rose, lily of the valley, marigold and narcissus.</li>
<li><strong>Base:</strong> sandalwood, amber, musk, heliotrope and patchouli.</li>
</ul>
<p>It is graceful, clean and easy to wear: a good everyday scent for the office, weddings and special days alike.</p>
<h2>Calvin Klein Eternity for men</h2>
<p>[[men|Calvin Klein Eternity for Men Eau de Toilette]] ({{men}}, 100ml) is a fresh aromatic fragrance: citrus and lavender first, then herbs, then warm woods.</p>
<ul>
<li><strong>Top:</strong> mandarin orange, lavender, bergamot and lemon.</li>
<li><strong>Heart:</strong> sage, juniper berries, basil, geranium, jasmine and coriander.</li>
<li><strong>Base:</strong> sandalwood, vetiver, musk, amber and Brazilian rosewood.</li>
</ul>
<p>It feels crisp and clean, with a warm finish, and suits daytime and work as well as evenings.</p>
<h2>Eternity for women vs for men: the key differences</h2>
<ul>
<li><strong>Character:</strong> the women's Eternity is floral, built around lily, carnation and rose. The men's is aromatic, built around lavender and herbs such as sage, juniper and basil.</li>
<li><strong>What they share:</strong> mandarin and sage near the top, and sandalwood, amber and musk in the base. That is why they feel like a pair.</li>
<li><strong>Strength:</strong> we stock the women's Eternity as an eau de parfum and the men's as an eau de toilette. An eau de parfum typically holds around 15–20% perfume oil and an eau de toilette around 5–15%, so the women's feels a little fuller on skin. Read <a href="/blogs/journal/extrait-vs-eau-de-parfum">what the labels mean</a>.</li>
<li><strong>Who can wear them:</strong> anyone. Many women enjoy the men's lavender freshness, and many men like the women's soft florals. Choose by the notes you love.</li>
</ul>
<h2>The newer Eternity scents, in miniature</h2>
<p>Calvin Klein has added deeper versions of Eternity. Our 10ml minis are an easy way to try them:</p>
<ul>
<li>[[parfum|Calvin Klein Eternity Parfum for men]] ({{parfum}}, 10ml): lavender and rum, warm spices and aromatic notes, then vanilla, woods and amber. Deeper and warmer than the classic men's EDT.</li>
<li>[[ae-men|Eternity Aromatic Essence Parfum Intense for men]] ({{ae-men}}, 10ml): juniper berry and fresh aromatic notes, lavender and a coconut accord, then cardamom, woods and amber.</li>
<li>[[ae-women|Eternity Aromatic Essence Parfum Intense for women]] ({{ae-women}}, 10ml): lavender and fresh aromatic notes, a floral and coconut heart, then amber, woods and musk.</li>
</ul>
<p>See all our <a href="/collections/travel-size-minis">travel-size minis</a>.</p>
<h2>Eternity as a gift</h2>
<p>For her, the [[set|Calvin Klein Women's Miniature Fragrance Set]] ({{set}}) holds four 15ml bottles: Eternity Eau de Parfum, CK One Eau de Toilette and two Obsession Eau de Parfum, so she can try three classic styles. For him, pair the Eternity for Men EDT with the Eternity Parfum mini for travel. More ideas in our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a>.</p>
<h2>If you like Eternity, try</h2>
<ul>
<li>[[defy|Calvin Klein Defy Parfum]] ({{defy}}): mandarin, pink pepper, lavender and a suede accord over vetiver, amber and woods. A modern pick for Eternity for Men fans who like lavender.</li>
<li>[[euphoria|Calvin Klein My Euphoria Eau de Parfum]] ({{euphoria}}, 10ml): a floral gourmand mini for women who want something sweeter than Eternity's clean florals.</li>
</ul>
<h2>How to wear it</h2>
<ul>
<li><strong>Spray on moisturised skin</strong> at the neck and chest; scent has more to hold on to. See <a href="/blogs/journal/how-to-use-body-butter">how to use a body butter</a>.</li>
<li><strong>Two or three sprays</strong> of eau de toilette, or one or two of eau de parfum or parfum, is a good start.</li>
<li><strong>Keep the bottle cool</strong> and out of sunlight.</li>
</ul>
<p>Shop all <a href="/collections/calvin-klein">Calvin Klein</a>, <a href="/collections/perfume-for-women">perfume for women</a> and <a href="/collections/perfume-for-men">perfume for men</a>, 100% authentic and dispatched from the UK.</p>""",
    "faq": [
        ["What is the difference between Calvin Klein Eternity for women and for men?",
         "Eternity for women is a floral eau de parfum with lily, carnation, rose and freesia over sandalwood and musk. Eternity for men is a fresh aromatic eau de toilette with lavender, citrus, sage and juniper over sandalwood and vetiver."],
        ["What does Calvin Klein Eternity for women smell like?",
         "Fresh citrus and freesia at the start, then a bouquet of lily, carnation, violet, jasmine and rose, and a soft base of sandalwood, amber and musk."],
        ["Can women wear Calvin Klein Eternity for men?",
         "Yes. Fragrance has no rules. Eternity for men's lavender, citrus and herbs suit anyone who likes fresh, clean scents."],
        ["Is there a Calvin Klein Eternity gift set?",
         "The Calvin Klein Women's Miniature Fragrance Set holds Eternity Eau de Parfum 15ml with CK One and two Obsession minis. For men, pair Eternity for Men EDT with the 10ml Eternity Parfum mini."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_ck_eternity_2026-11-06.jsonl")

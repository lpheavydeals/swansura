"""Journal guide 'Aftershave under £50: men's fragrances by scent type'
(user, 26 Nov 2026: 'Go ahead with barcodes and the two guides', from the ChatGPT + Google strategy).

Why this topic: Google and ChatGPT buyers in November chose men's eau de parfum under £60 on product
pages (Mercedes-Benz Club Black, Chopard Oud Malaki, Mugler Alien Man set). 'Aftershave for men',
'men's aftershave under £50' and Christmas 'gift for him' questions are budget questions AI assistants
answer with a short list; this gives one grouped by scent type. Facts = stored custom.sw notes
(Admin read 26 Nov) or each description's 'Fragrance notes' list. NO PRICES in the text (band only).

Usage: python3 tools/shopify/guide_aftershave_under_50.py <storefront products dump dir>
Output: docs/seo/guide_aftershave_under_50_2026-11-26.jsonl
"""
import glob
import json
import sys

from journal_lib import build

A = {
    "title": "Aftershave under £50: men's fragrances by scent type",
    "handle": "aftershave-under-50",
    "tag": "Gift guide",
    "summary": "Designer and Arabian men's fragrances under £50, grouped by scent: fresh, woody, warm and sweet, and leather. With the notes in each, so you can pick one for yourself or as a gift.",
    "mt": "Aftershave Under £50: Men's Fragrances by Scent | Swansura",
    "md": "Men's aftershave under £50 in the UK: Azzaro, Davidoff, Calvin Klein, Mercedes-Benz, Joop!, Ferragamo and Rasasi, grouped by scent type with notes.",
    "pick": {
        "chrome": "azzaro-chrome-legend-eau-de-toilette-75ml-men-s-fresh-aromatic-fragrance",
        "eternity": "calvin-klein-eternity-for-men-eau-de-toilette-100ml-men-s-fresh-aromatic-fragrance",
        "desireblue": "dunhill-desire-blue-eau-de-toilette-100ml-men-s-fresh-aquatic-fragrance",
        "champion": "davidoff-champion-eau-de-toilette-90ml-men-s-fresh-woody-aromatic-fragrance",
        "game": "davidoff-the-game-eau-de-toilette-100ml-men-s-woody-aromatic-fragrance",
        "hunter": "armaf-hunter-eau-de-parfum-100ml-men-s-fresh-woody-aromatic-fragrance",
        "private": "mercedes-benz-man-private-eau-de-parfum-100ml",
        "aventure": "al-haramain-l-aventure-eau-de-parfum-100ml-men-s-fresh-woody-fragrance",
        "clubblack": "mercedes-benz-club-black-eau-de-parfum-100ml",
        "joop": "joop-homme-le-parfum-75ml-men-s-warm-spicy-amber-fragrance",
        "hawas": "rasasi-hawas-elixir-eau-de-parfum-100ml",
        "uomo": "salvatore-ferragamo-uomo-eau-de-toilette-100ml",
        "khamrah": "lattafa-khamrah-qahwa-eau-de-parfum-100ml",
        "leather": "dunhill-signature-collection-british-leather-eau-de-parfum-100ml-men-s-leather-woody-fragrance",
        "polored": "ralph-lauren-polo-red-parfum-75ml",
        "cavalli": "roberto-cavalli-uomo-parfum-100ml",
    },
    "titles": {},
    "shop": ["clubblack", "chrome", "game", "joop", "hawas", "uomo", "eternity", "private"],
    "body": """<p><strong>A good aftershave does not need a big budget.</strong> Every men's fragrance below is under £50 at Swansura at the time of writing. In the UK 'aftershave' usually means a men's eau de toilette or eau de parfum spray, and that is what these are. We have grouped them by scent type, with the notes in each, so you can choose one for yourself or as a gift.</p>
<h2>Fresh and clean</h2>
<p>Citrus, herbs and light woods. Easy for every day, the office and warmer weather.</p>
<ul>
<li>[[chrome|Azzaro Chrome Legend Eau de Toilette]] (75ml): green apple, tea and bitter orange, then moss and tonka bean, over cedarwood and musk.</li>
<li>[[eternity|Calvin Klein Eternity for Men Eau de Toilette]] (100ml): mandarin, lavender and bergamot, then sage, juniper and geranium, over sandalwood, vetiver and musk. Our <a href="/blogs/journal/calvin-klein-eternity-for-women-vs-for-men">Eternity guide</a> compares it with the women's version.</li>
<li>[[desireblue|Dunhill Desire Blue Eau de Toilette]] (100ml): bergamot and citrus, then lotus and marine notes, over amber, musk and woods.</li>
<li>[[champion|Davidoff Champion Eau de Toilette]] (90ml): lemon and bergamot, then clary sage and galbanum, over cedarwood and oakmoss.</li>
</ul>
<h2>Woody and aromatic</h2>
<p>Herbs and spice over cedar, vetiver or patchouli. Smart without being heavy.</p>
<ul>
<li>[[game|Davidoff The Game Eau de Toilette]] (100ml): juniper berries, then iris, over ebony wood. Short and simple.</li>
<li>[[private|Mercedes-Benz Man Private Eau de Parfum]] (100ml): cardamom, cypress and artemisia, then lavender, labdanum and ambroxan, over cashmere wood, cedar and patchouli.</li>
<li>[[hunter|Armaf Hunter Eau de Parfum]] (100ml): grapefruit, mandarin, rosemary and cardamom, then tuberose and olibanum, over cedarwood, vetiver and musk.</li>
<li>[[aventure|Al Haramain L'Aventure Eau de Parfum]] (100ml): lemon, bergamot and elemi, then jasmine and woody notes, over patchouli, amber and musk.</li>
</ul>
<h2>Warm, spicy and sweet</h2>
<p>Vanilla, tonka and spice. Best for evenings, colder months and anyone who likes a richer trail.</p>
<ul>
<li>[[clubblack|Mercedes-Benz Club Black Eau de Parfum]] (100ml): bergamot, then incense and jasmine, over vanilla, benzoin, ambroxan and woods. Smoky-sweet.</li>
<li>[[joop|Joop! Homme Le Parfum]] (75ml): lavender and cinnamon, then orange blossom and tonka bean, over vanilla, amber and woods.</li>
<li>[[hawas|Rasasi Hawas Elixir Eau de Parfum]] (100ml): mugwort, bergamot and mint, then dark chocolate, lavender and benzoin, over vanilla, tonka and white musk.</li>
<li>[[uomo|Salvatore Ferragamo Uomo Eau de Toilette]] (100ml): bergamot, black pepper and cardamom, then orange blossom and a tiramisu note, over sandalwood, cashmere wood and tonka.</li>
<li>[[khamrah|Lattafa Khamrah Qahwa Eau de Parfum]] (100ml, unisex): cinnamon, cardamom and ginger, then praline and candied fruits, over coffee, vanilla and tonka. Our <a href="/blogs/journal/lattafa-khamrah-qahwa-arabian-perfume">Khamrah Qahwa guide</a> has more.</li>
</ul>
<h2>Leather and dark woods</h2>
<ul>
<li>[[leather|Dunhill Signature Collection British Leather]] (100ml): bergamot, citrus and herbs, then leather and spices, over vetiver, patchouli, amber and woods.</li>
<li>[[polored|Ralph Lauren Polo Red Parfum]] (75ml): bergamot, blood orange and pink pepper, then orris, absinthe and lavender, over musk, cedar and opoponax.</li>
<li>[[cavalli|Roberto Cavalli Uomo Parfum]] (100ml): bergamot and citron, then black pepper, saffron and violet, over ambroxan, musk and woods.</li>
</ul>
<p>Prefer oud? See the oud perfumes in our <a href="/collections/oud-perfume">oud collection</a> and our <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a>.</p>
<h2>Which one should you choose?</h2>
<ul>
<li><strong>For every day and the office:</strong> Azzaro Chrome Legend or CK Eternity for Men.</li>
<li><strong>Smart, woody and versatile:</strong> Mercedes-Benz Man Private or Davidoff The Game.</li>
<li><strong>Evenings and winter:</strong> Mercedes-Benz Club Black, Joop! Homme Le Parfum or Rasasi Hawas Elixir.</li>
<li><strong>Something different:</strong> Ralph Lauren Polo Red Parfum or Dunhill British Leather.</li>
</ul>
<h2>Buying it as a gift</h2>
<p>If you are not sure of his taste, a fresh scent is the safest choice; a warm, sweet one is a better pick for someone who already wears a rich fragrance. For a boxed present, see our <a href="/collections/aftershave-gift-sets-for-him">aftershave gift sets for him</a> and <a href="/collections/gifts-under-50">gifts under £50</a>, or browse every <a href="/collections/perfume-for-men">men's fragrance</a>. All are 100% authentic and ship from the UK, with free UK delivery over £40.</p>""",
    "faq": [
        ["What is a good aftershave under £50?",
         "For a fresh everyday scent, Azzaro Chrome Legend or Calvin Klein Eternity for Men. For a woody one, Mercedes-Benz Man Private or Davidoff The Game. For a warm, sweet evening scent, Mercedes-Benz Club Black, Joop! Homme Le Parfum or Rasasi Hawas Elixir."],
        ["Is aftershave the same as eau de toilette?",
         "In the UK 'aftershave' is often used for any men's fragrance spray. The fragrances in this guide are eau de toilette, eau de parfum or parfum. An after-shave balm is a separate skincare product."],
        ["What is the difference between eau de toilette and eau de parfum?",
         "An eau de parfum usually carries a higher concentration of fragrance oils than an eau de toilette, so it feels richer. Our guide to extrait vs eau de parfum explains the labels."],
        ["Are these men's fragrances authentic?",
         "Yes. Every fragrance at Swansura is 100% authentic and ships from the UK, with free UK delivery over £40."],
    ],
}

if __name__ == "__main__":
    ALL = {}
    for f in glob.glob(sys.argv[1] + "/*.json"):
        d = json.load(open(f))
        if isinstance(d, dict) and "products" in d:
            for p in d["products"]:
                ALL[p["handle"]] = p
    build(A, ALL, "guide_aftershave_under_50_2026-11-26.jsonl")

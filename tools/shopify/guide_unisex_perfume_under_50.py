"""Journal guide 'Unisex perfume under £50: scents to share, by mood'
(user, 28 Nov 2026: 'Go ahead with the two guides').

Every scent below was in stock at £50 or less (smallest size) on the storefront on 28 Nov 2026 and sits in
unisex-perfume. Facts = each description's notes list. anatomē left out (claim-style names).
NO PRICES in the text (band only).

Usage: python3 tools/shopify/guide_unisex_perfume_under_50.py <storefront products dump dir>
Output: docs/seo/guide_unisex_perfume_under_50_2026-11-28.jsonl
"""
import glob
import json
import sys

from journal_lib import build

A = {
    "title": "Unisex perfume under £50: scents to share, by mood",
    "handle": "unisex-perfume-under-50",
    "tag": "Gift guide",
    "summary": "Unisex perfumes under £50 that suit men and women alike, grouped by mood: fresh and citrus, rose, sweet and gourmand, and warm amber and incense. With the notes in each.",
    "mt": "Unisex Perfume Under £50: Scents to Share by Mood | Swansura",
    "md": "Unisex perfume under £50 in the UK: Acqua di Parma, Chopard, Al Haramain, Lattafa, Korloff, Elie Saab and S.T. Dupont, grouped by mood with notes.",
    "pick": {
        "colonia": "acqua-di-parma-colonia-pura-eau-de-cologne-20ml-unisex",
        "dive": "afnan-9am-dive-eau-de-parfum-100ml",
        "pacific": "maison-alhambra-pacific-blue-porto-neroli-eau-de-parfum-80ml",
        "bleu": "al-haramain-amber-oud-bleu-edition-eau-de-parfum-60ml-luxury-unisex-fresh-woody-fragrance",
        "sandalo": "acqua-di-parma-sandalo-edp-20ml-unisex",
        "royalrose": "korloff-royal-rose-eau-de-parfum-88ml",
        "elierose": "elie-saab-la-collection-des-essences-no-1-rose-eau-de-parfum-100ml-luxury-unisex-rose-fragrance",
        "infini": "maison-alhambra-infini-rose-eau-de-parfum-100ml",
        "zafferano": "acqua-di-parma-zafferano-edp-20ml-unisex",
        "khamrah": "lattafa-khamrah-qahwa-eau-de-parfum-100ml",
        "teriaq": "lattafa-teriaq-eau-de-parfum-100ml",
        "gold": "al-haramain-amber-oud-gold-edition-eau-de-parfum-luxury-unisex-fruity-amber-fragrance",
        "tea": "fomo-fraglovers-tea-extrait-de-parfum-100ml",
        "lalique": "lalique-noir-premier-or-intemporel-1888-eau-de-parfum-100ml",
        "amalaki": "chopard-amber-malaki-eau-de-parfum-80ml-luxury-unisex-amber-fragrance",
        "incense": "chopard-black-incense-malaki-eau-de-parfum-80ml-luxury-unisex-incense-fragrance",
        "tobacco": "al-haramain-amber-oud-tobacco-edition-eau-de-parfum-60ml-luxury-unisex-spicy-tobacco-fragrance",
        "perfect": "s-t-dupont-perfect-tobacco-eau-de-parfum-100ml-unisex-woody-spicy-tobacco-fragrance",
        "royalamber": "s-t-dupont-royal-amber-eau-de-parfum-100ml-unisex-amber-woody-fragrance",
        "musk": "al-haramain-amber-musk-eau-de-parfum-100ml-luxury-unisex-amber-musk-fragrance",
        "leather": "fumeri-smokey-leather-unisex-eau-de-parfum-100ml",
    },
    "titles": {},
    "shop": ["colonia", "dive", "royalrose", "khamrah", "amalaki", "gold", "elierose", "perfect"],
    "body": """<p><strong>A unisex perfume is the easiest scent to share, and the safest one to give.</strong> Every fragrance below is sold for men and women alike and was under £50 at Swansura at the time of writing (for scents sold in more than one size, at least the smallest size is). We have grouped them by mood, with the notes in each.</p>
<h2>Fresh and citrus</h2>
<p>Citrus, herbs and clean woods. Easy for every day, the office and warmer weather.</p>
<ul>
<li>[[colonia|Acqua di Parma Colonia Pura]] (20ml eau de cologne): bergamot, orange and petitgrain, then jasmine, narcissus and coriander, over musk, cedarwood and patchouli. Our <a href="/blogs/journal/acqua-di-parma-guide">Acqua di Parma guide</a> compares the range.</li>
<li>[[dive|Afnan 9am Dive]] (100ml eau de parfum): lemon, mint, pink pepper and blackcurrant, then apple, incense and cedarwood, over patchouli, ginger and sandalwood.</li>
<li>[[pacific|Maison Alhambra Pacific Blue]] (80ml eau de parfum): bergamot, mandarin, lemon and lavender, then orange blossom, jasmine and neroli, over amber and ambrette.</li>
<li>[[bleu|Al Haramain Amber Oud Bleu Edition]] (from 60ml): grapefruit, lemon and mint, then ginger, nutmeg and jasmine, over incense, vetiver, sandalwood and white musk.</li>
<li>[[sandalo|Acqua di Parma Sandalo]] (20ml eau de parfum): bergamot, lemon and orange, then cardamom and lavender, over sandalwood, amber and tonka bean.</li>
</ul>
<h2>Rose</h2>
<ul>
<li>[[royalrose|Korloff Royal Rose]] (88ml eau de parfum): bergamot, mandarin and pink pepper, then rose, elemi and incense, over sandalwood, patchouli and woods.</li>
<li>[[elierose|Elie Saab La Collection des Essences No. 1 Rose]] (100ml eau de parfum): rose and soft florals over amber, woods and musk. Elegant rather than sweet.</li>
<li>[[infini|Maison Alhambra Infini Rose]] (100ml eau de parfum): bergamot and pink pepper, then Bulgarian rose, Turkish rose and jasmine, over vanilla and amber.</li>
<li>[[zafferano|Acqua di Parma Zafferano]] (20ml eau de parfum): bergamot, bitter orange and coriander, then saffron, rose and jasmine, over tonka bean, vanilla and woods.</li>
</ul>
<h2>Sweet and gourmand</h2>
<p>Spice, coffee, caramel and vanilla. Cosy, and best in the colder months.</p>
<ul>
<li>[[khamrah|Lattafa Khamrah Qahwa]] (100ml eau de parfum): cinnamon, cardamom and ginger, then praline and candied fruits, over coffee, vanilla and tonka. Our <a href="/blogs/journal/lattafa-khamrah-qahwa-arabian-perfume">Khamrah Qahwa guide</a> has more.</li>
<li>[[teriaq|Lattafa Teriaq]] (100ml eau de parfum): caramel, bitter almond and apricot, then honey, rhubarb and rose, over leather, vanilla and labdanum.</li>
<li>[[gold|Al Haramain Amber Oud Gold Edition]] (from 60ml): bergamot, then melon, pineapple and amber, over vanilla, musk and woods. Our <a href="/blogs/journal/al-haramain-amber-oud-editions">Amber Oud editions guide</a> compares every one.</li>
<li>[[tea|Fomo Fraglover's Tea]] (100ml extrait de parfum): tea, bergamot and cardamom, then fig, jasmine and osmanthus, over tobacco, tonka and sandalwood.</li>
<li>[[lalique|Lalique Noir Premier Or Intemporel 1888]] (100ml eau de parfum): bergamot, black pepper and cardamom, then coffee, tobacco and violet, over patchouli, tolu balsam and vanilla.</li>
</ul>
<h2>Warm amber, incense and tobacco</h2>
<p>Resins, smoke and woods. For evenings, winter and special occasions.</p>
<ul>
<li>[[amalaki|Chopard Amber Malaki]] (80ml eau de parfum): orange blossom and frankincense, then amber and papyrus, over labdanum and Bourbon vanilla.</li>
<li>[[incense|Chopard Black Incense Malaki]] (80ml eau de parfum): incense and spices, then oud and leather, over amber, woods and resins.</li>
<li>[[tobacco|Al Haramain Amber Oud Tobacco Edition]] (60ml eau de parfum): tobacco leaf, cinnamon and black pepper, then vanilla, clove and cacao, over tobacco, dried fruits and woods.</li>
<li>[[perfect|S.T. Dupont Perfect Tobacco]] (100ml eau de parfum): spices, then a sweet tobacco heart with a floral side, over amber, woods and vanilla.</li>
<li>[[royalamber|S.T. Dupont Royal Amber]] (100ml eau de parfum): spices, then amber and resins, over woods, musk and vanilla.</li>
<li>[[musk|Al Haramain Amber Musk]] (100ml eau de parfum): amber and florals, then musk and woods, over vanilla and resins. A soft, close scent.</li>
<li>[[leather|Fumeri Smokey Leather]] (100ml eau de parfum): warm spices and smoky accords, then leather, cedarwood and amber, over musk, dark woods and sandalwood.</li>
</ul>
<p>Prefer oud? See our <a href="/blogs/journal/oud-perfume-under-60">oud perfume under £60 guide</a>.</p>
<h2>Which one should you choose?</h2>
<ul>
<li><strong>For every day and the office:</strong> Acqua di Parma Colonia Pura or Afnan 9am Dive.</li>
<li><strong>A gift when you are not sure:</strong> Korloff Royal Rose or Al Haramain Amber Musk.</li>
<li><strong>Something sweet and cosy:</strong> Lattafa Khamrah Qahwa or Al Haramain Amber Oud Gold.</li>
<li><strong>Evenings and winter:</strong> Chopard Amber Malaki or S.T. Dupont Perfect Tobacco.</li>
</ul>
<h2>Buying it as a gift</h2>
<p>A unisex scent suits a couple to share, or anyone whose taste you do not know well. For a boxed present, see our <a href="/blogs/journal/perfume-gift-sets-under-30">perfume gift sets under £30 guide</a>; for single bottles by gender, our <a href="/blogs/journal/womens-perfume-under-50">women's perfume under £50</a> and <a href="/blogs/journal/aftershave-under-50">aftershave under £50</a> guides. Browse every <a href="/collections/unisex-perfume">unisex perfume</a> and <a href="/collections/gifts-under-50">gift under £50</a>. All are 100% authentic and ship from the UK, with free UK delivery over £40.</p>""",
    "faq": [
        ["What is a good unisex perfume under £50?",
         "For a fresh everyday scent, Acqua di Parma Colonia Pura or Afnan 9am Dive. For rose, Korloff Royal Rose. For something sweet, Lattafa Khamrah Qahwa. For a warm evening scent, Chopard Amber Malaki or S.T. Dupont Perfect Tobacco."],
        ["What makes a perfume unisex?",
         "A unisex perfume is sold for men and women alike. Fresh citrus, woody, amber and incense scents are often unisex; any perfume can be worn by anyone who likes it."],
        ["What is the difference between eau de toilette, eau de parfum and extrait?",
         "They differ in concentration of fragrance oils: eau de toilette is usually the lightest, eau de parfum richer, and extrait de parfum the richest. Our guide to extrait vs eau de parfum explains the labels."],
        ["Are these unisex perfumes authentic?",
         "Yes. Every perfume at Swansura is 100% authentic and ships from the UK, with free UK delivery over £40."],
    ],
}

if __name__ == "__main__":
    ALL = {}
    for f in glob.glob(sys.argv[1] + "/*.json"):
        d = json.load(open(f))
        if isinstance(d, dict) and "products" in d:
            for p in d["products"]:
                ALL[p["handle"]] = p
    build(A, ALL, "guide_unisex_perfume_under_50_2026-11-28.jsonl")

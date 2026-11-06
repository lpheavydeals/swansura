"""Journal guide 'Lattafa Khamrah Qahwa and Arabian perfume: a guide to the notes' (user, 6 Nov 2026).

Target keywords (Semrush UK; seo/Swansura_Product_SEO_Merged_2026-11-02.xlsx 'Top new products' / 'Brand
searches', seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): lattafa khamrah qahwa 5,400/mo (KD 23), lattafa
perfume 2,400 (KD 24), arabiyat prestige nyla 1,300 (KD 15), lattafa teriaq 590, afnan 9am dive 480, maison
alhambra perfume 390, afnan perfume 390, oud perfume uk 170.

The Lattafa / Afnan / Arabiyat Prestige / Maison Alhambra products added on 2 Nov 2026 were all sold out on
6 Nov 2026 (stock 0), so they are linked in the text only ('soldout'); 'Shop the story' uses in-stock Al
Haramain, Fumeri, SAP, La Maison de la Vanille and Montale. Maison Alhambra has no photos yet: brand collection
link only. Facts = the scent notes in our product descriptions. No 'long-lasting' / projection promises; no
'dupe' or 'smells like' comparisons. Prices are written into the text: re-run if prices change.

Usage: python3 tools/shopify/guide_arabian_perfume.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_arabian_perfume_2026-11-06.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Lattafa Khamrah Qahwa and Arabian perfume: a guide to the notes",
    "handle": "lattafa-khamrah-qahwa-arabian-perfume",
    "tag": "Scent Studio",
    "summary": "Lattafa Khamrah Qahwa's notes explained, plus Arabian perfume from Lattafa, Afnan, Al Haramain and more, and how to choose.",
    "mt": "Lattafa Khamrah Qahwa & Arabian Perfume Guide | Swansura",
    "md": "Lattafa Khamrah Qahwa's coffee, spice and praline notes explained, plus Lattafa, Afnan and Al Haramain Arabian perfumes and how to choose one.",
    "soldout": ["kq", "teriaq", "yara", "maahir", "dive", "supremacy", "nyla"],
    "pick": {
        "kq": "lattafa-khamrah-qahwa-eau-de-parfum-100ml", "teriaq": "lattafa-teriaq-eau-de-parfum-100ml",
        "yara": "lattafa-yara-candy-eau-de-parfum-100ml", "maahir": "lattafa-maahir-black-edition-eau-de-parfum-100ml",
        "dive": "afnan-9am-dive-eau-de-parfum-100ml", "supremacy": "afnan-supremacy-gold-eau-de-parfum-100ml",
        "nyla": "arabiyat-prestige-nyla-eau-de-parfum-80ml",
        "tobacco": None, "gold": None, "black": None, "ruby": None, "musk": None,
        "fumeri": "fumeri-oud-saffron-for-men-eau-de-parfum-100ml", "sap": "sap-saffron-oud-extrait-de-parfum-100ml",
        "royal": "la-maison-de-la-vanille-royal-oud-eau-de-parfum-100ml",
        "montale": "montale-aoud-safran-eau-de-parfum-100ml-luxury-unisex-saffron-oud-fragrance",
    },
    "titles": {
        "tobacco": "Al Haramain Amber Oud Tobacco Edition", "gold": "Al Haramain Amber Oud Gold Edition",
        "black": "Al Haramain Amber Oud Black Edition", "ruby": "Al Haramain Amber Oud Ruby Edition",
        "musk": "Al Haramain Amber Musk",
    },
    "shop": ["tobacco", "gold", "black", "ruby", "musk", "fumeri", "royal", "montale"],
    "body": """<p>Few perfumes have travelled by word of mouth like <strong>Lattafa Khamrah Qahwa</strong>. It belongs to a wave of Arabian perfume houses, from Lattafa and Afnan to Al Haramain, Arabiyat Prestige and Maison Alhambra, whose rich, warm scents have found a big following in the UK. Here is what is in Khamrah Qahwa, what makes a perfume "Arabian", and how to choose one.</p>
<h2>What does Lattafa Khamrah Qahwa smell like?</h2>
<p>"Qahwa" is the Arabic word for coffee, and that is the idea at the heart of [[kq|Lattafa Khamrah Qahwa Eau de Parfum]] ({{kq}}, 100ml). Its notes, from top to base:</p>
<ul>
<li><strong>Top:</strong> cinnamon, cardamom and ginger, the spices of Arabic coffee.</li>
<li><strong>Heart:</strong> praline, candied fruits and white flowers.</li>
<li><strong>Base:</strong> coffee, vanilla, tonka bean, benzoin and musk.</li>
</ul>
<p>So it opens spicy, turns sweet and nutty, and settles into coffee and vanilla. It is an amber-woody, gourmand scent made for men and women, and it suits cooler months and evenings best.</p>
<h2>More from Lattafa</h2>
<p><strong>Lattafa perfume</strong> is known for warm, generous scents at friendly prices. Alongside Khamrah Qahwa, we list:</p>
<ul>
<li>[[teriaq|Lattafa Teriaq]] ({{teriaq}}): caramel, bitter almond, pink pepper and apricot, then honey, rhubarb and rose over leather, vanilla and musk. Unisex.</li>
<li>[[maahir|Lattafa Maahir Black Edition]] ({{maahir}}): black and pink pepper with saffron, then labdanum and cade oil over leather, cedarwood, guaiac wood and patchouli. A darker, smoky choice.</li>
<li>[[yara|Lattafa Yara Candy]] ({{yara}}): green mandarin and blackcurrant, a strawberry-candy and gardenia heart, and vanilla, musk and sandalwood. Made for women.</li>
</ul>
<p>See every Lattafa scent on the <a href="/collections/lattafa">Lattafa page</a>.</p>
<h2>Afnan, Arabiyat Prestige and Maison Alhambra</h2>
<p>[[dive|Afnan 9am Dive]] ({{dive}}) is the fresh one: lemon, mint, pink pepper and blackcurrant, then apple, incense and cedarwood. [[supremacy|Afnan Supremacy Gold]] ({{supremacy}}) is warmer, with nutmeg, violet and peach blossom over amber, vanilla, oud and benzoin. More on the <a href="/collections/afnan">Afnan page</a>.</p>
<p>[[nyla|Arabiyat Prestige Nyla]] ({{nyla}}, 80ml) is a bright floral-fruity scent for women: coconut, peach and mandarin, then tiare, jasmine and rose over white musk. See <a href="/collections/arabiyat-prestige">Arabiyat Prestige</a>. <a href="/collections/maison-alhambra">Maison Alhambra</a> adds a wide range of floral, fruity and woody eau de parfums at friendly prices.</p>
<h2>What makes a perfume "Arabian"?</h2>
<p>There is no strict rule, but Arabian perfume usually leans on a few ingredients:</p>
<ul>
<li><strong>Oud</strong> (agarwood): a deep, woody, slightly smoky note.</li>
<li><strong>Amber and resins</strong> such as benzoin and labdanum: warm and sweet.</li>
<li><strong>Saffron, cardamom and cinnamon:</strong> spice.</li>
<li><strong>Rose and musk:</strong> soft and rounded.</li>
</ul>
<p>Most of the scents above are eau de parfum, which typically holds around 15–20% perfume oil. Read <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> for what each label means.</p>
<h2>Arabian perfume in stock now</h2>
<h3>Warm and spicy</h3>
<p>[[tobacco|Al Haramain Amber Oud Tobacco Edition]] ({{tobacco}}, 60ml) shares Khamrah Qahwa's love of spice: tobacco leaf, cinnamon, black pepper and ginger, then vanilla, clove, star anise, cacao and tonka bean. [[black|Al Haramain Amber Oud Black Edition]] ({{black}}) pairs cardamom and lavender with leather, amber and benzoin.</p>
<h3>Sweet and fruity</h3>
<p>[[gold|Al Haramain Amber Oud Gold Edition]] ({{gold}}) is bergamot, melon and pineapple over vanilla and musk, a popular first Arabian perfume. [[ruby|Al Haramain Amber Oud Ruby Edition]] ({{ruby}}) mixes saffron and bitter almond with jasmine and ambergris. [[musk|Al Haramain Amber Musk]] ({{musk}}) is softer: amber, musk, vanilla and resins.</p>
<h3>Oud and saffron</h3>
<p>[[fumeri|Fumeri Oud Saffron]] ({{fumeri}}) and [[sap|SAP Saffron Oud Extrait de Parfum]] ({{sap}}) both open on saffron and spice before oud, cedarwood and smoky woods, with amber, leather and musk. [[montale|Montale Aoud Safran]] ({{montale}}) builds on saffron and oud with rose and amber, while [[royal|La Maison de la Vanille Royal Oud]] ({{royal}}) softens oud with Turkish rose and jasmine.</p>
<p>Browse all <a href="/collections/arabian-perfume">Arabian perfume</a> and <a href="/collections/oud-perfume">oud perfume</a>.</p>
<h2>How to wear a rich, warm perfume</h2>
<ul>
<li><strong>Start small:</strong> one or two sprays on the neck or wrists. You can add more; you cannot take it away.</li>
<li><strong>Spray on moisturised skin,</strong> so the scent has something to sit on. We explain how in <a href="/blogs/journal/layer-oud-with-body-butter">how to layer oud with body butter</a>.</li>
<li><strong>Try it on skin before you decide.</strong> Warm notes change over the first hour, so judge the base, not just the first spray.</li>
<li><strong>Patch test</strong> if your skin is sensitive to fragrance.</li>
</ul>
<p>Arabian perfume also makes a generous gift: see our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a>.</p>""",
    "faq": [
        ["What does Lattafa Khamrah Qahwa smell like?",
         "It opens with cinnamon, cardamom and ginger, turns sweet with praline, candied fruits and white flowers, and settles into coffee, vanilla, tonka bean, benzoin and musk. It is a warm, gourmand amber-woody scent for men and women."],
        ["Is Lattafa Khamrah Qahwa for men or women?",
         "Both. Lattafa makes it as a unisex eau de parfum in a 100ml bottle."],
        ["What is Arabian perfume?",
         "Perfume in the Middle Eastern style, usually built on oud, amber, resins such as benzoin, spices like saffron and cardamom, rose and musk. Lattafa, Afnan, Al Haramain, Arabiyat Prestige and Maison Alhambra are well-known houses."],
        ["How many sprays of an Arabian perfume should I use?",
         "Start with one or two sprays on the neck or wrists, on moisturised skin. Rich, warm scents are often best worn lightly at first."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_arabian_perfume_2026-11-06.jsonl")

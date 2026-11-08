"""Journal guide 'Oud perfume: Tom Ford Oud Wood, Gucci Intense Oud and other oud fragrances' (user, 8 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): tom ford oud wood 18,100/mo (KD 16),
gucci intense oud 6,600 (KD 21), chopard oud malaki 590 (KD 17), guerlain oud essentiel 590 (KD 19),
tom ford oud wood eau de parfum 320, oud perfume uk 170, gucci intense oud review 140, oud perfume for women uk 50,
oud perfume for men uk 30. Facts = the products' stored key notes (8 Nov 2026). Left out: 'long-lasting',
'lasting presence', 'dupe' / 'smells like' comparisons, performance claims. The Arabian guide (Lattafa / Al Haramain
Gold, Ruby, Tobacco, Black, Montale Aoud Safran) and the oud layering article are linked, not repeated.
Tom Ford Oud Wood has two listings (50ml at £124.99 and a 30/50ml listing with 50ml at £164.99): the guide links
the 30/50ml one; the price difference is flagged for the client. Prices are written into the text: re-run the
generator and update the body if prices change.

Usage: python3 tools/shopify/guide_oud_perfume.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_oud_perfume_2026-11-08.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Oud perfume: Tom Ford Oud Wood, Gucci Intense Oud and other oud fragrances",
    "handle": "oud-perfume-guide",
    "tag": "Scent Studio",
    "summary": "What oud is, how Tom Ford Oud Wood, Gucci Intense Oud, Guerlain, Chopard and Montale use it, and how to choose and wear an oud perfume.",
    "mt": "Oud Perfume Guide: Tom Ford Oud Wood & Gucci | Swansura",
    "md": "What oud smells like, and how Tom Ford Oud Wood, Gucci Intense Oud, Guerlain Oud Essentiel, Chopard Oud Malaki and Montale compare. Notes, prices, tips.",
    "pick": {
        "tf": "tom-ford-oud-wood-eau-de-parfum-50ml-unisex",
        "gucci": "gucci-intense-oud-eau-de-parfum-90ml-luxury-unisex-oud-fragrance",
        "guerlain": "guerlain-oud-essentiel-eau-de-parfum-125ml-luxury-unisex-oud-woody-fragrance",
        "chopard": "chopard-oud-malaki-eau-de-parfum-80ml-luxury-men-s-oud-fragrance",
        "damascus": "montale-aoud-damascus-eau-de-parfum-100ml-women-s-rose-oud-fragrance",
        "white": "al-haramain-amber-oud-white-edition-eau-de-parfum-luxury-women-s-floral-oriental-fragrance",
        "carbon": "al-haramain-amber-oud-carbon-edition-eau-de-parfum-men-s-fresh-woody-fragrance",
        "bleu": "al-haramain-amber-oud-bleu-edition-eau-de-parfum-60ml-luxury-unisex-fresh-woody-fragrance",
    },
    "titles": {},
    "shop": ["tf", "gucci", "guerlain", "chopard", "damascus", "white", "carbon", "bleu"],
    "body": """<p><strong>Oud</strong> is one of the most talked-about notes in perfume: deep, woody and a little smoky. Designer houses such as Tom Ford, Gucci, Guerlain and Chopard each have their own take on it. Here is what oud is, how the best-known <strong>oud perfumes</strong> differ, and how to choose and wear one.</p>
<h2>What is oud?</h2>
<p>Oud, also called agarwood or aoud, is a dark, fragrant resin that forms in the wood of agar (Aquilaria) trees. It has been treasured in the Middle East and South Asia for centuries, burned as incense and worn as an oil. Natural oud is rare, so many modern perfumes use an <em>oud accord</em>: a blend of woods, resins and leathery notes built to give the same rich effect. Gucci, for example, lists an oud accord in its base notes.</p>
<h2>Tom Ford Oud Wood</h2>
<p>[[tf|Tom Ford Oud Wood Eau de Parfum]] ({{tf}}, 30ml or 50ml) is the gentlest way into oud. Its key notes are oud wood, rosewood and cardamom over sandalwood, vetiver, tonka bean and amber, so the oud reads smooth and warm rather than smoky. It is unisex and easy to wear in the office or in the evening. See every <a href="/collections/tom-ford">Tom Ford</a> fragrance.</p>
<h2>Gucci Intense Oud</h2>
<p>[[gucci|Gucci Intense Oud Eau de Parfum]] ({{gucci}}, 90ml) is darker. Black pepper and olibanum (frankincense) open it; amber woods, sandalwood and cedarwood sit at the heart; leather, patchouli, gurjun balsam and the oud accord form the base. Expect incense and leather more than sweetness. Shop all <a href="/collections/gucci">Gucci</a>.</p>
<h2>Tom Ford Oud Wood or Gucci Intense Oud?</h2>
<ul>
<li><strong>Choose Oud Wood</strong> if you want a soft, creamy wood with a touch of spice that suits everyday wear.</li>
<li><strong>Choose Intense Oud</strong> if you like incense, leather and a bolder, smokier trail for evenings and colder months.</li>
</ul>
<h2>Three more oud perfumes</h2>
<ul>
<li>[[guerlain|Guerlain Oud Essentiel]] ({{guerlain}}, 125ml): saffron and pelargonium, then rose, oud and cedarwood over leather, frankincense and guaiac wood. A rose-and-leather oud, made unisex.</li>
<li>[[chopard|Chopard Oud Malaki]] ({{chopard}}, 80ml): grapefruit, lavender and artemisia, then tobacco, spices and leather over oud, ambergris and dark woods. Made for men, and the most affordable oud in this guide.</li>
<li>[[damascus|Montale Aoud Damascus]] ({{damascus}}, 100ml): damask rose, aoud and saffron with amber, woods and musk. Montale is known for rose and oud, and this one is made for women.</li>
</ul>
<h2>The Al Haramain Amber Oud editions</h2>
<p>Al Haramain's Amber Oud range is a popular Arabian line, but read the notes: not every edition is built around oud. [[white|Amber Oud White Edition]] ({{white}}) is bergamot and orange, then jasmine, rose and freesia over musk, vanilla and patchouli, and is listed for women. [[carbon|Amber Oud Carbon Edition]] ({{carbon}}) is a fresh, aromatic men's scent of lavender, rosemary, bergamot, sage and vetiver. [[bleu|Amber Oud Bleu Edition]] ({{bleu}}) is citrus and mint over incense, vetiver and sandalwood. For the Gold, Ruby, Tobacco and Black editions, and for Lattafa, read our guide to <a href="/blogs/journal/lattafa-khamrah-qahwa-arabian-perfume">Arabian perfume and Lattafa Khamrah Qahwa</a>.</p>
<h2>Which oud perfume suits you?</h2>
<ul>
<li><strong>New to oud:</strong> Tom Ford Oud Wood, or a fresher Amber Oud edition.</li>
<li><strong>You love incense and leather:</strong> Gucci Intense Oud or Guerlain Oud Essentiel.</li>
<li><strong>You love rose:</strong> Montale Aoud Damascus or Guerlain Oud Essentiel.</li>
<li><strong>Warm and spicy:</strong> Chopard Oud Malaki.</li>
</ul>
<p>Oud is traditionally unisex, so "for men" or "for women" on the label is only a starting point. Browse <a href="/collections/unisex-perfume">unisex perfume</a>, <a href="/collections/perfume-for-men">perfume for men</a> and <a href="/collections/perfume-for-women">perfume for women</a>.</p>
<h2>How to wear oud</h2>
<ol>
<li><strong>Start small:</strong> one or two sprays. Oud notes are rich, and a little goes a long way.</li>
<li><strong>Apply to moisturised skin</strong> on the wrists, neck or chest. Our guide to <a href="/blogs/journal/layer-oud-with-body-butter">layering oud with body butter</a> explains why.</li>
<li><strong>Let it settle:</strong> do not rub your wrists together. Oud perfumes often change a lot after the first half hour, so judge them later in the day.</li>
<li><strong>Test before you buy</strong> a full bottle if you can, or start with a smaller size.</li>
</ol>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum</strong> is the most common strength for oud perfumes; read <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> for what the label means.</li>
<li><strong>Patch test</strong> on your inner arm if you have sensitive skin, and keep perfume away from your eyes.</li>
<li><strong>Store bottles</strong> away from heat and sunlight, with the cap on.</li>
</ul>
<p>Shop every <a href="/collections/oud-perfume">oud perfume</a>, all <a href="/collections/arabian-perfume">Arabian perfume</a> and <a href="/collections/niche-perfume">niche perfume</a>, all 100% authentic and dispatched from the UK.</p>""",
    "faq": [
        ["What does oud smell like?",
         "Deep, woody and slightly smoky, often with a leathery or resinous edge. Many perfumes soften it with rose, spice, amber or vanilla, so oud perfumes can range from creamy to dark and incense-like."],
        ["What is the difference between Tom Ford Oud Wood and Gucci Intense Oud?",
         "Tom Ford Oud Wood is smoother and creamier: oud wood, rosewood and cardamom over sandalwood, vetiver, tonka bean and amber. Gucci Intense Oud is darker, with black pepper, frankincense, leather and patchouli."],
        ["Is oud perfume for men or women?",
         "Both. Oud is traditionally worn by everyone. Tom Ford Oud Wood, Gucci Intense Oud and Guerlain Oud Essentiel are unisex; Chopard Oud Malaki is made for men and Montale Aoud Damascus for women."],
        ["Is the oud in perfume real?",
         "Natural oud is rare and expensive, so many perfumes use an oud accord: a blend of woods, resins and leathery notes that recreates the effect. Gucci Intense Oud, for example, lists an oud accord in its base."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_oud_perfume_2026-11-08.jsonl")

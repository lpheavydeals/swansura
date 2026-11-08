"""Journal guide 'Tom Ford perfume: Black Orchid, Noir Extreme, Neroli Portofino and more' (user, 8 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): tom ford perfume 33,100/mo (KD 55),
tom ford black orchid 22,200 (KD 22), tom ford noir extreme 8,100 (KD 15), tom ford neroli portofino 3,600 (KD 14),
tom ford noir extreme parfum 1,600, tom ford perfume for men 1,600, tom ford ebene fume 880, tom ford black orchid
parfum 720. Facts = the products' stored notes (8 Nov 2026). Oud Wood is covered by the oud perfume guide (linked).
The three non-Tom Ford picks are scents with a similar mood, never called a dupe or 'smells like'. Left out:
longevity / 'long-lasting', launch dates, perfumers. Prices are written into the text: re-run the generator and
update the body if prices change.

Usage: python3 tools/shopify/guide_tom_ford.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_tom_ford_2026-11-08.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Tom Ford perfume: Black Orchid, Noir Extreme, Neroli Portofino and more",
    "handle": "tom-ford-perfume-guide",
    "tag": "Scent Studio",
    "summary": "Tom Ford's best-known perfumes side by side: Black Orchid, Noir Extreme, Neroli Portofino, Ébène Fumé and Oud Wood, with their notes and who each suits.",
    "mt": "Tom Ford Perfume: Black Orchid & Noir Extreme | Swansura",
    "md": "Tom Ford Black Orchid, Noir Extreme, Neroli Portofino, Ébène Fumé and Oud Wood compared: the notes, when to wear each, and which one suits you.",
    "pick": {
        "orchid": "tom-ford-black-orchid-parfum-100ml-unisex",
        "noir": "tom-ford-noir-extreme-parfum-100ml-for-men",
        "neroli": "tom-ford-neroli-portofino-eau-de-parfum-50ml-unisex",
        "ebene": "tom-ford-ebene-fume-eau-de-parfum-50ml-unisex",
        "oud": "tom-ford-oud-wood-eau-de-parfum-50ml-unisex",
        "colonia": "acqua-di-parma-colonia-pura-eau-de-cologne-20ml-unisex",
        "joop": "joop-homme-le-parfum-75ml-men-s-warm-spicy-amber-fragrance",
        "bvlgari": "bvlgari-man-in-black-eau-de-parfum-100ml-luxury-men-s-fragrance",
    },
    "titles": {},
    "shop": ["orchid", "noir", "neroli", "ebene", "oud", "colonia", "joop", "bvlgari"],
    "body": """<p><strong>Tom Ford perfume</strong> covers a wide range, from dark, velvety evening scents to bright citrus colognes. Here are the Tom Ford fragrances we stock, what is in each one, when to wear it, and a few other scents in a similar mood if you want to compare.</p>
<h2>Signature and Private Blend</h2>
<p>Tom Ford's perfumes fall into two main lines. The <strong>Signature</strong> collection includes Black Orchid and Noir Extreme. The <strong>Private Blend</strong> collection includes Oud Wood, Neroli Portofino and Ébène Fumé, and is usually sold in smaller bottles at a higher price. Both are made for anyone to wear: "for men" on a label is only a guide.</p>
<h2>Tom Ford Black Orchid</h2>
<p>[[orchid|Tom Ford Black Orchid Parfum]] ({{orchid}}, 100ml) is dark and rich. It opens on truffle and plum, moves into rum, ylang-ylang and black orchid, and settles on patchouli. It is an amber floral, made unisex, and best for evenings, special occasions and the colder months. The parfum is a stronger concentration than eau de parfum, so one or two sprays are plenty.</p>
<h2>Tom Ford Noir Extreme</h2>
<p>[[noir|Tom Ford Noir Extreme Parfum]] ({{noir}}, 100ml) is warm and spicy-sweet. Cardamom, nutmeg, saffron, mandarin and neroli open it; rose, jasmine, orange blossom and kulfi, a milky, dessert-like accord, form the heart; vanilla, amber, sandalwood and woods make the base. It is made for men and suits evenings and cooler weather.</p>
<h2>Tom Ford Neroli Portofino</h2>
<p>[[neroli|Tom Ford Neroli Portofino Eau de Parfum]] ({{neroli}}, 50ml) is the bright one. Italian bergamot, mandarin and Sicilian lemon lead into Tunisian neroli, orange flower and lavender, over a light base of amber and rosemary. It is unisex and easy to wear in the daytime, at work and on holiday.</p>
<h2>Ébène Fumé and Oud Wood</h2>
<p>[[ebene|Tom Ford Ébène Fumé]] ({{ebene}}, 50ml) is smoky and woody: palo santo and black pepper, then rose and leather, over ebony wood and resin. [[oud|Tom Ford Oud Wood]] ({{oud}}, 30ml or 50ml) is smoother: oud wood, rosewood and cardamom over sandalwood, vetiver, tonka bean and amber. For more on oud, read our <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a>.</p>
<h2>Which Tom Ford perfume suits you?</h2>
<ul>
<li><strong>Fresh and easy for daytime:</strong> Neroli Portofino.</li>
<li><strong>Warm, spicy and sweet:</strong> Noir Extreme.</li>
<li><strong>Dark, rich and dramatic:</strong> Black Orchid.</li>
<li><strong>Smoky and woody:</strong> Ébène Fumé, or the softer Oud Wood.</li>
</ul>
<p>The season helps too. Neroli Portofino suits spring and summer, while Black Orchid, Noir Extreme, Ébène Fumé and Oud Wood come into their own in autumn and winter. Many people keep one fresh and one warm scent and switch as the weather changes.</p>
<h2>Other scents in a similar mood</h2>
<p>These are different perfumes, not copies, but they share some of the same notes:</p>
<ul>
<li>If you like Neroli Portofino's citrus: [[colonia|Acqua di Parma Colonia Pura]] ({{colonia}}, 20ml), with bergamot, orange and petitgrain over jasmine, coriander, musk and cedarwood.</li>
<li>If you like Noir Extreme's spice and vanilla: [[joop|Joop! Homme Le Parfum]] ({{joop}}, 75ml), with lavender and cinnamon, orange blossom and tonka bean, then vanilla, amber and woods.</li>
<li>If you like Black Orchid's rum and depth: [[bvlgari|Bvlgari Man in Black]] ({{bvlgari}}, 100ml), with rum, spices and tobacco, leather, tuberose and iris, over guaiac wood, benzoin and tonka bean.</li>
</ul>
<h2>How to wear it</h2>
<ol>
<li><strong>Start with one or two sprays</strong> on the neck or wrists; parfums and eau de parfums are concentrated.</li>
<li><strong>Spray on moisturised skin</strong> so the scent has something to sit on: see our guide to <a href="/blogs/journal/layer-oud-with-body-butter">layering perfume with body butter</a>.</li>
<li><strong>Let it settle</strong> before you judge it. The base notes come through after the first half hour.</li>
</ol>
<h2>Good to know</h2>
<ul>
<li><strong>Parfum vs eau de parfum:</strong> read <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> for what the labels mean.</li>
<li><strong>Sizes:</strong> Black Orchid and Noir Extreme come in 100ml bottles, Neroli Portofino and Ébène Fumé in 50ml, and Oud Wood in 30ml or 50ml.</li>
<li><strong>Gifting?</strong> Tom Ford makes a generous present; see our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a>.</li>
<li><strong>Store bottles</strong> away from heat and sunlight, with the cap on.</li>
</ul>
<p>Shop every <a href="/collections/tom-ford">Tom Ford</a> fragrance, all <a href="/collections/perfume-for-men">perfume for men</a>, <a href="/collections/unisex-perfume">unisex perfume</a> and <a href="/collections/niche-perfume">niche perfume</a>, all 100% authentic and dispatched from the UK.</p>""",
    "faq": [
        ["What does Tom Ford Black Orchid smell like?",
         "Dark and rich: truffle and plum at the top, rum, ylang-ylang and black orchid in the heart, and patchouli in the base. It is an amber floral, made unisex, and best for evenings."],
        ["Is Tom Ford Noir Extreme for men?",
         "It is made for men, but anyone can wear it. It is warm and spicy-sweet, with cardamom, nutmeg and saffron, a rose and kulfi heart, and vanilla, amber and sandalwood."],
        ["Which Tom Ford perfume is best for daytime?",
         "Neroli Portofino: bergamot, mandarin and lemon with neroli, orange flower and lavender, over amber and rosemary. It is fresh, unisex and easy to wear to work."],
        ["What is the difference between Tom Ford Signature and Private Blend?",
         "They are Tom Ford's two main perfume lines. Black Orchid and Noir Extreme are Signature scents; Oud Wood, Neroli Portofino and Ébène Fumé are Private Blend, usually sold in smaller bottles at a higher price."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_tom_ford_2026-11-08.jsonl")

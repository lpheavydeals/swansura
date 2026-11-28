"""Journal guide 'Oud perfume under £60: real oud notes, and where the name is only a name'
(user, 26 Nov 2026: 'Go ahead with barcodes and the two guides', from the ChatGPT + Google strategy).

Why this topic: November orders from ChatGPT were oud/amber perfumes landing on product pages
(Amber Oud Gold, Chopard Amber Malaki, Franck Olivier Parisian Oud). People ask AI assistants
'best affordable oud perfume UK'; this answers it with the in-stock oud scents under £60.
Facts = stored custom.sw notes (Admin read 26 Nov) or the 'Fragrance notes' list in each product's
description. Says plainly which 'oud' names list no oud note. NO PRICES in the text (only the band).

Usage: python3 tools/shopify/guide_oud_under_60.py <storefront products dump dir>
Output: docs/seo/guide_oud_under_60_2026-11-26.jsonl
"""
import glob
import json
import sys

from journal_lib import build

A = {
    "title": "Oud perfume under £60: real oud notes, and where the name is only a name",
    "handle": "oud-perfume-under-60",
    "tag": "Scent Studio",
    "summary": "The oud perfumes we stock for under £60, with the notes in each one: smoky and leathery, rose and saffron, soft and sweet. Plus which 'oud' names list no oud at all.",
    "mt": "Oud Perfume Under £60: Affordable Oud Scents | Swansura",
    "md": "Affordable oud perfume in the UK: Chopard, Swiss Arabian, SAP, Korloff, Fumeri, Elie Saab and Dunhill oud scents under £60, with their notes.",
    "pick": {
        "chopard": "chopard-oud-malaki-eau-de-parfum-80ml-luxury-men-s-oud-fragrance",
        "shaghaf": "swiss-arabian-shaghaf-oud-royale-eau-de-parfum-75ml",
        "sapsaffron": "sap-saffron-oud-extrait-de-parfum-100ml",
        "sapleopard": "sap-oud-leopard-fr-extrait-de-parfum-100ml",
        "korloff": "royal-oud-korloff-paris-eau-de-parfum-88ml",
        "fumeri": "fumeri-oud-saffron-for-men-eau-de-parfum-100ml",
        "elie": "elie-saab-la-collection-des-essences-no-4-oud-eau-de-parfum-100ml-luxury-unisex-oud-fragrance",
        "agar": "dunhill-signature-collection-agar-wood-eau-de-parfum-100ml-men-s-woody-spicy-fragrance",
        "javarose": "franck-olivier-sun-java-rose-oud-eau-de-parfum-75ml",
        "royaloud": "franck-olivier-sun-royal-oud-eau-de-parfum-75ml",
        "bentley": "bentley-for-men-absolute-eau-de-parfum-100ml-men-s-woody-spicy-fragrance",
        "gold": "al-haramain-amber-oud-gold-edition-eau-de-parfum-luxury-unisex-fruity-amber-fragrance",
        "tobacco": "al-haramain-amber-oud-tobacco-edition-eau-de-parfum-60ml-luxury-unisex-spicy-tobacco-fragrance",
    },
    "titles": {},
    "shop": ["chopard", "shaghaf", "sapsaffron", "korloff", "fumeri", "elie", "agar", "javarose"],
    "body": """<p><strong>Oud perfume does not have to cost three figures.</strong> Every scent below is under £60 at Swansura at the time of writing and lists oud (agarwood) in its notes. Most of them are eau de parfum or extrait, so they carry more fragrance than an eau de toilette. We also explain which popular 'oud' names do not list an oud note at all, so you know what you are buying.</p>
<h2>What oud smells like</h2>
<p>Oud, or agarwood, is a dark, resinous wood note. On its own it can smell smoky, leathery or slightly medicinal, so perfumers usually soften it with rose, saffron, amber or vanilla. Most oud in perfume today is an oud accord rather than pure oud oil. Our <a href="/blogs/journal/oud-perfume-guide">oud perfume guide</a> explains this in more detail and covers Tom Ford Oud Wood and Gucci Intense Oud.</p>
<h2>Smoky, leathery oud</h2>
<ul>
<li>[[chopard|Chopard Oud Malaki]] (80ml, for men): grapefruit, lavender and artemisia, then tobacco, spices and leather, over oud, ambergris and dark woods. The most polished of the darker ones here.</li>
<li>[[sapleopard|SAP Oud Leopard Extrait de Parfum]] (100ml, unisex): smoky spice at the top, then oud, leather and cedarwood, over amber, musk and vanilla.</li>
<li>[[fumeri|Fumeri Oud Saffron for Men]] (100ml): saffron and spices, then oud, cedarwood and smoky woods, over amber, leather and musk.</li>
<li>[[agar|Dunhill Signature Collection Agar Wood]] (100ml, for men): pink pepper, ginger and bergamot, then agarwood, saffron and black iris, over tobacco and suede.</li>
</ul>
<h2>Rose and saffron oud</h2>
<ul>
<li>[[shaghaf|Swiss Arabian Shaghaf Oud Royale]] (75ml, unisex): saffron and rose, then oud and praline, over vanilla, amber and musk. Sweeter and softer than the smoky group.</li>
<li>[[sapsaffron|SAP Saffron Oud Extrait de Parfum]] (100ml, unisex): saffron and warm spices, then oud, cedarwood and smoky woods, over amber, leather and musk.</li>
<li>[[korloff|Korloff Royal Oud]] (88ml, unisex): rose, incense and nutmeg, then oud, patchouli and labdanum, over sandalwood, amber, musk and vanilla.</li>
<li>[[javarose|Franck Olivier Sun Java Rose Oud]] (75ml, unisex): bergamot, orange and blackcurrant, then rose, jasmine and ylang-ylang, over oud, amber, sandalwood and vanilla. A floral rose with oud in the base.</li>
</ul>
<h2>Soft, woody oud</h2>
<ul>
<li>[[elie|Elie Saab La Collection des Essences No. 4 Oud]] (100ml, unisex): oud with woody accords and spices, over amber, resins and musk. Smooth rather than smoky, so a good first oud.</li>
<li>[[bentley|Bentley for Men Absolute]] (100ml): ginger and pink pepper, then papyrus, sandalwood and olibanum, with oud in the base beside cedarwood and amber. Oud is a background note here.</li>
</ul>
<h2>Names with 'oud' but no oud note</h2>
<p>Some well-known scents carry 'oud' in the name but do not list oud in their notes. That does not make them worse; it just means you should choose them for what they do list.</p>
<ul>
<li>The Al Haramain Amber Oud line: [[gold|Amber Oud Gold Edition]] is fruity and sweet (melon, pineapple, amber, vanilla) and [[tobacco|Amber Oud Tobacco Edition]] is spicy tobacco with vanilla and cacao. Our <a href="/blogs/journal/al-haramain-amber-oud-editions">Amber Oud editions guide</a> compares every one.</li>
<li>[[royaloud|Franck Olivier Sun Royal Oud]]: lemon, then patchouli, rose and white woods, over vanilla.</li>
</ul>
<h2>Which one should you choose?</h2>
<ul>
<li><strong>Dark and leathery:</strong> Chopard Oud Malaki or SAP Oud Leopard.</li>
<li><strong>Rose and saffron:</strong> Swiss Arabian Shaghaf Oud Royale or Korloff Royal Oud.</li>
<li><strong>Your first oud:</strong> Elie Saab No. 4 Oud or Franck Olivier Sun Java Rose Oud.</li>
<li><strong>Sweet rather than smoky:</strong> Shaghaf Oud Royale, or Amber Oud Gold if you want no oud at all.</li>
</ul>
<h2>How to wear oud</h2>
<p>Oud is a rich note. It suits cooler months and evenings best. For a warmer, softer trail, our guide to <a href="/blogs/journal/layer-oud-with-body-butter">layering oud with body butter</a> shows how. Browse every <a href="/collections/oud-perfume">oud perfume</a> and <a href="/collections/arabian-perfume">Arabian perfume</a> we stock, or see <a href="/collections/gifts-under-50">gifts under £50</a>. All are 100% authentic and ship from the UK, with free UK delivery over £40.</p>""",
    "faq": [
        ["What is the best oud perfume under £60?",
         "It depends on the style. For dark, leathery oud try Chopard Oud Malaki or SAP Oud Leopard; for rose and saffron, Swiss Arabian Shaghaf Oud Royale or Korloff Royal Oud; for a soft first oud, Elie Saab No. 4 Oud."],
        ["Does Al Haramain Amber Oud contain oud?",
         "The stored note lists for the Amber Oud editions we sell do not name oud. Amber Oud Gold is fruity and sweet, and Amber Oud Tobacco is spicy tobacco with vanilla. Choose them for those notes."],
        ["Is oud perfume unisex?",
         "Many oud perfumes are sold as unisex, including Shaghaf Oud Royale, SAP Saffron Oud, Korloff Royal Oud and Elie Saab No. 4 Oud. Chopard Oud Malaki, Fumeri Oud Saffron and Dunhill Agar Wood are sold for men."],
        ["Are these oud perfumes authentic?",
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
    build(A, ALL, "guide_oud_under_60_2026-11-26.jsonl")

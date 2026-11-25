"""Journal guide 'Bvlgari perfume: Man in Black, the Man Essence sets and Splendida compared'
(user, 25 Nov 2026: 'Write and Publish All'; Bvlgari replaced Dunhill after the Search Console + Trends check).

Semrush UK: bvlgari perfume 8,100, bvlgari man in black 1,900. Trends: ~60% of Guerlain, peaks early Dec.
4 Bvlgari in stock with photos (allp_map 25 Nov); Man Rain Essence + Man Wood Essence sets, Rose Goldea Blossom
Delight set and Omnia Amethyste sold out: text links only. 4 more cards = scents in a similar mood (Guerlain
Habit Rouge, Chopard Black Incense Malaki, Acqua di Parma Sandalo, Gucci Bloom set), named as different perfumes.
Facts = stored custom.sw notes + descriptions (Admin read 25 Nov). NO PRICES in the text.

Usage: python3 tools/shopify/guide_bvlgari.py <allp_map.json>
Output: docs/seo/guide_bvlgari_2026-11-25.jsonl
"""
import json
import sys

from journal_lib import build

B = "bvlgari-"
A = {
    "title": "Bvlgari perfume: Man in Black, the Man Essence sets and Splendida compared",
    "handle": "bvlgari-perfume-guide",
    "tag": "Scent Studio",
    "summary": "The Bvlgari fragrances we stock: Man in Black, the Man Glacial Essence and Man Terrae Essence gift sets, and Splendida Tubereuse Mystique, with the notes and who each suits.",
    "mt": "Bvlgari Perfume: Man in Black & Essence Sets | Swansura",
    "md": "Bvlgari perfume compared: Man in Black, the Man Glacial Essence and Terrae Essence gift sets, and Splendida Tubereuse Mystique for women.",
    "pick": {
        "black": B + "man-in-black-eau-de-parfum-100ml-luxury-men-s-fragrance",
        "glacial": B + "man-glacial-essence-eau-de-parfum-gift-set-100ml-15ml-men-s-fragrance-set",
        "terrae": B + "man-terrae-essence-eau-de-parfum-gift-set-100ml-15ml-new-pack-men-s-fragrance-set",
        "splendida": B + "splendida-tubereuse-mystique-eau-de-parfum-100ml-luxury-women-s-floral-fragrance",
        "rain": B + "man-rain-essence-eau-de-parfum-gift-set-100ml-15ml-luxury-men-s-fragrance-set",
        "wood": B + "man-wood-essence-eau-de-parfum-gift-set-100ml-15ml-soft-box-men-s-fragrance-set",
        "goldea": B + "rose-goldea-blossom-delight-eau-de-parfum-gift-set-75ml-15ml-new-pack-women-s-fragrance-set",
        "omnia": B + "omnia-amethyste-eau-de-toilette-25ml-women-s-floral-fragrance",
        "habit": "guerlain-habit-rouge-eau-de-parfum-100ml-luxury-men-s-amber-woody-fragrance",
        "incense": "chopard-black-incense-malaki-eau-de-parfum-80ml-luxury-unisex-incense-fragrance",
        "sandalo": "acqua-di-parma-sandalo-edp-20ml-unisex",
        "bloom": "gucci-bloom-eau-de-parfum-gift-set-100ml-10ml-body-lotion-100ml-women-s-fragrance-set",
    },
    "titles": {},
    "soldout": ["rain", "wood", "goldea", "omnia"],
    "shop": ["black", "glacial", "terrae", "splendida", "habit", "incense", "sandalo", "bloom"],
    "body": """<p><strong>Bvlgari perfume</strong> for men centres on Man in Black and the Man Essence family, which we stock as gift sets with a travel spray. For women, we have Splendida Tubereuse Mystique. Here is every Bvlgari fragrance in stock, what is in each one, and who it suits.</p>
<h2>Bvlgari Man in Black</h2>
<p>[[black|Bvlgari Man in Black Eau de Parfum]] (100ml) is warm and dark. Rum, spices and tobacco open it; leather sits at the heart, softened by tuberose and iris; and guaiac wood, benzoin and tonka bean give a smooth, rich finish. It suits evenings and the colder months.</p>
<h2>The Bvlgari Man Essence gift sets</h2>
<p>Each set holds a 100ml eau de parfum and a 15ml travel spray of the same scent.</p>
<ul>
<li>[[glacial|Man Glacial Essence]]: juniper berries, ginger and geranium, then sandalwood, orris root and artemisia, over clearwood, cedar and musk. Cool, fresh and woody.</li>
<li>[[terrae|Man Terrae Essence]]: citron and calamansi, then vetiver and orris, over a terrae accord and styrax. Earthier and warmer than Glacial.</li>
</ul>
<p>The [[rain|Man Rain Essence]] and [[wood|Man Wood Essence]] sets are sold out at the moment.</p>
<p><strong>Glacial or Terrae?</strong> Choose Glacial for a crisp, cool scent for every day; choose Terrae for an earthy, resinous one.</p>
<h2>Bvlgari for women: Splendida Tubereuse Mystique</h2>
<p>[[splendida|Splendida Tubereuse Mystique Eau de Parfum]] (100ml) puts creamy tuberose at the centre. Blackcurrant and davana add a fruity lift at the top, and vanilla absolute and myrrh give it a warm, resinous depth. Rich and heady, it is an evening floral. [[goldea|Rose Goldea Blossom Delight]] and [[omnia|Omnia Amethyste]] are sold out at the moment.</p>
<h2>Which Bvlgari perfume should you choose?</h2>
<ul>
<li><strong>Warm, boozy and leathery:</strong> Man in Black.</li>
<li><strong>Cool and fresh, with a travel spray:</strong> Man Glacial Essence.</li>
<li><strong>Earthy and woody, with a travel spray:</strong> Man Terrae Essence.</li>
<li><strong>A rich white floral for her:</strong> Splendida Tubereuse Mystique.</li>
</ul>
<h2>Other scents in a similar mood</h2>
<p>These are different perfumes, not copies:</p>
<ul>
<li>If you like Man in Black's leather and vanilla: [[habit|Guerlain Habit Rouge Eau de Parfum]] (100ml), with citrus, then rose, cinnamon and patchouli, over leather, vanilla, amber and benzoin. More in our <a href="/blogs/journal/guerlain-perfume-guide">Guerlain perfume guide</a>.</li>
<li>If you like its darker side: [[incense|Chopard Black Incense Malaki]] (80ml), with incense and spices, oud and leather, over amber, woods and resins.</li>
<li>If you like the Essence sets' woods: [[sandalo|Acqua di Parma Sandalo]] (20ml), with bergamot and citrus, cardamom and lavender, over sandalwood, amber and tonka bean.</li>
<li>If you like Splendida's tuberose: the [[bloom|Gucci Bloom Eau de Parfum Gift Set]], built around jasmine, tuberose and Rangoon creeper.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Buying for him?</strong> See <a href="/collections/aftershave-gift-sets-for-him">aftershave gift sets for him</a> and our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a>.</li>
<li><strong>What the labels mean:</strong> read <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a>.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/bvlgari">Bvlgari</a> fragrance, or browse <a href="/collections/perfume-for-men">perfume for men</a>.</p>""",
    "faq": [
        ["What does Bvlgari Man in Black smell like?",
         "Man in Black Eau de Parfum opens with rum, spices and tobacco, has leather with tuberose and iris in the heart, and dries down to guaiac wood, benzoin and tonka bean."],
        ["What is in the Bvlgari Man Essence gift sets?",
         "Each set holds a 100ml eau de parfum and a 15ml travel spray of the same scent. We have Man Glacial Essence and Man Terrae Essence in stock."],
        ["What is the difference between Man Glacial Essence and Man Terrae Essence?",
         "Glacial Essence is cool and fresh, with juniper, ginger and geranium over clearwood, cedar and musk. Terrae Essence is earthier, with citron and calamansi, vetiver and orris, over a terrae accord and styrax."],
        ["Do you sell Bvlgari perfume for women?",
         "Yes: Splendida Tubereuse Mystique Eau de Parfum, a rich tuberose with blackcurrant, davana, vanilla and myrrh. Rose Goldea Blossom Delight and Omnia Amethyste are sold out at the moment."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_bvlgari_2026-11-25.jsonl")

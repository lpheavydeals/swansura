"""Journal guide 'Deyga Organics in the UK: the brand, the ingredients and where to start' (user, 16 Nov 2026).

Targets Search Console brand searches (4-10 Nov): deyga organics 415 impr (pos 6), deyga organics alternatives 147,
deyga 31, deyga products, is deyga a good brand, deyga skincare, deyga organic, deyga online shopping.
Facts = stored brand story (custom.brand on /collections/deyga), stored custom.inci, live prices.
No founder / location / history facts (not in our data). No skin or hair claims; Hair Growth Oil named once.
Usage: python3 tools/shopify/guide_deyga_organics_uk.py <allp_map.json>  ->  docs/seo/guide_deyga_organics_uk_2026-11-16.jsonl
"""
import json
import sys

from journal_lib import build

ALL = json.load(open(sys.argv[1]))
T = {"pot": "Deyga Beetroot Lip Balm Classic", "combo": "Deyga Soft Lip Combo", "oat": "Deyga Oat Milk Face Wash",
     "charcoal": "Deyga Charcoal Face Wash", "vitc": "Deyga Vitamin C Foaming", "rose": "Deyga Pure Rose Water",
     "ha": "Deyga 2% Hyaluronic", "spf": "Deyga Sunscreen", "choc": "Deyga Chocolate Body Butter", "saffron": "Deyga Shea Saffron Bath Bar",
     "foot": "Deyga Mini Foot Spa", "rice": "Deyga  Rice Water Shampoo", "soy": "Deyga's Soy Milk Conditioner",
     "hairkit": "Deyga Hair Care Kit", "glowkit": "Deyga Best Selling Face Care Kit"}
A = {
    "title": "Deyga Organics in the UK: the brand, the ingredients and where to start",
    "handle": "deyga-organics-uk",
    "tag": "Skin Studio",
    "summary": "Deyga, also known as Deyga Organics, explained for UK shoppers: what the brand makes, how to read its ingredient lists, the products to start with and how to buy it in the UK.",
    "mt": "Deyga Organics UK: The Brand and Where to Start | Swansura",
    "md": "Deyga Organics explained for UK shoppers: what the brand makes, how to read its ingredient lists, the best products to start with and where to buy.",
    "pick": {k: None for k in T}, "titles": T,
    "shop": ["pot", "oat", "charcoal", "ha", "spf", "choc", "rice", "foot"],
    "body": """<p><strong>Quick answer:</strong> <strong>Deyga</strong>, often searched as <strong>Deyga Organics</strong>, is an Indian natural care brand that makes skin, lip, body, foot and hair care with plant-based ingredients, many of which the brand says are grown on its own farm in India. It is best known for its beetroot lip balm, charcoal face wash and zinc oxide sunscreen. Swansura is an official UK partner of Deyga, so you can buy the range from UK stock, with free UK delivery over £40.</p>
<h2>Is Deyga the same as Deyga Organics?</h2>
<p>Yes. Deyga and Deyga Organics are the same brand and the same products; you will see both names on packs and online. On our site the range sits under <a href="/collections/deyga">Deyga</a>.</p>
<h2>What makes Deyga different?</h2>
<p>The clearest way to understand any brand is its ingredient lists, and Deyga's are unusually readable:</p>
<ul>
<li><strong>Short lists.</strong> The [[pot|Beetroot Lip Balm]] has seven ingredients and the [[rose|Pure Rose Water Toner]] two: rose and distilled water.</li>
<li><strong>Plant names in Sanskrit.</strong> Many lists add the traditional Indian name next to the Latin one, such as Satapatrika for rose, Kanya for aloe and Paldka for beetroot.</li>
<li><strong>Plant waters.</strong> Several products are built on hydrosols (plant waters): tea tree in the [[charcoal|Charcoal Face Wash]], citrus in the [[vitc|Vitamin C Foaming Face Wash]], rice water in the [[rice|Rice Water Shampoo]].</li>
<li><strong>Mild coconut- and corn-derived cleansers</strong> such as decyl glucoside and sodium cocoyl glycinate in the washes and shampoos.</li>
</ul>
<p>Two things worth knowing: some Deyga washes and shampoos list an added fragrance (marked IFRA approved), and several products use nut oils such as almond. The full ingredient list is on every Deyga product page on our site, so you can check before you buy.</p>
<h2>Where to start with Deyga</h2>
<h3>Lips</h3>
<p>The [[pot|Beetroot Lip Balm Classic]] ({{pot}}) is the product most people know Deyga for: a tinted balm with no added fragrance. Our guide <a href="/blogs/journal/deyga-beetroot-lip-balm-stick-or-pot">Deyga Beetroot Lip Balm: stick or pot</a> compares the two versions and the price per gram. The [[combo|Soft Lip Combo]] ({{combo}}) adds a mint sugar scrub.</p>
<h3>Face</h3>
<ul>
<li>[[oat|Oat Milk Face Wash]] ({{oat}}): oat milk and kaolin with coconut-derived cleansers.</li>
<li>[[charcoal|Charcoal Face Wash]] ({{charcoal}}): coconut-shell charcoal in tea tree hydrosol.</li>
<li>[[vitc|Vitamin C Foaming Face Wash]] ({{vitc}}): ascorbyl glucoside, a stable form of vitamin C, in citrus waters.</li>
<li>[[rose|Pure Rose Water Toner]] ({{rose}}): rose and distilled water only.</li>
<li>[[ha|2% Hyaluronic Acid Serum]] ({{ha}}): sodium hyaluronate with aloe, centella and panthenol.</li>
<li>[[spf|Deyga Sunscreen]] ({{spf}}): a zinc oxide sunscreen in SPF 30 or SPF 50, with raspberry, carrot seed and sunflower oils.</li>
</ul>
<p>Prefer a set? The [[glowkit|Best Selling Face Care Kit]] ({{glowkit}}) puts a routine in one box. Our <a href="/blogs/journal/face-wash-for-your-skin-type">face wash guide</a> and <a href="/blogs/journal/face-serum-guide">face serum guide</a> help you choose by skin type.</p>
<h3>Body and feet</h3>
<p>[[choc|Chocolate Body Butter]] ({{choc}}) is cocoa powder, shea butter, almond and jojoba oils and cocoa butter, with no water in the list. Deyga's handmade bath bars, such as [[saffron|Shea Saffron]] ({{saffron}}), are true soaps made with coconut and olive oils, and the [[foot|Mini Foot Spa Combo]] ({{foot}}) boxes a foot soak, scrub and butter. See our <a href="/blogs/journal/how-to-use-body-butter">body butter guide</a>, <a href="/blogs/journal/natural-body-wash-guide">body wash and bath bar guide</a> and <a href="/blogs/journal/foot-cream-guide">foot cream guide</a>.</p>
<h3>Hair</h3>
<p>[[rice|Rice Water Shampoo]] ({{rice}}) pairs with [[soy|Soy Milk Conditioner]] ({{soy}}), made with soybean extract, argan oil and panthenol. The [[hairkit|Deyga Hair Care Kit]] ({{hairkit}}) adds Deyga's Hair Growth Oil, a coconut, almond and castor oil blend with amla, bhringraj and hibiscus. Our <a href="/blogs/journal/hair-oil-guide">hair oil guide</a> and <a href="/blogs/journal/natural-shampoo-guide">natural shampoo guide</a> explain how to use them.</p>
<h2>Is Deyga a good brand?</h2>
<p>That depends on what you want, and we sell it, so here are the facts rather than a verdict. Deyga publishes full ingredient lists, keeps most of them short and leans on plant oils, butters and hydrosols. It does not suit everyone: some products contain added fragrance or essential oils, several contain nut oils, the lip balms contain beeswax, and the bath bars are true soap. Patch test anything new, and if you have a skin condition, ask a pharmacist or GP first. We do not publish invented reviews; real customer reviews appear on each product page.</p>
<h2>Buying Deyga in the UK</h2>
<ul>
<li><strong>Genuine stock:</strong> Swansura is an official UK partner of Deyga.</li>
<li><strong>Ships from the UK:</strong> no waiting for an overseas parcel and no import charge on delivery.</li>
<li><strong>Delivery:</strong> free UK delivery over £40, and £5 off orders over £70 with code SAVE5.</li>
<li><strong>Returns:</strong> unopened items within 14 days of delivery.</li>
</ul>
<h2>Looking for Deyga alternatives?</h2>
<p>Vilvah is the other Indian natural brand we stock as an official UK partner, known for goat milk and botanical care. Read <a href="/blogs/journal/vilvah-uk">Vilvah in the UK</a>, compare the two in <a href="/blogs/journal/deyga-or-vilvah">Deyga or Vilvah</a>, or see our <a href="/blogs/journal/indian-skincare-uk-guide">Indian skincare in the UK</a> guide. Shop all <a href="/collections/deyga">Deyga</a> or the wider <a href="/collections/natural-skincare">natural skincare</a> range.</p>""",
    "faq": [
        ["Is Deyga the same as Deyga Organics?",
         "Yes. Deyga and Deyga Organics are the same brand and the same products. On swansura.com the range is under Deyga."],
        ["Where can I buy Deyga in the UK?",
         "Swansura is an official UK partner of Deyga. Orders ship from UK stock with no import charge on delivery, and UK delivery is free on orders over £40."],
        ["Is Deyga a good brand?",
         "Deyga publishes full ingredient lists, keeps most of them short and uses plant oils, butters and hydrosols. Some products contain added fragrance, essential oils, nut oils or beeswax, so check the list and patch test anything new."],
        ["What is Deyga best known for?",
         "Its Beetroot Lip Balm, Charcoal Face Wash and zinc oxide sunscreen are the products most people start with, along with its body butters and handmade bath bars."],
    ],
}
build(A, ALL, "guide_deyga_organics_uk_2026-11-16.jsonl")

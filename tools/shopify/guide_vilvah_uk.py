"""Journal guide 'Vilvah in the UK: the brand, goat milk care and where to start' (user, 16 Nov 2026).

Targets brand searches: vilvah 480/mo (Semrush; GSC 91 impr pos 8), vilvah uk (pos 4, 1 click), vilvah products,
vilvah skincare, vilvah brand, vilvah store. Facts = stored brand story (custom.brand on /collections/vilvah),
stored custom.inci, live prices. Goat milk vs plant milks checked in each INCI (Milk Drops / toner = rice milk,
Milk Mud Mask / Milk Body Lotion = oat milk). No 'sulphate-free' (shampoos list disodium laureth sulfosuccinate),
no skin / hair claims, Hair Growth Oil not featured.
Usage: python3 tools/shopify/guide_vilvah_uk.py <allp_map.json>  ->  docs/seo/guide_vilvah_uk_2026-11-16.jsonl
"""
import json
import sys

from journal_lib import build

ALL = json.load(open(sys.argv[1]))
T = {"shampoo": "Vilvah Goat Milk Shampoo 250ML", "cond": "Vilvah Cream Conditioner 250ML", "hairkit": "Vilvah Bestseller Hair Kit",
     "mask": "Vilvah Goat Milk Hair Mask", "frizz": "Vilvah Anti-Frizz", "wash": "Vilvah Goat Milk Body Wash", "soap": "Classic Goatmilk Soap",
     "lotion": "Vilvah Milk Body Lotion", "deo": "Vilvah Deo Shot Kit", "ffwash": "Vilvah Fragrance-Free Cream Face Wash",
     "honey": "Vilvah Honey Face Wash", "drops": "Vilvah Milk Drops Hydrating Serum", "cream": "Vilvah Ultra Moisturising Cream",
     "spf": "Vilvah Skin Finish Sunscreen", "lipspf": "Vilvah Milk Lip Balm SPF", "mudmask": "Vilvah Milk Mud Mask"}
A = {
    "title": "Vilvah in the UK: the brand, goat milk care and where to start",
    "handle": "vilvah-uk",
    "tag": "Skin Studio",
    "summary": "Vilvah explained for UK shoppers: what the brand makes, which products use goat milk and which use plant milks, where to start for face, hair and body, and how to buy Vilvah in the UK.",
    "mt": "Vilvah UK: The Brand, Goat Milk Care and Where to Start",
    "md": "Vilvah explained for UK shoppers: the goat milk and botanical range, which milk is in which product, where to start and how to buy Vilvah in the UK.",
    "pick": {k: None for k in T}, "titles": T,
    "shop": ["drops", "shampoo", "cond", "ffwash", "cream", "spf", "wash", "lotion"],
    "body": """<p><strong>Quick answer:</strong> <strong>Vilvah</strong> is an Indian natural beauty brand known for goat milk and botanical formulas for face, hair and body. The products most people start with are the [[drops|Milk Drops serum]] and the [[shampoo|Goat Milk Shampoo]]. Swansura is an official UK partner of Vilvah, so you can buy the range from UK stock, with free UK delivery over £40.</p>
<h2>What is Vilvah known for?</h2>
<p>Goat milk runs through the range, alongside plant extracts, hydrosols and short ingredient lists. Every Vilvah product page on our site shows the full ingredient list, so you can see exactly what you are buying.</p>
<h2>Goat milk or plant milk? It depends on the product</h2>
<p>Many Vilvah products have milk in the name, but not all of them contain goat milk. From each ingredient list:</p>
<ul>
<li><strong>Goat milk:</strong> [[shampoo|Goat Milk Shampoo]], [[mask|Goat Milk Hair Mask]], [[wash|Goat Milk Body Wash]] and the goat milk soap bars, such as [[soap|Classic Goatmilk Soap]].</li>
<li><strong>Rice milk extract:</strong> [[drops|Milk Drops]] serum and the Milk Face Toner.</li>
<li><strong>Oat milk:</strong> [[mudmask|Milk Mud Mask]] and [[lotion|Milk Body Lotion]].</li>
<li><strong>Soy milk extract:</strong> [[lipspf|Milk Lip Balm SPF 30 PA+++]].</li>
</ul>
<p>So if you avoid animal ingredients, the goat milk products are not for you, but several of the milk products are plant-based. Our <a href="/blogs/journal/goat-milk-soap-guide">goat milk soap guide</a> explains the soap bars in detail.</p>
<h2>Where to start with Vilvah</h2>
<h3>Face</h3>
<ul>
<li>[[ffwash|Fragrance-Free Cream Face Wash]] ({{ffwash}}): a creamy wash with banana fruit extract and no added fragrance.</li>
<li>[[honey|Honey Face Wash]] ({{honey}}): a gel wash with raw honey and papaya and blackberry extracts.</li>
<li>[[drops|Milk Drops serum]] ({{drops}}): a light gel serum with hyaluronic acid and rice milk extract. Our <a href="/blogs/journal/vilvah-milk-drops-serum">Vilvah Milk Drops guide</a> covers the ingredients and the 20ml vs 40ml sizes.</li>
<li>[[cream|Ultra Moisturising Cream]] ({{cream}}): olive squalane with bamboo and goji berry extracts.</li>
<li>[[spf|Skin Finish Sunscreen SPF 50 PA+++]] ({{spf}}): a daily face sunscreen with ceramides and niacinamide.</li>
</ul>
<h3>Hair</h3>
<p>The [[shampoo|Goat Milk Shampoo 250ML]] ({{shampoo}}) and [[cond|Cream Conditioner 250ML]] ({{cond}}) are the classic pair, sold together as the [[hairkit|Bestseller Hair Kit]] ({{hairkit}}). For dry, frizzy lengths, add the [[mask|Goat Milk Hair Mask]] ({{mask}}) or the [[frizz|Anti-Frizz Hair Serum]] ({{frizz}}), an oil serum with black seed, curry leaf and hibiscus oils and no silicones in its list. See our <a href="/blogs/journal/natural-shampoo-guide">natural shampoo guide</a> and <a href="/blogs/journal/frizzy-hair-serum-oil-mask">frizzy hair guide</a>.</p>
<h3>Body</h3>
<p>[[wash|Goat Milk Body Wash]] ({{wash}}) uses goat milk and coconut oil in a chamomile water base; follow it with [[lotion|Milk Body Lotion]] ({{lotion}}), made with oat milk and ceramide. The [[deo|Deo Shot Kit]] ({{deo}}) holds two solid balm deodorants made without aluminium. Our <a href="/blogs/journal/natural-body-wash-guide">body wash and bath bar guide</a> and <a href="/blogs/journal/foot-cream-guide">foot cream guide</a> cover more of the range.</p>
<h3>Lips</h3>
<p>[[lipspf|Milk Lip Balm SPF 30 PA+++]] ({{lipspf}}) uses mineral filters for daytime; Vilvah also makes tinted lip balms. Compare them in our <a href="/blogs/journal/lip-balm-guide">lip balm guide</a>.</p>
<h2>Is Vilvah a good brand?</h2>
<p>We sell it, so here are the facts rather than a verdict. Vilvah publishes full ingredient lists, uses goat milk and plant extracts throughout, and keeps several lists very short; its rose water toner is only steam-distilled rose water. It does not suit everyone: the goat milk products are not vegan, some products contain essential oils or added fragrance, and the shampoos use a mild sulfosuccinate cleanser, so we do not call them sulphate-free. Patch test anything new, and if you have a skin condition, ask a pharmacist or GP first. Real customer reviews appear on each product page; we do not publish invented ones.</p>
<h2>Buying Vilvah in the UK</h2>
<ul>
<li><strong>Genuine stock:</strong> Swansura is an official UK partner of Vilvah.</li>
<li><strong>Ships from the UK:</strong> no overseas wait and no import charge on delivery.</li>
<li><strong>Delivery:</strong> free UK delivery over £40, and £5 off orders over £70 with code SAVE5.</li>
<li><strong>Returns:</strong> unopened items within 14 days of delivery.</li>
</ul>
<h2>Vilvah or Deyga?</h2>
<p>Deyga is the other Indian natural brand we stock as an official UK partner. Read <a href="/blogs/journal/deyga-organics-uk">Deyga Organics in the UK</a>, compare the two in <a href="/blogs/journal/deyga-or-vilvah">Deyga or Vilvah</a>, or start with our <a href="/blogs/journal/indian-skincare-uk-guide">Indian skincare in the UK</a> guide. Shop all <a href="/collections/vilvah">Vilvah</a> or the wider <a href="/collections/natural-skincare">natural skincare</a> range.</p>""",
    "faq": [
        ["Can I buy Vilvah in the UK?",
         "Yes. Swansura is an official UK partner of Vilvah. Orders ship from UK stock with no import charge on delivery, and UK delivery is free on orders over £40."],
        ["Is Vilvah vegan?",
         "Not all of it. The goat milk products, such as the Goat Milk Shampoo, Body Wash and soap bars, contain goat milk. Some milk-named products use plant milks instead, such as rice milk in Milk Drops and oat milk in the Milk Body Lotion. Check each ingredient list."],
        ["What is Vilvah best known for?",
         "Goat milk and botanical care. Milk Drops serum and the Goat Milk Shampoo are where most people start."],
        ["Which Vilvah products should I start with?",
         "For face, a cleanser such as the Fragrance-Free Cream Face Wash with Milk Drops serum and Skin Finish Sunscreen SPF 50. For hair, the Goat Milk Shampoo and Cream Conditioner, sold together as the Bestseller Hair Kit."],
    ],
}
build(A, ALL, "guide_vilvah_uk_2026-11-16.jsonl")

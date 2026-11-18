"""Journal guide 'Winter skincare for dry skin: a simple Vilvah and Deyga routine'
(user, 17-18 Nov 2026: 'Write and Publish All').

Keywords (workbook, Semrush UK): moisturiser for dry skin 2,900, body lotion for dry skin 1,300, face wash for dry skin
1,600, lip balm for dry lips 1,000, foot cream 5,400 (guides already exist for these: linked, not repeated).
Vilvah + Deyga first (best margin). Facts = stored custom.inci (Admin read 18 Nov) and descriptions. No claims:
no eczema / dermatitis / heals / repairs barrier / cracked heels; persistent dryness, itching or cracks -> pharmacist/GP.
Prices are written into the text: re-run and update if prices change.

Usage: python3 tools/shopify/guide_winter_skincare.py <allp_map.json>
Output: docs/seo/guide_winter_skincare_2026-11-18.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Winter skincare for dry skin: a simple Vilvah and Deyga routine",
    "handle": "winter-skincare-dry-skin",
    "tag": "Skin Studio",
    "summary": "Cold air outside and heating inside leave skin feeling tight. A simple winter routine for face, body, lips and feet, with Vilvah and Deyga products and what is in them.",
    "mt": "Winter Skincare for Dry Skin: A Simple Routine | Swansura",
    "md": "A simple winter skincare routine for dry skin: a gentle cleanser, a richer moisturiser, body lotion, lip balm and foot cream from Vilvah and Deyga.",
    "pick": {
        "ffwash": "vilvah-fragrance-free-cream-face-wash-100ml-gentle-hydrating-cleanser-for-sensitive-dry-skin-sulfate-free-paraben-free-silicone-free-enriched-with-banana-coconut-milk-extracts",
        "oatwash": "deyga-oat-milk-face-wash-100-ml",
        "ha": "deyga-2-hyaluronic-acid-serum-20ml",
        "deep": "deyga-deep-moisturising-face-cream-30g",
        "ultra": "vilvah-ultra-moisturising-cream-anti-aging-hydration-for-fine-lines-wrinkles-50ml",
        "spf": "vilvah-skin-finish-sunscreen-spf-50-pa",
        "lotion": "vilvah-milk-body-lotion-250ml-vegan-paraben-free-with-oat-milk-ceramides-olive-squalane-deep-moisturizing-for-dry-sensitive-skin-non-greasy-fast-absorbing-formula",
        "choc": "deyga-chocolate-body-butter-100g",
        "beet": "deygas-beetroot-lip-balm-classic-10-g-100-natural-no-harsh-chemicals",
        "lipspf": "vilvah-milk-lip-balm-spf-30-pa-natural-uv-protection-hydrating-lip-care-for-all-skin-types",
        "footcream": "vilvah-foot-care-cream-100ml-moisturising-treatment-for-cracked-heels-dry-calloused-feet-enriched-with-peppermint-argan-kalonji-oils-shea-mango-avocado-butters-unisex-all-skin-types",
        "footbutter": "foot-butter-40-g-deygas-deep-moisture-butter-for-dry-cracked-heels-rough-feet",
        "hairmask": "vilvah-goat-milk-hair-mask-200g-deep-conditioning-treatment-for-frizz-flyaway-control-curl-definition-moisture-repair-mask",
    },
    "titles": {},
    "shop": ["ffwash", "deep", "ultra", "ha", "lotion", "choc", "beet", "footcream"],
    "body": """<p>Cold air outside and central heating inside both dry the air, and skin often feels it first: a tight face after washing, rough patches on legs and elbows, dry lips. The fix is usually not more products but slightly different ones. Here is a simple <strong>winter skincare routine for dry skin</strong>, using Vilvah and Deyga, with what is in each product.</p>
<h2>1. Cleanse gently</h2>
<p>In winter, a cream or low-foam cleanser leaves skin feeling more comfortable than a strong foaming wash. [[ffwash|Vilvah Fragrance-Free Cream Face Wash]] ({{ffwash}}, 100ml) uses mild cleansers (disodium cocoyl glutamate, coco-glucoside) with glycerine, banana fruit extract and hydrolysed wheat protein, and has no added fragrance. [[oatwash|Deyga Oat Milk Face Wash]] ({{oatwash}}, 100ml) is built on oat milk with betaine, provitamin B5 and kaolin; it does contain fragrance. Wash with lukewarm rather than hot water, and pat dry. Our guide to <a href="/blogs/journal/face-wash-for-your-skin-type">face wash for your skin type</a> has more options.</p>
<h2>2. Add a hydrating serum</h2>
<p>A watery serum on slightly damp skin, before your cream, adds a light layer of moisture. [[ha|Deyga 2% Hyaluronic Acid Serum]] ({{ha}}, 20ml) pairs sodium hyaluronate with glycerine, panthenol, aloe vera and centella asiatica, without fragrance. Our <a href="/blogs/journal/face-serum-guide">face serum guide</a> explains how to layer one.</p>
<h2>3. Switch to a richer moisturiser</h2>
<p>If your summer moisturiser feels too light, winter is the time for a richer cream.</p>
<ul>
<li>[[deep|Deyga Deep Moisturising Face Cream]] ({{deep}}, 30g): centella asiatica, cardamom, marula oil, almond oil and shea butter, with glycerine. A short, butter-rich list.</li>
<li>[[ultra|Vilvah Ultra Moisturising Cream]] ({{ultra}}, 50ml): glycerine and olive squalane, with bamboo, goji berry and sophora extracts and a hint of white lily essential oil.</li>
</ul>
<p>Apply morning and night. Our guide to <a href="/blogs/journal/moisturiser-for-your-skin-type">moisturiser for your skin type</a> compares more creams.</p>
<h2>4. Keep wearing SPF</h2>
<p>Winter sun is lower, but UV still reaches the skin, especially on bright days, in snow and at altitude. [[spf|Vilvah Skin Finish Sunscreen SPF 50 PA+++]] ({{spf}}) is a light sunscreen whose list also includes glycerine, sodium hyaluronate and ceramides. Apply it as the last step in the morning.</p>
<h2>5. Body: lotion by day, butter by night</h2>
<ul>
<li>[[lotion|Vilvah Milk Body Lotion]] ({{lotion}}, 250ml): oat milk, ceramide NP, olive squalane, coconut oil and jojoba oil. Light enough to wear under clothes every morning.</li>
<li>[[choc|Deyga Chocolate Body Butter]] ({{choc}}, 100g): cocoa powder, shea butter, almond oil, jojoba oil, cocoa butter and vitamin E, with no water in the list. Richer, for elbows, knees and shins at night.</li>
</ul>
<p>Apply either straight after a shower, while skin is still slightly damp. Our <a href="/blogs/journal/how-to-use-body-butter">body butter guide</a> and <a href="/blogs/journal/natural-body-wash-guide">body wash guide</a> cover the rest of the shower routine.</p>
<h2>6. Lips</h2>
<p>Lips have no oil glands of their own, so they dry out first. [[beet|Deyga Beetroot Lip Balm]] ({{beet}}, 10g) is made with beetroot extract, almond, avocado and jojoba oils, shea butter and beeswax, with a sheer tint. On bright or snowy days, [[lipspf|Vilvah Milk Lip Balm SPF 30 PA+++]] ({{lipspf}}) uses zinc oxide and titanium dioxide. Our <a href="/blogs/journal/lip-balm-guide">lip balm guide</a> compares them all.</p>
<h2>7. Feet</h2>
<p>Boots and heating are hard on heels. [[footcream|Vilvah Foot Care Cream]] ({{footcream}}, 100ml) is rich in shea, avocado, mango and cocoa butters with sunflower, argan and kalonji oils and peppermint oil. [[footbutter|Deyga Foot Butter]] ({{footbutter}}, 40g) is a waterless balm of coconut oil, olive oil, beeswax and vitamin E; apply it at night under cotton socks. See our <a href="/blogs/journal/foot-cream-guide">foot cream guide</a> for an at-home pedicure.</p>
<h2>Hair</h2>
<p>Dry indoor air can leave lengths feeling rough too. Once a week, [[hairmask|Vilvah Goat Milk Hair Mask]] ({{hairmask}}) pairs goat milk with ceramides and argan oil. Our <a href="/blogs/journal/frizzy-hair-serum-oil-mask">frizzy hair guide</a> has more.</p>
<h2>Small habits that help</h2>
<ul>
<li><strong>Shorter, warm showers</strong> rather than long hot ones.</li>
<li><strong>Moisturise within a few minutes</strong> of washing, while skin is damp.</li>
<li><strong>Patch test</strong> any new product, one at a time.</li>
<li><strong>See a pharmacist or your GP</strong> if dryness comes with redness, itching or cracks that do not settle.</li>
</ul>
<p>Shop every product for <a href="/collections/dry-skin">dry skin</a>, or browse all <a href="/collections/vilvah">Vilvah</a> and <a href="/collections/deyga">Deyga</a>. Swansura is an official UK partner of both brands, and every order ships from the UK, with free UK delivery over £40.</p>""",
    "faq": [
        ["How should I change my skincare routine in winter?",
         "Keep it simple: switch to a gentle cream or low-foam cleanser, add a hydrating serum on damp skin, use a richer moisturiser, keep wearing SPF in the morning, and add body lotion or butter, lip balm and foot cream."],
        ["What is the best moisturiser for dry skin in winter?",
         "A richer cream than you use in summer. Deyga Deep Moisturising Face Cream is made with marula oil, almond oil and shea butter, and Vilvah Ultra Moisturising Cream with glycerine and olive squalane. Apply morning and night on clean skin."],
        ["Do I need sunscreen in winter?",
         "Yes, on bright days and especially in snow or at altitude, because UV still reaches the skin. Apply an SPF such as Vilvah Skin Finish Sunscreen SPF 50 PA+++ as the last step in your morning routine, and an SPF lip balm on your lips."],
        ["Body lotion or body butter for dry skin in winter?",
         "Many people use both: a lighter lotion such as Vilvah Milk Body Lotion in the morning, and a richer butter such as Deyga Chocolate Body Butter at night on elbows, knees and shins. Apply either on slightly damp skin after a shower."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_winter_skincare_2026-11-18.jsonl")

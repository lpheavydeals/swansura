"""Journal guide 'Hair oils explained: amla, bhringraj, castor and how to oil your hair' (user, 27 Oct 2026).

Target keywords (Semrush UK): hair growth oil 5,400/mo (KD 21), castor oil for hair 3,600, amla hair oil 2,900 (KD 9),
hair oil for dry hair 1,900, bhringraj oil 720, ayurvedic hair oil 390, natural hair oil 390, hibiscus hair oil 140.
Facts come from our INCI data (docs/data/deyga_inci_2026-10-23.json, docs/data/vilvah_inci_2026-10-22.json) and the
product descriptions. NO growth / hair-fall / greying / dandruff-treatment claims (ASA): 'hair growth oil' and
'Premature Greying' appear only as product names and as the search term, with an honest note that oils condition
hair and scalp and that hair loss or a persistent flaky scalp needs a GP or pharmacist.

Usage: python3 tools/shopify/guide_hair_oil.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_hair_oil_2026-10-27.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Hair oils explained: amla, bhringraj, castor and how to oil your hair",
    "handle": "hair-oil-guide",
    "tag": "Skin Studio",
    "summary": "What amla, bhringraj, castor, neem and rosemary bring to a hair oil, and how to oil your hair step by step.",
    "mt": "Hair Oil Guide: Amla, Bhringraj & Castor Oil | Swansura",
    "md": "How to oil your hair, and what amla, bhringraj, castor, neem and rosemary oils bring to it: a simple guide to Indian hair oiling, with tips for dry hair.",
    "pick": {
        "deyga-oil": None, "vilvah-oil": None,
        "greying": "deyga-premature-greying-hair-oil-100ml", "dandruff-oil": None,
        "neem": "deyga-neem-seed-oil-30ml", "rice": None, "goat": "vilvah-goat-milk-shampoo-250ml",
        "dandruff-shampoo": None, "comb": None, "serum": None,
    },
    "titles": {
        "deyga-oil": "Deyga's Hair Growth Oil", "vilvah-oil": "Vilvah Hair Growth Oil",
        "dandruff-oil": "Vilvah Anti-Dandruff Hair Oil", "rice": "Deyga  Rice Water Shampoo",
        "dandruff-shampoo": "Vilvah Herbal Shampoo for Dandruff Control", "comb": "Neem Wood Comb Set of 3",
        "serum": "Vilvah Anti-Frizz Hair Serum",
    },
    "shop": ["deyga-oil", "vilvah-oil", "greying", "dandruff-oil", "neem", "rice", "goat", "comb"],
    "body": """<p>In India, oiling your hair is a weekly ritual passed down through families: warm oil massaged into the scalp, left to soak in, then washed out. It is one of the simplest ways to make dry hair feel softer and look glossier, and it is easy to start. Here is what the classic ingredients (amla, bhringraj, castor oil and more) bring to a hair oil, how to choose one, and how to oil your hair step by step.</p>
<h2>What does a hair oil do?</h2>
<p>A hair oil coats the hair shaft, so lengths feel softer, smoother and less frizzy, and look shinier. Used before washing, it cushions the lengths so they feel less dry after shampoo. And the scalp massage that goes with it is relaxing in itself. Think of a hair oil as a conditioning treatment for hair and scalp.</p>
<h2>The key ingredients, explained</h2>
<ul>
<li><strong>Amla</strong> (Indian gooseberry, <em>Emblica officinalis</em>) is the best-known ingredient in Ayurvedic hair care. In an <strong>amla hair oil</strong>, the dried fruit is steeped in a base oil such as coconut.</li>
<li><strong>Bhringraj</strong> (<em>Eclipta prostrata</em>) is a herb traditionally used in Indian hair oils, often alongside amla. <strong>Bhringraj oil</strong> is usually a herbal infusion rather than a pure oil.</li>
<li><strong>Castor oil</strong> is thick and rich. On its own it can feel heavy, so it works best mixed with lighter oils, which is how you will find it in most blends.</li>
<li><strong>Coconut oil</strong> is the classic base for Indian hair oils, light enough for the scalp and rich enough for the lengths.</li>
<li><strong>Hibiscus</strong>, <strong>fenugreek</strong> and <strong>curry leaf</strong> are kitchen-garden ingredients that often join amla in traditional blends.</li>
<li><strong>Neem</strong>, <strong>tea tree</strong> and <strong>peppermint</strong> give an oil a fresh, cooling feel on the scalp.</li>
<li><strong>Rosemary</strong> essential oil adds a herbal scent and is a popular addition to modern blends.</li>
</ul>
<h2>Our hair oils, compared</h2>
<ul>
<li>[[deyga-oil|Deyga Hair Growth Oil]] ({{deyga-oil}}, 100ml): virgin coconut, almond, castor and sunflower oils infused with amla, bhringraj, hibiscus, fenugreek, curry leaves and other herbs, plus rosemary essential oil. A lightweight blend with an applicator tip for the scalp, and free from mineral oil and synthetic fragrance.</li>
<li>[[vilvah-oil|Vilvah Hair Growth Oil]] ({{vilvah-oil}}, 200ml): pumpkin seed, black seed (kalonji), castor, grapeseed and almond oils with vitamin E, rosemary and peppermint. Alcohol-free and non-sticky.</li>
<li>[[greying|Deyga Premature Greying Hair Oil]] ({{greying}}, 100ml): virgin coconut oil infused with amla, bhringraj, henna, bakuchi, moringa and liquorice, a classic Ayurvedic herbal blend.</li>
<li>[[dandruff-oil|Vilvah Anti-Dandruff Hair Oil]] ({{dandruff-oil}}, 100ml): almond, neem and sesame oils with tea tree, peppermint, camphor, lemon and basil oils and amla oil, for a fresh, cooling scalp massage.</li>
<li>[[neem|Deyga Neem Seed Oil]] ({{neem}}, 30ml): pure cold-pressed neem seed oil, a single ingredient. It has a strong natural smell, so most people mix a few drops into a lighter oil.</li>
</ul>
<p>See every <a href="/collections/hair-oil">hair oil</a> in one place.</p>
<h2>A note on "hair growth" oils</h2>
<p><strong>Hair growth oil</strong> is one of the most searched hair care terms in the UK, and it is the name several brands give their blends (see them on our <a href="/collections/hair-growth-oil">hair growth oil</a> page). Be realistic about what any oil can do: it conditions hair and scalp, makes lengths feel softer and helps them look healthier. Hair loss has many causes, from genes to hormones, stress and diet, and no oil can change those. If you notice sudden, patchy or heavy hair loss, speak to your GP.</p>
<h2>How to oil your hair, step by step</h2>
<ol>
<li><strong>Start with dry or slightly damp hair,</strong> before you wash it.</li>
<li><strong>Warm the oil.</strong> Stand the bottle in a bowl of warm water for a few minutes. Coconut-based oils turn solid in a cold bathroom; this melts them again.</li>
<li><strong>Part your hair into sections</strong> and apply a little oil along each parting with your fingertips or the applicator.</li>
<li><strong>Massage your scalp</strong> for 3 to 5 minutes with your fingertips in small circles, gently, without scratching.</li>
<li><strong>Smooth what is left through the lengths and ends,</strong> then comb through with a wide-tooth comb, such as a [[comb|neem wood comb]] ({{comb}}).</li>
<li><strong>Leave it on</strong> for at least 30 minutes, or overnight with a towel over your pillow.</li>
<li><strong>Shampoo,</strong> and if hair still feels oily, shampoo a second time. Then condition the lengths.</li>
</ol>
<p>Once or twice a week is plenty for most people.</p>
<h2>Hair oil for dry hair</h2>
<p>If your hair is dry, focus on the lengths and ends rather than the scalp, and choose a richer blend with coconut and castor oil. Between washes, smooth a single drop over the ends to tame flyaways, or use a lighter leave-in such as [[serum|Vilvah Anti-Frizz Hair Serum]] ({{serum}}). More ideas: <a href="/collections/hair-oil-for-dry-hair">hair oil for dry hair</a> and <a href="/collections/hair-serum-for-frizzy-hair">hair serum for frizzy hair</a>.</p>
<h2>Washing it out</h2>
<p>A gentle shampoo removes oil without leaving hair squeaky and dry. Try [[rice|Deyga Rice Water Shampoo]] ({{rice}}) or [[goat|Vilvah Goat Milk Shampoo]] ({{goat}}, 250ml) with goat milk, jasmine and pea protein. If your scalp tends to flake, [[dandruff-shampoo|Vilvah Herbal Shampoo for Dandruff Control]] ({{dandruff-shampoo}}) pairs with the Anti-Dandruff Hair Oil; see all <a href="/collections/shampoo-for-dandruff">shampoos for dandruff</a>. If flaking or itching does not settle, ask a pharmacist.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test first,</strong> especially with oils that contain essential oils such as tea tree, peppermint, camphor or rosemary.</li>
<li><strong>Keep oil away from your eyes,</strong> and do not use it on a broken, sore or irritated scalp.</li>
<li><strong>Protect your pillow and clothes:</strong> oils can mark fabric.</li>
</ul>
<p>Explore all our <a href="/collections/haircare">haircare</a>, all dispatched from the UK.</p>""",
    "faq": [
        ["How long should I leave oil in my hair?",
         "At least 30 minutes before you wash it. Many people leave it overnight with a towel over the pillow, then shampoo in the morning."],
        ["How often should I oil my hair?",
         "Once or twice a week, before washing, is plenty for most people. Very dry hair can have a drop of oil on the ends between washes."],
        ["What is amla hair oil?",
         "Amla is the Indian gooseberry. In an amla hair oil, the dried fruit is infused in a base oil such as coconut. It is one of the best-known ingredients in Ayurvedic hair care."],
        ["Does hair oil make hair grow?",
         "A hair oil conditions hair and scalp, so lengths feel softer and look healthier. Hair loss has many causes that no oil can change; if you notice sudden or patchy hair loss, speak to your GP."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_hair_oil_2026-10-27.jsonl")

"""Journal guide 'Frizzy hair: serum, oil or mask? How to choose for dry, frizzy hair' (user, 14 Nov 2026: 'Write the next 2 Journal guides').

Chosen from the client's Search Console export (4-10 Nov 2026, docs/seo/gsc_performance_7d_2026-11-14.xlsx): about 250
impressions a week, 0 clicks, positions 20-60, no guide yet: hair serum for frizzy hair (30, pos 35), serum for frizzy hair
(22, pos 41), frizzy hair serum (18, pos 21), dry hair mask (18, pos 58), hair oil for dry hair (18, pos 53), hair oil for
dry scalp, hair oil for dry frizzy hair, anti frizz hair serum. Semrush UK: hair mask for dry hair 2,400 (KD 13), hair oil
for dry hair 1,900 (KD 30), hair serum for frizzy hair 1,000 (KD 27), conditioner for dry hair 1,000, hair treatment for
dry hair 720. Facts = product descriptions + stored custom.inci (Admin read 14 Nov 2026).
Left out (ASA / unprovable): heat and UV protection, prevents split ends, reduces breakage, strengthens, repairs, rebuilds,
restores the barrier, curl definition, 'eliminates flyaways', hair growth / hair fall (Deyga Hair Growth Oil named once as a
pre-wash oil, not explained), 'safe in pregnancy', 'sulphate-free' (Vilvah Goat Milk Shampoo lists disodium laureth
sulfosuccinate). 'Silicone-free' kept for the serum and conditioner: the brand says it and their INCI lists no silicone.
Frizz explained in general cosmetic terms only. Prices are written into the text: re-run the generator and update the
body if prices change.

Usage: python3 tools/shopify/guide_frizzy_hair.py <allp_map.json>   (handle -> storefront product)
Output: docs/seo/guide_frizzy_hair_2026-11-14.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Frizzy hair: serum, oil or mask? How to choose for dry, frizzy hair",
    "handle": "frizzy-hair-serum-oil-mask",
    "tag": "Skin Studio",
    "summary": "What causes frizz, when to reach for a hair serum, a hair oil or a hair mask, and a simple weekly routine for dry, frizzy hair.",
    "mt": "Hair Serum for Frizzy Hair: Serum, Oil or Mask? | Swansura",
    "md": "How to choose a hair serum for frizzy hair, a hair mask for dry hair or a pre-wash oil, with a simple weekly routine for dry, frizzy hair.",
    "pick": {
        "serum": "vilvah-anti-frizz-hair-serum-30ml-silicone-free-hair-serum-with-black-seed-curry-leaf-oil-for-frizz-control-split-end-prevention-and-heat-protection",
        "mask": "vilvah-goat-milk-hair-mask-200g-deep-conditioning-treatment-for-frizz-flyaway-control-curl-definition-moisture-repair-mask",
        "frizzkit": "vilvah-frizz-free-hair-kit",
        "cond": "vilvah-cream-conditioner-500-ml-intense-moisturization-for-dry-frizzy-damaged-hair-with-tucuma-butter-broccoli-oil",
        "shampoo": "vilvah-goat-milk-shampoo-500-ml-intense-moisturisation-pea-protein-jasmine-for-frizz-control-shine",
        "gmkit": "vilvah-goat-milk-hair-kit",
        "serumkit": "vilvah-shampoo-hair-serum-kit",
        "soy": "deygas-soy-milk-conditioner-220-ml-vegan-protein-enriched-hair-conditioner-smooth-soft-frizz-free-hair",
        "rice": "deygas-rice-water-shampoo-220ml-natural-hair-care-for-smooth-nourished-hair",
        "deyoil": "deygas-hair-growth-oil-100-ml-natural-blend-of-coconut-amla-hibiscus-stronger-hair",
        "comb": "vilvah-neem-wood-comb-fine-wide-tooth-eco-friendly-anti-static-anti-frizz-anti-breakage-gentle-detangling-comb-for-all-hair-types-handcrafted-from-100-herbal-indian-neem-wood-set-of-2",
    },
    "titles": {},
    "shop": ["serum", "mask", "frizzkit", "cond", "shampoo", "gmkit", "soy", "comb"],
    "body": """<p>Frizz is one of the most common hair complaints, and it is usually a sign that hair is dry. The good news is that the fix is mostly moisture and a gentle routine, not a cupboard full of products. Here is what causes frizz, when to reach for a <strong>hair serum for frizzy hair</strong>, a pre-wash oil or a <strong>hair mask for dry hair</strong>, and how to put them together.</p>
<h2>Why hair goes frizzy</h2>
<p>Each strand has a smooth outer layer. When hair is dry, that layer lifts a little, strands lose their shine and they take in moisture from damp air, so they swell and stop lying flat. Rough towel drying, hot water, heat styling and brushing hair while it is wet all make it worse. That is why frizz often gets worse in winter, when indoor heating dries hair out, and on wet British days.</p>
<h2>Serum, oil or mask: what each one does</h2>
<ul>
<li><strong>A hair serum</strong> is a light leave-in for the lengths and ends. It smooths the surface of dry hair after washing, so flyaways lie flatter and hair looks glossier.</li>
<li><strong>A hair oil</strong> is usually richer and used before washing, on the scalp and lengths, then shampooed out.</li>
<li><strong>A hair mask</strong> is a thicker conditioner you leave on for longer, once or twice a week, for hair that feels rough and dry.</li>
</ul>
<p>Most dry, frizzy hair does well with all three in their place: a mask weekly, a conditioner every wash and a few drops of serum to finish.</p>
<h2>Hair serum for frizzy hair</h2>
<p>[[serum|Vilvah Anti-Frizz Hair Serum]] ({{serum}}, 30ml) is a light oil serum made without silicones. Its ingredient list is short: black seed oil, aloe vera, curry leaf oil, jasmine flower extract, hibiscus oil, glycerine, arnica oil, fenugreek seed extract, baobab oil, amla fruit extract, vitamin E and cypress essential oil.</p>
<p>Warm two or three drops between your palms and smooth them over the mid-lengths and ends of towel-dried or dry hair, keeping away from the roots. Start with less: you can always add a drop, but too much leaves hair looking greasy. It also comes as the [[serumkit|Vilvah Shampoo &amp; Hair Serum Kit]] ({{serumkit}}) with the Goat Milk Shampoo. Browse every <a href="/collections/hair-serum-for-frizzy-hair">hair serum for frizzy hair</a>.</p>
<h2>Hair mask for dry hair</h2>
<p>[[mask|Vilvah Goat Milk Hair Mask]] ({{mask}}, 200g) is made with goat milk, ceramides, argan oil, vitamin E, glycerine and a seaweed-based moisturising blend. Vilvah says it can be used as a mask, as a conditioner or as a small leave-in amount for styling.</p>
<p>As a mask, smooth it through clean, damp hair from the mid-lengths to the ends, comb it through with a wide-tooth comb, leave it for 10 to 15 minutes and rinse. Once or twice a week is plenty. The [[gmkit|Vilvah Goat Milk Hair Kit]] ({{gmkit}}) pairs the mask with the Goat Milk Shampoo. See more <a href="/collections/hair-mask-for-dry-hair">hair masks for dry hair</a>.</p>
<h2>Shampoo and conditioner for dry, frizzy hair</h2>
<p>A creamy shampoo and a rich conditioner do most of the daily work. [[shampoo|Vilvah Goat Milk Shampoo]] ({{shampoo}}) is made with goat milk, jasmine flower water, jojoba oil, panthenol and hydrolysed pea protein. Follow it with [[cond|Vilvah Cream Conditioner]] ({{cond}}), made without silicones and with tucuma butter, broccoli seed oil, aloe vera and pea protein; Vilvah says you can also leave it on for up to 15 minutes as a mask.</p>
<p>If you prefer something lighter, [[rice|Deyga Rice Water Shampoo]] ({{rice}}) uses rice water and mild coconut-derived cleansers, and [[soy|Deyga Soy Milk Conditioner]] ({{soy}}) adds soybean extract, argan oil and provitamin B5 without weighing hair down. For more on choosing one, read our <a href="/blogs/journal/natural-shampoo-guide">natural shampoo guide</a>.</p>
<h2>Pre-wash hair oil for dry hair</h2>
<p>Oiling before you wash is a long-standing Indian hair ritual, and it suits dry lengths well. [[deyoil|Deyga Hair Growth Oil]] ({{deyoil}}, 100ml) blends virgin coconut, almond, castor and sunflower oils infused with amla, hibiscus, fenugreek and bhringraj, with an applicator tip for the scalp. Leave it on for an hour or overnight, then shampoo it out. Our <a href="/blogs/journal/hair-oil-guide">hair oil guide</a> explains amla, bhringraj and castor oil and how to oil step by step, and you can browse every <a href="/collections/hair-oil-for-dry-hair">hair oil for dry hair</a>.</p>
<h2>A simple routine for frizzy hair</h2>
<ol>
<li><strong>Once a week, before washing:</strong> massage a little oil into the scalp and lengths and leave it on for an hour.</li>
<li><strong>Wash with lukewarm water,</strong> not hot, and a creamy shampoo. Lather mainly at the scalp.</li>
<li><strong>Condition every time,</strong> from the mid-lengths to the ends. Once or twice a week, swap the conditioner for a hair mask.</li>
<li><strong>Blot, do not rub.</strong> Squeeze water out with a soft towel or an old cotton T-shirt.</li>
<li><strong>Detangle gently</strong> with a wide-tooth comb, starting at the ends. A wooden comb such as the [[comb|Vilvah Neem Wood Comb]] ({{comb}}) glides through without tugging.</li>
<li><strong>Finish with two or three drops of serum</strong> on the ends, then air dry or blow-dry on a cool setting.</li>
</ol>
<p>Want it all in one box? The [[frizzkit|Vilvah Frizz Free Hair Kit]] ({{frizzkit}}) holds the Goat Milk Shampoo, Cream Conditioner and Anti-Frizz Hair Serum.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Less is more with serum and oil:</strong> start with a few drops and add more only if your ends still feel dry.</li>
<li><strong>Patch test</strong> products with essential oils, such as the serum and the pre-wash oil, before first use.</li>
<li><strong>Silk or satin pillowcases</strong> and a loose plait at night can help hair stay smoother by morning.</li>
<li><strong>Sudden changes</strong> in your hair or scalp, such as itching, soreness or hair loss, are worth showing to a pharmacist or your GP.</li>
</ul>
<p>Shop every <a href="/collections/hair-mask">hair mask</a>, <a href="/collections/conditioner">conditioner</a> and the full <a href="/collections/haircare">haircare</a> range, all dispatched from the UK.</p>""",
    "faq": [
        ["What is the best hair serum for frizzy hair?",
         "A light serum you can smooth over the ends without weighing hair down. The Vilvah Anti-Frizz Hair Serum is made without silicones, with black seed, curry leaf, hibiscus and baobab oils. Use two or three drops on towel-dried or dry hair, away from the roots."],
        ["Is a hair mask or a hair oil better for dry hair?",
         "They do different jobs. A hair oil is usually used before washing and shampooed out; a hair mask is a rich conditioner you leave on for 10 to 15 minutes after shampooing. Many people with dry hair use an oil once a week and a mask once or twice a week."],
        ["How often should I use a hair mask?",
         "Once or twice a week is plenty for most dry or frizzy hair. On the other wash days, use a regular conditioner from the mid-lengths to the ends."],
        ["Can I use hair serum every day?",
         "Yes, a few drops on the ends is fine daily. If hair starts to look heavy or greasy, use less or skip a day, and wash it out with your usual shampoo."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_frizzy_hair_2026-11-14.jsonl")

"""Journal guide 'Natural shampoo: how to choose one for dry hair, frizz and a flaky scalp' (user, 7 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): natural shampoo 3,600/mo (KD 21),
hair mask for dry hair 2,400 (KD 13), shampoo for dry hair 1,600 (KD 29), shampoo for dandruff 1,600 (KD 31),
rice water shampoo 1,300 (KD 13), conditioner for dry hair 1,000 (KD 22), paraben free shampoo 1,000 (KD 22).
Facts = product descriptions + the stored custom.inci lists (7 Nov 2026). Description claims NOT repeated (ASA):
combats dandruff, reduces hair fall / strengthens follicles, 'clinically proven', repairs / rebuilds damage. Dandruff:
product names and ingredients only, persistent flakes -> pharmacist/GP (same rule as the hair oil guide).
No 'sulphate-free' wording: Vilvah's shampoos list disodium laureth sulfosuccinate, so it is left unsaid.
Prices are written into the text: re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_natural_shampoo.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_natural_shampoo_2026-11-07.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Natural shampoo: how to choose one for dry hair, frizz and a flaky scalp",
    "handle": "natural-shampoo-guide",
    "tag": "Skin Studio",
    "summary": "How to choose a natural shampoo for dry hair, frizz or a flaky scalp, plus the conditioner and hair mask to follow it.",
    "mt": "Natural Shampoo Guide: Dry Hair, Frizz & Scalp | Swansura",
    "md": "How to choose a natural shampoo for dry hair, frizz or a flaky scalp, what rice water and goat milk shampoos are, and which conditioner or hair mask to use.",
    "pick": {
        "goat": "vilvah-goat-milk-shampoo-250ml",
        "rice": "deygas-rice-water-shampoo-220ml-natural-hair-care-for-smooth-nourished-hair",
        "deyga-ad": "deygas-anti-dandruff-shampoo-220-ml-scalp-soothing-flake-control-hair-cleanser",
        "herbal": "vilvah-herbal-shampoo-for-dandruff-control-500ml-natural-anti-dandruff-shampoo-with-neem-tea-tree-rosemary-black-pepper-paraben-sls-free-suitable-for-all-hair-types",
        "cond": "vilvah-cream-conditioner-250ml",
        "soy": "deygas-soy-milk-conditioner-220-ml-vegan-protein-enriched-hair-conditioner-smooth-soft-frizz-free-hair",
        "mask": "vilvah-goat-milk-hair-mask-200g-deep-conditioning-treatment-for-frizz-flyaway-control-curl-definition-moisture-repair-mask",
        "kit": "vilvah-shampoo-hair-serum-kit",
    },
    "titles": {},
    "shop": ["goat", "rice", "herbal", "deyga-ad", "cond", "soy", "mask", "kit"],
    "body": """<p>More people are switching to a <strong>natural shampoo</strong>: one built on plant-derived cleansers, with milks, waters and botanical extracts in place of a long list of synthetics. But "natural" is not a legal term in the UK, so the label alone tells you little. Here is how to read a shampoo, which one suits dry hair, frizz or a flaky scalp, and the conditioner or hair mask to follow it with.</p>
<h2>What makes a shampoo "natural"?</h2>
<p>Every shampoo needs a cleanser to lift oil and dirt. In the shampoos below, most come from coconut, corn or sugar beet: names such as <em>decyl glucoside</em>, <em>coco-glucoside</em>, <em>sodium cocoyl isethionate</em> and <em>cocamidopropyl betaine</em>. Around them sit the ingredients that give each shampoo its character, such as rice water, goat milk, rosemary or neem. Always read the full ingredient list on the product page: it tells you far more than the word "natural" on the front.</p>
<h2>Shampoo for dry hair</h2>
<p>Dry hair needs a cleanse that leaves moisture behind. Look for a creamy shampoo with milks, proteins or oils.</p>
<ul>
<li>[[goat|Vilvah Goat Milk Shampoo]] ({{goat}}, 250ml): goat milk and jasmine flower water with hydrolysed keratin, pea protein, panthenol and jojoba oil, in a creamy lather. Vilvah makes it for dry, frizzy or chemically treated hair.</li>
<li>[[rice|Deyga Rice Water Shampoo]] ({{rice}}, 50ml or 220ml): rice water with coconut- and corn-derived cleansers. A light, everyday shampoo for all hair types.</li>
</ul>
<h3>Rice water shampoo</h3>
<p>Rice water has long been used in Asian hair care, where people rinsed their hair with the water left from soaking rice. A <strong>rice water shampoo</strong> puts that into an easy, everyday cleanser; the Deyga one leads its ingredient list with rice water and leaves hair feeling soft and smooth.</p>
<h2>Shampoo for a flaky scalp</h2>
<p>Scalp shampoos use herbal ingredients with a fresh, clean feel:</p>
<ul>
<li>[[herbal|Vilvah Herbal Shampoo for Dandruff Control]] ({{herbal}}): neem leaf, tea tree and black pepper oils, rosemary and basil waters and amla, made without parabens.</li>
<li>[[deyga-ad|Deyga Anti Dandruff Shampoo]] ({{deyga-ad}}, 220ml): rosemary leaf hydrosol, ginger extract and a yeast ferment extract, with mild cleansers. Deyga makes it for frequent use and says it is safe for colour-treated hair.</li>
</ul>
<p>Massage it into the scalp, not just the lengths, and leave it for a minute before rinsing. Flakes, itching or redness that do not settle are worth showing to a pharmacist or your GP. Shop every <a href="/collections/shampoo-for-dandruff">shampoo for dandruff</a>, or see our <a href="/collections/concern-dandruff">dandruff care</a> edit.</p>
<h2>Conditioner for dry hair</h2>
<p>Conditioner smooths the hair after shampoo, so it detangles easily and feels softer.</p>
<ul>
<li>[[cond|Vilvah Cream Conditioner]] ({{cond}}, 250ml): tucuma butter, broccoli seed oil, aloe vera, jasmine and pea protein. Vilvah says it can also be left on for up to 15 minutes as a mask.</li>
<li>[[soy|Deyga Soy Milk Conditioner]] ({{soy}}, 50ml): soybean extract, argan oil, provitamin B5 and vitamin E in a lightweight texture.</li>
</ul>
<h2>Hair mask for dry hair</h2>
<p>Once a week, swap your conditioner for a mask. [[mask|Vilvah Goat Milk Hair Mask]] ({{mask}}, 200g) combines goat milk with ceramides, argan oil, vitamin E and a seaweed extract. Apply it to clean, damp lengths, leave it for 10 to 15 minutes, then rinse. Vilvah says it also works as a leave-in styling aid for curls. See every <a href="/collections/hair-mask-for-dry-hair">hair mask for dry hair</a>.</p>
<h2>How to wash your hair</h2>
<ol>
<li><strong>Wet your hair thoroughly</strong> with warm, not hot, water.</li>
<li><strong>Use a coin-sized amount</strong> of shampoo, more for long or thick hair.</li>
<li><strong>Focus on the scalp,</strong> massaging with your fingertips, not your nails. The lather will clean the lengths as you rinse.</li>
<li><strong>Rinse well,</strong> then apply conditioner to the mid-lengths and ends.</li>
<li><strong>Leave it for a minute or two,</strong> comb through with a wide-tooth comb, and rinse.</li>
<li><strong>Pat dry</strong> with a towel rather than rubbing, which can rough up the hair.</li>
</ol>
<p>How often? Dry or curly hair often does well with two or three washes a week; an oily scalp may prefer every other day. Natural shampoos can lather less than you are used to, so a second, smaller wash is fine.</p>
<h2>Before and after the wash</h2>
<p>Oiling before a wash is a long tradition in Indian hair care: read our <a href="/blogs/journal/hair-oil-guide">guide to hair oils</a>. For frizz after drying, a few drops of serum help smooth flyaways; the [[kit|Vilvah Shampoo &amp; Hair Serum Kit]] ({{kit}}) pairs the Goat Milk Shampoo with the Anti-Frizz Hair Serum. See all <a href="/collections/hair-serum-for-frizzy-hair">hair serums for frizzy hair</a>.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test</strong> a new shampoo behind the ear, especially one with essential oils such as tea tree or rosemary.</li>
<li><strong>Keep it out of your eyes;</strong> rinse with water if it gets in.</li>
<li><strong>Switching brands?</strong> Give your hair two or three weeks to settle before you judge.</li>
</ul>
<p>Shop every <a href="/collections/natural-shampoo">natural shampoo</a> and the full <a href="/collections/haircare">haircare</a> range, all dispatched from the UK.</p>""",
    "faq": [
        ["What is a natural shampoo?",
         "A shampoo built mainly on plant-derived cleansers, such as those from coconut, corn or sugar beet, with botanical ingredients like rice water, goat milk, rosemary or neem. 'Natural' is not a legal term in the UK, so always read the full ingredient list."],
        ["Which shampoo is best for dry hair?",
         "A creamy shampoo with milks, proteins or oils, such as the Vilvah Goat Milk Shampoo, followed by a conditioner and a weekly hair mask."],
        ["Should I use a hair mask or conditioner for dry hair?",
         "Both. Use conditioner after every wash and a hair mask, such as the Vilvah Goat Milk Hair Mask, once a week in place of conditioner, left on for 10 to 15 minutes."],
        ["How often should I wash my hair?",
         "Dry or curly hair often does well with two or three washes a week, while an oily scalp may prefer every other day. Focus the shampoo on the scalp and the conditioner on the lengths."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_natural_shampoo_2026-11-07.jsonl")

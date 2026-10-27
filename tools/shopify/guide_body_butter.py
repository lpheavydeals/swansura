"""Journal guide 'Body butter: how to choose it and how to use it' (user, 27 Oct 2026).

Target keywords (Semrush UK): body butter 6,600/mo (KD 12), body lotion for dry skin 1,300, cocoa butter body
lotion 480, body butter for dry skin 260, chocolate body butter 210. Facts come from product descriptions and our
INCI data (docs/data/deyga_inci_2026-10-23.json, docs/data/vilvah_inci_2026-10-22.json). Description claims
(stretch marks, skin barrier repair, age-defying, firming, calluses) are NOT repeated (ASA).
The body scrub guide is still unpublished, so it is not linked (link /collections/body-scrub instead).

Usage: python3 tools/shopify/guide_body_butter.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_body_butter_2026-10-27.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Body butter: how to choose it and how to use it",
    "handle": "how-to-use-body-butter",
    "tag": "Skin Studio",
    "summary": "Body butter vs body lotion, which suits dry skin, and how to use a body butter for soft skin all day.",
    "mt": "Body Butter Guide: Butter vs Lotion & How to Use | Swansura",
    "md": "Body butter vs body lotion, which suits dry skin and how to use it: chocolate, rose and luxury body butters compared, plus simple tips for soft skin.",
    "pick": {
        "choc": "deyga-chocolate-body-butter-100g", "rose": "deyga-rose-geranium-body-butter-40g",
        "hb": "natural-luminosity-body-butter", "almond": "deyga-almond-milk-body-lotion-100-ml",
        "milk": None, "foot": None, "lip": "superior-lip-butter-15ml",
        "polish": "vilvah-cookie-n-cream-body-polish-200ml", "deyga-scrub": "deyga-body-scrub-100g",
    },
    "titles": {"milk": "Vilvah Milk Body Lotion 250ml", "foot": "Deyga Foot Butter"},
    "shop": ["choc", "rose", "hb", "almond", "milk", "foot", "lip", "polish"],
    "body": """<p>When skin feels tight and dry, a <strong>body butter</strong> is the richest way to put comfort back. It is thicker than a lotion, melts on contact with warm skin and leaves a soft, cushioned finish. Here is how a body butter differs from a body lotion, which one suits your skin, and how to use it so a little goes a long way.</p>
<h2>Body butter vs body lotion: what is the difference?</h2>
<p>The difference is mostly water. A <strong>body lotion</strong> is mainly water with some oils and butters, so it feels light, sinks in fast and suits everyday use. A <strong>body butter</strong> is made mostly or entirely of plant butters and oils, such as shea butter, cocoa butter and almond oil, so it is richer, takes a little longer to sink in and leaves skin feeling soft for longer. Body creams sit in between.</p>
<ul>
<li><strong>Choose a body butter</strong> for very dry or rough skin, for elbows, knees, shins and heels, at night, and in cold weather.</li>
<li><strong>Choose a body lotion</strong> for a quick morning routine, for warm days, or if you dislike a rich finish.</li>
</ul>
<p>Many people use both: a lotion in the morning and a butter at night.</p>
<h2>Our body butters, compared</h2>
<h3>Chocolate body butter</h3>
<p>[[choc|Deyga Chocolate Body Butter]] ({{choc}}, 100g) is a short, simple blend: cocoa powder, shea butter, almond oil, jojoba oil, cocoa butter and vitamin E, with no water in the ingredient list. The cocoa gives it a light, natural chocolate scent rather than a sweet perfume, which makes this <strong>chocolate body butter</strong> a favourite for evenings and a lovely small gift.</p>
<h3>Rose and geranium body butter</h3>
<p>[[rose|Deyga Rose &amp; Geranium Body Butter]] ({{rose}}, 40g) swaps cocoa for floral essential oils: rose and geranium with shea butter, almond oil, jojoba oil and vitamin E. The 40g size is small enough for a handbag, for dry hands and elbows on the go.</p>
<h3>A luxury body butter</h3>
<p>[[hb|Highborn London Natural Luminosity Body Butter]] ({{hb}}) comes in a large 220ml glass jar in recyclable packaging, free from parabens and sulphates. Its butter-soft formula is made to smooth over the whole body, and the brand says it can be used on the face too.</p>
<h2>Body butter for dry skin: how to use it</h2>
<ol>
<li><strong>Apply after a shower or bath,</strong> while skin is still slightly damp. The butter seals in the water on your skin.</li>
<li><strong>Warm a small amount</strong>, about the size of a grape for each leg, between your palms until it softens.</li>
<li><strong>Press, then smooth</strong> it over the skin in long strokes, rather than rubbing hard.</li>
<li><strong>Add a little more</strong> to elbows, knees, shins and heels.</li>
<li><strong>Give it a few minutes</strong> to sink in before getting dressed. At night, it can work while you sleep.</li>
</ol>
<p>Once or twice a week, use a scrub first, such as [[polish|Vilvah Cookie N Cream Body Polish]] ({{polish}}) or [[deyga-scrub|Deyga Body Scrub]] ({{deyga-scrub}}). On freshly smoothed skin, a body butter spreads further and feels more even. Browse all <a href="/collections/body-scrub">body scrubs</a>.</p>
<h2>Prefer something lighter? Body lotions for dry skin</h2>
<p>If a butter feels too rich, a <strong>body lotion for dry skin</strong> gives you the same ingredients in a lighter texture:</p>
<ul>
<li>[[almond|Deyga Almond Milk Body Lotion]] ({{almond}}, 100ml): almond milk, cocoa butter, shea butter and almond oil with cucumber water. A good pick if you are looking for a <strong>cocoa butter body lotion</strong> that is quick to absorb.</li>
<li>[[milk|Vilvah Milk Body Lotion]] ({{milk}}, 250ml): oat milk, ceramides, olive squalane, coconut and jojoba oils in a vegan formula, made for daily use.</li>
</ul>
<p>See all <a href="/collections/body-lotion-for-dry-skin">body lotions for dry skin</a>, or shop more for <a href="/collections/dry-skin">dry skin</a>.</p>
<h2>Feet and lips</h2>
<p>Heels and lips are the driest places of all, and they have their own butters. [[foot|Deyga Foot Butter]] ({{foot}}, 40g) blends virgin coconut oil, olive oil, beeswax, vitamin E and vanilla essential oil; apply it at night and pull on cotton socks. For lips, [[lip|Highborn London Superior Lip Butter]] ({{lip}}) comes in a 15ml size, or a large 50ml.</p>
<h2>Body butter and perfume</h2>
<p>Perfume lasts longer on moisturised skin, because there is something for it to hold on to. Smooth an unscented or lightly scented butter over your pulse points before you spray. We explain how in <a href="/blogs/journal/layer-oud-with-body-butter">how to layer oud with body butter</a>.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test first,</strong> especially with butters that contain essential oils, such as rose, geranium or vanilla.</li>
<li><strong>Keep it cool.</strong> Natural butters soften in warm rooms and firm up in the cold; keep the jar out of direct sun and heat.</li>
<li><strong>Not for broken or irritated skin.</strong> If your skin is very dry, cracked or itchy for a long time, speak to a pharmacist or your GP.</li>
</ul>
<p>Shop all <a href="/collections/body-butter">body butters</a> and the rest of our <a href="/collections/bodycare">bath and body</a> range, all dispatched from the UK.</p>""",
    "faq": [
        ["What is the difference between body butter and body lotion?",
         "Body lotion is mostly water, so it feels light and sinks in fast. Body butter is made mostly of plant butters and oils, so it is richer and leaves skin feeling soft for longer."],
        ["Is body butter good for dry skin?",
         "Yes. Body butter is the richest way to moisturise dry or rough skin, especially on elbows, knees, shins and heels. Apply it to slightly damp skin after a shower."],
        ["Can I use body butter every day?",
         "Yes. Many people use a body butter every night, or a lighter body lotion in the morning and a butter at night."],
        ["Can I use body butter on my face?",
         "Only if the pack says face and body, as the Highborn London Natural Luminosity Body Butter does. Most body butters are too rich for facial skin."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_body_butter_2026-10-27.jsonl")

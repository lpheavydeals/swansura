"""Journal guide 'Body wash or bath bar? Natural body care for dry skin' (user, 16 Nov 2026: 'Write the next 2 Journal guides').

Semrush UK: natural body wash 1,300 (KD 19), body lotion for dry skin 1,300 (KD 11), bath bar 590 (KD 22),
charcoal soap 590 (KD 9). The body butter guide compares butters; the goat milk soap guide covers the Vilvah soaps;
this guide covers the wash itself and the lotion after it, and links both. All products in stock on 16 Nov
(storefront dump allp_map_1116.json). Facts = stored custom.inci + the descriptions rewritten 8 Nov (Admin read 16 Nov 2026).
Left out (ASA / unprovable): acne, oil control, pores, toxins, brightening / glow / skin tone, 'deeply hydrates',
'repairs the barrier', soothing, 'chemical-free', pH 5.5 (brand text only), antioxidant claims. The Spinach & Cucumber
bar's INCI has no spinach: described by its listed ingredients. Neem & Turmeric bar: name + ingredients only.
'Sulphate-free' only where the brand says it AND the INCI agrees (Deyga Wild Berry + Charcoal washes).
Prices are written into the text: re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_body_wash.py <allp_map.json>   (handle -> storefront product)
Output: docs/seo/guide_body_wash_2026-11-16.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Body wash or bath bar? Natural body care for dry skin",
    "handle": "natural-body-wash-guide",
    "tag": "Skin Studio",
    "summary": "Natural body wash or a bath bar: what is inside each, which suits dry skin, a shower routine for winter and the body lotion to follow.",
    "mt": "Natural Body Wash or Bath Bar for Dry Skin | Swansura",
    "md": "Natural body wash or bath bar for dry skin: the ingredients in each, a gentle shower routine for winter and the body lotion to use after.",
    "pick": {
        "goatwash": "vilvah-goat-milk-body-wash-200ml-moisturizing-body-wash-with-vanilla-extract-virgin-coconut-oil-acai-oil-gentle-cleanser-for-dry-sensitive-skin-ph-5-5",
        "berry": "deyga-wild-berry-body-wash-220ml",
        "charwash": "deyga-activated-charcoal-body-wash-220ml",
        "saffron": "deyga-shea-saffron-bath-bar-100g",
        "rose": "deyga-rose-pink-clay-bath-bar-100g",
        "spinach": "click-to-see-full-view-deyga-spinach-cucumber-bath-bar-100g",
        "neem": "deyga-neem-turmeric-bath-bar-100g",
        "charbar": "charcoal-bath-bar-130-g-deygas-natural-activated-charcoal-soap-for-all-skin-types-deep-cleansing-body-bar",
        "almond": "deyga-almond-milk-body-lotion-100-ml",
        "milklotion": "vilvah-milk-body-lotion-250ml-vegan-paraben-free-with-oat-milk-ceramides-olive-squalane-deep-moisturizing-for-dry-sensitive-skin-non-greasy-fast-absorbing-formula",
        "lotionkit": "vilvah-foot-cream-body-lotion-kit",
        "bathoil": "bath-shower-oil-with-roman-chamomile-cornish-lavender",
    },
    "titles": {},
    "shop": ["goatwash", "berry", "saffron", "rose", "spinach", "charwash", "milklotion", "almond"],
    "body": """<p>Hot showers, central heating and cold wind all leave skin feeling tight in winter, and the wash you use is the first place to make a change. A <strong>natural body wash</strong> or a simple <strong>bath bar</strong> made from plant oils can clean skin without that squeaky, stripped feel, especially when it is followed by a good <strong>body lotion for dry skin</strong>. Here is how the two compare, what is inside the ones we stock, and a simple shower routine for dry skin.</p>
<h2>Body wash or bath bar: what is the difference?</h2>
<p>A <strong>bath bar</strong> is true soap: plant oils and butters turned into soap with lye, which is why sodium hydroxide appears on the ingredient list. None of it is left in the finished bar. Bars are compact, last a long time on a draining dish and come with little or no plastic.</p>
<p>A <strong>body wash</strong> is a liquid made with mild cleansers, usually derived from coconut or sugar, plus water-based ingredients such as plant waters (hydrosols) and glycerin. It is easy to share, works well on a loofah and is simple to use on dry or sensitive skin.</p>
<p>Neither is better for every skin. If your skin feels tight after showering, try a creamy wash or a butter-rich bar, keep showers short, and always follow with a lotion.</p>
<h2>Natural body washes</h2>
<ul>
<li>[[goatwash|Vilvah Goat Milk Body Wash]] ({{goatwash}}, 200ml) is made for dry and sensitive skin, with goat milk, virgin coconut oil, acai oil and glycerine in a chamomile water base, cleansed with coconut-derived coco glucoside. It has a low lather and a soft vanilla scent.</li>
<li>[[berry|Deyga Wild Berry Body Wash]] ({{berry}}, 220ml) uses juniper berry and grapefruit hydrosols with a mild, fruity scent. Decyl glucoside from coconut gives a gentle lather, with glycerin and betaine from sugar beet. It is made without sulphates or parabens.</li>
<li>[[charwash|Deyga Activated Charcoal Body Wash]] ({{charwash}}, 220ml) has coconut-shell charcoal in a cucumber and vetiver hydrosol base, also without sulphates. It gives a thorough, fresh-feeling wash after the gym; follow it with a lotion if your skin runs dry.</li>
</ul>
<p>Browse every <a href="/collections/shower-gel-body-wash">shower gel and body wash</a>.</p>
<h2>Bath bars made with plant oils</h2>
<p>Deyga's bars share a base of extra virgin coconut oil, olive oil and castor oil, with a different hero ingredient in each:</p>
<ul>
<li>[[saffron|Deyga Shea Saffron Bath Bar]] ({{saffron}}, 100g): saffron, raw shea butter and sunflower oil, for a richer, creamy wash. A good pick for dry skin.</li>
<li>[[rose|Deyga Rose Pink Clay Bath Bar]] ({{rose}}, 100g): rose hydrosol, pink kaolin clay and raw shea butter.</li>
<li>[[spinach|Deyga Spinach &amp; Cucumber Bath Bar]] ({{spinach}}, 100g): cucumber hydrosol and raw shea butter, coloured green with spirulina and matcha.</li>
<li>[[charbar|Deyga Charcoal Bath Bar]] ({{charbar}}, 130g): activated charcoal, tea tree hydrosol and oil, aloe vera and unrefined shea butter. This is our <strong>charcoal soap</strong>.</li>
<li>[[neem|Deyga Neem &amp; Turmeric Bath Bar]] ({{neem}}, 100g): neem hydrosol and turmeric, two ingredients with a long history in Indian bathing traditions, with raw shea butter.</li>
</ul>
<p>Prefer goat milk? Our <a href="/blogs/journal/goat-milk-soap-guide">goat milk soap guide</a> covers the Vilvah bars.</p>
<h2>A shower routine for dry skin</h2>
<ol>
<li><strong>Keep the water warm, not hot,</strong> and the shower short.</li>
<li><strong>Use a little wash or a light lather from the bar,</strong> and focus on the areas that need it.</li>
<li><strong>Exfoliate once or twice a week, not every day.</strong> Our <a href="/blogs/journal/how-to-use-body-scrub">body scrub guide</a> explains how.</li>
<li><strong>Pat skin almost dry</strong> with a towel instead of rubbing.</li>
<li><strong>Apply a body lotion straight away,</strong> while skin is still slightly damp.</li>
</ol>
<h2>The body lotion for dry skin to follow</h2>
<ul>
<li>[[milklotion|Vilvah Milk Body Lotion]] ({{milklotion}}, 250ml): oat milk, ceramide NP, olive squalane, jojoba oil and glycerin in a light, non-greasy texture. It contains fragrance.</li>
<li>[[almond|Deyga Almond Milk Body Lotion]] ({{almond}}, 100ml): almond milk, cocoa butter, shea butter and almond oil, a handy size for travel.</li>
<li>The [[lotionkit|Vilvah Foot Cream &amp; Body Lotion Kit]] ({{lotionkit}}) pairs a body lotion with a foot cream for winter.</li>
</ul>
<p>Need something richer for elbows, knees and shins? Read our <a href="/blogs/journal/how-to-use-body-butter">body butter guide</a>, and see the <a href="/blogs/journal/foot-cream-guide">foot cream guide</a> for dry heels. For a slower evening, [[bathoil|anatomē Bath &amp; Shower Oil with Roman Chamomile &amp; Cornish Lavender]] ({{bathoil}}) can be smoothed over damp skin as the last step of a shower or added to a bath.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Let bars dry between uses</strong> on a draining dish so they stay firm and last longer.</li>
<li><strong>Patch test</strong> new products before first use, especially those with essential oils, such as the tea tree in the charcoal bar.</li>
<li><strong>Charcoal washes and bars</strong> can feel more thorough; on dry skin, use them a few times a week rather than every day.</li>
<li><strong>Skin that stays very dry, itchy, cracked or sore</strong> despite moisturising is worth showing to a pharmacist or your GP.</li>
</ul>
<p>Shop all <a href="/collections/bodycare">body care</a>, <a href="/collections/body-lotion">body lotions</a> and products for <a href="/collections/dry-skin">dry skin</a>, all dispatched from the UK with free UK delivery over £40.</p>""",
    "faq": [
        ["Is a bath bar or a body wash better for dry skin?",
         "Either can work. Choose a creamy body wash with mild cleansers, or a bar rich in plant butters such as shea, keep showers short and warm rather than hot, and apply a body lotion straight after, while skin is still slightly damp."],
        ["What is a natural body wash?",
         "A body wash made mainly from plant-derived ingredients. Ours use mild cleansers from coconut or sugar, such as decyl glucoside and coco glucoside, with plant waters, glycerin and oils. The full ingredient list is on each product page."],
        ["Why does a natural soap bar list sodium hydroxide?",
         "Soap is made by mixing oils and butters with lye (sodium hydroxide). The reaction turns them into soap and glycerin, and no lye remains in the finished bar, but it is still listed because it was used to make it."],
        ["When should I apply body lotion?",
         "Straight after a bath or shower, while skin is still slightly damp, and again whenever skin feels tight. Give extra attention to elbows, knees and shins in winter."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_body_wash_2026-11-16.jsonl")

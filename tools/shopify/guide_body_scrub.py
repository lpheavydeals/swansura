"""Journal guide 'Body scrub: how to choose one and how often to use it' (user, 27 Oct 2026).

Target keywords (Semrush UK): body scrub 12,100/mo (KD 18), coffee body scrub 390, body scrub for dry skin 70,
natural body scrub uk 30. Facts come from product descriptions and our INCI data (docs/data/deyga_inci_2026-10-23.json,
docs/data/vilvah_inci_2026-10-22.json). Description claims (removes tan, unclogs pores, reduces pigmentation /
breakouts, cracked heels) are NOT repeated (ASA).

Usage: python3 tools/shopify/guide_body_scrub.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_body_scrub_2026-10-27.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Body scrub: how to choose one and how often to use it",
    "handle": "how-to-use-body-scrub",
    "tag": "Skin Studio",
    "summary": "Cream, coffee and powder body scrubs compared, how to use one step by step, and how often to scrub.",
    "mt": "Body Scrub Guide: How to Choose & Use One | Swansura",
    "md": "How to choose a body scrub and how often to use it: cream, coffee and powder scrubs compared, a step-by-step routine and tips for dry and sensitive skin.",
    "pick": {
        "polish": "vilvah-cookie-n-cream-body-polish-200ml",
        "deyga-scrub": "deyga-body-scrub-100g",
        "powder": None, "luminosity": "natural-luminosity-scrub", "loofah": "deyga-organic-loofah-for-body-exfoliation",
        "kit": None, "hb-set": "scrub-and-glow-luminosity-set",
        "choc": "deyga-chocolate-body-butter-100g", "rose-butter": "deyga-rose-geranium-body-butter-40g",
        "hb-butter": "natural-luminosity-body-butter", "lotion": None,
        "foot-scrub": "deyga-foot-scrub-100-g", "foot-butter": None,
        "strawberry": None, "vilvah-lip": None,
    },
    "titles": {
        "powder": "Deyga Face & Body Exfoliator Powder", "kit": "Vilvah Body Polishing Kit",
        "lotion": "Vilvah Milk Body Lotion 250ml", "foot-butter": "Deyga Foot Butter",
        "strawberry": "Deyga Strawberry Lip Scrub", "vilvah-lip": "Vilvah Natural Lip Scrub",
    },
    "shop": ["polish", "deyga-scrub", "luminosity", "kit", "powder", "choc", "foot-scrub", "loofah"],
    "body": """<p>A <strong>body scrub</strong> is the quickest way to make skin feel smoother. It buffs away the dry, dull surface layer, so skin feels softer straight away and your body lotion or butter spreads more easily afterwards. But scrubs are not all the same: some are creamy, some are gritty, some are powders you mix yourself. Here is how to choose a body scrub, how to use it and how often.</p>
<h2>What does a body scrub do?</h2>
<p>A body scrub is a physical exfoliator: small grains, such as sugar, coffee or fine plant powders, gently lift away dead skin cells as you massage. The result is skin that feels smoother and looks more even and fresh. It also makes the next step work better, because a moisturiser goes onto clean, smooth skin rather than a dry, flaky layer.</p>
<h2>Which type of body scrub is right for you?</h2>
<h3>Cream body polish: gentle and quick</h3>
<p>A cream polish mixes fine grains into a soft, creamy base, so it cleans and exfoliates at the same time and can replace your shower gel on scrub days. [[polish|Vilvah Cookie N Cream Body Polish]] ({{polish}}, 200ml) combines coffee powder and ivory palm seed powder with shea butter, olive oil, argan oil and almond milk extract. It suits most skin types, including dry skin.</p>
<h3>Powder scrubs: mix to the texture you like</h3>
<p>Powder scrubs come dry; you mix a spoonful with water, rose water or toner into a paste. That makes them easy to adjust: a thicker paste for elbows and knees, a thinner one for softer skin. [[deyga-scrub|Deyga Body Scrub]] ({{deyga-scrub}}, 100g) is a blend of dried fruit powders (lemon, papaya, pineapple, pomegranate and bitter orange) with purple rice. For something finer that also works on the face, [[powder|Deyga Face &amp; Body Exfoliator]] ({{powder}}, 50g) blends lemon, neem, matcha and black rice.</p>
<h3>A luxury scrub in a jar</h3>
<p>[[luminosity|Highborn London Natural Luminosity Scrub]] ({{luminosity}}) is a natural exfoliant in a large 220ml glass jar, free from parabens and sulphates, in recyclable packaging. A good choice for a treat or a gift.</p>
<h3>Tools: a loofah</h3>
<p>Prefer to use your usual shower gel? A natural loofah such as the [[loofah|Deyga Organic Loofah]] ({{loofah}}), made from plant fibres and biodegradable, adds gentle exfoliation to every wash.</p>
<h2>Coffee body scrub: why it is so popular</h2>
<p>A <strong>coffee body scrub</strong> is one of the most searched types in the UK. Ground coffee gives a satisfying, even texture and a warm, comforting smell that makes scrub day feel like a treat. Look for one in a creamy base with oils or butters, so skin does not feel tight afterwards; the Vilvah Cookie N Cream Body Polish is a good example. Rinse the shower tray afterwards so grounds do not build up in the drain.</p>
<h2>How to use a body scrub, step by step</h2>
<ol>
<li><strong>Warm up.</strong> Shower or bathe for a few minutes first, so skin is warm and damp.</li>
<li><strong>Take a small amount</strong>, about a tablespoon for each arm or leg.</li>
<li><strong>Massage in slow circles</strong> with light pressure. Let the grains do the work; you do not need to press hard.</li>
<li><strong>Spend a little longer on rough areas</strong>, such as elbows, knees and heels.</li>
<li><strong>Rinse well</strong> with warm, not hot, water and pat skin dry.</li>
<li><strong>Moisturise straight away</strong>, while skin is still slightly damp.</li>
</ol>
<h2>How often should you use a body scrub?</h2>
<p>For most people, <strong>once or twice a week</strong> is plenty. Dry or sensitive skin may prefer once a week, or a gentler cream polish. Scrubbing every day can leave skin feeling tight or tender, so more is not better. Skip the scrub on skin that is sunburnt, irritated, broken or freshly shaved or waxed; many people scrub the day before hair removal instead.</p>
<h2>Body scrub for dry skin: what to use afterwards</h2>
<p>If your skin is dry, the step after the scrub matters most. A rich butter locks in moisture on freshly exfoliated skin:</p>
<ul>
<li>[[choc|Deyga Chocolate Body Butter]] ({{choc}}, 100g): cocoa powder, cocoa butter and shea butter with almond and jojoba oils, and a light chocolate scent.</li>
<li>[[rose-butter|Deyga Rose &amp; Geranium Body Butter]] ({{rose-butter}}, 40g): shea butter, almond and jojoba oils with rose and geranium essential oils, in a handbag size.</li>
<li>[[hb-butter|Highborn London Natural Luminosity Body Butter]] ({{hb-butter}}), the partner to the Luminosity Scrub, in a 220ml glass jar.</li>
<li>Prefer something lighter? [[lotion|Vilvah Milk Body Lotion]] ({{lotion}}) with oat milk, ceramides and olive squalane.</li>
</ul>
<p>See all our <a href="/collections/body-butter">body butters</a>, and more ideas for <a href="/collections/dry-skin">dry skin</a>.</p>
<h2>Scrub sets</h2>
<p>The [[kit|Vilvah Body Polishing Kit]] ({{kit}}) pairs the Cookie N Cream Body Polish with a matching body mask made with kaolin clay, almond milk extract and coffee extract. The [[hb-set|Highborn London Scrub and Glow Luminosity Set]] ({{hb-set}}) puts two Highborn products for face and body together in one box.</p>
<h2>Don't forget feet and lips</h2>
<p>Feet and lips need their own scrubs: body scrubs are too coarse for lips, and heels usually need a stronger one. For feet, use [[foot-scrub|Deyga Foot Scrub]] ({{foot-scrub}}) once a week, then [[foot-butter|Deyga Foot Butter]] ({{foot-butter}}) before socks. For lips, a sugar scrub such as [[strawberry|Deyga Strawberry Lip Scrub]] ({{strawberry}}) or [[vilvah-lip|Vilvah Natural Lip Scrub]] ({{vilvah-lip}}) is all you need; see all <a href="/collections/lip-scrub">lip scrubs</a>.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test first</strong> on a small area, especially if your skin is sensitive.</li>
<li><strong>Keep body scrubs off your face</strong> unless the pack says face and body: facial skin is thinner.</li>
<li><strong>Keep water out of the jar</strong> and use dry hands to scoop, so the scrub stays fresh.</li>
</ul>
<p>Shop every <a href="/collections/body-scrub">body scrub</a> and the rest of our <a href="/collections/bodycare">bath and body</a> range, all dispatched from the UK.</p>""",
    "faq": [
        ["How often should I use a body scrub?",
         "Once or twice a week is plenty for most people. Dry or sensitive skin may prefer once a week or a gentler cream polish."],
        ["Should I use a body scrub before or after shaving?",
         "Scrub before, not straight after. Many people scrub the day before shaving or waxing, because freshly shaved skin can feel tender."],
        ["Can I use a body scrub on my face?",
         "Only if the pack says face and body, such as the Deyga Face & Body Exfoliator. Most body scrubs are too coarse for facial skin."],
        ["What should I use after a body scrub?",
         "A moisturiser, straight away while skin is still slightly damp. A body butter suits dry skin; a body lotion feels lighter."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_body_scrub_2026-10-27.jsonl")

"""Journal guide 'Under eye cream: how to choose one and how to apply it' (user, 8 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): under eye cream 2,900/mo (KD 19),
under eye cream for dark circles 1,000 (KD 20; answered honestly: no promise to remove dark circles),
deyga under eye cream 20, vilvah under eye cream 20. Facts = product descriptions + stored custom.inci (8 Nov 2026;
Imperial Eye Gel has no stored list, so its ingredients come from its description). Left out (ASA / unprovable):
reduces dark circles / puffiness / melanin, smooths fine lines and wrinkles, 'visible results in 4 weeks',
improves circulation, skin repair, firmness. Prices are written into the text: re-run the generator and update
the body if prices change.

Usage: python3 tools/shopify/guide_under_eye_cream.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_under_eye_cream_2026-11-08.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Under eye cream: how to choose one and how to apply it",
    "handle": "under-eye-cream-guide",
    "tag": "Skin Studio",
    "summary": "Eye cream, eye gel or eye balm? How to choose an under eye cream, how to apply it gently, and what an eye cream can and cannot do.",
    "mt": "Under Eye Cream Guide: How to Choose & Apply | Swansura",
    "md": "How to choose an under eye cream, gel or balm, how to apply it without tugging, and an honest look at dark circles and tired-looking eyes.",
    "pick": {
        "deyga": "deygas-under-eye-cream-15-g-natural-organic-eye-brightening-moisturizer-for-dark-circles-puffiness",
        "vilvah": "vilvah-natural-under-eye-cream-for-dark-circles-puffiness-under-eye-dark-circle-control-cream-bamboo-goji-berry-dipalmitoyl-hydroxyproline-20-ml",
        "gel": "imperial-eye-gel",
        "mask": "deyga-under-eye-mask-15g",
        "lift": "vilvah-face-lift-kit",
        "ha": "deyga-2-hyaluronic-acid-serum-20ml",
        "spf": "vilvah-skin-finish-sunscreen-spf-50-pa",
        "rose": "deyga-pure-rose-water-toner-100-ml",
    },
    "titles": {},
    "shop": ["deyga", "vilvah", "gel", "mask", "lift", "ha", "spf", "rose"],
    "body": """<p>The skin around your eyes is thinner than the rest of your face, and it moves every time you blink, smile or squint. That is why many people give it its own product. An <strong>under eye cream</strong> is a small, gentle moisturiser made for this delicate area. Here is how to choose one, how to apply it, and what to expect.</p>
<h2>Do you need an eye cream?</h2>
<p>You can use your face moisturiser around the eyes, as long as it does not sting. An eye cream is worth it if your moisturiser feels too rich or makes your eyes water, if the area feels dry or tight, or if you simply enjoy a separate step. Eye creams come in small jars, have a texture made for patting on, and are usually made without added fragrance.</p>
<h2>Cream, gel or balm?</h2>
<ul>
<li><strong>Light creams</strong> suit most skin and sit well under make-up.</li>
<li><strong>Gels</strong> feel cool and weightless, and suit oily skin or a morning routine.</li>
<li><strong>Balms and oils</strong> are richer, and suit dry skin or a night routine.</li>
</ul>
<h2>Under eye creams to try</h2>
<p>[[deyga|Deyga Under Eye Cream]] ({{deyga}}, 15g) is a light, cooling cream of aloe vera, cucumber hydrosol, almond oil, potato starch and vitamin E. Deyga makes it without silicones, parabens or artificial fragrance, and it can sit under make-up. [[vilvah|Vilvah Natural Under Eye Cream]] ({{vilvah}}, 20ml) is a little richer: glycerine, witch hazel, shea butter and sunflower seed oil with bamboo, goji berry and cardamom extracts, made without alcohol or silicones.</p>
<p>For a gel, [[gel|Highborn London Imperial Eye Gel]] ({{gel}}, 10ml, 15ml or 30ml) gives lightweight moisture with a cooling feel: glycerin and a form of hyaluronic acid with argan, avocado and sunflower oils. It contains fragrance, so patch test it if your skin is sensitive. See every <a href="/collections/eye-cream">eye cream</a>.</p>
<h2>An eye balm for night</h2>
<p>[[mask|Deyga Under Eye Mask]] ({{mask}}, 15g) is a rich balm rather than a sheet mask: kalonji (black seed), hemp seed, almond, rosehip and carrot seed oils with beeswax. Dab a little on before bed, when there is no make-up to layer on top.</p>
<h2>What about dark circles?</h2>
<p>Dark circles have many causes, from the shape of the face and the shadows it casts to genes, tiredness and allergies. An eye cream keeps the skin moisturised and comfortable, and a cool, light texture can make tired-looking eyes feel fresher, but no cream can promise to remove dark circles. Sleep, sunscreen and a little concealer often help more. If the area suddenly darkens, swells or itches, ask a pharmacist or your GP.</p>
<h2>How to apply eye cream</h2>
<ol>
<li><strong>Cleanse and tone</strong> first. A gentle toner such as [[rose|Deyga Pure Rose Water Toner]] ({{rose}}) keeps the routine simple; read our guide to <a href="/blogs/journal/face-wash-for-your-skin-type">face wash for your skin type</a>.</li>
<li><strong>Take a rice-grain amount</strong> for both eyes. More is not better here.</li>
<li><strong>Use your ring finger,</strong> which has the lightest touch, and dot the cream along the orbital bone, below the eye and under the brow.</li>
<li><strong>Pat, do not rub,</strong> working from the inner corner outwards. Keep it off the lash line and out of your eyes.</li>
<li><strong>Follow with your moisturiser</strong> on the rest of the face, and SPF in the morning.</li>
</ol>
<p>If you use a serum, apply it before the eye cream; [[ha|Deyga 2% Hyaluronic Acid Serum]] ({{ha}}) is a light option. For moisturiser, see <a href="/blogs/journal/moisturiser-for-your-skin-type">moisturiser for your skin type</a>.</p>
<h2>Morning and night</h2>
<p>In the morning, choose a light cream or gel that sits well under make-up, and finish with sunscreen: the skin around the eyes is often forgotten. [[spf|Vilvah Skin Finish Sunscreen SPF 50 PA+++]] ({{spf}}) is a light everyday option; keep it just outside the eye area if it stings. At night you can use a richer cream or balm. The [[lift|Vilvah Face Lift Kit]] ({{lift}}) pairs Vilvah's Ultra Moisturising Cream with its Under Eye Cream (Advanced), which contains bakuchiol, niacinamide, ceramides and hyaluronic acid.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test</strong> any new eye product on your jaw or inner arm first.</li>
<li><strong>Keep it out of your eyes;</strong> rinse with clean water if it gets in.</li>
<li><strong>Use clean fingers</strong> and close the jar after use.</li>
<li><strong>Stinging, redness or swelling</strong> that does not settle is worth showing to a pharmacist or your GP.</li>
</ul>
<p>Explore more for <a href="/collections/sensitive-skin">sensitive skin</a> and <a href="/collections/concern-hydration">hydration</a>, every <a href="/collections/serum">serum</a> and <a href="/collections/sunscreen">sunscreen</a>, and the full <a href="/collections/skincare">skincare</a> range, all dispatched from the UK.</p>""",
    "faq": [
        ["Do I need an under eye cream?",
         "Not always. You can use your face moisturiser around the eyes if it does not sting. An eye cream helps if your moisturiser feels too rich there, or if the area feels dry or tight."],
        ["Can an eye cream get rid of dark circles?",
         "No cream can promise that. Dark circles have many causes, including face shape, genes and tiredness. An eye cream keeps the skin moisturised and comfortable; sleep, sunscreen and concealer often help more."],
        ["How do I apply eye cream?",
         "Use a rice-grain amount for both eyes, dot it along the orbital bone with your ring finger and pat it in from the inner corner outwards, keeping it off the lash line."],
        ["Should I use eye cream in the morning or at night?",
         "Both work. Choose a light cream or gel in the morning so it sits well under make-up and sunscreen, and a richer cream or balm, such as the Deyga Under Eye Mask, at night."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_under_eye_cream_2026-11-08.jsonl")

"""Journal guide 'Face wash for your skin type: dry, oily and sensitive skin' (user, 7 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): tea tree face wash 1,900/mo (KD 28),
face wash for dry skin 1,600 (KD 29), face wash for oily skin 1,600 (KD 33), face wash for sensitive skin 1,600
(KD 22), vitamin c face wash 1,000 (KD 21), natural face wash 880 (KD 21), charcoal face wash 590 (KD 11).
Facts = product descriptions + the stored custom.inci lists (7 Nov 2026). Description claims NOT repeated (ASA):
reduces pigmentation / fades dark spots, controls oil for 8 hours, calms inflammation / acne, minimises pores,
boosts collagen / cell repair. Skin-type suitability is taken from the brands' own descriptions.
Prices are written into the text: re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_face_wash.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_face_wash_2026-11-07.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Face wash for your skin type: dry, oily and sensitive skin",
    "handle": "face-wash-for-your-skin-type",
    "tag": "Skin Studio",
    "summary": "How to choose a face wash for dry, oily or sensitive skin, what tea tree, charcoal and vitamin C washes are, and how to cleanse.",
    "mt": "Face Wash for Dry, Oily & Sensitive Skin: A Guide | Swansura",
    "md": "How to choose a face wash for dry, oily or sensitive skin: cream, foam and powder cleansers, tea tree, charcoal and vitamin C washes, and how to cleanse.",
    "pick": {
        "oat": "deyga-oat-milk-face-wash-100-ml",
        "ff": "vilvah-fragrance-free-cream-face-wash-100ml-gentle-hydrating-cleanser-for-sensitive-dry-skin-sulfate-free-paraben-free-silicone-free-enriched-with-banana-coconut-milk-extracts",
        "honey": "vilvah-honey-face-wash-raw-honey-fruit-extracts-100ml",
        "powder": "vilvah-store-milk-powder-face-wash-50g-brightening-powder-to-foam-cleanser-with-rice-complex-hyaluronic-acid-papain-for-normal-to-oily-skin-fragrance-talc-free",
        "charcoal": "charcoal-face-wash-100ml-natural-deep-cleansing-for-all-skin-types-deygas",
        "vitc": "deyga-vitamin-c-foaming-face-wash-100ml",
        "shiseido": "shiseido-complete-cleansing-microfoam-180ml-gentle-foaming-face-cleanser",
        "crystal": "crystal-cleanser-100ml",
    },
    "titles": {},
    "shop": ["oat", "ff", "honey", "powder", "charcoal", "vitc", "shiseido", "crystal"],
    "body": """<p>A good cleanse is the first step of every skincare routine, and the wrong <strong>face wash</strong> can undo the rest. Too harsh, and skin feels tight and dry; too rich, and oily skin feels heavy. Here is how to choose a face wash for your skin type, what the different textures and ingredients mean, and how to cleanse.</p>
<h2>First, know your skin type</h2>
<p>Wash with a mild cleanser, pat dry and wait about an hour without applying anything. Then look and feel:</p>
<ul>
<li><strong>Dry:</strong> feels tight, and may look flaky or dull.</li>
<li><strong>Oily:</strong> looks shiny all over, especially on the forehead, nose and chin.</li>
<li><strong>Combination:</strong> shiny in the centre, normal or dry on the cheeks.</li>
<li><strong>Sensitive:</strong> easily stings, turns red or reacts to fragrance.</li>
</ul>
<h2>Face wash for dry skin</h2>
<p>Dry skin needs a cleanser that lifts away the day without stripping. Look for creamy or milky textures and soothing, moisture-loving ingredients.</p>
<p>[[oat|Deyga Oat Milk Face Wash]] ({{oat}}, 100ml) combines oat milk with provitamin B5, kaolin and mild cleansers made from coconut and corn. Deyga makes it for dry, sensitive and normal skin. [[ff|Vilvah Fragrance-Free Cream Face Wash]] ({{ff}}, 100ml) is a soft cream with banana fruit extract, hydrolysed wheat protein and glycerine. Shop every <a href="/collections/face-wash-for-dry-skin">face wash for dry skin</a>.</p>
<h2>Face wash for sensitive skin</h2>
<p>If your skin reacts easily, keep the ingredient list short and skip added fragrance. The Vilvah Fragrance-Free Cream Face Wash is made without fragrance, and Vilvah describes it as pH-balanced. The Deyga Oat Milk Face Wash is mild too, but it does contain fragrance, so patch test it first. See more for <a href="/collections/sensitive-skin">sensitive skin</a>.</p>
<h2>Face wash for oily skin</h2>
<p>Oily skin likes a foaming or gel wash that leaves skin feeling fresh but not squeaky. Over-washing can make skin feel tighter without making it any less shiny, so twice a day is enough.</p>
<ul>
<li>[[honey|Vilvah Honey Face Wash]] ({{honey}}, 100ml): 10% raw honey with papaya and blackberry extracts, witch hazel and gotu kola, and a citrus-vanilla scent. Vilvah makes it for normal to oily skin, with a medium foam.</li>
<li>[[powder|Vilvah Milk Powder Face Wash]] ({{powder}}, 50g): a water-free powder that turns to foam in wet hands, with rice powder, rice milk extract, oat flour, hyaluronic acid and papain, a papaya enzyme. Fragrance-free and made for normal to oily skin.</li>
</ul>
<p>Shop every <a href="/collections/face-wash-for-oily-skin">face wash for oily skin</a> and more for <a href="/collections/oily-skin">oily skin</a>.</p>
<h2>Tea tree, charcoal and vitamin C face washes</h2>
<h3>Tea tree and charcoal</h3>
<p>[[charcoal|Deyga Charcoal Face Wash]] ({{charcoal}}, 100ml) is a gel built on tea tree hydrosol, with activated charcoal from coconut shell and gentle coconut and corn-based cleansers. It is a popular pick if you are looking for a <strong>tea tree face wash</strong>: fresh-feeling, and made for all skin types.</p>
<h3>Vitamin C</h3>
<p>[[vitc|Deyga Vitamin C Foaming Face Wash]] ({{vitc}}, 100ml) uses ascorbyl glucoside, a stable form of vitamin C, with citron, bitter orange and lemon hydrosols in a light foam. A bright, zesty wash for the morning.</p>
<h2>Cream, foam or powder?</h2>
<ul>
<li><strong>Cream and milk washes</strong> feel the softest: good for dry and sensitive skin.</li>
<li><strong>Foams and gels</strong> feel fresh and light: good for oily and combination skin. [[shiseido|Shiseido Complete Cleansing Microfoam]] ({{shiseido}}, 180ml) is a fine, lightweight foam for everyday use.</li>
<li><strong>Powders</strong> are mixed with water as you use them, and travel well.</li>
<li><strong>A luxury cleanser:</strong> [[crystal|Highborn London Crystal Cleanser]] ({{crystal}}, 100ml) contains co-enzyme Q10 and is made for morning and night.</li>
</ul>
<h2>How to wash your face</h2>
<ol>
<li><strong>Wet your face</strong> with lukewarm water, not hot.</li>
<li><strong>Use a small amount,</strong> about the size of a 5p coin, and work it into a lather in your hands.</li>
<li><strong>Massage gently</strong> for 30 to 60 seconds, including the hairline and jaw. Keep it away from your eyes.</li>
<li><strong>Rinse well</strong> and pat dry with a clean towel.</li>
<li><strong>Follow straight away</strong> with toner or moisturiser while skin is still slightly damp.</li>
</ol>
<p>Most people do best washing twice a day: morning and night. If you wear make-up or sunscreen, cleanse twice at night: once to lift it, once to clean the skin.</p>
<h2>After cleansing</h2>
<p>A cleanser is only the first step. Add a <a href="/collections/toner">toner</a> if you like one, then a moisturiser: see our <a href="/collections/moisturiser-for-dry-skin">moisturisers for dry skin</a>. Light, soothing layers such as aloe vera gel suit oily skin; read <a href="/blogs/journal/how-to-use-aloe-vera-gel">how to use aloe vera gel</a>. Not sure which natural brand suits you? Compare them in <a href="/blogs/journal/deyga-or-vilvah">Deyga or Vilvah</a>.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test</strong> any new face wash on your jaw or inner arm first.</li>
<li><strong>Change one thing at a time,</strong> so you know what suits you.</li>
<li><strong>Breakouts, redness or itching that last</strong> are worth showing to a pharmacist or your GP.</li>
</ul>
<p>Browse every <a href="/collections/cleanser">cleanser</a> and the full <a href="/collections/skincare">skincare</a> range, all dispatched from the UK.</p>""",
    "faq": [
        ["What is the best face wash for dry skin?",
         "Choose a creamy or milky face wash without harsh foaming agents, such as the Deyga Oat Milk Face Wash or the Vilvah Fragrance-Free Cream Face Wash, and follow it with a moisturiser while skin is still slightly damp."],
        ["What face wash is good for oily skin?",
         "A light foaming or gel wash, used twice a day, such as the Vilvah Honey Face Wash or the Vilvah Milk Powder Face Wash, both made for normal to oily skin."],
        ["Which face wash suits sensitive skin?",
         "A short ingredient list without added fragrance. The Vilvah Fragrance-Free Cream Face Wash is made without fragrance. Patch test any new cleanser first."],
        ["How often should I wash my face?",
         "Twice a day, morning and night, suits most people. Washing more often can leave skin feeling tight. If you wear make-up or sunscreen, cleanse twice at night."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_face_wash_2026-11-07.jsonl")

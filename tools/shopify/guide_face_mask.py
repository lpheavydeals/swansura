"""Journal guide 'Face masks: clay, charcoal and face packs, and how to use them' (user, 7 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): face mask 22,200/mo (KD 30),
clay face mask 1,900 (KD 22), face mask for oily skin 210 (KD 20), multani mitti face pack 140 (KD 25).
Facts = product descriptions + stored custom.inci (7 Nov 2026; the 24K Gold mask has no stored list, so its
ingredients come from its description). Left out (ASA / unprovable): draws out toxins, reduces acne / blemishes /
dark spots / pigmentation / tan, minimises pores, controls oil, boosts collagen, reduces dark circles / puffiness,
'instantly brightens'. Multani mitti is explained but not sold. Prices are written into the text: re-run the
generator and update the body if prices change.

Usage: python3 tools/shopify/guide_face_mask.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_face_mask_2026-11-07.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Face masks: clay, charcoal and face packs, and how to use them",
    "handle": "face-mask-guide",
    "tag": "Skin Studio",
    "summary": "Clay, charcoal, cream and powder face masks explained: which suits your skin, how to use a face mask and how often.",
    "mt": "Face Masks Guide: Clay, Charcoal & Face Packs | Swansura",
    "md": "Clay, charcoal, cream and powder face masks explained: which face mask suits oily, dry or sensitive skin, how to use one and how often.",
    "pick": {
        "deyga-char": "deyga-charcoal-detox-face-mask-100g",
        "vil-char": "vilvah-charcoal-face-mask-100ml-activated-charcoal-aloe-vera-tea-tree-hydrosol-for-acne-dark-spots-pore-minimising-natural-skincare-for-oily-acne-prone-skin",
        "rose": "vilvah-wild-rose-face-mask-100ml-natural-brightening-clay-mask-for-even-skin-tone-deep-hydration",
        "mud": "vilvah-milk-mud-mask-50ml-de-tan-brightening-face-mask-with-oat-milk-saffron-kaolin-clay-natural-tan-removal-oil-control-radiant-glow-for-all-skin-types",
        "orange": "deyga-orange-almond-face-pack-powder-100g",
        "matcha": "deyga-spirulina-matcha-face-pack-150g",
        "gold": "24k-gold-hydrating-face-mask",
        "eye": "deyga-under-eye-mask-15g",
        "rosewater": "deyga-pure-rose-water-toner-100-ml",
    },
    "titles": {},
    "shop": ["mud", "rose", "deyga-char", "vil-char", "orange", "matcha", "gold", "eye"],
    "body": """<p>A <strong>face mask</strong> is the easiest way to give your skin ten minutes of extra care. Once or twice a week, it can leave skin feeling fresher, softer or more comfortable, depending on the type you choose. Here are the main kinds of face mask, which suits your skin, and how to use one.</p>
<h2>The main types of face mask</h2>
<ul>
<li><strong>Clay masks</strong> use clays such as kaolin or French pink clay. They dry down on the skin and feel deep-cleansing, which makes them popular with oily and combination skin.</li>
<li><strong>Charcoal masks</strong> add activated charcoal, often with tea tree, for a fresh, clarifying feel.</li>
<li><strong>Powder face packs</strong> are dry blends of plant powders that you mix with water, rose water or aloe gel just before use.</li>
<li><strong>Cream and gel masks</strong> are hydrating and stay soft on the skin, which suits dry and tired-looking skin.</li>
</ul>
<h2>Clay face masks</h2>
<p>[[mud|Vilvah Milk Mud Mask]] ({{mud}}, 50ml) is a creamy <strong>clay face mask</strong>: kaolin clay with oat milk extract, saffron extract and liquorice root extract, made without sulphates, silicones or artificial fragrance, and suitable for all skin types including sensitive skin. [[rose|Vilvah Wild Rose Face Mask]] ({{rose}}, 100ml) keeps things short and simple: aloe vera, French pink clay and rose hydrosol. Vilvah suggests using it two or three times a week.</p>
<h2>Charcoal face masks</h2>
<p>[[deyga-char|Deyga Charcoal Detox Face Mask]] ({{deyga-char}}, 100g) combines activated charcoal with tea tree and jasmine hydrosols, and is made without parabens or artificial fragrance. [[vil-char|Vilvah Charcoal Face Mask]] ({{vil-char}}, 100ml) pairs charcoal with aloe vera and tea tree hydrosol. Both have a fresh, clean feel that many people with oily skin enjoy. See more <a href="/collections/face-mask-for-oily-skin">face masks for oily skin</a>.</p>
<h2>Powder face packs</h2>
<p>Face packs are a long-standing part of Indian skincare: dried herbs, fruit peels and clays ground to a powder and mixed fresh each time.</p>
<ul>
<li>[[orange|Deyga Orange &amp; Almond Face Pack]] ({{orange}}, 100g): sun-dried orange pulp and zest, almond meal and turmeric. The almond meal gives it a gentle, polishing texture.</li>
<li>[[matcha|Deyga Spirulina Matcha Face Pack]] ({{matcha}}, 150g): spirulina, matcha, neem, moringa and aloe vera powder, for a green, earthy mask.</li>
</ul>
<p>Mix a teaspoon with water, or with [[rosewater|Deyga Pure Rose Water Toner]] ({{rosewater}}) for a softer scent, into a smooth paste. You may know the classic Indian clay <strong>multani mitti</strong> (Fuller's earth) used the same way; kaolin and French pink clay are other clays used in face masks.</p>
<h2>Hydrating masks and eye masks</h2>
<p>For skin that feels dry or tired rather than oily, choose a cream or gel mask that stays soft. The [[gold|24K Gold Hydrating Face Mask]] ({{gold}}) combines 24K gold with hyaluronic acid, ceramides, shea butter and centella asiatica, and makes a lovely treat or gift. For the delicate eye area, [[eye|Deyga Under Eye Mask]] ({{eye}}, 15g) is a balm of kalonji, hemp seed, almond, rosehip and carrot seed oils with beeswax, to dab on at night.</p>
<h2>Which face mask suits your skin?</h2>
<ul>
<li><strong>Oily or combination skin:</strong> clay or charcoal masks, on the T-zone or the whole face.</li>
<li><strong>Dry skin:</strong> a hydrating cream mask, or a creamy clay mask such as the Milk Mud Mask, rinsed off before it dries completely.</li>
<li><strong>Sensitive skin:</strong> a short ingredient list without added fragrance, and a patch test first.</li>
<li><strong>Not sure?</strong> Try multi-masking: clay on the oily areas, a hydrating mask on the dry ones.</li>
</ul>
<h2>How to use a face mask</h2>
<ol>
<li><strong>Cleanse first</strong> with a face wash that suits your skin: see <a href="/blogs/journal/face-wash-for-your-skin-type">face wash for your skin type</a>.</li>
<li><strong>Apply an even layer</strong> with clean fingertips or a brush, avoiding the eyes and lips.</li>
<li><strong>Leave it on</strong> for the time on the pack, usually 10 to 15 minutes. Rinse clay masks before they crack and pull, so skin does not feel tight.</li>
<li><strong>Rinse with lukewarm water</strong> and a soft cloth, then pat dry.</li>
<li><strong>Follow with toner and moisturiser</strong> straight away. Aloe vera gel is a light option: read <a href="/blogs/journal/how-to-use-aloe-vera-gel">how to use aloe vera gel</a>.</li>
</ol>
<h2>How often should you use a face mask?</h2>
<p>For most people, clay and charcoal masks <strong>once or twice a week</strong> are plenty; dry or sensitive skin may prefer once a week. Hydrating masks can be used more often. Always follow the directions on the pack.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test</strong> any new mask on your jaw or inner arm first.</li>
<li><strong>Turmeric can leave a faint yellow tint</strong> on skin and towels; rinse well and use an old towel.</li>
<li><strong>Skip masks</strong> on broken, sunburnt or irritated skin. Breakouts or redness that last are worth showing to a pharmacist or your GP.</li>
</ul>
<p>Explore more for <a href="/collections/oily-skin">oily skin</a>, <a href="/collections/dry-skin">dry skin</a> and <a href="/collections/sensitive-skin">sensitive skin</a>, or the full <a href="/collections/natural-skincare">natural skincare</a> range, all dispatched from the UK.</p>""",
    "faq": [
        ["Which face mask is best for oily skin?",
         "Clay or charcoal masks, such as the Vilvah Wild Rose Face Mask, the Vilvah Charcoal Face Mask or the Deyga Charcoal Detox Face Mask, used once or twice a week."],
        ["How often should I use a face mask?",
         "Once or twice a week suits most people for clay and charcoal masks. Dry or sensitive skin may prefer once a week. Hydrating masks can be used more often; always follow the pack."],
        ["How long should I leave a clay mask on?",
         "Usually 10 to 15 minutes, or as the pack says. Rinse it off before it cracks and pulls, so your skin does not feel tight afterwards."],
        ["What is a face pack?",
         "A dry powder of herbs, fruit peels or clays that you mix with water, rose water or aloe gel just before use, such as the Deyga Orange & Almond or Spirulina Matcha face packs."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_face_mask_2026-11-07.jsonl")

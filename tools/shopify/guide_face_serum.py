"""Journal guide 'Face serum guide: vitamin C, hyaluronic acid, niacinamide and how to layer them' (user, 8 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): vitamin c serum 33,100/mo (KD 44),
niacinamide serum 14,800 (KD 38), face serum 9,900 (KD 30), face serum for glowing skin 480 (KD 29).
Facts = product descriptions + stored custom.inci (8 Nov 2026; Highborn MOISTUREBURST has no stored list, so its
ceramides come from its description). Deyga 10% Vitamin C Serum: the stored INCI lists cleansing agents and does not
show the ectoin named in the description, so only ingredients in both (ascorbyl glucoside, citrus extracts) are
used; flagged for the client. Left out (ASA / unprovable): fades dark spots / pigmentation / acne scars, reduces fine
lines / wrinkles, firming, collagen, repairs skin, 'deep' penetration, UV protection. Prices are written into the
text: re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_face_serum.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_face_serum_2026-11-08.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Face serum guide: vitamin C, hyaluronic acid, niacinamide and how to layer them",
    "handle": "face-serum-guide",
    "tag": "Skin Studio",
    "summary": "What a face serum does, how vitamin C, hyaluronic acid, niacinamide, ceramides and face oils differ, and how to layer a serum in your routine.",
    "mt": "Face Serum Guide: Vitamin C, Niacinamide & HA | Swansura",
    "md": "How to choose a face serum: vitamin C, hyaluronic acid, niacinamide, ceramides and face oils explained, plus how to layer serums morning and night.",
    "pick": {
        "vitc": "10-vitamin-c-face-serum-20ml-deygas-natural-brightening-even-skin-tone-dark-spots-suitable-for-all-skin-types",
        "ha": "deyga-2-hyaluronic-acid-serum-20ml",
        "drops": "milk-drops-brightening-serum-40-ml-rice-milk-alpha-arbutin-skin-brightening-treatment-for-dark-spots-uneven-skin-tone",
        "better": "vilvah-better-ageing-serum-20ml-natural-anti-ageing-firming-wrinkle-reducing-face-serum-with-organic-botanicals",
        "ampm": "vilvah-am-pm-serum-kit",
        "burst": "moistureburst-hydrating-glow-ceramide-serum",
        "rose": "deyga-rose-glow-serum-30ml",
        "beauty": "deygas-beautifying-serum-30-ml-natural-glow-even-tone-face-serum-with-organic-oils",
    },
    "titles": {},
    "shop": ["vitc", "ha", "drops", "better", "ampm", "burst", "rose", "beauty"],
    "body": """<p>A <strong>face serum</strong> is a light, concentrated step that sits between cleansing and moisturising. Most are watery or gel-like and carry one or two key ingredients, such as vitamin C, hyaluronic acid or niacinamide. Here is what each of those ingredients is, how to choose a serum, and how to layer it.</p>
<h2>Serum, moisturiser or face oil?</h2>
<ul>
<li><strong>Water-based serums</strong> are thin and quick to absorb. They go on first, after cleansing and toning.</li>
<li><strong>Moisturisers</strong> are creams or lotions that hold moisture in. They go on after your serum.</li>
<li><strong>Oil serums</strong> are blends of plant oils. They can be used last at night, or mixed with a drop of moisturiser.</li>
</ul>
<h2>Vitamin C serum</h2>
<p>Vitamin C is an antioxidant, and one of the most searched serum ingredients. Pure vitamin C (ascorbic acid) can be unstable, so many serums use a gentler, more stable form. [[vitc|Deyga 10% Vitamin C Face Serum]] ({{vitc}}, 20ml) uses ascorbyl glucoside, a stable form of vitamin C, with orange and citrus extracts. Use a <strong>vitamin C serum</strong> in the morning, and always finish with sunscreen. See every <a href="/collections/vitamin-c-serum">vitamin C serum</a>.</p>
<h2>Hyaluronic acid serum</h2>
<p>Hyaluronic acid is a moisture-loving ingredient that holds water in the skin, so it suits every skin type, including oily skin. [[ha|Deyga 2% Hyaluronic Acid Serum]] ({{ha}}, 20ml) combines sodium hyaluronate with glycerine, panthenol, aloe vera and centella asiatica, and is made without fragrance. [[drops|Vilvah Milk Drops Hydrating Serum]] ({{drops}}) pairs aloe vera juice and hyaluronic acid with rice milk extract and alpha arbutin. Apply either to slightly damp skin.</p>
<h2>Niacinamide, bakuchiol and ceramides</h2>
<p>Niacinamide is a form of vitamin B3 that is easy to pair with other ingredients. If you are looking for a <strong>niacinamide serum</strong>, read the full ingredient list: niacinamide often works alongside other ingredients rather than on its own. Bakuchiol is a plant extract often used as a gentle alternative to retinol, and ceramides are lipids that are naturally found in skin. [[better|Vilvah Better Ageing Serum]] ({{better}}, 20ml) brings all three together, with hyaluronic acid, olive squalane, blue pea flower extract and a plant peptide extract. The [[ampm|Vilvah AM PM Serum Kit]] ({{ampm}}) pairs it with Milk Drops: Milk Drops in the morning, Better Ageing at night. For dry, mature skin, [[burst|Highborn London MOISTUREBURST Serum]] ({{burst}}) is a ceramide serum made to layer under moisturiser.</p>
<h2>Face oil serums</h2>
<p>Oil serums suit dry skin and evening routines. [[rose|Deyga Rose Glow Serum]] ({{rose}}, 30ml) blends rose and saffron with coconut, pomegranate seed, rosehip, almond and jojoba oils. [[beauty|Deyga Beautifying Serum]] ({{beauty}}, 30ml) uses moringa, kukui, grapeseed and vetiver oils. Warm two or three drops between your palms and press them into the skin.</p>
<h2>How to choose a face serum</h2>
<ul>
<li><strong>Dry or tight skin:</strong> hyaluronic acid, ceramides or a face oil at night.</li>
<li><strong>Oily skin:</strong> a light hyaluronic acid serum, which can be enough on its own on warm days.</li>
<li><strong>Dull-looking skin:</strong> a vitamin C serum in the morning, with sunscreen.</li>
<li><strong>Sensitive skin:</strong> a short, fragrance-free list, and one new product at a time.</li>
</ul>
<h2>How to layer a serum</h2>
<ol>
<li><strong>Cleanse</strong> with a face wash that suits you: see <a href="/blogs/journal/face-wash-for-your-skin-type">face wash for your skin type</a>.</li>
<li><strong>Apply 2 or 3 drops</strong> of a water-based serum to slightly damp skin and press it in.</li>
<li><strong>Go thinnest to thickest:</strong> serum, then eye cream, then moisturiser. Read <a href="/blogs/journal/moisturiser-for-your-skin-type">moisturiser for your skin type</a> and our <a href="/blogs/journal/under-eye-cream-guide">under eye cream guide</a>.</li>
<li><strong>In the morning, finish with SPF.</strong> Browse every <a href="/collections/sunscreen">sunscreen</a>.</li>
</ol>
<p>You do not need several serums. One in the morning and one at night is plenty for most people.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test</strong> a new serum on your jaw or inner arm for 24 hours.</li>
<li><strong>Introduce one new serum at a time,</strong> so you know what suits your skin.</li>
<li><strong>Store serums</strong> with the cap closed, away from heat and sunlight, and use them within the time shown on the pack.</li>
<li><strong>Stinging, redness or itching that lasts</strong> is worth showing to a pharmacist or your GP.</li>
</ul>
<p>Shop every <a href="/collections/serum">serum</a>, explore <a href="/collections/concern-hydration">hydration</a> and <a href="/collections/concern-glow">glow</a>, or the full <a href="/collections/skincare">skincare</a> range, all dispatched from the UK.</p>""",
    "faq": [
        ["What does a face serum do?",
         "A serum is a light, concentrated step that delivers one or two key ingredients, such as vitamin C, hyaluronic acid or niacinamide. It goes on after cleansing and before moisturiser."],
        ["When should I use a vitamin C serum?",
         "In the morning, after cleansing and before moisturiser, and always followed by sunscreen. The Deyga 10% Vitamin C Face Serum uses ascorbyl glucoside, a stable form of vitamin C."],
        ["Can I use hyaluronic acid and niacinamide together?",
         "Yes, they are easy to pair. The Vilvah Better Ageing Serum contains both, along with bakuchiol and ceramides. Introduce one new product at a time and patch test first."],
        ["Do I put serum before or after moisturiser?",
         "Before. Go from the thinnest texture to the thickest: serum, then eye cream, then moisturiser, and sunscreen last in the morning. Oil serums can go last at night."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_face_serum_2026-11-08.jsonl")

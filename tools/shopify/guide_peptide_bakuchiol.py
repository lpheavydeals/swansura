"""Journal guide 'Peptide serum and bakuchiol serum: what they are and how to use them'
(user, 17-18 Nov 2026: 'Write and Publish All').

Semrush UK (10 Nov): peptide serum 4,400 (KD 22), bakuchiol serum 2,400, ceramide serum 1,000.
Facts = stored descriptions / custom.inci (Admin read 18 Nov): YOUTHBOOST lists Matrixyl 3000, Argireline,
Tripeptide-5, Copper Tripeptide-1; Bakuchiol Youth Elixir lists only bakuchiol; MOISTUREBURST = ceramides; Vilvah Better
Ageing Serum INCI (natural peptide extract, bakuchiol, ceramides, niacinamide, HA). Ingredients explained in general terms
only. Left out (ASA): wrinkles / fine lines / firming / collagen / elasticity / anti-ageing results / 'retinol
alternative' as an effect claim (described as 'often used instead of retinol'). Claim-named products use the name once.
Prices are written into the text: re-run and update if prices change.

Usage: python3 tools/shopify/guide_peptide_bakuchiol.py <allp_map.json>
Output: docs/seo/guide_peptide_bakuchiol_2026-11-18.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Peptide serum and bakuchiol serum: what they are and how to use them",
    "handle": "peptide-bakuchiol-serum-guide",
    "tag": "Skin Studio",
    "summary": "What peptides, bakuchiol and ceramides are, how a peptide or bakuchiol serum fits into a routine, and the serums we stock from Highborn London and Vilvah.",
    "mt": "Peptide Serum and Bakuchiol Serum Explained | Swansura",
    "md": "What peptides, bakuchiol and ceramides are, how to use a peptide or bakuchiol serum, and the serums we stock from Highborn London and Vilvah.",
    "pick": {
        "youthboost": "youthboost-anti-ageing-peptide-serum",
        "bakuchiol": "bakuchiol-youth-elixir",
        "moisture": "moistureburst-hydrating-glow-ceramide-serum",
        "better": "vilvah-better-ageing-serum-20ml-natural-anti-ageing-firming-wrinkle-reducing-face-serum-with-organic-botanicals",
        "betterkit": "vilvah-better-ageing-kit-face-serum-20-ml-ultra-moisturising-cream-50-g-natural-anti-aging-skincare-for-wrinkles-fine-lines-skin-elasticity",
        "nightkit": "vilvah-night-repair-kit-better-ageing-serum-under-eye-cream-targets-fine-lines-wrinkles-dark-circles-natural-bakuchiol-peptides-bamboo-extract-goji-berry",
        "caviar": "caviar-serum-with-24k-gold",
        "imperial": "imperial-moisturiser",
        "spf": "vilvah-skin-finish-sunscreen-spf-50-pa",
    },
    "titles": {},
    "shop": ["youthboost", "bakuchiol", "better", "moisture", "betterkit", "nightkit", "caviar", "imperial"],
    "body": """<p>Peptides and bakuchiol are two of the most searched serum ingredients in the UK, often alongside ceramides. They do different jobs and suit different routines. Here is what each one is, how to use a <strong>peptide serum</strong> or a <strong>bakuchiol serum</strong>, and the serums we stock that contain them.</p>
<h2>What are peptides?</h2>
<p>Peptides are short chains of amino acids, the building blocks of proteins. In skincare they are made in the lab or taken from plants, and they usually appear in serums and creams in small amounts. Different peptides have different trade names, such as Matrixyl or Argireline, so a peptide serum often lists several of them together.</p>
<h3>Peptide serums we stock</h3>
<ul>
<li>[[youthboost|Highborn London YOUTHBOOST Peptide Serum]] ({{youthboost}}) combines four peptide ingredients in one lightweight, vegan-friendly serum: Matrixyl 3000, Argireline, Tripeptide-5 and Copper Tripeptide-1 (a copper peptide).</li>
<li>[[caviar|Caviar Serum with 24K Gold]] ({{caviar}}) is a Swansura Selection serum with tremella polysaccharide, beta-glucan and sodium hyaluronate for hydration, aloe vera and oat kernel extract, amino acids and peptides, carnosine and 24K gold leaf.</li>
</ul>
<h2>What is bakuchiol?</h2>
<p>Bakuchiol is a plant-derived ingredient, taken from the seeds of the babchi plant (Psoralea corylifolia). It is often chosen instead of retinol by people who prefer a plant-based ingredient. It can usually be used morning and night; as with any new serum, patch test first.</p>
<h3>Bakuchiol serums we stock</h3>
<ul>
<li>[[bakuchiol|Highborn London Bakuchiol Youth Elixir]] ({{bakuchiol}}) is a bakuchiol serum made in England for mature and sensitive skin, for morning or evening use.</li>
<li>[[better|Vilvah Better Ageing Serum]] ({{better}}, 20ml) has the longest list: bakuchiol and a natural peptide extract (from sacha inchi seed), with blue pea flower extract, pomegranate seed oil, hyaluronic acid, two ceramides, niacinamide and olive squalane. It brings peptides, bakuchiol and ceramides together in one bottle, in a light texture.</li>
</ul>
<h2>What are ceramides?</h2>
<p>Ceramides are lipids that occur naturally in the outer layer of skin. In skincare they are added to help skin feel smooth and comfortable, and they pair well with peptides or bakuchiol. [[moisture|Highborn London MOISTUREBURST Hydrating Glow Ceramide Serum]] ({{moisture}}, 30ml or 50ml) is a lightweight ceramide serum for dry, dehydrated and mature skin, made to layer under moisturiser.</p>
<h2>How to use a peptide or bakuchiol serum</h2>
<ol>
<li><strong>Cleanse</strong> and, if you use one, apply toner. Our <a href="/blogs/journal/face-wash-for-your-skin-type">face wash guide</a> and <a href="/blogs/journal/toner-for-dry-skin">toner guide</a> help you choose.</li>
<li><strong>Apply 2 or 3 drops</strong> of serum to the face and neck and press it in.</li>
<li><strong>Follow with moisturiser</strong>, such as [[imperial|Highborn London Imperial Moisturiser]] ({{imperial}}). See <a href="/blogs/journal/moisturiser-for-your-skin-type">moisturiser for your skin type</a>.</li>
<li><strong>In the morning, finish with SPF</strong>, for example [[spf|Vilvah Skin Finish Sunscreen SPF 50 PA+++]] ({{spf}}).</li>
</ol>
<p>Use one new serum at a time, so you know what suits your skin. One serum in the morning and one at night is plenty for most people.</p>
<h2>Can you use peptides and bakuchiol together?</h2>
<p>Yes, they are commonly layered, and the Vilvah Better Ageing Serum already contains both. If you use two serums, apply the thinner, watery one first and the richer one after, or use one in the morning and one at night.</p>
<h2>Ready-made routines</h2>
<ul>
<li>The [[betterkit|Vilvah Better Ageing Kit]] ({{betterkit}}) pairs the Better Ageing Serum with the Ultra Moisturising Cream (glycerine, olive squalane, bamboo and goji berry extracts) for an evening routine.</li>
<li>The [[nightkit|Vilvah Night Repair Kit]] ({{nightkit}}) pairs the same serum with an Under Eye Cream made with shea butter, sunflower seed oil, bamboo and goji berry extracts.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test</strong> any new serum on your jaw or inner arm for 24 hours.</li>
<li><strong>Pregnant or breastfeeding?</strong> Check new skincare ingredients with your GP or pharmacist first.</li>
<li><strong>Stinging, redness or itching that lasts</strong> is worth showing to a pharmacist or your GP.</li>
<li>For vitamin C, hyaluronic acid and niacinamide, see our <a href="/blogs/journal/face-serum-guide">face serum guide</a>.</li>
</ul>
<p>Shop every <a href="/collections/serum">serum</a>, or browse <a href="/collections/highborn-london">Highborn London</a> and <a href="/collections/vilvah">Vilvah</a>. Every order ships from the UK, with free UK delivery over £40.</p>""",
    "faq": [
        ["What is a peptide serum?",
         "A serum that contains peptides, short chains of amino acids made in the lab or taken from plants. Highborn London YOUTHBOOST Peptide Serum, for example, combines four peptide ingredients: Matrixyl 3000, Argireline, Tripeptide-5 and Copper Tripeptide-1."],
        ["What is bakuchiol?",
         "Bakuchiol is a plant-derived ingredient from the seeds of the babchi plant. It is often chosen instead of retinol by people who prefer a plant-based ingredient, and it can usually be used morning and night. Patch test any new serum first."],
        ["Can I use peptides and bakuchiol together?",
         "Yes. They are commonly layered, and Vilvah Better Ageing Serum contains both, with ceramides, niacinamide and hyaluronic acid. If you use two serums, apply the thinner one first, or use one in the morning and one at night."],
        ["Where does a peptide serum go in my routine?",
         "After cleansing and toning, before moisturiser. Apply 2 or 3 drops, press them in, then follow with moisturiser and, in the morning, sunscreen."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_peptide_bakuchiol_2026-11-18.jsonl")

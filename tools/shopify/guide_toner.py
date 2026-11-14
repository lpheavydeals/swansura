"""Journal guide 'Toner for dry skin: how to choose one, and which suits oily or sensitive skin' (user, 14 Nov 2026).

Chosen from the client's Search Console export (4-10 Nov 2026, docs/seo/gsc_performance_7d_2026-11-14.xlsx): about 90
impressions at positions 20-50 for toner for dry skin (33, pos 21), face toner for dry skin, hydrating toner uk dry skin,
hydrating / hydration toner for dry skin, toner for dry sensitive skin; only /collections/toner-for-dry-skin showed
(pos 30). Semrush UK: toner for oily skin 1,000/mo (KD 19), toner for dry skin 720 (KD 16), rose water toner 590 (KD 22).
Facts = product descriptions + stored custom.inci (14 Nov 2026; Highborn Diamond Toner has no stored list, so only its
description is used). Left out (ASA / unprovable): reduces acne / blemishes / breakouts, controls oil, minimises pores,
brightens, 'scientifically backed', 'visible results', soothes irritation, balances pH. Glycolic acid explained as a
gentle exfoliating acid with a sunscreen reminder (general guidance, no effect claim). Prices are written into the text:
re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_toner.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_toner_2026-11-14.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Toner for dry skin: how to choose one, and which suits oily or sensitive skin",
    "handle": "toner-for-dry-skin",
    "tag": "Skin Studio",
    "summary": "What a face toner does, how to choose a hydrating toner for dry or sensitive skin, which toner suits oily skin, and how to use one.",
    "mt": "Toner for Dry Skin UK: How to Choose a Face Toner | Swansura",
    "md": "How to choose a hydrating toner for dry or sensitive skin, which toner suits oily skin, and how to use rose water, tea tree and milk toners.",
    "pick": {
        "rose": "deyga-pure-rose-water-toner-100-ml",
        "milk": "vilvah-milk-face-toner-100ml-earth-marine-water-rice-milk-glycolic-acid-pore-minimizer-hydrating-brightening-toner",
        "diamond": "diamond-toner-100ml",
        "tea": "deyga-tea-tree-facial-toner-100ml",
        "crystal": "crystal-cleanser-100ml",
        "oat": "deyga-oat-milk-face-wash-100-ml",
        "ha": "deyga-2-hyaluronic-acid-serum-20ml",
        "deep": "deyga-deep-moisturising-face-cream-30g",
    },
    "titles": {},
    "shop": ["rose", "milk", "diamond", "tea", "crystal", "oat", "ha", "deep"],
    "body": """<p>A <strong>face toner</strong> is the light, watery step between cleansing and moisturising. Old-fashioned toners were often astringent and full of alcohol, which is why many people with dry skin still avoid them. Today most toners are gentle and hydrating instead. Here is how to choose a <strong>toner for dry skin</strong>, which toner suits oily or sensitive skin, and how to use one.</p>
<h2>What does a toner do?</h2>
<p>After cleansing, a toner takes off any last traces of cleanser or tap water and gives skin a first layer of moisture. Skin that is slightly damp takes serum and moisturiser more evenly, so a toner makes the rest of your routine easier to apply. It is an optional step: if your skin feels comfortable without one, you can skip it.</p>
<h2>How to choose a toner for dry skin</h2>
<ul>
<li><strong>Look for hydrating ingredients</strong> such as glycerine, rose water or aloe near the top of the list.</li>
<li><strong>Avoid a high level of alcohol</strong> (listed as alcohol denat. or SD alcohol), which can leave dry skin feeling tight.</li>
<li><strong>Keep it short</strong> if your skin is sensitive too: fewer ingredients make it easier to see what suits you.</li>
<li><strong>Go easy on acids</strong> such as glycolic acid, which gently exfoliate. Dry skin may prefer them two or three times a week rather than daily.</li>
</ul>
<h2>Hydrating toners for dry and sensitive skin</h2>
<p>[[rose|Deyga Pure Rose Water Toner]] ({{rose}}, 100ml) is the simplest toner we stock: just rose (Rosa centifolia) and distilled water, with no alcohol. It is a classic <strong>rose water toner</strong> that you can spritz on or sweep over with a cotton pad, and it also works as a midday refresher over bare skin. It is a good first toner for dry or sensitive skin.</p>
<p>[[diamond|Highborn London Diamond Toner]] ({{diamond}}, 100ml) is a moisturising toner made to follow [[crystal|Highborn London Crystal Cleanser]] ({{crystal}}) as the second step of the Highborn routine. Press it in with your hands or sweep it on with a cotton pad before serum and moisturiser.</p>
<h2>A toner with a gentle acid</h2>
<p>[[milk|Vilvah Milk Face Toner]] ({{milk}}, 100ml) is water and earth marine water with glycerin, a xylitol-based moisturising blend and rice milk extract, plus <strong>glycolic acid</strong>, a gentle exfoliating acid. That makes it a good fit for normal and combination skin that wants a smoother feel. If your skin is dry or sensitive, start with two or three evenings a week, and wear sunscreen during the day while you use it.</p>
<h2>Toner for oily skin</h2>
<p>Oily skin still benefits from a light, hydrating toner: stripping skin with alcohol can leave it feeling tight while it still looks shiny. [[tea|Deyga Tea Tree Facial Toner]] ({{tea}}, 100ml) is three ingredients: tea tree, mulethi (liquorice root) and distilled water, and Deyga makes it without alcohol. Its fresh, herbal feel suits oily and combination skin. Tea tree is an essential oil, so patch test it first if your skin is sensitive. More ideas for <a href="/collections/oily-skin">oily skin</a>.</p>
<h2>Which toner suits you?</h2>
<ul>
<li><strong>Dry skin:</strong> Deyga Pure Rose Water Toner or Highborn London Diamond Toner, every day.</li>
<li><strong>Sensitive skin:</strong> the two-ingredient rose water toner, and a patch test first.</li>
<li><strong>Normal or combination skin:</strong> Vilvah Milk Face Toner, a few times a week to start.</li>
<li><strong>Oily skin:</strong> Deyga Tea Tree Facial Toner.</li>
</ul>
<h2>How to use a toner</h2>
<ol>
<li><strong>Cleanse</strong> with a gentle face wash such as [[oat|Deyga Oat Milk Face Wash]] ({{oat}}), then pat your face almost dry. Our guide to <a href="/blogs/journal/face-wash-for-your-skin-type">face wash for your skin type</a> helps you choose.</li>
<li><strong>Apply the toner</strong> with clean hands or a cotton pad, pressing it over the face and neck. Avoid the eyes.</li>
<li><strong>While skin is still damp,</strong> apply a serum such as [[ha|Deyga 2% Hyaluronic Acid Serum]] ({{ha}}). Read our <a href="/blogs/journal/face-serum-guide">face serum guide</a>.</li>
<li><strong>Finish with moisturiser.</strong> Dry skin likes something richer, such as [[deep|Deyga Deep Moisturising Face Cream]] ({{deep}}); see <a href="/blogs/journal/moisturiser-for-your-skin-type">moisturiser for your skin type</a>.</li>
<li><strong>In the morning, add sunscreen</strong> as the last step.</li>
</ol>
<h2>Good to know</h2>
<ul>
<li><strong>Toner is not a cleanser:</strong> it will not take off make-up or sunscreen on its own.</li>
<li><strong>Rose water also mixes face packs:</strong> see our <a href="/blogs/journal/face-mask-guide">face mask guide</a>.</li>
<li><strong>Patch test</strong> any new toner on your jaw or inner arm for 24 hours.</li>
<li><strong>Stinging, redness or flaking that lasts</strong> is worth showing to a pharmacist or your GP.</li>
</ul>
<p>Shop every <a href="/collections/toner">toner</a>, our <a href="/collections/toner-for-dry-skin">toners for dry skin</a>, and more for <a href="/collections/dry-skin">dry skin</a> and <a href="/collections/sensitive-skin">sensitive skin</a>, all dispatched from the UK.</p>""",
    "faq": [
        ["What is the best toner for dry skin?",
         "A hydrating toner without a high level of alcohol, such as the Deyga Pure Rose Water Toner (rose and distilled water only) or the Highborn London Diamond Toner. Apply it after cleansing, then serum and moisturiser while skin is still damp."],
        ["Do I need a toner if I have dry skin?",
         "It is optional. A hydrating toner gives skin a first layer of moisture and helps serum and moisturiser spread evenly, but if your skin feels comfortable without one, you can skip it."],
        ["Which toner is good for oily skin?",
         "A light toner without alcohol, such as the Deyga Tea Tree Facial Toner, made with tea tree, mulethi and distilled water. Patch test it first if your skin is sensitive."],
        ["Can I use a toner with glycolic acid on dry skin?",
         "Yes, but gently. Start with two or three evenings a week, follow with moisturiser, and wear sunscreen during the day. The Vilvah Milk Face Toner contains glycolic acid."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_toner_2026-11-14.jsonl")

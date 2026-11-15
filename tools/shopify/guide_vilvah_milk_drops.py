"""Journal guide 'Vilvah Milk Drops serum: what is in it, 20ml or 40ml, and is it worth it?' (user, 16 Nov 2026).

Targets brand searches: vilvah milk drops 390/mo (Semrush), vilvah milk drops review, vilvah serum; Search Console
shows Vilvah brand terms at pos 4-12. Facts = stored custom.inci (11 ingredients, identical in every kit), live
variant prices (price per ml computed here). The brand calls it a brightening serum: we describe ingredients only,
no claim on dark spots / pigmentation / tone (ASA). Alpha arbutin described factually, no effect claimed.
Usage: python3 tools/shopify/guide_vilvah_milk_drops.py <allp_map.json>  ->  docs/seo/guide_vilvah_milk_drops_2026-11-16.jsonl
"""
import json
import sys

from brand_guide_lib import vprice, gbp, fill
from journal_lib import build

ALL = json.load(open(sys.argv[1]))
m20, m40 = vprice(ALL, "Vilvah Milk Drops Hydrating Serum", "20 ml"), vprice(ALL, "Vilvah Milk Drops Hydrating Serum", "40 ml")
assert m40 < 2 * m20
V = {"m20": gbp(m20), "m40": gbp(m40), "m20ml": gbp(m20 / 20), "m40ml": gbp(m40 / 40), "two20": gbp(2 * m20)}
T = {"drops": "Vilvah Milk Drops Hydrating Serum", "ageing": "Vilvah Better Ageing Serum", "ampm": "Vilvah AM PM Serum Kit",
     "facekit": "Vilvah Milk Face Kit", "hydkit": "Vilvah Skin Hydration Kit", "toner": "Vilvah Milk Face Toner",
     "cream": "Vilvah Ultra Moisturising Cream", "spf": "Vilvah Skin Finish Sunscreen", "ffwash": "Vilvah Fragrance-Free Cream Face Wash",
     "powder": "Vilvah Milk Powder Face Wash"}
A = {
    "title": "Vilvah Milk Drops serum: what is in it, 20ml or 40ml, and is it worth it?",
    "handle": "vilvah-milk-drops-serum",
    "tag": "Skin Studio",
    "summary": "Vilvah Milk Drops explained: the eleven ingredients, what the milk in the name is, 20ml or 40ml, how to layer it and how it compares with Vilvah Better Ageing Serum.",
    "mt": "Vilvah Milk Drops Serum: Ingredients, Size and Worth It?",
    "md": "Vilvah Milk Drops explained: the eleven ingredients, what the milk is, 20ml vs 40ml, how to use it and how it compares with Better Ageing.",
    "pick": {k: None for k in T}, "titles": T,
    "shop": ["drops", "ageing", "ampm", "facekit", "hydkit", "toner", "cream", "spf"],
    "body": """<p><strong>Quick answer:</strong> <strong>Vilvah Milk Drops</strong> is a light, water-based gel serum with eleven ingredients, led by aloe vera juice, betaine, glycerin and hyaluronic acid, plus alpha arbutin, a brown seaweed extract and rice milk extract. The milk in the name is rice milk extract: there is no dairy in the list. It comes in 20ml (%%m20%%, about %%m20ml%% per ml) and 40ml (%%m40%%, about %%m40ml%% per ml), so the 40ml is the better value if you use it daily.</p>
<h2>What is in Vilvah Milk Drops?</h2>
<p>The full ingredient list, in pack order:</p>
<ol>
<li><strong>Aqua</strong> (water): the base of the gel.</li>
<li><strong>Aloe vera juice:</strong> a watery plant juice that gives a light, cool feel.</li>
<li><strong>Betaine:</strong> from sugar beet, it helps skin feel moisturised.</li>
<li><strong>Glycerin:</strong> a humectant that draws water into the skin's surface.</li>
<li><strong>Xanthan gum:</strong> thickens the serum into a gel.</li>
<li><strong>Hyaluronic acid:</strong> holds water, so skin feels plump and hydrated.</li>
<li><strong>Caprylic/capric triglyceride:</strong> a light, coconut-derived emollient.</li>
<li><strong>Cystoseira tamariscifolia extract:</strong> a brown seaweed extract.</li>
<li><strong>Alpha arbutin:</strong> a stable form of arbutin, a molecule found in plants such as bearberry.</li>
<li><strong>Rice milk extract:</strong> the milk in Milk Drops.</li>
<li><strong>Sodium benzoate and potassium sorbate:</strong> the preservatives.</li>
</ol>
<p>Things the list does not contain: added fragrance, essential oils, alcohol, silicones or oils beyond the light triglyceride, and no animal-derived ingredients.</p>
<h2>Is Milk Drops a brightening serum?</h2>
<p>Vilvah names it a brightening serum, and you will see that word on packs and online. We describe what is in it rather than promise a result: day to day it works as a lightweight, hydrating layer that sits well under moisturiser and makeup. We cannot promise any change to dark spots or skin tone. If a patch of pigmentation is new, changing or worrying you, show it to a pharmacist or your GP, and whatever serum you use, daily sunscreen is the step that matters most.</p>
<h2>20ml or 40ml: which size?</h2>
<ul>
<li><strong>20ml</strong> (%%m20%%): a good size to try it, or for travel.</li>
<li><strong>40ml</strong> (%%m40%%): about %%m40ml%% per ml against %%m20ml%% for the 20ml, and less than two 20ml bottles (%%two20%%).</li>
</ul>
<p>At two to three drops morning and night, either size lasts a good while. Both are the same formula.</p>
<h2>How to use Milk Drops</h2>
<ol>
<li>Cleanse: [[ffwash|Vilvah Fragrance-Free Cream Face Wash]] ({{ffwash}}) or the powder-to-foam [[powder|Milk Powder Face Wash]] ({{powder}}).</li>
<li>Tone if you like: [[toner|Vilvah Milk Face Toner]] ({{toner}}) contains glycolic acid, so start it every other day.</li>
<li>Press two or three drops of Milk Drops over the face and neck.</li>
<li>Moisturise: [[cream|Vilvah Ultra Moisturising Cream]] ({{cream}}) or your usual cream.</li>
<li>In the morning, finish with sunscreen such as [[spf|Vilvah Skin Finish Sunscreen SPF 50 PA+++]] ({{spf}}).</li>
</ol>
<p>Our <a href="/blogs/journal/face-serum-guide">face serum guide</a> explains layering serums, and our <a href="/blogs/journal/toner-for-dry-skin">toner guide</a> and <a href="/blogs/journal/moisturiser-for-your-skin-type">moisturiser guide</a> help you choose the steps around it. Patch test before first use.</p>
<h2>Milk Drops or Vilvah Better Ageing Serum?</h2>
<ul>
<li><strong>[[drops|Milk Drops]]:</strong> water-based gel; aloe, hyaluronic acid, alpha arbutin, rice milk extract. Light, for morning and evening.</li>
<li><strong>[[ageing|Better Ageing Serum]]</strong> ({{ageing}}, 20ml): a silkier serum with bakuchiol, niacinamide, ceramides, hyaluronic acid, pomegranate seed oil and olive squalane. Vilvah suggests it for evenings.</li>
</ul>
<p>Many people use both: Milk Drops in the morning and Better Ageing at night. The [[ampm|Vilvah AM PM Serum Kit]] ({{ampm}}) boxes the two together.</p>
<h2>Kits with Milk Drops</h2>
<ul>
<li>[[facekit|Vilvah Milk Face Kit]] ({{facekit}}): Milk Drops with the Milk Mud Mask, a kaolin clay mask with oat milk and saffron extracts.</li>
<li>[[hydkit|Vilvah Skin Hydration Kit]] ({{hydkit}}): Milk Drops with the Milk Face Toner.</li>
<li>[[ampm|Vilvah AM PM Serum Kit]] ({{ampm}}): Milk Drops with Better Ageing Serum.</li>
</ul>
<h2>Is Vilvah Milk Drops worth it?</h2>
<p>It is worth it if you want a light, fragrance-free hydrating serum with a short list that layers easily under other products. Skip it if you want a rich, oily texture (choose Better Ageing) or a vitamin C serum (see our <a href="/blogs/journal/face-serum-guide">face serum guide</a>). Real customer reviews appear on the product page; we do not publish invented ones.</p>
<h2>Buying Vilvah in the UK</h2>
<p>Swansura is an official UK partner of Vilvah, so every bottle is genuine and ships from UK stock with no import charge on delivery. UK delivery is free over £40. New to the brand? Read <a href="/blogs/journal/vilvah-uk">Vilvah in the UK</a>, compare it with Deyga in <a href="/blogs/journal/deyga-or-vilvah">Deyga or Vilvah</a>, or shop all <a href="/collections/vilvah">Vilvah</a> and every <a href="/collections/serum">face serum</a>.</p>""",
    "faq": [
        ["What is in Vilvah Milk Drops?",
         "Eleven ingredients: water, aloe vera juice, betaine, glycerin, xanthan gum, hyaluronic acid, caprylic/capric triglyceride, a brown seaweed extract, alpha arbutin, rice milk extract and two preservatives. There is no added fragrance."],
        ["Does Vilvah Milk Drops contain milk?",
         "The milk in the name is rice milk extract. There is no dairy or other animal-derived ingredient in its list."],
        ["Should I buy Milk Drops in 20ml or 40ml?",
         "Both are the same formula. The 40ml costs less per ml, so it is the better value for daily use; the 20ml is a good size to try it or to travel with."],
        ["Can I use Milk Drops with Vilvah Better Ageing Serum?",
         "Yes. Many people use Milk Drops in the morning and Better Ageing Serum in the evening; the Vilvah AM PM Serum Kit pairs the two. Patch test before first use."],
    ],
}
A["body"] = fill(A["body"], V)
build(A, ALL, "guide_vilvah_milk_drops_2026-11-16.jsonl")

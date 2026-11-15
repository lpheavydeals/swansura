"""Journal guide 'Deyga Beetroot Lip Balm: stick or pot, what is in it, and is it worth it?' (user, 16 Nov 2026:
brand long-tail guides for Deyga + Vilvah, 'Go with all the four').

Targets brand long-tail searches seen in Search Console (4-10 Nov): deyga beetroot lip balm (19 impr, pos 24),
deyga lip balm, deyga beetroot lip balm ingredients list, and 'is the deyga lip balm stick worth it' style questions.
Facts = stored custom.inci (pot and stick lists are identical) + live prices (price per gram computed here).
Deyga's own blog claims lightening / healing: NOT used (ASA); answered honestly instead.
Usage: python3 tools/shopify/guide_deyga_beetroot.py <allp_map.json>  ->  docs/seo/guide_deyga_beetroot_2026-11-16.jsonl
"""
import json
import sys

from brand_guide_lib import find, vprice, gbp, fill
from journal_lib import build

ALL = json.load(open(sys.argv[1]))
pot1, pot2 = vprice(ALL, "Deyga Beetroot Lip Balm Classic", "1"), vprice(ALL, "Deyga Beetroot Lip Balm Classic", "2")
st1, st2 = vprice(ALL, "Deyga Beetroot Lip Balm Stick", "1"), vprice(ALL, "Deyga Beetroot Lip Balm Stick", "2")
mint = float(ALL[find(ALL, "Deyga Mint Lip Scrub")]["variants"][0]["price"])
combo = float(ALL[find(ALL, "Deyga Soft Lip Combo")]["variants"][0]["price"])
assert combo < mint + pot1
V = {
    "pot1": gbp(pot1), "pot2": gbp(pot2), "st1": gbp(st1), "st2": gbp(st2),
    "potg": gbp(pot1 / 10), "potg2": gbp(pot2 / 20), "stg": gbp(st1 / 5.5), "stg2": gbp(st2 / 11),
    "sep": gbp(mint + pot1), "ratio": f"{(st1 / 5.5) / (pot1 / 10):.1f}".rstrip("0").rstrip("."),
}

A = {
    "title": "Deyga Beetroot Lip Balm: stick or pot, what is in it, and is it worth it?",
    "handle": "deyga-beetroot-lip-balm-stick-or-pot",
    "tag": "Skin Studio",
    "summary": "The Deyga Beetroot Lip Balm in a pot and in a stick: the seven ingredients, the price per gram, what it does and does not do, and which one to buy.",
    "mt": "Deyga Beetroot Lip Balm: Stick or Pot, Is It Worth It?",
    "md": "Deyga Beetroot Lip Balm stick vs pot: the same seven ingredients, the price per gram, what it can and cannot do, and which one to buy in the UK.",
    "pick": {"pot": None, "stick": None, "combo": None, "stickkit": None, "potkit": None, "mint": None, "straw": None,
             "spf": None, "shea": None},
    "titles": {"pot": "Deyga Beetroot Lip Balm Classic", "stick": "Deyga Beetroot Lip Balm Stick", "combo": "Deyga Soft Lip Combo",
               "stickkit": "Deyga Nourished Lips Stick Kit", "potkit": "Deyga Nourished Lip Care Kit", "mint": "Deyga Mint Lip Scrub",
               "straw": "Deyga Strawberry Lip Scrub", "spf": "Vilvah Milk Lip Balm SPF", "shea": "Deyga Shea Butter Lip Balm"},
    "shop": ["pot", "stick", "combo", "stickkit", "potkit", "mint", "straw", "spf"],
    "body": """<p><strong>Quick answer:</strong> the <strong>Deyga Beetroot Lip Balm</strong> comes as a 10g pot (%%pot1%%) and a 5.5g twist-up stick (%%st1%%), and both have exactly the same seven ingredients. The pot works out at about %%potg%% per gram and the stick at about %%stg%% per gram, so the pot is the better value and the stick is the tidier one to carry. It is a moisturising balm with a sheer beetroot tint. It has no SPF, and no lip balm can promise to lighten your lips.</p>
<h2>What is in Deyga Beetroot Lip Balm?</h2>
<p>The full ingredient list, in pack order, is the same for the [[pot|Classic pot]] and the [[stick|stick]]:</p>
<ol>
<li><strong>Beetroot extract</strong> (listed as <em>Beta vulgaris</em>, with its Sanskrit name, paldka): the only colour in the list, which gives the sheer pink tint.</li>
<li><strong>Almond oil:</strong> a light oil that helps the balm glide.</li>
<li><strong>Avocado oil:</strong> a richer oil for a cushioned feel.</li>
<li><strong>Jojoba oil:</strong> a light liquid wax.</li>
<li><strong>Shea butter:</strong> a soft plant butter.</li>
<li><strong>Refined beeswax:</strong> sets the balm and holds it on the lips.</li>
<li><strong>Vitamin E.</strong></li>
</ol>
<p>That is it: no water, no added fragrance and no preservative in the list, because a balm made only of oils, butter and wax does not need one. Because of the beeswax it is not vegan, and the almond oil matters if you have a nut allergy.</p>
<h2>Stick or pot: which should you buy?</h2>
<ul>
<li><strong>Price:</strong> pot %%pot1%% for 10g (about %%potg%%/g); stick %%st1%% for 5.5g (about %%stg%%/g). Gram for gram the stick costs roughly %%ratio%% times as much.</li>
<li><strong>Packs of two:</strong> two pots are %%pot2%% (about %%potg2%%/g) and two sticks %%st2%% (about %%stg2%%/g).</li>
<li><strong>Applying:</strong> the pot needs a fingertip; the stick twists up and goes straight on, which is easier on the move, in gloves or without a mirror.</li>
<li><strong>Colour:</strong> the same tint in both. With the stick, a second swipe builds it; with the pot, dab a little more.</li>
<li><strong>Cold days:</strong> the stick slips into a coat pocket; the pot is handy on a bedside table for a thicker layer at night.</li>
</ul>
<p>Choose the <strong>pot</strong> for value and for night-time use. Choose the <strong>stick</strong> if you will actually carry it and reapply through the day.</p>
<h2>Does beetroot lip balm lighten dark lips?</h2>
<p>You will see that claim online, including on some brand pages. We do not make it. Beetroot extract gives this balm a tint, so lips look pinker while it is on, and the oils and butter leave them feeling soft. That is a cosmetic effect that lasts while you wear it. Lips can darken for many reasons, from sun to smoking to medicines; if your lips change colour, or a patch is new or changing, show it to a pharmacist or your GP.</p>
<h2>Is the Deyga Beetroot Lip Balm worth it?</h2>
<p>It is worth it if you want:</p>
<ul>
<li>a short, readable ingredient list with no added fragrance;</li>
<li>a sheer, natural-looking tint rather than a lipstick colour;</li>
<li>a balm that feels cushioned rather than waxy.</li>
</ul>
<p>Look elsewhere if you need sun protection (it has no SPF), a strong colour, or a vegan balm. For daytime outdoors, pair it with [[spf|Vilvah Milk Lip Balm SPF 30 PA+++]] ({{spf}}). If you would rather skip the tint, [[shea|Deyga Shea Butter Lip Balm]] ({{shea}}) is the plain everyday choice.</p>
<h2>How to use it</h2>
<ol>
<li>Start with clean, dry lips.</li>
<li>Once or twice a week, use a lip scrub first: [[mint|Deyga Mint Lip Scrub]] ({{mint}}) or [[straw|Deyga Strawberry Lip Scrub]] ({{straw}}), both sugar in avocado and almond oils with shea butter.</li>
<li>Apply the balm in a thin layer; add a second for more tint.</li>
<li>Reapply whenever lips feel dry, and add a thicker layer at night.</li>
</ol>
<p>Our <a href="/blogs/journal/how-to-use-lip-scrub">lip scrub guide</a> explains how often to scrub, and our <a href="/blogs/journal/lip-balm-guide">lip balm guide</a> compares SPF, tinted and natural balms from every brand we stock.</p>
<h2>Deyga lip sets with the beetroot balm</h2>
<ul>
<li>[[combo|Deyga Soft Lip Combo]] ({{combo}}): Mint Lip Scrub with the Classic pot, less than the %%sep%% they cost separately.</li>
<li>[[potkit|Deyga Nourished Lip Care Kit]] ({{potkit}}): Strawberry Lip Scrub with the Classic pot.</li>
<li>[[stickkit|Deyga Nourished Lips Stick Kit]] ({{stickkit}}): Strawberry Lip Scrub with the stick.</li>
</ul>
<h2>Buying Deyga in the UK</h2>
<p>Swansura is an official UK partner of Deyga, so every balm is genuine and ships from our UK stock, with no import charge to pay on delivery. UK delivery is free over £40, and the full ingredient list is on every product page. New to the brand? Read <a href="/blogs/journal/deyga-organics-uk">Deyga Organics in the UK</a>, compare the two Indian brands we stock in <a href="/blogs/journal/deyga-or-vilvah">Deyga or Vilvah</a>, or shop all <a href="/collections/deyga">Deyga</a> and every <a href="/collections/lip-balm">lip balm</a>.</p>""",
    "faq": [
        ["Is the Deyga Beetroot Lip Balm stick the same as the pot?",
         "Yes. Both list the same seven ingredients: beetroot extract, almond oil, avocado oil, jojoba oil, shea butter, refined beeswax and vitamin E. The pot holds 10g and the stick 5.5g, so the pot costs less per gram."],
        ["Does Deyga beetroot lip balm lighten dark lips?",
         "We do not claim that. The beetroot extract gives a sheer pink tint while you wear it, and the oils and butter keep lips feeling soft. If your lips change colour or a patch is new or changing, ask a pharmacist or your GP."],
        ["Is Deyga Beetroot Lip Balm vegan?",
         "No. It contains refined beeswax. It also contains almond oil, which matters if you have a nut allergy."],
        ["Does Deyga Beetroot Lip Balm have SPF?",
         "No. For daytime outdoors, pair it with a lip balm that has sun protection, such as Vilvah Milk Lip Balm SPF 30 PA+++."],
    ],
}
A["body"] = fill(A["body"], V)
build(A, ALL, "guide_deyga_beetroot_2026-11-16.jsonl")

"""Journal guide 'Foot cream: how to look after dry, rough feet at home' (user, 15 Nov 2026: 'Write the next 2 Journal guides').

Semrush UK: foot cream 5,400 (KD 22). No foot-care guide yet; all 6 foot products (Vilvah Foot Care Cream, Foot Cream &
Body Lotion Kit; Deyga Foot Butter, Foot Scrub, Foot Soak Powder, Mini Foot Spa Combo) in stock on 15 Nov. Winter angle
(boots, central heating). Facts = stored custom.inci + the descriptions rewritten 8 Nov (Admin read 15 Nov 2026).
Left out (ASA / medical): heals / repairs cracked heels, removes calluses or hard skin, antimicrobial / odour control,
'detox', muscle tension, 'dermatologically tested', 'chemical-free'. Vilvah Home Pedicure Gift Set not used (contents not
stated in our data). Diabetes / poor circulation and painful or bleeding cracks → GP, pharmacist or podiatrist (standard
NHS foot-care advice: do not soak feet for long, dry between the toes). Prices are written into the text: re-run the
generator and update the body if prices change.

Usage: python3 tools/shopify/guide_foot_cream.py <allp_map.json>   (handle -> storefront product)
Output: docs/seo/guide_foot_cream_2026-11-15.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Foot cream: how to look after dry, rough feet at home",
    "handle": "foot-cream-guide",
    "tag": "Skin Studio",
    "summary": "Foot cream, foot butter, scrub or soak: what each one does, a simple at-home pedicure, and how to keep dry feet comfortable through winter.",
    "mt": "Foot Cream for Dry Feet: How to Choose and Use It | Swansura",
    "md": "How to choose a foot cream or foot butter for dry, rough feet, plus a simple at-home pedicure with a foot soak and scrub.",
    "pick": {
        "vcream": "vilvah-foot-care-cream-100ml-moisturising-treatment-for-cracked-heels-dry-calloused-feet-enriched-with-peppermint-argan-kalonji-oils-shea-mango-avocado-butters-unisex-all-skin-types",
        "vkit": "vilvah-foot-cream-body-lotion-kit",
        "dbutter": "foot-butter-40-g-deygas-deep-moisture-butter-for-dry-cracked-heels-rough-feet",
        "dscrub": "deyga-foot-scrub-100-g",
        "dsoak": "deyga-foot-soak-powder-160g",
        "dspa": "deyga-mini-foot-spa-combo",
        "loofah": "deyga-organic-loofah-for-body-exfoliation",
        "rosebutter": "deyga-rose-geranium-body-butter-40g",
    },
    "titles": {},
    "shop": ["vcream", "dbutter", "dscrub", "dsoak", "dspa", "vkit", "rosebutter", "loofah"],
    "body": """<p>Feet have thicker skin than the rest of the body and few oil glands, so they are often the first place to feel dry, especially in winter, when boots, tights and central heating all take their toll. A good <strong>foot cream</strong>, used regularly, keeps heels and soles feeling soft and comfortable. Here is how to choose one, and how to fit it into a simple at-home pedicure.</p>
<h2>Why feet get so dry</h2>
<p>The skin on your heels and soles takes your weight all day. It is naturally thick, and when it dries out it can feel rough and tight. Hot baths, long showers, walking barefoot on hard floors and closed shoes in heated rooms all make it drier. Moisturising little and often works better than an occasional rescue.</p>
<h2>Foot cream or foot butter?</h2>
<ul>
<li><strong>A foot cream</strong> contains water as well as oils and butters, so it sinks in quickly. It suits daily use, morning or night.</li>
<li><strong>A foot butter</strong> or balm has no water: it is a solid blend of oils, butters and wax that sits on the skin for longer. It suits very dry heels and works well at night under cotton socks.</li>
</ul>
<h2>Foot cream: Vilvah Foot Care Cream</h2>
<p>[[vcream|Vilvah Foot Care Cream]] ({{vcream}}, 100ml) is a rich cream with four butters (shea, avocado, mango and cocoa), sunflower, argan and kalonji (black seed) oils, glycerine and a little peppermint oil for a cool, fresh scent. Massage it into clean, dry feet, ideally before bed. It also comes as the [[vkit|Vilvah Foot Cream &amp; Body Lotion Kit]] ({{vkit}}), paired with the Milk Body Lotion (oat milk, ceramide, olive squalane and jojoba oil) for the rest of the body.</p>
<h2>Foot butter: Deyga Foot Butter</h2>
<p>[[dbutter|Deyga Foot Butter]] ({{dbutter}}, 40g) is a short-ingredient balm: virgin coconut oil, olive oil, refined beeswax, vitamin E and vanilla essential oil. Warm a little between your fingers and work it into heels, soles and toes. For a richer finish, put it on at night and slip on cotton socks. It contains beeswax, so it is not vegan.</p>
<p>Already have a favourite body butter? A rich one such as [[rosebutter|Deyga Rose &amp; Geranium Body Butter]] ({{rosebutter}}) works on feet too; our <a href="/blogs/journal/how-to-use-body-butter">body butter guide</a> explains how to use it.</p>
<h2>A simple at-home pedicure</h2>
<ol>
<li><strong>Soak.</strong> Dissolve two spoonfuls of [[dsoak|Deyga Foot Soak Powder]] ({{dsoak}}, 160g) in a bowl of warm water. It blends sea salt and Himalayan pink salt with rose, lemon and peppermint oil. Soak for 10 to 15 minutes, no longer.</li>
<li><strong>Scrub.</strong> Massage [[dscrub|Deyga Foot Scrub]] ({{dscrub}}, 100g) over damp feet in slow circles, focusing on the heels. Granulated sugar gives it a gentle grit, in coconut and almond oils with shea butter. Rinse with warm water. Once or twice a week is enough.</li>
<li><strong>Dry well,</strong> especially between the toes.</li>
<li><strong>Moisturise</strong> with foot cream or foot butter, then put on clean cotton socks if it is bedtime.</li>
</ol>
<p>The [[dspa|Deyga Mini Foot Spa Combo]] ({{dspa}}) puts the soak, the scrub and the foot butter in one box, which also makes an easy Christmas present. A natural [[loofah|Deyga Organic Loofah]] ({{loofah}}) is handy for a quick buff of the heels in the shower. For scrubs for the rest of the body, see our <a href="/blogs/journal/how-to-use-body-scrub">body scrub guide</a>.</p>
<h2>Everyday habits for comfortable feet</h2>
<ul>
<li><strong>Moisturise daily,</strong> ideally after a bath or shower, while skin is still slightly damp.</li>
<li><strong>Keep showers warm, not hot,</strong> and do not leave feet soaking for long.</li>
<li><strong>Wear socks</strong> around the house in winter rather than walking barefoot on cold, hard floors.</li>
<li><strong>Do not use foot cream between the toes;</strong> keep that skin dry.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test</strong> before first use: the cream, butter and soak all contain essential oils, and the scrub contains almond oil.</li>
<li><strong>Do not scrub broken or sore skin.</strong></li>
<li><strong>If you have diabetes or poor circulation,</strong> ask your GP or a podiatrist before soaking or scrubbing your feet.</li>
<li><strong>Painful, deep or bleeding cracks</strong> in the heels, or any change you are unsure about, are worth showing to a pharmacist, your GP or a podiatrist.</li>
</ul>
<p>Shop the full <a href="/collections/bodycare">body care</a> range, every <a href="/collections/body-butter">body butter</a> and <a href="/collections/body-scrub">body scrub</a>, all dispatched from the UK with free UK delivery over £40.</p>""",
    "faq": [
        ["What is the difference between a foot cream and a foot butter?",
         "A foot cream contains water as well as oils and butters, so it sinks in quickly and suits daily use. A foot butter has no water: it is a solid blend of oils, butters and wax that stays on the skin for longer, which suits very dry heels and night-time use under cotton socks."],
        ["How often should I use foot cream?",
         "Once or twice a day, ideally after a bath or shower and before bed. Moisturising little and often keeps feet more comfortable than an occasional rich treatment."],
        ["How often should I scrub my feet?",
         "Once or twice a week is enough. Scrub damp feet gently, focusing on the heels, rinse, dry well and follow with foot cream or foot butter. Do not scrub broken or sore skin."],
        ["Should I wear socks after foot cream?",
         "At night, yes: a layer of foot cream or foot butter under clean cotton socks helps it stay on your feet rather than the sheets. During the day, let the cream sink in for a few minutes before putting on socks and shoes."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_foot_cream_2026-11-15.jsonl")

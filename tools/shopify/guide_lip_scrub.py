"""Journal guide 'Lip scrub: how to use one, and the lip balm to follow it' (user, 6 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): lip scrub 5,400/mo (KD 16),
spf lip balm 4,400 (KD 30), tinted lip balm 2,900 (KD 21), natural lip balm 1,300 (KD 10), lip balm for dry
lips 1,000. Facts come from product descriptions and our INCI data (docs/data/deyga_inci_2026-10-23.json,
docs/data/vilvah_inci_2026-10-22.json). Description claims (reduces pigmentation, lightening, heals cuts,
prevents ageing) are NOT repeated (ASA); the Vilvah Lip Lightening Kit is left out because its name is a claim.
Prices are written into the text: re-run and update the article body if prices change.

Usage: python3 tools/shopify/guide_lip_scrub.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_lip_scrub_2026-11-06.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Lip scrub: how to use one, and the lip balm to follow it",
    "handle": "how-to-use-lip-scrub",
    "tag": "Skin Studio",
    "summary": "How to use a lip scrub, how often, and which lip balm to follow it with: natural, tinted or SPF.",
    "mt": "Lip Scrub Guide: How to Use It & Which Lip Balm | Swansura",
    "md": "How to use a lip scrub, how often to scrub, and which lip balm to follow it with: natural, tinted and SPF lip balms from Deyga and Vilvah.",
    "pick": {
        "mint": "deyga-mint-lip-scrub-16g", "straw": None, "vscrub": None,
        "beet": None, "stick": None, "vanilla": "deyga-natural-vanilla-lip-balm-8g",
        "grape": "vilvah-grape-fruit-lip-balm-10g", "spf": None, "tint-kit": "vilvah-tinted-lip-balm-kit",
        "combo": "deyga-soft-lip-combo", "nourish": None, "vkit": None,
        "hb": "superior-lip-butter-15ml",
    },
    "titles": {
        "straw": "Deyga Strawberry Lip Scrub", "vscrub": "Vilvah Natural Lip Scrub",
        "beet": "Deyga Beetroot Lip Balm Classic", "stick": "Deyga Beetroot Lip Balm Stick",
        "spf": "Vilvah Milk Lip Balm SPF 30", "nourish": "Deyga Nourished Lip Care Kit",
        "vkit": "Vilvah Lip Nourishing Kit",
    },
    "shop": ["mint", "straw", "vscrub", "beet", "spf", "combo", "vkit", "hb"],
    "body": """<p>Dry, flaky lips are one of the first things cold weather, central heating and long days in a mask or scarf leave behind. A <strong>lip scrub</strong> lifts the loose, flaky bits so your lips feel smooth again, and a good lip balm straight after keeps them soft. Here is how to use a lip scrub, how often, and which lip balm to pair with it.</p>
<h2>What is a lip scrub?</h2>
<p>A lip scrub is a small pot of fine sugar held in butters and oils. The sugar does the gentle polishing; the butters and oils leave a soft, cushioned layer behind. Ours are short, simple blends:</p>
<ul>
<li>[[mint|Deyga Mint Lip Scrub]] ({{mint}}, 16g): avocado and almond oils, beeswax, shea butter, granulated sugar, mint essential oil and vitamin E. Fresh and cooling to use.</li>
<li>[[straw|Deyga Strawberry Lip Scrub]] ({{straw}}, 16g): the same base with strawberry essential oil for a fruity scent, free from artificial colours, alcohol and parabens.</li>
<li>[[vscrub|Vilvah Natural Lip Scrub]] ({{vscrub}}, 10g): organic shea butter, avocado and almond oils, organic sugar, beeswax, and lemon and spearmint essential oils, free from alcohol and silicones. The small pot is easy to keep in a handbag.</li>
</ul>
<h2>How to use a lip scrub</h2>
<ol>
<li><strong>Start with clean, dry lips.</strong> Take off lipstick or balm first.</li>
<li><strong>Take a small amount,</strong> about the size of a grain of rice, on a clean fingertip.</li>
<li><strong>Massage in small circles</strong> for 30 seconds to a minute. Use light pressure: let the sugar do the work.</li>
<li><strong>Wipe or rinse it off</strong> with a soft, damp cloth or lukewarm water. Some people simply lick the sugar away.</li>
<li><strong>Apply a lip balm straight away,</strong> while lips are soft and smooth.</li>
</ol>
<h2>How often should you use a lip scrub?</h2>
<p>For most people, <strong>two or three times a week</strong> is plenty. Lip skin is thin, so scrubbing every day can leave it feeling sore. In winter, or if your lips are very dry, use it when they feel flaky rather than on a fixed schedule. Before a matte or long-wear lipstick, a quick scrub helps the colour go on more evenly.</p>
<h2>The lip balm to follow it</h2>
<p>A scrub without a balm is only half the job. Choose the balm by what you want from it.</p>
<h3>A natural lip balm for everyday</h3>
<p>[[beet|Deyga Beetroot Lip Balm Classic]] ({{beet}}, 10g) blends beetroot extract with almond, avocado and jojoba oils, shea butter, beeswax and vitamin E. The beetroot gives lips a soft, natural flush. [[vanilla|Deyga Natural Lip Balm]] ({{vanilla}}, 8g) is the plain choice: almond and jojoba oils, beeswax, shea butter and vanilla extract, in a light, non-greasy texture that sits well under lipstick.</p>
<h3>A tinted lip balm</h3>
<p>If you like a hint of colour, the [[stick|Deyga Beetroot Lip Balm Stick]] ({{stick}}, 5.5g) has the same beetroot blend in an easy tube. [[grape|Vilvah Grape Fruit Lip Balm]] ({{grape}}) adds red iron oxide for a tint, with organic shea butter, avocado and almond oils and grapefruit essential oil. The [[tint-kit|Vilvah Tinted Lip Balm Kit]] ({{tint-kit}}) brings two tinted balms together.</p>
<h3>An SPF lip balm for daytime</h3>
<p>Lips burn too, and most lip balms have no sun protection. [[spf|Vilvah Milk Lip Balm SPF 30 PA+++]] ({{spf}}) uses mineral filters, titanium dioxide and zinc oxide, with soy milk, soy butter, shea butter and kokum butter. Wear it outdoors and reapply as the pack directs, especially after eating or drinking.</p>
<h3>A rich lip butter for night</h3>
<p>[[hb|Highborn London Superior Lip Butter]] ({{hb}}, 15ml) is a richer, softer texture to smooth on before bed after a scrub.</p>
<h2>Lip scrub and balm sets</h2>
<p>Sets pair a scrub with its balm, and make a neat small gift or stocking filler:</p>
<ul>
<li>[[combo|Deyga Soft Lip Combo]] ({{combo}}): Mint Lip Scrub and Beetroot Lip Balm.</li>
<li>[[nourish|Deyga Nourished Lip Care Kit]] ({{nourish}}): Strawberry Lip Scrub and Beetroot Lip Balm.</li>
<li>[[vkit|Vilvah Lip Nourishing Kit]] ({{vkit}}): Vilvah Lip Scrub and Grapefruit Lip Balm.</li>
</ul>
<p>For more small gifts, see our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a>.</p>
<h2>Part of a wider routine</h2>
<p>Lips are the driest skin of all, but the same idea works for the body: polish, then moisturise. Read <a href="/blogs/journal/how-to-use-body-scrub">how to choose a body scrub</a> and <a href="/blogs/journal/how-to-use-body-butter">how to use a body butter</a>. Not sure which natural brand to start with? Compare them in <a href="/blogs/journal/deyga-or-vilvah">Deyga or Vilvah</a>.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Patch test first,</strong> especially with scrubs and balms that contain essential oils such as mint, lemon or grapefruit.</li>
<li><strong>Skip the scrub</strong> on cracked, cut, sore or sunburnt lips, or during a cold sore. Use only a balm until they have settled.</li>
<li><strong>Lips that stay sore,</strong> split or swollen for a long time are worth showing to a pharmacist or your GP.</li>
<li><strong>Keep pots clean:</strong> use a clean fingertip and close the lid after use.</li>
</ul>
<p>Shop all <a href="/collections/lip-scrub">lip scrubs</a>, every <a href="/collections/lip-balm">lip balm</a>, and the full <a href="/collections/concern-lips">lip care</a> edit, all dispatched from the UK.</p>""",
    "faq": [
        ["How often should I use a lip scrub?",
         "Two or three times a week suits most people. Lip skin is thin, so daily scrubbing can leave it sore. Use it when your lips feel flaky, and always follow with a lip balm."],
        ["Should I use lip balm after a lip scrub?",
         "Yes. A scrub lifts dry, flaky skin; a balm straight afterwards keeps lips soft. Choose a natural balm for everyday, a tinted balm for colour, or an SPF lip balm for daytime outdoors."],
        ["Can I use a lip scrub before lipstick?",
         "Yes. A gentle scrub a few minutes before lipstick helps the colour go on more evenly, especially matte or long-wear shades. Apply a thin layer of balm first and blot it before the lipstick."],
        ["When should I not use a lip scrub?",
         "Skip it on cracked, cut, sore or sunburnt lips and during a cold sore. Use only a balm until they have settled, and speak to a pharmacist if they stay sore."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_lip_scrub_2026-11-06.jsonl")

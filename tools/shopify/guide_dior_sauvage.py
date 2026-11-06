"""Journal guide 'Dior Sauvage EDT vs EDP vs Parfum: which one to choose' (user, 6 Nov 2026).

Target keywords (Semrush UK, seo/Swansura_Keyword_Research.xlsx 'Semrush Data'): dior sauvage parfum 5,400/mo
(KD 35), dior sauvage eau de parfum 4,400 (KD 28), dior sauvage price 590, dior sauvage extrait 210; head term
dior sauvage 60,500 (KD 38). On 6 Nov 2026 the store has only the Sauvage EDP 100ml + 10ml gift set and the Dior
Iconics mini set (holds Sauvage EDT 5ml); there is no standalone EDT or Parfum, so the article says so and does
not list notes for versions we have no product data for. Concentration ranges are described as typical (same
wording as the 'extrait vs eau de parfum' article). Other in-stock men's scents are shown as fresh / aromatic
picks, never as 'dupes' or 'smells like Sauvage'. No 'long-lasting' promises. Prices are written into the text:
re-run if prices change.

Usage: python3 tools/shopify/guide_dior_sauvage.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_dior_sauvage_2026-11-06.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Dior Sauvage EDT vs EDP vs Parfum: which one to choose",
    "handle": "dior-sauvage-edt-vs-edp-vs-parfum",
    "tag": "Scent Studio",
    "summary": "Dior Sauvage eau de toilette, eau de parfum and parfum compared: what the labels mean, the EDP notes, and how to choose.",
    "mt": "Dior Sauvage EDT vs EDP vs Parfum: Which to Pick | Swansura",
    "md": "Dior Sauvage eau de toilette, eau de parfum and parfum compared: what each label means, the Sauvage EDP notes, gift sets and how to choose yours.",
    "pick": {
        "set": "dior-sauvage-eau-de-parfum-100ml-10ml-men-s-gift-set",
        "iconics": "dior-iconics-mini-perfume-discovery-set-5-x-5ml",
        "ck-edt": "calvin-klein-eternity-for-men-eau-de-toilette-100ml-men-s-fresh-aromatic-fragrance",
        "defy": "calvin-klein-defy-parfum-men-s-warm-woody-fragrance",
        "carbon": None, "aventure": "al-haramain-l-aventure-eau-de-parfum-100ml-men-s-fresh-woody-fragrance",
        "hunter": "armaf-hunter-eau-de-parfum-100ml-men-s-fresh-woody-aromatic-fragrance",
        "black": None,
    },
    "titles": {"carbon": "Al Haramain Amber Oud Carbon Edition", "black": "Al Haramain Amber Oud Black Edition"},
    "shop": ["set", "iconics", "ck-edt", "defy", "carbon", "black", "aventure", "hunter"],
    "body": """<p><strong>Dior Sauvage</strong> is one of the best-known men's fragrances in the UK, and it comes in more than one strength. The eau de toilette, the eau de parfum and the parfum share a name and a bottle shape, but they are not the same scent at different volumes. Here is what each label means, what is in the <strong>Dior Sauvage eau de parfum</strong>, and how to choose.</p>
<h2>EDT, EDP and Parfum: what the labels mean</h2>
<p>The label tells you how much perfume oil is in the bottle. The ranges below are typical; every house sets its own.</p>
<ul>
<li><strong>Eau de toilette (EDT):</strong> typically around 5–15% perfume oil. Lighter, with a bright opening that suits daytime and warm weather.</li>
<li><strong>Eau de parfum (EDP):</strong> usually around 15–20%. Fuller and rounder, and the most popular strength today.</li>
<li><strong>Parfum (also called extrait):</strong> the most concentrated form, typically around 20–40%. Richer and closer to the skin, so a little goes further.</li>
</ul>
<p>A higher concentration does not simply mean "stronger". Perfumers often rework the formula for each strength, so the notes, the balance and the feel on skin change too. We explain this in more detail in <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum: what the label means</a>.</p>
<h2>Dior Sauvage eau de parfum: the notes</h2>
<p>Sauvage EDP is an amber fougère inspired by the desert at sundown, mixing fresh, spicy and warm notes:</p>
<ul>
<li><strong>Top:</strong> Calabrian bergamot and Sichuan pepper.</li>
<li><strong>Heart:</strong> star anise, nutmeg and lavender.</li>
<li><strong>Base:</strong> Papua New Guinea vanilla and ambroxan.</li>
</ul>
<p>Compared with an eau de toilette, an EDP like this tends to feel softer and warmer, with the vanilla and amber showing more as it settles. It works year-round, and especially in the evening and in cooler months.</p>
<h2>Sauvage eau de toilette</h2>
<p>The EDT is the lighter, brighter version and the one many people try first. You can try it in miniature in the [[iconics|Dior Iconics Mini Perfume Discovery Set]] ({{iconics}}), which holds five 5ml Dior scents: Sauvage Eau de Toilette, J'adore Eau de Parfum, Hypnotic Poison Eau de Toilette, and Miss Dior in both Eau de Parfum and Eau de Toilette. It is a good way to compare styles before choosing a full bottle, and a generous gift.</p>
<h2>Sauvage Parfum</h2>
<p><strong>Dior Sauvage Parfum</strong> is the most concentrated of the three and is usually described as the richest and warmest. We do not carry the Parfum at present, so if you have your heart set on it, <a href="/pages/contact">get in touch</a> and we will let you know if that changes.</p>
<h2>Which Dior Sauvage should you choose?</h2>
<ul>
<li><strong>Choose the EDT</strong> if you want something fresh for daytime, the office or summer.</li>
<li><strong>Choose the EDP</strong> if you want a softer, warmer version for every day and evenings.</li>
<li><strong>Choose the Parfum</strong> if you prefer a rich scent that sits close to the skin.</li>
<li><strong>Not sure?</strong> Try a mini first, then buy the full size.</li>
</ul>
<h2>The Dior Sauvage gift set</h2>
<p>The [[set|Dior Sauvage Eau de Parfum 100ml + 10ml Men's Gift Set]] ({{set}}) pairs a full 100ml bottle with a 10ml travel spray, so there is one for home and one for the gym bag or a trip. See more gift ideas in our <a href="/blogs/journal/christmas-gift-guide">Christmas gift guide</a>.</p>
<h2>More fresh, aromatic men's fragrances</h2>
<p>If you like Sauvage's mix of citrus, pepper and lavender, these share some of those notes, each in its own style:</p>
<ul>
<li>[[ck-edt|Calvin Klein Eternity for Men Eau de Toilette]] ({{ck-edt}}, 100ml): mandarin, lavender, bergamot and lemon, then sage, juniper and basil over sandalwood and vetiver.</li>
<li>[[defy|Calvin Klein Defy Parfum]] ({{defy}}): mandarin and pink pepper, lavender and a suede accord, then vetiver, amber and woods.</li>
<li>[[carbon|Al Haramain Amber Oud Carbon Edition]] ({{carbon}}): lavender, rosemary and bergamot, then sage, cedarwood and geranium over vetiver and amber.</li>
<li>[[black|Al Haramain Amber Oud Black Edition]] ({{black}}): cardamom, grapefruit and lavender with leather, amber and benzoin.</li>
<li>[[aventure|Al Haramain L'Aventure]] ({{aventure}}): lemon, bergamot and elemi over patchouli, amber and musk.</li>
<li>[[hunter|Armaf Hunter]] ({{hunter}}): grapefruit, mandarin, rosemary and cardamom over cedarwood, vetiver and musk.</li>
</ul>
<h2>How to wear it</h2>
<ul>
<li><strong>Two to four sprays</strong> of an EDT, one to three of an EDP, and one or two of a parfum is a good starting point.</li>
<li><strong>Spray on moisturised skin</strong> at the neck and chest. There is no need to rub it in.</li>
<li><strong>Keep the bottle cool</strong> and out of direct sunlight, not on a bathroom windowsill.</li>
</ul>
<p>Shop all <a href="/collections/dior">Dior</a> and every <a href="/collections/perfume-for-men">perfume for men</a>, 100% authentic and dispatched from the UK.</p>""",
    "faq": [
        ["What is the difference between Dior Sauvage EDT, EDP and Parfum?",
         "The amount of perfume oil and the formula. The eau de toilette is the lightest and freshest, the eau de parfum is softer and warmer with more vanilla and amber, and the parfum is the most concentrated and richest."],
        ["What are the notes in Dior Sauvage eau de parfum?",
         "Calabrian bergamot and Sichuan pepper at the top; star anise, nutmeg and lavender in the heart; and Papua New Guinea vanilla and ambroxan in the base."],
        ["Is Dior Sauvage EDP stronger than the EDT?",
         "It has a higher concentration of perfume oil, typically around 15–20% against 5–15% for an eau de toilette. It also smells different: softer and warmer, rather than just a louder version of the EDT."],
        ["Is there a Dior Sauvage gift set?",
         "Yes. The Dior Sauvage Eau de Parfum gift set pairs a 100ml bottle with a 10ml travel spray. The Dior Iconics mini set includes Sauvage Eau de Toilette 5ml among five Dior scents."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_dior_sauvage_2026-11-06.jsonl")

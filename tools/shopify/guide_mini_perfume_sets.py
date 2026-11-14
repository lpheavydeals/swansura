"""Journal guide 'Mini perfume sets: Jimmy Choo, Dior and the miniature sets worth giving' (user, 14 Nov 2026).

Chosen from the client's Search Console export (4-10 Nov 2026, docs/seo/gsc_performance_7d_2026-11-14.xlsx): jimmy choo
mini set (10 impressions, pos 30), miniature jimmy choo perfume (9, pos 21), mini perfume jimmy choo (8, pos 22), jimmy
choo mini perfume (8, pos 29), dior mini perfume set (14, pos 32), miniature perfume sets for her (1 click, pos 4).
Semrush UK has only brand-set terms (chloe / dkny / gucci miniature set 30/mo each). Differs from the published
best-perfume-gift-sets-uk-2026 guide (which only names the mini sets) by listing what is inside each set with its notes;
it links that guide and the stocking fillers guide instead of repeating them. Facts = the products' stored descriptions
(14 Nov 2026; the Dior Iconics and Hermès sets have no notes stored, so only the scent names are given). Left out:
longevity, 'luxury' superlatives, 'dupe', price-per-ml claims. Prices are written into the text: re-run the generator
and update the body if prices change.

Usage: python3 tools/shopify/guide_mini_perfume_sets.py <allp.json>   (handle -> storefront product, /collections/all)
Output: docs/seo/guide_mini_perfume_sets_2026-11-14.jsonl
"""
import json
import sys

from journal_lib import build

A = {
    "title": "Mini perfume sets: Jimmy Choo, Dior and the miniature sets worth giving",
    "handle": "mini-perfume-sets-guide",
    "tag": "Gift guide",
    "summary": "What is inside the Jimmy Choo, Dior, Marc Jacobs, Chloé, Gucci and Paco Rabanne mini perfume sets, plus single minis under £20.",
    "mt": "Mini Perfume Sets UK: Jimmy Choo, Dior & More | Swansura",
    "md": "What is inside the Jimmy Choo, Dior, Marc Jacobs, Chloé, Gucci and Paco Rabanne mini perfume sets, with notes, sizes and prices, plus minis under £20.",
    "pick": {
        "jc": "jimmy-choo-women-s-miniature-fragrance-gift-set-5x4-5ml-5-piece-perfume-collection",
        "jcf": "jimmy-choo-i-want-choo-forever-eau-de-parfum-4-5ml-miniature-women-s-floral-gourmand-fragrance",
        "dior": "dior-iconics-mini-perfume-discovery-set-5-x-5ml",
        "mj": "marc-jacobs-women-s-miniature-fragrance-gift-set-2025-daisy-daisy-eau-so-fresh-perfect-daisy-wild",
        "chloe": "chloe-women-s-miniature-perfume-set-4x5ml-nomade-edt-rose-tangerine-edt-chloe-edp-nomade-edp",
        "flora": "gucci-flora-gorgeous-miniature-perfume-set-3x5ml-gardenia-magnolia-orchid",
        "guerlain": "guerlain-mon-guerlain-miniature-perfume-gift-set-4x5ml-women-s-fragrance-collection",
        "dkny": "product-title-dkny-women-s-miniature-eau-de-parfum-set-4x7ml-be-delicious-golden-delicious-be-extra-delicious-be-100-delicious",
        "ck": "calvin-klein-women-s-miniature-fragrance-set-4x15ml-obsession-eternity-ck-one",
        "pacow": "paco-rabanne-womens-miniature-set-lady-million-olympea-fame-5ml-6ml-4ml-4ml",
        "pacom3": "paco-rabanne-mens-miniature-eau-de-toilette-set-1-million-invictus-phantom-3-x-4ml",
        "pacom4": "paco-rabanne-mens-miniature-set-phantom-invictus-1-million-elixir-1-million-4-x-5ml",
        "dgm": "dolce-gabbana-men-s-miniature-fragrance-set-devotion-k-edt-k-edp-the-one-light-blue-pour-homme",
        "hermes": "hermes-miniature-edt-gift-set-4-x-7-5ml-unisex-fragrances",
        "bloom": "gucci-bloom-eau-de-toilette-10ml-miniature-women-s-floral-perfume",
        "perfect": "marc-jacobs-perfect-eau-de-toilette-10ml-miniature-women-s-floral-fragrance",
        "defy": "calvin-klein-defy-parfum-10ml-miniature-men-s-warm-woody-fragrance",
        "eros": "versace-eros-pour-femme-eau-de-toilette-miniature-5ml",
        "dylan": "versace-dylan-blue-pour-homme-eau-de-toilette-miniature-5ml",
    },
    "titles": {},
    "shop": ["jc", "dior", "mj", "chloe", "flora", "pacow", "pacom4", "jcf"],
    "body": """<p>A <strong>mini perfume set</strong> is a box of small bottles, usually 4ml to 15ml each, from one perfume house. It lets someone try several scents before buying a full bottle, keep a favourite in their bag, or simply enjoy a little collection. Here is what is inside the miniature sets we stock, starting with Jimmy Choo and Dior.</p>
<h2>Why choose a mini perfume set?</h2>
<ul>
<li><strong>To try before buying:</strong> wear each scent for a day or two and see which one you reach for.</li>
<li><strong>For travel and handbags:</strong> small bottles take up little room.</li>
<li><strong>As a gift when you are not sure of their taste:</strong> several scents from a house they like is a safer bet than one full bottle.</li>
</ul>
<p>Sizes vary from set to set, so check the millilitres as well as the number of bottles.</p>
<h2>Jimmy Choo mini perfume set</h2>
<p>The [[jc|Jimmy Choo Women’s Miniature Fragrance Gift Set]] ({{jc}}) holds five 4.5ml eau de parfums, 22.5ml in all:</p>
<ul>
<li><strong>I Want Choo:</strong> peach and mandarin, red spider lily and jasmine, vanilla.</li>
<li><strong>Jimmy Choo Eau de Parfum:</strong> pear, mandarin and green notes, orchid, toffee and patchouli.</li>
<li><strong>I Want Choo Forever:</strong> rose and bitter almond, cherry, jasmine and vetiver, vanilla, tonka bean, oakmoss and amber.</li>
<li><strong>Rose Passion:</strong> frangipani and jasmine, coconut milk and orchid, vanilla and sandalwood.</li>
<li><strong>I Want Choo Le Parfum:</strong> blackberry, pear and gardenia, jasmine, patchouli and ambrette, praline, sandalwood and moss.</li>
</ul>
<p>If you already know you love I Want Choo Forever, it also comes as a single [[jcf|4.5ml miniature]] ({{jcf}}). See every <a href="/collections/jimmy-choo">Jimmy Choo</a> fragrance.</p>
<h2>Dior mini perfume set</h2>
<p>The [[dior|Dior Iconics Mini Perfume Discovery Set]] ({{dior}}) has five 5ml minis for women and men: J’adore Eau de Parfum, Miss Dior Eau de Parfum, Miss Dior Eau de Toilette, Hypnotic Poison Eau de Toilette and Sauvage Eau de Toilette. It is the set to choose for someone who loves Dior but whose favourite you do not know. Not sure which Sauvage they wear? Read <a href="/blogs/journal/dior-sauvage-edt-vs-edp-vs-parfum">Sauvage EDT vs EDP vs Parfum</a>. More from <a href="/collections/dior">Dior</a>.</p>
<h2>More miniature perfume sets for her</h2>
<ul>
<li>[[mj|Marc Jacobs Miniature Gift Set 2025]] ({{mj}}): Daisy, Daisy Eau So Fresh and Daisy Wild (4ml each) and Perfect (5ml). Fresh fruity florals, plus Perfect’s rhubarb, narcissus and almond milk.</li>
<li>[[chloe|Chloé Miniature Perfume Set]] ({{chloe}}): four 5ml bottles, Chloé Eau de Parfum, Nomade Eau de Parfum and Eau de Toilette, and Rose Tangerine.</li>
<li>[[flora|Gucci Flora Gorgeous Miniature Set]] ({{flora}}): three 5ml bottles, Gorgeous Gardenia (pear blossom, gardenia, brown sugar), Gorgeous Magnolia (dewberries, coconut, magnolia) and Gorgeous Orchid (vanilla, vanilla orchid).</li>
<li>[[guerlain|Mon Guerlain Miniature Set]] ({{guerlain}}): four 5ml bottles, two Mon Guerlain Eau de Parfum, Mon Guerlain Florale and Bloom of Rose, all built on lavender and vanilla.</li>
<li>[[dkny|DKNY Delicious Miniature Set]] ({{dkny}}): four 7ml eau de parfums, Be Delicious, Golden Delicious, Be Extra Delicious and Be 100% Delicious.</li>
<li>[[pacow|Paco Rabanne Women’s Miniature Set]] ({{pacow}}): Lady Million, Olympéa, and Fame in two strengths.</li>
<li>[[ck|Calvin Klein Women’s Miniature Set]] ({{ck}}): bigger 15ml bottles, two Obsession, one Eternity and one CK One.</li>
</ul>
<h2>Mini aftershave sets for him</h2>
<ul>
<li>[[pacom4|Paco Rabanne Men’s Miniature Set]] ({{pacom4}}): four 5ml bottles, Phantom, Invictus, 1 Million and 1 Million Elixir.</li>
<li>[[pacom3|Paco Rabanne Men’s Eau de Toilette Set]] ({{pacom3}}): 1 Million, Invictus and Phantom in 4ml bottles, a smaller and cheaper way to try them.</li>
<li>[[dgm|Dolce &amp; Gabbana Men’s Miniature Set]] ({{dgm}}): Devotion, K Eau de Toilette, K Eau de Parfum, The One and Light Blue Pour Homme.</li>
</ul>
<p>For a set anyone can wear, the [[hermes|Hermès Miniature Gift Set]] ({{hermes}}) holds four 7.5ml unisex scents from the Jardins collection: Un Jardin à Cythère, Un Jardin sur le Nil, Le Jardin de Monsieur Li and Un Jardin sur la Lagune.</p>
<h2>Single minis under £20</h2>
<p>When one scent is enough, a single miniature makes an easy stocking filler: [[bloom|Gucci Bloom Eau de Toilette 10ml]] ({{bloom}}), [[perfect|Marc Jacobs Perfect Eau de Toilette 10ml]] ({{perfect}}), [[eros|Versace Eros Pour Femme 5ml]] ({{eros}}), [[defy|Calvin Klein Defy Parfum 10ml]] ({{defy}}) and [[dylan|Versace Dylan Blue Pour Homme 5ml]] ({{dylan}}). Browse every <a href="/collections/travel-size-minis">travel-size mini</a>.</p>
<h2>Good to know</h2>
<ul>
<li><strong>Eau de parfum or eau de toilette?</strong> Many sets mix the two; read <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> for what the labels mean.</li>
<li><strong>Want a full bottle with extras instead?</strong> See our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">best perfume gift sets</a> guide.</li>
<li><strong>Filling a stocking?</strong> Our <a href="/blogs/journal/stocking-fillers-for-her-under-25">stocking fillers under £25</a> has more ideas.</li>
<li><strong>Store minis</strong> upright, away from heat and sunlight, with the cap on.</li>
</ul>
<p>Shop <a href="/collections/perfume-gift-sets-for-her">perfume gift sets for her</a>, <a href="/collections/aftershave-gift-sets-for-him">aftershave gift sets for him</a> and <a href="/collections/gifts-under-50">gifts under £50</a>. Everything is 100% authentic and dispatched from the UK, with free UK delivery over £40.</p>""",
    "faq": [
        ["What is in the Jimmy Choo mini perfume set?",
         "Five 4.5ml eau de parfums: I Want Choo, Jimmy Choo Eau de Parfum, I Want Choo Forever, Rose Passion and I Want Choo Le Parfum, 22.5ml in total."],
        ["What is in the Dior mini perfume set?",
         "The Dior Iconics Mini Perfume Discovery Set has five 5ml minis: J’adore Eau de Parfum, Miss Dior Eau de Parfum, Miss Dior Eau de Toilette, Hypnotic Poison Eau de Toilette and Sauvage Eau de Toilette."],
        ["Is a mini perfume set a good gift?",
         "Yes, especially when you know the brand they like but not their favourite scent. They can try each one and buy the full bottle of the one they wear most."],
        ["Do you sell mini perfume sets for men?",
         "Yes: Paco Rabanne men’s sets with Phantom, Invictus and 1 Million, and a Dolce & Gabbana men’s set with Devotion, K, The One and Light Blue Pour Homme, plus single minis such as Calvin Klein Defy Parfum 10ml."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_mini_perfume_sets_2026-11-14.jsonl")

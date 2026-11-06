"""'About this page' copy + SEO for the 27 brand collections added on 2 Nov 2026 (+ Armaf, whose copy
still described its single pre-November bottle). Same shape as the Day-4 collection copy
(tools/shopify/day4_collections.py): custom.seo_heading (H2) + custom.seo_copy (HTML), SEO description,
extra FAQs, and the brand header's 'You may also love' list (custom.brand.others).

Inputs:  docs/data/new_brand_catalogue_2026-11-06.json (storefront snapshot: handle, title, prices per collection)
         docs/seo/existing_collections_2026-11-02.tsv + new_collection_ids_2026-11-02.tsv (live handles for link checks)
Outputs: docs/seo/new_brand_copy_2026-11-06.jsonl  (collectionUpdate inputs, written to the store only after OK)
         docs/seo/new_brand_copy_2026-11-06.md     (review copy for the user)

Copy rules (CLAUDE.md): primary keyword ('<brand> perfume') in the H2 and the first sentence; 150-380 words;
2-4+ internal links to live collections/products; facts from our catalogue only (names, sizes, notes,
concentration, gender, prices); no medical claims, no stock mentions, no partner claim (Deyga/Vilvah only),
no brand-history claims we cannot check. Prices are filled from the live snapshot ({£handle}); counts are
not written into the copy (they go stale when products are added).
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CAT = json.load(open(ROOT / "docs/data/new_brand_catalogue_2026-11-06.json"))
COLL = {l.split("\t")[0].strip() for f in ("existing_collections_2026-11-02.tsv", "new_collection_ids_2026-11-02.tsv")
        for l in open(ROOT / "docs/seo" / f) if l.strip()}
PRICE = {p["handle"]: p["prices"] for ps in CAT.values() for p in ps}
IDS = {l.split("\t")[0]: l.split("\t")[1].strip() for l in open(ROOT / "docs/seo/new_collection_ids_2026-11-02.tsv") if l.strip()}
IDS["armaf"] = "713388917123"

# Brand header 'You may also love' lists (custom.brand.others): [name, url, line, logo file or null]
ARABIAN = [["Lattafa", "/collections/lattafa", "Arabian perfume house", None],
           ["Al Haramain", "/collections/al-haramain", "Arabian perfume house", "al-haramain"],
           ["Armaf", "/collections/armaf", "Club de Nuit and Miss Armaf", None],
           ["Maison Alhambra", "/collections/maison-alhambra", "Arabian-inspired eaux de parfum", None],
           ["Afnan", "/collections/afnan", "Arabian perfume house", None],
           ["Signature D'orient", "/collections/signature-dorient", "Arabian-inspired, with travel sprays", None]]
DESIGNER = [["Guess", "/collections/guess", "Fashion fragrances and body mists", None],
            ["Calvin Klein", "/collections/calvin-klein", "Designer fragrances", None],
            ["Gucci", "/collections/gucci", "Designer fragrances", None],
            ["Hugo Boss", "/collections/hugo-boss", "Designer fragrances", None],
            ["Dunhill", "/collections/dunhill", "Designer fragrances for men", None]]
VALUE = [["Franck Olivier", "/collections/franck-olivier", "French-style perfumes at everyday prices", None],
         ["Fumeri", "/collections/fumeri", "Bold scents, everyday prices", None],
         ["Maison Alhambra", "/collections/maison-alhambra", "Arabian-inspired eaux de parfum", None],
         ["Jo Milano", "/collections/jo-milano", "Game of Spades and more", None],
         ["Guess", "/collections/guess", "Fashion fragrances and body mists", None]]
NICHE = [["Tiziana Terenzi", "/collections/tiziana-terenzi", "Italian niche extraits", "tiziana-terenzi"],
         ["Fomo", "/collections/fomo", "Niche extraits de parfum", None],
         ["Natural By Woods", "/collections/natural-by-woods", "Woody eaux de parfum with travel atomisers", None],
         ["Attar Collection", "/collections/attar-collection", "Arabian-inspired eaux de parfum", None],
         ["Montale", "/collections/montale", "Oud and rose specialists", None]]
MEN = [["Mercedes-Benz", "/collections/mercedes-benz", "Fragrances for men", None],
       ["Jaguar", "/collections/jaguar", "Fragrances for men", None],
       ["David Beckham", "/collections/david-beckham", "Fragrances for men", None],
       ["Dunhill", "/collections/dunhill", "Designer fragrances for men", None],
       ["Bentley", "/collections/bentley", "Fragrances for men", None]]

# h2, desc (meta description <= 160), others, faq (extra Q/A added after the existing two), body (markdown-ish)
B = {}

B["vera-wang"] = dict(
    h2="Vera Wang perfume: Embrace Green Tea and Pear Blossom",
    desc="Vera Wang perfume at Swansura UK: Embrace Green Tea and Pear Blossom eau de toilette, a fresh floral for women. 100% authentic, free UK delivery over £40.",
    others=DESIGNER,
    faq=[["Which Vera Wang perfume do you sell?", "Vera Wang Embrace Green Tea and Pear Blossom Eau de Toilette 30ml, a fresh floral scent for women."]],
    body="""Vera Wang perfume at Swansura starts with [Vera Wang Embrace Green Tea and Pear Blossom Eau de Toilette 30ml](/products/vera-wang-embrace-green-tea-and-pear-blossom-eau-de-toilette-30ml), a light, fresh floral for women at {£vera-wang-embrace-green-tea-and-pear-blossom-eau-de-toilette-30ml}.

### How it smells
Pear blossom, green tea and bergamot open the scent, so the first impression is clean and bright. Freesia, orange blossom and peony form the heart, and a soft base of sandalwood, cedar and musk keeps it gentle as it settles. It is an easy everyday fragrance that suits work, weekends and warmer days.

### Why the 30ml size works
The 30ml eau de toilette is a handy size for a handbag or a gym bag, and a simple way to try a Vera Wang perfume without committing to a big bottle. It also makes a thoughtful small present, and it sits in our [£15 to £25](/collections/price-15-25) range.

### More like this
If you like fresh florals, compare it with the rest of our [perfume for women](/collections/perfume-for-women) and the [floral fragrances](/collections/scent-floral) family, or try a fruity [Guess body mist](/collections/guess) for a lighter layer. Every Vera Wang perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["david-beckham"] = dict(
    h2="David Beckham perfume: Beyond eau de toilette",
    desc="David Beckham perfume at Swansura UK: Beyond eau de toilette 60ml, a woody aromatic scent for men. 100% authentic, free UK delivery over £40.",
    others=MEN,
    faq=[["Which David Beckham perfume do you sell?", "David Beckham Beyond Eau de Toilette 60ml, a woody aromatic scent for men."]],
    body="""David Beckham perfume at Swansura means [David Beckham Beyond Eau de Toilette 60ml](/products/david-beckham-beyond-eau-de-toilette-60ml), a woody aromatic scent for men at {£david-beckham-beyond-eau-de-toilette-60ml}.

### How it smells
Beyond opens with a cool mojito accord, cardamom and grapefruit, so it starts fresh and a little spicy. Cedarwood, geranium and black pepper give the heart a clean, woody feel, and patchouli, vanilla and leather round it off with a smooth, warm finish. It is easy to wear in the day and still has enough depth for the evening.

### A good-value gift
At 60ml and under £20, Beyond is one of the easiest fragrance gifts for him on our shelf. You will find it in our [£15 to £25](/collections/price-15-25) range, and it pairs well with a men's shower gel or deodorant from our [men's grooming](/collections/mens-grooming) edit.

### More like this
Compare it with other woody scents in our [perfume for men](/collections/perfume-for-men) edit, or look at fellow men's houses such as [Mercedes-Benz](/collections/mercedes-benz) and [Jaguar](/collections/jaguar). Every David Beckham perfume we sell is 100% authentic and ships from the UK, and UK delivery is free on orders over £40.""")

B["lattafa"] = dict(
    h2="Lattafa perfume: Khamrah Qahwa, Teriaq and Yara Candy",
    desc="Lattafa perfume at Swansura UK: Khamrah Qahwa, Teriaq, Maahir Black Edition and Yara Candy eaux de parfum. 100% authentic, free UK delivery over £40.",
    others=[a for a in ARABIAN if a[0] != "Lattafa"] + [["Swiss Arabian", "/collections/swiss-arabian", "Arabian perfume house", None]],
    faq=[["Which Lattafa perfume should I start with?", "Khamrah Qahwa is warm and spicy with coffee and vanilla; Yara Candy is a sweet gourmand for women; Teriaq and Maahir Black Edition are deeper amber-woody scents."],
         ["What size are your Lattafa perfumes?", "All four Lattafa perfumes we stock are 100ml eaux de parfum."]],
    body="""Lattafa perfume is known for rich, long-lasting Arabian blends, and our edit brings together four 100ml eaux de parfum from {£min}. Three are unisex amber-woody scents and one is a sweet gourmand for women.

### Lattafa Khamrah Qahwa
[Lattafa Khamrah Qahwa](/products/lattafa-khamrah-qahwa-eau-de-parfum-100ml) ({£lattafa-khamrah-qahwa-eau-de-parfum-100ml}) opens with cinnamon, cardamom and ginger. Praline, candied fruits and white flowers follow, then a base of coffee, vanilla, tonka bean, benzoin and musk. Warm, spicy and a little sweet, it suits cooler months and evenings.

### Teriaq and Maahir Black Edition
[Lattafa Teriaq](/products/lattafa-teriaq-eau-de-parfum-100ml) ({£lattafa-teriaq-eau-de-parfum-100ml}) mixes caramel, bitter almond and apricot with honey and rose over leather, vanilla and vetiver. [Lattafa Maahir Black Edition](/products/lattafa-maahir-black-edition-eau-de-parfum-100ml) ({£lattafa-maahir-black-edition-eau-de-parfum-100ml}) is drier and smokier: black and pink pepper with saffron, then labdanum and cade oil, and a base of leather, cedar, guaiac wood and moss.

### Lattafa Yara Candy
[Lattafa Yara Candy](/products/lattafa-yara-candy-eau-de-parfum-100ml) ({£lattafa-yara-candy-eau-de-parfum-100ml}) is the playful one: green mandarin and blackcurrant, a strawberry fizz candy accord with gardenia, and a soft base of vanilla syrup, musk, sandalwood and amber.

### More Arabian perfume
If you enjoy Lattafa perfume, browse our full [Arabian perfume](/collections/arabian-perfume) edit, the [oud perfume](/collections/oud-perfume) page, or houses with a similar style such as [Afnan](/collections/afnan), [Maison Alhambra](/collections/maison-alhambra) and [Armaf](/collections/armaf). Every bottle is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["guess"] = dict(
    h2="Guess perfume and Guess body mists",
    desc="Guess perfume at Swansura UK: Seductive, Seductive Noir and Red, Girl Belle, Dare and Guess Man, plus 250ml body mists and gift sets. Free UK delivery over £40.",
    others=[["Franck Olivier", "/collections/franck-olivier", "French-style perfumes at everyday prices", None],
            ["Vera Wang", "/collections/vera-wang", "Fragrances for women", None],
            ["Calvin Klein", "/collections/calvin-klein", "Designer fragrances", None],
            ["Juicy Couture", "/collections/juicy-couture", "Playful fragrances for women", None],
            ["Ariana Grande", "/collections/ariana-grande", "Sweet fragrances for women", None]],
    faq=[["What is the difference between a Guess body mist and a Guess eau de toilette?", "A body mist is a lighter spray you can use generously over the body; an eau de toilette is more concentrated, so a few sprays last longer. Several Guess scents, such as Seductive, Seductive Noir, Seductive Red and Girl Belle, come in both."],
         ["Do you sell Guess gift sets?", "Yes: the Guess Seductive mini set (4 x 15ml), Guess Pink and Seductive Noir sets for women, and Seductive Homme Noir and Uomo sets for men."]],
    body="""Guess perfume at Swansura covers the full range: eaux de toilette for women and men, 250ml body mists, and gift sets, with prices from {£min}. Most of the line is bright, fruity and floral, with warmer woody scents for men.

### Guess Seductive, Noir and Red
[Guess Seductive Eau de Toilette 75ml](/products/guess-seductive-eau-de-toilette-75ml) blends bergamot, blackcurrant and pear with jasmine and orange flower over vanilla and cashmere wood. Seductive Noir adds sage, iris and vetiver for a cooler, more grown-up feel, while Seductive Red brings cherry, almond and pink pepper over tonka and sandalwood. Each comes as an eau de toilette and a body mist, and the [Seductive mini set (4 x 15ml)](/products/guess-seductive-eau-de-toilette-gift-set-seductive-noir-red-blue-4-x-15ml) lets you try four at once.

### Guess body mists
The 250ml Guess body mists, from {£guess-bella-vita-body-mist-250ml}, are easy to layer and refresh through the day. Choose from Bella Vita and Bella Vita Rosa, the 1981 trio, Girl and Girl Belle, the Love line, the Sexy Skin line (including Sweet Sugar and Solar Warmth) and the shimmer mists such as Ibiza Radiant and Miami Vibes.

### Guess for men
[Guess Man Eau de Toilette 150ml](/products/guess-man-eau-de-toilette-150ml) pairs apple, lavender and bergamot with cedarwood and sandalwood. Seductive Homme Red is warmer with cinnamon, fig and vanilla, and the Seductive Homme Noir and Uomo gift sets add a body spray, a shower gel and a bag.

### More gift ideas
Browse our [perfume gift sets](/collections/perfume-gift-sets), [gifts under £25](/collections/gifts-under-25) and [Christmas gifts](/collections/christmas-gifts), or compare with other [perfume for women](/collections/perfume-for-women). Every Guess perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["swiss-arabian"] = dict(
    h2="Swiss Arabian perfume: Shaghaf Oud Royale",
    desc="Swiss Arabian perfume at Swansura UK: Shaghaf Oud Royale eau de parfum 75ml, saffron and rose over oud, praline and vanilla. Free UK delivery over £40.",
    others=[a for a in ARABIAN if a[0] != "Signature D'orient"],
    faq=[["Which Swiss Arabian perfume do you sell?", "Swiss Arabian Shaghaf Oud Royale Eau de Parfum 75ml, a unisex oud scent with saffron, rose, praline and vanilla."]],
    body="""Swiss Arabian perfume at Swansura starts with [Swiss Arabian Shaghaf Oud Royale Eau de Parfum 75ml](/products/swiss-arabian-shaghaf-oud-royale-eau-de-parfum-75ml), a warm, unisex oud scent at {£swiss-arabian-shaghaf-oud-royale-eau-de-parfum-75ml}.

### How it smells
Shaghaf Oud Royale opens with saffron and rose, a classic Arabian pairing. At its heart, agarwood (oud) meets a sweet praline note, which softens the smoky, resinous side of the oud. The base of vanilla, amber and musk keeps it smooth and cosy as it dries down. It is a good choice if you like oud but want something sweeter and easier to wear than a dark, smoky oud.

### How to wear it
Oud scents are rich, so one or two sprays on the wrists or neck are usually enough. It works well for evenings, cooler weather and special occasions, and the 75ml bottle is a generous size for a gift.

### More like this
Explore our full [oud perfume](/collections/oud-perfume) and [Arabian perfume](/collections/arabian-perfume) edits, or compare it with sweet amber scents from [Lattafa](/collections/lattafa) and [Al Haramain](/collections/al-haramain). Every Swiss Arabian perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["jaguar"] = dict(
    h2="Jaguar perfume: Classic Red, Classic Gold and Ultimate Power",
    desc="Jaguar perfume at Swansura UK: Classic Red, Classic Gold, Classic Motion and Ultimate Power eaux de toilette 100ml, plus a gift set. Free UK delivery over £40.",
    others=[m for m in MEN if m[0] != "Jaguar"],
    faq=[["Which Jaguar perfume should I choose?", "Classic Red is fruity and warm, Classic Gold is fresh then woody, Classic Motion is green and woody, and Ultimate Power is crisp with mint and ginger."],
         ["Do you sell a Jaguar gift set?", "Yes: the Jaguar Classic Eau de Toilette & Shower Gel Gift Set (100ml + 200ml)."]],
    body="""Jaguar perfume at Swansura is a small, good-value line of 100ml eaux de toilette, from {£min}, plus a ready-made gift set. They are easy scents for every day.

### The Jaguar Classic line
[Jaguar Classic Red Eau de Toilette 100ml](/products/jaguar-classic-red-eau-de-toilette-100ml) opens with raspberry, blueberry and bergamot, then black pepper and jasmine, and settles on tonka bean, amber and vanilla. [Jaguar Classic Gold](/products/jaguar-classic-gold-eau-de-toilette-100ml) starts with apple, lime and bergamot before orange blossom, teak wood and a vanilla-patchouli base. Classic Motion is greener, with mint and birch leaf over violet, vetiver and sandalwood.

### Jaguar Ultimate Power
[Jaguar Ultimate Power](/products/jaguar-ultimate-power-eau-de-toilette-100ml) is the freshest of the group: bergamot, lemon and mint lead into apple, green leaves and ginger, with moss, patchouli and white woods underneath. It suits daytime and warmer weather.

### A ready-made gift
The [Jaguar Classic Eau de Toilette & Shower Gel Gift Set](/products/jaguar-classic-eau-de-toilette-shower-gel-gift-set-100ml-200ml) pairs a 100ml bottle with a 200ml shower gel, so it is a simple present. See more in [perfume gift sets](/collections/perfume-gift-sets) and [gifts under £25](/collections/gifts-under-25), or compare with our [perfume for men](/collections/perfume-for-men). Every Jaguar perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["rasasi"] = dict(
    h2="Rasasi perfume: Hawas Elixir",
    desc="Rasasi perfume at Swansura UK: Hawas Elixir eau de parfum 100ml, mint and bergamot over dark chocolate, lavender and vanilla. Free UK delivery over £40.",
    others=ARABIAN[:5],
    faq=[["Which Rasasi perfume do you sell?", "Rasasi Hawas Elixir Eau de Parfum 100ml, an aromatic woody scent with mint, dark chocolate, lavender and vanilla."]],
    body="""Rasasi perfume at Swansura starts with [Rasasi Hawas Elixir Eau de Parfum 100ml](/products/rasasi-hawas-elixir-eau-de-parfum-100ml), an aromatic woody scent at {£rasasi-hawas-elixir-eau-de-parfum-100ml}.

### How it smells
Hawas Elixir opens with mugwort, bergamot and mint, so the first spray is fresh and herbal. The heart turns richer, with dark chocolate, lavender and benzoin, and the base of vanilla, tonka bean and white musk gives it a smooth, sweet trail. It balances fresh and warm, which makes it easy to wear from the office to an evening out.

### How to wear it
As an eau de parfum it is fairly concentrated, so two or three sprays are plenty. The 100ml bottle makes it a generous present, and it sits in our [£25 to £50](/collections/price-25-50) range.

### More like this
Browse our [Arabian perfume](/collections/arabian-perfume) and [perfume for men](/collections/perfume-for-men) pages, or try the Club de Nuit and Private Key extraits from [Armaf](/collections/armaf). Every Rasasi perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["tous"] = dict(
    h2="Tous perfume: Touch The Luminous Gold",
    desc="Tous perfume at Swansura UK: Touch The Luminous Gold eau de toilette 50ml, lemon and pink pepper over jasmine, tuberose and amber. Free UK delivery over £40.",
    others=DESIGNER[:1] + [["Armand Basi", "/collections/armand-basi", "Spanish fashion fragrances", None],
                           ["Vera Wang", "/collections/vera-wang", "Fragrances for women", None],
                           ["Chloé", "/collections/chloe", "Designer fragrances for women", None],
                           ["Marc Jacobs", "/collections/marc-jacobs", "Designer fragrances", None]],
    faq=[["Which Tous perfume do you sell?", "Tous Touch The Luminous Gold Eau de Toilette 50ml, a bright floral scent for women."]],
    body="""Tous perfume at Swansura starts with [Tous Touch The Luminous Gold Eau de Toilette 50ml](/products/tous-touch-the-luminous-gold-eau-de-toilette-50ml), a bright floral for women at {£tous-touch-the-luminous-gold-eau-de-toilette-50ml}.

### How it smells
Lemon and pink pepper give it a sparkling, slightly spicy start. Jasmine and tuberose form a creamy white-flower heart, and amber, musk and patchouli add warmth as it settles. It feels polished but easy, so it works for daytime and evenings alike.

### Why the 50ml size
The 50ml eau de toilette is a comfortable size for everyday use and slips easily into a bag. It is also a neat gift, and it sits in our [£25 to £50](/collections/price-25-50) range.

### More like this
If you like white florals, browse the [floral fragrances](/collections/scent-floral) family and our [perfume for women](/collections/perfume-for-women), or try [Armand Basi In Red](/collections/armand-basi). Every Tous perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["afnan"] = dict(
    h2="Afnan perfume: 9am Dive, Supremacy Gold and Tribute Blue",
    desc="Afnan perfume at Swansura UK: 9am Dive, Supremacy Gold and Tribute Blue eaux de parfum 100ml, unisex Arabian scents. 100% authentic, free UK delivery over £40.",
    others=[a for a in ARABIAN if a[0] != "Afnan"],
    faq=[["Which Afnan perfume should I start with?", "9am Dive is fresh with mint and citrus, Supremacy Gold is warm with amber, vanilla and oud, and Tribute Blue is airy with bergamot, cashmere wood and incense."]],
    body="""Afnan perfume at Swansura brings together three unisex 100ml eaux de parfum, from {£min}, each with a different mood.

### Afnan 9am Dive
[Afnan 9am Dive](/products/afnan-9am-dive-eau-de-parfum-100ml) is the fresh one. Lemon, pink pepper, mint and blackcurrant open it, apple, incense and cedarwood follow, and patchouli, jasmine, ginger and sandalwood make a clean, woody base. It suits daytime, the gym bag and warmer weather.

### Afnan Supremacy Gold
[Afnan Supremacy Gold](/products/afnan-supremacy-gold-eau-de-parfum-100ml) ({£afnan-supremacy-gold-eau-de-parfum-100ml}) is warmer. Nutmeg, violet, peach blossom and cumin lead into iris and patchouli, and the base mixes amber, vanilla, agarwood (oud) and benzoin. It is a good evening scent for anyone who likes a soft oud.

### Afnan Tribute Blue
[Afnan Tribute Blue](/products/afnan-tribute-blue-eau-de-parfum-100ml) ({£afnan-tribute-blue-eau-de-parfum-100ml}) sits in between: bergamot, pimento and nutmeg over cashmere wood and amber, with vetiver, incense and musk. Airy at first and smoky later, it works all year round.

### More like this
Compare these with the rest of our [Arabian perfume](/collections/arabian-perfume) and [unisex perfume](/collections/unisex-perfume) edits, or try [Lattafa](/collections/lattafa) and [Armaf](/collections/armaf). Every Afnan perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["maison-alhambra"] = dict(
    h2="Maison Alhambra perfume: Philos, Baroque, Narissa and more",
    desc="Maison Alhambra perfume at Swansura UK: Philos, Baroque la Rouge, Narissa, Pink Shimmer Secret, Salvo and more, from under £20. Free UK delivery over £40.",
    others=[a for a in ARABIAN if a[0] != "Maison Alhambra"],
    faq=[["What do Maison Alhambra perfumes cost at Swansura?", "Most are 80ml or 100ml eaux de parfum between about £18 and £28."],
         ["Which Maison Alhambra perfume is best for men?", "Salvo is a woody aromatic scent for men with bergamot, pepper, lavender and ambroxan; Philos Opus Noir and Jean Lowe Fraiche are warm, woody unisex options."]],
    body="""Maison Alhambra perfume is one of the biggest Arabian-inspired lines on our shelf: 80ml and 100ml eaux de parfum from {£min}, covering fresh, floral, fruity and warm amber scents.

### Philos and Baroque
The Philos range gives you four moods: Philos Pura is bright with orange, bergamot and white musk; Philos Rosso pairs raspberry and lemon with jasmine and rose; Philos Centro mixes hyacinth and pineapple with iris; and [Philos Opus Noir](/products/maison-alhambra-philos-opus-noir-eau-de-parfum-100ml) is darker, with Turkish rose, leather and nutmeg. [Baroque la Rouge](/products/maison-alhambra-baroque-la-rouge-eau-de-parfum-100ml) is a saffron and jasmine scent over amberwood and fir resin, and the Extreme version adds bitter almond.

### Florals for her
For a soft floral, try Narissa Ambre (frangipani, amber and cashmeran) or Narissa Ruby (rose, iris and tuberose). Pink Shimmer Secret is fruity with strawberry and peony, Pink Velvet is a spicy rose, and [Infini Rose](/products/maison-alhambra-infini-rose-eau-de-parfum-100ml) layers Bulgarian and Turkish rose over vanilla.

### Fresh and woody
[Salvo](/products/maison-alhambra-salvo-eau-de-parfum-100ml) is a woody aromatic for men with bergamot, pepper and lavender over ambroxan and cedar. Pacific Blue (Porto Neroli) is a fresh citrus and neroli scent, while Athena and Galatea bring green, herbal openings over leather and vanilla.

### More like this
Browse the full [Arabian perfume](/collections/arabian-perfume) edit and our [£15 to £25](/collections/price-15-25) range, or compare with [Lattafa](/collections/lattafa) and [Afnan](/collections/afnan). Every Maison Alhambra perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["arabiyat-prestige"] = dict(
    h2="Arabiyat Prestige perfume: Nyla and Nyla Vani-elle",
    desc="Arabiyat Prestige perfume at Swansura UK: Nyla and Nyla Vani-elle eaux de parfum 80ml, tropical floral and creamy vanilla scents. Free UK delivery over £40.",
    others=[a for a in ARABIAN][:5],
    faq=[["What is the difference between Arabiyat Prestige Nyla and Nyla Vani-elle?", "Nyla is a tropical floral with coconut, peach, tiare and jasmine; Nyla Vani-elle is a sweeter vanilla scent with caramel, amber and tonka bean."]],
    body="""Arabiyat Prestige perfume at Swansura is the Nyla pair: two 80ml eaux de parfum for women at {£arabiyat-prestige-nyla-eau-de-parfum-80ml} each, one tropical and floral, one creamy and sweet.

### Arabiyat Prestige Nyla
[Arabiyat Prestige Nyla](/products/arabiyat-prestige-nyla-eau-de-parfum-80ml) opens with coconut, peach, mandarin and bergamot, so it feels sunny from the first spray. Tiare, white flowers, jasmine and rose form the heart, and white musk and patchouli give it a soft, clean finish. It is a bright, holiday-style floral that suits warm days and summer evenings.

### Arabiyat Prestige Nyla Vani-elle
[Arabiyat Prestige Nyla Vani-elle](/products/arabiyat-prestige-nyla-vani-elle-eau-de-parfum-80ml) is the gourmand side of the pair. Vanilla bean and jasmine lead into caramel and amber, and the base of vanilla, tonka bean and musk keeps it creamy and cosy. Choose it if you like sweet, comforting scents for cooler months.

### Wearing them together
Because both share the Nyla style, some people wear Nyla by day and Vani-elle in the evening. The 80ml bottles are a good size for a gift.

### More like this
Browse our [Arabian perfume](/collections/arabian-perfume) edit, sweet scents in the [amber fragrances](/collections/scent-amber) family, or try [Lattafa Yara Candy](/products/lattafa-yara-candy-eau-de-parfum-100ml). Every Arabiyat Prestige perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["armaf"] = dict(
    h2="Armaf perfume: Club de Nuit, Private Key and Miss Armaf",
    desc="Armaf perfume at Swansura UK: Club de Nuit Intense and Precieux, the Private Key extraits, Miss Armaf and Hunter, plus gift sets. Free UK delivery over £40.",
    others=[a for a in ARABIAN if a[0] != "Armaf"],
    story="Armaf perfume at Swansura: Club de Nuit, the Private Key extraits, Miss Armaf eaux de parfum and Armaf Hunter, all 100% authentic and shipped from the UK.",
    faq=[["Which Armaf perfume should I start with?", "Club de Nuit Intense is a rose, saffron and oud eau de parfum; Club de Nuit Precieux and the Private Key extraits are richer; Miss Armaf is a line of fruity florals for women; Hunter is a fresh woody scent for men."],
         ["Do you sell Armaf gift sets?", "Yes: the Club de Nuit men's and women's sets (3 x 30ml) and the Club de Nuit Woman travel set (2 x 12ml)."]],
    body="""Armaf perfume is popular for confident scents at friendly prices, and our edit now covers the house's best-known lines: Club de Nuit, the Private Key extraits, Miss Armaf and Hunter, from {£min}.

### Club de Nuit
[Armaf Club de Nuit Intense Eau de Parfum 105ml](/products/armaf-club-de-nuit-intense-eau-de-parfum-105ml) blends rose, saffron and geranium with nutmeg and violet over patchouli, oud, vanilla and amber. [Club de Nuit Precieux Extrait de Parfum 55ml](/products/armaf-club-de-nuit-precieux-extrait-de-parfum-55ml) is sweeter, with pineapple, caramel and pear over ambergris, vanilla and leather. The men's and women's Club de Nuit sets (3 x 30ml) and a 2 x 12ml travel set make easy gifts.

### The Private Key extraits
The Private Key line (100ml extraits de parfum) has five scents: To My Dreams (pepper, cardamom and leather), To My Life (citrus and white flowers), To My Love (peach, pear and passion fruit), To My Soul (citrus, sage and vanilla) and To My Success (ginger, chilli pepper and vetiver).

### Miss Armaf and Hunter
Miss Armaf is a set of fruity florals for women at {£armaf-miss-armaf-chic-eau-de-parfum-100ml}: Chic, Catwalk, Dazzling, Grandeur, Magnifiq, Mystique, Attitude and Voce Viva. For men, [Armaf Hunter](/products/armaf-hunter-eau-de-parfum-100ml-men-s-fresh-woody-aromatic-fragrance) is fresh and woody with grapefruit, rosemary and cedarwood.

### More like this
Browse our [Arabian perfume](/collections/arabian-perfume) and [perfume gift sets](/collections/perfume-gift-sets) edits, or compare with [Lattafa](/collections/lattafa) and [Afnan](/collections/afnan). Every Armaf perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["formula-1"] = dict(
    h2="Formula 1 perfume: Carbon Reign race vial",
    desc="Formula 1 perfume at Swansura UK: Carbon Reign eau de toilette 1.5ml race vial, pink and timut pepper over lavender and vetiver. Free UK delivery over £40.",
    others=MEN[:4] + [["Mercedes-Benz", "/collections/mercedes-benz", "Fragrances for men", None]][:0],
    faq=[["What is the Formula 1 race vial?", "A 1.5ml sample vial of Formula 1 Carbon Reign Eau de Toilette, handy for trying the scent or adding to a gift."]],
    body="""Formula 1 perfume at Swansura starts small: the [Formula 1 Carbon Reign Race Vial Eau de Toilette 1.5ml](/products/formula-1-carbon-reign-race-vial-eau-de-toilette-1-5ml), at {£formula-1-carbon-reign-race-vial-eau-de-toilette-1-5ml}.

### How it smells
Carbon Reign opens with pink pepper and timut pepper, a bright, slightly citrusy spice. Geranium and lavender give the heart a clean, aromatic feel, and vetiver, patchouli and amber crystals finish it with a warm, woody trail. It is unisex, but its peppery, aromatic style will appeal to anyone who likes fresh men's scents.

### Why a vial
At 1.5ml, the race vial is an easy way to try the scent, and it fits in a pocket, a wash bag or a stocking. Add it to an order as a small extra, or pair it with a full-size bottle as a gift.

### More like this
Browse our [travel size and mini perfumes](/collections/travel-size-minis) and [stocking fillers](/collections/stocking-fillers), or compare with fuller bottles from [Mercedes-Benz](/collections/mercedes-benz) and [Jaguar](/collections/jaguar). Every Formula 1 perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["franck-olivier"] = dict(
    h2="Franck Olivier perfume: Sun Java, Bella, Passion and Collection Privée",
    desc="Franck Olivier perfume at Swansura UK: Sun Java, Bella, Passion, Black Touch and Collection Privée, plus deodorants and gift sets. Free UK delivery over £40.",
    others=[v for v in VALUE if v[0] != "Franck Olivier"],
    faq=[["What is Franck Olivier Collection Privée?", "A line of 100ml 'le parfum' scents (Ambre Gold, Black Tiger, Magic Blossom, Parisian Oud, Red Addict, Santal Velvet and Tribal), richer than the brand's eaux de toilette."],
         ["Do you sell Franck Olivier deodorant sprays?", "Yes, 250ml deodorant sprays in several of the brand's scents, such as Black Touch, Bamboo, Bella In Paris and Sunrise."]],
    body="""Franck Olivier perfume brings French-style scents at everyday prices, and we stock a wide line-up: eaux de toilette and eaux de parfum, the richer Collection Privée, 250ml deodorant sprays and gift sets, from {£min}.

### For men: Sun Java, Black Touch and Eau de Passion
[Franck Olivier Sun Java Intense Men](/products/franck-olivier-sun-java-intense-men-eau-de-parfum-75ml) mixes mandarin, mint and lavender with amber and woods, while Sun Java Blue and Sun Java White are fresher eaux de toilette. [Black Touch Men](/products/franck-olivier-black-touch-men-eau-de-toilette-100ml) is spicy with cardamom and grapefruit over vetiver and patchouli; Blue Touch, In Black, Bamboo America and Eau de Passion complete the men's side.

### For women: Bella, Passion and Giorgia
[Franck Olivier Bella In Paris Women](/products/franck-olivier-bella-in-paris-women-eau-de-parfum-75ml) pairs peach, pear and orange with Turkish rose and magnolia. Passion and Passion Extreme are fruity florals, One Kiss is soft with vanilla and praline, and Giorgia, In Pink and Nature are bright and fresh.

### Collection Privée
The Collection Privée (100ml le parfum) is the richest line: Parisian Oud, Black Tiger, Tribal, Red Addict, Santal Velvet, Ambre Gold and [Magic Blossom](/products/franck-olivier-magic-blossom-collection-privee-le-parfum-100ml), at {£franck-olivier-magic-blossom-collection-privee-le-parfum-100ml} each.

### Deodorants and gift sets
The 250ml deodorant sprays match several scents, and the Bella and Black Touch gift sets pair a bottle with its deodorant. See our [deodorants](/collections/deodrants), [gifts under £25](/collections/gifts-under-25) and [perfume for men](/collections/perfume-for-men). Every Franck Olivier perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["armand-basi"] = dict(
    h2="Armand Basi perfume: In Red eau de parfum",
    desc="Armand Basi perfume at Swansura UK: In Red eau de parfum 100ml, ginger and bergamot over jasmine, rose and white musk. Free UK delivery over £40.",
    others=[["Tous", "/collections/tous", "Spanish fashion fragrances", None]] + DESIGNER[:4],
    faq=[["Which Armand Basi perfume do you sell?", "Armand Basi In Red Eau de Parfum 100ml, a floral fruity scent for women."]],
    body="""Armand Basi perfume at Swansura starts with [Armand Basi In Red Eau de Parfum 100ml](/products/armand-basi-in-red-eau-de-parfum-100ml), a warm, spicy floral for women at {£armand-basi-in-red-eau-de-parfum-100ml}.

### How it smells
In Red opens with ginger, bergamot, mandarin and cardamom, so it starts bright with a gentle spice. Jasmine, violet leaf, rose and lily of the valley make up a fresh floral heart, and woody notes and white musk give it a clean, soft finish. It sits between fresh and warm, which makes it easy to wear all year.

### A generous bottle
The 100ml eau de parfum is good value for everyday use and a smart choice for a gift. It sits in our [£25 to £50](/collections/price-25-50) range.

### More like this
Compare it with other [perfume for women](/collections/perfume-for-women) and the [floral fragrances](/collections/scent-floral) family, or try [Tous](/collections/tous) for another bright floral. Every Armand Basi perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["bois-1920"] = dict(
    h2="Bois 1920 perfume: Oro gift set",
    desc="Bois 1920 perfume at Swansura UK: the Oro eau de parfum gift set, five 18ml Italian niche scents in one box. 100% authentic, free UK delivery over £40.",
    others=NICHE,
    faq=[["What is in the Bois 1920 Oro gift set?", "Five 18ml eaux de parfum from the Bois 1920 Oro line in one box."]],
    body="""Bois 1920 perfume at Swansura comes as a discovery box: the [Bois 1920 Oro Eau de Parfum Gift Set](/products/bois-1920-oro-eau-de-parfum-gift-set-5-scents-5-x-18ml), five 18ml eaux de parfum from the Italian house's Oro line, at {£bois-1920-oro-eau-de-parfum-gift-set-5-scents-5-x-18ml}.

### Why a set of five
Niche perfume can be hard to choose online. With five 18ml bottles you can wear each scent for a few days, see how it develops on your skin and decide which you like best. The 18ml size is also easy to carry, so the set doubles as a travel wardrobe of scents.

### A gift for a perfume lover
The boxed set is one of the most generous fragrance presents on our shelf. You will find it with our [luxury gifts over £50](/collections/gifts-over-50), [perfume gift sets](/collections/perfume-gift-sets) and [Christmas gifts](/collections/christmas-gifts).

### More like this
If you enjoy Italian niche perfume, explore [Tiziana Terenzi](/collections/tiziana-terenzi) and our [niche perfume](/collections/niche-perfume) edit. Every Bois 1920 perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["mercedes-benz"] = dict(
    h2="Mercedes-Benz perfume: Club Black, Le Parfum, Intense and Man Private",
    desc="Mercedes-Benz perfume at Swansura UK: Club Black, Le Parfum, Intense, Man Private and the Trio Nomade set (Land, Sea & Air). Free UK delivery over £40.",
    others=[m for m in MEN if m[0] != "Mercedes-Benz"],
    faq=[["Which Mercedes-Benz perfume should I choose?", "Club Black is warm with incense, vanilla and benzoin; Le Parfum adds saffron and oud; Intense is fresh and peppery; Man Private is aromatic with cardamom, lavender and cashmere wood."]],
    body="""Mercedes-Benz perfume at Swansura covers four men's scents and two gift sets, from {£min}, all with a polished, aromatic woody style.

### Mercedes-Benz Club Black
[Mercedes-Benz Club Black Eau de Parfum 100ml](/products/mercedes-benz-club-black-eau-de-parfum-100ml) is the warmest: bergamot, then incense and jasmine, over vanilla, benzoin, ambroxan and woods. The [Club Black Eau de Toilette & Shower Gel Gift Set](/products/mercedes-benz-club-black-eau-de-toilette-shower-gel-gift-set-100ml) pairs the scent with a matching shower gel.

### Le Parfum, Intense and Man Private
[Mercedes-Benz Le Parfum 120ml](/products/mercedes-benz-le-parfum-120ml) opens with pink pepper and bergamot, adds violet leaf, saffron and galbanum, and settles on oud, amber and patchouli. Mercedes-Benz Intense (120ml eau de toilette) is fresher, with lemon, mandarin and Bourbon pepper over vetiver and cedar. Man Private combines cardamom, cypress and lavender with cashmere wood.

### The Trio Nomade set
The [Mercedes-Benz Trio Nomade set](/products/mercedes-benz-trio-nomade-eau-de-parfum-set-land-sea-air-3-x-30ml) holds three 30ml eaux de parfum, Land, Sea and Air, so you can switch scents with the day.

### More like this
Browse our [perfume for men](/collections/perfume-for-men) and [gifts for him](/collections/gifts-for-him), or compare with [Jaguar](/collections/jaguar) and [Dunhill](/collections/dunhill). Every Mercedes-Benz perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["notebook"] = dict(
    h2="Notebook perfume: Cassis & Pink Pepper",
    desc="Notebook perfume at Swansura UK: Cassis & Pink Pepper eau de toilette 100ml, blackcurrant and pink pepper over rose and jasmine. Free UK delivery over £40.",
    others=VALUE,
    faq=[["Which Notebook perfume do you sell?", "Notebook Cassis & Pink Pepper Eau de Toilette 100ml, a spicy-fruity floral with rose, jasmine and musk."]],
    body="""Notebook perfume at Swansura starts with [Notebook Cassis & Pink Pepper Eau de Toilette 100ml](/products/notebook-cassis-pink-pepper-eau-de-toilette-100ml), at {£notebook-cassis-pink-pepper-eau-de-toilette-100ml}.

### How it smells
As the name says, blackcurrant (cassis) and pink pepper lead the way: juicy, tart and lightly spicy. Rose and jasmine soften the heart, and musk, cedarwood and amber give it a smooth, warm finish. It is a cheerful everyday scent with a little more character than a plain fruity floral, and it works in any season.

### Good value for everyday wear
The 100ml eau de toilette is a generous bottle at a friendly price, so it is easy to wear daily without saving it for best. Spray it on pulse points after a shower for the most even finish. It sits in our [£15 to £25](/collections/price-15-25) range.

### More like this
Browse our [perfume for women](/collections/perfume-for-women), the [amber fragrances](/collections/scent-amber) family, or try fruity florals from [Franck Olivier](/collections/franck-olivier). Every Notebook perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["attar-collection"] = dict(
    h2="Attar Collection perfume: Crystal Love, Azalea, Areej and more",
    desc="Attar Collection perfume at Swansura UK: Crystal Love for men and women, Azalea, Areej, Floral Musk and The Persian Gold, 100ml EDP. Free UK delivery over £40.",
    others=ARABIAN[:5],
    faq=[["Which Attar Collection perfume should I start with?", "Crystal Love for Women is a gourmand with milk chocolate and vanilla; Crystal Love for Men is warmer with cinnamon, rose and leather; Azalea, Areej and Floral Musk are soft florals; The Persian Gold is a sweet rose and caramel scent."]],
    body="""Attar Collection perfume brings Arabian-inspired eaux de parfum with a sweet, soft style, and we stock six 100ml bottles from {£min}.

### Crystal Love for women and men
[Attar Collection Crystal Love for Women](/products/attar-collection-crystal-love-eau-de-parfum-for-women-100ml) is a gourmand: fruits and rose over milk chocolate, white musk and nutmeg, then Bourbon vanilla and tonka bean. [Crystal Love for Men](/products/attar-collection-crystal-love-eau-de-parfum-for-men-100ml) shares the idea but turns warmer, with citrus, cinnamon and rose over ambergris, patchouli and leather.

### Floral and powdery
[Attar Collection Azalea](/products/attar-collection-azalea-eau-de-parfum-100ml) mixes ylang-ylang and orchid with heliotrope, marzipan and vanilla over myrrh and sandalwood. Areej is soft and powdery with magnolia, Damask rose and white musk, and Floral Musk combines jasmine, caramel and amber over sandalwood.

### The Persian Gold
[The Persian Gold](/products/attar-collection-the-persian-gold-eau-de-parfum-100ml) is the richest of the group: powdery tea rose, rose syrup and caramel, then nutmeg, vanilla and patchouli.

### More like this
Browse our [Arabian perfume](/collections/arabian-perfume) edit and the [amber fragrances](/collections/scent-amber) family, or compare with [Lattafa](/collections/lattafa) and [Maison Alhambra](/collections/maison-alhambra). Every Attar Collection perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["fomo"] = dict(
    h2="Fomo perfume: Gary's Den, Envy and the extraits",
    desc="Fomo perfume at Swansura UK: Gary's Den, Envy, Fraglover's Tea and Essence of The Other World, all 100ml. Free UK delivery over £40.",
    others=[n for n in NICHE if n[0] != "Fomo"],
    faq=[["What is the difference between Fomo le parfum and extrait de parfum?", "Both are concentrated; the extraits (Fraglover's Tea and Essence of The Other World) are the richer of the two."]],
    body="""Fomo perfume at Swansura is a small niche line of four 100ml scents, from {£min}: two le parfum bottles and two extraits de parfum.

### Fomo Gary's Den and Envy
[Fomo Gary's Den](/products/fomo-garys-den-le-parfum-100ml) opens with lavender and bergamot, then iris, labdanum, cardamom and coriander, and settles on vanilla, patchouli, cedarwood and amber. It is warm and polished. [Fomo Envy](/products/fomo-envy-le-parfum-100ml) is spicier, with grapefruit, black pepper and clove over sandalwood, carnation and rose, and a base of patchouli, labdanum and tonka.

### The extraits
[Fomo Fraglover's Tea](/products/fomo-fraglovers-tea-extrait-de-parfum-100ml) pairs tea, bergamot and cardamom with fig, jasmine and osmanthus over tobacco, tonka and sandalwood. [Essence of The Other World](/products/fomo-essence-of-the-other-world-extrait-de-parfum-100ml) mixes jasmine, neroli, eucalyptus and anise with amber, rose and heliotrope over myrrh and vanilla. Both are unisex.

### More like this
Explore our [niche perfume](/collections/niche-perfume) and [unisex perfume](/collections/unisex-perfume) edits, or compare with [Tiziana Terenzi](/collections/tiziana-terenzi). Every Fomo perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["adi-guru"] = dict(
    h2="Adi Guru perfume: Elegance, Harmony, Sensation and Soul",
    desc="Adi Guru perfume at Swansura UK: Elegance, Harmony, Sensation and Soul eaux de parfum 100ml, warm amber and woody scents. Free UK delivery over £40.",
    others=ARABIAN[:5],
    faq=[["Which Adi Guru perfume should I choose?", "Harmony is fresh with citrus and sea notes, Elegance is herbal and floral, Sensation is a warm tobacco and vanilla scent, and Soul pairs juniper and violet with leather and woods."]],
    body="""Adi Guru perfume at Swansura is a set of four 100ml eaux de parfum at {£min} each, from fresh to warm.

### Fresh: Harmony and Elegance
[Adi Guru Harmony](/products/adi-guru-harmony-eau-de-parfum-100ml) opens with lemon, mandarin and sea notes, adds rosemary, thyme and white flowers, and finishes on vanilla, patchouli and amber. [Adi Guru Elegance](/products/adi-guru-elegance-eau-de-parfum-100ml) is more herbal: bergamot, cumin, lemon and rosemary over basil, carnation and jasmine, with amber, oakmoss and sandalwood beneath.

### Warm: Sensation and Soul
[Adi Guru Sensation](/products/adi-guru-sensation-eau-de-parfum-100ml) is a cosy tobacco scent, with tobacco leaf and spices, tonka bean, tobacco blossom and vanilla, and dried fruits and woods. [Adi Guru Soul](/products/adi-guru-soul-eau-de-parfum-100ml) pairs juniper berries and black violet with a leather accord, blonde woods, vetiver and raspberry.

### More like this
Browse our [Arabian perfume](/collections/arabian-perfume) and [amber fragrances](/collections/scent-amber) edits, or compare with [Lattafa](/collections/lattafa) and [Inaaya](/collections/inaaya). Every Adi Guru perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["fun-basics"] = dict(
    h2="Fun & Basics perfume: Be Fun and Funtastic",
    desc="Fun & Basics perfume at Swansura UK: Be Fun and Funtastic for men and women, 100ml at an easy price. 100% authentic, free UK delivery over £40.",
    others=VALUE,
    faq=[["Which Fun & Basics perfume should I choose?", "Be Fun Man is a coffee, chocolate and leather scent; Be Fun Women is fruity with lemon, peach and apple; Funtastic Man and Funtastic Woman are fresh citrus scents with warm woody bases."]],
    body="""Fun & Basics perfume at Swansura is a playful, good-value line: four 100ml bottles at {£min} each, two for men and two for women.

### Be Fun
[Fun & Basics Be Fun Man](/products/fun-basics-be-fun-man-eau-de-toilette-100ml) is a gourmand for men: bergamot and myrtle, then roasted coffee beans, chocolate and hazelnut, over leather and cedarwood. [Be Fun Women](/products/fun-basics-be-fun-women-eau-de-toilette-100ml) is lighter and fruitier, with Amalfi lemon, peach and red apple over violet, jasmine and soft woods.

### Funtastic
[Funtastic Man](/products/fun-basics-funtastic-man-eau-de-parfum-100ml) opens with orange, grapefruit and bergamot and dries down to musk, patchouli, sandalwood and tonka bean. [Funtastic Woman](/products/fun-basics-funtastic-woman-eau-de-parfum-100ml) pairs lemon, grapefruit, pink pepper and mint with melon, jasmine and ginger, over sandalwood, cedarwood and amber.

### An easy gift
At under £20 for a full 100ml, these sit in our [£15 to £25](/collections/price-15-25) range; compare them with [Franck Olivier](/collections/franck-olivier). Every Fun & Basics perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["inaaya"] = dict(
    h2="Inaaya perfume: Amal, Ghali, Jasim and more",
    desc="Inaaya perfume at Swansura UK: Amal, Ghali, Jasim, Nawaal, Sameer and Shajah eaux de parfum 100ml, sweet Arabian-inspired scents. Free UK delivery over £40.",
    others=ARABIAN[:5],
    faq=[["What do Inaaya perfumes smell like?", "Mostly warm and sweet: Amal has strawberry and marshmallow, Ghali almond, hazelnut and cocoa, Sameer spiced honey and tobacco leaf, and Shajah tropical fruits and white flowers."]],
    body="""Inaaya perfume brings Arabian-inspired, mostly sweet and warm eaux de parfum, and we stock six 100ml bottles from {£min}.

### Sweet and gourmand
[Inaaya Amal](/products/inaaya-amal-eau-de-parfum-100ml) is the sweetest: lemon, strawberry and marshmallow over coconut and nectarine blossom, with musk and vanilla. [Inaaya Ghali](/products/inaaya-ghali-eau-de-parfum-100ml) ({£inaaya-ghali-eau-de-parfum-100ml}) mixes cardamom, almond and hazelnut with pear, freesia and peony over nougat, cocoa and cream.

### Warm and spicy
[Inaaya Sameer](/products/inaaya-sameer-eau-de-parfum-100ml) pairs spiced honey and cardamom with lavender, orange blossom and tobacco leaf over vanilla and tonka. Jasim is spicy with pink pepper, chestnut and clove, and Nawaal mixes cardamom and pink pepper with pineapple and sage.

### Soft and floral
[Inaaya Shajah](/products/inaaya-shajah-eau-de-parfum-100ml) is the softest of the six: mandarin, heliotrope and orchid with tropical fruits and white flowers, over vanilla, sandalwood and warm amber.

### More like this
Browse our [Arabian perfume](/collections/arabian-perfume) edit and the [amber fragrances](/collections/scent-amber) family, or compare with [Lattafa](/collections/lattafa) and [Maison Alhambra](/collections/maison-alhambra). Every Inaaya perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["natural-by-woods"] = dict(
    h2="Natural By Woods perfume with travel atomisers",
    desc="Natural By Woods perfume at Swansura UK: 100ml eaux de parfum with a travel atomiser, from Bloom to Royal Night, and a discovery set. Free UK delivery over £40.",
    others=[n for n in NICHE if n[0] != "Natural By Woods"],
    faq=[["What comes with a Natural By Woods perfume?", "Each bottle is a 100ml eau de parfum with a travel atomiser (5ml; 15ml with Flame)."],
         ["Is there a Natural By Woods discovery set?", "Yes, the Natural By Woods Discovery Set lets you try several scents before choosing a full bottle."]],
    body="""Natural By Woods perfume at Swansura comes in a handy format: each scent is a 100ml eau de parfum with a travel atomiser, from {£min}, so you have a bottle for home and a travel spray for your bag.

### Fresh and bright
[Natural By Woods North Star](/products/natural-by-woods-north-star-eau-de-parfum-with-travel-atomiser-100ml-5ml) is citrusy with bergamot, lemon and grapefruit over cedarwood, frankincense and sandalwood. Sun mixes citrus, orange and ginger with cedarwood, olibanum and rose, and Dawn pairs pear with jasmine, amber and patchouli.

### Woody and warm
[Natural By Woods Earth](/products/natural-by-woods-earth-eau-de-parfum-with-travel-atomiser-100ml-5ml) blends bergamot, pink pepper and cardamom with patchouli, cedarwood and vetiver over amber, sandalwood and oakmoss. Dusk is similar but simpler, and Flame (with a 15ml atomiser) pairs lemon zest and bitter orange blossom with spices and amber.

### Rose, saffron and oud
[Natural By Woods Royal Night](/products/natural-by-woods-royal-night-eau-de-parfum-with-travel-atomiser-100ml-5ml) pairs saffron and cardamom with rose and oud. Essence mixes saffron and cypress with Bulgarian rose, then oud, vanilla and leather, and Bloom combines lychee, rhubarb and Turkish rose with incense.

### Try before you choose
The Natural By Woods Discovery Set lets you sample the range first. See also our [oud perfume](/collections/oud-perfume) and [woody fragrances](/collections/scent-woody) pages. Every Natural By Woods perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["unlimited"] = dict(
    h2="Unlimited perfume: Courage, Desire, Passion and Attitude",
    desc="Unlimited perfume at Swansura UK: Courage, Desire, Passion and Attitude eaux de parfum 100ml. 100% authentic, shipped from the UK, free UK delivery over £40.",
    others=VALUE,
    faq=[["Which Unlimited perfume should I choose?", "Desire is fresh with lemon, orange blossom and apple over woods and vanilla; Attitude is clean with citrus, lavender and cedarwood; Courage and Passion are white-flower scents with tuberose, jasmine and ylang-ylang."]],
    body="""Unlimited perfume at Swansura is a line of four 100ml eaux de parfum, from {£min}, ranging from crisp and clean to rich white florals.

### Unlimited Desire and Attitude
[Unlimited Desire](/products/unlimited-desire-eau-de-parfum-100ml) opens with lemon, orange blossom and crisp apple, adds patchouli, woods and a lemony rose, and finishes with vanilla and musk. [Unlimited Attitude](/products/unlimited-attitude-eau-de-parfum-100ml) is cleaner and simpler: fresh citrus and bergamot, lavender and jasmine, over musk and cedarwood. Both are easy everyday scents.

### Unlimited Courage and Passion
[Unlimited Courage](/products/unlimited-courage-eau-de-parfum-100ml) and [Unlimited Passion](/products/unlimited-passion-eau-de-parfum-100ml) both centre on tuberose and tomato leaf, with jasmine, ylang-ylang and vanilla at the heart and patchouli and oakmoss in the base. They suit anyone who likes a bold, creamy white-flower scent.

### More like this
Browse our [perfume for men](/collections/perfume-for-men), the [floral fragrances](/collections/scent-floral) family and our [gifts £25 to £50](/collections/gifts-25-to-50), or compare with [Fomo](/collections/fomo). Every Unlimited perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["maison-de-milan"] = dict(
    h2="Maison de Milan perfume: Milano Girl, Amalfi Bleu and more",
    desc="Maison de Milan perfume at Swansura UK: Milano Girl, Amalfi Bleu, L'Homme Suave, Opulent Gold and more, 100ml EDP under £20. Free UK delivery over £40.",
    others=VALUE,
    faq=[["Which Maison de Milan perfume is for men?", "Amalfi Bleu and L'Homme Suave are for men; Brave Lad, M, Opulent Gold and Valiant Pour Homme are unisex; the rest are for women."]],
    body="""Maison de Milan perfume at Swansura is a large line of 100ml eaux de parfum at friendly prices, from {£min}, for women, men and everyone.

### For women
The Milano Girl trio covers three moods: [Milano Girl Red](/products/maison-de-milan-milano-girl-red-eau-de-parfum-100ml) is floral, fruity and amber, Milano Girl White is a soft white-flower and musk scent, and Milano Girl Black is floral and woody. Bliss Rouge opens with blood orange, Gossip Pour Femme pairs citrus and pear with violet, and Delight, Elegance and Invincible complete the women's side.

### For men and unisex
[Maison de Milan Amalfi Bleu](/products/maison-de-milan-amalfi-bleu-eau-de-parfum-100ml) is fresh with mint and melon, and L'Homme Suave mixes bergamot, lavender and pepper. Unisex options include Opulent Gold (floral over warm woods), M (bergamot and green apple), Brave Lad (juicy fruits) and Valiant Pour Homme (citrus and spice).

### Good value for everyday wear
With most bottles under £20, these sit in our [£15 to £25](/collections/price-15-25) range and are an easy way to try a new style. Compare them with other [perfume for women](/collections/perfume-for-women) or [Franck Olivier](/collections/franck-olivier). Every Maison de Milan perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["chris-adams"] = dict(
    h2="Chris Adams perfume for men",
    desc="Chris Adams perfume at Swansura UK: CA DX 77 Pour Homme eau de parfum and Black Shadow Pour Homme eau de toilette, 100ml each. Free UK delivery over £40.",
    others=MEN,
    faq=[["Which Chris Adams perfume do you sell?", "CA DX 77 Pour Homme Eau de Parfum 100ml (citrus and bergamot) and Black Shadow Pour Homme Eau de Toilette 100ml (a chypre scent), both for men."]],
    body="""Chris Adams perfume at Swansura is two 100ml bottles for men, both under £15, making them some of the best-value full-size scents on our shelf.

### Chris Adams CA DX 77 Pour Homme
[Chris Adams CA DX 77 Pour Homme Eau de Parfum 100ml](/products/chris-adams-ca-dx-77-pour-homme-eau-de-parfum-100ml) ({£chris-adams-ca-dx-77-pour-homme-eau-de-parfum-100ml}) opens with citrus and bergamot, giving it a clean, fresh start that suits daytime and the office. As an eau de parfum it is a little more concentrated than an eau de toilette.

### Chris Adams Black Shadow Pour Homme
[Chris Adams Black Shadow Pour Homme Eau de Toilette 100ml](/products/chris-adams-black-shadow-pour-homme-eau-de-toilette-100ml) ({£chris-adams-black-shadow-pour-homme-eau-de-toilette-100ml}) is a chypre scent: a classic style built on a fresh opening and a mossy, woody base. It is a smart choice for evenings.

### Easy gifts
At these prices, both sit in our [under £15](/collections/price-0-15) range, or pair one with a shower gel from our [men's grooming](/collections/mens-grooming) edit. See more [perfume for men](/collections/perfume-for-men). Every Chris Adams perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")

B["rihanah"] = dict(
    h2="Rihanah perfume: Ajwaa Oud",
    desc="Rihanah perfume at Swansura UK: Ajwaa Oud unisex eau de parfum 100ml, an Arabian oud scent at an easy price. 100% authentic, free UK delivery over £40.",
    others=ARABIAN[:5],
    faq=[["Which Rihanah perfume do you sell?", "Rihanah Ajwaa Oud Unisex Eau de Parfum 100ml. Message us for the full scent notes before you buy."]],
    body="""Rihanah perfume at Swansura starts with [Rihanah Ajwaa Oud Unisex Eau de Parfum 100ml](/products/rihanah-ajwaa-oud-eau-de-parfum-100ml), an Arabian-style oud scent at {£rihanah-ajwaa-oud-eau-de-parfum-100ml}.

### An easy way into oud
Oud perfume is built around agarwood, a dark, resinous note with a smoky, woody depth. Ajwaa Oud is a 100ml eau de parfum for men and women, which makes it one of the most affordable ways to try an oud fragrance on our shelf. We do not yet have the full list of notes from the brand, so message us before you buy if you would like the details.

### How to wear oud
Oud scents are rich, so start with one or two sprays on the wrists or neck. They suit cooler weather and evenings, and they layer well with a warm body butter.

### More like this
Explore our full [oud perfume](/collections/oud-perfume) and [Arabian perfume](/collections/arabian-perfume) edits, or compare with [Swiss Arabian Shaghaf Oud Royale](/collections/swiss-arabian) and [Al Haramain](/collections/al-haramain). Every Rihanah perfume we sell is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")


# Hub pages whose copy predates the 2 Nov brands (counts and prices out of date, no links to the new
# Arabian houses). Same rules; keyword = the collection's primary keyword.
HUB = {}
HUB["arabian-perfume"] = dict(
    kw="Arabian perfume",
    h2="Arabian perfume: oud, amber and musk from Lattafa, Armaf, Al Haramain and more",
    desc="Arabian perfume at Swansura UK: Lattafa, Armaf, Al Haramain, Afnan, Maison Alhambra, Swiss Arabian, Rasasi and more. 100% authentic, free UK delivery over £40.",
    explore_add=[["Lattafa", "/collections/lattafa"], ["Afnan", "/collections/afnan"], ["Maison Alhambra", "/collections/maison-alhambra"],
                 ["Arabiyat Prestige", "/collections/arabiyat-prestige"], ["Swiss Arabian", "/collections/swiss-arabian"], ["Rasasi", "/collections/rasasi"]],
    body="""Arabian perfume is known for rich, long-lasting blends of oud, amber, musk and rose. This edit brings together more than a dozen houses, from {£min}, ranging from fresh everyday scents to deep evening blends.

### Lattafa, Afnan and Rasasi
[Lattafa](/collections/lattafa) is one of the most searched names in Arabian perfume: Khamrah Qahwa mixes cinnamon and cardamom with coffee and vanilla, and Yara Candy is a sweet gourmand. [Afnan](/collections/afnan) adds 9am Dive, Supremacy Gold and Tribute Blue, and [Rasasi Hawas Elixir](/collections/rasasi) pairs mint and bergamot with dark chocolate and vanilla.

### Armaf and Al Haramain
[Armaf](/collections/armaf) covers Club de Nuit Intense and Precieux, the five Private Key extraits and the Miss Armaf florals. [Al Haramain](/collections/al-haramain) is famous for the Amber Oud editions and the fresher L'Aventure line.

### Maison Alhambra, Signature D'orient and more
[Maison Alhambra](/collections/maison-alhambra) offers a large range of 80ml and 100ml eaux de parfum at everyday prices, from Philos and Baroque to Narissa and Salvo. Signature D'orient bottles often come with a travel spray. For soft, sweet styles, try [Arabiyat Prestige](/collections/arabiyat-prestige) Nyla, Attar Collection, Inaaya and Adi Guru, and for oud, [Swiss Arabian](/collections/swiss-arabian) Shaghaf Oud Royale.

### How to choose
If you are new to Arabian perfume, start with a fresh or sweet scent such as 9am Dive or Yara Candy, then move to amber and oud. These scents are concentrated, so one or two sprays are usually enough. See also our [oud perfume](/collections/oud-perfume) page and the [amber fragrances](/collections/scent-amber) family. Every bottle is 100% authentic and ships from the UK, with free UK delivery on orders over £40.""")
HUB["oud-perfume"] = dict(
    kw="oud perfume",
    h2="Oud perfume from Arabian, niche and designer houses",
    desc="Oud perfume at Swansura UK: Al Haramain Amber Oud, Swiss Arabian, Montale, Tom Ford, Gucci and more, from under £20. Free UK delivery over £40.",
    explore_add=[["Swiss Arabian", "/collections/swiss-arabian"], ["Lattafa", "/collections/lattafa"], ["Afnan", "/collections/afnan"],
                 ["Armaf", "/collections/armaf"], ["Maison Alhambra", "/collections/maison-alhambra"], ["Rasasi", "/collections/rasasi"]],
    body="""Oud perfume is built around agarwood, a dark, resinous material with a smoky, woody depth that lasts for hours on skin. This edit brings together oud fragrances from Arabian, niche and designer houses, from {£min}, so you can find the style that suits you.

### Arabian oud
Al Haramain's Amber Oud family is the easiest way in: the [Gold Edition](/products/al-haramain-amber-oud-gold-edition-eau-de-parfum-luxury-unisex-fruity-amber-fragrance) is rich and sweet, Tobacco is warm and smoky, and Black is deep and bold. [Swiss Arabian Shaghaf Oud Royale](/products/swiss-arabian-shaghaf-oud-royale-eau-de-parfum-75ml) ({£swiss-arabian-shaghaf-oud-royale-eau-de-parfum-75ml}) softens oud with saffron, rose and praline, and Rihanah Ajwaa Oud is an easy, low-cost way to try the note. Fumeri and SAP pair oud with saffron.

### Niche and designer oud
Montale's Aoud Safran and Aoud Damascus blend oud with saffron and rose, Mancera Black Noir is dark and rich, and Tiziana Terenzi Caput Mundi and Gold Rose Oudh are concentrated extraits. From the designer houses, Gucci Intense Oud, Guerlain Oud Essentiel, Chopard Oud Malaki and [Tom Ford Oud Wood](/products/tom-ford-oud-wood-eau-de-parfum-50ml-unisex) are smoother takes on the note, and Franck Olivier's Parisian Oud and Sun Royal Oud are good-value options.

### More oud to explore
Several Arabian houses use oud inside sweeter blends: try [Afnan](/collections/afnan) Supremacy Gold, [Armaf](/collections/armaf) Club de Nuit Intense or [Lattafa](/collections/lattafa) for amber, coffee and spice. Oud is strong, so start with one or two sprays on the wrists or neck. Explore the [oud fragrances](/collections/scent-oud) family and our [Arabian perfume](/collections/arabian-perfume) page. Every bottle is 100% authentic and ships from the UK, with free UK delivery over £40.""")


BANNED = re.compile(r"\b(cure|treat|heal|acne|eczema|in stock|sold out|limited stock|official (uk )?partner|best[- ]selling|bestseller|clinically|guarantee)\b", re.I)


def fill(text, handle):
    prices = [float(x) for p in CAT[handle] for x in p["prices"]]

    def rep(m):
        k = m.group(1)
        if k == "min":
            return f"£{min(prices):.2f}"
        assert k in PRICE, (handle, k)
        return f"£{float(PRICE[k][0]):.2f}"
    return re.sub(r"\{£([a-z0-9-]+)\}", rep, text)


def to_html(md):
    out = []
    for para in md.strip().split("\n\n"):
        para = para.strip()
        if para.startswith("### "):
            head, _, para = para.partition("\n")
            out.append(f"<h3>{html.escape(head[4:], quote=False)}</h3>")
            if not para.strip():
                continue
        t = html.escape(para, quote=False)
        t = re.sub(r"\[([^\]]+)\]\((/[^)]+)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
        out.append(f"<p>{t}</p>")
    return "".join(out)


def check(handle, d, body_html):
    errs = []
    text = html.unescape(re.sub(r"<[^>]+>", " ", body_html))
    words = len(re.findall(r"[A-Za-zÀ-ÿ0-9£'’.-]+", text))
    kw = d["kw"].lower()
    first = html.unescape(re.sub(r"<[^>]+>", "", re.search(r"<p>(.*?)</p>", body_html).group(1))).split(". ")[0].lower()
    if not 150 <= words <= 380:
        errs.append(f"words {words}")
    if kw not in d["h2"].lower():
        errs.append("kw not in H2")
    if kw not in first:
        errs.append("kw not in first sentence")
    if len(d["desc"]) > 160:
        errs.append(f"desc {len(d['desc'])}")
    links = re.findall(r'href="([^"]+)"', body_html)
    if len(links) < 2:
        errs.append("links < 2")
    for l in links:
        kind, h = l.split("/")[1:3]
        if kind == "collections" and h not in COLL:
            errs.append(f"bad collection {h}")
        if kind == "products" and h not in PRICE and h not in ALLP:
            errs.append(f"bad product {h}")
    if BANNED.search(text) or BANNED.search(d["desc"]):
        errs.append(f"banned word {BANNED.search(text + d['desc']).group(0)}")
    return words, len(links), errs


ALLP = set()
if len(sys.argv) > 1:  # optional: storefront /products.json dump for link checks on older products
    ALLP = {p["handle"] for p in json.load(open(sys.argv[1]))}

rows, md, bad = [], ["# New brand pages: 'About this page' copy (draft, 6 Nov 2026)\n"], 0
ORDER = ["vera-wang", "david-beckham", "lattafa", "guess", "swiss-arabian", "jaguar", "rasasi", "tous", "afnan",
         "maison-alhambra", "arabiyat-prestige", "armaf", "formula-1", "franck-olivier", "armand-basi", "bois-1920",
         "mercedes-benz", "notebook", "attar-collection", "fomo", "adi-guru", "fun-basics", "inaaya",
         "natural-by-woods", "unlimited", "maison-de-milan", "chris-adams", "rihanah"]
assert set(ORDER) == set(B), set(B) ^ set(ORDER)
for h in ORDER:
    d = B[h]
    d["kw"] = CAT[h][0]["vendor"].replace("Fun & Basics", "Fun & Basics") + " perfume"
    if h == "david-beckham":
        d["kw"] = "David Beckham perfume"
    body = to_html(fill(d["body"], h))
    words, nlinks, errs = check(h, d, body)
    bad += bool(errs)
    rows.append({"handle": h, "id": f"gid://shopify/Collection/{IDS[h]}", "seo_description": d["desc"],
                 "seo_heading": d["h2"], "seo_copy": body, "faq_add": d["faq"], "others": d["others"],
                 "story": d.get("story"), "words": words, "links": nlinks, "errors": errs})
    md.append(f"\n## {d['kw']} — /collections/{h}\n\n*{words} words · {nlinks} links · meta description ({len(d['desc'])} chars):* {d['desc']}\n")
    if errs:
        md.append(f"\n**CHECK:** {', '.join(errs)}\n")
    md.append(f"\n**{d['h2']}**\n\n" + re.sub(r"<h3>(.*?)</h3>", r"\n**\1**\n\n", body).replace("<p>", "").replace("</p>", "\n\n"))
    md.append("\nExtra FAQs: " + " · ".join(f"*{q}* {a}" for q, a in d["faq"]) + "\n")
    md.append("\n'You may also love': " + ", ".join(o[0] for o in d["others"]) + "\n")

for h, d in HUB.items():
    body = to_html(fill(d["body"], h))
    words, nlinks, errs = check(h, d, body)
    bad += bool(errs)
    rows.append({"handle": h, "id": None, "seo_description": d["desc"], "seo_heading": d["h2"], "seo_copy": body,
                 "explore_add": d["explore_add"], "words": words, "links": nlinks, "errors": errs})
    md.append(f"\n## {d['kw']} (refresh) — /collections/{h}\n\n*{words} words · {nlinks} links · meta description ({len(d['desc'])} chars):* {d['desc']}\n")
    if errs:
        md.append(f"\n**CHECK:** {', '.join(errs)}\n")
    md.append(f"\n**{d['h2']}**\n\n" + re.sub(r"<h3>(.*?)</h3>", r"\n**\1**\n\n", body).replace("<p>", "").replace("</p>", "\n\n"))
    md.append("\nExplore pills added: " + ", ".join(e[0] for e in d["explore_add"]) + "\n")

with open(ROOT / "docs/seo/new_brand_copy_2026-11-06.jsonl", "w") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
open(ROOT / "docs/seo/new_brand_copy_2026-11-06.md", "w").write("".join(md))
for r in rows:
    print(f"{r['handle']:20} {r['words']:4}w {r['links']}l {r['errors'] or ''}")
print(len(rows), "pages,", bad, "with errors")

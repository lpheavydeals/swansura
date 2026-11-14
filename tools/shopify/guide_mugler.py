"""Journal guide 'Mugler perfume: Alien, Angel and Les Exceptions compared' (user, 15 Nov 2026: 'Write the next 2 Journal guides').

Semrush UK: mugler alien 6,600 (KD 25), mugler perfume 4,400 (KD 32), mugler angel 3,600 (KD 23), mugler angel nova 1,000
(KD 18). No Mugler guide yet; 12 of the 13 Mugler listings in stock on 15 Nov (storefront dump allp_map_1115c.json; the
Alien Goddess 30ml + 10ml set is sold out and linked in the text only).
Facts = each product's stored notes (custom.sw + description, Admin read 15 Nov 2026). Les Exceptions sit in our niche
perfume collection. No longevity / projection / 'dupe' / 'iconic' / 'most popular' wording, no launch dates or designer
history (not in our data). Prices are written into the text: re-run the generator and update the body if prices change.

Usage: python3 tools/shopify/guide_mugler.py <allp_map.json>   (handle -> storefront product)
Output: docs/seo/guide_mugler_2026-11-15.jsonl
"""
import json
import sys

from journal_lib import build

M = "mugler-"
A = {
    "title": "Mugler perfume: Alien, Angel and Les Exceptions compared",
    "handle": "mugler-perfume-guide",
    "tag": "Scent Studio",
    "summary": "The Mugler fragrances we stock, side by side: Alien and Alien Goddess, Angel, Angel Elixir and Angel Nova, Alien Man, the Les Exceptions collection and the 10ml colognes.",
    "mt": "Mugler Perfume: Alien, Angel and Les Exceptions | Swansura",
    "md": "Mugler Alien, Alien Goddess, Angel, Angel Elixir and Angel Nova compared: the notes, the sizes and which Mugler perfume to choose.",
    "pick": {
        "alien": M + "alien-eau-de-parfum-refillable",
        "supra": M + "alien-goddess-supra-florale-eau-de-parfum",
        "goddessset": M + "alien-goddess-eau-de-parfum-gift-set-30ml-10ml",
        "alienman": M + "alien-man-eau-de-toilette-body-shampoo-travel-set-100ml-50ml",
        "angel": M + "angel-eau-de-parfum-25ml",
        "elixir": M + "angel-elixir-eau-de-parfum-refillable-star",
        "nova": M + "angel-nova-eau-de-toilette-50ml",
        "wonder": M + "les-exceptions-wonder-bouquet-eau-de-parfum-80ml",
        "mystic": M + "les-exceptions-mystic-aromatic-eau-de-parfum-80ml",
        "blow": M + "cologne-blow-it-up-eau-de-toilette-10ml",
        "fly": M + "cologne-fly-away-eau-de-toilette-10ml",
        "heal": M + "cologne-heal-your-mind-eau-de-toilette-10ml",
        "love": M + "cologne-love-you-all-eau-de-toilette-10ml",
    },
    "titles": {},
    "soldout": ["goddessset"],
    "shop": ["alien", "supra", "angel", "elixir", "nova", "alienman", "wonder", "mystic"],
    "body": """<p>Mugler's fragrances fall into a few clear families: Alien, built around jasmine and amber; Angel, sweet and gourmand; the fresh Mugler Colognes; and the Les Exceptions collection. Here is every <strong>Mugler perfume</strong> we stock, with its notes, the sizes on offer and who each one suits.</p>
<h2>Mugler Alien: jasmine and white amber</h2>
<p>[[alien|Mugler Alien Eau de Parfum]] ({{alien}}, 30ml or 90ml, refillable) has just three notes: jasmine sambac, cashmeran wood and white amber. That short list makes it clear and easy to read on the skin: bright jasmine first, then a smooth, slightly powdery wood and a warm amber finish. It is a statement scent for evenings and colder weather.</p>
<p>[[supra|Alien Goddess Supra Florale Eau de Parfum]] ({{supra}}, 10ml, 60ml or 90ml) keeps the jasmine but makes it more floral: a cactus flower accord, jasmine grandiflorum and everlasting flower absolute. The original Alien Goddess (bergamot and coconut water, jasmine and heliotrope, over Bourbon vanilla and cashmeran) is in our [[goddessset|Alien Goddess gift set]], currently out of stock.</p>
<h3>Alien Man</h3>
<p>The [[alienman|Alien Man Eau de Toilette &amp; Body Shampoo Travel Set]] ({{alienman}}) pairs a refillable 100ml eau de toilette with a 50ml body shampoo. The scent opens with beech wood, dill, anise, lavender, lemon, mint and thyme, moves to leather, osmanthus, pepper and geranium, and dries down to white amber, cashmeran and vanilla: herbal at first, then warm and leathery.</p>
<h2>Mugler Angel: sweet and gourmand</h2>
<p>[[angel|Mugler Angel Eau de Parfum]] ({{angel}}, 25ml) is the dessert of the family. Cotton candy, coconut, cassis and fruit open it; honey, red berries, plum and flowers fill the heart; and patchouli, chocolate, caramel, vanilla and tonka bean make the base. The contrast between the sugary notes and the earthy patchouli is what gives it its character. A bold pick for winter nights and parties.</p>
<ul>
<li>[[elixir|Angel Elixir Eau de Parfum]] ({{elixir}}, 50ml or 100ml, refillable star bottle): pink pepper, then ylang-ylang, orange blossom, jasmine and sandalwood, over Bourbon vanilla and amber. More floral than Angel, with a warm, cosy finish.</li>
<li>[[nova|Angel Nova Eau de Toilette]] ({{nova}}, 50ml): lychee and bergamot, rose and magnolia, over akigalawood and amberwood. The lightest and fruitiest of the Angel scents, easy for daytime and spring.</li>
</ul>
<h2>Mugler Les Exceptions</h2>
<p>Les Exceptions is Mugler's collection of eau de parfums, both unisex and in 80ml bottles. You will also find them in our <a href="/collections/niche-perfume">niche perfume</a> edit.</p>
<ul>
<li>[[wonder|Les Exceptions Wonder Bouquet]] ({{wonder}}): shiso, lily of the valley, petitgrain, orange and tangerine, then brioche, jasmine sambac, tuberose, orange blossom and rose, over beeswax, hazelnut, vanilla and cashmeran. A rich floral with a soft, bakery-sweet edge.</li>
<li>[[mystic|Les Exceptions Mystic Aromatic]] ({{mystic}}): thyme, basil, clary sage and fig leaf, then grey amber, over Peru balsam and cedarwood. Green and herbal, with a resinous base.</li>
</ul>
<h2>Mugler Colognes: four 10ml minis</h2>
<p>The Mugler Colognes are fresh eau de toilettes in 10ml sprays at {{blow}} each, a low-cost way to try something new:</p>
<ul>
<li>[[blow|Blow It Up]]: sorbet, vetiver and black currant.</li>
<li>[[fly|Fly Away]]: grapefruit, a green cannabis accord and vetiver.</li>
<li>[[heal|Heal Your Mind]] (sold for men): lavender, hazelnut and vanilla.</li>
<li>[[love|Love You All]]: blue liquorice, white amber and musk.</li>
</ul>
<p>Small sizes like these make easy stocking fillers; our <a href="/blogs/journal/mini-perfume-sets-guide">mini perfume sets guide</a> has more ideas.</p>
<h2>Which Mugler perfume should you choose?</h2>
<ul>
<li><strong>You like warm, statement florals:</strong> Alien, or Alien Goddess Supra Florale for more flowers.</li>
<li><strong>You love sweet, dessert-like scents:</strong> Angel, or Angel Elixir for a more floral version.</li>
<li><strong>You want something light and fruity:</strong> Angel Nova.</li>
<li><strong>Buying for him:</strong> the Alien Man set.</li>
<li><strong>You like something different and unisex:</strong> Les Exceptions Wonder Bouquet or Mystic Aromatic.</li>
<li><strong>You want to try before you commit:</strong> a 10ml Mugler Cologne, or the 10ml Alien Goddess Supra Florale.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li><strong>Refillable bottles:</strong> Alien, Angel Elixir and the Alien Man eau de toilette come in bottles made to be refilled.</li>
<li><strong>Eau de parfum or eau de toilette?</strong> Our guide to <a href="/blogs/journal/extrait-vs-eau-de-parfum">extrait vs eau de parfum</a> explains the labels.</li>
<li><strong>As a gift:</strong> see our <a href="/blogs/journal/best-perfume-gift-sets-uk-2026">perfume gift sets guide</a> for more Christmas ideas.</li>
<li><strong>Every bottle is 100% authentic</strong> and dispatched from the UK, with free UK delivery over £40.</li>
</ul>
<p>Shop every <a href="/collections/mugler">Mugler</a> fragrance, or browse <a href="/collections/perfume-for-women">perfume for women</a> and <a href="/collections/scent-amber">amber fragrances</a>.</p>""",
    "faq": [
        ["What does Mugler Alien smell like?",
         "Mugler Alien has three notes: jasmine sambac, cashmeran wood and white amber. It opens with bright jasmine, then turns smooth, slightly powdery and warm. Alien Goddess Supra Florale is a more floral version, with a cactus flower accord, jasmine grandiflorum and everlasting flower absolute."],
        ["What is the difference between Mugler Angel, Angel Elixir and Angel Nova?",
         "Angel is the sweetest: cotton candy, fruit and honey over patchouli, chocolate, caramel and vanilla. Angel Elixir is more floral, with pink pepper, ylang-ylang, orange blossom and jasmine over vanilla and amber. Angel Nova is the lightest, with lychee, rose and magnolia over woods."],
        ["Is Mugler Alien refillable?",
         "Yes. We stock Mugler Alien Eau de Parfum in its refillable bottle, in 30ml and 90ml. Angel Elixir and the Alien Man eau de toilette also come in refillable bottles."],
        ["Are Mugler Les Exceptions unisex?",
         "Yes. Les Exceptions Wonder Bouquet and Mystic Aromatic are both unisex eau de parfums in 80ml bottles. Wonder Bouquet is a rich floral with brioche and hazelnut; Mystic Aromatic is green and herbal, with thyme, basil and fig leaf over Peru balsam and cedarwood."],
    ],
}

build(A, json.load(open(sys.argv[1])), "guide_mugler_2026-11-15.jsonl")

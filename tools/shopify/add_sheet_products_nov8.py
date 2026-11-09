"""Add the fragrances that are new in the client's 8 Nov 2026 sheet (user: "Balance Fragrances are Added in this Sheet …
what are the new fragrances which are not added in the store … add the products with the relevant SEO, H1s, meta …").

Input : docs/data/Swansura_Fragrance_Data_2026-11-08.xlsm ('Fragrance Catalogue', 821 rows) and the 2 Nov sheet.
        Rows whose name + size were already in the 2 Nov sheet are skipped (all of those were handled on 2 Nov).
        The other 147 rows are 20 brands with no product in Shopify at all (checked 8 Nov with Admin product search,
        all statuses, 780 products): Paco Rabanne, Salvatore Ferragamo, Mugler, Lalique, Narciso Rodriguez, Thomas
        Kosmala, Issey Miyake, Roberto Cavalli, Versace, Ralph Lauren, Moschino, Superdry, Grès, Michael Kors,
        Clinique, Lacoste, Lanvin, Rochas (+ 'Paco' = Paco Rabanne) and Rimmel (a lipstick: left out, not a fragrance).
Output: docs/seo/sheet_nov8_products_2026-11-08.json     productSet inputs (ACTIVE, tracked stock 0, client prices)
        docs/seo/sheet_nov8_collections_2026-11-08.json  collectionCreate inputs for the 18 new brand pages
        docs/seo/sheet_nov8_review_2026-11-08.md         review list (H1, title, description, sizes, prices, notes)
The client descriptions are mostly template text ('should be confirmed against the manufacturer's product
information', 'Please confirm the exact contents'), so the product text is written from the sheet's structured data
(name, type, size, gender, notes) instead. Families: the client's labels, with the overrides in FAM_FIX.
Run: python3 tools/shopify/add_sheet_products_nov8.py
"""
import json, re, html, pathlib, collections, unicodedata
import openpyxl
ROOT = pathlib.Path(__file__).resolve().parents[2]
LOC = 'gid://shopify/Location/111879553411'

def rows(p):
    wb = openpyxl.load_workbook(p, data_only=True)
    return [(i + 2, r) for i, r in enumerate(wb['Fragrance Catalogue'].iter_rows(min_row=2, values_only=True)) if any(r)]
key = lambda r: (str(r[6]).strip().lower(), str(r[9]).strip().lower())
OLD = {key(r) for _, r in rows(ROOT / 'docs/data/Swansura_Fragrance_Data_2026-11-02.xlsx')}
# FINAL sheet (client, 9 Nov 2026; adds an 'Alt Text' column, so size/price sit one column later). Same rows in the
# same order as the 8 Nov sheet; it changed only: Clinique 'Parfum Spray' -> 'Eau de Parfum', Phantom 'Parfum' ->
# 'Parfum Spray', Issey Eau & Magnolia + Wood & Wood prices (100ml/50ml swapped), Paco 4x10ml set contents.
NEW = {x: dict(brand=r[1], cat=r[2], gender=r[3], family=r[4], type=r[5], name=r[6], desc=r[7], notes=r[8], size=r[10],
               price=float(r[12])) for x, r in rows(ROOT / 'docs/data/Swansura_Fragrance_Data_2026-11-09_final.xlsx')
       if (str(r[6]).strip().lower(), str(r[10]).strip().lower()) not in OLD}
assert len(NEW) == 147, len(NEW)

# sheet row -> (H1, variant/size label). Rows with the same H1 become one product with a Size option.
T = {
 676: ('Clinique Aromatics Elixir Eau de Parfum', '100ml'),
 677: ('Grès Cabotine Turquoise Eau de Parfum', '100ml'),
 678: ('Grès Cabotine Rose Eau de Toilette & Body Lotion Gift Set', '100ml + 200ml'),
 679: ("Issey Miyake A Drop d'Issey Eau de Parfum Fraîche", '90ml'),
 680: ("Issey Miyake Le Sel d'Issey Eau de Toilette", '10ml'),
 681: ("Issey Miyake L'Eau d'Issey Eau de Toilette", '50ml'),
 682: ("Issey Miyake L'Eau d'Issey Eau & Magnolia Eau de Toilette Intense", '100ml'),
 683: ("Issey Miyake L'Eau d'Issey Eau & Magnolia Eau de Toilette Intense", '50ml'),
 684: ("Issey Miyake L'Eau d'Issey Pour Homme Eau de Toilette", '75ml'),
 685: ("Issey Miyake L'Eau d'Issey Pour Homme Eau de Toilette", '125ml'),
 686: ("Issey Miyake L'Eau d'Issey Pour Homme Wood & Wood Eau de Parfum Intense", '100ml'),
 687: ("Issey Miyake L'Eau d'Issey Pour Homme Wood & Wood Eau de Parfum Intense", '50ml'),
 688: ("Issey Miyake L'Eau d'Issey Pure Pétale de Nectar Eau de Toilette", '90ml'),
 689: ("Issey Miyake L'Eau d'Issey Rose & Rose Eau de Parfum Intense", '90ml'),
 690: ("Lacoste L'Homme Lacoste Deodorant Stick", '70g'),
 691: ('Lalique Amethyst Eau de Parfum', '100ml'),
 692: ('Lalique Amethyst Éclat Eau de Parfum', '100ml'),
 693: ('Lalique de Lalique Eau de Parfum', '100ml'),
 694: None,   # same set as 695 (listed twice, £29.99 and £31.99): the later row is used
 695: ("Lalique Hommage à l'Homme Eau de Toilette & Shower Gel Gift Set", '100ml + 150ml'),
 696: ("Lalique L'Amour Eau de Parfum", '100ml'),
 697: ('Lalique Le Parfum Eau de Parfum', '100ml'),
 698: ("Lalique L'Insoumis Eau de Toilette", '100ml'),
 699: ('Lalique Lion Eau de Parfum', '125ml'),
 700: ('Lalique Noir Premier Or Intemporel 1888 Eau de Parfum', '100ml'),
 701: ('Lalique Perles Eau de Parfum', '100ml'),
 702: ('Lalique Satine Eau de Parfum', '100ml'),
 703: ('Lalique White Eau de Toilette', '125ml'),
 704: ('Lanvin Mon Éclat Eau de Parfum Mini with Pouch', '7.5ml'),
 705: ('Michael Kors Pour Femme Eau de Parfum Miniature', '5ml'),
 706: ('Michael Kors Pour Homme Eau de Parfum Miniature', '5ml'),
 707: ('Moschino I Love Love Eau de Toilette Miniature', '4.9ml'),
 708: ('Moschino Toy Boy Eau de Parfum', '100ml'),
 709: ('Moschino Toy Boy Eau de Parfum', '5ml'),
 710: ('Mugler Alien Eau de Parfum Refillable', '30ml'),
 711: ('Mugler Alien Eau de Parfum Refillable', '90ml'),
 712: ('Mugler Alien Goddess Supra Florale Eau de Parfum', '90ml'),
 713: ('Mugler Alien Goddess Eau de Parfum Gift Set', '30ml + 10ml'),
 714: ('Mugler Alien Goddess Supra Florale Eau de Parfum', '10ml'),
 715: ('Mugler Alien Goddess Supra Florale Eau de Parfum', '60ml'),
 716: ('Mugler Alien Man Eau de Toilette & Body Shampoo Travel Set', '100ml + 50ml'),
 717: ('Mugler Angel Eau de Parfum', '25ml'),
 718: ('Mugler Angel Elixir Eau de Parfum Refillable Star', '100ml'),
 719: ('Mugler Angel Elixir Eau de Parfum Refillable Star', '50ml'),
 720: ('Mugler Angel Nova Eau de Toilette', '50ml'),
 721: ('Mugler Cologne Blow It Up Eau de Toilette', '10ml'),
 722: ('Mugler Cologne Fly Away Eau de Toilette', '10ml'),
 723: ('Mugler Cologne Heal Your Mind Eau de Toilette', '10ml'),
 724: ('Mugler Cologne Love You All Eau de Toilette', '10ml'),
 725: ('Mugler Les Exceptions Mystic Aromatic Eau de Parfum', '80ml'),
 726: ('Mugler Les Exceptions Wonder Bouquet Eau de Parfum', '80ml'),
 727: ('Narciso Rodriguez For Her Eau de Toilette', '100ml'),
 728: ('Narciso Rodriguez All of Me Eau de Parfum', '90ml'),
 729: ('Narciso Rodriguez For Her Eau de Parfum', '10ml'),
 730: ('Narciso Rodriguez For Her Eau de Parfum', '50ml'),
 731: ('Narciso Rodriguez For Her Eau de Toilette', '50ml'),
 732: ('Narciso Rodriguez For Him Bleu Noir Eau de Toilette', '50ml'),
 733: ('Narciso Rodriguez Musc Noir For Her Eau de Parfum', '10ml'),
 734: ('Narciso Rodriguez Musc Noir For Her Eau de Parfum', '50ml'),
 735: ('Narciso Rodriguez Musc Noir Rose For Her Eau de Parfum', '10ml'),
 736: ('Narciso Rodriguez Narciso Ambrée Eau de Parfum', '10ml'),
 737: ('Narciso Rodriguez Narciso Cristal Eau de Parfum', '10ml'),
 738: ('Narciso Rodriguez Pure Musc For Her Eau de Parfum', '10ml'),
 739: ("Paco Rabanne Women's Miniature Set (Lady Million, Olympéa, Fame)", '5ml + 6ml + 4ml + 4ml'),
 740: ('Paco Rabanne 1 Million Eau de Toilette', '200ml'),
 741: ('Paco Rabanne Fame Eau de Parfum Refillable', '80ml'),
 742: ('Paco Rabanne Fame Eau de Parfum Intense', '30ml'),
 743: ('Paco Rabanne Fame Eau de Parfum Gift Set', '50ml + 10ml'),
 744: ('Paco Rabanne Fame Eau de Parfum & Parfum Mini Set', '4ml + 4ml'),
 745: ('Paco Rabanne Fame Parfum', '10ml'),
 746: ('Paco Rabanne Miniature Eau de Parfum Set', '8 x 2ml'),
 747: ('Paco Rabanne Invictus Eau de Toilette', '200ml'),
 748: ('Paco Rabanne Invictus Eau de Toilette Gift Set', '200ml + 10ml'),
 749: ('Paco Rabanne Invictus Eau de Toilette & Deodorant Gift Set', '100ml + 150ml + 10ml'),
 750: ('Paco Rabanne Invictus Victory Eau de Parfum Extrême', '100ml'),
 751: ('Paco Rabanne Lady Million Eau de Parfum', '15ml'),
 752: ('Paco Rabanne Lady Million Royal Eau de Parfum', '30ml'),
 753: ("Paco Rabanne Men's Miniature Set (Phantom, Invictus, 1 Million Elixir, 1 Million)", '4 x 5ml'),
 754: ("Paco Rabanne Men's Miniature Eau de Toilette Set (1 Million, Invictus, Phantom)", '3 x 4ml'),
 755: ('Paco Rabanne Olympéa Flora Eau de Parfum Intense', '80ml'),
 756: ('Paco Rabanne Phantom Parfum & Deodorant Gift Set', '100ml + 150ml + 10ml'),
 757: ('Paco Rabanne Phantom Eau de Toilette & Deodorant Gift Set', '100ml + 150ml + 10ml'),
 758: None,   # exact repeat of 757
 759: ('Paco Rabanne Phantom Parfum Spray', '15ml'),
 760: ('Paco Rabanne Ultraviolet Eau de Parfum', '80ml'),
 761: ('Paco Rabanne XS Black Eau de Toilette', '100ml'),
 762: ("Paco Rabanne Women's Miniature Eau de Parfum Gift Set (Lady Million, Olympéa)", '4 x 10ml'),
 763: ('Ralph Lauren Polo Cologne Intense', '59ml'),
 764: ('Ralph Lauren Polo Blue Eau de Toilette Refillable', '75ml'),
 765: ('Ralph Lauren Polo Red Eau de Toilette Refillable', '125ml'),
 766: ('Ralph Lauren Polo Red Parfum', '75ml'),
 767: ('Superdry Real Fragrance 01 Feminin Eau de Toilette', '100ml'),
 768: ('Superdry Real Fragrance 02 Feminin Eau de Toilette', '100ml'),
 769: ('Superdry Real Fragrance 02 Masculin Eau de Toilette', '100ml'),
 770: None,   # Rimmel liquid lipstick: not a fragrance
 771: ('Roberto Cavalli Florence Eau de Parfum', '50ml'),
 772: ('Roberto Cavalli Florence Eau de Parfum', '75ml'),
 773: ('Roberto Cavalli Gold Collection Bloodiris Eau de Parfum', '100ml'),
 774: ('Roberto Cavalli Just Cavalli Eau de Toilette for Her', '30ml'),
 775: ('Roberto Cavalli Paradiso Eau de Parfum', '100ml'),
 776: ('Roberto Cavalli Paradiso Assoluto Eau de Parfum', '100ml'),
 777: ('Roberto Cavalli Uomo Eau de Toilette', '100ml'),
 778: ('Roberto Cavalli Uomo Parfum', '100ml'),
 779: ('Rochas Girl Life Eau de Parfum', '40ml'),
 780: ('Salvatore Ferragamo Bright Leather Eau de Toilette Gift Set', '100ml + 10ml + 100ml'),
 781: ('Salvatore Ferragamo Intense Leather Eau de Parfum Gift Set', '100ml + 10ml + 100ml'),
 782: ('Salvatore Ferragamo Incanto Shine Eau de Toilette', '50ml'),
 783: ('Salvatore Ferragamo Pour Femme Eau de Parfum', '100ml'),
 784: ('Salvatore Ferragamo Signorina Eau de Toilette', '100ml'),
 785: ('Salvatore Ferragamo Signorina Eleganza Eau de Parfum', '100ml'),
 786: ('Salvatore Ferragamo Signorina In Fiore Eau de Toilette', '100ml'),
 787: ('Salvatore Ferragamo Signorina Ribelle Eau de Parfum', '100ml'),
 788: ('Salvatore Ferragamo Signorina Ribelle Eau de Parfum', '10ml'),
 789: ('Salvatore Ferragamo Signorina Ribelle Eau de Parfum', '20ml'),
 802: ('Salvatore Ferragamo Uomo Eau de Toilette', '100ml'),
 803: ('Thomas Kosmala Exsupero Eau de Parfum', '100ml'),
 804: ('Thomas Kosmala No. 10 Desire du Coeur Eau de Parfum', '100ml'),
 805: ('Thomas Kosmala No. 10 Desire du Coeur Elixir Eau de Parfum', '100ml'),
 806: ("Thomas Kosmala No. 4 Après l'Amour Parfum & Hair Mist Travel Kit", '30ml + 30ml'),
 807: ('Thomas Kosmala No. 4 Candy Eau de Parfum', '100ml'),
 808: ('Thomas Kosmala No. 4 Neon Eau de Parfum', '100ml'),
 809: ('Thomas Kosmala No. 4 Sport Eau de Parfum', '100ml'),
 810: ('Thomas Kosmala No. 9 Bukhoor Elixir de Parfum', '100ml'),
 811: ('Thomas Kosmala No. 1 A Never Ending Love Eau de Parfum', '100ml'),
 812: ('Thomas Kosmala No. 12 Oud Douze Eau de Parfum', '100ml'),
 813: ('Thomas Kosmala Star Chaser Eau de Parfum', '100ml'),
 814: ('Thomas Kosmala Wild Stride Eau de Parfum', '100ml'),
 815: ('Versace Dylan Blue Pour Homme Eau de Toilette Miniature', '5ml'),
 816: ('Versace Eros Eau de Toilette', '200ml'),
 817: ('Versace Eros Parfum', '100ml'),
 818: ('Versace Eros Parfum', '200ml'),
 819: ('Versace Eros Pour Femme Eau de Parfum', '100ml'),
 820: ('Versace Eros Pour Femme Eau de Toilette Miniature', '5ml'),
 821: ('Versace Man Eau Fraîche Eau de Toilette Miniature', '5ml'),
 822: ('Versace Yellow Diamond Eau de Toilette', '90ml'),
}
for x, n in zip(range(790, 802), ['Arte Orafa', 'Bianco di Carrara', 'E Pur Si Muove', 'Gentil Suono', 'La Commedia', 'La Corte',
                                    'Orto delle Spezie', 'Punta Ala', 'Rinascimento', 'Terra Rossa', 'Vendemmia', 'Viola Essenziale']):
    T[x] = (f'Salvatore Ferragamo Tuscan Creations {n} Eau de Parfum', '100ml')
assert set(T) == set(NEW), sorted(set(NEW) ^ set(T))
for x, v in T.items():
    if v:
        assert NEW[x]['brand'].split()[0].lower() in v[0].lower() or x == 767 or NEW[x]['brand'] in ('Gres', 'Real Superdry'), (x, v)

BRAND = {'Paco': 'Paco Rabanne', 'Gres': 'Grès', 'Real Superdry': 'Superdry'}
# set contents, written from the set names in the client sheet ('Sg' = shower gel)
SETS = {
 678: ['Cabotine Rose eau de toilette 100ml', 'Perfumed body lotion 200ml'],
 695: ["Hommage à l'Homme eau de toilette 100ml", 'Shower gel 150ml'],
 704: ['Mon Éclat eau de parfum 7.5ml spray', 'Mini pouch'],
 713: ['Alien Goddess eau de parfum 30ml', 'Alien Goddess eau de parfum 10ml'],
 716: ['Alien Man eau de toilette 100ml (refillable)', 'Body shampoo 50ml'],
 739: ['Lady Million eau de parfum 5ml', 'Olympéa eau de parfum 6ml', 'Fame eau de parfum 4ml', 'Fame parfum 4ml'],
 743: ['Fame eau de parfum 50ml', 'Fame eau de parfum 10ml'],
 744: ['Fame eau de parfum 4ml splash', 'Fame parfum 4ml splash'],
 746: ['Mesh Metal eau de parfum 2ml', 'Silver Skin eau de parfum 2ml', 'Midnight Sex eau de parfum 2ml', 'Rose 1969 eau de parfum 2ml',
       'Night Soul eau de parfum 2ml', 'Armure Mara eau de parfum 2ml', 'After Club eau de parfum 2ml', 'Oud Montaigne eau de parfum 2ml'],
 748: ['Invictus eau de toilette 200ml', 'Invictus eau de toilette 10ml'],
 749: ['Invictus eau de toilette 100ml spray', 'Deodorant spray 150ml', 'Invictus eau de toilette 10ml spray'],
 753: ['Phantom eau de toilette 5ml', 'Invictus eau de toilette 5ml', '1 Million Elixir 5ml', '1 Million eau de toilette 5ml'],
 754: ['1 Million eau de toilette 4ml', 'Invictus eau de toilette 4ml', 'Phantom eau de toilette 4ml'],
 756: ['Phantom 100ml spray', 'Deodorant spray 150ml', 'Phantom 10ml spray'],
 757: ['Phantom eau de toilette 100ml', 'Deodorant spray 150ml', 'Phantom eau de toilette 10ml'],
 762: ['Lady Million eau de parfum 10ml', 'Lady Million Fabulous eau de parfum 10ml', 'Olympéa eau de parfum 10ml', 'Olympéa Blossom eau de parfum 10ml'],
 780: ['Bright Leather eau de toilette 100ml', 'Bright Leather eau de toilette 10ml', 'Shower gel 100ml'],
 781: ['Intense Leather eau de parfum 100ml', 'Intense Leather eau de parfum 10ml', 'Shampoo & shower gel 100ml'],
 806: ["Après l'Amour parfum 30ml", "Après l'Amour hair mist 30ml"],
}
FAM = {'woody': 'woody', 'amber': 'amber', 'floral': 'floral', 'fruity': 'floral', 'citrus': 'fresh', 'aquatic': 'fresh', 'aromatic': 'fresh'}
FAM_FIX = {796: 'amber',   # Orto delle Spezie: dates, saffron, nutmeg (sheet: Aquatic)
           795: 'floral',  # La Corte: jasmine, almond milk, freesia (sheet: Aromatic)
           821: 'fresh',   # Versace Man Eau Fraîche (sheet: Floral)
           765: 'woody',   # Polo Red EDT, men (sheet: Fruity)
           807: 'amber',   # Kosmala No. 4 Candy, gourmand (sheet: Fruity)
           812: 'oud'}     # 'Oud' in the name stays oud (store rule)
NICHE = ('Thomas Kosmala', 'Tuscan Creations', 'Les Exceptions', 'Gold Collection')
LINE = {'Paco Rabanne': 'Parisian designer fragrances', 'Salvatore Ferragamo': 'Italian designer fragrances',
        'Mugler': 'Parisian designer fragrances', 'Lalique': 'French crystal-house fragrances', 'Narciso Rodriguez': 'Musk-led designer fragrances',
        'Thomas Kosmala': 'Niche eaux de parfum', 'Issey Miyake': 'Japanese designer fragrances', 'Roberto Cavalli': 'Italian designer fragrances',
        'Versace': 'Italian designer fragrances', 'Ralph Lauren': 'American designer fragrances', 'Moschino': 'Italian designer fragrances',
        'Superdry': 'Everyday fragrances', 'Grès': 'French fragrances', 'Michael Kors': 'American designer fragrances',
        'Clinique': 'Classic fragrances', 'Lacoste': 'Fragrances and grooming for men', 'Lanvin': 'Parisian fragrances',
        'Rochas': 'Parisian fragrances'}
OTHERS = [['Dior', '/collections/dior', 'Iconic French fragrances', None], ['Gucci', '/collections/gucci', 'Italian designer fragrances', None],
          ['Yves Saint Laurent', '/collections/yves-saint-laurent', 'Parisian designer fragrances', None],
          ['Giorgio Armani', '/collections/giorgio-armani', 'Italian designer fragrances', None],
          ['Carolina Herrera', '/collections/carolina-herrera', 'Designer fragrances', None],
          ['Calvin Klein', '/collections/calvin-klein', 'Designer fragrances', None]]

def handleize(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = s.replace('&', ' ').replace("'", '')
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s)).strip('-')
def esc(s): return html.escape(str(s or '').strip(), quote=False)
def price_band(p): return 'price-0-15' if p < 15 else 'price-15-25' if p < 25 else 'price-25-50' if p < 50 else 'price-50-9999'
def ml(s): return [float(v) for v in re.findall(r'(\d+(?:\.\d+)?)\s*ml', s)]
def sz_sort(s): return (ml(s) or [0])[0]

def notes_html(sc):
    if not sc:
        return ''
    out = '<h3>Scent notes</h3>'
    for part in str(sc).split('||'):
        m = re.match(r'\s*([^:|]+?):\s*(?=Top Notes)', part)
        if m:
            out += f'<h4>{esc(m.group(1))}</h4>'
            part = part[m.end():]
        out += '<ul>' + ''.join(f'<li>{esc(p)}</li>' for p in part.split('|') if p.strip()) + '</ul>'
    return out

def kind_of(h1):
    for k, w in (('Elixir de Parfum', 'elixir de parfum'), ('Eau de Parfum', 'eau de parfum'), ('Eau de Toilette', 'eau de toilette'),
                 ('Parfum Spray', 'parfum'), ('Parfum', 'parfum'), ('Cologne', 'cologne'), ('Deodorant', 'deodorant stick')):
        if k in h1:
            return w
    return 'fragrance'

groups = collections.OrderedDict()
for x in sorted(T):
    if T[x]:
        groups.setdefault(T[x][0], []).append(x)
TAKEN = set()
products, brand_count, review = [], collections.Counter(), []
rank = 900
for h1, xs in groups.items():
    rs = [dict(NEW[x], xl=x, label=T[x][1]) for x in xs]
    rs.sort(key=lambda r: sz_sort(r['label']))
    r0 = next(r for r in rs if r['xl'] == xs[0])
    brand = BRAND.get(r0['brand'], r0['brand'])
    g = {'Men': 'Men', 'Women': 'Women'}.get(r0['gender'], 'Unisex')
    if xs[0] == 762:   # sheet says Unisex, but all four scents in the final sheet's contents are women's
        g = 'Women'
    fam = FAM_FIX.get(xs[0]) or FAM.get(str(r0['family'] or '').lower())
    gift = xs[0] in SETS
    deo = 'Deodorant Stick' in h1
    multi = len(rs) > 1
    sizes = [r['label'] for r in rs]
    title = h1 if multi else f'{h1} {sizes[0]}'
    handle = handleize(title)
    assert handle not in TAKEN, handle
    TAKEN.add(handle)
    pmin = min(r['price'] for r in rs)
    kind = 'deodorant stick' if deo else ('fragrance gift set' if gift else kind_of(h1))
    gword = {'Men': 'for men', 'Women': 'for women'}.get(g, 'for everyone (unisex)')
    art = 'An' if (fam or kind)[0] in 'aeiou' else 'A'
    fam_w = (fam + ' ') if fam else ''
    if gift:
        intro = f'<p>{esc(h1)} is {art.lower()} {fam_w}{kind} {gword} from {esc(brand)}.</p><h3>In the set</h3><ul>' + \
                ''.join(f'<li>{esc(i)}</li>' for i in SETS[xs[0]]) + '</ul>'
    else:
        refill = ' The bottle is refillable.' if 'Refillable' in h1 else ''
        intro = f'<p>{esc(h1)} is {art.lower()} {fam_w}{kind} {gword} from {esc(brand)}, in {esc(" and ".join(sizes) if multi else sizes[0])}.{refill}</p>'
    notes = r0['notes'] or next((r['notes'] for r in rs if r['notes']), None)
    desc = intro + notes_html(notes) + '<h3>Details</h3><ul>' + \
        (f'<li>Size: {esc(", ".join(sizes))}</li>' if not gift else f'<li>Set size: {esc(sizes[0])}</li>') + \
        f"<li>{'Made for men' if g == 'Men' else 'Made for women' if g == 'Women' else 'Unisex: for men and women'}</li>" + \
        f'<li>Brand: {esc(brand)}</li><li>100% authentic, dispatched from the UK</li></ul>'
    # ---- SEO (same format as the 2 Nov products: '… | Swansura UK' ≤60, 'Buy … for £X at Swansura UK …' ≤160)
    short = h1.replace('Eau de Parfum', 'EDP').replace('Eau de Toilette', 'EDT')
    short = re.sub(r'\s*\(.*?\)', '', short)
    sz_ = '' if multi else f' {sizes[0]}'
    cands = [f'{h1}{sz_} | Swansura UK', f'{h1}{sz_} | Swansura', f'{short}{sz_} | Swansura', f'{h1} | Swansura', f'{short} | Swansura',
             f"{short.replace('Salvatore Ferragamo', 'Ferragamo')}{sz_} | Swansura", f"{short.replace('Salvatore Ferragamo', 'Ferragamo')} | Swansura"]
    s2 = short
    for a, b in (("Issey Miyake L'Eau d'Issey", "L'Eau d'Issey"), ('Salvatore Ferragamo', 'Ferragamo'), ('Miniature Set', 'Mini Set'),
                 ('Eau de Toilette', 'EDT'), ('Eau de Parfum', 'EDP'), (' & Deodorant', ''), (' & Body Shampoo', ''), (' & Shower Gel', ''), (' & Hair Mist', ''), (' & Body Lotion', ''), (' Parfum Travel Kit', ' Travel Kit')):
        s2 = s2.replace(a, b)
        cands += [f'{s2}{sz_} | Swansura', f'{s2} | Swansura']
    seo_t = next((c for c in cands if len(c) <= 60), None)
    assert seo_t, (h1, cands)
    gw = {'Men': "men's", 'Women': "women's"}.get(g, 'unisex')
    price_txt = f'from £{pmin:.2f}' if multi and len({r["price"] for r in rs}) > 1 else f'for £{pmin:.2f}'
    name_txt = f'{h1} ({", ".join(sizes)})' if multi else f'{h1}{sz_}'
    def D(nm, tail):
        return f'Buy {nm} {price_txt} at Swansura UK. {art} {fam_w}{gw} {kind}.{tail}'.replace("'", '’')
    dc = [D(name_txt, ' 100% authentic, fast UK delivery, free over £40.'), D(name_txt, ' 100% authentic, free UK delivery over £40.'),
          D(h1, ' 100% authentic, free UK delivery over £40.'), D(name_txt, ' 100% authentic.'), D(h1, ' 100% authentic.'), D(short, ' 100% authentic.')]
    seo_d = next((c for c in dc if len(c) <= 158), None)
    assert seo_d, (h1, [len(c) for c in dc])
    # ---- collections
    colls = ['fragrance', handleize(brand), price_band(pmin)]
    if not deo:
        colls.append({'Men': 'perfume-for-men', 'Women': 'perfume-for-women', 'Unisex': 'unisex-perfume'}[g])
    if fam:
        colls.append('scent-' + fam)
    if fam == 'oud':
        colls.append('oud-perfume')
    if any(n in h1 for n in NICHE):
        colls.append('niche-perfume')
    if gift:
        colls += ['perfume-gift-sets', 'sets-combos', 'christmas-gifts']
        colls += {'Men': ['gifts-for-him'], 'Women': ['gifts-for-her']}.get(g, ['gifts-for-her', 'gifts-for-him'])
        colls.append('gifts-under-25' if pmin < 25 else 'gifts-25-to-50' if pmin < 50 else 'gifts-over-50')
    if deo:
        colls.append('deodrants')
    if (gift and max(ml(sizes[0]) or [99]) <= 15) or (not gift and any((ml(s) or [99])[0] <= 15 for s in sizes)):
        colls.append('travel-size-minis')
    colls = list(dict.fromkeys(colls))
    # ---- variants
    variants = [{'optionValues': [{'optionName': 'Size' if multi else 'Title', 'name': r['label'] if multi else 'Default Title'}],
                 'price': f"{r['price']:.2f}", 'inventoryItem': {'tracked': True},
                 'inventoryQuantities': [{'locationId': LOC, 'name': 'available', 'quantity': 0}]} for r in rs]
    options = [{'name': 'Size', 'values': [{'name': s} for s in sizes]}] if multi else [{'name': 'Title', 'values': [{'name': 'Default Title'}]}]
    type_chip = 'Gift set' if gift else 'Deodorant' if deo else {'eau de parfum': 'Eau de Parfum', 'eau de toilette': 'Eau de Toilette',
                                                                  'parfum': 'Parfum', 'elixir de parfum': 'Parfum', 'cologne': 'Cologne'}.get(kind, 'Fragrance')
    chips = ([fam.capitalize() + ' family'] if fam else []) + [{'Men': 'For men', 'Women': 'For women'}.get(g, 'Unisex'), type_chip]
    top = ''
    if notes:
        m = re.search(r'Top Notes:\s*([^|]+)', str(notes))
        top = m.group(1).strip() if m else ''
    sw = {'t': {'Men': 'For him', 'Women': 'For her'}.get(g, 'Unisex'), 's': [], 'c': [], 'k': False, 'r': rank, 'f': fam,
          'w': {'Men': 'For him', 'Women': 'For her'}.get(g, 'Unisex'), 'n': None,
          'a': [f"{'An' if (fam or 's')[0] in 'aeiou' else 'A'} {fam or 'signature'} fragrance{': ' + top if top else ''}."]}
    pdp = {'cat': 'fragrance', 'ben': '', 'more': False, 'chips': chips, 'how': [],
           'pair': ['deyga-chocolate-body-butter-100g', 'somali-frankincense-sleep-pillow-spray-overactive-mind-anatome'], 'sim': [],
           'kw': [[{'Men': 'Perfume for men', 'Women': 'Perfume for women'}.get(g, 'Unisex perfume'),
                   '/collections/' + {'Men': 'perfume-for-men', 'Women': 'perfume-for-women'}.get(g, 'unisex-perfume')]] +
                 ([['Perfume gift sets', '/collections/perfume-gift-sets']] if gift else [])}
    rank += 1
    brand_count[brand] += 1
    mf = lambda k, t, v: {'namespace': 'custom', 'key': k, 'type': t, 'value': v}
    products.append(dict(rows=xs, brand=brand, gender=g, handle=handle, colls=colls, input={
        'title': title, 'handle': handle, 'status': 'ACTIVE', 'vendor': brand, 'productType': 'Fragrance',
        'tags': ['Fragrance', 'New 2026-11', 'Photo pending'] + (['Gift set'] if gift else []),
        'descriptionHtml': desc, 'seo': {'title': seo_t, 'description': seo_d},
        'productOptions': options, 'variants': variants,
        'metafields': [mf('h1', 'single_line_text_field', h1), mf('sw', 'json', json.dumps(sw, ensure_ascii=False)),
                       mf('pdp', 'json', json.dumps(pdp, ensure_ascii=False))]}))
    review.append(dict(rows=xs, h1=h1, title=title, seo_t=seo_t, seo_d=seo_d, sizes=sizes, prices=[r['price'] for r in rs], fam=fam,
                       client_fam=r0['family'], g=g, colls=colls))
# similar: same brand, same gender first
for p in products:
    same = [q['handle'] for q in products if q['brand'] == p['brand'] and q['handle'] != p['handle']]
    sim = sorted(same, key=lambda h: next(q['gender'] for q in products if q['handle'] == h) != p['gender'])[:4]
    for m in p['input']['metafields']:
        if m['key'] == 'pdp':
            d = json.loads(m['value']); d['sim'] = sim; m['value'] = json.dumps(d, ensure_ascii=False)

newcolls = []
for brand, n in sorted(brand_count.items()):
    h = handleize(brand)
    word = 'Deodorant' if brand == 'Lacoste' else 'Perfume'
    seo_t = f'{brand} {word} | Shop at Swansura UK'
    seo_d = f'Shop {brand} {word.lower()} at Swansura: {n} product{"s" if n > 1 else ""}, 100% authentic and shipped from the UK. Free UK delivery over £40.'
    assert len(seo_t) <= 60 and len(seo_d) <= 158, (seo_t, seo_d)
    bj = {'name': brand, 'world': 'scent', 'partner': False, 'line': LINE[brand],
          'story': f'{brand} at Swansura: {n} product{"s" if n > 1 else ""}, 100% authentic and shipped from the UK.', 'count': n,
          'others': OTHERS[:5]}
    faq = [[f'Is {brand} at Swansura genuine?', f'Yes. Every {brand} product at Swansura is 100% authentic and ships from the UK.'],
           [f'How fast is {brand} delivery?', f'All {brand} orders ship from Swansura in the UK. UK delivery is free on orders over £40, and orders over £70 also get £5 off.']]
    mf = lambda k, t, v: {'namespace': 'custom', 'key': k, 'type': t, 'value': v}
    newcolls.append(dict(handle=h, input={'title': brand, 'handle': h, 'sortOrder': 'MANUAL', 'seo': {'title': seo_t, 'description': seo_d},
                     'metafields': [mf('h1', 'single_line_text_field', f'{brand} {word}'), mf('brand', 'json', json.dumps(bj, ensure_ascii=False)),
                                    mf('faq', 'json', json.dumps(faq, ensure_ascii=False))]}))
json.dump(products, open(ROOT / 'docs/seo/sheet_nov8_products_2026-11-08.json', 'w'), ensure_ascii=False, indent=1)
json.dump(newcolls, open(ROOT / 'docs/seo/sheet_nov8_collections_2026-11-08.json', 'w'), ensure_ascii=False, indent=1)
with open(ROOT / 'docs/seo/sheet_nov8_review_2026-11-08.md', 'w') as f:
    f.write(f'# New fragrances from the 8 Nov 2026 client sheet\n\n{len(products)} products from 144 sheet rows '
            f'(147 new rows − 1 duplicate set − 1 repeated row − Rimmel lipstick), {len(newcolls)} new brand pages.\n\n')
    f.write('| Sheet rows | H1 | Sizes / prices | Family | For | SEO title | SEO description |\n|---|---|---|---|---|---|---|\n')
    for r in review:
        f.write(f"| {', '.join(map(str, r['rows']))} | {r['h1']} | {', '.join(f'{s} £{p:.2f}' for s, p in zip(r['sizes'], r['prices']))} | "
                f"{r['fam'] or '–'} (sheet: {r['client_fam']}) | {r['g']} | {r['seo_t']} | {r['seo_d']} |\n")
print(len(products), 'products;', len(newcolls), 'brand collections;', collections.Counter(len(p['rows']) for p in products))

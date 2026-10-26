"""Build theme/templates/index.json (homepage) + header/footer groups for the Swansura theme.

Content comes from the approved prototype (prototype/products.json, prototype/seocopy.js) and the store's
real collections. Prototype routes that have no Shopify collection yet link to a product search until the
collections are created. Run from the repo root:  python3 tools/theme/build_home.py
"""
import json, re, subprocess, html

P = json.load(open('prototype/products.json'))
def find(rx):
    for p in P:
        if re.search(rx, p['title'], re.I) and p['available']: return p['h']
def handles(keys): return [h for h in dict.fromkeys(find(k) for k in keys) if h]

COLL = {'c-skincare': 'skincare', 'c-haircare': 'haircare', 'c-bath-body': 'bodycare', 'c-fragrance': 'fragrance',
        'c-gifts': 'sets-combos', 'c-all': 'all', 'b-deyga': 'milk-drop-brightening-serum-1', 'b-vilvah': 'milk-drop-brightening-serum',
        'b-tiziana-terenzi': 'tiziana-terenzi', 'b-al-haramain': 'al-haramain', 'b-gucci': 'gucci', 'b-hemel': 'hemel-h',
        'b-jo-milano': 'luxury-collection-1', 'b-signature-d-orient': 'signature-sillage-dorient', 'b-dolce-gabbana': 'dolce-gabbana',
        'b-calvin-klein': 'calvin-klein', 'b-chloe': 'chloe'}
def url(route):
    if route in COLL: return f"/collections/{COLL[route]}"
    m = re.match(r'(k|concern|scent|range|price|b)-(.+)', route)
    if m: return '/search?type=product&q=' + m.group(2).replace('-', '+')
    if route.startswith('p-'):
        p = next((x for x in P if x['id'] == route[2:]), None); return f"/products/{p['h']}" if p else '/collections/all'
    return {'rituals': '/collections/sets-combos', 'brands': '/collections', 'journal': '/blogs/news', 'advent': '/collections/sets-combos'}.get(route, '/')
def md(t):  # prototype copy: [text](#route) -> HTML link
    t = html.escape(t, quote=False)
    return re.sub(r'\[([^\]]+)\]\(#([^)]+)\)', lambda m: f'<a href="{url(m.group(2))}">{m.group(1)}</a>', t)

copy = json.loads(subprocess.run(['node', '-e', 'global.window={};require("vm").runInThisContext(require("fs").readFileSync("prototype/seocopy.js","utf8"));process.stdout.write(JSON.stringify(window.SW_COPY.home))'], capture_output=True, text=True).stdout)
seo_body = ''.join((f"<h3>{html.escape(b['h3'])}</h3>" if b.get('h3') else '') + f"<p>{md(b['p'])}</p>" for b in copy['blocks'])

skin = handles(['beetroot lip balm', 'charcoal face wash', 'milk drops', 'sunscreen', 'hyaluronic', 'goat milk shampoo', 'hair growth oil', 'ultra moisturising'])
scent = handles(['amber oud ruby', 'kaff', 'gold rose oudh', 'rosado', 'santal', 'intense oud', 'ambre night', 'amber oud bleu'])
byid = {p['id']: p['h'] for p in P}
xmas = [byid[i] for i in ['16303208038787', '16368958308739', '16372985856387']]

def tiles(name, heading, style, items, link=None, count=False, band=False):
    blocks, order = {}, []
    for i, it in enumerate(items):
        k = f"tile_{i}"; order.append(k)
        title, sub, coll, link_ = (list(it) + [None] * 4)[:4]
        s = {'title': title}
        if sub: s['subtitle'] = sub
        if coll: s['collection'] = coll
        if link_: s['link'] = link_
        blocks[k] = {'type': 'tile', 'settings': s}
    st = {'heading': heading, 'style': style, 'show_count': count, 'band': band}
    if link: st.update(link_label=link[0], link_url=link[1])
    return name, {'type': 'sw-tiles', 'blocks': blocks, 'block_order': order, 'settings': st}

S = q = lambda s: '/search?type=product&q=' + s.replace(' ', '+')
sections = dict([
 ('hero', {'type': 'sw-hero', 'blocks': {f'f{i}': {'type': 'fact', 'settings': {'value': v, 'label': l}} for i, (v, l) in enumerate([(str(len(P)), 'Products'), (str(len({p['brand'] for p in P})), 'Brands'), ('100%', 'Authentic'), ('£40', 'Free UK delivery')])},
   'block_order': ['f0', 'f1', 'f2', 'f3'], 'settings': {'h1': 'Natural skincare UK · Niche perfume',
   'title': 'Rituals for the <strong>skin</strong>, <em>signatures</em> for the <strong>senses</strong>.',
   'lede': 'Best-loved natural skincare and niche and designer perfume, in one UK studio. Chosen with care, 100% authentic, delivered from the UK.',
   'button1_label': 'Shop skincare', 'button1_link': 'shopify://collections/skincare', 'button2_label': 'Discover fragrance', 'button2_link': 'shopify://collections/fragrance',
   'skin_products': skin[:6], 'scent_products': scent[:6], 'interval': 1}}),
 tiles('categories', 'Shop by category', 'category', [('Face wash', None, 'cleanser'), ('Serums', None, 'serum'), ('Moisturisers', None, 'moisturizers-gels'), ('Sunscreen', None, 'sunscreen'), ('Lip care', None, 'lip-balm'), ('Hair oil', None, 'hair-oil'), ('Shampoo', None, 'shampoo'), ('Body care', None, 'body-cream-exfoliants'), ('Fragrance', None, 'fragrance'), ('Gift sets', None, 'sets-combos')], link=('Shop all', 'shopify://collections/all')),
 ('studios', {'type': 'sw-studios', 'blocks': {
    's1': {'type': 'studio', 'settings': {'style': 'skin', 'mark': 'Skin', 'title': 'The Skin Studio', 'text': 'Natural skincare from Deyga, Vilvah, Highborn London and more. Cleansers, serums, lip care, hair and body.',
      'links': '<a href="/collections/skincare" title="Skincare">Skincare</a> <a href="/collections/haircare" title="Haircare">Haircare</a> <a href="/collections/bodycare" title="Bath & Body">Bath &amp; Body</a> <a href="/collections/milk-drop-brightening-serum-1" title="Deyga">Deyga</a> <a href="/collections/milk-drop-brightening-serum" title="Vilvah">Vilvah</a>'}},
    's2': {'type': 'studio', 'settings': {'style': 'scent', 'mark': 'Scent', 'title': 'The Scent Studio', 'text': "Tiziana Terenzi extraits, Al Haramain Amber Oud, Hemel, Signature D'orient, Gucci, Bvlgari and more.",
      'links': '<a href="/collections/fragrance" title="All fragrance">All fragrance</a> <a href="' + q('oud') + '" title="Oud">Oud</a> <a href="' + q('amber') + '" title="Amber">Amber</a> <a href="/collections/tiziana-terenzi" title="Tiziana Terenzi">Tiziana Terenzi</a> <a href="/collections/al-haramain" title="Al Haramain">Al Haramain</a>'}}},
   'block_order': ['s1', 's2'], 'settings': {}}),
 tiles('price', 'Shop by price', 'price', [('Under £15', 'Lip care, minis and add-ons', 'lip-balm', '/collections/all?filter.v.price.lte=15'), ('£15 – £25', 'Everyday heroes', 'serum', '/collections/all?filter.v.price.gte=15&filter.v.price.lte=25'), ('£25 – £50', 'Routines and treats', 'fragrance', '/collections/all?filter.v.price.gte=25&filter.v.price.lte=50'), ('Over £50', 'Luxury gifts', 'tiziana-terenzi', '/collections/all?filter.v.price.gte=50')], link=('Gifts & sets', 'shopify://collections/sets-combos')),
 ('bestsellers', {'type': 'sw-product-tabs', 'blocks': {'t1': {'type': 'tab', 'settings': {'label': 'Skincare & body', 'products': skin, 'limit': 8}}, 't2': {'type': 'tab', 'settings': {'label': 'Fragrance', 'products': scent, 'limit': 8}}},
   'block_order': ['t1', 't2'], 'settings': {'heading': 'Iconic bestsellers', 'link_label': 'View all', 'link_url': 'shopify://collections/best-sellers'}}),
 tiles('concerns', 'Shop by concern', 'concern', [('Acne & oil control', 'Face wash for oily skin', 'cleanser', q('oily skin')), ('Glow & even tone', 'Serums for glowing skin', 'serum'), ('Deep hydration', 'Moisturiser for dry skin', 'moisturizers-gels'), ('Lip care', 'Balms and scrubs', 'lip-balm'), ('Sun care', 'SPF 50 sunscreen', 'sunscreen'), ('Hair fall', 'Hair oils', 'hair-oil'), ('Dandruff', 'Scalp care', 'shampoo', q('dandruff')), ('Calm & soothe', 'Aloe vera and gentle care', 'toner', q('aloe vera'))]),
 tiles('families', 'Find your signature scent', 'family', [('Oud', 'Smoky, resinous and deep', None, q('oud')), ('Amber', 'Warm, sweet and enveloping', None, q('amber')), ('Floral', 'Rose, jasmine and bright petals', None, q('floral')), ('Woody', 'Sandalwood, cedar and vetiver', None, q('woody')), ('Fresh', 'Citrus, aquatic and green', None, q('fresh'))], link=('All fragrance', 'shopify://collections/fragrance')),
 tiles('brands', 'Shop by brand', 'brand', [('Deyga', 'Official UK partner', 'milk-drop-brightening-serum-1'), ('Vilvah', 'Official UK partner', 'milk-drop-brightening-serum'), ('Tiziana Terenzi', 'Italian niche extraits', 'tiziana-terenzi'), ('Al Haramain', 'Arabian perfume house', 'al-haramain'), ('Gucci', 'Designer fragrance', 'gucci'), ('Hemel', 'Arabian-inspired luxury', 'hemel-h'), ('Signature D\'orient', 'Oud and amber', 'signature-sillage-dorient'), ('Dolce & Gabbana', 'Designer fragrance', 'dolce-gabbana')], link=('All brands', 'shopify://collections'), count=True),
 ('story_deyga', {'type': 'sw-story', 'settings': {'eyebrow': 'Behind the brand · Official UK partner', 'heading': 'Deyga: grown, made, and now shipped from the UK',
   'text': '<p>Deyga is a family-run Indian brand that grows many of its own botanicals and turns them into simple, plant-based skin, hair and body care. Swansura is its official UK partner, so every Deyga product is 100% authentic and ships from the UK.</p>',
   'products': [find('charcoal face wash'), find('shea saffron')], 'button1_label': 'Shop all Deyga', 'button1_link': 'shopify://collections/milk-drop-brightening-serum-1', 'button2_label': 'Discover Vilvah', 'button2_link': 'shopify://collections/milk-drop-brightening-serum', 'reverse': False}}),
 ('story_vilvah', {'type': 'sw-story', 'settings': {'eyebrow': 'Behind the brand · Official UK partner', 'heading': 'Vilvah: the goat-milk ritual, from India to the UK',
   'text': '<p>Vilvah is known for goat milk and botanical formulas for face, hair and body, from Milk Drops to its goat milk shampoo. Swansura is its official UK partner, with every product 100% authentic and dispatched from the UK.</p>',
   'products': [find('milk drops'), find('goat milk shampoo')], 'button1_label': 'Shop all Vilvah', 'button1_link': 'shopify://collections/milk-drop-brightening-serum', 'button2_label': 'Shop moisturisers', 'button2_link': 'shopify://collections/moisturizers-gels', 'reverse': True}}),
 ('xmas', {'type': 'sw-xmas', 'settings': {'heading': 'Christmas gifting, sorted',
   'text': 'Perfume gift sets, miniatures and natural skincare kits for everyone on your list. Every gift is 100% authentic and dispatched from the UK, with free UK delivery over £40.',
   'links': ' '.join(f'<a href="{u}" title="{l}">{l}</a>' for l, u in [('Gifts for her', q('gift set women')), ('Gifts for him', q('gift set men')), ('Under £25', '/collections/all?filter.v.price.lte=25'), ('Perfume gift sets', q('perfume gift set')), ('Stocking fillers', q('miniature')), ('Skincare kits', '/collections/skincare-tools-kits')]),
   'button_label': 'Shop Christmas gifts', 'button_link': 'shopify://collections/sets-combos', 'products': xmas}}),
 ('popular', {'type': 'sw-chips', 'blocks': {f'c{i}': {'type': 'chip', 'settings': {'label': l, 'link': u}} for i, (l, u) in enumerate([
   ('Natural skincare', '/collections/skincare'), ('Moisturiser for dry skin', '/collections/moisturizers-gels'), ('Face wash for oily skin', '/collections/cleanser'), ('Hair growth oil', '/collections/hair-oil'), ('Natural shampoo', '/collections/shampoo'),
   ('Lip balm', '/collections/lip-balm'), ('Body butter', q('body butter')), ('Sunscreen SPF 50', '/collections/sunscreen'), ('Aloe vera gel', q('aloe vera gel')), ('Oud perfume', q('oud')), ('Amber perfume', q('amber')),
   ('Tiziana Terenzi', '/collections/tiziana-terenzi'), ('Al Haramain Amber Oud', '/collections/al-haramain'), ('Perfume gift sets', q('perfume gift set')), ('Miniature perfume', q('miniature'))])},
   'block_order': [f'c{i}' for i in range(15)], 'settings': {'heading': 'Popular searches', 'band': True}}),
 ('seo', {'type': 'sw-seo-copy', 'settings': {'eyebrow': 'About Swansura', 'heading': copy['h2'], 'body': seo_body}}),
 ('newsletter', {'type': 'sw-newsletter', 'settings': {}}),
])
order = ['hero', 'categories', 'studios', 'price', 'bestsellers', 'concerns', 'families', 'brands', 'story_deyga', 'story_vilvah', 'xmas', 'popular', 'seo', 'newsletter']
json.dump({'sections': sections, 'order': order}, open('theme/templates/index.json', 'w'), ensure_ascii=False, separators=(',', ':'))

# header group: Swansura announcement bar + Dawn header (kept for cart drawer / search / menus)
hg_path = 'theme/sections/header-group.json'
raw = open(hg_path).read(); hg = json.loads(raw[raw.index('{'):])
hg['sections'] = {'sw-announcement': {'type': 'sw-announcement', 'blocks': {
    'm1': {'type': 'message', 'settings': {'text': 'Save <strong>5%</strong> on routines &amp; bundles', 'link': 'shopify://collections/sets-combos'}},
    'm2': {'type': 'message', 'settings': {'text': 'Free UK delivery over <strong>£40</strong> · <strong>£5 off</strong> over £70', 'link': 'shopify://collections/all'}},
    'm3': {'type': 'message', 'settings': {'text': 'Official UK partner of <strong>Deyga</strong> &amp; <strong>Vilvah</strong>', 'link': 'shopify://collections/milk-drop-brightening-serum-1'}}},
    'block_order': ['m1', 'm2', 'm3'], 'settings': {'speed': 1}}, 'header': hg['sections']['header']}
hg['order'] = ['sw-announcement', 'header']
hg['sections']['header']['settings'].update({'menu': 'sw-main', 'menu_type_desktop': 'mega', 'logo_position': 'top-center', 'show_line_separator': False, 'sticky_header_type': 'on-scroll-up'})
json.dump(hg, open(hg_path, 'w'), ensure_ascii=False, indent=2)

FOOT_MENUS = [('Shop', 'sw-footer-shop'), ('Concerns', 'sw-footer-concerns'), ('Ranges', 'sw-footer-ranges'),
              ('Brands', 'sw-footer-brands'), ('Popular searches', 'sw-footer-popular-searches'), ('Help', 'sw-footer-help')]
fg_path = 'theme/sections/footer-group.json'
raw = open(fg_path).read(); fg = json.loads(raw[raw.index('{'):])
fg['sections'] = {'sw-footer': {'type': 'sw-footer', 'blocks': {
    # the prototype footer's six columns (store menus sw-footer-*, built by tools/shopify/proto_menus.py)
    **{f'b{i}': {'type': 'menu', 'settings': {'heading': h, 'menu': m}} for i, (h, m) in enumerate(FOOT_MENUS, 1)}},
    'block_order': [f'b{i}' for i in range(1, len(FOOT_MENUS) + 1)], 'settings': {
    'legal_links': 'sw-legal', 'sitemap_url': '/pages/sitemap','text': 'Natural skincare and rare fragrance, 100% authentic and shipped from the UK.',
    'promises': '<ul><li>Official UK partner of Deyga &amp; Vilvah</li><li>Dispatched from the UK in 1–2 working days</li><li>Free UK delivery over £40</li><li>£5 off orders over £70</li></ul>'}}}
fg['order'] = ['sw-footer']
json.dump(fg, open(fg_path, 'w'), ensure_ascii=False, indent=2)
print('index sections', len(order), '| skin', len(skin), 'scent', len(scent))

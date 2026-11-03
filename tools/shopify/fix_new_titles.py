"""Fix product titles of the 2 Nov 2026 new products where the packaging photos show the real name
(user, 3 Nov 2026: "Fix the product titles from the client check list"; list docs/images/drive_nov_client_checks_2026-11-03.csv).

- Mercedes-Benz 'le Eau de Parfum' 120ml -> Le Parfum 120ml (bottle + case)
- Guess Miami 'Ribes' -> Miami Vibes (bottle + box)
- Franck Olivier Eau de Passion Intense Men: Eau de Toilette -> Eau de Parfum (box 'Eau de Parfum pour lui')
- Guess 'Green' EDT 150ml -> Guess Man (box)
- Fun & Basics Be Fun Men / Funtastic Men / Funtastic Women -> Man / Man / Woman (labels)
- Tous The Luminous Gold -> Tous Touch The Luminous Gold (box)
- Natural By Woods: client names '<Name> 100 … 5ml' / 'Flame 100 Fragrance 15ml' are a 100ml EDP + travel atomiser
  (photos/box) -> '<Name> Eau de Parfum with Travel Atomiser 100ml + 5ml' (Flame + 15ml); every NBW description
  rewritten so it no longer calls the product 5ml; 'Discovery Set None' -> 'Discovery Set'.
Handles change with redirects (redirectNewHandle); custom.pdp 'sim' lists of other products are updated to the new
handles. Updates docs/seo/sheet_live_products_2026-11-02.json in place and writes
docs/seo/title_fixes_2026-11-03.json (before/after + productUpdate inputs).
"""
import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
F = ROOT / 'docs/seo/sheet_live_products_2026-11-02.json'
L = json.load(open(F))
B = {p['handle']: p for p in L}

REPL = {  # handle: (new handle, [(old, new) text replacements in title/h1/seo/description/metafields])
 'mercedes-benz-le-eau-de-parfum-120ml': ('mercedes-benz-le-parfum-120ml',
    [('Mercedes Benz le Eau de Parfum (EDP) 120ml is an Eau de Parfum (EDP) created', 'Mercedes-Benz Le Parfum 120ml is a parfum created'),
     ('Mercedes-Benz le Eau de Parfum', 'Mercedes-Benz Le Parfum'), ("men's eau de parfum", "men's parfum"),
     ('<li>Eau de Parfum, 120ml</li>', '<li>Le Parfum, 120ml</li>'), ('"Eau de Parfum"', '"Le Parfum"')]),
 'guess-miami-ribes-shimmer-body-mist-250ml': ('guess-miami-vibes-shimmer-body-mist-250ml', [('Miami Ribes', 'Miami Vibes')]),
 'franck-olivier-eau-de-passion-intense-men-eau-de-toilette-75ml': ('franck-olivier-eau-de-passion-intense-men-eau-de-parfum-75ml',
    [('Eau de Toilette (EDT)', 'Eau de Parfum (EDP)'), ('Eau de Toilette', 'Eau de Parfum'), (' EDT', ' EDP'),
     ('eau de toilette', 'eau de parfum')]),
 'guess-green-eau-de-toilette-150ml': ('guess-man-eau-de-toilette-150ml', [('Guess Green', 'Guess Man')]),
 'fun-basics-be-fun-men-eau-de-toilette-100ml': ('fun-basics-be-fun-man-eau-de-toilette-100ml', [('Be Fun Men', 'Be Fun Man')]),
 'fun-basics-funtastic-men-eau-de-parfum-100ml': ('fun-basics-funtastic-man-eau-de-parfum-100ml', [('Funtastic Men', 'Funtastic Man')]),
 'fun-basics-funtastic-women-eau-de-parfum-100ml': ('fun-basics-funtastic-woman-eau-de-parfum-100ml', [('Funtastic Women', 'Funtastic Woman')]),
 'tous-the-luminous-gold-eau-de-toilette-50ml': ('tous-touch-the-luminous-gold-eau-de-toilette-50ml', [('Tous The Luminous Gold', 'Tous Touch The Luminous Gold')]),
}
NBW_RENAME = {'natural-by-woods-bloom-100-eau-de-parfum-5ml': ('Bloom', 5), 'natural-by-woods-dusk-100-eau-de-parfum-5ml': ('Dusk', 5),
              'natural-by-woods-north-star-100-eau-de-parfum-5ml': ('North Star', 5),
              'natural-by-woods-royal-night-100-eau-de-parfum-5ml': ('Royal Night', 5),
              'natural-by-woods-flame-100-fragrance-15ml': ('Flame', 15)}
NBW_DESC = {'dawn': 'Dawn', 'earth': 'Earth', 'eclipse': 'Eclipse', 'essence': 'Essence', 'glow': 'Glow', 'karma': 'Karma', 'sun': 'Sun'}


def h1_of(i):
    return next(m for m in i['metafields'] if m['key'] == 'h1')


def nbw_para(name, n):
    return (f'<p>Natural By Woods {name} is an Eau de Parfum (EDP) for all-gender wear, with a structured woody profile and '
            f'smooth, refined depth. It comes as a 100ml bottle with a {n}ml travel atomiser, so you can keep a little with you '
            'during the day.</p>')


fixes, handle_map = [], {}
for p in L:
    i, h = p['input'], p['handle']
    before = {'title': i['title'], 'handle': h, 'h1': h1_of(i)['value'], 'seo': dict(i['seo']), 'descriptionHtml': i['descriptionHtml']}
    new_h = None
    if h in REPL:
        new_h, reps = REPL[h]
        for a, b in reps:
            i['title'] = i['title'].replace(a, b)
            i['seo'] = {k: v.replace(a, b) for k, v in i['seo'].items()}
            i['descriptionHtml'] = i['descriptionHtml'].replace(a, b)
            for m in i['metafields']:
                m['value'] = m['value'].replace(a, b)
    elif p['brand'] == 'Natural By Woods':
        name = n = None
        if h in NBW_RENAME:
            name, n = NBW_RENAME[h]
            new_h = f'natural-by-woods-{name.lower().replace(" ", "-")}-eau-de-parfum-with-travel-atomiser-100ml-{n}ml'
        else:
            for k, v in NBW_DESC.items():
                if h.startswith(f'natural-by-woods-{k}-'):
                    name, n = v, 5
        if name:
            price = i['variants'][0]['price']
            i['title'] = f'Natural By Woods {name} Eau de Parfum with Travel Atomiser 100ml + {n}ml'
            h1_of(i)['value'] = f'Natural By Woods {name} Eau de Parfum with Travel Atomiser'
            st = f'Natural By Woods {name} EDP with Travel Atomiser | Swansura'
            if len(st) > 60:
                st = f'Natural By Woods {name} EDP 100ml + {n}ml | Swansura'
            sd = (f'Buy Natural By Woods {name} Eau de Parfum 100ml with a {n}ml travel atomiser for £{price} at Swansura UK. '
                  'A woody unisex eau de parfum. 100% authentic.')
            assert len(st) <= 60 and len(sd) <= 160, (st, len(sd))
            i['seo'] = {'title': st, 'description': sd}
            d = i['descriptionHtml']
            d = re.sub(r'^<p>.*?</p>', nbw_para(name, n), d, count=1)
            d = re.sub(r'<li>(Eau de Parfum|Fragrance \(type not specified\)), [^<]*</li>',
                       f'<li>Eau de Parfum, 100ml bottle + {n}ml travel atomiser</li>', d)
            i['descriptionHtml'] = d
            for m in i['metafields']:
                if m['key'] == 'pdp':
                    m['value'] = m['value'].replace('"Fragrance"', '"Eau de Parfum"')
        elif h == 'natural-by-woods-discovery-set-none':
            new_h = 'natural-by-woods-discovery-set'
            i['title'] = 'Natural By Woods Discovery Set'
            h1_of(i)['value'] = 'Natural By Woods Discovery Set'
            i['seo'] = {'title': 'Natural By Woods Discovery Set | Swansura UK',
                        'description': f"Buy the Natural By Woods Discovery Set for £{i['variants'][0]['price']} at Swansura UK. "
                                       'Woody unisex fragrances to try. 100% authentic, free UK delivery over £40.'}
            i['descriptionHtml'] = i['descriptionHtml'].replace(
                'Presented in a full-size format, it works well for daily use or gifting.',
                'Message us on WhatsApp or Instagram for the sizes and scents in the set.').replace(
                '<li>Fragrance (type not specified)</li>', '<li>Discovery set</li>')
    if new_h or i['title'] != before['title'] or i['descriptionHtml'] != before['descriptionHtml']:
        if new_h:
            handle_map[h] = new_h
            p['handle'] = i['handle'] = new_h
        fixes.append({'id': p['id'], 'before': before,
                      'input': {'id': p['id'], 'title': i['title'], 'handle': i['handle'], 'redirectNewHandle': True,
                                'seo': i['seo'], 'descriptionHtml': i['descriptionHtml'],
                                'metafields': [m for m in i['metafields'] if m['key'] in ('h1', 'pdp', 'sw')]}})
# point other products' 'similar' lists at the new handles
sim_updates = []
for p in L:
    for m in p['input']['metafields']:
        if m['key'] == 'pdp':
            v = m['value']
            for a, b in handle_map.items():
                v = v.replace(f'"{a}"', f'"{b}"')
            if v != m['value']:
                m['value'] = v
                if not any(f['id'] == p['id'] for f in fixes):
                    sim_updates.append({'ownerId': p['id'], 'namespace': 'custom', 'key': 'pdp', 'type': 'json', 'value': v})
                else:
                    for f in fixes:
                        if f['id'] == p['id']:
                            for mm in f['input']['metafields']:
                                if mm['key'] == 'pdp':
                                    mm['value'] = v
json.dump(L, open(F, 'w'), ensure_ascii=False, indent=1)
json.dump({'fixes': fixes, 'handle_map': handle_map, 'sim_metafields': sim_updates},
          open(ROOT / 'docs/seo/title_fixes_2026-11-03.json', 'w'), ensure_ascii=False, indent=1)
for f in fixes:
    print(f['before']['title'], '->', f['input']['title'], '|', f['input']['handle'])
print(len(fixes), 'products;', len(handle_map), 'new handles;', len(sim_updates), 'similar-list updates')

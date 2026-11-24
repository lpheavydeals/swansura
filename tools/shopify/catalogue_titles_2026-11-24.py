# 24 Nov 2026 (user: 'Clean the catalogue titles, then make it live'): the Meta catalogue cards show the Shopify product
# title, and the fragrance-catalogue brands carried marketing tails (' – Luxury Unisex Niche Perfume', '– Long Lasting …').
# New titles: no tails, gender kept in the store's style (Unisex / for Men / for Women), Tiziana Terenzi gets its brand,
# collection names kept in brackets (two Caput Mundi listings differ only by it). Handles, SEO titles, H1s unchanged.
# Writes docs/seo/catalogue_titles_2026-11-24.json (id, before, after = undo list).
import json,sys
B=json.load(open(sys.argv[1]))  # Admin products query result (id, title)
TT='Tiziana Terenzi '
NEW={
'16267730977155':TT+'Casanova Anniversary Extrait de Parfum 100ml Unisex',
'16269063553411':TT+'Chimaera Anniversary Extrait de Parfum 100ml Unisex',
'16269862404483':TT+'Andromeda Extrait de Parfum 100ml Unisex',
'16271521874307':TT+'Draconis Extrait de Parfum 100ml Unisex',
'16271537504643':TT+'Dubhe Assoluto Extrait de Parfum 100ml Unisex',
'16272506651011':TT+'Ecstasy Extrait de Parfum 100ml Unisex',
'16272514122115':TT+'Akragas Extrait de Parfum 100ml Unisex (Classic Collection)',
'16273306190211':TT+'Leo Extrait de Parfum 100ml Unisex (Luna Collection)',
'16273311170947':TT+'Caput Mundi Extrait de Parfum 100ml Unisex',
'16273328275843':TT+'Deriva Extrait de Parfum 100ml Unisex (Sea Stars Collection)',
'16273541792131':TT+'Gold Rose Oudh Extrait de Parfum 100ml Unisex',
'16273546150275':TT+'Gumin Extrait de Parfum 100ml Unisex',
'16274498945411':TT+'Kaff Extrait de Parfum 100ml Unisex',
'16274581029251':TT+'Kirke Extrait de Parfum 100ml Unisex',
'16274590695811':TT+'Borelli Extrait de Parfum Linea TT 100ml Unisex (Comete Collection)',
'16279916380547':TT+'Orza Extrait de Parfum Linea TT 100ml Unisex',
'16279972610435':TT+'Caput Mundi Extrait de Parfum 100ml Unisex (Luna Collection)',
'16280027496835':TT+'Moro di Venezia Extrait de Parfum 100ml Unisex (Luna Collection)',
'16280044241283':TT+'Orion Extrait de Parfum 100ml Unisex',
'16280056529283':TT+'Porpora Extrait de Parfum 100ml Unisex (Luna Collection Red Moon)',
'16280073404803':TT+'Saiph Extrait de Parfum 100ml Unisex (Luna Stars Gold)',
'16280091394435':TT+'White Fire Extrait de Parfum 100ml Unisex',
'16281929843075':'Chopard Amber Malaki Eau de Parfum 80ml Unisex',
'16282276069763':'Chopard Black Incense Malaki Eau de Parfum 80ml Unisex',
'16282293141891':'Chopard Gardens of Paradise Eau de Parfum Discovery Set 4x10ml Unisex',
'16282354745731':'Chopard Imperiale Iris Malika Eau de Parfum 100ml for Women',
'16296009793923':'Chopard Oud Malaki Eau de Parfum 80ml for Men',
'16303068152195':'Gucci Women’s Perfume Set 4x5ml (Guilty EDT, Flora Gorgeous Orchid, Flora Gorgeous Gardenia & Bloom)',
'16303139422595':'Gucci Women’s Miniature Perfume Set 4x5ml (Bloom EDP & Flora Gorgeous Gardenia EDP)',
'16303149285763':'Gucci Bloom Eau de Toilette 10ml Miniature for Women',
'16303189557635':'Gucci Bloom Parfum 10ml Miniature Spray for Women',
'16303208038787':'Gucci Bloom Eau de Parfum Gift Set 100ml + 10ml + Body Lotion 100ml for Women',
'16303236546947':'Gucci Bloom Profumo di Fiori Eau de Parfum 10ml Pen Spray for Women',
'16303298478467':'Gucci Flora Gorgeous Miniature Perfume Set 3x5ml (Gardenia, Magnolia & Orchid)',
'16303309291907':'Gucci Flora Gorgeous Gardenia Eau de Parfum 50ml for Women',
'16303440363907':'Gucci Flora Gorgeous Orchid Eau de Parfum 10ml Miniature for Women',
'16303446131075':'Gucci Guilty Pour Femme Eau de Parfum Gift Set 50ml + Body Lotion 50ml',
'16303462187395':'Gucci Guilty Pour Femme Eau de Parfum 10ml Miniature Spray',
'16303465922947':'Gucci Guilty Pour Homme Eau de Toilette 90ml',
'16303477227907':'Gucci Intense Oud Eau de Parfum 90ml Unisex',
'16305050354051':'Al Haramain Amber Musk Eau de Parfum 100ml Unisex',
'16305115955587':'Al Haramain Amber Oud Eau de Parfum 60ml Unisex',
'16305137451395':'Al Haramain Amber Oud Black Edition Eau de Parfum 100ml Unisex',
'16305271734659':'Al Haramain Amber Oud Bleu Edition Eau de Parfum Unisex',
'16305337237891':'Al Haramain Amber Oud Carbon Edition Eau de Parfum for Men',
'16305569694083':'Al Haramain Amber Oud Extreme Gold Edition Extrait de Parfum Unisex',
'16306788008323':'Al Haramain Amber Oud Gold Edition Eau de Parfum Unisex',
'16306908594563':'Al Haramain Amber Oud Ruby Edition Eau de Parfum Unisex',
'16306954502531':'Al Haramain Amber Oud Tobacco Edition Eau de Parfum 60ml Unisex',
'16316357476739':'Al Haramain Amber Oud White Edition Eau de Parfum for Women',
'16316457615747':'Al Haramain Detour Noir Eau de Parfum 100ml Unisex',
'16318017634691':'Al Haramain L’Aventure Eau de Parfum 100ml for Men',
'16318036836739':'Al Haramain L’Aventure Blanche Eau de Parfum 100ml for Women',
'16318043685251':'Al Haramain L’Aventure Femme Eau de Parfum 100ml',
'16318046372227':'Al Haramain L’Aventure Gold Eau de Parfum 100ml for Women',
'16318051647875':'Al Haramain L’Aventure Intense Eau de Parfum 100ml for Men',
}
cur={n['id'].split('/')[-1]:n['title'] for n in B['data']['products']['nodes']}
out=[{'id':'gid://shopify/Product/'+k,'before':cur[k],'after':v} for k,v in NEW.items() if cur[k]!=v]
bad=[o for o in out if any(w in o['after'].lower() for w in ['luxury','long','niche','–'])]
assert not bad,bad
json.dump(out,open('docs/seo/catalogue_titles_2026-11-24.json','w'),indent=1,ensure_ascii=False)
print(len(out),'changes')

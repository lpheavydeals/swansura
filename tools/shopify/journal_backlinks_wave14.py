"""Wave 14 back-links (20 Nov 2026): the 5 guides published 20 Nov (Chloé, Dolce & Gabbana, Lalique, Armaf Club de
Nuit, skincare gift sets). One sentence per link, nothing else changed.

Usage: python3 journal_backlinks_wave14.py <admin.json>
admin.json = Admin query {data:{a1:{nodes:[id,handle,body]}, c:{nodes:[id,handle,sc{value,type}]}}}
Writes docs/seo/journal_backlinks_wave14_2026-11-20.json (before/after = undo).
"""
import json, sys
J = '/blogs/journal/'
CH = f'<a href="{J}chloe-perfume-guide">Chloé perfume guide</a>'
DG = f'<a href="{J}dolce-gabbana-perfume-guide">Dolce &amp; Gabbana perfume guide</a>'
LA = f'<a href="{J}lalique-perfume-guide">Lalique perfume guide</a>'
AR = f'<a href="{J}armaf-club-de-nuit-guide">Armaf Club de Nuit guide</a>'
SK = f'<a href="{J}skincare-gift-sets-guide">skincare gift sets guide</a>'
E = {
 'christmas-gift-guide': [
  ('More boxed sets are in <a href="/collections/giftsets">gift sets</a>.</p>',
   f'More boxed sets are in <a href="/collections/giftsets">gift sets</a>. Our {SK} lists what is in every Vilvah and Deyga kit.</p>')],
 'stocking-fillers-for-her-under-25': [
  ('Rose &amp; Vanilla and Lavender &amp; Sage.</li>',
   f'Rose &amp; Vanilla and Lavender &amp; Sage. More small kits are in our {SK}.</li>')],
 'mini-perfume-sets-guide': [
  ('and Rose Tangerine.</li>', f'and Rose Tangerine. Our {CH} compares the full bottles.</li>'),
  ('K Eau de Parfum, The One and Light Blue Pour Homme.</li>',
   f'K Eau de Parfum, The One and Light Blue Pour Homme. See our {DG} for the whole range.</li>')],
 'best-perfume-gift-sets-uk-2026': [
  ('suits the office as well as an evening out.</li>',
   f'suits the office as well as an evening out. More in our {CH}.</li>'),
  ('One for home, one for her bag.</li>',
   f'One for home, one for her bag. Our {DG} compares the whole range.</li>'),
  ('pistachio and vanilla.</li>',
   f'pistachio and vanilla. For a full-size bottle on a budget, see our {LA}.</li>')],
 'lattafa-khamrah-qahwa-arabian-perfume': [
  ('Amber Oud guide</a>.', f'Amber Oud guide</a>, and Armaf Club de Nuit in our {AR}.')],
 'oud-perfume-guide': [
  ('compares them all.', f'compares them all. Armaf Club de Nuit Intense, with agarwood (oud) in its base, is in our {AR}.')],
}
C = {
 'chloe': [('Every piece is 100% authentic.</p>', f'Every piece is 100% authentic. Our {CH} compares them all.</p>')],
 'dolce-gabbana': [('with a few bright, fruity choices too.</p>', f'with a few bright, fruity choices too. Our {DG} compares every one.</p>')],
 'lalique': [('Lalique White Eau de Toilette 125ml</a> for men.</p>', f'Lalique White Eau de Toilette 125ml</a> for men. Our {LA} compares them all.</p>')],
 'armaf': [('Miss Armaf and Hunter.</p>', f'Miss Armaf and Hunter. Our {AR} compares Intense, Precieux and the Private Key extraits.</p>')],
 'skincare-gift-sets': [('so every kit here is authentic and ships from the UK.</p>',
   f'so every kit here is authentic and ships from the UK. Our {SK} lists what is in each one.</p>')],
}
d = json.load(open(sys.argv[1]))['data']
A = {a['handle']: a for a in d['a1']['nodes']}
out = {'articles': [], 'collections': []}
for h, eds in E.items():
    b = a = A[h]['body']
    for o, n in eds:
        assert a.count(o) == 1, (h, o); a = a.replace(o, n)
    out['articles'].append({'handle': h, 'id': A[h]['id'], 'before': b, 'after': a})
for c in d['c']['nodes']:
    b = a = c['sc']['value']
    for o, n in C[c['handle']]:
        assert a.count(o) == 1, (c['handle'], o); a = a.replace(o, n)
    out['collections'].append({'handle': c['handle'], 'id': c['id'], 'type': c['sc']['type'], 'before': b, 'after': a})
json.dump(out, open('docs/seo/journal_backlinks_wave14_2026-11-20.json', 'w'), ensure_ascii=False, indent=1)
print('ok', len(out['articles']), len(out['collections']))

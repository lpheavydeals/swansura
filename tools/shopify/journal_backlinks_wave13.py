"""Wave 13 back-links (18 Nov 2026): the 5 guides published 18 Nov (Versace, Narciso Rodriguez, Issey Miyake,
winter skincare, peptide/bakuchiol). One sentence per link, nothing else changed.

Usage: python3 journal_backlinks_wave13.py <admin.json>
admin.json = Admin query {data:{articles:{nodes:[id,handle,body]}, collections:{nodes:[id,handle,seo_copy{id,value}]}}}
Writes docs/seo/journal_backlinks_wave13_2026-11-18.json (before/after = undo).
"""
import json, sys
J = '/blogs/journal/'
V = f'<a href="{J}versace-perfume-guide">Versace perfume guide</a>'
N = f'<a href="{J}narciso-rodriguez-perfume-guide">Narciso Rodriguez perfume guide</a>'
I = f'<a href="{J}issey-miyake-leau-dissey-guide">L’Eau d’Issey guide</a>'
W = f'<a href="{J}winter-skincare-dry-skin">winter skincare routine for dry skin</a>'
P = f'<a href="{J}peptide-bakuchiol-serum-guide">peptide and bakuchiol serum guide</a>'
E = {
 'mini-perfume-sets-guide': [
  ('<a href="/blogs/journal/mugler-perfume-guide">Mugler perfume guide</a>.</p>',
   f'<a href="/blogs/journal/mugler-perfume-guide">Mugler perfume guide</a>. The Versace 5ml minis are compared in our {V}.</p>')],
 'best-perfume-gift-sets-uk-2026': [
  ('For Mugler Alien and Angel, see our <a href="/blogs/journal/mugler-perfume-guide">Mugler perfume guide</a>.</p>',
   f'For Mugler Alien and Angel, see our <a href="/blogs/journal/mugler-perfume-guide">Mugler perfume guide</a>, and for the Narciso Rodriguez 10ml sprays, our {N}.</p>'),
  ('See our <a href="/blogs/journal/paco-rabanne-perfume-guide">Paco Rabanne perfume guide</a>.</p>',
   f'See our <a href="/blogs/journal/paco-rabanne-perfume-guide">Paco Rabanne perfume guide</a>, or for Versace Eros, our {V}.</p>')],
 'extrait-vs-eau-de-parfum': [
  ('<a href="/blogs/journal/calvin-klein-eternity-for-women-vs-for-men">Calvin Klein Eternity for women vs for men</a>.</p>',
   f'<a href="/blogs/journal/calvin-klein-eternity-for-women-vs-for-men">Calvin Klein Eternity for women vs for men</a>. Versace Eros eau de toilette and Eros Parfum are compared in our {V}.</p>')],
 'moisturiser-for-your-skin-type': [
  ('Look for a cream with butters and oils.</p>',
   f'Look for a cream with butters and oils. When the weather turns cold, see our {W}.</p>')],
 'face-wash-for-your-skin-type': [
  ('Look for creamy or milky textures and soothing, moisture-loving ingredients.</p>',
   f'Look for creamy or milky textures and soothing, moisture-loving ingredients. For a full cold-weather routine, see our {W}.</p>')],
 'how-to-use-body-butter': [
  ('at night, and in cold weather.</li>',
   f'at night, and in cold weather. Our {W} puts it in a full routine.</li>')],
 'face-serum-guide': [
  ('is a ceramide serum made to layer under moisturiser.</p>',
   f'is a ceramide serum made to layer under moisturiser. Our {P} explains these ingredients in more detail.</p>')],
}
C = {
 'versace': [('Yellow Diamond and Eros Pour Femme are the picks for women.</p>',
   f'Yellow Diamond and Eros Pour Femme are the picks for women. Our {V} compares every one.</p>')],
 'narciso-rodriguez': [('a run of 10ml sprays that make it easy to try a scent.</p>',
   f'a run of 10ml sprays that make it easy to try a scent. Our {N} compares them all.</p>')],
 'issey-miyake': [("you will find newer floral editions and Le Sel d'Issey.</p>",
   f"you will find newer floral editions and Le Sel d'Issey. Our {I} explains how each version differs.</p>")],
}
d = json.load(open(sys.argv[1]))['data']
A = {a['handle']: a for a in d['articles']['nodes']}
out = {'articles': [], 'collections': []}
for h, eds in E.items():
    b = a = A[h]['body']
    for o, n in eds:
        assert a.count(o) == 1, (h, o); a = a.replace(o, n)
    out['articles'].append({'handle': h, 'id': A[h]['id'], 'before': b, 'after': a})
for c in d['collections']['nodes']:
    b = a = c['seo_copy']['value']
    for o, n in C[c['handle']]:
        assert a.count(o) == 1, (c['handle'], o); a = a.replace(o, n)
    out['collections'].append({'handle': c['handle'], 'id': c['id'], 'metafield_id': c['seo_copy']['id'], 'before': b, 'after': a})
json.dump(out, open('docs/seo/journal_backlinks_wave13_2026-11-18.json', 'w'), ensure_ascii=False, indent=1)
print('ok', len(out['articles']), len(out['collections']), [len(x['after']) for x in out['articles']])

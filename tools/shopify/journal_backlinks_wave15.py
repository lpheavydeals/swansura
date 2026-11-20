"""Wave 15 back-links (20 Nov 2026): the 5 guides published 20 Nov, second set (Marc Jacobs, Acqua di Parma, Hugo Boss,
Burberry, Calvin Klein). One sentence per link, nothing else changed.

Usage: python3 journal_backlinks_wave15.py <admin.json>
admin.json = Admin query {data:{a1:{nodes:[id,handle,body]}, c:{nodes:[id,handle,sc{value,type}]}}}
Writes docs/seo/journal_backlinks_wave15_2026-11-20.json (before/after = undo).
"""
import json, sys
J = '/blogs/journal/'
MJ = f'<a href="{J}marc-jacobs-perfume-guide">Marc Jacobs perfume guide</a>'
AP = f'<a href="{J}acqua-di-parma-guide">Acqua di Parma guide</a>'
HB = f'<a href="{J}hugo-boss-perfume-guide">Hugo Boss perfume guide</a>'
BU = f'<a href="{J}burberry-perfume-guide">Burberry perfume guide</a>'
CK = f'<a href="{J}calvin-klein-perfume-guide">Calvin Klein perfume guide</a>'
E = {
 'christmas-gift-guide': [
  ('matching body lotion for layering.</li>', f'matching body lotion for layering. Our {HB} compares every Hugo Boss scent.</li>'),
  ('including Her London Dream.</li>', f'including Her London Dream. More in our {BU}.</li>'),
  ('with Obsession, Eternity and CK One.</li>', f'with Obsession, Eternity and CK One. Our {CK} covers Defy and Euphoria too.</li>')],
 'mini-perfume-sets-guide': [
  ('rhubarb, narcissus and almond milk.</li>', f'rhubarb, narcissus and almond milk. Our {MJ} compares the full bottles.</li>'),
  ('one Eternity and one CK One.</li>', f'one Eternity and one CK One. Our {CK} compares the rest of the range.</li>')],
 'best-perfume-gift-sets-uk-2026': [
  ('Narciso Rodriguez perfume guide</a>.</p>', f'Narciso Rodriguez perfume guide</a>. Marc Jacobs Perfect and Daisy are compared in our {MJ}.</p>'),
  ('three bright Mediterranean scents.', f'three bright Mediterranean scents. Our {AP} lists what is in both its discovery sets.')],
 'calvin-klein-eternity-for-women-vs-for-men': [
  ('A modern pick for Eternity for Men fans who like lavender.</li>', f'A modern pick for Eternity for Men fans who like lavender. Our {CK} compares all three Defy versions.</li>')],
 'tom-ford-perfume-guide': [
  ('over jasmine, coriander, musk and cedarwood.</li>', f'over jasmine, coriander, musk and cedarwood. Our {AP} covers the rest of the range.</li>')],
}
C = {
 'hugo-boss': [('for him and her.</p>', f'for him and her. Our {HB} compares them all.</p>')],
 'acqua-di-parma': [('before you commit to a big bottle.</p>', f'before you commit to a big bottle. Our {AP} compares every one.</p>')],
 'burberry': [('You will find five bottles and sets here.</p>', f'You will find five bottles and sets here. Our {BU} compares them all.</p>')],
 'calvin-klein': [('Every Calvin Klein perfume on this page is 100% authentic.</p>', f'Every Calvin Klein perfume on this page is 100% authentic. Our {CK} compares them all.</p>')],
 'marc-jacobs': [('and a gift set.</p>', f'and a gift set. Our {MJ} compares them all.</p>')],
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
json.dump(out, open('docs/seo/journal_backlinks_wave15_2026-11-20.json', 'w'), ensure_ascii=False, indent=1)
print('ok', len(out['articles']), len(out['collections']))

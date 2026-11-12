"""List a public Google Drive folder tree through drive.google.com/embeddedfolderview (no login).
Usage: python3 drive_tree.py <folder_id> <out.json>   -> [{path, id, title, kind folder|file, modified}]
"""
import sys, json, re, html, urllib.request, concurrent.futures
UA = {'User-Agent': 'Mozilla/5.0'}
def ls(fid):
    s = urllib.request.urlopen(urllib.request.Request(f'https://drive.google.com/embeddedfolderview?id={fid}', headers=UA), timeout=60).read().decode('utf-8', 'replace')
    out = []
    for m in re.finditer(r'<div class="flip-entry" id="entry-([^"]+)".*?<a href="([^"]+)".*?<div class="flip-entry-title">(.*?)</div>.*?<div class="flip-entry-last-modified"><div>(.*?)</div>', s, re.S):
        i, href, t, mod = m.groups()
        out.append(dict(id=i, title=html.unescape(t), kind='folder' if '/folders/' in href else 'file', modified=html.unescape(mod)))
    return out
root, outp = sys.argv[1], sys.argv[2]
res, todo = [], [(root, '')]
with concurrent.futures.ThreadPoolExecutor(8) as ex:
    while todo:
        batch, todo = todo, []
        for (fid, path), items in zip(batch, ex.map(lambda b: ls(b[0]), batch)):
            for it in items:
                it['path'] = (path + '/' if path else '') + it['title']; res.append(it)
                if it['kind'] == 'folder': todo.append((it['id'], it['path']))
json.dump(res, open(outp, 'w'), ensure_ascii=False, indent=0)
print(len(res), 'entries;', sum(r['kind'] == 'file' for r in res), 'files;', sum(r['kind'] == 'folder' for r in res), 'folders')

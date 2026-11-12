#!/usr/bin/env python3
"""Vilvah + Deyga back to their original photos, every photo square (user, 12 Nov 2026:
'the Cut-out ... Not Suitable for ... Deyga ... and Vilvah ... Reverse that to Original and Make the
Dimension as 1:1' -> sample on /collections/serum -> 'Okay Go head, all the 3').

For every image on the active Vilvah/Deyga products (Admin read saved as <scratch>/cur.json):
  -fill file   -> the original from docs/backups/graphic_fill_originals_2026-11-11/ (fileUpdate in place)
  -cutout file -> the original media it replaced (detached 11 Nov, still in Files) is attached again at the
                  same position, the cut-out is detached (not deleted), variant links move back
  other        -> kept (the 12 Nov sample products, already originals)
Photos that are not square (Deyga ~4:5, a few Vilvah) are widened to 1200x1200 with their own edge colours
(graphic_fill.py square mode), never cropped; saved to docs/images/square_2026-11-12/ as <stem>-sq.<ext>
(same format as the stored file: fileUpdate needs the extension to match) and served via raw.githubusercontent.

  square_photos.py <scratch>    needs cur.json, cutmap.json, orig_nodes.json in <scratch>
  -> <scratch>/plan.json, docs/images/square_2026-11-12/*, <scratch>/sheets/*.jpg (contact sheets to check)
"""
import json
import sys
import urllib.request
from io import BytesIO
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
import graphic_fill as gf  # noqa: E402

gf.set_square(1200)
ROOT = Path(__file__).resolve().parents[2]
RAW = 'https://raw.githubusercontent.com/lpheavydeals/swansura/claude/sweet-edison-hchm9o/'
FILL_ORIG = 'docs/backups/graphic_fill_originals_2026-11-11/'
OUT = 'docs/images/square_2026-11-12/'


def base(url):
    return url.split('/')[-1].split('?')[0]


def is_sq(w, h):
    return 0.98 < w / h < 1.02


def save(im, path):
    ext = path.suffix.lower()
    if ext in ('.jpg', '.jpeg'):
        im.convert('RGB').save(path, 'JPEG', quality=90, optimize=True)
    elif ext == '.png':
        im.convert('RGB').save(path, 'PNG', optimize=True)
    else:
        im.convert('RGB').save(path, 'WEBP', quality=88, method=6)


def fetch(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return Image.open(BytesIO(r.read())).copy()


def main(scratch):
    S = Path(scratch)
    cur = json.load(open(S / 'cur.json'))
    cutmap = json.load(open(S / 'cutmap.json'))
    onodes = {n['id']: n for n in json.load(open(S / 'orig_nodes.json'))['data']['nodes']}
    fills = {i['mid']: i for i in json.load(open(ROOT / 'docs/backups/graphic_fill_before_2026-11-11.json'))['items']}
    (ROOT / OUT).mkdir(parents=True, exist_ok=True)
    plan = {'content': [], 'add': [], 'rem': [], 'reorder': [], 'vl': [], 'squared': []}
    for p in cur:
        pid = p['id']
        order = []
        for m in p['media']['nodes']:
            u = m.get('image')
            if not u:
                order.append(m['id'])
                continue
            fn = base(u['url'])
            if '-fill' in fn:
                it = fills[m['id']]
                im = Image.open(ROOT / FILL_ORIG / it['orig_file'])
                tid, ext, stem = m['id'], Path(fn).suffix, Path(base(it['src'])).stem
                if is_sq(*im.size):
                    plan['content'].append({'id': tid, 'originalSource': RAW + FILL_ORIG + it['orig_file'],
                                            'filename': stem + ext})
                    order.append(tid)
                    continue
                src = im
            elif '-cutout' in fn:
                oid = cutmap[m['id']]['orig']
                o = onodes[oid]
                plan['add'].append({'id': oid, 'referencesToAdd': [pid]})
                plan['rem'].append({'id': m['id'], 'referencesToRemove': [pid]})
                for v in p['variants']['nodes']:
                    vm = v['media']['nodes']
                    if vm and vm[0]['id'] == m['id']:
                        plan['vl'].append({'product': pid, 'variant': v['id'], 'old': m['id'], 'new': oid})
                order.append(oid)
                if is_sq(o['image']['width'], o['image']['height']):
                    continue
                tid, ext, stem = oid, Path(base(o['image']['url'])).suffix, Path(base(o['image']['url'])).stem
                src = fetch(o['image']['url'])
            else:
                order.append(m['id'])
                if is_sq(u['width'], u['height']):
                    continue
                tid, ext, stem = m['id'], Path(fn).suffix, Path(fn).stem
                src = fetch(u['url'])
            name = f'{stem}-sq{ext.lower()}'
            save(gf.auto(src), ROOT / OUT / name)
            plan['content'].append({'id': tid, 'originalSource': RAW + OUT + name, 'filename': name})
            plan['squared'].append({'product': p['handle'], 'id': tid, 'file': name, 'from': list(src.size)})
            print(p['vendor'], name, src.size, flush=True)
        if order != [m['id'] for m in p['media']['nodes']]:
            plan['reorder'].append({'id': pid, 'moves': [{'id': mid, 'newPosition': str(i)} for i, mid in enumerate(order)]})
    json.dump(plan, open(S / 'plan.json', 'w'), indent=1)
    print({k: len(v) for k, v in plan.items()})


if __name__ == '__main__':
    main(sys.argv[1])

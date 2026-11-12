#!/usr/bin/env python3
"""Remaining '-fill' graphics (4:5, anatomē / Jo Milano / Highborn / others) -> square (user, 12 Nov 2026:
'The complete website should be in the 1:1 dimension'). The original of each -fill (docs/backups/
graphic_fill_originals_2026-11-11/) is widened to 1200x1200 with its own edge colours (graphic_fill square
mode) and replaces the -fill file in place (same media id, alt, position, variant links).

  square_fills.py <storefront products.json dump (list)> <out plan.json>
"""
import json
import shutil
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
import graphic_fill as gf  # noqa: E402
from square_photos import ROOT, RAW, OUT, save  # noqa: E402

gf.set_square(1200)
FILL_ORIG = ROOT / 'docs/backups/graphic_fill_originals_2026-11-11/'

items = {i['out']: i for i in json.load(open(ROOT / 'docs/backups/graphic_fill_before_2026-11-11.json'))['items']}
prods = json.load(open(sys.argv[1]))
plan = []
(ROOT / OUT).mkdir(parents=True, exist_ok=True)
for p in prods:
    for im in p['images']:
        fn = im['src'].split('/')[-1].split('?')[0]
        if '-fill.' not in fn:
            continue
        it = items.get(fn)
        if not it:
            print('NO ORIGINAL', p['handle'], fn)
            continue
        src = Image.open(FILL_ORIG / it['orig_file'])
        name = fn.replace('-fill', '-sq')
        dst = ROOT / OUT / name
        if not dst.exists():
            w, h = src.size
            if 0.98 < w / h < 1.02:
                shutil.copy(FILL_ORIG / it['orig_file'], dst) if Path(it['orig_file']).suffix == dst.suffix else save(src, dst)
            else:
                save(gf.auto(src), dst)
        plan.append({'id': it['mid'], 'originalSource': RAW + OUT + name, 'filename': name,
                     'product': p['handle'], 'vendor': p['vendor'], 'from': list(src.size)})
json.dump(plan, open(sys.argv[2], 'w'), indent=1)
print(len(plan))

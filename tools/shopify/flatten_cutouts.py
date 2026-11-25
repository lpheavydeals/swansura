"""Flatten transparent cut-out photos onto the emerald tint #EEF3F0 (25 Nov 2026).

Why: Shopify's CDN serves transparent images to iPhones (Safari, Instagram/Facebook in-app browsers) as PNG,
5-7x heavier than the WebP that Android gets; an opaque image is served as WebP to every browser. The theme already
paints #EEF3F0 behind every *-cutout file, so a flattened file looks the same on the site.

python3 tools/shopify/flatten_cutouts.py <media.json> <outdir>
  media.json: [{"id": "gid://shopify/MediaImage/..", "url": "https://cdn.shopify.com/...-cutout.webp?v=..", "alt": ".."}]
  Writes <outdir>/<same file name>.webp (opaque, 1200x1500, WebP q86) + <outdir>/plan.json (id, filename, before bytes,
  after bytes) and keeps each original in <outdir>/orig/ (undo = fileUpdate back to the original).
"""
import io, json, os, sys, urllib.request
from PIL import Image

TINT = (0xEE, 0xF3, 0xF0)

def fetch(url):
    req = urllib.request.Request(url, headers={'Accept': 'image/webp,*/*', 'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=60).read()

def main(src, out):
    media = json.load(open(src))
    os.makedirs(os.path.join(out, 'orig'), exist_ok=True)
    plan = []
    for m in media:
        base = m['url'].split('?')[0]
        name = base.rsplit('/', 1)[1]
        raw = fetch(base)
        open(os.path.join(out, 'orig', name), 'wb').write(raw)
        im = Image.open(io.BytesIO(raw))
        im.load()
        if im.mode not in ('RGBA', 'LA', 'PA') and 'transparency' not in im.info:
            plan.append({**m, 'filename': name, 'skip': 'already opaque'}); continue
        im = im.convert('RGBA')
        bg = Image.new('RGBA', im.size, TINT + (255,))
        flat = Image.alpha_composite(bg, im).convert('RGB')
        buf = io.BytesIO(); flat.save(buf, 'WEBP', quality=86, method=6)
        open(os.path.join(out, name), 'wb').write(buf.getvalue())
        plan.append({**m, 'filename': name, 'before': len(raw), 'after': buf.tell(), 'size': flat.size})
    json.dump(plan, open(os.path.join(out, 'plan.json'), 'w'), indent=1)
    print(len(plan), 'files;', sum(1 for p in plan if 'skip' in p), 'skipped')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

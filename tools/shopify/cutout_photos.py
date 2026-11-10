"""Cut-out product photos for the 'single background' look (user, 10 Nov 2026: Option B, soft emerald tint #EEF3F0,
trial brand first).

For each input photo: remove the background (rembg, birefnet-general-lite: isnet-general-use lost pale box faces, e.g. Mugler Angel Elixir), make everything inside the product outline
solid (white box faces were coming out semi-transparent), trim, place on a transparent 1200x1500 (4:5) canvas at a
fixed size/position with a soft floor shadow, save as <handle>-cutout.webp (alpha). The theme paints the background
colour, so it can be changed later without re-editing photos. Also writes a review sheet on the chosen colour.

Run: python3 tools/shopify/cutout_photos.py <in_dir with <handle>.webp> <out_dir> [#EEF3F0] [rembg model]
Needs: pip install "rembg[cpu]" scipy
"""
import sys, pathlib
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
from scipy import ndimage
from rembg import remove, new_session

W, H = 1200, 1500
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
bg = sys.argv[3] if len(sys.argv) > 3 else '#EEF3F0'
out.mkdir(parents=True, exist_ok=True)
session = new_session(sys.argv[4] if len(sys.argv) > 4 else 'birefnet-general-lite')

def cutout(path):
    im = Image.open(path).convert('RGB')
    a = np.array(remove(im, session=session).split()[-1]).astype(float)
    solid = ndimage.binary_fill_holes(a > 25)
    lab, n = ndimage.label(solid)                        # drop specks: keep pieces >= 1% of the largest
    if n > 1:
        sizes = ndimage.sum(solid, lab, range(1, n + 1))
        solid = np.isin(lab, [i + 1 for i, s in enumerate(sizes) if s >= sizes.max() * 0.01])
    core = ndimage.binary_erosion(solid, iterations=3)
    alpha = np.where(core, 255, np.where(solid, np.maximum(a, 128), 0)).astype('uint8')
    rgba = im.copy(); rgba.putalpha(Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(0.8)))
    c = rgba.crop(rgba.getbbox())
    sc = min(W * 0.80 / c.width, H * 0.74 / c.height)
    c = c.resize((max(1, int(c.width * sc)), max(1, int(c.height * sc))), Image.LANCZOS)
    x, y = (W - c.width) // 2, (H - c.height) // 2 + int(H * 0.03)
    sh = Image.new('L', (W, H), 0)
    ImageDraw.Draw(sh).ellipse((x + int(c.width * 0.05), y + c.height - 18, x + int(c.width * 0.95), y + c.height + 22), fill=70)
    shadow = Image.new('RGBA', (W, H), (60, 50, 40, 0)); shadow.putalpha(sh.filter(ImageFilter.GaussianBlur(18)))
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0)); layer.paste(c, (x, y), c)
    return Image.alpha_composite(Image.alpha_composite(Image.new('RGBA', (W, H), (0, 0, 0, 0)), shadow), layer), im

files = sorted(src.glob('*.webp'))
tiles = []
for f in files:
    if (out / f'{f.stem}-cutout.webp').exists():   # resume: already cut
        continue
    cut, orig = cutout(f)
    cut.save(out / f'{f.stem}-cutout.webp', 'WEBP', quality=90, method=6)
    pair = Image.new('RGB', (800, 500), 'white')
    o = orig.copy(); o.thumbnail((400, 500)); pair.paste(o, (0, (500 - o.height) // 2))
    v = Image.new('RGBA', (W, H), bg); v = Image.alpha_composite(v, cut).convert('RGB'); v.thumbnail((400, 500)); pair.paste(v, (400, 0))
    tiles.append(pair); print(f.stem)
cols = 2
sheet = Image.new('RGB', (800 * cols, 500 * ((len(tiles) + cols - 1) // cols)), 'white')
for i, t in enumerate(tiles):
    sheet.paste(t, ((i % cols) * 800, (i // cols) * 500))
sheet.save(out / 'review_sheet.jpg', quality=82)
print(len(tiles), 'done')

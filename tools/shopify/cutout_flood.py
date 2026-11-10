"""Fallback cut-out for studio shots on a plain light background, where rembg models drop pale gift boxes
(white / silver / gold boxes, e.g. Paco Rabanne sets, 10 Nov 2026).

Removes only background-coloured pixels CONNECTED to the photo edge (flood fill from the border), so a white box
inside the outline stays. Background colour = median of the border; a pixel counts as background when it is within
TOL of that colour (or of the local border colour, for soft gradients). Same canvas / placement / shadow as
cutout_photos.py, so the theme treats both the same (<name>-cutout.webp).

Run: python3 tools/shopify/cutout_flood.py <in_dir> <out_dir> [tolerance=22]
"""
import sys, pathlib
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
from scipy import ndimage

W, H = 1200, 1500
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
TOL = float(sys.argv[3]) if len(sys.argv) > 3 else 22
out.mkdir(parents=True, exist_ok=True)


def mask(im):
    a = np.asarray(im).astype(float)
    h, w, _ = a.shape
    # per-row background estimate from the left/right borders (handles vertical gradients)
    edge = np.concatenate([a[:, :8], a[:, -8:]], axis=1)
    rowbg = np.median(edge, axis=1)                                   # h x 3
    rowbg = ndimage.uniform_filter1d(rowbg, 31, axis=0)
    dist = np.sqrt(((a - rowbg[:, None, :]) ** 2).sum(-1))
    cand = dist < TOL
    seeds = np.zeros_like(cand)
    seeds[0, :] = seeds[-1, :] = seeds[:, 0] = seeds[:, -1] = True
    lab, _ = ndimage.label(cand)
    ids = np.unique(lab[seeds & cand])
    bg = np.isin(lab, ids[ids > 0])
    fg = ~bg
    fg = ndimage.binary_opening(fg, iterations=2)
    fg = ndimage.binary_fill_holes(fg)
    lab, n = ndimage.label(fg)
    if n > 1:
        sizes = ndimage.sum(fg, lab, range(1, n + 1))
        fg = np.isin(lab, [i + 1 for i, s in enumerate(sizes) if s >= sizes.max() * 0.01])
    # soft edge: alpha from distance to background colour near the boundary
    soft = np.clip((dist - TOL * 0.5) / (TOL * 0.5), 0, 1) * 255
    core = ndimage.binary_erosion(fg, iterations=2)
    alpha = np.where(core, 255, np.where(fg, np.maximum(soft, 140), 0)).astype('uint8')
    return alpha


def place(im, alpha):
    rgba = im.copy(); rgba.putalpha(Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(0.8)))
    c = rgba.crop(rgba.getbbox())
    sc = min(W * 0.80 / c.width, H * 0.74 / c.height)
    c = c.resize((max(1, int(c.width * sc)), max(1, int(c.height * sc))), Image.LANCZOS)
    x, y = (W - c.width) // 2, (H - c.height) // 2 + int(H * 0.03)
    sh = Image.new('L', (W, H), 0)
    ImageDraw.Draw(sh).ellipse((x + int(c.width * 0.05), y + c.height - 18, x + int(c.width * 0.95), y + c.height + 22), fill=70)
    shadow = Image.new('RGBA', (W, H), (60, 50, 40, 0)); shadow.putalpha(sh.filter(ImageFilter.GaussianBlur(18)))
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0)); layer.paste(c, (x, y), c)
    return Image.alpha_composite(Image.alpha_composite(Image.new('RGBA', (W, H), (0, 0, 0, 0)), shadow), layer)


for f in sorted(src.glob('*.webp')):
    im = Image.open(f).convert('RGB')
    place(im, mask(im)).save(out / f'{f.stem}-cutout.webp', 'WEBP', quality=90, method=6)
    print(f.stem)

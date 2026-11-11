#!/usr/bin/env python3
"""Fit a graphic / infographic / lifestyle photo into the 4:5 product frame WITHOUT a box around it.

User, 11 Nov 2026: graphics (e.g. a brown 'Real People Real Stories' square) sat inside the beige mount
as a separate box. Instead, extend the image to 4:5 with its own edge colours: the band above takes the
colours of the image's top edge, the band below its bottom edge (sides likewise), blurring more the
further from the image, so the graphic flows into the frame. The image itself is not changed.
Output name <handle>-NN-fill.webp; the theme shows '-fill' files edge to edge (no padding, no beige).

Edges that are mostly picture (risk >= 0.35, e.g. a garden scene) use fill_blur instead.

  graphic_fill.py <in_dir> <out_dir>   (every *.webp/*.jpg/*.png in in_dir -> out_dir/<stem>-fill.webp)
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter1d

OW, OH = 1200, 1500


def _band(edge, n, width, med):
    """edge: (k, L, 3) strip at the image border (row 0 = outermost). Returns (n, L, 3) band, row 0 next to the image.
    Where something (hair, a bottle) touches the edge, the band fades from that colour into the edge's
    background colour within a short distance instead of smearing it across the whole band."""
    e = edge.mean(axis=0)                         # (L,3)
    near = e[np.linalg.norm(e - med, axis=1) < 45]  # this edge's background: pixels close to the image's border colour
    med = np.median(near, axis=0) if len(near) > len(e) * 0.15 else np.median(e, axis=0)
    dev = np.clip(np.linalg.norm(e - med, axis=1) / 60.0, 0, 1)        # 0 = background, 1 = an object
    dev = gaussian_filter1d(dev, width / 30, mode='nearest')
    bg = e * (1 - dev[:, None]) + med * dev[:, None]                    # edge with objects replaced by background
    out = np.empty((n, e.shape[0], 3), np.float32)
    s0, s1 = max(2.0, width / 60), width / 6      # blur next to the image -> far away
    fade = max(8, n * 0.45)
    for d in range(n):
        t = d / max(1, n - 1)
        s = s0 + (s1 - s0) * t
        b = gaussian_filter1d(e, s, axis=0, mode='nearest') if d else e
        g = gaussian_filter1d(bg, s, axis=0, mode='nearest')
        r = np.clip(d / fade, 0, 1)
        a = (dev * r * r * (3 - 2 * r))[:, None]
        out[d] = b * (1 - a) + g * a
    return out


def fill_blur(im):
    """For full-bleed scenes (an edge that is all picture, no plain background): the frame shows a blurred,
    enlarged copy of the photo itself, and the photo fades into it over its outer few percent."""
    from PIL import ImageFilter
    im = im.convert('RGB')
    w, h = im.size
    if abs(w / h - 0.8) < 0.01:
        return im.resize((OW, OH), Image.LANCZOS)
    sc = max(OW / w, OH / h)
    bg = im.resize((round(w * sc), round(h * sc)), Image.LANCZOS)
    bg = bg.crop(((bg.width - OW) // 2, (bg.height - OH) // 2, (bg.width - OW) // 2 + OW, (bg.height - OH) // 2 + OH))
    bg = bg.filter(ImageFilter.GaussianBlur(40))
    bg = Image.blend(bg, Image.new('RGB', bg.size, (255, 255, 255)), 0.08)
    sc = min(OW / w, OH / h)
    fg = im.resize((round(w * sc), round(h * sc)), Image.LANCZOS)
    m = np.ones((fg.height, fg.width), np.float32)
    f = max(6, round(min(fg.size) * 0.04))
    r = np.linspace(0, 1, f)
    r = r * r * (3 - 2 * r)
    if fg.height < OH:
        m[:f] *= r[:, None]; m[-f:] *= r[::-1][:, None]
    if fg.width < OW:
        m[:, :f] *= r[None]; m[:, -f:] *= r[::-1][None]
    bg.paste(fg, ((OW - fg.width) // 2, (OH - fg.height) // 2), Image.fromarray((m * 255).astype(np.uint8)))
    return bg


def edge_risk(im):
    """Share of the edge (the one next to the bands) that is picture rather than plain background."""
    a = np.asarray(im.convert('RGB'), np.float32)
    h, w, _ = a.shape
    if abs(w / h - 0.8) < 0.01:
        return 0.0
    es = [a[:3].mean(0), a[-3:].mean(0)] if w / h > 0.8 else [a[:, :3].mean(1), a[:, -3:].mean(1)]
    return max(float((np.linalg.norm(e - np.median(e, 0), axis=1) > 45).mean()) for e in es)


def auto(im, limit=0.35):
    return fill_blur(im) if edge_risk(im) >= limit else fill(im)


def fill(im):
    im = im.convert('RGB')
    w, h = im.size
    if abs(w / h - 0.8) < 0.01:
        return im.resize((OW, OH), Image.LANCZOS)
    if w / h > 0.8:     # wider than 4:5: bands above and below
        nw, nh = OW, round(h * OW / w)
    else:               # narrower: bands left and right
        nw, nh = round(w * OH / h), OH
    a = np.asarray(im.resize((nw, nh), Image.LANCZOS), np.float32)
    k = 4
    med = np.median(np.concatenate([a[:k].reshape(-1, 3), a[-k:].reshape(-1, 3), a[:, :k].reshape(-1, 3), a[:, -k:].reshape(-1, 3)]), axis=0)
    canvas = np.zeros((OH, OW, 3), np.float32)
    if nw == OW:
        top = (OH - nh) // 2
        bot = OH - nh - top
        canvas[top:top + nh] = a
        if top:
            canvas[:top] = _band(a[:k], top, OW, med)[::-1]
        if bot:
            canvas[top + nh:] = _band(a[-k:][::-1], bot, OW, med)
    else:
        left = (OW - nw) // 2
        right = OW - nw - left
        canvas[:, left:left + nw] = a
        t = a.transpose(1, 0, 2)
        if left:
            canvas[:, :left] = _band(t[:k], left, OH, med)[::-1].transpose(1, 0, 2)
        if right:
            canvas[:, left + nw:] = _band(t[-k:][::-1], right, OH, med).transpose(1, 0, 2)
    return Image.fromarray(np.clip(canvas + np.random.uniform(-.5, .5, canvas.shape), 0, 255).astype(np.uint8))


if __name__ == '__main__':
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.mkdir(parents=True, exist_ok=True)
    for f in sorted(src.iterdir()):
        if f.suffix.lower() in ('.webp', '.jpg', '.jpeg', '.png'):
            auto(Image.open(f)).save(dst / f'{f.stem}-fill.webp', 'WEBP', quality=88, method=6)
            print(f.name)

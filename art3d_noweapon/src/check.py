"""Colour check of a 3D character script against its screenshot.

usage: python3 check.py <name> [<name> ...]   -> chk_<name>.png

Paints the model's front faces and decals as a flat colour map in
screenshot pixels (front-most on top), compares it with the screenshot in
Lab space and marks pixels whose colour clearly differs.  The sheet shows:
screenshot | model colour map | mismatches (red) on a faded screenshot.
"""
import sys
import numpy as np
from PIL import Image, ImageDraw

import lib3d
from compare import IMG, SRC
from overlay import load_scene

S = 3  # display upscale


def to_lab(rgb):
    c = rgb / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ M.T / np.array([0.9505, 1.0, 1.089])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    L = 116 * f[..., 1] - 16
    a = 500 * (f[..., 0] - f[..., 1])
    b = 200 * (f[..., 1] - f[..., 2])
    return np.stack([L, a, b], -1)


def model_map(script, W, H):
    zoom = 2.0
    for line in open(script).read().splitlines():
        if line.startswith('ZOOM'):
            zoom = float(line.split('=')[1])
    scene, _ = load_scene(script)
    items = []
    for p in scene.parts:
        if p.alpha < 1:
            continue
        for fc in p.faces:
            if fc.n[2] <= 0.5:
                continue
            z = float(fc.pts[:, 2].mean())
            col = fc.color if fc.color is not None else p.color
            items.append((z, 0, [(x / zoom, y / zoom) for x, y, _ in fc.pts], col))
            for k, (pts3, dc, _) in enumerate(fc.decals):
                items.append((z, 1 + k, [(x / zoom, y / zoom) for x, y, _ in pts3], dc))
    items.sort(key=lambda t: (t[0], t[1]))
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for _, _, pts, col in items:
        d.polygon(pts, fill=tuple(int(v) for v in col) + (255,))
    return np.asarray(img).astype(np.float32), zoom


def check(name):
    script = f'c3dn_{name}.py'
    shot = np.asarray(Image.open(f'{IMG}/{SRC[name]}.png').convert('RGB')).astype(np.float32)
    H, W = shot.shape[:2]
    mm, zoom = model_map(script, W, H)
    cov = mm[..., 3] > 0
    L1, L2 = to_lab(shot), to_lab(mm[..., :3])
    d = np.sqrt(((L1[..., 0] - L2[..., 0]) * 0.45) ** 2 + (L1[..., 1] - L2[..., 1]) ** 2 + (L1[..., 2] - L2[..., 2]) ** 2)
    bad = cov & (d > 28)
    ys, xs = np.nonzero(cov)
    x0, x1 = max(xs.min() - 6, 0), min(xs.max() + 7, W)
    y0, y1 = max(ys.min() - 6, 0), min(ys.max() + 7, H)
    crop = lambda a: a[y0:y1, x0:x1]
    shot_im = Image.fromarray(crop(shot).astype(np.uint8))
    bg = np.full_like(mm[..., :3], 255)
    mm_rgb = np.where(cov[..., None], mm[..., :3], bg)
    mm_im = Image.fromarray(crop(mm_rgb).astype(np.uint8))
    faded = crop(shot) * 0.35 + 255 * 0.65
    faded[crop(bad)] = (230, 0, 30)
    diff_im = Image.fromarray(faded.astype(np.uint8))
    w, h = x1 - x0, y1 - y0
    sheet = Image.new('RGB', (3 * w * S + 20, h * S), (255, 255, 255))
    for i, im in enumerate((shot_im, mm_im, diff_im)):
        sheet.paste(im.resize((w * S, h * S), Image.NEAREST), (i * (w * S + 10), 0))
    grid = Image.new('RGBA', sheet.size, (0, 0, 0, 0))
    dr = ImageDraw.Draw(grid)
    # grid on the screenshot and model panels, labelled in model units
    for panel in (0, 1):
        ox = panel * (w * S + 10)
        for gx in range(((x0 + 9) // 10) * 10, x1, 10):
            X = ox + (gx - x0) * S
            major = gx % 50 == 0
            dr.line([(X, 0), (X, h * S)], fill=(0, 0, 0, 110) if major else (0, 0, 0, 45), width=1)
            if major:
                dr.text((X + 2, 18), str(int(gx * zoom)), fill=(0, 0, 0, 255))
        for gy in range(((y0 + 9) // 10) * 10, y1, 10):
            Y = (gy - y0) * S
            major = gy % 50 == 0
            dr.line([(ox, Y), (ox + w * S, Y)], fill=(0, 0, 0, 110) if major else (0, 0, 0, 45), width=1)
            if major:
                dr.text((ox + 2, Y + 2), str(int(gy * zoom)), fill=(0, 0, 0, 255))
    sheet = Image.alpha_composite(sheet.convert('RGBA'), grid).convert('RGB')
    dr = ImageDraw.Draw(sheet)
    score = bad.sum() / max(cov.sum(), 1)
    dr.rectangle((0, 0, 190, 16), fill=(0, 0, 0))
    dr.text((4, 3), f'{name} {score * 100:.1f}%', fill=(255, 255, 0))
    sheet.save(f'chk_{name}.png')
    return score


if __name__ == '__main__':
    for n in sys.argv[1:]:
        print(f'{n:24s} {check(n) * 100:5.1f}%')

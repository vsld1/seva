"""Draw a 3D character script's front outlines on top of its screenshot.

usage: python3 overlay.py c3dn_<name>.py out.png [crop x0 y0 x1 y1 in screenshot px]

Model x/y are screenshot pixels * ZOOM; front-facing faces (and decals) are
projected straight onto the screenshot so any misalignment is obvious.
"""
import sys
import numpy as np
from PIL import Image, ImageDraw

import lib3d
from compare import IMG, SRC

SHOW = 4  # upscale of the screenshot in the debug image


def load_scene(script):
    box = {}
    src = open(script).read()
    g = {'__name__': '__main__'}
    lib3d_render = lib3d.render
    lib3d.render = lambda s, path, **kw: box.setdefault('s', s)
    sys_argv = sys.argv
    sys.argv = [script, '/dev/null']
    try:
        exec(compile(src.replace('from lib3d import *', 'from lib3d import *\nrender = lib3d.render'), script, 'exec'),
             {**g, 'lib3d': lib3d})
    finally:
        lib3d.render = lib3d_render
        sys.argv = sys_argv
    return box['s'], g


def main():
    script, out = sys.argv[1], sys.argv[2]
    name = script.split('c3dn_')[-1].split('c3d_')[-1][:-3]
    src_txt = open(script).read()
    zoom = 2.0
    for line in src_txt.splitlines():
        if line.startswith('ZOOM'):
            zoom = float(line.split('=')[1])
    scene, _ = load_scene(script)
    shot = Image.open(f'{IMG}/{SRC[name]}.png').convert('RGB')
    W, H = shot.size
    im = shot.resize((W * SHOW, H * SHOW), Image.NEAREST).convert('RGBA')
    lay = Image.new('RGBA', im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    k = SHOW / zoom
    for p in scene.parts:
        for fc in p.faces:
            if fc.n[2] > 0.5:
                pts = [(x * k, y * k) for x, y, _ in fc.pts]
                d.line(pts + [pts[0]], fill=(255, 0, 200, 170), width=2)
            for pts3, col, _ in fc.decals:
                if fc.n[2] > 0.5:
                    pts = [(x * k, y * k) for x, y, _ in pts3]
                    d.line(pts + [pts[0]], fill=(0, 230, 255, 190), width=2)
    if len(sys.argv) >= 7:
        x0, y0, x1, y1 = (int(v) * SHOW for v in sys.argv[3:7])
    else:
        allp = np.concatenate([f.pts for p in scene.parts for f in p.faces])
        x0, y0 = (allp[:, :2].min(0) / zoom - 12) * SHOW
        x1, y1 = (allp[:, :2].max(0) / zoom + 12) * SHOW
    x0, y0 = int(max(x0, 0)), int(max(y0, 0))
    x1, y1 = int(min(x1, im.width)), int(min(y1, im.height))
    # faint grid every 10 screenshot px, labelled in model units every 50 px
    step = 10 * SHOW
    for gx in range((x0 // step + 1) * step, x1, step):
        major = (gx // SHOW) % 50 == 0
        d.line([(gx, y0), (gx, y0 + (14 if major else 6))], fill=(0, 0, 0, 255), width=1)
        if major:
            d.text((gx + 2, y0 + 14), str(int(gx / SHOW * zoom)), fill=(0, 0, 0, 255))
    for gy in range((y0 // step + 1) * step, y1, step):
        major = (gy // SHOW) % 50 == 0
        d.line([(x0, gy), (x0 + (14 if major else 6), gy)], fill=(0, 0, 0, 255), width=1)
        if major:
            d.text((x0 + 16, gy - 5), str(int(gy / SHOW * zoom)), fill=(0, 0, 0, 255))
    im = Image.alpha_composite(im, lay).convert('RGB')
    im = im.crop((x0, y0, x1, y1))
    if im.height > 1150:
        im = im.resize((round(im.width * 1150 / im.height), 1150), Image.LANCZOS)
    im.save(out)


if __name__ == '__main__':
    main()

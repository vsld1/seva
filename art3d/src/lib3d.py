"""Tiny z-buffer renderer for blocky, cel-shaded "voxel sticker" characters.

Model space: x right, y DOWN, z toward the viewer (x/y use the same units as
the 2D drawings).  A character is a set of parts - boxes, extruded polygons,
cylinders and low-poly spheres.  Flat decals (eyes, stripes, patches ...) are
painted onto a part's faces.

`render` shows the model from the front and slightly above with a one-point
perspective: tops of blocks are visible, protruding things show their inner
sides.  Faces get flat tones (light tops, darker sides), parts cast soft cel
shadows, blocks are separated by thin black lines and the whole figure gets
a thick black outline.  The result is an anti-aliased RGBA PNG.
"""
import math

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

OUT = (21, 21, 27)


# ---------------------------------------------------------------- colours
def rgb(c):
    if isinstance(c, str):
        c = c.lstrip('#')
        return np.array([int(c[i:i + 2], 16) for i in (0, 2, 4)], np.float32)
    return np.asarray(c, np.float32)


def tint(c, f):
    """Lighten (f > 0) toward white or darken (f < 0) a colour."""
    c = rgb(c)
    return c + (255 - c) * f if f >= 0 else c * (1 + f)


def mix(a, b, t):
    return rgb(a) * (1 - t) + rgb(b) * t


# ---------------------------------------------------------------- 2D shapes
def R(x0, y0, x1, y1):
    x0, x1 = sorted((x0, x1))
    y0, y1 = sorted((y0, y1))
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def D(cx, cy, r, ry=None):
    ry = r if ry is None else ry
    return [(cx, cy - ry), (cx + r, cy), (cx, cy + ry), (cx - r, cy)]


def E(cx, cy, rx, ry, n=40):
    return [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]


def C(cx, cy, r, n=40):
    return E(cx, cy, r, r, n)


def P(*pts):
    return [tuple(p) for p in pts]


def centroid(pts):
    xs, ys = zip(*pts)
    return sum(xs) / len(xs), sum(ys) / len(ys)


def rot(pts, ang, c=None):
    """Rotate 2D points clockwise on screen (same sense as SVG rotate)."""
    c = centroid(pts) if c is None else c
    a = math.radians(ang)
    ca, sa = math.cos(a), math.sin(a)
    return [(c[0] + (x - c[0]) * ca - (y - c[1]) * sa, c[1] + (x - c[0]) * sa + (y - c[1]) * ca) for x, y in pts]


def RR(cx, cy, w, h, ang=0):
    return rot(R(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), ang, (cx, cy))


def B(a, b, w):
    """A stick of width w from point a to point b."""
    (ax, ay), (bx, by) = a, b
    L = math.hypot(bx - ax, by - ay) or 1
    nx, ny = -(by - ay) / L * w / 2, (bx - ax) / L * w / 2
    return [(ax + nx, ay + ny), (bx + nx, by + ny), (bx - nx, by - ny), (ax - nx, ay - ny)]


def star(cx, cy, r1, r2, n, a0=-90):
    return [(cx + (r1 if i % 2 == 0 else r2) * math.cos(math.radians(a0 + 180 * i / n)),
             cy + (r1 if i % 2 == 0 else r2) * math.sin(math.radians(a0 + 180 * i / n))) for i in range(2 * n)]


def _inside(pt, poly):
    x, y = pt
    c = False
    for i in range(len(poly)):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


# ---------------------------------------------------------------- 3D rotation
def _rotm(rz=0, ry=0, rx=0):
    a, b, g = (math.radians(v) for v in (rz, ry, rx))
    Rz = np.array([[math.cos(a), -math.sin(a), 0], [math.sin(a), math.cos(a), 0], [0, 0, 1]])
    Ry = np.array([[math.cos(b), 0, math.sin(b)], [0, 1, 0], [-math.sin(b), 0, math.cos(b)]])
    Rx = np.array([[1, 0, 0], [0, math.cos(g), -math.sin(g)], [0, math.sin(g), math.cos(g)]])
    return Rx @ Ry @ Rz


DIRS = {'front': (0, 0, 1), 'back': (0, 0, -1), 'top': (0, -1, 0), 'bottom': (0, 1, 0),
        'left': (-1, 0, 0), 'right': (1, 0, 0)}


class Face:
    def __init__(self, pts, part, group):
        self.pts = np.asarray(pts, np.float64)
        n = np.zeros(3)
        for i in range(len(self.pts)):  # Newell's method
            a, b = self.pts[i], self.pts[(i + 1) % len(self.pts)]
            n += np.array([(a[1] - b[1]) * (a[2] + b[2]), (a[2] - b[2]) * (a[0] + b[0]), (a[0] - b[0]) * (a[1] + b[1])])
        self.n = n / (np.linalg.norm(n) or 1)
        self.part, self.group = part, group
        self.color = None      # per-face colour override
        self.decals = []

    def orient(self, outward):
        if self.n @ outward < 0:
            self.n = -self.n
            self.pts = self.pts[::-1].copy()


class Part:
    def __init__(self, color, line=True, cast=True, alpha=1.0, receive=True):
        self.color, self.line, self.cast, self.alpha, self.receive = rgb(color), line, cast, alpha, receive
        self.faces = []

    def face(self, key='front'):
        d = np.array(DIRS[key], float) if isinstance(key, str) else np.asarray(key, float)
        return max(self.faces, key=lambda f: f.n @ d)

    def paint(self, key, color):
        """Give one face its own colour (e.g. a different top)."""
        self.face(key).color = rgb(color)
        return self

    def f(self, pts, color, line=False, key='front'):
        """Paint a flat decal on a face.  2D points: (x, y) for front/back,
        (x, z) for top/bottom and (z, y) for left/right faces."""
        fc = self.face(key)
        n, h = fc.n, fc.n @ fc.pts[0]
        ax = int(np.argmax(np.abs(n)))
        out = []
        for p in pts:
            if ax == 2:
                x, y = p
                out.append((x, y, (h - n[0] * x - n[1] * y) / n[2]))
            elif ax == 1:
                x, z = p
                out.append((x, (h - n[0] * x - n[2] * z) / n[1], z))
            else:
                z, y = p
                out.append(((h - n[1] * y - n[2] * z) / n[0], y, z))
        fc.decals.append((np.array(out), rgb(color), line))
        return self


class Scene:
    def __init__(self):
        self.parts = []

    def _part(self, faces, groups, color, center, **kw):
        p = Part(color, **kw)
        for pts, g in zip(faces, groups):
            fc = Face(pts, p, g)
            fc.orient(fc.pts.mean(0) - center)
            p.faces.append(fc)
        self.parts.append(p)
        return p

    def box(self, x0, y0, x1, y1, z0, z1, color, rz=0, ry=0, rx=0, pivot=None, **kw):
        x0, x1 = sorted((x0, x1))
        y0, y1 = sorted((y0, y1))
        z0, z1 = sorted((z0, z1))
        v = np.array([[x, y, z] for z in (z0, z1) for y in (y0, y1) for x in (x0, x1)], float)
        c = np.array([(x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2])
        if rz or ry or rx:
            pv = c if pivot is None else np.asarray(pivot, float)
            v = (v - pv) @ _rotm(rz, ry, rx).T + pv
            c = (c - pv) @ _rotm(rz, ry, rx).T + pv
        # vertex index = zi*4 + yi*2 + xi
        quads = [(4, 5, 7, 6), (0, 1, 3, 2), (0, 1, 5, 4), (2, 3, 7, 6), (0, 2, 6, 4), (1, 3, 7, 5)]
        return self._part([v[list(q)] for q in quads], range(6), color, c, **kw)

    def cube(self, cx, cy, cz, w, h, d, color, **kw):
        return self.box(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, cz - d / 2, cz + d / 2, color, **kw)

    def prism(self, pts, z0, z1, color, smooth=False, rz=0, ry=0, rx=0, pivot=None, **kw):
        """Extrude a 2D polygon (x, y) between z0 and z1."""
        pts = [tuple(p) for p in pts]
        z0, z1 = sorted((z0, z1))
        n = len(pts)
        front = [(x, y, z1) for x, y in pts]
        back = [(x, y, z0) for x, y in pts]
        faces, groups, outs = [front, back], [0, 1], [(0, 0, 1), (0, 0, -1)]
        for i in range(n):
            (ax, ay), (bx, by) = pts[i], pts[(i + 1) % n]
            faces.append([(ax, ay, z0), (bx, by, z0), (bx, by, z1), (ax, ay, z1)])
            groups.append(2 if smooth else 2 + i)
            nx, ny = by - ay, -(bx - ax)
            L = math.hypot(nx, ny) or 1
            mid = ((ax + bx) / 2 + nx / L * 0.01, (ay + by) / 2 + ny / L * 0.01)
            s = -1 if _inside(mid, pts) else 1
            outs.append((s * nx, s * ny, 0))
        cx, cy = centroid(pts)
        center = np.array([cx, cy, (z0 + z1) / 2])
        faces = [np.array(f, float) for f in faces]
        outs = [np.array(o, float) for o in outs]
        if rz or ry or rx:
            pv = center if pivot is None else np.asarray(pivot, float)
            M = _rotm(rz, ry, rx)
            faces = [(f - pv) @ M.T + pv for f in faces]
            outs = [M @ o for o in outs]
            center = (center - pv) @ M.T + pv
        p = Part(color, **kw)
        for pts3, g, o in zip(faces, groups, outs):
            fc = Face(pts3, p, g)
            fc.orient(o)
            p.faces.append(fc)
        self.parts.append(p)
        return p

    def cyl(self, cx, cy, z0, z1, r, color, n=28, ry_=None, **kw):
        """Cylinder along z (coins, clock faces, portholes)."""
        return self.prism(E(cx, cy, r, r if ry_ is None else ry_, n), z0, z1, color, smooth=True, **kw)

    def sphere(self, cx, cy, cz, r, color, nlat=7, nlon=14, **kw):
        c = np.array([cx, cy, cz], float)
        faces = []
        for i in range(nlat):
            t0, t1 = math.pi * i / nlat, math.pi * (i + 1) / nlat
            for j in range(nlon):
                p0, p1 = 2 * math.pi * j / nlon, 2 * math.pi * (j + 1) / nlon
                q = []
                for t, ph in ((t0, p0), (t0, p1), (t1, p1), (t1, p0)):
                    q.append(c + r * np.array([math.sin(t) * math.cos(ph), -math.cos(t), math.sin(t) * math.sin(ph)]))
                if i == 0:
                    q = [q[0], q[2], q[3]]
                elif i == nlat - 1:
                    q = [q[0], q[1], q[2]]
                faces.append(q)
        return self._part(faces, [0] * len(faces), color, c, **kw)


# ---------------------------------------------------------------- shading
def face_tone(c, n):
    c = rgb(c)
    up, dn = max(-n[1], 0) ** 2, max(n[1], 0) ** 2
    lf, rt = max(-n[0], 0) ** 2, max(n[0], 0) ** 2
    fr, bk = max(n[2], 0) ** 2, max(-n[2], 0) ** 2
    top = c + (255 - c) * 0.30
    col = fr * c + up * top + dn * c * 0.62 + lf * c * 0.86 + rt * c * 0.74 + bk * c * 0.70
    return col / (up + dn + lf + rt + fr + bk)


def _poly_mask(pts, x0, y0, w, h):
    img = Image.new('L', (w, h), 0)
    ImageDraw.Draw(img).polygon([(x - x0, y - y0) for x, y in pts], fill=1)
    return np.asarray(img, dtype=bool)


def render(scene, path, size=1024, ss=3, elev=16.0, dist=2.4, light=(0.55, 1.0, -0.8),
           out_w=8.0, in_w=3.2, shade=0.80, margin=16, bg=None):
    faces = [f for p in scene.parts if p.alpha >= 1 for f in p.faces]
    glass = [f for p in scene.parts if p.alpha < 1 for f in p.faces]
    allp = np.concatenate([f.pts for f in faces + glass])
    lo, hi = allp.min(0), allp.max(0)
    ctr = (lo + hi) / 2
    ext = max(hi[0] - lo[0], hi[1] - lo[1])

    e = math.radians(elev)
    Cam = ctr + np.array([0, -math.sin(e), math.cos(e)]) * dist * ext
    fw = ctr - Cam
    fw /= np.linalg.norm(fw)
    rt = np.cross(np.array([0, -1.0, 0]), fw)
    rt /= np.linalg.norm(rt)
    up = np.cross(fw, rt)
    Mc = np.stack([rt, up, fw])

    def proj(pts):
        q = (pts - Cam) @ Mc.T
        return np.stack([q[:, 0] / q[:, 2], -q[:, 1] / q[:, 2]], 1), q

    vis = []
    for fc in faces + glass:
        s, q = proj(fc.pts)
        nc = Mc @ fc.n
        h = nc @ q[0]
        if h < 0:
            fc.s, fc.nc, fc.h = s, nc, h
            vis.append(fc)
    vis_op = [f for f in vis if f.part.alpha >= 1]
    vis_gl = [f for f in vis if f.part.alpha < 1]

    sp = np.concatenate([f.s for f in vis])
    smin, smax = sp.min(0), sp.max(0)
    S, m = size * ss, margin * ss
    F = (S - 2 * m) / max(smax - smin)
    W = int(math.ceil((smax[0] - smin[0]) * F + 2 * m))
    H = int(math.ceil((smax[1] - smin[1]) * F + 2 * m))
    W, H = W + (-W) % ss, H + (-H) % ss
    ox, oy = m - smin[0] * F, m - smin[1] * F

    def raster(fc, pts2):
        x0 = max(int(math.floor(pts2[:, 0].min())), 0)
        x1 = min(int(math.ceil(pts2[:, 0].max())) + 1, W)
        y0 = max(int(math.floor(pts2[:, 1].min())), 0)
        y1 = min(int(math.ceil(pts2[:, 1].max())) + 1, H)
        if x1 <= x0 or y1 <= y0:
            return None
        mk = _poly_mask(pts2, x0, y0, x1 - x0, y1 - y0)
        ys, xs = np.nonzero(mk)
        if len(ys) == 0:
            return None
        ys, xs = ys + y0, xs + x0
        a = (xs + 0.5 - ox) / F
        b = -(ys + 0.5 - oy) / F
        z = fc.h / (fc.nc[0] * a + fc.nc[1] * b + fc.nc[2])
        return ys, xs, z

    zbuf = np.full((H, W), np.inf, np.float32)
    fid = np.full((H, W), -1, np.int32)
    for i, fc in enumerate(vis_op):
        r = raster(fc, fc.s * F + [ox, oy])
        if r is None:
            continue
        ys, xs, z = r
        ok = z <= zbuf[ys, xs] * (1 + 2e-6)
        zbuf[ys[ok], xs[ok]] = z[ok]
        fid[ys[ok], xs[ok]] = i

    # per-face tone, line id, light facing
    L = np.asarray(light, float)
    L /= np.linalg.norm(L)
    nf = len(vis_op)
    tones = np.zeros((nf + 1, 3), np.float32)
    lids = np.zeros(nf + 1, np.int32)
    lit = np.zeros(nf + 1, bool)
    normals = np.zeros((nf + 1, 3), np.float32)
    lid_line = [False]
    gkey = {}
    for i, fc in enumerate(vis_op):
        tones[i] = face_tone(fc.color if fc.color is not None else fc.part.color, fc.n)
        k = (id(fc.part), fc.group)
        if k not in gkey:
            gkey[k] = len(lid_line)
            lid_line.append(fc.part.line)
        lids[i] = gkey[k]
        lit[i] = fc.n @ L < -0.05 and fc.part.receive
        normals[i] = fc.n
    fig = fid >= 0
    col = tones[fid]
    lid = np.where(fig, lids[fid], 0)

    # decals, clipped to the visible part of their face
    for i, fc in enumerate(vis_op):
        for pts3, dc, dline in fc.decals:
            s, _ = proj(pts3)
            r = raster(fc, s * F + [ox, oy])
            if r is None:
                continue
            ys, xs, _ = r
            ok = fid[ys, xs] == i
            ys, xs = ys[ok], xs[ok]
            col[ys, xs] = face_tone(dc, fc.n)
            if dline:
                lid[ys, xs] = len(lid_line)
                lid_line.append(True)

    # cast shadows from a directional light (orthographic shadow map)
    lr = np.cross(L, np.array([0, 0, 1.0]))
    lr /= np.linalg.norm(lr)
    lu = np.cross(L, lr)
    Ml = np.stack([lr, lu, L])
    casters = [f for f in faces if f.part.cast and f.n @ L < 0]
    lp = np.concatenate([f.pts for f in casters]) @ Ml.T
    lmin, lmax = lp.min(0), lp.max(0)
    SM = 2048
    ls = (SM - 4) / max(lmax[0] - lmin[0], lmax[1] - lmin[1])
    smap = np.full((SM, SM), np.inf, np.float32)
    for fc in casters:
        q = fc.pts @ Ml.T
        p2 = (q[:, :2] - lmin[:2]) * ls + 2
        nl = Ml @ fc.n
        hl = nl @ q[0]
        x0, x1 = max(int(p2[:, 0].min()), 0), min(int(math.ceil(p2[:, 0].max())) + 1, SM)
        y0, y1 = max(int(p2[:, 1].min()), 0), min(int(math.ceil(p2[:, 1].max())) + 1, SM)
        if x1 <= x0 or y1 <= y0 or abs(nl[2]) < 1e-6:
            continue
        mk = _poly_mask(p2, x0, y0, x1 - x0, y1 - y0)
        ys, xs = np.nonzero(mk)
        ys, xs = ys + y0, xs + x0
        X = (xs + 0.5 - 2) / ls + lmin[0]
        Y = (ys + 0.5 - 2) / ls + lmin[1]
        d = (hl - nl[0] * X - nl[1] * Y) / nl[2]
        np.minimum.at(smap, (ys, xs), d.astype(np.float32))
    ys, xs = np.nonzero(fig)
    fi = fid[ys, xs]
    sel = lit[fi]
    ys, xs, fi = ys[sel], xs[sel], fi[sel]
    zc = zbuf[ys, xs]
    a = (xs + 0.5 - ox) / F
    b = -(ys + 0.5 - oy) / F
    wp = Cam + (np.stack([a * zc, b * zc, zc], 1) @ Mc) + normals[fi] * (2.5 / ls * 2)
    q = wp @ Ml.T
    ix = np.clip(((q[:, 0] - lmin[0]) * ls + 2).astype(int), 0, SM - 1)
    iy = np.clip(((q[:, 1] - lmin[1]) * ls + 2).astype(int), 0, SM - 1)
    dark = q[:, 2] > smap[iy, ix] + 3.0 / ls
    col[ys[dark], xs[dark]] *= shade

    # lines between blocks and a thick silhouette outline
    lline = np.array(lid_line, bool)
    edge = np.zeros((H, W), bool)
    for dy, dx in ((0, 1), (1, 0)):
        a_, b_ = lid[:H - dy, :W - dx], lid[dy:, dx:]
        fa, fb = fig[:H - dy, :W - dx], fig[dy:, dx:]
        d = (a_ != b_) & fa & fb & lline[a_] & lline[b_]
        edge[:H - dy, :W - dx] |= d
        edge[dy:, dx:] |= d
    inner = ndimage.distance_transform_edt(~edge) <= in_w * ss / 2
    ring = (~fig) & (ndimage.distance_transform_edt(~fig) <= out_w * ss)
    img = np.zeros((H, W, 4), np.float32)
    img[..., :3] = col
    img[..., 3] = fig * 255.0
    img[inner & fig, :3] = OUT
    img[ring, :3] = OUT
    img[ring, 3] = 255

    # translucent parts (glow, beams, glass) on top
    for fc in sorted(vis_gl, key=lambda f: -float(((f.pts - Cam) @ fw).mean())):
        r = raster(fc, fc.s * F + [ox, oy])
        if r is None:
            continue
        ys, xs, z = r
        ok = z < zbuf[ys, xs]
        ys, xs = ys[ok], xs[ok]
        a_ = fc.part.alpha
        c_ = face_tone(fc.color if fc.color is not None else fc.part.color, fc.n)
        cur_a = img[ys, xs, 3:4] / 255
        new_a = a_ + cur_a * (1 - a_)
        img[ys, xs, :3] = (c_ * a_ + img[ys, xs, :3] * cur_a * (1 - a_)) / np.maximum(new_a, 1e-6)
        img[ys, xs, 3] = new_a[:, 0] * 255

    if bg is not None:
        base = np.zeros_like(img)
        base[..., :3] = rgb(bg)
        base[..., 3] = 255
        a_ = img[..., 3:4] / 255
        img[..., :3] = img[..., :3] * a_ + base[..., :3] * (1 - a_)
        img[..., 3] = 255
    im = Image.fromarray(np.clip(np.rint(img), 0, 255).astype(np.uint8), 'RGBA')
    im = im.convert('RGBa').resize((W // ss, H // ss), Image.BOX).convert('RGBA')
    im.save(path)
    return im


# ---------------------------------------------------------------- helpers
def gem(s, cx, cy, r, z0, z1, col, ry=None, **kw):
    """Raised diamond gem with a light upper-left and a dark lower-right facet."""
    ry = r if ry is None else ry
    return s.prism(D(cx, cy, r, ry), z0, z1, col, **kw).f(
        P((cx, cy - ry), (cx, cy), (cx - r, cy)), tint(col, 0.45)).f(
        P((cx, cy), (cx + r, cy), (cx, cy + ry)), tint(col, -0.22))


def crystal(s, cx, cy, w, h, col, ang=0, z=0, d=None, **kw):
    """Upright crystal: a block rotated in the picture plane with a pointed tip."""
    d = w if d is None else d
    tip = min(w * 0.55, h * 0.3)
    pts = [(cx - w / 2, cy + h / 2), (cx - w / 2, cy - h / 2 + tip), (cx, cy - h / 2),
           (cx + w / 2, cy - h / 2 + tip), (cx + w / 2, cy + h / 2)]
    return s.prism(rot(pts, ang, (cx, cy)), z - d / 2, z + d / 2, col, **kw)

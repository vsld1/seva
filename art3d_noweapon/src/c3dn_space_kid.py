import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1120 - x
BOTH = (lambda x: x, M)
NAVY, GRAY, FACE, INDIGO = '#0A0A5A', '#C8C4D8', '#DCC4F8', '#1A0AD8'

# little planet with a ring, floating by the shoulder
s.sphere(136, 492, 20, 52, '#20A8F8')
s.cyl(136, 500, 14, 26, 96, '#F8ECC8', ry_=22, rz=-12)

# antenna
s.box(413, 60, 425, 140, -6, 6, '#B8A8D0')
s.box(404, 36, 434, 64, -15, 15, '#FFFFFF')

# boots, legs
for f in BOTH:
    s.box(f(388), 884, f(556), 966, -70, 92, '#1A20C8').f(R(f(388), 928, f(556), 966), '#2A108A')
    s.box(f(390), 786, f(554), 888, -66, 66, '#050540')

# torso with stars, chest panel with three lights, belt
torso = s.box(383, 562, M(383), 792, -90, 90, NAVY)
for x, y, sz in ((420, 676, 12), (662, 710, 14), (496, 732, 10)):
    torso.f(R(x, y, x + sz, y + sz), '#FFFFFF')
panel = s.box(455, 574, M(455), 694, 88, 100, '#BEBAD0')
for x, col in ((490, '#FFF000'), (560, '#10F0F0'), (630, '#F8A0F0')):
    s.box(x - 15, 604, x + 15, 634, 98, 108, col)
s.box(370, 728, M(370), 782, -94, 94, GRAY)

# arms with grey cuffs
for f in BOTH:
    s.box(f(238), 472, f(384), 812, -66, 66, NAVY)
    s.box(f(226), 676, f(396), 718, -70, 70, GRAY)

# collar, glass helmet, face panel, visor band
s.box(333, 516, M(333), 572, -96, 96, GRAY)
s.box(332, 128, M(332), 526, -110, 96, '#C4D4F8')
head = s.box(383, 190, M(383), 522, -80, 102, FACE)
s.box(370, 136, M(370), 196, -90, 104, INDIGO)
for x in (455, M(515)):
    head.f(R(x, 322, x + 60, 408), INDIGO).f(R(x + 10, 334, x + 28, 360), '#C8B8F8')
for f in BOTH:
    head.f(R(f(418), 414, f(466), 440), '#F090E8')
head.f(R(535, 456, 585, 472), '#3A10B8')

# sparkles around the helmet
for x, y, r in [(400, 246, 22), (515, 234, 20), (645, 234, 22), (310, 262, 18), (268, 286, 14), (296, 328, 14),
                (346, 346, 14), (756, 246, 20), (790, 336, 16), (830, 266, 18), (852, 294, 16), (836, 316, 14)]:
    inside = 332 < x < 788
    s.cube(x, y, 112 if inside else 40, r * 1.2, r * 1.2, r * 1.2, '#FFFFF4', rz=45, ry=20)

render(s, sys.argv[1])

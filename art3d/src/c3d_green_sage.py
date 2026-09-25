import sys
from lib3d import *

s = Scene()
M = lambda x: 1076 - x
BOTH = (lambda x: x, M)
G, G_DK, MINT, SKIN, BEARD = '#10A850', '#0A5A2A', '#48E0A8', '#FCE0C4', '#F6F0EC'

# crooked, stacked wizard hat
s.cube(426, 70, -20, 52, 56, 50, G_DK, rz=-30)
s.cube(456, 106, -10, 88, 66, 80, MINT, rz=-12)
s.cube(496, 166, 0, 168, 90, 150, G, rz=-5)
s.box(390, 188, M(390) + 20, 280, -100, 100, G_DK).f(R(390, 256, M(390) + 20, 280), MINT)

# robe with mint stripes, gold belt
robe = s.box(330, 690, M(330), 1186, -104, 104, G).f(R(330, 1156, M(330), 1186), G_DK)
for y in (784, 858, 928, 1046, 1120):
    robe.f(R(330, y, M(330), y + 26), MINT)
s.box(345, 966, M(345), 1022, -108, 108, '#F8C820')

# arms: green sleeves with a mint band, hands
for f in BOTH:
    s.box(f(198), 690, f(350), 1004, -76, 76, '#10B058').f(R(f(198), 900, f(350), 952), MINT)
    s.box(f(200), 998, f(346), 1046, -72, 72, SKIN)

# emerald staff in the left hand
s.prism(B((290, 990), (236, 902), 46), 80, 124, '#4A2418')
s.cube(134, 862, 100, 124, 114, 104, MINT, rz=30, ry=16)
s.cube(90, 832, 150, 50, 46, 40, G_DK, rz=30)
s.cube(295, 852, 130, 20, 20, 20, '#A0FFD8', rz=45)

# head: face, hat crown with a diamond, mint band, wide brim
head = s.box(356, 396, M(356), 722, -110, 110, SKIN)
s.box(348, 276, M(348), 346, -110, 110, G)
gem(s, 538, 315, 40, 108, 120, '#F0FFFC')
s.box(338, 340, M(338), 370, -118, 118, MINT)
s.box(262, 364, M(262), 402, -150, 150, G)

# face: bushy white brows, eyes
for f in BOTH:
    head.f(P((f(402), 480), (f(500), 462), (f(500), 488), (f(402), 504)), BEARD, line=True)
for x, hx in ((428, 436), (M(486), M(472))):
    head.f(R(x, 510, x + 58, 570), '#0A0A1E').f(R(hx, 515, hx + 16, 538), '#FFFFFF')

# long white beard in three tiers with a pink nose on top
s.box(483, 936, M(483), 1026, 104, 124, BEARD)
s.box(422, 800, M(422), 946, 106, 132, BEARD)
s.box(370, 606, M(370), 812, 108, 140, BEARD).f(R(418, 606, M(418), 650), '#FFFFFF')
s.box(510, 562, M(510), 608, 136, 150, '#F4B8A0')

render(s, sys.argv[1])

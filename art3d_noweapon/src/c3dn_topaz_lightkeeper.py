import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1224 - x
BOTH = (lambda x: x, M)
WH, GOLD, FACE, HAIR = '#FCF8F0', '#F0A818', '#FCEAD0', '#FFF0B0'

# floating square halo ring
for x0, y0, x1, y1 in ((452, 50, 776, 72), (452, 112, 776, 134), (446, 50, 494, 134), (734, 50, 782, 134)):
    s.box(x0, y0, x1, y1, -60, 60, '#FFF8A0')

# legs, lower robe, yellow hem
for f in BOTH:
    s.box(f(425), 1072, f(600), 1116, -76, 96, '#B04810')
s.box(405, 940, M(405), 1046, -100, 100, WH)
s.box(398, 1036, M(398), 1080, -104, 104, '#FFD800')

# robe with a topaz stripe and a big chest topaz, gold belt
s.box(417, 668, M(417), 948, -100, 100, WH).f(R(583, 668, M(583), 948), '#FFE878', line=True)
s.prism(D(612, 772, 88), 98, 106, '#E06810')
gem(s, 612, 772, 66, 104, 116, '#FFD000')
s.box(403, 878, M(403), 945, -104, 104, GOLD)

# arms with pale yellow bands, golden mantle over the shoulders
for f in BOTH:
    s.box(f(258), 672, f(418), 970, -80, 80, WH)
    s.box(f(252), 834, f(424), 894, -84, 84, '#FFF098')
s.box(246, 578, M(246), 682, -110, 110, GOLD)

# head: hair at the sides, face, hair on top, circlet with a topaz
for f in BOTH:
    s.box(f(392), 300, f(422), 532, -100, 80, '#FFF4C0')
head = s.box(418, 330, M(418), 650, -110, 110, FACE)
s.box(408, 206, M(408), 324, -116, 116, HAIR)
s.box(400, 312, M(400), 336, -118, 118, '#E8A020')
gem(s, 612, 322, 52, 116, 132, '#FFD000')

# face
for x, hx in ((495, 502), (M(555), M(548))):
    head.f(R(x, 422, x + 60, 488), '#8A2A08').f(R(hx, 437, hx + 20, 460), '#FFFFFF')
for f in BOTH:
    head.f(R(f(450), 515, f(505), 540), '#F8C8A0')
head.f(R(580, 560, M(580), 574), '#D04008')

render(s, sys.argv[1])

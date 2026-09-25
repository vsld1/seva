import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 932 - x
BOTH = (lambda x: x, M)
GR, DK, OR, YEL = '#555468', '#3E3D52', '#FF8A10', '#FFD000'

# grey block with a blue crystal on top of the helmet
s.box(408, 104, 510, 138, -40, 40, '#7A7680')
crystal(s, 461, 90, 42, 96, '#3A70C0', z=0, d=38)

# legs, lower robe with an orange hem
for f in BOTH:
    s.box(f(320), 808, f(452), 848, -60, 70, '#6A1A08')
s.box(304, 686, M(304), 792, -86, 86, '#4A4960')
s.box(300, 784, M(300), 816, -90, 90, OR)

# torso with a yellow yoke, scratches and a yellow core diamond, belt
t = s.box(314, 458, M(314), 672, -86, 86, GR).f(R(314, 458, M(314), 494), YEL)
t.f(RR(388, 528, 56, 14, -12), '#A8A8B8').f(RR(526, 608, 72, 14, 20), '#A8A8B8')
s.prism(D(466, 552, 46), 84, 94, '#15151F')
gem(s, 466, 552, 32, 92, 102, '#FFE800')
s.box(310, 660, M(310), 692, -90, 90, '#12121E')

# arms with yellow bands and dark hands
for f in BOTH:
    s.box(f(192), 426, f(314), 612, -62, 62, '#5E5D72')
    s.box(f(186), 606, f(320), 646, -66, 66, YEL)
    s.box(f(192), 640, f(314), 708, -62, 64, DK)

# helmet: top, orange frame, dark void face, lower mask, glowing eyes
s.box(294, 134, M(294), 182, -96, 96, '#3E3D4E')
s.box(288, 176, M(288), 462, -104, 100, OR)
face = s.box(320, 202, M(320), 370, 96, 106, '#151525')
for x in (378, M(424)):
    face.f(R(x, 318, x + 46, 342), '#FFE800')
s.box(320, 368, M(320), 458, 96, 108, '#2A2A3E')

render(s, sys.argv[1])

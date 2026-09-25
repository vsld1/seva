import sys
from lib3d import *

s = Scene()
M = lambda x: 928 - x
BOTH = (lambda x: x, M)
OR, YEL, BODY = '#FF7A10', '#FFE020', '#F8A030'
SKIN, PEACH, CREAM = '#FCE4C8', '#FDD090', '#FDEBD0'

# crystals on top and on the side of the hood
crystal(s, 392, 128, 46, 70, '#F0D850', ang=-25, z=0, d=40)
crystal(s, 518, 124, 44, 68, '#F070E8', ang=25, z=0, d=40)
crystal(s, 456, 106, 58, 110, '#F09040', z=-10, d=50)
crystal(s, 252, 384, 22, 44, '#F09040', ang=-30, z=20, d=20)
s.cube(254, 446, 20, 30, 30, 30, '#F070E8', rz=-20)

# legs and feet
for f in BOTH:
    s.box(f(305), 758, f(458), 862, -66, 66, '#FF5008')
    s.box(f(302), 852, f(460), 932, -70, 90, '#FFD000').f(R(f(302), 896, f(460), 932), '#C88010')

# body with three stacked gems, belt
s.box(304, 518, M(304), 760, -96, 96, BODY)
gem(s, 464, 682, 40, 94, 104, '#F060E8')
gem(s, 464, 630, 40, 96, 106, '#F8C070')
gem(s, 464, 582, 45, 98, 110, '#FFE060')
s.box(299, 722, M(299), 762, -100, 100, YEL)

# arms: peach upper, cream lower, orange band on the right
for f in BOTH:
    s.box(f(173), 478, f(304), 700, -62, 62, PEACH)
    s.box(f(173), 694, f(304), 792, -64, 64, CREAM)
s.box(M(310), 678, M(166), 726, -68, 68, OR)

# pink scroll with a golden ring, held across the left hand
s.box(86, 634, 300, 696, 58, 116, '#F070F0')
s.prism(E(200, 666, 28, 40), 50, 124, '#FFF030', smooth=True)

# hood: orange shell, yellow frame, face, forehead tab
s.box(262, 150, M(262), 508, -110, 100, OR)
s.box(270, 196, M(270), 508, -104, 104, YEL)
head = s.box(302, 222, M(302), 526, -96, 108, SKIN)
s.box(416, 188, M(416), 266, 100, 114, YEL)
for x in (367, M(417)):
    head.f(R(x, 335, x + 50, 412), '#D00808')
for f in BOTH:
    head.f(R(f(332), 418, f(377), 440), '#F8B0B8')
head.f(R(438, 455, M(438), 467), '#C82008')

render(s, sys.argv[1])

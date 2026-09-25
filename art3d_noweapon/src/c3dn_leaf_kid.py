import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 896 - x           # symmetric around x = 448
BOTH = (lambda x: x, M)
SKIN, GREEN, DKGREEN = '#F8DCB0', '#60B010', '#2A7A08'

# little red mushroom and leaf clumps on the hood
s.box(339, 92, 369, 142, -15, 15, '#F8F0E0')
s.box(309, 44, 396, 92, -40, 40, '#FF1010')
s.box(379, 101, 499, 128, -70, 50, '#80D020')
s.box(345, 124, 420, 152, -60, 60, '#90E020')
s.box(420, 112, 578, 152, -80, 60, '#78D018')

# boots and legs
for f in BOTH:
    x0, x1 = sorted((f(300), f(431)))
    s.box(x0, 735, x1, 825, -66, 66, '#6A3818')
    x0, x1 = sorted((f(296), f(433)))
    s.box(x0, 821, x1, 885, -70, 90, '#4A1E08')

# brown tunic, belt, diagonal strap
s.box(289, 518, M(289), 735, -96, 96, '#A05A18')
s.box(281, 679, M(281), 724, -100, 100, '#7A2A08')
s.prism(B((555, 503), (341, 742), 18), 96, 104, '#7A2A08')

# green sleeves with dark cuffs, hands
for f in BOTH:
    x0, x1 = sorted((f(168), f(303)))
    s.box(x0, 450, x1, 746, -64, 64, GREEN).f(R(x0, 641, x1, 671), DKGREEN).f(R(x0, 671, x1, 746), SKIN)

# green hood around the face, collar
s.box(259, 150, M(259), 480, -120, 110, DKGREEN).f(R(259, 150, M(259), 199), '#48A010')
s.box(279, 480, M(279), 521, -104, 104, DKGREEN)

# face: eyes, freckles, mouth
head = s.box(304, 248, M(304), 499, -100, 118, SKIN)
for x in (358, M(405)):
    head.f(R(x, 330, x + 47, 405), '#05051A')
for f in BOTH:
    for a, b, y in ((342, 353, 401), (364, 371, 411)):
        head.f(R(min(f(a), f(b)), y, max(f(a), f(b)), y + 10), '#E0A050')
head.f(R(422, 430, M(422), 444), '#A02010')

render(s, sys.argv[1])

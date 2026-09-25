import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 1064 - x          # symmetric around x = 532
BOTH = (lambda x: x, M)
BLUE, WHITE, SKIN, DKBLUE = '#28C8F8', '#F6F2F2', '#FCE0D4', '#0858D0'

# white snow cube on top of the hood
s.box(478, 75, M(478), 150, -50, 50, '#F8F4F0').f(R(532, 75, M(478), 150), '#D0D4E8')

# white boots and dark blue trousers
for f in BOTH:
    x0, x1 = sorted((f(372), f(528)))
    s.box(x0, 856, x1, 930, -70, 96, WHITE)
    x0, x1 = sorted((f(380), f(528)))
    s.box(x0, 788, x1, 860, -66, 66, DKBLUE)

# blue parka with a zip, pockets and a white hem
p = s.box(352, 520, M(352), 760, -98, 98, BLUE).f(R(521, 540, M(521), 776), '#A8A8B8')
for x in (382, M(461)):
    p.f(R(x, 679, x + 79, 731), '#10A8E8')
s.box(348, 746, M(348), 791, -102, 102, WHITE)

# sleeves with white cuffs and blue mittens, snow on the shoulders
for f in BOTH:
    x0, x1 = sorted((f(222), f(352)))
    s.box(x0, 470, x1, 784, -66, 66, BLUE).f(R(x0, 668, x1, 705), WHITE).f(R(x0, 705, x1, 784), DKBLUE)
    s.box(min(f(236), f(300)), 458, max(f(236), f(300)), 474, -40, 30, '#E8F8FF')

# white fur hood with a blue top band, face inside
s.box(334, 139, M(334), 199, -116, 116, BLUE)
s.box(330, 191, M(330), 540, -120, 120, WHITE)
face = s.box(390, 266, M(390), 491, -100, 126, SKIN)
for x in (401, 476):
    for xx in (x, M(x + 27)):
        face.f(R(xx, 262, xx + 27, 312 if x == 476 else 298), '#A8E0F0')
for x in (435, M(488)):
    face.f(R(x, 330, x + 53, 409), '#05051A')
face.f(R(409, 409, 469, 441), '#FF8898').f(R(M(469), 409, M(409), 441), '#FF8898')
face.f(R(515, 404, M(515), 428), '#FF9AA8')
face.f(R(511, 452, M(511), 477), '#A01018')

render(s, sys.argv[1])

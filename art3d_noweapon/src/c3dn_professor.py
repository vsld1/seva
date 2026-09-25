import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 920 - x
BOTH = (lambda x: x, M)
NAVY, SKIN, WH = '#0E2A80', '#FCE0C8', '#F4F2F2'

# legs and shoes
for f in BOTH:
    s.box(f(275), 860, f(452), 960, -80, 80, '#28304A')
    s.box(f(268), 950, f(452), 1034, -84, 106, '#101014')

# jacket with lapels, white shirt, yellow suspenders, red bowtie, pocket with chalk, belt
s.box(262, 552, M(262), 866, -100, 100, NAVY).f(R(400, 580, 520, 690), WH)
for x1, x2 in ((318, 400), (M(400), M(318))):
    s.prism(P((x1, 580), (x2, 568), (x2, 700), (x1 + (x2 - x1) * 0.5, 720)), 98, 106, '#0A1E62')
for x in (382, M(418)):
    s.box(x, 572, x + 36, 836, 100, 108, '#FFE000')
for y in (606, 662, 716):
    s.box(498, y - 3, 518, y + 3, 106, 110, '#101030')
s.prism(P((400, 560), (460, 572), (M(400), 560), (M(400), 602), (460, 590), (400, 602)), 100, 112, '#F81010')
s.box(536, 700, 620, 786, 100, 108, '#0A2068')
s.box(525, 678, 554, 750, 104, 114, '#B0E0F8')
s.box(554, 684, 583, 754, 104, 114, '#F8B8E0')
s.box(252, 796, M(252), 842, -104, 104, '#060818')

# arms: navy sleeves, white cuffs, hands; a chalk scratch on the jacket
for f in BOTH:
    s.box(f(100), 500, f(262), 740, -80, 80, NAVY)
    s.box(f(96), 730, f(266), 776, -84, 84, WH)
    s.box(f(100), 770, f(262), 866, -78, 80, SKIN)
s.prism(B((318, 750), (380, 780), 8), 100, 104, '#E8E8F0', line=False)

# head: white hair tufts at the sides, face, white hair with a swept fringe
for f in BOTH:
    s.box(f(248), 180, f(272), 260, -80, 60, WH)
head = s.box(270, 186, M(270), 556, -110, 110, SKIN)
s.box(262, 116, M(262), 196, -116, 116, WH)
s.cube(360, 128, 90, 192, 60, 60, '#FAF8F8', rz=-6)

# face: grey brows, glasses with arms, white mustache, mouth
for f in BOTH:
    head.f(R(f(336), 290, f(416), 302), '#D8D8DC')
s.box(250, 354, 322, 366, 60, 116, '#101014')
s.box(M(322), 354, M(250), 366, 60, 116, '#101014')
for x in (320, M(436)):
    s.box(x, 322, x + 116, 420, 110, 118, '#101014')
    s.box(x + 12, 334, x + 104, 408, 116, 120, '#A8B8D0').f(R(x + 30, 334, x + 56, 378), '#F4F6FA')
s.box(434, 350, 486, 360, 110, 118, '#101014')
s.box(400, 430, 526, 452, 108, 118, WH)
head.f(R(430, 462, 492, 476), '#8A2A10')

render(s, sys.argv[1])

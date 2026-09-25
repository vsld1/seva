import sys
from lib3d import *

ZOOM = 3
s = Scene()
SKIN, HAIR, OR = '#F0B070', '#1A0808', '#E07818'

# spiky hair on top, side lock, hair band
for x0, y0, x1, a, col in ((250, 130, 325, -6, HAIR), (300, 125, 410, -4, HAIR), (390, 138, 465, 0, '#2A1010'), (465, 120, 560, 8, '#4A2018')):
    s.cube((x0 + x1) / 2, (y0 + 215) / 2, -20, x1 - x0, 215 - y0, 90, col, rz=a)
s.box(220, 195, 265, 420, -90, 60, HAIR)
s.box(260, 210, 605, 320, -112, 112, HAIR).f(R(270, 263, 540, 268), '#3A1A28')
s.box(235, 305, 605, 335, -114, 114, OR)
gem(s, 432, 322, 50, 112, 124, '#2A2A48')
gem(s, 398, 282, 15, 112, 120, '#FFF020')

# legs, skirt with a diamond pattern, orange band, tan belt
for x0, x1 in ((238, 385), (390, 545)):
    s.box(x0, 940, x1, 985, -70, 84, '#6A2008')
s.box(230, 900, 555, 945, -92, 92, OR)
sk = s.box(230, 800, 565, 905, -96, 96, '#B84A08')
for cx in (275, 335, 395, 455, 522):
    sk.f(D(cx, 855, 30), '#8A3008')
s.box(225, 765, 580, 800, -100, 100, '#F0C878')

# bare chest under a one-shoulder tunic with patches
s.box(240, 565, 570, 800, -94, 94, SKIN)
t = s.prism(P((240, 578), (425, 578), (425, 660), (565, 660), (565, 800), (240, 800)), 90, 100, '#C05A08')
for r in (R(370, 650, 410, 682), R(478, 672, 522, 708), R(305, 702, 348, 738), R(445, 748, 485, 778)):
    t.f(r, '#8A3A08')

# arms with an orange band
for x0, x1 in ((95, 240), (575, 710)):
    s.box(x0, 520, x1, 825, -72, 72, SKIN).f(R(x0, 620, x1, 648), OR)

# face: brows, eyes, big open smile, scar
head = s.box(238, 320, 588, 570, -106, 106, SKIN)
head.f(R(318, 342, 398, 365), '#2A1008').f(P((465, 340), (542, 350), (542, 370), (465, 362)), '#2A1008')
for x in (330, 470):
    head.f(R(x, 368, x + 53, 445), '#05051A').f(R(x + 8, 380, x + 27, 405), '#FFFFFF')
head.f(R(355, 478, 490, 522), '#7A0000').f(R(370, 475, 478, 502), '#FFFFFF').f(R(507, 468, 550, 488), '#8A4020')

render(s, sys.argv[1])

import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 826 - x           # symmetric around the face centre (x = 413)
BOTH = (lambda x: x, M)
SKIN, HAIR, OR = '#F0B070', '#1A0808', '#E07818'

# chunky hair tufts on top, a side lock, the hair band
for cx, w, h, a, col in ((276, 70, 70, -8, HAIR), (346, 72, 80, -4, '#241010'), (412, 64, 72, 2, HAIR), (488, 92, 88, 10, '#4A2018')):
    s.cube(cx, 215 - h / 2, -30, w, h, 70, col, rz=a)
s.box(210, 205, 250, 420, -90, 60, HAIR)
s.box(228, 210, M(228), 320, -112, 112, HAIR).f(R(240, 263, M(240), 268), '#3A1A28')
s.box(228, 305, M(228), 335, -114, 114, OR)
gem(s, 413, 322, 50, 112, 124, '#2A2A48')
gem(s, 379, 282, 15, 112, 120, '#FFF020')

# legs, skirt with a diamond pattern, orange band, tan belt
for f in BOTH:
    s.box(min(f(246), f(408)), 940, max(f(246), f(408)), 985, -70, 84, '#6A2008')
s.box(243, 900, M(243), 945, -92, 92, OR)
sk = s.box(238, 800, M(238), 905, -96, 96, '#B84A08')
for cx in (289, 351, 413, 475, 537):
    sk.f(D(cx, 855, 30), '#8A3008')
s.box(233, 765, M(233), 800, -100, 100, '#F0C878')

# bare chest under a one-shoulder tunic with patches
s.box(248, 565, M(248), 800, -94, 94, SKIN)
t = s.prism(P((248, 578), (433, 578), (433, 660), (M(248), 660), (M(248), 800), (248, 800)), 90, 100, '#C05A08')
for r in (R(378, 650, 418, 682), R(486, 672, 530, 708), R(313, 702, 356, 738), R(453, 748, 493, 778)):
    t.f(r, '#8A3A08')

# arms with an orange band
for f in BOTH:
    x0, x1 = sorted((f(103), f(248)))
    s.box(x0, 520, x1, 825, -72, 72, SKIN).f(R(x0, 620, x1, 648), OR)

# face: brows, eyes, big open smile, scar
head = s.box(238, 320, M(238), 570, -106, 106, SKIN)
head.f(R(304, 342, 384, 365), '#2A1008').f(P((M(384), 340), (M(304), 350), (M(304), 370), (M(384), 362)), '#2A1008')
for x in (316, M(369)):
    head.f(R(x, 368, x + 53, 445), '#05051A').f(R(x + 8, 380, x + 27, 405), '#FFFFFF')
head.f(R(346, 478, 481, 522), '#7A0000').f(R(361, 475, 469, 502), '#FFFFFF').f(R(493, 468, 536, 488), '#8A4020')

render(s, sys.argv[1])

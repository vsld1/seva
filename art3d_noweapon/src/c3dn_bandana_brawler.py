import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 872 - x           # symmetric around x = 436
BOTH = (lambda x: x, M)
SKIN, NAVY, ROCK = '#F4C080', '#2A2A4A', '#A8A6C0'

# red bandana with white dots
s.box(285, 60, M(285), 84, -100, 100, '#FF3050')
bd = s.box(263, 82, M(263), 210, -116, 116, '#FF0010')
for x0, y0 in ((306, 156), (375, 174), (513, 165)):
    bd.f(R(x0, y0, x0 + 21, y0 + 21), '#FFF4EE')

# legs and boots
for f in BOTH:
    x0, x1 = sorted((f(274), f(420)))
    s.box(x0, 664, x1, 769, -66, 66, '#7A7896')
    s.box(x0, 766, x1, 833, -70, 90, '#20203A')

# navy tank top with a yellow diamond, belt with a grey buckle
s.box(250, 400, M(250), 608, -98, 98, NAVY).f(R(362, 400, M(362), 469), SKIN)
gem(s, 436, 529, 59, 98, 112, '#FFD800')
s.box(262, 608, M(262), 664, -102, 102, '#15152A')
s.box(388, 604, M(388), 679, 102, 116, '#9A98B0')

# bare arms with wrist wraps, spiked stone gauntlets, rocky shoulders
for f, a in ((lambda x: x, 1), (M, -1)):
    x0, x1 = sorted((f(110), f(252)))
    s.box(x0, 398, x1, 604, -64, 64, SKIN).f(R(x0, 548, x1, 604), '#F4EDE4')
    x0, x1 = sorted((f(96), f(266)))
    s.box(x0, 604, x1, 686, -80, 84, '#8A88A0')
    for cx in (f(125), f(181), f(237)):
        s.cube(cx, 640, 92, 44, 44, 20, '#C8C6D6', rz=45)
    s.cube(f(165), 368, 0, 100, 70, 100, ROCK, rz=12 * a)
    s.cube(f(228), 345, -10, 62, 62, 70, '#8A88A8', rz=-20 * a)

# head: angry brows, eyes, stubble, mouth, plaster on the cheek
head = s.box(276, 205, M(276), 420, -106, 106, SKIN).f(R(324, 330, M(324), 413), '#E8A868')
head.f(P((321, 214), (411, 233), (411, 254), (321, 231)), '#3A1408').f(P((M(411), 233), (M(321), 214), (M(321), 231), (M(411), 254)), '#3A1408')
for x in (339, M(390)):
    head.f(R(x, 244, x + 51, 306), '#05051A').f(R(x + 6, 244, x + 25, 278), '#FFFFFF')
head.f(R(399, 351, M(399), 369), '#5A0A08')
head.f(R(296, 300, 338, 330), '#F8E8D0').f(R(305, 289, 330, 341), '#F8E8D0')

render(s, sys.argv[1])

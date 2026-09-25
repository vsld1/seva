import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 864 - x
BOTH = (lambda x: x, M)
WH, LILAC, SKIN = '#FAF6F8', '#E8C0F8', '#FDE8E0'

# legs and boots with pink diamonds
for f in BOTH:
    s.box(f(255), 780, f(415), 880, -70, 70, '#E0D0F0')
    s.box(f(248), 872, f(420), 960, -74, 90, WH)
    gem(s, 333 if f(0) == 0 else 505, 924, 22, 88, 96, '#F888D0')

# dress with a triangle-diamond emblem, lilac hem
s.box(240, 504, M(240), 780, -96, 96, WH)
s.prism(D(420, 622, 88), 94, 102, '#C8C0D0').f(P((398, 580), (398, 660), (348, 624)), '#A8E0F8')
s.box(232, 732, M(232), 780, -100, 100, LILAC)

# arms: white sleeves, lilac bands, hands
for f in BOTH:
    s.box(f(80), 444, f(240), 676, -76, 76, WH)
    s.box(f(90), 668, f(240), 712, -72, 72, LILAC)
    s.box(f(90), 706, f(240), 790, -70, 72, SKIN)

# head: face, pastel hair band with three crown gems
head = s.box(244, 176, M(244), 506, -100, 100, SKIN)
s.prism(P((234, 92), (M(234), 92), (M(234), 216), (608, 226), (548, 208), (490, 222), (424, 206), (362, 222), (300, 208), (234, 226)),
        -106, 106, '#D8F2F8')
s.box(226, 138, M(226), 172, -110, 110, '#C8C0CC')
gem(s, 318, 154, 36, 108, 120, '#A8F4D8')
gem(s, 432, 138, 56, 108, 124, '#DDA8F8')
gem(s, 546, 154, 36, 108, 120, '#F8A8E0')

# face: big sparkly eyes, blush, little nose
for x in (312, 472):
    head.f(R(x, 292, x + 60, 386), '#05051A').f(R(x + 10, 302, x + 28, 334), '#FFFFFF').f(R(x + 34, 352, x + 44, 364), '#FFFFFF')
head.f(R(268, 386, 326, 414), '#F8C0D8').f(R(520, 386, 578, 414), '#F8C0D8')
head.f(R(412, 424, 450, 442), '#F070A8')

render(s, sys.argv[1])

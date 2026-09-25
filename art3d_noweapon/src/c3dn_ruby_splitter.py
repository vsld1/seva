import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 996 - x
BOTH = (lambda x: x, M)
NAVY, RED, RED_DK, SKIN, BEARD, RUBY = '#20223A', '#800010', '#3A0A10', '#F8C090', '#FF4A00', '#FF1030'

# curved horns on the helmet
for f in BOTH:
    s.prism(B((f(292), 262), (f(266), 150), 42), -30, 30, '#F4ECE4')
    s.prism(B((f(264), 170), (f(254), 84), 32), -24, 24, '#F4ECE4')

# legs, skirt panels
for f in BOTH:
    s.box(f(338), 866, f(488), 942, -70, 90, '#0A0206')
s.box(326, 792, M(326), 872, -90, 90, RED_DK).f(R(330, 792, 388, 872), RED).f(R(458, 792, 538, 872), RED).f(R(M(388), 792, M(330), 872), RED)

# torso with a strap of rubies, belt with a ruby buckle
s.box(326, 598, M(326), 764, -88, 88, RED).f(B((600, 800), (410, 605), 40), NAVY)
s.box(310, 740, M(310), 802, -92, 92, '#2A0A10')
s.box(450, 744, 528, 810, 90, 100, NAVY)
for x, y, r in ((548, 640, 22), (490, 688, 22), (432, 728, 22), (489, 778, 26)):
    gem(s, x, y, r, 88 if y < 740 else 98, 98 if y < 740 else 108, RUBY)

# arms: bare skin, bracers (a ruby on the right), dark gloves
for f in BOTH:
    s.box(f(191), 505, f(326), 690, -64, 64, SKIN)
    s.box(f(184), 748, f(333), 818, -66, 68, RED_DK)
    s.box(f(180), 675, f(337), 756, -70, 70, NAVY)
gem(s, M(268), 715, 22, 68, 78, RUBY)

# fur collar under the head
s.box(306, 480, M(306), 612, -96, 96, '#8A4028')

# head: face, helmet with a ruby, brim, nose guard
head = s.box(335, 288, M(335), 562, -104, 104, SKIN)
s.box(314, 176, M(314), 276, -110, 110, NAVY)
s.box(306, 268, M(306), 296, -114, 114, '#14162A')
gem(s, 498, 228, 40, 108, 124, RUBY)
s.box(480, 290, 516, 396, 102, 112, NAVY)

# face: angry brows, eyes, red war paint
for f in BOTH:
    head.f(P((f(384), 328), (f(466), 350), (f(466), 370), (f(384), 348)), '#3A0808')
    head.f(R(f(378), 426, f(462), 446), '#F82838')
for x, hx in ((398, 405), (M(450), M(434))):
    head.f(R(x, 355, x + 52, 420), '#0A0A1E').f(R(hx, 370, hx + 15, 390), '#FFFFFF')

# fiery beard with a long braid
s.box(476, 574, M(476), 658, 100, 126, BEARD)
s.box(472, 648, M(472), 678, 98, 130, '#FF4040')
s.box(370, 470, M(370), 582, 102, 136, BEARD).f(R(464, 490, M(464), 505), '#5A0808')

render(s, sys.argv[1])

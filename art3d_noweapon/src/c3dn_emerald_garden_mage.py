import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1232 - x
BOTH = (lambda x: x, M)
GREEN, STRAW, SKIN, TAN = '#20C850', '#F8DC80', '#FCDEC0', '#F0C880'

# sprout and flower on the hat
s.prism(B((540, 150), (540, 94), 10), -5, 5, '#58D050')
s.prism(B((540, 124), (496, 96), 10), -5, 5, '#7AE070')
s.prism(B((540, 124), (578, 104), 10), -5, 5, '#7AE070')
s.box(660, 122, 736, 150, 60, 100, '#F8A0E0')
s.box(688, 110, 708, 126, 70, 90, '#FFE040')

# legs and boots
for f in BOTH:
    s.box(f(428), 1036, f(610), 1086, -80, 80, '#8A3A10')
    s.box(f(424), 1080, f(612), 1138, -84, 104, '#4A1406')

# green tunic, apron with a pocket of flowers, vine strap with leaves
s.box(418, 662, M(418), 1004, -110, 110, GREEN)
s.box(459, 730, M(459), 1046, 108, 118, TAN).f(R(525, 895, 685, 985), '#D8A040')
s.box(552, 878, 598, 930, 110, 130, '#FFF000')
s.box(620, 878, 668, 948, 110, 130, '#F8A0E8')
s.prism(B((496, 964), (720, 684), 18), 118, 134, '#40D850')
for x, y in ((690, 720), (585, 855), (515, 940)):
    s.prism(RR(x, y, 36, 22, -52), 128, 138, '#8AE890')

# arms: leafy sleeves and hands
for f in BOTH:
    s.box(f(250), 606, f(418), 906, -84, 84, '#22D062').f(RR(f(334), 760, 160, 12, -12 if f(0) == 0 else 12), '#10A838')
    s.box(f(250), 900, f(418), 990, -80, 82, SKIN)
    s.prism(P((f(318), 618), (f(376), 600), (f(360), 628)), 80, 92, '#8AF0A0')

# hair pins sticking out at the sides
s.box(285, 376, 340, 386, -8, 8, '#F8A0E0')
s.box(336, 372, 358, 394, -14, 14, '#1A1A24')
s.box(870, 372, 895, 394, -14, 14, '#1A1A24')
s.box(893, 376, 955, 386, -8, 8, '#FFE800')

# head: hair at the sides, face, straw hat with a green band and emerald, wide brim
for f in BOTH:
    s.box(f(393), 300, f(420), 472, -100, 80, '#8A3A10')
head = s.box(418, 294, M(418), 672, -110, 110, SKIN)
s.box(439, 140, M(439), 234, -100, 100, STRAW)
s.box(426, 224, M(426), 262, -106, 106, GREEN)
gem(s, 616, 236, 38, 104, 118, '#30E070')
s.box(280, 256, M(280), 308, -150, 150, '#F4D878')

# face
for x, hx in ((492, 498), (670, 676)):
    head.f(R(x, 435, x + 60, 528), '#0A6A1A').f(R(hx, 448, hx + 22, 475), '#FFFFFF')
head.f(R(450, 535, 505, 560), '#F8B8A8').f(R(717, 535, 772, 560), '#F8B8A8')
head.f(R(581, 582, M(581), 600), '#8A2A10')

render(s, sys.argv[1])

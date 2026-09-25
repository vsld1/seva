import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 914 - x
BOTH = (lambda x: x, M)
SKIN, HAIR, CREAM = '#F7C58C', '#FF4A00', '#F8EEDF'
LBR = '#B87A45'

# boots and pants
for f in BOTH:
    s.box(f(310), 764, f(445), 834, -64, 86, '#521808')
s.box(297, 654, M(297), 774, -82, 82, '#6E2A0A').f(R(454, 654, 460, 774), '#561F07')

# tunic, fur collar with diamond flaps, belt with a buckle, pouch
s.box(305, 466, M(305), 634, -80, 80, '#8B4212')
s.box(292, 402, M(292), 472, -90, 90, LBR)
for x in (354, 457, M(354)):
    gem(s, x, 472, 32, 86, 100, '#C99060')
s.box(294, 628, M(294), 657, -86, 86, '#E6C27A')
s.box(340, 634, 364, 654, 84, 94, '#FFD08A')
s.box(535, 640, 606, 704, 82, 114, LBR)

# arms with cream wristbands
for f in BOTH:
    s.box(f(180), 410, f(305), 678, -62, 62, SKIN)
    s.box(f(173), 488, f(310), 516, -66, 66, CREAM)

# head: long hair at the sides, face, hair on top, headband with a knot
s.box(300, 150, 322, 326, -90, 70, HAIR)
s.box(M(322), 150, M(300), 303, -90, 70, HAIR)
head = s.box(315, 156, M(315), 438, -100, 108, SKIN)
s.box(308, 104, M(308), 164, -106, 114, HAIR)
s.box(302, 176, M(302), 198, -104, 112, CREAM)
s.box(447, 190, 467, 232, 110, 120, CREAM)

# face
for x in (372, M(416)):
    head.f(R(x, 253, x + 44, 323), '#3A0000').f(R(x + 6, 262, x + 20, 282), '#FFFFFF')
for f in BOTH:
    head.f(R(f(342), 330, f(387), 341), '#FF8A1A').f(R(f(342), 350, f(387), 361), '#FF8A1A')
head.f(R(433, 369, M(433), 381), '#8B2A0A')

render(s, sys.argv[1])

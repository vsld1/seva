import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1156 - x
BOTH = (lambda x: x, M)
BLUE, GOLD, BROWN = '#0A4A9A', '#D8A020', '#2A1408'
FACE, CREAM, INK = '#E4ECF0', '#F8EEE0', '#101828'


def clock(cx, cy, r, z):
    s.cyl(cx, cy, z, z + 12, r, GOLD)
    dial = s.cyl(cx, cy, z + 10, z + 16, r - 10, CREAM)
    return dial

# ice crystals on the hat
crystal(s, 505, 186, 64, 136, '#8FE8F8', ang=-14, z=-10, d=54)
crystal(s, 568, 212, 34, 90, '#C8F4FC', z=10, d=30)
crystal(s, 628, 206, 44, 100, '#C8F4FC', ang=20, z=-6, d=40)

# boots, legs
for f in BOTH:
    s.box(f(394), 1166, f(572), 1226, -76, 96, GOLD)
    s.box(f(398), 1066, f(570), 1172, -72, 72, '#0A1640')

# torso with a big clock, belt
s.box(388, 810, M(388), 1030, -100, 100, BLUE)
clock(578, 922, 94, 98)
s.box(571, 858, 585, 936, 112, 120, INK)
s.box(383, 1014, M(383), 1070, -104, 104, BROWN)

# arms: blue sleeves, gold cuffs, frayed epaulettes
for f in BOTH:
    s.box(f(230), 772, f(388), 968, -72, 72, BLUE)
    s.box(f(224), 958, f(394), 1056, -76, 78, '#F0B830')
    s.prism(P((f(226), 712), (f(390), 712), (f(390), 778), (f(352), 778), (f(344), 764), (f(310), 764), (f(300), 786),
              (f(268), 786), (f(260), 770), (f(226), 770)), -82, 82, '#D0A050')

# head: face, gold collar, hat with a clock, brim
head = s.box(390, 452, M(390), 816, -104, 104, FACE).f(R(390, 798, M(390), 816), GOLD)
s.box(430, 246, M(430), 402, -80, 80, BLUE).f(R(418, 280, 432, 402), GOLD).f(R(M(432), 280, M(418), 402), GOLD)
s.box(418, 386, M(418), 428, -86, 86, GOLD)
clock(578, 325, 78, 78)
s.box(571, 284, 584, 338, 92, 98, INK)
s.box(530, 324, 584, 338, 92, 98, INK)
s.box(338, 424, M(338), 456, -118, 118, BROWN)

# face: brows, monocle, blue eye, crystal tears, mouth
for f in BOTH:
    head.f(P((f(452), 560), (f(534), 554), (f(534), 578), (f(452), 584)), '#1E3A6A')
head.f(R(632, 586, 690, 672), '#0A6ABA').f(R(642, 598, 660, 622), '#FFFFFF').f(R(546, 728, 606, 743), '#1E3A6A')
head.f(B((476, 670), (432, 766), 6), GOLD)
s.cyl(492, 628, 102, 110, 52, GOLD)
s.cyl(492, 628, 108, 114, 42, '#5FE0C8').face('front').decals.append(
    (np.array([(470, 598, 114), (488, 598, 114), (488, 622, 114), (470, 622, 114)], float), rgb('#FFFFFF'), False))
gem(s, 443, 700, 18, 102, 110, '#7AF0F8')
gem(s, 712, 705, 18, 102, 110, '#7AF0F8')

# floating sparkles
for x, y, r, col in [(165, 822, 22, '#FFE81A'), (378, 800, 24, '#FFE81A'), (808, 808, 26, '#FFE81A'), (1000, 836, 18, '#FFE81A'),
                     (222, 806, 20, '#FFFFFF'), (795, 672, 14, '#FFFFFF'), (882, 695, 16, '#FFFFFF'), (902, 772, 14, '#FFFFFF'),
                     (797, 900, 18, '#FFFFFF'), (375, 1068, 18, '#FFFFFF'), (590, 1020, 16, '#FFFFFF'), (590, 796, 26, '#C0F4FC'),
                     (955, 815, 20, '#C8F4FC')]:
    inside = 388 < x < 768 and 452 < y < 1070
    s.cube(x, y, 130 if inside else 60, r * 1.3, r * 1.3, r * 1.3, col, rz=45, ry=20)

render(s, sys.argv[1])

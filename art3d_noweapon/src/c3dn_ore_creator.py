import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 976 - x
BOTH = (lambda x: x, M)
SKIN, BROWN, BODY, BEARD = '#FCD8BE', '#8B4A1A', '#2E1008', '#4A1606'
YEL = '#FFF000'

# crystals standing on the flat hat
s.prism(B((418, 272), (402, 140), 10), -4, 8, '#F8D820')
crystal(s, 380, 205, 82, 144, '#C8C8D8', ang=-12, z=-6, d=64)
crystal(s, 574, 200, 30, 144, '#28A8F0', ang=10, z=-26, d=28)
crystal(s, 598, 198, 80, 154, '#F01860', ang=12, z=6, d=64)
crystal(s, 487, 190, 78, 174, '#F8A020', z=0, d=66)
s.box(474, 98, 500, 118, -8, 8, '#F0A0B0')

# crystals on the shoulders (small ones behind, big ones hanging in front)
crystal(s, 138, 642, 50, 130, '#F89040', z=0, d=44)
crystal(s, 218, 536, 50, 76, '#F8D830', ang=-28, z=0, d=44)
crystal(s, 850, 652, 56, 140, '#28E8B0', z=0, d=48)
crystal(s, 764, 548, 56, 84, '#40E8C0', ang=22, z=0, d=48)
crystal(s, 238, 648, 84, 180, '#FF3A8A', z=96, d=62)
crystal(s, 728, 658, 86, 180, '#28A0F8', z=96, d=62)

# feet, gold band, pants
for f in BOTH:
    s.box(f(318), 1034, f(484), 1072, -60, 82, BODY)
s.box(300, 1002, M(300), 1040, -100, 100, '#FFC800')
s.box(306, 900, M(306), 1006, -96, 96, BODY)

# arms: dark sleeves, yellow cuffs, pale hands; brown shoulder pads
for f in BOTH:
    s.box(f(180), 648, f(308), 804, -64, 64, '#3A1608')
    s.box(f(174), 798, f(314), 824, -68, 68, YEL)
    s.box(f(180), 818, f(308), 890, -64, 66, '#F4E0C8')
    s.box(f(160), 584, f(330), 690, -80, 80, BROWN).f(R(f(310), 620, f(330), 680), '#F0A020', line=True)

# torso, belt with five ore gems
s.box(306, 588, M(306), 904, -96, 96, BODY)
s.box(304, 844, M(304), 906, -100, 100, '#140606')
for x, col in zip((378, 433, 488, 543, 598), ('#1E90F0', '#20D8A0', '#F8D820', '#E0E0F0', '#F89020')):
    gem(s, x, 876, 24, 98, 110, col)

# head: face, flat hat brim, yellow band
head = s.box(315, 330, M(315), 600, -110, 110, SKIN)
s.box(294, 270, M(294), 314, -122, 122, '#7A3410').f(P((478, 280), (498, 280), (488, 300)), '#F8A020')
s.box(287, 310, M(287), 336, -118, 118, YEL)
for f in BOTH:
    head.f(P((f(365), 402), (f(452), 414), (f(452), 440), (f(365), 428)), '#5A1A0A')
for x in (380, M(435)):
    head.f(R(x, 448, x + 55, 500), '#FFFF50').f(R(x + 6, 454, x + 30, 466), '#FFFFC4')

# beard: wide upper block, mustache, narrow lower block
s.box(385, 700, M(385), 806, 100, 128, BEARD)
s.box(328, 534, M(328), 712, 106, 136, BEARD)
s.box(375, 526, M(375), 566, 132, 146, '#2A0A04')

# floating ore cubes by the head
s.cube(674, 388, -60, 36, 50, 36, '#10D080', rz=10)
s.cube(715, 432, 40, 62, 62, 62, '#2A7AE8', rz=14, ry=20)

render(s, sys.argv[1])

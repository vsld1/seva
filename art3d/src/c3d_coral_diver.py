import sys
from lib3d import *

s = Scene()
M = lambda x: 1092 - x
BOTH = (lambda x: x, M)
BRONZE, RING, CYAN, SALMON, PINK = '#C87818', '#8A4A10', '#18C8E0', '#F88878', '#F8B0E0'

# corals growing out of the helmet
s.prism(B((412, 200), (384, 128), 26), -30, -4, SALMON)
s.cube(382, 118, -17, 40, 36, 36, SALMON, rz=-10)
s.prism(B((680, 200), (700, 128), 26), -30, -4, PINK)
s.cube(700, 118, -17, 40, 36, 36, PINK, rz=10)

# legs, bronze boots, teal soles
for f in BOTH:
    s.box(f(370), 858, f(540), 950, -76, 76, '#18B8D0')
    s.box(f(366), 940, f(542), 1016, -80, 90, BRONZE)
    s.box(f(366), 1008, f(542), 1050, -80, 94, '#18A0A0')

# cyan suit with a weight belt and a coral clinging to it
s.box(366, 636, M(366), 900, -100, 100, CYAN)
s.box(354, 794, M(354), 862, -104, 104, '#484868')
for x1 in (412, M(484)):
    s.box(x1, 788, x1 + 72, 882, 100, 116, '#10101E')
s.cube(626, 710, 108, 34, 46, 20, SALMON, rz=20)
s.cube(606, 686, 108, 22, 30, 16, PINK, rz=20)

# arms: cyan sleeves, bronze gloves
for f in BOTH:
    s.box(f(214), 540, f(366), 764, -74, 74, '#20D0E8')
    s.box(f(210), 754, f(370), 862, -78, 80, BRONZE)

# coral bouquet on a wooden board in the left hand
s.box(140, 740, 330, 772, 70, 140, '#A86A20')
for (bx, by), (tx, ty) in (((160, 752), (118, 712)), ((240, 750), (198, 700)), ((318, 754), (292, 712))):
    s.prism(B((bx, by), (tx, ty), 22), 94, 116, '#7A5A40')
    s.cube(tx, ty, 105, 42, 42, 42, SALMON, rz=45, ry=20)

# diving helmet: knob, top, side knob, main body with a porthole, collar with rivets
s.box(470, 164, M(470), 192, -60, 60, '#A85A10')
s.box(355, 338, 374, 442, -40, 40, '#A85A10')
s.box(398, 186, M(398), 244, -96, 96, BRONZE)
s.box(368, 236, M(368), 562, -110, 110, BRONZE)
s.cyl(546, 420, 108, 118, 122, RING)
glass = s.cyl(546, 420, 116, 120, 104, '#88D8D8')
s.box(540, 316, 552, 524, 118, 124, RING)
s.box(442, 414, 650, 426, 118, 124, RING)
col = s.box(338, 540, M(338), 642, -118, 118, BRONZE)
for x in (388, 478, M(478), M(388)):
    col.f(R(x - 10, 593, x + 10, 613), RING)

render(s, sys.argv[1])

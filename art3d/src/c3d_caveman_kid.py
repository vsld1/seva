import sys
from lib3d import *

s = Scene()
M = lambda x: 1010 - x
BOTH = (lambda x: x, M)
SKIN, HAIR, TUN, TAN = '#FACB90', '#6E2A04', '#C05A0A', '#E8C27A'
STONE = '#9496B0'

# feet, legs, fur leg-wraps
for f in BOTH:
    s.box(f(338), 878, f(492), 932, -60, 86, '#6E2204')
    s.box(f(342), 754, f(495), 840, -64, 64, '#A84200')
    s.box(f(332), 830, f(497), 884, -68, 70, '#D8963A')

# bare chest under a one-shoulder tunic with patches, skirt, belt, pouch
s.box(332, 470, M(332), 708, -90, 90, SKIN)
tunic = s.prism(P((485, 478), (M(332), 478), (M(332), 708), (332, 708), (332, 566), (485, 566)), -94, 94, TUN)
for r in (R(498, 556, 537, 588), R(556, 606, 597, 638), R(414, 660, 453, 690)):
    tunic.f(r, '#7A2A08')
s.box(330, 728, M(330), 760, -92, 92, TUN)
s.box(327, 702, M(327), 732, -96, 96, TAN)
s.box(322, 708, 402, 782, 92, 122, '#D0902E')

# arms
for f in BOTH:
    s.box(f(190), 450, f(334), 752, -70, 70, SKIN)

# slingshot with a pebble in the left hand
s.prism(B((258, 708), (258, 672), 30), 76, 102, '#7A3A12')
s.prism(B((258, 690), (192, 630), 22), 78, 100, '#8B4A1A').f(R(170, 610, 215, 650), '#E07A2A')
s.prism(B((258, 690), (310, 630), 22), 78, 100, '#8B4A1A').f(R(290, 610, 330, 650), '#E07A2A')
s.box(196, 628, 306, 640, 84, 92, '#FF4A4A')
s.cube(250, 662, 112, 46, 44, 44, STONE, rz=8)

# head: hair tuft and leaf, face, hair
s.prism(P((548, 108), (580, 78), (622, 108)), -30, 30, HAIR)
s.prism(B((408, 108), (578, 74), 12), 56, 70, '#3EC21E')
head = s.box(343, 196, M(343), 488, -100, 104, SKIN)
s.box(337, 104, M(337), 204, -106, 110, HAIR)

# face: eyes, mouth, freckle beads, stone nose and cheek stones
for x in (405, M(465)):
    head.f(R(x, 276, x + 60, 362), '#05051A').f(R(x + 12, 290, x + 27, 315), '#FFFFFF')
head.f(R(472, 402, M(472), 426), '#8B1A0A')
for x, y in ((398, 372), (418, 388), (M(410), 372), (M(430), 388)):
    head.f(R(x, y, x + 12, y + 12), '#F08A1A')
s.box(474, 365, 536, 419, 102, 128, '#8E90A8')
s.box(393, 395, 447, 449, 102, 122, '#E8E0DA')
s.box(562, 396, 618, 452, 102, 122, '#CFCCDA')

render(s, sys.argv[1])

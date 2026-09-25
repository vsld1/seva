import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 980 - x
BOTH = (lambda x: x, M)
PEACH, CREAM, PALE, ORANGE, RED = '#FFC888', '#FFDDA8', '#FFEAC4', '#FF7A20', '#E84808'

# napkin pieces on top
s.cube(412, 150, -10, 176, 84, 150, '#F8E6CC', rz=-8)
s.cube(556, 140, 20, 118, 100, 110, '#FBEAD4', rz=14)

# arms behind the stack
for f in BOTH:
    s.box(f(164), 470, f(314), 612, -66, 66, '#FFA028')
    s.box(f(150), 604, f(322), 642, -70, 70, CREAM)
    s.box(f(164), 638, f(314), 810, -66, 68, '#FFB050')
s.box(M(314), 668, M(164), 712, -70, 70, RED)

# the pancake stack, each layer a slightly different width
layers = [(195, 230, 176, PEACH), (226, 256, 190, RED), (252, 276, 176, PEACH), (272, 300, 192, CREAM),
          (298, 448, 178, PEACH),
          (444, 476, 184, '#F06A18'), (474, 496, 178, CREAM), (494, 522, 190, RED), (520, 542, 180, PEACH),
          (540, 592, 190, '#E04A08'), (590, 620, 184, ORANGE), (618, 656, 186, CREAM), (654, 684, 182, '#F07020'),
          (682, 732, 192, '#FF6A10'), (730, 778, 180, PALE), (776, 852, 186, RED), (850, 882, 196, CREAM),
          (880, 906, 186, RED), (904, 942, 192, PALE), (940, 972, 170, '#FFF0C8')]
face = None
for y1, y2, hw, col in layers:
    b = s.box(490 - hw, y1, 490 + hw, y2, -hw * 0.62, hw * 0.62, col)
    if y1 == 298:
        face = b
for x in (378, M(442)):
    face.f(R(x, 348, x + 64, 392), '#FFFFFF')

# sugar sparkles
for x, y in ((282, 322), (212, 366), (238, 425), (145, 520), (148, 585), (385, 470), (598, 475), (672, 325),
             (740, 430), (752, 370), (830, 715), (718, 760), (495, 745), (210, 862), (758, 880), (372, 948), (606, 958)):
    inside = 298 < x < 682 and 190 < y < 972
    s.cube(x, y, 130 if inside else 40, 24, 24, 24, '#FFFFFF', rz=12, ry=20)

render(s, sys.argv[1])

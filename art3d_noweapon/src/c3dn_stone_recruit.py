import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 860 - x           # symmetric around x = 430
BOTH = (lambda x: x, M)
STONE, DARK, BROWN = '#C0BECE', '#8A8AA0', '#A85A20'

# stone helmet: knob, top, crown with a scratched tick, brim
s.box(381, 103, M(381), 142, -40, 40, '#6A6A88').f(R(430, 103, M(381), 142), '#3A3A6A')
s.box(321, 141, M(321), 176, -80, 80, '#A8A8BC')
s.box(268, 170, M(268), 238, -110, 110, DARK).f(B((325, 232), (336, 247), 11), '#2A2A40').f(B((336, 247), (364, 190), 11), '#2A2A40')
s.box(246, 234, M(246), 278, -130, 130, '#7A7A92')

# legs, stone boots
for f in BOTH:
    x0, x1 = sorted((f(292), f(418)))
    s.box(x0, 724, x1, 806, -66, 66, '#5A2A0E')
    x0, x1 = sorted((f(290), f(420)))
    s.box(x0, 802, x1, 866, -72, 92, '#9A98B0')

# brown harness with a stone chest plate, rivets and a crack
t = s.box(283, 480, M(283), 660, -100, 100, BROWN).f(R(307, 499, M(307), 649), '#B8B6C8').f(R(307, 499, M(307), 529), DARK)
for x in (321, M(341)):
    for y in (534, 626):
        t.f(R(x, y, x + 20, y + 19), '#9A98AE')
t.f(B((466, 551), (489, 615), 6), '#4A4A68')
s.box(283, 701, M(283), 724, -98, 98, BROWN)
s.box(276, 660, M(276), 701, -104, 104, '#3A1A0A')
s.box(398, 658, M(398), 712, 104, 116, '#C8C6D6')
s.box(294, 679, 357, 739, 104, 124, '#A0501C')

# arms with cloth wraps, stone pauldron on the right shoulder
for f in BOTH:
    x0, x1 = sorted((f(159), f(283)))
    s.box(x0, 450, x1, 724, -64, 64, STONE).f(R(x0, 634, x1, 694), '#F0E0B8')
s.cube(650, 500, 0, 140, 92, 150, '#B8B6CA', rz=10)

# head, helmet nose guard, angry brows, eyes, mouth, worn patches
head = s.box(289, 275, M(289), 495, -106, 106, STONE).f(R(412, 278, M(412), 356), '#7A7A92')
head.f(P((337, 318), (397, 330), (397, 346), (337, 334)), '#2A2A48').f(P((M(397), 330), (M(337), 318), (M(337), 334), (M(397), 346)), '#2A2A48')
for x in (345, M(390)):
    head.f(R(x, 345, x + 45, 413), '#05051A').f(R(x + 6, 355, x + 21, 375), '#FFFFFF')
head.f(R(404, 433, M(404), 446), '#2A2A48')
head.f(R(307, 428, 345, 458), '#A8A6B8').f(R(M(345), 428, M(307), 458), '#A8A6B8')

render(s, sys.argv[1])

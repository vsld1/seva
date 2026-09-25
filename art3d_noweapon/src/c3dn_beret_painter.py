import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 852 - x           # symmetric around x = 426
BOTH = (lambda x: x, M)
SKIN, WHITE, BLUE, HAND = '#FF8838', '#F8F4F4', '#1050D8', '#FF9A58'
STRIPES = ((484, 503), (540, 559), (589, 609), (641, 664))

# red beret with a stem
s.box(379, 70, 398, 100, -10, 10, '#C0001A')
s.box(270, 88, 590, 112, -100, 100, '#FF3060')
s.box(240, 108, 612, 195, -120, 120, '#FF1848').f(R(240, 168, 612, 195), '#D0002A')

# dark trousers
for f in BOTH:
    x0, x1 = sorted((f(268), f(420)))
    s.box(x0, 698, x1, 844, -68, 80, '#3A1408')

# striped shirt, apron with straps, pocket, paint splats and a brush
t = s.box(268, 461, M(268), 701, -96, 96, WHITE)
for y0, y1 in STRIPES:
    t.f(R(268, y0, M(268), y1), BLUE)
for x in (315, M(334)):
    s.box(x, 461, x + 19, 484, 96, 104, '#F8E8D4')
a = s.box(300, 484, M(300), 769, 96, 104, '#F8E8D4').f(R(300, 619, M(300), 634), '#F0DCC0').f(R(349, 634, 480, 686), '#F4E2CC')
a.f(P((470, 510), (510, 516), (506, 551), (465, 545)), '#E85A10').f(R(328, 559, 356, 581), '#E85A10').f(R(442, 712, 476, 739), '#E85A10')
a.f(B((373, 590), (386, 664), 8), '#B85A10').f(R(360, 568, 388, 593), '#1050D0')

# striped sleeves and hands
for f in BOTH:
    x0, x1 = sorted((f(134), f(268)))
    sl = s.box(x0, 409, x1, 700, -64, 64, WHITE).f(R(x0, 560, x1, 700), HAND)
    for y0, y1 in STRIPES[:2]:
        sl.f(R(x0, y0, x1, y1), BLUE)

# head: brows, eyes, blush, curled moustache smile, paint smudge
head = s.box(278, 191, M(278), 461, -104, 104, SKIN)
for x in (334, M(390)):
    head.f(R(x, 259, x + 56, 274), '#3A1008')
for x in (336, M(384)):
    head.f(R(x, 285, x + 48, 356), '#05051A').f(R(x + 6, 296, x + 24, 315), '#FFFFFF')
head.f(R(300, 349, 339, 379), '#FFA070').f(R(M(339), 349, M(300), 379), '#FFA070')
head.f(P((339, 358), (369, 358), (369, 371), (401, 382), (451, 382), (483, 371), (483, 358), (513, 358),
         (513, 375), (494, 390), (456, 401), (396, 401), (358, 390), (339, 375)), '#3A1008')
head.f(R(497, 240, 531, 263), '#E05A10')

render(s, sys.argv[1])

import sys
from lib3d import *

ZOOM = 3
s = Scene()
FUR, LIGHT, PINK, BROWN = '#AC8A7A', '#C8A89A', '#F8B0C8', '#8A4010'

# ears with pink insides
for cx, cy, a in ((340, 155, -12), (650, 135, 12)):
    e = s.cube(cx, cy, -40, 140, 150, 40, '#A88878', rz=a)
    e.f(RR(cx, cy + 8, 90, 110, a), PINK)

# yellow hard hat with a lamp
s.box(382, 100, 625, 172, -80, 80, '#FFD800')
s.box(365, 168, 645, 195, -100, 100, '#FFC800')
s.box(478, 135, 534, 185, 78, 92, '#FFFBE8')

# feet and legs
for x0, x1 in ((318, 470), (488, 660)):
    s.box(x0, 880, x1, 1000, -70, 110, PINK)
for x0, x1 in ((320, 475), (495, 655)):
    s.box(x0, 825, x1, 920, -66, 66, BROWN)

# body with brown overalls: bib, buttons, pocket and a patch
s.box(310, 565, 660, 830, -96, 96, FUR)
ov = s.box(375, 565, 620, 820, 94, 104, BROWN).f(R(438, 565, 552, 675), LIGHT)
ov.f(R(385, 680, 425, 705), '#C8A800').f(R(565, 680, 605, 705), '#C8A800').f(R(450, 725, 538, 778), '#6A2A08').f(R(388, 785, 438, 820), '#5A1A08')

# arms with pink paws and white claws
for x0, x1, claws in ((155, 315, (155, 208, 260)), (665, 835, (685, 745, 803))):
    s.box(x0, 475, x1, 830, -76, 76, FUR).f(R(x0, 720, x1, 830), PINK)
    for cx in claws:
        s.box(cx, 725, cx + 40, 835, 70, 96, '#E8E0E0').f(R(cx, 725, cx + 40, 760), '#A88068')

# head, eyes, snout with a pink nose and teeth, whiskers
head = s.box(325, 185, 690, 565, -110, 110, FUR).f(R(370, 485, 635, 565), LIGHT)
for x in (396, 557):
    head.f(R(x, 300, x + 56, 375), '#05051A').f(R(x + 9, 308, x + 26, 332), '#FFFFFF')
s.box(418, 395, 598, 485, 108, 150, LIGHT)
s.box(470, 405, 535, 465, 148, 160, PINK)
s.box(467, 520, 527, 565, 112, 126, '#FFFFFF')
for a, b in (((295, 445), (420, 470)), ((305, 490), (420, 478)), ((600, 470), (725, 445)), ((600, 478), (715, 500))):
    s.prism(B(a, b, 7), 126, 132, '#3A2A30', line=False)

render(s, sys.argv[1])

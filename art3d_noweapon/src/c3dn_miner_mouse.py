import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 1014 - x          # symmetric around x = 507
BOTH = (lambda x: x, M)
FUR, LIGHT, PINK, BROWN = '#AC8A7A', '#C8A89A', '#F8B0C8', '#8A4010'

# ears with pink insides
for f, a in ((lambda x: x, -12), (M, 12)):
    e = s.cube(f(345), 150, -40, 140, 150, 40, '#A88878', rz=a)
    e.f(RR(f(345), 158, 90, 110, a), PINK)

# yellow hard hat with a lamp
s.box(385, 100, M(385), 172, -80, 80, '#FFD800')
s.box(367, 168, M(367), 195, -100, 100, '#FFC800')
s.box(479, 135, M(479), 185, 78, 92, '#FFFBE8')

# feet and legs
for f in BOTH:
    s.box(min(f(338), f(498)), 880, max(f(338), f(498)), 1000, -70, 110, PINK)
    s.box(min(f(342), f(497)), 825, max(f(342), f(497)), 920, -66, 66, BROWN)

# body with brown overalls: bib, buttons, pocket and a patch
s.box(332, 565, M(332), 830, -96, 96, FUR)
ov = s.box(385, 565, M(385), 820, 94, 104, BROWN).f(R(450, 565, M(450), 675), LIGHT)
ov.f(R(395, 680, 435, 705), '#C8A800').f(R(M(435), 680, M(395), 705), '#C8A800')
ov.f(R(463, 725, 551, 778), '#6A2A08').f(R(398, 785, 448, 820), '#5A1A08')

# arms with pink paws and white claws
for f in BOTH:
    x0, x1 = sorted((f(172), f(332)))
    s.box(x0, 475, x1, 830, -76, 76, FUR).f(R(x0, 720, x1, 830), PINK)
    for cx in (180, 233, 285):
        c0, c1 = sorted((f(cx), f(cx + 40)))
        s.box(c0, 725, c1, 835, 70, 96, '#E8E0E0').f(R(c0, 725, c1, 760), '#A88068')

# head, eyes, snout with a pink nose and teeth, whiskers
head = s.box(325, 185, M(325), 565, -110, 110, FUR).f(R(375, 485, M(375), 565), LIGHT)
for x in (396, M(452)):
    head.f(R(x, 300, x + 56, 375), '#05051A').f(R(x + 9, 308, x + 26, 332), '#FFFFFF')
s.box(418, 395, M(418), 485, 108, 150, LIGHT)
s.box(475, 405, M(475), 465, 148, 160, PINK)
s.box(477, 520, M(477), 565, 112, 126, '#FFFFFF')
for f in BOTH:
    for a, b in (((295, 445), (420, 470)), ((305, 490), (420, 478))):
        s.prism(B((f(a[0]), a[1]), (f(b[0]), b[1]), 7), 126, 132, '#3A2A30', line=False)

render(s, sys.argv[1])

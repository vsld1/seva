import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 830 - x
BOTH = (lambda x: x, M)
G, G_DK = '#2ED12A', '#0D8A10'
SKIN = '#FAD7B4'

# legs, feet with white claws
for f in BOTH:
    s.box(f(275), 688, f(407), 792, -68, 68, '#1FB81C')
    s.box(f(271), 782, f(409), 848, -72, 100, G_DK)
    for x in (285, 326, 366):
        s.box(f(x), 812, f(x + 20), 838, 98, 112, '#FFFFFF')

# dino suit body with a striped belly
s.box(258, 434, M(258), 694, -95, 95, G)
belly = s.box(325, 465, M(325), 656, 92, 102, '#E2F0B2')
for y in (504, 548, 592):
    belly.f(R(325, y, M(325), y + 9), '#C4DA86')

# arms: sleeves and hands
for f in BOTH:
    s.box(f(128), 418, f(258), 610, -66, 66, '#3DDB38')
    s.box(f(124), 604, f(258), 700, -68, 68, SKIN)

# hood: orange horn, top, sides framing the face, teeth, eyes on top
s.box(404, 58, 426, 104, -24, 24, '#FFA800')
s.box(238, 96, M(238), 178, -120, 112, G)
for f in BOTH:
    s.box(f(238), 170, f(276), 422, -120, 112, G)
s.box(276, 170, M(276), 422, -120, -20, G)
head = s.box(276, 178, M(276), 442, -100, 100, SKIN)
for x in (283, 349, 415, M(349), M(283)):
    s.prism(P((x - 16, 174), (x + 16, 174), (x + 8, 198), (x - 8, 198)), 100, 116, '#EDEDF5')
for f in BOTH:
    s.box(f(298), 70, f(352), 118, 20, 64, '#FFE81A').f(R(f(318), 76, f(332), 114), '#0B0B14')

# face
for x in (328, M(375)):
    head.f(R(x, 270, x + 47, 342), '#05051A')
for f in BOTH:
    head.f(R(f(296), 342, f(336), 362), '#F7AFA4')
head.f(R(383, 372, M(383), 393), '#8B2410')

render(s, sys.argv[1])

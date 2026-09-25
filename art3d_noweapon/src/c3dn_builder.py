import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 870 - x
BOTH = (lambda x: x, M)
WH, OR, SKIN, REFL, YEL = '#F8F0E4', '#FF8C00', '#F8D4A8', '#C0C0C8', '#FFD800'

# legs with knee patches, boots
for f in BOTH:
    s.box(f(290), 722, f(432), 812, -66, 66, '#3A80D0').f(R(f(320), 748, f(390), 792), '#F4EEE4')
    s.box(f(282), 800, f(432), 884, -70, 90, '#8A4410')

# white shirt, orange hi-vis vest halves with reflective strips, belt, tape measure
s.box(262, 462, M(262), 724, -90, 90, WH).f(R(398, 666, 472, 724), '#B85A10')
for x1, x2 in ((262, 402), (468, 612)):
    s.box(x1, 470, x2, 716, 88, 100, OR).f(R(x1, 546, x2, 566), REFL).f(R(x1, 616, x2, 636), REFL)
s.box(272, 678, 346, 744, 94, 116, YEL)

# arms: white sleeves, yellow gloves
for f in BOTH:
    s.box(f(142), 438, f(262), 626, -60, 60, WH)
    s.box(f(138), 612, f(268), 730, -64, 66, YEL)

# head: face, hard hat with an orange stripe, brim, yellow ear piece
head = s.box(280, 206, M(280), 470, -96, 96, SKIN)
s.box(410, 60, 466, 96, -30, 30, '#F0E6D8')
s.box(262, 90, M(262), 180, -100, 100, WH).f(R(302, 110, 388, 162), OR)
s.box(242, 172, M(242), 212, -124, 124, '#F4ECE0')
s.box(268, 240, 284, 300, -20, 20, '#FFD000')

# face: brows, eyes, smile, bandage
for f in BOTH:
    head.f(R(f(336), 248, f(400), 266), '#8A4410')
for x in (344, M(392)):
    head.f(R(x, 272, x + 48, 348), '#05051A').f(R(x + 8, 286, x + 22, 306), '#FFFFFF')
head.f(P((390, 376), (406, 376), (406, 390), (470, 390), (470, 376), (486, 376), (486, 404), (390, 404)), '#8A2A10')
head.f(R(512, 362, 562, 386), '#FAF2EC')

render(s, sys.argv[1])

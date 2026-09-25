import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 860 - x
BOTH = (lambda x: x, M)
OR, RUST, DARK, SKIN = '#FF5A00', '#C82A10', '#2A2E3A', '#FCD8B4'

# propeller beanie
s.box(314, 68, 552, 94, -12, 12, '#F01818')
s.box(408, 52, 460, 82, -16, 16, '#FFC800')
s.box(424, 88, 440, 170, -8, 8, '#3A3E4A')

# legs and boots
for f in BOTH:
    s.box(f(275), 830, f(424), 916, -70, 70, OR).f(R(f(300), 850, f(345), 890), RUST)
    s.box(f(270), 908, f(426), 976, -74, 92, '#4A1A10')

# dark shirt under orange overalls with patches, a gear emblem and a yellow strap
s.box(262, 546, M(262), 842, -90, 90, '#2A2A34')
bib = s.box(292, 576, M(292), 842, 88, 98, OR).f(R(478, 690, 530, 732), RUST).f(R(340, 576, 364, 640), '#FFE000', line=True)
for x in (330, 520):
    bib.f(R(x, 596, x + 26, 622), '#9098A8', line=True)
s.box(252, 736, M(252), 846, -96, 104, OR).f(R(318, 780, 366, 822), RUST).f(R(512, 796, 560, 836), RUST)
s.prism(star(430, 660, 52, 36, 8), 96, 108, '#8A90A0').f(R(416, 646, 444, 674), DARK)

# arms: dark sleeves, grey gloves
for f in BOTH:
    s.box(f(122), 510, f(266), 718, -70, 70, DARK)
    s.box(f(122), 704, f(266), 800, -72, 74, '#6A6E7E')

# head: face, spiky hair, goggle strap with green goggles
head = s.box(268, 202, M(268), 552, -104, 104, SKIN)
s.prism(P((262, 170), (330, 170), (370, 126), (410, 164), (452, 164), (490, 126), (526, 170), (M(262), 170), (M(262), 230), (262, 230)),
        -110, 110, '#8A2A08')
s.box(254, 256, M(254), 290, -110, 110, '#1E2230')
for cx in (360, 512):
    s.cyl(cx, 272, 106, 120, 58, '#1E2230')
    s.cyl(cx, 272, 118, 124, 42, '#10C850')

# face: brows, eyes, mouth, bandage on the cheek
head.f(P((330, 336), (396, 330), (396, 348), (330, 354)), '#6A1A08')
head.f(P((542, 336), (476, 330), (476, 348), (542, 354)), '#6A1A08')
for x in (334, 484):
    head.f(R(x, 356, x + 52, 436), '#05051A').f(R(x + 8, 370, x + 22, 394), '#FFFFFF')
head.f(P((378, 474), (470, 466), (470, 488), (378, 496)), '#7A0A08')
s.prism(RR(544, 452, 64, 24, 14), 102, 110, '#101014')

render(s, sys.argv[1])

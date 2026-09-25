import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 1180 - x
BOTH = (lambda x: x, M)
FUR, HOOD, TUN, STRAP = '#B87A40', '#8B4A1A', '#A35E28', '#5A1A08'
SKIN, IVORY = '#F8D4AA', '#FAFAF7'

# legs and fur boots
for f in BOTH:
    s.box(f(437), 798, f(582), 842, -60, 60, '#5A2A0E')
    s.box(f(432), 836, f(584), 906, -64, 86, FUR).f(R(f(432), 868, f(584), 890), '#6A3010')

# torso with a bandolier, belt, hip band, bone charm
s.box(413, 562, M(413), 716, -90, 90, TUN).f(B((712, 790), (505, 560), 44), STRAP)
s.box(410, 704, M(410), 756, -96, 96, STRAP)
s.box(405, 750, M(405), 806, -92, 92, TUN).f(B((700, 790), (660, 735), 42), STRAP)
s.prism(B((535, 746), (518, 798), 16), 94, 106, IVORY)

# arms: sleeves, fur cuffs, dark gloves; fur mantle over the shoulders
for f in BOTH:
    s.box(f(282), 486, f(413), 654, -66, 66, TUN)
    s.box(f(276), 648, f(419), 704, -70, 70, FUR)
    s.box(f(282), 700, f(413), 778, -66, 68, '#6E2A0A')
s.box(395, 486, M(395), 570, -100, 100, FUR)

# head: hood sides, face, fur band, hood, knob, tusks
for f in BOTH:
    s.box(f(400), 188, f(441), 492, -100, 106, '#B06E38')
head = s.box(438, 210, M(438), 506, -96, 98, SKIN).f(R(478, 418, M(478), 500), '#F0BE8A')
s.box(430, 188, M(430), 216, -104, 110, FUR)
s.box(407, 144, M(407), 192, -108, 108, HOOD)
s.box(534, 124, M(534), 148, -40, 40, FUR)
for f, a in ((M, 12), (lambda x: x, -12)):
    s.cube(f(425), 216, 80, 44, 88, 40, IVORY, rz=a)
    s.box(f(390), 244, f(454), 304, 70, 112, IVORY)

# face
for f in BOTH:
    head.f(P((f(484), 288), (f(562), 298), (f(562), 318), (f(484), 308)), STRAP)
for x in (498, M(546)):
    head.f(R(x, 316, x + 48, 388), '#05051A')

render(s, sys.argv[1])

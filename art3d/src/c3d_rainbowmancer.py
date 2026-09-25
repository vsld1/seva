import sys
from lib3d import *

s = Scene()
M = lambda x: 872 - x
BOTH = (lambda x: x, M)
WH, LILAC, SKIN = '#FCF8F8', '#E4D8F8', '#FCE8E0'

# stepped white hat with a tilted tip
s.cube(368, 138, -10, 48, 104, 44, '#F4F4F8', rz=-10)
s.box(345, 184, 468, 256, -70, 60, WH)
s.box(331, 250, M(331), 324, -90, 90, WH)

# rainbow skirt panels over a pale base
s.box(296, 990, M(296), 1014, -84, 100, '#F0E8F8')
for i, col in enumerate(('#D030F0', '#10C8F8', '#30F040', '#FFF000', '#FFB000', '#F83040')):
    x = 299 + i * 46
    s.box(x, 862, x + 46, 996, -80, 84 + (i % 2) * 6, col)

# torso with rainbow stripes, lilac belt
t = s.box(276, 654, M(276), 866, -84, 84, WH)
for i, col in enumerate(('#F83850', '#FFB000', '#FFE800', '#30F040', '#10D0F0', '#D040F0')):
    y = 678 + i * 19
    t.f(R(276, y, M(276), y + 17), col, line=True)
s.box(276, 828, M(276), 866, -88, 88, LILAC)

# arms: white sleeves, lilac bands, hands
for f in BOTH:
    s.box(f(151), 624, f(276), 806, -60, 60, WH)
    s.box(f(145), 798, f(282), 848, -64, 64, LILAC)
    s.box(f(151), 842, f(276), 892, -60, 62, SKIN)

# a cup of rainbow crystal sticks in the left hand
for a, b, col in (((214, 794), (134, 740), '#20E8F8'), ((216, 794), (184, 730), '#FFE800'), ((220, 794), (232, 730), '#F82838')):
    s.prism(B(a, b, 14), 80, 94, col)
s.box(190, 778, 244, 826, 66, 108, '#F4F4FA')

# head: lilac hair at the sides, face, hat brim, red crystal on the forehead
s.box(278, 402, 300, 540, -80, 60, LILAC)
s.box(M(300), 402, M(278), 512, -80, 60, LILAC)
head = s.box(292, 396, M(292), 662, -100, 100, SKIN)
s.box(281, 318, M(281), 402, -106, 106, WH)
s.prism(P((436, 306), (458, 328), (454, 380), (436, 406), (418, 380), (414, 328)), 100, 120, '#F81838')
for x in (346, M(393)):
    head.f(R(x, 490, x + 47, 560), '#6A1AE0').f(R(x + 9, 500, x + 24, 520), '#FFFFFF')
for f in BOTH:
    head.f(R(f(315), 566, f(355), 584), '#FCC8E0')
head.f(R(416, 598, M(416), 608), '#C04888')

render(s, sys.argv[1])

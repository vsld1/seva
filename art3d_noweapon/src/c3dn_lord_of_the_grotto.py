import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1104 - x
BOTH = (lambda x: x, M)
GOLD, RED, SKIN, BEARD = '#E8B800', '#D00818', '#FCE0CC', '#C06008'

# tall gold crown pillars behind the band
for cx, top, w, z in ((415, 118, 60, -30), (604, 142, 32, -40), (455, 56, 62, -60), (662, 74, 58, -50), (551, 28, 76, -70)):
    s.box(cx - w / 2, top, cx + w / 2, 262, z - w / 2, z + w / 2, GOLD)

# lower robe, gold hem
s.box(362, 966, M(362), 1088, -100, 100, RED)
s.box(352, 1078, M(352), 1130, -104, 104, '#FFE000')

# robe, gold belt with studs
s.box(362, 690, M(362), 924, -100, 100, RED)
s.box(352, 904, M(352), 976, -104, 104, GOLD).f(R(405, 924, 455, 972), '#F4D060').f(R(M(455), 924, M(405), 972), '#F4D060')

# arms: red sleeves, gold cuffs, gold shoulder blocks
for f in BOTH:
    s.box(f(192), 728, f(362), 892, -78, 78, RED)
    s.box(f(192), 880, f(362), 988, -82, 82, '#F0C020')
    s.box(f(186), 608, f(366), 738, -90, 90, '#E8BC20')

# head: face, crown band with pointed bumps and a big ruby
head = s.box(359, 328, M(359), 702, -116, 116, SKIN)
for x1, x2 in ((342, 432), (508, 596), (M(432), M(342))):
    s.prism(P((x1, 262), (x1, 226), ((x1 + x2) / 2, 188), (x2, 226), (x2, 262)), 88, 122, GOLD)
s.box(335, 254, M(335), 334, -122, 122, GOLD)
gem(s, 552, 292, 52, 120, 138, '#FF1030')

# face
for f in BOTH:
    head.f(P((f(420), 414), (f(512), 424), (f(512), 454), (f(420), 444)), '#8B3A10')
for x in (435, 603):
    head.f(R(x, 450, x + 60, 540), '#05051A').f(R(x + 8, 462, x + 30, 490), '#FFFFFF')

# ginger beard with golden threads and a gold clasp
s.box(435, 740, M(435), 862, 110, 140, BEARD)
s.box(378, 574, M(378), 772, 114, 150, BEARD).f(R(440, 610, M(440), 772), '#B85A08')
s.box(428, 560, M(428), 612, 146, 158, '#8B3208')
s.box(478, 620, 494, 822, 148, 154, '#FFE000')
s.box(M(494), 616, M(478), 850, 148, 154, '#FFE000')
s.box(425, 844, M(425), 892, 132, 152, GOLD)

render(s, sys.argv[1])

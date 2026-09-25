import sys
from lib3d import *

s = Scene()
M = lambda x: 724 - x
BOTH = (lambda x: x, M)
GOLD, WHITE, ICE, SKIN = '#E8B800', '#F4F6FA', '#F4F8FC', '#FCE0CC'

# diamond crystals rising from the crown
for cx, top, w, z in ((277, 100, 42, -20), (447, 104, 34, -20), (320, 86, 44, -30), (420, 90, 40, -30), (366, 40, 50, -40)):
    crystal(s, cx, (top + 180) / 2, w, 180 - top, ICE, z=z, d=w * 0.9)
for x1, x2 in ((228, 300), (338, 394), (M(300), M(228))):
    s.prism(P((x1, 180), (x1, 158), ((x1 + x2) / 2, 132), (x2, 158), (x2, 180)), 60, 92, GOLD)

# feet, purple skirt, yellow hem
s.box(240, 756, M(240), 790, -70, 86, '#F0F0F8')
s.box(229, 650, M(229), 742, -84, 84, '#6A10D8')
s.box(226, 732, M(226), 762, -88, 88, '#FFE000')

# white robe, silver chest plate with a golden-framed diamond, belt
s.box(228, 444, M(228), 636, -84, 84, WHITE)
plate = s.box(248, 468, M(248), 632, 82, 92, '#B8C4D4')
for x in (272, 362, 452):
    plate.f(R(x - 4, 470, x + 4, 490), '#15151B')
s.prism(D(362, 555, 58), 90, 98, GOLD)
gem(s, 362, 555, 44, 96, 106, '#FFFFFF')
s.box(230, 620, M(230), 656, -88, 88, '#E0B000')

# arms: white sleeves, gold band on the right, silver shoulders with crystals
for f, a in ((lambda x: x, -30), (M, 30)):
    crystal(s, f(150), 408, 28, 80, ICE, ang=a, z=0, d=26)
for f in BOTH:
    s.box(f(122), 482, f(240), 668, -58, 58, WHITE)
    s.box(f(105), 438, f(244), 492, -66, 66, '#E0E4EC')
s.box(M(242), 580, M(118), 620, -62, 62, '#E0B000')

# golden box full of diamonds in the left hand
s.box(110, 520, 228, 640, 54, 120, '#F0C820')
for x, y, sz in ((155, 552, 30), (205, 548, 26), (132, 578, 22), (182, 578, 34), (150, 618, 22), (202, 602, 26)):
    gem(s, x, y, sz / 1.4, 118, 128, '#FFFFFF')

# head: face, crown band, white brows, blue eyes, white beard
head = s.box(240, 222, M(240), 472, -90, 90, SKIN)
s.box(226, 174, M(226), 230, -96, 96, GOLD)
for f in BOTH:
    head.f(P((f(282), 288), (f(346), 294), (f(346), 308), (f(282), 302)), '#F4F0F0', line=True)
for x, hx in ((292, 322), (M(342), M(336))):
    head.f(R(x, 305, x + 50, 368), '#0A2A9A').f(R(hx, 314, hx + 14, 332), '#FFFFFF')
s.box(270, 380, M(270), 472, 88, 112, '#F8F6F4')

render(s, sys.argv[1])

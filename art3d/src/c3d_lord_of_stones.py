import sys
from lib3d import *

s = Scene()
M = lambda x: 1096 - x
BOTH = (lambda x: x, M)
GOLD, NAVY, SLEEVE = '#EBB800', '#14173F', '#1C2150'
SKIN, BEARD = '#FBDCC4', '#F7F2EE'
RED, ORANGE, YEL = '#FF3A4A', '#FFA010', '#FFE81A'
PURPLE, CYAN, GREEN = '#B040F0', '#22D0F8', '#3AF040'
MAG, BLUE, WHITE = '#F030E0', '#1E6AE8', '#F6F4F8'

# crystals rising out of the crown
crystal(s, 548, 150, 88, 200, WHITE, z=-30)
crystal(s, 548, 176, 58, 150, RED, z=14, d=50)
crystal(s, 452, 188, 64, 124, ORANGE, ang=-16, z=0, d=54)
crystal(s, 612, 206, 44, 124, CYAN, ang=12, z=-14, d=40)
crystal(s, 646, 192, 66, 116, PURPLE, ang=16, z=10, d=54)
crystal(s, 738, 318, 52, 104, ORANGE, ang=-14, z=60, d=46)

# crystal clusters on the shoulders
crystal(s, 160, 660, 62, 176, '#FF6A7A', z=10, d=58)
s.cube(240, 620, 0, 80, 70, 76, '#F8D040', ry=12)
crystal(s, 300, 690, 90, 176, PURPLE, z=112, d=80)
crystal(s, 225, 520, 44, 94, RED, ang=-30, z=20, d=40)
crystal(s, 285, 430, 44, 88, GREEN, ang=-12, z=-10, d=40)
s.cube(758, 616, 0, 80, 70, 76, BLUE, ry=-12)
crystal(s, 765, 525, 40, 76, PURPLE, ang=8, z=20, d=38)
crystal(s, 820, 555, 44, 100, CYAN, ang=28, z=20, d=40)
crystal(s, 840, 700, 88, 206, CYAN, z=112, d=80)
crystal(s, 925, 650, 64, 140, GREEN, z=0, d=58)

# feet, lower robe, gold hem
for f in BOTH:
    s.box(f(400), 968, f(540), 1018, -60, 82, '#9A8A6A')
s.box(378, 866, M(378), 962, -100, 100, NAVY)
s.box(372, 954, M(372), 976, -104, 104, GOLD)

# arms: navy sleeves with gold cuffs
for f in BOTH:
    s.box(f(252), 592, f(396), 784, -70, 70, SLEEVE)
    s.box(f(246), 776, f(402), 840, -74, 74, GOLD)

# robe, gold belt, gold chest plate with a 3x3 grid of gem tiles, white fur mantle
s.box(360, 600, M(360), 870, -100, 100, NAVY)
s.box(363, 820, M(363), 870, -104, 104, GOLD)
s.box(393, 652, M(393), 872, 98, 112, GOLD)
cells = [[GOLD, '#08081A', '#AD8F90'], [RED, BLUE, '#12EE78'], [ORANGE, '#F8F0F0', '#FFA8F0']]
for r, row in enumerate(cells):
    for k, col in enumerate(row):
        x1, y1 = 405 + k * 98, 678 + r * 62
        s.box(x1, y1, x1 + 92, y1 + 56, 110, 120, col)
s.box(345, 610, M(345), 676, -106, 106, BEARD)

# head: face, crown spikes, crown band with a white diamond, green gem on the forehead
head = s.box(393, 330, M(393), 600, -110, 110, SKIN)
for x1, x2 in ((380, 462), (512, 584), (M(462), M(380))):
    s.prism(P((x1, 280), (x1, 240), ((x1 + x2) / 2, 210), (x2, 240), (x2, 280)), 72, 112, GOLD)
s.box(380, 274, M(380), 338, -116, 116, GOLD)
gem(s, 548, 306, 36, 114, 130, WHITE)
gem(s, 553, 358, 24, 108, 120, '#22E022')

# face: white bushy brows, eyes, big white beard with a mustache
for f in BOTH:
    head.f(P((f(438), 400), (f(522), 412), (f(522), 436), (f(438), 426)), BEARD, line=True)
for x in (462, M(508)):
    head.f(R(x, 440, x + 46, 512), '#05051A').f(R(x + 5, 450, x + 19, 470), '#FFFFFF')
s.box(403, 522, M(403), 690, 106, 140, BEARD).f(R(403, 522, M(403), 576), '#FFFFFF').f(R(403, 576, M(403), 584), '#E2DAD4')

# big white crystal cube in the left hand, small cubes around it
s.cube(216, 730, 116, 104, 104, 104, WHITE, rz=32, ry=18)
s.cube(280, 836, 110, 44, 52, 44, CYAN, rz=6)
s.cube(184, 832, 100, 44, 44, 44, MAG, rz=-8)
s.cube(330, 756, 150, 42, 40, 40, GREEN, rz=10)
s.cube(822, 282, 40, 48, 84, 44, WHITE, rz=-12)
s.cube(405, 405, 124, 40, 84, 40, WHITE, rz=-14)

# tumbling jewels all around
for x, y, r, col in [(328, 410, 26, MAG), (432, 360, 26, CYAN), (245, 482, 26, RED), (212, 562, 26, YEL),
                     (678, 366, 28, YEL), (780, 416, 30, YEL), (797, 468, 22, YEL), (848, 490, 26, RED),
                     (882, 572, 26, MAG), (448, 526, 32, MAG), (505, 650, 36, CYAN), (567, 792, 38, GREEN),
                     (540, 860, 38, WHITE), (620, 906, 34, YEL), (755, 950, 30, YEL), (665, 976, 30, YEL),
                     (692, 1010, 24, RED), (330, 940, 30, MAG), (430, 1000, 30, CYAN), (542, 1020, 30, GREEN),
                     (830, 870, 26, RED), (252, 846, 20, RED)]:
    inside = 360 < x < 736 and 330 < y < 980
    s.cube(x, y, 160 if inside else 60, r * 1.25, r * 1.25, r * 1.25, col, rz=45, ry=22, rx=12)

render(s, sys.argv[1])

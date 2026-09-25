import sys
from lib3d import *

s = Scene()
M = lambda x: 1414 - x
BOTH = (lambda x: x, M)
ST, DK, NAVY, RUNE = '#5E5D78', '#45445E', '#2A2A40', '#20F0F0'

# blue crystals on the head and shoulders
crystal(s, 612, 176, 54, 124, '#48B8F0', ang=-20, z=-10, d=46)
crystal(s, 672, 188, 44, 100, '#2A90E8', z=-30, d=40)
crystal(s, 782, 164, 56, 136, '#3AA8F0', ang=26, z=-10, d=48)
crystal(s, 340, 446, 42, 80, '#48B8F0', ang=-30, z=-40, d=38)
crystal(s, 1046, 474, 50, 114, '#8AD8F8', ang=30, z=0, d=44)

# feet and legs
for f in BOTH:
    s.box(f(520), 968, f(690), 1030, -80, 100, '#1A1A30')
    s.box(f(540), 866, f(700), 976, -76, 76, '#3A3A58')
s.box(602, 866, M(602), 976, -60, 60, '#0E0E20')

# torso with a cyan rune, belt
t = s.box(492, 590, M(492), 816, -120, 120, NAVY)
for a, b in (((707, 756), (707, 648)), ((707, 708), (656, 656)), ((707, 708), (758, 656))):
    t.f(B(a, b, 14), RUNE)
s.box(470, 806, M(470), 870, -124, 124, '#0E0E1A')

# right arm: forearm, fist with a glowing seam, big tilted shoulder block
s.box(895, 686, 1115, 780, -100, 100, '#48475E')
s.box(890, 772, 1116, 942, -104, 104, '#3E3D55').f(R(955, 856, 1045, 868), RUNE)
s.cube(1030, 592, 0, 290, 192, 230, ST, rz=8)

# head: top, green trim, band, face with glowing eyes, jaw
head = s.box(522, 232, M(522), 510, -130, 130, ST)
s.box(650, 222, 840, 236, -60, 60, '#3AAA28')
s.box(508, 290, M(508), 366, -136, 136, DK)
for x in (585, M(660)):
    head.f(R(x, 382, x + 75, 416), '#8AF0F8').f(R(x + 6, 386, x + 40, 394), '#D8FCFE')
s.box(530, 500, M(530), 610, 118, 140, '#54536C').f(R(607, 532, M(607), 548), '#0A0A12')

# huge stone slab shield held in the left hand, leaning toward the viewer
slab = s.prism(P((128, 478), (466, 488), (458, 976), (44, 966)), 150, 200, '#9E96AA', rx=-8, pivot=(260, 730, 175))
s.box(110, 966, 468, 990, 150, 204, '#40F0F8')
s.box(190, 460, 430, 482, 170, 210, '#40F0F8')

render(s, sys.argv[1])

import sys
from lib3d import *

s = Scene()
M = lambda x: 1114 - x
BOTH = (lambda x: x, M)
BLUE, GOLD, GOLDH, FACE, SAPH = '#1030C8', '#D8A010', '#F8C820', '#FCE6DC', '#1060E8'

# lower robe, gold hem
s.box(360, 862, M(360), 996, -100, 100, '#0A28C0')
s.box(350, 986, M(350), 1022, -104, 104, GOLDH)

# robe with a gold stripe, lighter hips, gold collar
s.box(367, 612, M(367), 868, -96, 96, BLUE).f(R(367, 814, M(367), 868), '#2060E8').f(R(529, 612, M(529), 868), '#F0C020', line=True)
s.box(358, 584, M(358), 626, -100, 100, GOLD)

# arms: sleeves, gold bands, cuffs, hands
for f in BOTH:
    s.box(f(212), 540, f(367), 766, -74, 74, BLUE)
    s.box(f(205), 756, f(374), 808, -78, 78, GOLDH)
    s.box(f(218), 802, f(362), 860, -72, 72, '#1850E0')
    s.box(f(222), 856, f(358), 898, -68, 68, FACE)

# flat golden disc with an ice crystal and a sapphire, held in the left hand
s.cyl(212, 772, 18, 110, 100, '#D8A020', ry_=46, rx=90, pivot=(212, 772, 64))
s.cube(146, 734, 64, 64, 56, 56, '#90F4FC', rz=-10)
s.cube(238, 792, 110, 42, 42, 36, SAPH, rz=45)

# big crystal orb in front of the belly, sparkles around it
s.sphere(557, 745, 170, 98, '#BCE6F8')
s.cube(557, 745, 258, 64, 64, 30, '#EAF8FC', rz=45)
for x, y, r in ((422, 648, 14), (450, 722, 14), (655, 675, 14), (625, 795, 12)):
    s.cube(x, y, 230, r * 1.4, r * 1.4, r * 1.4, '#FFFFFF', rz=45, ry=20)

# hood, gold frame, face with a sapphire on the forehead
s.box(485, 150, M(485), 174, -40, 40, '#2040D0')
s.box(327, 168, M(327), 604, -110, 100, BLUE)
s.box(334, 222, M(334), 600, -104, 104, GOLD)
head = s.box(372, 250, M(372), 606, -96, 110, FACE)
s.prism(D(557, 318, 55), 108, 116, GOLD)
gem(s, 557, 318, 40, 114, 124, SAPH)

# face: glowing eyes with tears, mouth
for x in (442, M(500)):
    head.f(R(x, 392, x + 58, 458), '#90FCFC').f(R(x + 6, 398, x + 26, 410), '#D8FEFE')
for x in (465, M(478)):
    head.f(R(x, 472, x + 13, 530), '#90FCFC')
head.f(R(536, 527, M(536), 538), '#8A2020')

render(s, sys.argv[1])

import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1102 - x
BOTH = (lambda x: x, M)
P_, SILVER = '#9A50F0', '#C0C0CC'

# amethyst crystals on the helmet and shoulders
crystal(s, 436, 222, 52, 92, '#E0C0F8', ang=-20, z=-10, d=46)
crystal(s, 666, 222, 52, 92, '#E0C0F8', ang=20, z=-10, d=46)
crystal(s, 551, 190, 72, 160, '#E080F8', z=-20, d=62)
crystal(s, 236, 576, 52, 104, '#E88CF8', ang=-25, z=0, d=46)
crystal(s, M(236), 576, 52, 104, '#E88CF8', ang=25, z=0, d=46)

# legs, feet, codpiece with a silver edge
for f in BOTH:
    s.box(f(370), 986, f(532), 1068, -80, 80, '#4A28C8')
    s.box(f(356), 1060, f(536), 1142, -84, 100, '#3A1CA8')
s.box(460, 950, M(460), 1046, 100, 132, '#7A10E0')
s.box(452, 1030, M(452), 1076, 100, 138, SILVER)

# torso with a big amethyst in a silver frame, belt
s.box(366, 676, M(366), 918, -110, 110, '#4A1CC8')
s.prism(D(551, 792, 86), 108, 118, SILVER)
gem(s, 551, 792, 66, 116, 128, '#D070F8')
s.box(342, 898, M(342), 952, -114, 114, '#1E0A70')

# arms: sleeves, gloves, big tilted shoulder blocks with a silver stripe
for f, a in ((lambda x: x, -5), (M, 5)):
    s.box(f(190), 740, f(366), 910, -84, 84, '#5A30D8')
    s.box(f(186), 886, f(356), 970, -88, 88, P_)
    sh = s.cube(f(262), 668, 0, 212, 128, 200, '#6038E0', rz=a)
    sh.f(rot(R(f(262) - 106, 712, f(262) + 106, 724), a, (f(262), 668)), SILVER)

# helmet: top, main, silver band, visor slit, lower plate with vents, nose guard
s.box(380, 258, M(380), 318, -100, 100, '#6A2CD8')
s.box(360, 310, M(360), 670, -120, 120, P_)
s.box(350, 394, M(350), 420, -126, 126, SILVER)
v = s.box(398, 466, M(398), 512, 118, 126, '#0A0A14').f(R(436, 476, 498, 500), '#FFFFFF').f(R(M(498), 476, M(436), 500), '#FFFFFF')
low = s.box(388, 552, M(388), 646, 118, 128, '#5020C8')
for x in (430, 452, M(466), M(444)):
    low.f(R(x, 582, x + 14, 626), '#05050E')
s.box(536, 456, 566, 652, 124, 136, SILVER)

render(s, sys.argv[1])

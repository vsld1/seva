import sys
from lib3d import *

s = Scene()
M = lambda x: 1096 - x
BOTH = (lambda x: x, M)
SILVER, SHIRT, STRAP, SKIN = '#E4E6EC', '#A8B8D8', '#7888A8', '#FCE2CC'

# legs with knee plates, boots
for f in BOTH:
    s.box(f(380), 942, f(545), 1062, -76, 76, '#3A5690').f(R(f(405), 975, f(505), 1045), '#D8DCE8')
    s.box(f(370), 1054, f(547), 1120, -80, 96, '#A8ACBC')

# shirt with suspenders and a chest diamond, belt with a silver buckle
t = s.box(364, 660, M(364), 950, -104, 104, SHIRT)
t.f(R(428, 666, 470, 950), STRAP).f(R(M(470), 666, M(428), 950), STRAP).f(R(420, 738, M(420), 775), '#8898B8')
gem(s, 548, 756, 45, 102, 114, '#E8ECF4')
s.box(360, 882, M(360), 936, -108, 108, '#10142C')
s.box(513, 880, M(513), 950, 106, 120, SILVER)

# arms: silver shoulder blocks, blue sleeves with darker cuffs
for f in BOTH:
    s.box(f(200), 686, f(364), 900, -80, 80, '#B0C0DC').f(R(f(200), 820, f(364), 900), '#8898B8')
    s.box(f(196), 612, f(368), 694, -84, 84, '#D0D8E8')
s.cube(768, 712, 86, 20, 20, 20, '#FFFFFF', rz=45)

# silver pickaxe head held upright in the left hand
s.box(288, 840, 312, 892, 60, 120, '#5A2A18')
s.box(166, 740, 298, 1120, 64, 118, '#D8DCE6', rz=-4, pivot=(232, 930, 91)).f(
    rot(R(270, 740, 298, 1120), -4, (232, 930)), '#7890C8')

# head: face, miner helmet with a lamp, brim
head = s.box(369, 370, M(369), 670, -110, 110, SKIN)
s.box(520, 206, M(520), 250, -30, 30, SILVER)
s.box(345, 244, M(345), 352, -116, 116, SILVER)
s.box(490, 248, M(490), 342, 114, 130, '#A0A0A8')
s.box(507, 262, M(507), 328, 128, 134, '#FFFFFF')
s.box(322, 344, M(322), 376, -130, 130, '#D8DAE2')

# face: angry brows, eyes, big black mustache
for f in BOTH:
    head.f(P((f(430), 408), (f(512), 420), (f(512), 442), (f(430), 430)), '#10121E')
for x, hx in ((442, 448), (M(498), M(492))):
    head.f(R(x, 440, x + 56, 530), '#05051A').f(R(hx, 455, hx + 20, 480), '#FFFFFF')
s.prism(P((452, 550), (M(452), 550), (M(452), 568), (670, 568), (670, 636), (634, 636), (634, 590),
          (462, 590), (462, 636), (426, 636), (426, 568), (452, 568)), 108, 120, '#10121E')

render(s, sys.argv[1])

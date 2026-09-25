import sys
from lib3d import *

ZOOM = 3
s = Scene()
BLUE, SKIN, WHITE = '#5090F0', '#FCD8BC', '#F8F0EA'

# stepped pink hat with a pale tip
s.box(375, 105, 455, 190, -30, 30, '#F4D8F0').f(R(415, 105, 455, 190), '#D8C0E0')
s.box(370, 185, 480, 260, -50, 50, '#F8C0E0')
s.box(355, 250, 545, 350, -80, 80, '#F8C0E0')
s.box(330, 340, 615, 420, -110, 110, '#F8C0E0')
s.box(295, 410, 670, 510, -140, 140, '#F8C0E0')
s.box(288, 505, 677, 540, -146, 146, '#F870C0')

# quartz crystals on the shoulders
crystal(s, 222, 735, 60, 84, '#F0D8F0', ang=-20, z=-10, d=50)
crystal(s, 190, 775, 62, 44, '#D890E0', ang=-10, z=20, d=40)
crystal(s, 735, 757, 54, 72, '#F8F0F8', ang=20, z=0, d=46)

# boots and legs
for x0, x1 in ((315, 472), (482, 638)):
    s.box(x0, 1182, x1, 1255, -70, 96, '#7A300A').f(R(x0 + 12, 1195, x1 - 30, 1245), '#9A4818')
    s.box(x0 + 7, 1128, x1 - 3, 1190, -66, 66, '#8A4012')

# blue tunic, belt with a pink quartz buckle
s.box(305, 760, 655, 1130, -100, 100, BLUE).f(R(305, 1075, 655, 1130), '#3878E0')
s.box(297, 1018, 660, 1075, -104, 104, '#2A140A')
gem(s, 477, 1060, 42, 102, 116, '#F8E0F0')

# arms: blue sleeves, darker cuffs, hands
for x0, x1 in ((160, 305), (650, 800)):
    s.box(x0, 760, x1, 1100, -76, 76, BLUE).f(R(x0, 975, x1, 1010), '#3070E0').f(R(x0, 1010, x1, 1100), SKIN)

# head: face, white bushy brows, eyes, big nose
head = s.box(312, 538, 650, 760, -120, 120, SKIN)
head.f(P((365, 560), (445, 550), (445, 575), (365, 585)), '#FFFFFF', line=True)
head.f(P((518, 550), (600, 560), (600, 585), (518, 575)), '#FFFFFF', line=True)
for x in (383, 533):
    head.f(R(x, 590, x + 47, 645), '#05051A').f(R(x, 590, x + 22, 620), '#FFFFFF')

# long white beard in three tiers with a mustache, nose on top
s.box(415, 955, 545, 1015, 100, 124, WHITE)
s.box(365, 865, 595, 960, 102, 128, WHITE)
s.box(320, 708, 642, 870, 106, 134, WHITE).f(R(372, 708, 595, 745), '#FFFAF6')
s.box(440, 645, 522, 720, 128, 150, '#FFB0A0')

render(s, sys.argv[1])

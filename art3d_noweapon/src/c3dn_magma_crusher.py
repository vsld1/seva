import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 1044 - x
BOTH = (lambda x: x, M)
ROCK, DARK, PAD = '#3A2222', '#26151D', '#40293A'
LAVA, YEL = '#FF5A0A', '#FFF000'

# feet with glowing lava soles, cracked legs
for (x0, x1), crack in (((357, 504), ((445, 800), (418, 868))), ((516, 662), ((575, 806), (598, 873)))):
    s.box(x0, 890, x1, 962, -70, 92, '#0C0A0C').f(R(x0, 936, x1, 962), '#FF2A0A')
    s.box(x0, 796, x1, 896, -70, 70, DARK).f(B(crack[0], crack[1], 11), LAVA)

# torso with lava cracks and a yellow core gem, hips
torso = s.box(341, 536, M(341), 724, -100, 100, ROCK)
for a, b in (((457, 563), (422, 625)), ((578, 576), (615, 643)), ((455, 683), (466, 724)), ((595, 693), (583, 724))):
    torso.f(B(a, b, 11), LAVA)
gem(s, 522, 632, 56, 98, 116, YEL)
hips = s.box(341, 718, M(341), 802, -96, 96, DARK)
hips.f(B((462, 710), (480, 750), 11), LAVA).f(B((586, 715), (560, 758), 11), LAVA)

# arms: rocky forearms with a dark band, big shoulder blocks
for f in BOTH:
    s.box(f(182), 600, f(342), 812, -80, 80, ROCK).f(R(f(182), 690, f(342), 708), DARK)
    s.box(f(158), 470, f(362), 612, -94, 94, PAD)

# head: glowing knob, stepped hat, band, face, jaw with a lava mouth
s.box(425, 114, M(425), 172, -60, 60, DARK).paint('top', LAVA)
s.box(390, 166, M(390), 246, -90, 90, ROCK)
s.box(372, 240, M(372), 302, -104, 104, ROCK)
head = s.box(367, 340, M(367), 544, -110, 110, ROCK)
s.box(358, 296, M(358), 346, -116, 116, DARK)
for x in (426, 562):
    head.f(R(x, 363, x + 62, 390), YEL).f(R(x + 6, 367, x + 34, 374), '#FFFFB0')
s.box(383, 462, M(383), 548, 104, 122, DARK).f(R(448, 488, M(448), 503), LAVA)

render(s, sys.argv[1])

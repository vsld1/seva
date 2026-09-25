import sys
from lib3d import *

s = Scene()
M = lambda x: 1004 - x
BOTH = (lambda x: x, M)
ROCK, DARK, APRON = '#2E1A1C', '#1A0E14', '#8A2000'
OR, YEL, CREAM = '#FF9A00', '#FFF000', '#FFF8D0'

# molten cone on the head
s.box(447, 86, M(447), 132, -40, 40, CREAM)
s.box(402, 128, M(402), 194, -70, 70, YEL)
s.box(360, 190, M(360), 258, -96, 96, OR)

# feet
for f in BOTH:
    s.box(f(338), 928, f(495), 992, -70, 92, '#0A0A14')

# leather apron body with a pocket
s.box(342, 590, M(342), 936, -100, 100, APRON).f(R(342, 590, 356, 936), '#5A1406').f(R(M(356), 590, M(342), 936), '#5A1406')
s.box(432, 788, 568, 848, 98, 108, '#7A1A00')

# arms: dark shoulders with orange tabs, forearms, gloves; a lava crack on the right
for f in BOTH:
    s.box(f(190), 600, f(340), 760, -72, 72, '#2A1A1C')
    s.box(f(186), 752, f(342), 862, -76, 78, '#8A2A08')
    s.box(f(172), 528, f(340), 604, -84, 84, DARK)
    s.box(f(212), 512, f(268), 536, -30, 30, OR)
s.box(730, 650, 752, 722, 72, 76, OR)

# big smithing hammer head held in the left hand
ham = s.prism(P((96, 612), (292, 608), (286, 872), (86, 876)), 60, 150, '#5A6078')
ham.f(R(158, 650, 212, 702), '#0E1A2E').f(R(270, 690, 286, 820), YEL)
s.box(80, 866, 296, 906, 56, 154, OR)

# head: rocky face with lava cracks, band, glowing eyes
head = s.box(331, 254, M(331), 604, -110, 110, ROCK)
head.f(B((366, 345), (382, 295), 8), OR).f(B((642, 340), (626, 295), 8), OR)
s.box(322, 346, M(322), 386, -116, 116, DARK)
for x in (390, M(455)):
    head.f(R(x, 390, x + 65, 428), YEL).f(R(x + 6, 395, x + 36, 403), '#FFFFB8')

# fiery beard in tiers with a dark mustache, tongs hanging below
s.box(457, 740, 467, 832, 104, 114, '#1A2438')
s.box(450, 688, M(450), 746, 108, 130, CREAM)
s.box(402, 602, M(402), 692, 110, 138, YEL)
s.box(355, 496, M(355), 608, 110, 144, OR)
s.box(400, 474, M(400), 510, 140, 152, DARK)

render(s, sys.argv[1])

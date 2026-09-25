import sys
from lib3d import *

s = Scene()
M = lambda x: 976 - x
BOTH = (lambda x: x, M)
BR, SKIN = '#5A3A24', '#F8CCA8'

# legs and trousers with brown patches
for f in BOTH:
    s.box(f(300), 896, f(482), 1010, -80, 90, '#1E4A28')
hip = s.box(290, 842, M(290), 904, -96, 96, '#0E2412').f(R(300, 842, 400, 890), '#3A5A1E').f(R(M(400), 842, M(300), 890), '#3A5A1E')
for x1 in (350, M(422)):
    hip.f(R(x1, 845, x1 + 72, 890), '#4A1A10')

# jacket with buttons, a patch and pockets, dark collar, tan belt
s.box(296, 548, M(296), 846, -100, 100, BR).f(RR(582, 658, 72, 40, 12), '#3A1A0E')
s.box(286, 520, M(286), 576, -104, 104, '#2A1A10')
for y in (618, 682, 742):
    s.box(478, y - 12, 500, y + 12, 98, 108, '#E0B878')
for x1 in (338, 548):
    s.box(x1, 722, x1 + 94, 786, 98, 110, '#3A2414')
s.box(290, 776, M(290), 812, -104, 104, '#E4C078')

# arms: brown sleeves, lighter cuffs, hands
for f in BOTH:
    s.box(f(134), 478, f(296), 712, -78, 78, BR)
    s.box(f(128), 702, f(302), 754, -82, 82, '#7A5E4C')
    s.box(f(134), 748, f(296), 836, -76, 78, SKIN)

# rake held upright in the left hand: tines on top, grey handle, dark grip, white tip
s.box(58, 594, 272, 628, 70, 110, '#9098B8')
for x in (54, 110, 170, 234):
    s.box(x, 566, x + 32, 610, 74, 106, '#A8B0C8')
s.prism(B((140, 1062), (170, 680), 50), 66, 114, '#8890B0')
s.box(118, 680, 210, 772, 60, 120, '#5A5A70')
s.box(76, 864, 154, 936, 64, 116, '#5A2A14')
s.box(118, 1010, 160, 1066, 70, 110, '#FFFFFF')

# head: face, flat cap with a dark brim
head = s.box(304, 148, M(304), 542, -110, 110, SKIN).f(R(632, 180, 660, 204), '#101014')
s.box(290, 82, M(290), 132, -116, 116, '#6E5238')
s.box(314, 124, M(314), 168, -100, 130, '#343A48')

# face: brows, eyes, stubble, big nose, pipe
for f in BOTH:
    head.f(R(f(366), 252, f(460), 282), '#7A2A10')
for x in (380, M(442)):
    head.f(R(x, 290, x + 62, 368), '#0A0A20').f(R(x + 12, 296, x + 28, 330), '#FFFFFF')
head.f(R(344, 420, M(344) + 20, 526), '#E8B47A')
s.box(468, 352, 534, 418, 108, 128, '#F0B488')
s.box(336, 418, 400, 506, 110, 160, '#7A2A08')
s.prism(B((400, 468), (440, 486), 12), 110, 122, '#3A1A08')

render(s, sys.argv[1])

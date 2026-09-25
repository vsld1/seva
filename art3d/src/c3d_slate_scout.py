import sys
from lib3d import *

s = Scene()
M = lambda x: 1060 - x
BOTH = (lambda x: x, M)
BLUE, SKIN, CYAN, STRAP = '#3E6090', '#F8D4A8', '#10D0D8', '#3A1A08'

# little scout drone hovering above
s.box(112, 150, 346, 170, -14, 14, '#1E2A48')
s.box(194, 124, 258, 188, -26, 26, '#101828').f(R(204, 134, 222, 150), '#FFD400')

# red feather tucked into the hat
s.prism(B((382, 276), (366, 222), 18), -40, -20, '#E81818')

# legs and boots
for f in BOTH:
    s.box(f(368), 930, f(528), 1024, -76, 76, '#2A4068')
    s.box(f(352), 1012, f(532), 1104, -80, 100, '#101424').f(R(f(352), 1012, f(532), 1052), '#383A4C')

# coat with lapels, strap, belt, scarf tail, orange badge, map note
s.box(352, 640, M(352), 940, -100, 100, BLUE).f(B((630, 880), (664, 672), 16), STRAP)
s.prism(P((452, 668), (522, 668), (506, 764)), 98, 106, '#2A4674')
s.prism(P((538, 668), (620, 668), (556, 764)), 98, 106, '#2A4674')
s.box(342, 866, M(342), 918, -104, 104, '#2E1406')
s.box(402, 800, 438, 930, 100, 110, STRAP)
s.prism(E(438, 776, 16, 24), 100, 110, '#E89020')
s.prism(P((362, 660), (455, 660), (440, 800), (362, 792)), 104, 118, CYAN)
s.prism(RR(622, 846, 88, 96, 10), 106, 114, '#FCF0D0').f(RR(622, 846, 56, 8, -12), '#E82020')

# arms: blue sleeves, dark gloves
for f in BOTH:
    s.box(f(204), 606, f(352), 862, -74, 74, BLUE)
    s.box(f(204), 846, f(356), 936, -76, 78, '#12162A')

# spyglass held in the left hand
s.box(196, 768, 250, 876, 70, 130, '#B8BCD0')
s.box(246, 806, 326, 886, 84, 134, '#A8ACC0')

# head: face, turquoise scarf, hat with a gold band, wide brim
head = s.box(354, 330, M(354), 604, -104, 104, SKIN)
s.box(340, 590, M(340), 672, -110, 110, CYAN)
s.box(372, 194, M(372) - 30, 270, -86, 86, '#44658E')
s.box(362, 264, M(362) - 30, 290, -90, 90, '#FFC000')
s.box(272, 286, 796, 340, -150, 150, '#5474A0')

# face: brows, eyes with a scar, mouth
head.f(P((410, 400), (494, 406), (494, 424), (410, 418)), '#2E1406')
head.f(P((566, 406), (652, 398), (652, 416), (566, 424)), '#2E1406')
for x, hx in ((422, 432), (580, 594)):
    head.f(R(x, 432, x + 58, 506), '#05051A').f(R(hx, 440, hx + 18, 470), '#FFFFFF')
head.f(B((440, 502), (424, 420), 12), '#E88870').f(P((490, 566), (550, 570), (550, 582), (490, 578)), '#6A0A08')

render(s, sys.argv[1])

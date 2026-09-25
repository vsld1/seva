import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 1010 - x          # symmetric around x = 505
BOTH = (lambda x: x, M)
KHAKI, SKIN, BEARD, BROWN = '#D0B890', '#F8D0A0', '#E0DCDC', '#6A3A18'

# boots and trousers with knee patches
for f in BOTH:
    x0, x1 = sorted((f(345), f(495)))
    s.box(x0, 818, x1, 906, -66, 66, '#8A6040').f(R(min(f(375), f(450)), 836, max(f(375), f(450)), 889), '#B08050')
    s.box(x0, 902, x1, 968, -70, 92, '#4A2410')

# khaki shirt, red neckerchief, diagonal strap, belt with a brass buckle
t = s.box(350, 600, M(350), 818, -96, 96, KHAKI).f(R(375, 608, 411, 650), '#E4D4B4')
s.box(334, 560, M(334), 606, -100, 100, '#FF2010')
s.prism(B((405, 600), (600, 832), 30), 96, 104, BROWN).f(RR(490, 690, 40, 36, -48), '#A07040')
s.box(341, 761, M(341), 806, -100, 100, '#4A2410')
s.box(481, 757, M(481), 814, 100, 112, '#B09050')

# sleeves with patches, hands
for f in BOTH:
    x0, x1 = sorted((f(214), f(350)))
    px0, px1 = sorted((f(249), f(327)))
    s.box(x0, 518, x1, 825, -66, 66, '#D8C4A0').f(R(px0, 615, px1, 679), '#B8A080').f(R(x0, 731, x1, 825), SKIN)

# head: bushy grey brows, eyes, big nose
head = s.box(351, 285, M(351), 600, -106, 106, SKIN)
head.f(R(397, 334, 476, 362), '#D8D4D0').f(R(M(476), 334, M(397), 362), '#D8D4D0')
for x in (411, M(463)):
    head.f(R(x, 371, x + 52, 429), '#05051A').f(R(x + 9, 371, x + 23, 401), '#FFFFFF')

# white beard in three tiers with a moustache, nose on top
s.box(414, 578, M(414), 656, 100, 122, '#D8D4D4')
s.box(375, 480, M(375), 582, 104, 128, BEARD)
s.box(415, 464, M(415), 501, 126, 138, '#C8C4C4')
s.box(478, 428, M(478), 480, 106, 136, '#F4B080')

# wide-brimmed hat with a brown band
s.box(454, 150, M(454), 163, -40, 40, '#A87848')
s.box(366, 160, M(366), 229, -104, 104, '#C8A070')
s.box(360, 225, M(360), 255, -108, 108, '#7A3A10')
s.box(262, 250, M(262), 287, -150, 150, '#D0A878')

render(s, sys.argv[1])

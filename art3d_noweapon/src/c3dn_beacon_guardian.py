import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 994 - x
BOTH = (lambda x: x, M)
BL, NAVY = '#2448A0', '#1E3A7A'

# antenna, glass shield at the right arm, shoulder crystal
s.box(472, 14, 522, 80, -20, 20, '#5AA8D8')
crystal(s, 232, 360, 40, 90, '#F0F4F8', ang=-30, z=0, d=36)

# feet and legs
s.box(336, 794, M(336), 840, -70, 90, '#1A3478')
s.box(332, 698, M(332), 800, -76, 76, '#1E3E90').f(R(362, 718, 455, 800), '#3A5AB0').f(R(M(455), 718, M(362), 800), '#3A5AB0')

# torso with three white diamonds, belt with a pale top edge
s.box(330, 444, M(330), 672, -90, 90, '#2A52AA')
for x, y in ((418, 520), (M(418), 520), (497, 592)):
    gem(s, x, y, 34, 88, 98, '#FFFFFF')
s.box(312, 662, M(312), 700, -94, 94, '#0E1E50').f(R(312, 662, M(312), 680), '#D8F4FC')

# arms and shoulder blocks
for f in BOTH:
    s.box(f(190), 494, f(332), 700, -66, 66, BL)
    s.box(f(159), 380, f(334), 500, -80, 80, NAVY)

# head: hat with a white diamond, visor with the beacon lens, lower face panels
s.box(318, 74, M(318), 130, -96, 96, NAVY)
s.box(329, 124, M(329), 250, -90, 90, BL)
gem(s, 497, 192, 38, 88, 100, '#F4F8FC')
s.box(324, 238, M(324), 324, -94, 94, '#080A20').f(R(346, 272, M(346), 292), '#D8F8FC')
s.box(448, 258, M(448), 306, 92, 104, '#60F0F8').f(R(466, 264, M(466), 300), '#FFFFFF')
s.box(329, 316, M(329), 452, -90, 90, BL).f(R(345, 330, 395, 440), '#1A3070').f(R(M(395), 330, M(345), 440), '#1A3070')

# the light beam falling from the lens
s.prism(P((470, 300), (524, 300), (660, 836), (334, 836)), 104, 108, '#DCF5FF', alpha=0.45, line=False, cast=False)
s.prism(P((488, 300), (506, 300), (522, 836), (472, 836)), 108, 110, '#FFFFFF', alpha=0.5, line=False, cast=False)

render(s, sys.argv[1])

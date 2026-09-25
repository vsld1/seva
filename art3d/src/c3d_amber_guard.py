import sys
from lib3d import *

s = Scene()
M = lambda x: 910 - x
BOTH = (lambda x: x, M)
GOLD, BR, BELT = '#FFBE12', '#8B4A12', '#6E340B'
SKIN, GAUNT = '#FCDDBA', '#C8620C'


def quad(p0, c, p1, n=12):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t * t * p1[0],
             (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t * t * p1[1]) for t in (i / n for i in range(n + 1))]

# shield strapped to the side of the right arm
s.box(712, 524, 752, 692, -44, 44, BELT)

# legs with knee pads, boots with golden soles
for f in BOTH:
    s.box(f(318), 684, f(451), 768, -62, 62, '#5C2A0C').f(R(f(335), 700, f(415), 746), '#8B4A1A')
    s.box(f(312), 755, f(440), 814, -66, 84, '#C0600E').f(R(f(312), 794, f(440), 814), '#9C7A10')

# torso, golden chest plate, belt with a gem
s.box(310, 462, M(310), 692, -86, 86, BR)
s.box(349, 488, M(349), 632, 84, 98, GOLD).f(RR(418, 544, 32, 12, 28), BR)
s.box(305, 632, M(305), 692, -92, 92, BELT)
gem(s, 455, 660, 27, 90, 104, GOLD)

# arms: sleeves, gauntlets, big golden shoulder pads
for f in BOTH:
    s.box(f(186), 512, f(318), 612, -62, 62, BR)
    s.box(f(190), 600, f(318), 700, -66, 70, GAUNT)
    s.box(f(170), 428, f(322), 522, -76, 80, GOLD)

# amber sword held blade-down beside the left gauntlet: dark grip, pale diamond guard, golden blade
s.box(212, 450, 234, 500, 86, 108, '#4A2410')
blade = s.prism(P((206, 516), (238, 516), (238, 668), (222, 698), (206, 676)), 88, 106, '#FFC61A')
blade.paint('right', '#F0B090').f(R(219, 526, 225, 664), '#FFE27A')
s.cube(222, 504, 97, 40, 40, 36, '#FFE88A', rz=45)

# head: crest, sideburns, face, helmet, rim
s.box(430, 76, 480, 152, -40, 40, GOLD)
for f in BOTH:
    s.box(f(296), 256, f(326), 380, -80, 60, BR)
head = s.box(320, 246, M(320), 470, -100, 108, SKIN)
s.box(310, 142, M(310), 232, -110, 118, GOLD)
s.box(300, 228, M(300), 252, -114, 122, BR)
for f in BOTH:
    head.f(P((f(364), 274), (f(432), 283), (f(432), 297), (f(364), 289)), '#8B2A0A')
for x in (375, M(416)):
    head.f(R(x, 296, x + 41, 362), '#0A0A20').f(R(x + 6, 305, x + 18, 324), '#FFFFFF')
head.f(R(434, 402, 476, 414), '#8B1A0A')

render(s, sys.argv[1])

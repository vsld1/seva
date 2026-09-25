import sys
from lib3d import *

s = Scene()
M = lambda x: 956 - x
BOTH = (lambda x: x, M)
ST, DK, DKR = '#A9A6A0', '#6B6A63', '#56554F'
GR, GR_DK = '#3DAA28', '#1F8E14'
GLOW = '#F6FF5A'

# floating stones above the crown, green crystal and stone spikes
for cx, cy, sz, a, col in ((304, 170, 50, -12, '#5E5B55'), (350, 178, 44, 8, '#77746E'),
                           (M(304), 170, 50, 12, '#5E5B55'), (M(350), 178, 44, -8, '#77746E'), (478, 150, 56, 0, '#3E3D3A')):
    s.cube(cx, cy, 0, sz, sz, sz, col, rz=a)
crystal(s, 478, 242, 48, 130, '#62D84A', z=0)
for x in (365, 478, M(365)):
    s.prism(P((x, 240), (x + 32, 298), (x - 32, 298)), 66, 98, '#8C8983')

# feet, lower body, green trim
for f in BOTH:
    s.box(f(340), 918, f(470), 962, -60, 84, '#4E4D4A').f(R(f(340), 946, f(470), 962), GR)
s.box(335, 812, M(335), 900, -80, 80, DKR)
s.box(332, 895, M(332), 926, -84, 84, GR)

# torso, belt
s.box(328, 588, M(328), 780, -90, 90, ST)
s.box(323, 774, M(323), 816, -96, 96, DK)

# arms with bracers, dark pauldrons topped with white stones
for f in BOTH:
    s.box(f(160), 566, f(330), 832, -80, 80, ST).f(R(f(160), 700, f(330), 744), '#8F8C85')
    s.box(f(182), 518, f(322), 584, -88, 88, '#474950')
    s.box(f(215), 486, f(292), 524, -40, 40, '#F5F5F7')

# head, brow ridge, glowing eyes
head = s.box(345, 350, M(345), 604, -110, 110, ST)
s.box(336, 404, M(336), 448, -114, 120, DK)
for x in (390, M(441)):
    head.f(R(x, 455, x + 51, 482), GLOW).f(R(x + 6, 459, x + 30, 466), '#FFFFC8')

# green beard in tiers, mustache on top
s.box(439, 730, M(439), 792, 96, 124, '#38A828')
s.box(397, 644, M(397), 734, 100, 132, GR_DK)
s.box(355, 520, M(355), 646, 106, 140, '#3BA426')
s.box(390, 504, M(390), 540, 134, 150, GR_DK)

# crown band with notches, green trim, gem
s.box(327, 292, M(327), 336, -116, 116, '#9E9B94').f(R(350, 312, 372, 320), '#86837C').f(R(420, 318, 440, 326), '#86837C').f(
    R(540, 308, 566, 316), '#86837C').f(R(590, 318, 608, 326), '#86837C')
s.box(323, 330, M(323), 357, -120, 120, GR)
gem(s, 478, 318, 36, 118, 136, '#8CF55A')

# glowing rune tablet held in the left hand
s.prism(D(232, 690, 90), 84, 108, '#B6B2A8').f(D(232, 690, 62), '#5A5A58')
s.prism(D(232, 690, 42), 108, 118, '#8A877F')
gem(s, 232, 690, 24, 118, 126, GLOW)

render(s, sys.argv[1])

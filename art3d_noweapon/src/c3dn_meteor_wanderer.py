import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 920 - x
BOTH = (lambda x: x, M)
NAVY, OR, ROCK = '#1E2448', '#FF8A10', '#7A5040'


def rock(cx, cy, sz, ang, col=ROCK, z=90, glow=None):
    r = s.cube(cx, cy, z, sz, sz, sz * 0.9, col, rz=ang, ry=14)
    if glow:
        x0, y0, x1, y1 = glow
        r.f(rot(R(cx + x0, cy + y0, cx + x1, cy + y1), ang, (cx, cy)), '#FFD400')
    return r

# a rock behind the left arm and one floating above the head
rock(240, 96, 62, 25, '#4A2A22', z=0, glow=(-24, 6, -14, 16))

# legs with orange boots
for f in BOTH:
    s.box(f(322), 702, f(455), 846, -66, 76, NAVY).f(R(f(322), 826, f(455), 846), '#A04A10')

# torso with lightning streaks, red collar, belt
s.box(328, 524, M(328), 684, -86, 86, NAVY).f(B((405, 635), (440, 560), 9), '#FFD400').f(B((500, 602), (478, 562), 9), '#FFD400')
s.box(317, 488, M(317), 530, -90, 90, '#D02010')
s.box(320, 668, M(320), 706, -90, 90, '#5A3020')

# arms: sleeves and grey gloves
for f in BOTH:
    s.box(f(220), 480, f(340), 626, -60, 60, '#2A2F5A')
    s.box(f(228), 620, f(332), 730, -56, 58, '#5A5A8A')

# a floating rock by the right foot
rock(630, 760, 70, 25, z=60, glow=(8, 4, 22, 14))

# head: knob, hood, orange frame, face, goggles, scar, mouth
s.box(414, 180, M(414), 208, -40, 40, '#3A3A6A')
s.box(304, 198, M(304), 242, -92, 92, '#28305A')
s.box(296, 234, M(296), 498, -96, 96, OR)
head = s.box(326, 258, M(326), 500, 88, 104, '#EAD8D0')
g = s.box(340, 338, M(340), 398, 102, 112, '#FFF070').f(R(380, 338, 420, 398), '#FFC800').f(R(M(420), 338, M(380), 398), '#FFC800')
head.f(B((528, 452), (548, 405), 8), '#C88070').f(R(439, 444, M(439), 453), '#5A1A08')

render(s, sys.argv[1])

import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 970 - x
BOTH = (lambda x: x, M)
PUR, PUR_DK = '#2E1463', '#1E0B4A'
BONE = '#F5E9DA'
CYAN = '#8CF5E6'

# antlers on the hat
for f in BOTH:
    s.prism(B((f(398), 214), (f(372), 60), 22), -12, 12, '#E6CFB2')
    s.prism(B((f(390), 156), (f(312), 124), 18), -10, 10, '#E6CFB2')

# feet, lower robe, mint trim
for f in BOTH:
    s.box(f(342), 852, f(472), 898, -60, 82, '#0F7A48')
s.box(328, 724, M(328), 832, -84, 84, '#2A125A').f(R(482, 724, 488, 832), PUR_DK)
s.box(325, 824, M(325), 860, -88, 88, '#5CF2A2')

# robe torso with a dark collar, belt, bone beads and a gem
s.box(338, 500, M(338), 740, -84, 84, PUR).f(R(338, 500, M(338), 542), PUR_DK)
s.box(332, 700, M(332), 729, -90, 90, '#B06E3A')
for x, y in ((389, 579), (436, 569), (485, 561), (M(436), 569), (M(389), 579)):
    s.box(x - 16, y - 16, x + 16, y + 16, 82, 102, BONE)
gem(s, 485, 638, 36, 82, 98, CYAN)

# arms: sleeves and bony hands
for f in BOTH:
    s.box(f(216), 490, f(338), 664, -62, 62, PUR)
    s.box(f(212), 654, f(338), 752, -64, 66, BONE)

# head: skull and hat
head = s.box(346, 243, M(346), 514, -110, 110, BONE).f(R(346, 425, M(346), 514), '#E9DAC6')
s.box(333, 183, M(333), 248, -116, 116, PUR_DK)
for x in (393, M(459)):
    head.f(R(x, 320, x + 66, 373), '#0B0B12').f(R(x + 19, 336, x + 47, 360), CYAN)
head.f(D(485, 395, 17), '#0B0B12').f(R(420, 458, M(420), 471), '#0B0B12')
for x in (444, 470, 496, 522):
    head.f(R(x, 438, x + 5, 460), '#0B0B12')

# floating bone orbs
for cx, cy, sz, a in ((236, 392, 58, 18), (628, 516, 62, -14)):
    s.cube(cx, cy, 0 if cx < 485 else 118, sz, sz, sz, '#FFFFFF', rz=a, ry=20)

render(s, sys.argv[1])

import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 870 - x           # symmetric around the face centre (x = 435)
BOTH = (lambda x: x, M)
BLUE, SKIN, YEL = '#0898E8', '#F8D8B8', '#FFE800'

# hair with two tufts
s.cube(385, 120, -10, 65, 42, 60, '#3A1808', rz=-8)
s.cube(482, 120, -10, 95, 50, 70, '#3A1808', rz=6)
s.box(275, 130, M(275), 225, -110, 110, '#3A1808').f(R(275, 178, M(275), 182), '#5A3A2A')

# snorkel tube at the side of the head
s.box(250, 130, 282, 360, -40, -8, YEL)
s.box(245, 200, 275, 218, -44, -4, '#FF5A10')

# swim shoes with straps and legs
for f in BOTH:
    x0, x1 = sorted((f(277), f(432)))
    sx = x0 + 55
    s.box(x0, 815, x1, 935, -70, 110, '#FFC000').f(R(x0, 895, x1, 935), '#FF9A00').f(R(sx, 840, sx + 20, 880), '#FF9A00')
    x0, x1 = sorted((f(285), f(432)))
    s.box(x0, 785, x1, 820, -66, 66, BLUE)

# body with a yellow chest band and waist band, collar with gems
s.box(278, 485, M(278), 760, -92, 92, BLUE).f(R(278, 550, M(278), 575), YEL)
s.box(275, 755, M(275), 785, -96, 96, YEL)
s.box(335, 510, M(335), 528, 90, 96, '#F4F0EC')
for f in BOTH:
    gem(s, f(373), 530, 20, 94, 102, '#F8E0C0')
gem(s, 435, 545, 30, 94, 106, '#F8B8D8')

# arms: blue sleeves with a yellow band, hands
for f in BOTH:
    x0, x1 = sorted((f(140), f(278)))
    s.box(x0, 430, x1, 735, -70, 70, BLUE).f(R(x0, 545, x1, 575), YEL).f(R(x0, 635, x1, 735), SKIN)

# head, dive mask with straps, mouthpiece, mouth
head = s.box(280, 225, M(280), 490, -106, 106, SKIN).f(R(414, 422, 457, 438), '#8A2010')
for f in BOTH:
    x0, x1 = sorted((f(267), f(303)))
    s.box(x0, 295, x1, 340, -40, 110, '#141428')
mask = s.box(303, 270, M(303), 393, 104, 128, '#141428').f(R(318, 288, M(318), 382), '#2A6A98')
mask.f(R(342, 303, 390, 375), '#05051A').f(R(M(390), 303, M(342), 375), '#05051A')
s.box(275, 395, 365, 435, 100, 124, YEL)

render(s, sys.argv[1])

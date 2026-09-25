import sys
from lib3d import *

ZOOM = 3
s = Scene()
BLUE, SKIN, YEL = '#0898E8', '#F8D8B8', '#FFE800'

# hair with two tufts
s.cube(378, 120, -10, 65, 42, 60, '#3A1808', rz=-8)
s.cube(482, 120, -10, 95, 50, 70, '#3A1808', rz=6)
s.box(275, 130, 600, 225, -110, 110, '#3A1808').f(R(275, 178, 600, 182), '#5A3A2A')

# snorkel tube at the side of the head
s.box(250, 130, 282, 360, -40, -8, YEL)
s.box(245, 200, 275, 218, -44, -4, '#FF5A10')

# swim shoes and legs
for x0, x1, sx in ((270, 425, 330), (433, 587, 488)):
    s.box(x0, 815, x1, 935, -70, 110, '#FFC000').f(R(x0, 895, x1, 935), '#FF9A00').f(R(sx, 840, sx + 20, 880), '#FF9A00')
for x0, x1 in ((280, 425), (430, 570)):
    s.box(x0, 785, x1, 820, -66, 66, BLUE)

# body with a yellow chest band and waist band, collar with gems
s.box(270, 485, 585, 760, -92, 92, BLUE).f(R(270, 550, 585, 575), YEL)
s.box(270, 755, 590, 785, -96, 96, YEL)
s.box(330, 510, 530, 528, 90, 96, '#F4F0EC')
for cx in (368, 492):
    gem(s, cx, 530, 20, 94, 102, '#F8E0C0')
gem(s, 430, 545, 30, 94, 106, '#F8B8D8')

# arms: blue sleeves with a yellow band, hands
for x0, x1 in ((135, 273), (587, 725)):
    s.box(x0, 430, x1, 735, -70, 70, BLUE).f(R(x0, 545, x1, 575), YEL).f(R(x0, 635, x1, 735), SKIN)

# head, dive mask with straps, mouthpiece, mouth
head = s.box(280, 225, 590, 490, -106, 106, SKIN).f(R(430, 422, 473, 438), '#8A2010')
for x0, x1 in ((267, 303), (568, 602)):
    s.box(x0, 295, x1, 340, -40, 110, '#141428')
mask = s.box(303, 270, 568, 393, 104, 128, '#141428').f(R(318, 288, 552, 382), '#2A6A98')
mask.f(R(342, 303, 390, 375), '#05051A').f(R(480, 303, 530, 375), '#05051A')
s.box(275, 395, 365, 435, 100, 124, YEL)

render(s, sys.argv[1])

import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 1020 - x
BOTH = (lambda x: x, M)
BRONZE, SKIN = '#C85E14', '#F8C084'

# red crest on a bronze stem
s.box(465, 180, 547, 265, -30, 30, '#D87A10').f(R(465, 180, 490, 265), '#D8A070')
s.box(468, 138, 545, 190, -34, 34, '#FF1818').f(R(468, 138, 495, 190), '#FF5050')

# skirt tabs, lower band, boots
for x0, x1 in ((340, 485), (495, 645)):
    s.box(x0, 985, x1, 1040, -72, 92, '#A84A14')
s.box(333, 962, 657, 990, -96, 96, '#7A2A08')
sk = s.box(335, 865, 655, 965, -94, 94, '#6A3020')
for x0, x1 in ((340, 400), (470, 525), (590, 650)):
    sk.f(R(x0, 865, x1, 965), '#E06A10')

# tunic with teal edges, shoulder studs, chest seam and ridges, belt
t = s.box(335, 630, 670, 840, -100, 100, '#C05808').f(R(335, 630, 358, 840), '#108878').f(R(647, 630, 670, 840), '#108878')
t.f(R(498, 660, 508, 800), '#E07010').f(R(390, 688, 490, 708), '#F08020').f(R(520, 688, 620, 708), '#F08020')
for f in BOTH:
    gem(s, f(388), 660, 35, 98, 110, '#E09020')
s.box(330, 823, 668, 865, -104, 104, '#6A2A12')

# arms: skin, bronze cuff band, bracer, hand
for x0, x1 in ((195, 335), (668, 810)):
    s.box(x0, 570, x1, 875, -74, 74, SKIN).f(R(x0, 745, x1, 760), '#D0801C').f(R(x0, 760, x1, 825), '#B85A10')

# head: hair at the sides, face, helmet with rivets, brim, nose guard
for f in BOTH:
    s.box(min(f(315), f(360)), 380, max(f(315), f(360)), 530, -90, 80, '#C85A18')
head = s.box(350, 375, 670, 630, -110, 110, SKIN)
s.box(333, 245, 707, 360, -118, 118, BRONZE).f(R(387, 325, 408, 345), '#E8A020').f(R(630, 325, 651, 345), '#E8A020')
s.box(325, 352, 713, 380, -124, 124, '#A84810')
s.box(498, 375, 533, 468, 108, 120, '#B04A10')

# face: angry brows, eyes, beard with the mouth
head.f(P((405, 406), (472, 416), (472, 434), (405, 424)), '#6A1A08').f(P((553, 416), (622, 406), (622, 424), (553, 434)), '#6A1A08')
for x in (412, 560):
    head.f(R(x, 428, x + 53, 505), '#05051A').f(R(x + 8, 440, x + 26, 463), '#FFFFFF')
s.box(383, 547, 637, 630, 106, 130, '#8A3208').f(R(487, 547, 537, 560), '#5A0A08')

render(s, sys.argv[1])

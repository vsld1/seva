import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 1020 - x          # symmetric around the face centre (x = 510)
BOTH = (lambda x: x, M)
BRONZE, SKIN = '#C85E14', '#F8C084'


def mbox(x0, y0, x1, y1, z0, z1, col):
    """Box plus its mirror image on the other side."""
    return [s.box(min(f(x0), f(x1)), y0, max(f(x0), f(x1)), y1, z0, z1, col) for f in BOTH]

# red crest on a bronze stem
s.box(470, 180, 550, 265, -30, 30, '#D87A10').f(R(470, 180, 495, 265), '#D8A070')
s.box(472, 138, 548, 190, -34, 34, '#FF1818').f(R(472, 138, 498, 190), '#FF5050')

# boots, lower band, skirt with orange tabs
mbox(345, 985, 500, 1040, -72, 92, '#A84A14')
s.box(338, 962, M(338), 990, -96, 96, '#7A2A08')
sk = s.box(340, 865, M(340), 965, -94, 94, '#6A3020')
for x0 in (345, 480):
    sk.f(R(x0, 865, x0 + 60, 965), '#E06A10')
sk.f(R(M(405), 865, M(345), 965), '#E06A10')

# tunic with teal edges, shoulder studs, chest seam and ridges, belt
t = s.box(340, 630, M(340), 840, -100, 100, '#C05808').f(R(340, 630, 363, 840), '#108878').f(R(M(363), 630, M(340), 840), '#108878')
t.f(R(505, 660, 515, 800), '#E07010').f(R(395, 688, 495, 708), '#F08020').f(R(M(495), 688, M(395), 708), '#F08020')
for f in BOTH:
    gem(s, f(393), 660, 35, 98, 110, '#E09020')
s.box(335, 823, M(335), 865, -104, 104, '#6A2A12')

# arms: skin, bronze cuff band, bracer, hand
for b in mbox(195, 570, 340, 875, -74, 74, SKIN):
    x0, x1 = b.faces[0].pts[:, 0].min(), b.faces[0].pts[:, 0].max()
    b.f(R(x0, 745, x1, 760), '#D0801C').f(R(x0, 760, x1, 825), '#B85A10')

# head: hair at the sides, face, helmet with rivets, brim, nose guard
mbox(315, 380, 360, 530, -90, 80, '#C85A18')
head = s.box(350, 375, M(350), 630, -110, 110, SKIN)
s.box(323, 245, M(323), 360, -118, 118, BRONZE).f(R(382, 325, 403, 345), '#E8A020').f(R(M(403), 325, M(382), 345), '#E8A020')
s.box(317, 352, M(317), 380, -124, 124, '#A84810')
s.box(493, 375, 527, 468, 108, 120, '#B04A10')

# face: angry brows, eyes, beard with the mouth
head.f(P((405, 406), (472, 416), (472, 434), (405, 424)), '#6A1A08').f(P((M(472), 416), (M(405), 406), (M(405), 424), (M(472), 434)), '#6A1A08')
for x in (412, M(465)):
    head.f(R(x, 428, x + 53, 505), '#05051A').f(R(x + 8, 440, x + 26, 463), '#FFFFFF')
s.box(383, 547, M(383), 630, 106, 130, '#8A3208').f(R(485, 547, 535, 560), '#5A0A08')

render(s, sys.argv[1])

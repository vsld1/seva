import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1250 - x
BOTH = (lambda x: x, M)
ST, MID, PALE, GAUNT, BAND, CRACK = '#A89090', '#9A8080', '#D0BCC0', '#2A3048', '#1A1E30', '#FFC800'


def speck(p, x, y):
    p.f(R(x - 12, y - 12, x + 12, y + 12), '#EAE2E2')

# legs with lighter plates
for f in BOTH:
    s.box(f(430), 912, f(616), 1072, -90, 90, '#7A6468').f(R(f(450), 948, f(590), 1050), '#9A8488')

# torso with cracks and specks, belt
t = s.box(400, 596, M(400), 824, -130, 130, MID)
t.f(B((530, 795), (585, 650), 12), CRACK).f(B((752, 760), (738, 675), 12), CRACK)
for x, y in ((683, 665), (456, 760), (783, 828)):
    speck(t, x, y)
s.box(422, 818, M(422), 916, -126, 126, '#1E2238').f(B((548, 892), (515, 822), 12), CRACK)

# arms: pale upper stone, spiked dark gauntlets, big tilted shoulder stones
for f, a in ((lambda x: x, -8), (M, 8)):
    s.box(f(150), 730, f(402), 840, -110, 110, '#D8C8C8')
    g = s.box(f(155), 812, f(400), 1030, -106, 106, GAUNT).f(R(f(155), 812, f(400), 840), BAND).f(R(f(155), 960, f(400), 1000), BAND)
    for i in range(3):
        x0 = min(f(165 + i * 76), f(165 + i * 76 + 76))
        s.prism(P((x0, 956), (x0 + 38, 872), (x0 + 76, 956)), 104, 132, '#A88088')
    s.cube(f(288), 628, 0, 244, 204, 230, PALE, rz=a)
    s.box(f(218), 468, f(358), 548, -60, 60, '#9A8488')
s.box(215, 845, 245, 902, 106, 108, CRACK, line=False)

# head: stone blocks on top, upper tier with specks, band, face, jaw
s.box(458, 152, 545, 212, -60, 60, '#C0A8A8')
s.box(545, 144, 618, 212, -60, 60, '#8A8098')
s.box(618, 150, 798, 212, -60, 60, '#8A7078')
up = s.box(419, 205, M(419), 278, -110, 110, '#B09898')
speck(up, 492, 258)
speck(up, 776, 250)
head = s.box(419, 352, M(419), 522, -120, 120, ST)
s.box(400, 268, M(400), 362, -126, 126, MID)
for x in (492, M(572)):
    head.f(R(x, 370, x + 80, 412), '#FFF000').f(R(x + 6, 375, x + 40, 384), '#FFFFB0')
head.f(B((745, 500), (770, 418), 10), CRACK)
speck(head, 556, 460)
speck(head, 462, 487)
s.box(435, 504, M(435), 610, 110, 134, MID).f(R(513, 548, M(513), 566), '#3A1A1A')

render(s, sys.argv[1])

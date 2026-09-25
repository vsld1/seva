import sys
from lib3d import *

s = Scene()
M = lambda x: 1000 - x
BOTH = (lambda x: x, M)

SKIN = '#F2AC68'
BAND = '#C1621A'
TUN = '#B14E12'
BLACK = '#26262E'
WHITE = '#F8F3E8'
STONE = '#8088A8'

# feathers stuck into the headband
def feather(base, top, w, col, mark=None):
    (bx, by), (tx, ty) = base, top
    p = s.prism(B(base, top, w), -16, 16, col)
    if mark:
        a, b = mark
        L = math.hypot(tx - bx, ty - by)
        ux, uy = (tx - bx) / L, (ty - by) / L
        p.f(B((bx + ux * a, by + uy * a), (bx + ux * b, by + uy * b), w + 2), BLACK)
    return p

for f in BOTH:
    feather((f(470), 300), (f(452), 140), 32, BLACK)
    feather((f(378), 300), (f(318), 172), 40, '#F0201F')
    feather((f(444), 300), (f(414), 150), 46, '#FFDF1A', mark=(92, 136))
feather((500, 300), (500, 116), 42, WHITE, mark=(140, 190))

# white fur tufts at the band ends
for f in BOTH:
    s.prism(P((f(300), 262), (f(244), 284), (f(270), 300), (f(248), 318), (f(300), 338)), -70, 70, '#F4EAD8')

# legs, boots, front flap
for f in BOTH:
    s.box(f(292), 1010, f(492), 1126, -95, 95, '#9C4410')
    s.box(f(298), 1116, f(478), 1212, -100, 128, '#4A1A08')
s.box(452, 1012, 548, 1120, 96, 112, '#C2601E')

# torso with dark shoulder patches and a tooth necklace
s.box(280, 690, 720, 1000, -130, 130, TUN).f(R(292, 708, 344, 760), '#6E2A0C').f(R(656, 708, 708, 760), '#6E2A0C')
for t in range(-3, 4):
    x, y = 500 + t * 38, 778 + (9 - t * t) * 4.2
    s.prism(RR(x, y + 26, 18, 52, -t * 12), 128, 142, WHITE, line=True)

# arms with fur bands
for f in BOTH:
    s.box(f(82), 668, f(284), 1046, -112, 118, SKIN)
    s.box(f(72), 780, f(292), 824, -122, 128, '#F4EAD8')

# belt and skull buckle
s.box(274, 955, 726, 1025, -138, 138, '#561E0B')
s.box(458, 944, 542, 1046, 130, 166, WHITE).f(R(468, 980, 490, 1004), '#15151B').f(R(510, 980, 532, 1004), '#15151B')

# bone club held in front of the left hand, with stone spikes
s.box(40, 826, 82, 890, 150, 210, STONE)
s.box(226, 836, 284, 896, 150, 210, STONE)
s.box(124, 976, 196, 1030, 150, 210, STONE)
s.box(68, 764, 240, 990, 130, 230, WHITE)

# head: face, headband, black band, turquoise gem
head = s.box(304, 390, 696, 716, -150, 170, SKIN)
s.box(290, 326, 710, 402, -158, 178, BAND)
s.box(294, 258, 706, 328, -154, 174, BLACK)
s.prism(D(500, 362, 48), 176, 196, '#1FE8C8').f(P((500, 314), (500, 362), (452, 362)), '#A3F8EA').f(
    P((500, 362), (548, 362), (500, 410)), '#13B79C')

for f in BOTH:
    head.f(P((f(362), 410), (f(466), 438), (f(466), 470), (f(362), 442)), '#15151B')
    head.f(R(f(350), 470, f(372), 574), '#EE1F22')
    head.f(R(f(400), 548, f(421), 600), '#EE1F22')
for x1 in (386, M(444)):
    head.f(R(x1, 452, x1 + 58, 548), '#15151B').f(R(x1 + 9, 462, x1 + 27, 488), '#FFFFFF')
head.f(R(342, 610, 658, 706), '#101014').f(R(452, 622, 548, 638), '#8A0D0D')

render(s, sys.argv[1])

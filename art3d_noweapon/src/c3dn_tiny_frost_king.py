import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1120 - x
BOTH = (lambda x: x, M)
BLUE, ICE, SNOW, FACE = '#1E88F0', '#E8F0F8', '#F8F8FA', '#E4EEF8'

# ice crystals on the crown
for cx, top, w, z in ((478, 165, 36, -30), (M(478), 165, 36, -30), (432, 105, 60, -40), (M(432), 105, 60, -40), (560, 38, 62, -50)):
    crystal(s, cx, (top + 250) / 2, w, 250 - top, ICE, z=z, d=w * 0.9)

# legs, snowy boots, soles
for f in BOTH:
    s.box(f(385), 1040, f(553), 1086, -76, 96, '#90A8B8')
    s.box(f(390), 988, f(553), 1050, -74, 90, SNOW)
    s.box(f(395), 898, f(553), 994, -70, 70, '#1040E0')

# robe with a snowflake, gold belt with an ice gem
t = s.box(387, 650, M(387), 912, -100, 100, BLUE)
for a in (0, 60, -60):
    t.f(RR(560, 775, 12, 80, a), '#FFFFFF')
s.box(378, 850, M(378), 900, -104, 104, '#D8A000')
gem(s, 560, 878, 30, 102, 114, '#A0E0F8')

# arms: blue sleeves, snowy cuffs; small crystals on the shoulders
for f in BOTH:
    s.box(f(240), 590, f(387), 806, -70, 70, BLUE)
    s.box(f(232), 798, f(393), 876, -74, 74, SNOW)
s.box(M(387), 870, M(240), 926, -70, 72, SNOW)
crystal(s, 285, 560, 38, 86, '#D0E8F8', ang=-25, z=0, d=34)
crystal(s, M(285), 562, 38, 86, '#D0E8F8', ang=25, z=0, d=34)

# head: face, ice crown band with a blue gem
head = s.box(385, 308, M(385), 604, -100, 100, FACE)
s.box(363, 238, M(363), 316, -106, 106, '#C8E4F4')
gem(s, 560, 274, 42, 104, 120, '#20A0F0')

# face: white brows, blue eyes, rosy cheeks
for f in BOTH:
    head.f(P((f(440), 402), (f(525), 408), (f(525), 426), (f(440), 420)), '#FFFFFF', line=True)
    head.f(R(f(415), 522, f(462), 548), '#F8B8D0')
for x in (455, M(512)):
    head.f(R(x, 428, x + 57, 515), '#0A3AC0').f(R(x + 8, 442, x + 24, 468), '#FFFFFF')

# fur collar, white beard with a pink nose, ice pendant
s.box(350, 578, M(350), 662, -106, 106, SNOW)
s.box(420, 540, M(420), 680, 98, 130, '#FFFFFF')
s.box(537, 497, M(537), 532, 128, 140, '#F8B0C8')
s.box(487, 672, M(487), 742, 104, 122, '#B8DCF0')

# sparkles
for x, y, r, z in ((546, 20, 12, -40), (360, 778, 12, 110), (690, 905, 16, 110)):
    s.cube(x, y, z, r * 1.3, r * 1.3, r * 1.3, '#FFFFFF', rz=45, ry=20)

render(s, sys.argv[1])

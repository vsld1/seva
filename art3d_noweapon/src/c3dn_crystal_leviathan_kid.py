import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 964 - x
BOTH = (lambda x: x, M)
CY, CY_SH, CY_DK = '#18D8E8', '#10B8C8', '#0A8898'

# crystal horn and little hood horns
crystal(s, 479, 150, 44, 96, '#A8F0F8', z=0, d=40)
for f in BOTH:
    s.prism(P((f(300), 240), (f(272), 200), (f(302), 198)), -30, 30, CY_SH)

# legs and feet
for f in BOTH:
    s.box(f(330), 776, f(478), 882, -66, 66, '#10A8B8')
    s.box(f(326), 872, f(480), 940, -70, 90, CY_DK)

# body with a striped belly, belt with a peach gem
s.box(325, 538, M(325), 780, -96, 96, CY)
belly = s.box(388, 568, M(388), 760, 94, 104, '#DCEEE8')
for y in (610, 654, 698):
    belly.f(R(388, y, M(388), y + 10), '#B4E0D8')
s.box(318, 744, M(318), 780, -100, 100, CY_SH)
gem(s, 482, 764, 28, 100, 112, '#F8C0A8')

# arms with pale mint hands
for f in BOTH:
    s.box(f(204), 500, f(325), 706, -62, 62, '#20E2EE')
    s.box(f(204), 700, f(325), 790, -64, 66, '#B8F4EC')

# hood: sides, face, top, brim, eyes on top, teeth along the brim
for f in BOTH:
    s.box(f(292), 288, f(334), 552, -100, 100, CY_SH)
head = s.box(332, 288, M(332), 556, -96, 96, '#F2F4F2')
s.box(298, 194, M(298), 244, -104, 104, CY)
s.box(265, 238, M(265), 294, -110, 110, '#20D8E8')
for f in BOTH:
    s.box(f(355), 180, f(412), 238, 10, 60, '#FFE800').f(R(f(376), 186, f(390), 232), '#0B0B14')
for x in (350, 438, 526, 614):
    s.prism(D(x, 304, 12), 108, 118, '#D8D8E6')

# face
for x in (388, M(438)):
    head.f(R(x, 378, x + 50, 456), '#0A4A7A')
for f in BOTH:
    head.f(R(f(355), 452, f(398), 474), '#F8B8C8')
head.f(R(459, 488, M(459), 500), '#1A6A7A')

render(s, sys.argv[1])

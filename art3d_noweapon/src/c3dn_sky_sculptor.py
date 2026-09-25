import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1044 - x
BOTH = (lambda x: x, M)
WH, ROBE, BLUE, GOLD = '#F4F5FB', '#E6EAF7', '#1E90F0', '#D8A800'
SKIN = '#FCEBE0'

# floating halo
s.box(382, 88, M(382), 128, -70, 70, '#FFF200')

# feet, lower robe, blue hem with a gold edge
for f in BOTH:
    s.box(f(356), 978, f(505), 1016, -60, 84, '#4A8A7A')
s.box(342, 852, M(342), 960, -90, 90, ROBE).f(R(402, 852, 458, 876), BLUE).f(R(564, 852, 620, 876), BLUE)
s.box(336, 948, M(336), 986, -94, 94, BLUE).f(R(336, 978, M(336), 986), '#F8C800')

# robe with blue straps, gold belt with a gem
s.box(352, 590, M(352), 860, -88, 88, ROBE).f(R(402, 740, 458, 860), BLUE).f(R(564, 740, 620, 860), BLUE)
s.box(344, 806, M(344), 856, -92, 92, GOLD)
gem(s, 522, 831, 32, 90, 104, '#FFE800')

# arms with blue bands
for f in BOTH:
    s.box(f(222), 545, f(352), 870, -68, 68, ROBE).f(R(f(222), 764, f(352), 792), BLUE)

# head: side tuft, face, fluffy white hair
s.box(322, 258, 364, 364, -80, 70, WH)
head = s.box(360, 288, M(360), 612, -100, 104, SKIN)
hair = P((340, 146), (M(340), 146), (M(340), 306), (672, 306), (672, 288), (610, 288), (610, 300), (560, 300),
         (560, 284), (500, 284), (500, 298), (432, 298), (432, 318), (400, 318), (400, 296), (360, 296), (360, 306), (340, 306))
s.prism(hair, -110, 114, WH).f(R(545, 166, 598, 230), '#FFFFFF')

# face: white brows, blue eyes, rosy cheeks, beard and mustache
for f in BOTH:
    head.f(P((f(410), 380), (f(496), 370), (f(496), 394), (f(410), 404)), WH, line=True)
    head.f(R(f(388), 486, f(432), 508), '#F8C0D0')
for x, hx in ((422, 429), (568, 577)):
    head.f(R(x, 412, x + 52, 471), '#0A5AE8').f(R(hx, 412, hx + 16, 445), '#FFFFFF')
s.box(379, 526, M(379), 662, 100, 126, '#FBF3EE')
s.box(409, 656, 650, 749, 96, 118, '#F8F2EE')
s.box(425, 494, M(425), 536, 104, 132, '#FFFBF8')

render(s, sys.argv[1])

import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 900 - x
BOTH = (lambda x: x, M)
ST, BODY, DARK = '#7E6A66', '#664E4A', '#624E4A'
ZAP, ZAPW = '#F8F070', '#FFFFFF'

# legs and feet, with lightning cracks
for f in BOTH:
    s.box(f(292), 826, f(448), 868, -70, 90, '#2A1A18')
s.box(297, 732, 444, 834, -70, 70, '#3E2E2C').f(B((358, 818), (380, 750), 10), ZAP)
s.box(M(444), 732, M(297), 834, -70, 70, '#3E2E2C').f(B((540, 820), (510, 758), 10), ZAP)

# torso with lightning cracks and a white diamond core
torso = s.box(258, 466, M(258), 738, -110, 110, BODY)
for a, b, col in (((358, 502), (393, 565), ZAP), ((360, 568), (332, 625), ZAP), ((545, 512), (515, 578), ZAPW),
                  ((533, 578), (570, 638), ZAPW), ((385, 650), (412, 712), ZAP), ((508, 660), (485, 722), ZAPW)):
    torso.f(B(a, b, 10), col)
gem(s, 450, 572, 58, 108, 126, '#FFFFFF')

# arms with dark cuffs, glowing bits on the wrists, tilted shoulder blocks
for f in BOTH:
    s.box(f(116), 540, f(258), 744, -72, 72, ST).f(R(f(116), 632, f(258), 744), '#5E4A46')
for f, a in ((lambda x: x, -7), (M, 7)):
    s.cube(f(185), 470, 0, 192, 180, 170, '#8C7876', rz=a)
s.box(128, 634, 166, 664, 70, 82, '#FFFFFF')
s.box(166, 648, 210, 668, 70, 80, ZAP)
s.box(688, 648, 760, 680, 70, 84, '#FFFFFF')
s.box(684, 674, 704, 686, 70, 80, ZAP)

# head: three stones on top, stepped hat with a crack, band, face with glowing eyes
s.box(312, 98, 396, 158, -60, 60, '#A0908A')
s.box(396, 98, 436, 158, -60, 60, '#5A5868')
s.box(436, 96, M(312), 158, -60, 60, '#5A4848')
s.box(288, 154, M(288), 222, -96, 96, '#806A66').f(B((332, 165), (358, 214), 8), ZAPW)
head = s.box(288, 278, M(288), 490, -104, 104, ST)
s.box(267, 214, M(267), 284, -110, 110, DARK)
for x in (345, M(413)):
    head.f(R(x, 297, x + 68, 333), '#FFFFFF')
head.f(B((578, 352), (550, 400), 10), ZAP).f(B((563, 400), (585, 442), 10), ZAP)

render(s, sys.argv[1])

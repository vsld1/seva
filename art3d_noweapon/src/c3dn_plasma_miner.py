import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 872 - x
BOTH = (lambda x: x, M)
GRAY, BLUE, NAVY, DARK, CYAN = '#C8CCD8', '#2448A0', '#1A3A8A', '#0A1030', '#20F0F8'

# antenna
s.box(320, 95, 330, 168, -5, 5, '#2A3040')
s.box(314, 76, 336, 98, -11, 11, CYAN)

# legs with knee plates, feet
for f in BOTH:
    s.box(f(290), 702, f(430), 802, -64, 64, NAVY).f(R(f(305), 734, f(390), 790), '#B8BCC8')
    s.box(f(288), 794, f(432), 840, -68, 86, DARK)

# torso: navy frame, grey chest plate with a plasma core, belt with lights
s.box(286, 480, M(286), 712, -90, 90, NAVY)
s.box(304, 492, M(304), 680, 88, 100, GRAY)
s.cyl(436, 583, 98, 108, 46, '#2A3448')
s.cyl(436, 583, 106, 112, 34, CYAN)
s.box(278, 668, M(278), 706, -94, 94, '#0E1A40')
for x in (366, 436, 506):
    s.box(x - 9, 678, x + 9, 696, 92, 100, CYAN)

# arms: blue sleeves, dark gloves, grey shoulder pads with cyan trim
for f in BOTH:
    s.box(f(174), 504, f(286), 726, -58, 58, BLUE).f(R(f(174), 632, f(286), 726), DARK)
    s.box(f(164), 440, f(290), 504, -66, 66, GRAY)
    s.box(f(164), 500, f(290), 514, -62, 62, CYAN)

# helmet: ear knob, shell, face, mint visor
s.box(248, 280, 272, 372, -40, 40, '#A8ACBC')
s.box(264, 160, M(264), 494, -100, 90, GRAY)
head = s.box(287, 210, M(287), 492, 80, 96, '#FAD8B8')
visor = s.box(287, 244, M(287), 456, 94, 104, '#6ADFB8')
for x in (350, M(397)):
    visor.f(R(x, 318, x + 47, 384), '#05051A').f(R(x + 8, 326, x + 22, 346), '#FFFFFF')
visor.f(R(414, 420, M(414), 430), '#1A5A3A')

render(s, sys.argv[1])

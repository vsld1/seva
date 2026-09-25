import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1164 - x
BOTH = (lambda x: x, M)
NAVY, BODY, MAG = '#0E1036', '#07072C', '#FF1EF0'

# crystal antenna and magenta-lined horns on the helmet
crystal(s, 582, 212, 76, 176, '#4A80D0', z=-10, d=64)
s.prism(P((546, 132), (582, 108), (618, 132), (618, 150), (546, 150)), -40, 20, '#2050E0')
for f, a in ((lambda x: x, -14), (M, 14)):
    h = s.prism(RR(f(340), 292, 52, 100, a), -30, 30, NAVY)
    h.f(RR(f(340) + (-16 if f(0) == 0 else 16), 302, 20, 80, a), MAG)

# shoulder crystals
crystal(s, 262, 600, 50, 108, '#1E3AE0', ang=36, z=0, d=46)
crystal(s, M(262), 606, 50, 108, '#E0D8E8', ang=-36, z=0, d=46)

# legs with magenta diamonds, feet
for f in BOTH:
    s.box(f(396), 966, f(575), 1104, -88, 88, BODY)
    s.box(f(390), 1098, f(579), 1172, -92, 112, '#1A0A4A').f(R(f(390), 1140, f(579), 1172), '#4A0A8A')
    gem(s, f(485), 1046, 50, 86, 98, MAG)

# torso with the void ring, magenta belt
s.box(396, 680, M(396), 950, -110, 110, BODY)
s.cyl(582, 832, 108, 118, 68, MAG)
s.cyl(582, 832, 116, 122, 54, '#000000')
s.box(378, 936, M(378), 972, -114, 114, MAG)

# arms: shoulder blocks, sleeves with magenta bands, right cuff
for f in BOTH:
    s.box(f(206), 760, f(382), 1010, -84, 84, NAVY).f(R(f(206), 866, f(382), 906), MAG)
    s.box(f(192), 640, f(384), 772, -92, 92, NAVY)
s.box(M(382), 990, M(206), 1020, -86, 86, MAG)

# helmet with a magenta band and a starry void face
s.box(342, 278, M(342), 690, -118, 118, NAVY)
s.box(334, 330, M(334), 390, -124, 124, MAG)
face = s.box(390, 390, M(390), 680, 110, 124, '#000000')
for x, y, sz in ((474, 498, 44), (M(518), 498, 44), (462, 424, 12), (700, 434, 12), (514, 590, 13), (626, 620, 13),
                 (438, 638, 11), (716, 566, 12), (600, 470, 8)):
    face.f(R(x, y, x + sz, y + sz), '#FFFFFF')

render(s, sys.argv[1])

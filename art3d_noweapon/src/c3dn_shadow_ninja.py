import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1152 - x
BOTH = (lambda x: x, M)
BLK, NAVY, MAG = '#080818', '#1E2242', '#FF20E0'

# shoulder crystals
crystal(s, 262, 482, 66, 96, '#1850E0', ang=-25, z=0, d=56)
crystal(s, M(262), 488, 66, 96, '#E0D8F0', ang=25, z=0, d=56)

# legs, feet with a purple glow
for f in BOTH:
    s.box(f(380), 888, f(572), 1000, -90, 90, '#05050E')
    s.box(f(376), 990, f(574), 1070, -94, 110, '#0A0A1A').f(R(f(376), 1056, f(574), 1070), '#3A10A0')

# torso with a purple collar line, sheathed sword, belt with a magenta gem, shuriken
s.box(360, 598, M(360), 842, -120, 120, BLK).f(R(360, 598, M(360), 616), '#7A10E8')
s.prism(B((430, 906), (726, 600), 44), 118, 132, NAVY)
s.prism(B((392, 956), (408, 862), 22), 118, 130, '#2A2E50')
s.box(360, 822, M(360), 896, -124, 124, '#121430')
gem(s, 572, 864, 45, 122, 136, MAG)
for a in (0, 90):
    s.prism(RR(776, 706, 132, 28, a - 12), 118, 128, '#1A1E40')
gem(s, 776, 706, 16, 126, 132, MAG)

# arms with banded wraps
for f in BOTH:
    s.box(f(196), 548, f(361), 924, -84, 84, '#06061A')
    s.box(f(184), 760, f(372), 782, -90, 90, '#10142C')
    s.box(f(184), 800, f(372), 824, -90, 90, '#10142C')

# hood: top, band, dark face with glowing eyes, black mask
s.box(335, 84, M(335), 152, -110, 110, '#0A0A20')
s.box(318, 145, M(318), 604, -126, 110, '#10122C')
s.box(318, 144, M(318), 226, -130, 130, '#151836')
face = s.box(369, 224, M(369), 600, 100, 116, '#03030A')
for x in (436, M(524)):
    face.f(R(x, 340, x + 88, 376), '#FFD8FF')
s.box(355, 404, M(355), 596, 110, 128, '#000000')

render(s, sys.argv[1])

import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 1140 - x
BOTH = (lambda x: x, M)
ST, ST_DK, MOSS, RUNE = '#AEA9A2', '#807C74', '#3AAA28', '#40E8E0'

# sprout on top
s.prism(B((492, 150), (490, 96), 10), -5, 5, '#9ADC2A')
s.prism(B((490, 108), (454, 84), 10), -5, 5, '#C8F040')

# legs with moss knee patches, feet
for f in BOTH:
    s.box(f(390), 808, f(562), 930, -80, 80, ST_DK).f(R(f(410), 848, f(535), 894), MOSS)
    s.box(f(386), 924, f(564), 1000, -84, 104, '#5E5A54').f(R(f(386), 964, f(564), 1000), '#22A040')

# torso with glowing runes, hip band
t = s.box(362, 528, M(362), 748, -110, 110, '#86827A')
for a, b in (((468, 598), (468, 686)), ((448, 624), (492, 636)), ((560, 600), (560, 690)), ((536, 642), (586, 642)),
             ((656, 606), (660, 690)), ((636, 664), (680, 648))):
    t.f(B(a, b, 10), RUNE)
s.box(336, 738, M(336), 814, -116, 116, '#9A968E')

# arms: stone upper, dark bracer, stone lower with a rune diamond, mossy shoulder pads
for f in BOTH:
    s.box(f(186), 578, f(346), 704, -76, 76, ST)
    s.box(f(136), 700, f(382), 756, -100, 100, '#3A3834')
    s.box(f(146), 752, f(352), 886, -90, 90, ST)
    s.prism(D(f(258), 814, 56), 88, 96, RUNE).f(D(f(258), 814, 32), '#141414')
    s.box(f(126), 486, f(372), 584, -104, 104, ST)
    s.box(f(156), 440, f(350), 492, -86, 86, MOSS)

# glowing rune tablets floating beside the arms
for cx, a in ((292, -8), (M(292) + 10, 8)):
    s.prism(RR(cx, 690, 88, 132, a), 104, 124, '#7EF4EC').f(RR(cx, 690, 16, 68, a), '#1E4A48')

# head: face, top block, moss cap, band with a rune gem, glowing eyes, mouth
head = s.box(386, 302, M(386), 540, -112, 112, ST)
s.box(386, 176, M(386), 242, -104, 104, ST)
s.box(419, 144, M(419), 180, -86, 86, MOSS)
s.box(365, 238, M(365), 308, -118, 118, ST_DK)
gem(s, 570, 276, 40, 116, 130, RUNE)
for x in (455, M(525)):
    head.f(R(x, 335, x + 70, 372), '#40F0E0').f(R(x + 6, 340, x + 36, 348), '#B8FCF6')
head.f(R(492, 460, M(492), 474), '#141414')

render(s, sys.argv[1])

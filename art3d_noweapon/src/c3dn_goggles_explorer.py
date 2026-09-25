import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 850 - x           # symmetric around x = 425
BOTH = (lambda x: x, M)
SKIN, TAN, CREAM = '#FAD4A0', '#E0A840', '#F8ECD4'

# sun hat with round goggles on the front
s.box(285, 79, M(285), 222, -95, 95, '#F8D888').f(R(285, 79, M(285), 100), '#FCE4A8')
s.box(261, 218, M(261), 251, -118, 118, '#F0C050')
for cx in (360, M(360)):
    s.prism(C(cx, 210, 49), 118, 128, '#6A2A08', smooth=True).f(C(cx, 210, 37), '#FFC000')
s.box(405, 204, M(405), 216, 118, 126, '#6A2A08')

# legs with cuffs, boots
for f in BOTH:
    x0, x1 = sorted((f(285), f(416)))
    s.box(x0, 664, x1, 765, -66, 66, '#E8B050').f(R(x0, 720, x1, 765), '#F8DC98')
    s.box(x0, 762, x1, 810, -70, 90, '#8A3A08')

# jacket over a white shirt, pockets with flaps, belt and buckle
s.box(261, 442, M(261), 652, -96, 96, TAN).f(R(395, 442, M(395), 615), '#F8ECD8')
s.box(258, 650, M(258), 668, -98, 98, '#F8E8C8')
s.box(397, 611, M(397), 665, 96, 110, '#B88A00')
for x in (300, M(379)):
    s.box(x, 547, x + 79, 607, 96, 104, '#C87C20').f(R(x, 547, x + 79, 562), '#B86A10')

# sleeves with cuffs and hands
for f in BOTH:
    x0, x1 = sorted((f(154), f(270)))
    s.box(x0, 390, x1, 671, -64, 64, CREAM).f(R(x0, 560, x1, 592), '#F0DCB0').f(R(x0, 592, x1, 671), SKIN)

# head, eyes
head = s.box(288, 245, M(288), 445, -100, 100, SKIN)
for x in (342, M(387)):
    head.f(R(x, 274, x + 45, 344), '#05051A').f(R(x + 7, 284, x + 22, 308), '#FFFFFF')

# orange scarf with a hanging end
s.box(266, 346, M(266), 444, -108, 108, '#FFA510').f(R(330, 394, M(330), 428), '#F08000')
s.box(480, 412, 559, 540, 108, 124, '#FFA510')

render(s, sys.argv[1])

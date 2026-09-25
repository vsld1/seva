import sys
from lib3d import *

ZOOM = 2
s = Scene()
M = lambda x: 660 - x
BOTH = (lambda x: x, M)
BLACK, GOLD, SKIN, GLOVE = '#10142A', '#E8B800', '#FCE0CC', '#F8F4F4'

# legs and shoes
for f in BOTH:
    s.box(f(220), 612, f(326), 708, -50, 50, BLACK)
    s.box(f(216), 700, f(328), 726, -54, 70, '#05060E')

# tailcoat, golden vest with buttons, white shirt with a black bowtie
s.box(205, 436, M(205), 616, -78, 78, BLACK)
vest = s.box(272, 470, M(272), 610, 76, 84, '#FFC800')
for y in (515, 545, 578):
    vest.f(R(325, y - 5, 335, y + 5), '#E0C8A0')
s.prism(P((296, 438), (M(296), 438), (330, 512)), 76, 86, '#F8F4F0')
s.prism(P((296, 440), (330, 456), (M(296), 440), (M(296), 472), (330, 460), (296, 472)), 84, 92, '#05060E')
s.prism(E(242, 500, 8, 22), 76, 84, GOLD)

# arms: black sleeves with gold buttons, white gloves
for f in BOTH:
    s.box(f(106), 410, f(205), 556, -48, 48, BLACK)
    s.box(f(108), 550, f(212), 636, -50, 52, GLOVE)
s.prism(E(116, 458, 7, 20), 46, 54, GOLD)
s.prism(E(M(116), 482, 7, 20), 46, 54, GOLD)

# head: face, top hat with a gold band and green gem, brim
head = s.box(215, 208, M(215), 442, -84, 84, SKIN)
s.box(238, 68, M(238), 168, -62, 62, '#0A0A14')
s.box(236, 162, M(236), 196, -64, 64, GOLD)
gem(s, 330, 180, 22, 62, 72, '#20E8A0')
s.box(186, 192, M(186), 214, -90, 90, '#0A0A14')

# face: brows, gold monocle, eye, handlebar mustache, smile
head.f(P((252, 272), (300, 276), (300, 288), (252, 284)), '#5A2A10')
head.f(P((358, 276), (405, 270), (405, 284), (358, 290)), '#5A2A10')
head.f(R(362, 292, 402, 350), '#05051A').f(R(368, 300, 382, 316), '#FFFFFF')
head.f(B((262, 346), (242, 406), 4), GOLD)
s.cyl(278, 318, 82, 90, 34, GOLD)
s.cyl(278, 318, 88, 93, 25, '#FFE870')
s.prism(P((249, 344), (269, 344), (269, 356), (377, 356), (377, 344), (401, 344), (401, 380), (249, 380)), 82, 92, '#4A1A08')
head.f(R(300, 386, 336, 398), '#8B2A10')

render(s, sys.argv[1])

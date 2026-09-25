import sys
from lib3d import *

ZOOM = 3
s = Scene()
M = lambda x: 1012 - x
BOTH = (lambda x: x, M)
SKIN, BAND, TUN, BLACK, WHITE = '#F0AC66', '#C1621A', '#A84410', '#15151B', '#F8F3E8'


def feather(base, top, w, col, mark=None):
    p = s.prism(B(base, top, w), -14, 14, col)
    if mark:
        p.f(R(*mark), BLACK)

# feathers in the headband
feather((414, 200), (379, 150), 30, '#F0201F')
feather((M(414), 200), (M(379), 150), 30, '#F0201F')
feather((461, 200), (446, 128), 36, '#FFDF1A', mark=(438, 134, 457, 166))
feather((M(461), 200), (M(446), 128), 36, '#FFDF1A', mark=(M(457), 134, M(438), 166))
feather((478, 200), (472, 116), 22, BLACK)
feather((M(478), 200), (M(472), 116), 22, BLACK)
feather((506, 200), (506, 100), 27, WHITE, mark=(492, 100, 520, 134))

# fur tufts at the band ends
for f in BOTH:
    s.prism(P((f(360), 206), (f(334), 214), (f(344), 222), (f(332), 230), (f(360), 238)), -60, 60, '#F4EAD8')

# legs, boots, front flap
for f in BOTH:
    s.box(f(358), 744, f(493), 820, -66, 66, '#9C4410')
    s.box(f(364), 814, f(495), 881, -70, 90, '#4A1A08')
s.box(474, 758, 538, 814, 66, 78, '#B85A1C')

# torso: brown tunic with a lighter chest and dark shoulder patches, tooth necklace
t = s.box(345, 476, M(345), 697, -96, 96, TUN).f(R(345, 476, M(345), 566), '#C8742E')
t.f(R(354, 514, 396, 551), '#6E2A0C').f(R(M(396), 514, M(354), 551), '#6E2A0C').f(R(452, 518, 499, 531), '#6E2A0C')
for i, x in enumerate((424, 450, 476, 502, 529, 555, 581)):
    t.f(RR(x, 592, 10, 36, (i - 3) * -14), WHITE)

# arms with cream fur bands and a darker lower band
for f in BOTH:
    s.box(f(223), 491, f(345), 750, -84, 84, SKIN).f(R(f(223), 667, f(345), 709), '#D98A44')
    s.box(f(214), 570, f(352), 600, -90, 90, '#F4EAD8')

# belt with a skull buckle
s.box(342, 694, M(342), 744, -100, 100, '#561E0B')
s.box(474, 690, 538, 761, 96, 122, WHITE).f(R(482, 715, 497, 730), BLACK).f(R(510, 715, 526, 730), BLACK)

# head: face, brown headband with a turquoise gem, black band on top
head = s.box(367, 244, M(367), 519, -120, 120, SKIN)
s.box(357, 244, M(357), 296, -126, 126, BAND)
s.box(360, 197, M(360), 244, -122, 122, '#1D1D24')
gem(s, 506, 272, 36, 124, 138, '#1FE8C8')

# face: angry brows, eyes, red war paint, big open mouth
for f in BOTH:
    head.f(P((f(409), 308), (f(482), 326), (f(482), 348), (f(409), 330)), BLACK)
for x, hx in ((424, 429), (546, 551)):
    head.f(R(x, 330, x + 42, 401), BLACK).f(R(hx, 341, hx + 15, 360), '#FFFFFF')
for f in BOTH:
    head.f(R(f(399), 361, f(416), 435), '#EE1F22').f(R(f(433), 401, f(450), 435), '#EE1F22')
head.f(R(396, 446, M(396), 519), '#101014').f(R(474, 451, 540, 465), '#8A0D0D')

render(s, sys.argv[1])

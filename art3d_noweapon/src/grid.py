"""Raw screenshot upscaled with a labelled grid (labels in model units = px * zoom)."""
import sys
from PIL import Image, ImageDraw
from compare import IMG, SRC
name, zoom, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
x0, y0, x1, y1 = (int(v) for v in sys.argv[4:8]) if len(sys.argv) > 4 else (0, 0, 10 ** 5, 10 ** 5)
S = int(sys.argv[8]) if len(sys.argv) > 8 else 4
im = Image.open(f'{IMG}/{SRC[name]}.png').convert('RGB')
x1, y1 = min(x1, im.width), min(y1, im.height)
im = im.crop((x0, y0, x1, y1)).resize(((x1 - x0) * S, (y1 - y0) * S), Image.NEAREST).convert('RGBA')
lay = Image.new('RGBA', im.size, (0, 0, 0, 0))
d = ImageDraw.Draw(lay)
for gx in range(((x0 + 9) // 10) * 10, x1, 10):
    X = (gx - x0) * S
    major = gx % 50 == 0
    d.line([(X, 0), (X, im.height)], fill=(0, 0, 0, 90 if major else 40), width=1)
    if major:
        d.text((X + 2, 2), str(int(gx * zoom)), fill=(0, 0, 0, 255))
for gy in range(((y0 + 9) // 10) * 10, y1, 10):
    Y = (gy - y0) * S
    major = gy % 50 == 0
    d.line([(0, Y), (im.width, Y)], fill=(0, 0, 0, 90 if major else 40), width=1)
    if major:
        d.text((2, Y + 2), str(int(gy * zoom)), fill=(0, 0, 0, 255))
Image.alpha_composite(im, lay).convert('RGB').save(out)

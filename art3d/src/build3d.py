"""Render 3D character scripts into the repo and build lineup sheets."""
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

OUT = __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..')


def render(name):
    subprocess.run(['python3', f'c3d_{name}.py', f'{OUT}/{name}.png'], check=True)
    return name


def lineup(names, path, h=420, per_row=None):
    ims = [Image.open(f'{OUT}/{n}.png') for n in names]
    ims = [i.resize((round(i.width * h / i.height), h), Image.LANCZOS) for i in ims]
    rows = [ims] if not per_row else [ims[i:i + per_row] for i in range(0, len(ims), per_row)]
    W = max(sum(i.width for i in r) + 40 * (len(r) + 1) for r in rows)
    sheet = Image.new('RGBA', (W, len(rows) * (h + 40) + 40), (255, 255, 255, 255))
    y = 40
    for r in rows:
        x = 40
        for i in r:
            sheet.alpha_composite(i, (x, y))
            x += i.width + 40
        y += h + 40
    sheet.convert('RGB').save(path)


if __name__ == '__main__':
    names = sys.argv[1:]
    with ThreadPoolExecutor(3) as ex:
        for n in ex.map(render, names):
            print('rendered', n)

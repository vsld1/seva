"""Side-by-side sheets: original screenshot next to the 3D render."""
import sys
from PIL import Image, ImageDraw

IMG = '/tmp/claude-0/-home-user-seva/017fc82f-97b2-56db-a375-4fe9cf8801dd/images'
SRC = {'cave_chief': 2, 'amber_guard': 5, 'stone_king': 6, 'bone_shaman': 7, 'dino_kid': 8, 'redhead_kid': 9,
       'magma_crusher': 10, 'mammoth_hunter': 11, 'caveman_kid': 12, 'lord_of_stones': 13, 'ore_creator': 14,
       'sky_sculptor': 15, 'void_guardian': 16, 'chrono_crystal': 17, 'space_kid': 18, 'storm_golem': 19,
       'crystal_leviathan_kid': 20, 'ash_oracle': 21, 'moss_guardian': 22, 'pancake_tower': 23, 'beacon_guardian': 24,
       'lord_of_the_grotto': 25, 'titan_of_the_deep': 26, 'crystal_phoenix_kid': 27, 'plasma_miner': 28,
       'rainbowmancer': 29, 'meteor_wanderer': 30, 'diamond_emperor': 31, 'golden_baron': 32, 'tiny_frost_king': 33,
       'lava_smith': 34, 'ruby_splitter': 35, 'sapphire_seer': 36, 'emerald_garden_mage': 37, 'spike_golem': 38,
       'topaz_lightkeeper': 39, 'coral_diver': 41, 'shadow_ninja': 42, 'silver_miner': 43, 'green_sage': 44,
       'amethyst_vein_guard': 45, 'professor': 46, 'pipe_farmer': 47, 'pastel_princess': 48, 'rusty_mechanic': 49,
       'slate_scout': 50, 'builder': 51,
       'quartz_gnome': 59, 'bronze_digger': 60, 'miner_mouse': 61, 'flint_sparker': 62, 'snorkel_kid': 63,
       'goggles_explorer': 65, 'stone_recruit': 66, 'beret_painter': 67, 'leaf_kid': 68, 'bandana_brawler': 69}


def sheet(names, out, render_dir, h=440):
    tiles = []
    for n in names:
        o = Image.open(f'{IMG}/{SRC[n]}.png').convert('RGB')
        o = o.resize((round(o.width * h / o.height), h), Image.LANCZOS)
        r = Image.open(f'{render_dir}/{n}.png')
        r = r.resize((round(r.width * h / r.height), h), Image.LANCZOS)
        bg = Image.new('RGBA', r.size, (255, 255, 255, 255))
        bg.alpha_composite(r)
        pair = Image.new('RGB', (o.width + bg.width + 10, h), (255, 255, 255))
        pair.paste(o, (0, 0))
        pair.paste(bg.convert('RGB'), (o.width + 10, 0))
        tiles.append(pair)
    W = max(t.width for t in tiles)
    s = Image.new('RGB', (W * 2 + 30, (h + 20) * ((len(tiles) + 1) // 2) + 10), (255, 255, 255))
    for i, t in enumerate(tiles):
        s.paste(t, (10 + (i % 2) * (W + 10), 10 + (i // 2) * (h + 20)))
    s.save(out)


if __name__ == '__main__':
    out, rdir, *names = sys.argv[1:]
    sheet(names, out, rdir)

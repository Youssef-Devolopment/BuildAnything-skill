"""Rasterize assets/logo-mark.svg to assets/logo-mark.png (512x512).

The mark is simple geometry (rounded rect + 4 polygons + 1 rect), so it is
rasterized directly rather than through an SVG engine: render at 4x and
downscale with LANCZOS for clean anti-aliasing.
"""
from pathlib import Path

from PIL import Image, ImageDraw

REPO = Path(__file__).resolve().parent.parent
S = 512
SS = 4  # supersample factor
SIZE = S * SS

BG = (79, 70, 229, 255)      # #4F46E5
FG = (255, 255, 255, 255)


def u(v):
    """SVG user units -> supersampled pixels."""
    return v / 64.0 * SIZE


img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

d.rounded_rectangle([0, 0, SIZE - 1, SIZE - 1], radius=u(15), fill=BG)

# legs: four discrete blocks (the stages)
d.polygon([(u(23), u(18)), (u(30), u(18)), (u(26.11), u(35)), (u(19.11), u(35))], fill=FG)
d.polygon([(u(18.66), u(37)), (u(25.66), u(37)), (u(22), u(53)), (u(15), u(53))], fill=FG)
d.polygon([(u(34), u(18)), (u(41), u(18)), (u(44.89), u(35)), (u(37.89), u(35))], fill=FG)
d.polygon([(u(38.34), u(37)), (u(45.34), u(37)), (u(49), u(53)), (u(42), u(53))], fill=FG)

# crossbar: the stage gate bridging the seam
d.rounded_rectangle([u(21), u(33), u(43), u(40)], radius=u(1.5), fill=FG)

img = img.resize((S, S), Image.LANCZOS)
out = REPO / "assets" / "logo-mark.png"
img.save(out, "PNG", optimize=True)
print(f"wrote {out} ({out.stat().st_size} bytes)")

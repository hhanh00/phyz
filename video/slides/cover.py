"""Render a chapter's video cover, a 1920x1080 still for YouTube and the video's first seconds.

Usage: cover.py STEM

Writes video/out/STEM/STEM-cover.png. Each chapter's text and picture are in COVERS.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from manim import *  # noqa: E402,F403

from engine import FONT, MONO, T, Text  # noqa: E402

NAVY = "#152238"
SKY = "#60a5fa"
AMBER = "#fbbf24"
MINT = "#34d399"
SOFT = "#a9b6c8"


def chip(text, color, size=30):
    label = Text(text, font=MONO, color=color, font_size=size, weight=BOLD)
    box = RoundedRectangle(width=label.width + 0.5, height=label.height + 0.42, corner_radius=0.12,
                           stroke_color=color, stroke_width=4, fill_color=NAVY, fill_opacity=1)
    return VGroup(box, label.move_to(box))


def check(color=MINT):
    mark = Circle(radius=0.22, color=color, fill_color=color, fill_opacity=1, stroke_width=0)
    tick = Text("\u2713", font=FONT, color=NAVY, font_size=26, weight=BOLD)
    return VGroup(mark, tick.move_to(mark))


def thrown_paths():
    """The thrown ball of chapter 1: the real path, two bent paths with the same ends, and the action's flat spot."""
    import numpy as np
    w, h = 6.0, 3.0
    def pt(t, x):
        return [t / 2 * w - w / 2, x / 4.9 * h - h / 2, 0]
    art = VGroup()
    for eps, color, width in ((0.6, SOFT, 3), (-0.6, SOFT, 3), (0, SKY, 7)):
        curve = VMobject(stroke_color=color, stroke_width=width)
        curve.set_points_smoothly([pt(t, 9.8 * t - 4.9 * t * t + eps * np.sin(np.pi * t / 2)) for t in np.linspace(0, 2, 60)])
        art.add(curve)
    for t in (0, 2):
        art.add(Dot(pt(t, 0), color=WHITE, radius=0.12))
    art.add(Line(pt(-0.15, 0), pt(2.15, 0), color=SOFT, stroke_width=3))
    # the action of T - V against the bend: a flat spot at the real path
    bowl = VMobject(stroke_color=AMBER, stroke_width=6)
    bowl.set_points_smoothly([[e * 1.6, -3.3 + 1.3 * e * e, 0] for e in np.linspace(-1, 1, 40)])
    art.add(bowl, Dot([0, -3.3, 0], color=AMBER, radius=0.13),
            DashedLine([-0.9, -3.3, 0], [0.9, -3.3, 0], color=AMBER, stroke_width=3))
    art.add(Text("real path", font=FONT, color=SKY, font_size=30, weight=BOLD).next_to(pt(1, 5.6), UP, buff=0.2),
            Text("action: flat at the real path", font=FONT, color=AMBER, font_size=28, weight=BOLD).move_to([0, -4.05, 0]))
    return art


def two_slit_stripes():
    """Chapter 2: two slits open give stripes, dipping below what one slit alone delivers."""
    import numpy as np
    w, h = 6.4, 3.4
    A = lambda y: np.exp(-(y + 0.35) ** 2 / 2.6)
    B = lambda y: np.exp(-(y - 0.35) ** 2 / 2.6)
    both = lambda y: A(y) + B(y) + 2 * np.sqrt(A(y) * B(y)) * np.cos(4.2 * y)
    def pt(y, v):
        return [y / 3 * w / 2, v / 4.0 * h - h / 2, 0]
    ys = np.linspace(-3, 3, 240)
    art = VGroup(Line(pt(-3.1, 0), pt(3.1, 0), color=SOFT, stroke_width=3))
    summed = VMobject(stroke_color=SOFT, stroke_width=4)
    summed.set_points_smoothly([pt(y, A(y) + B(y)) for y in ys])
    one = VMobject(stroke_color=MINT, stroke_width=4)
    one.set_points_smoothly([pt(y, A(y)) for y in ys])
    curve = VMobject(stroke_color=SKY, stroke_width=7)
    curve.set_points_smoothly([pt(y, both(y)) for y in ys])
    dark = -np.pi / 4.2
    art.add(DashedVMobject(summed, num_dashes=50), one, curve, Dot(pt(dark, both(dark)), color=AMBER, radius=0.14))
    art.add(Text("both slits open", font=FONT, color=SKY, font_size=30, weight=BOLD).next_to(pt(0, 4.0), UP, buff=0.15),
            Text("one slit", font=FONT, color=MINT, font_size=26, weight=BOLD).move_to(pt(-2.7, 1.0)),
            Text("fewer here than with one slit", font=FONT, color=AMBER, font_size=28, weight=BOLD).move_to([0, -h / 2 - 0.7, 0]))
    return art


COVERS = {
    "01-classical-mechanics": {
        "kicker": "PHYZ  ·  CHAPTER 1",
        "title": ["Classical", "Mechanics"],
        "sub": "One motion, described three ways,\nready for quantum theory",
        "art": thrown_paths,
    },
    "02-first-quantization": {
        "kicker": "PHYZ  ·  CHAPTER 2",
        "title": ["First", "Quantization"],
        "sub": "From magnets and two slits\nto the Schrodinger equation",
        "art": two_slit_stripes,
    },
    # "STEM": {"kicker": "PHYZ  ·  CHAPTER N", "title": ["Line", "Line"], "sub": "One line\nor two", "art": a_function},
}


class Cover(Scene):
    def __init__(self, spec, **kwargs):
        super().__init__(**kwargs)
        self.spec = spec

    def construct(self):
        spec = self.spec
        kicker = Text(spec["kicker"], font=FONT, color=AMBER, font_size=30, weight=BOLD)
        title = VGroup(*[Text(line, font=FONT, color=WHITE, font_size=spec.get("title_size", 96), weight=BOLD) for line in spec["title"]])
        title.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        sub = Text(spec["sub"], font=FONT, color=SOFT, font_size=40)
        text = VGroup(kicker, title, sub).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        sub.shift(DOWN * 0.1)
        text.move_to([-7.3 + text.width / 2, 0.25, 0])
        art = spec["art"]()
        left = text.get_right()[0] + 0.7  # the picture fills the space right of the text
        art.scale_to_fit_width(7.3 - left)
        if art.height > 6.4:
            art.scale_to_fit_height(6.4)
        art.move_to([(left + 7.3) / 2, 0.1, 0])
        self.add(text, art)


stem = sys.argv[1]
config.frame_width, config.frame_height = 16, 9
config.pixel_width, config.pixel_height = 1920, 1080
config.background_color = NAVY
config.write_to_movie = False
config.save_last_frame = True
config.disable_caching = True
config.verbosity = "ERROR"
config.media_dir = "/tmp/cover-media"
scene = Cover(COVERS[stem])
scene.render()
target = HERE.parent / "out" / stem / f"{stem}-cover.png"
target.parent.mkdir(parents=True, exist_ok=True)
from PIL import Image  # noqa: E402

Image.fromarray(scene.renderer.get_frame()).convert("RGB").save(target)
print(f"wrote {target}")

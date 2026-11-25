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


def energy_ladder():
    """Chapter 3: the spring's energy well with its evenly spaced rungs, the lowest one above zero."""
    import numpy as np
    w, h = 6.0, 4.2
    top = 4.6
    def pt(x, e):
        return [x / 2.2 * w / 2, e / top * h - h / 2, 0]
    well = VMobject(stroke_color=SKY, stroke_width=7)
    well.set_points_smoothly([pt(x, x * x) for x in np.linspace(-2.15, 2.15, 80)])
    art = VGroup(Line(pt(-2.3, 0), pt(2.3, 0), color=SOFT, stroke_width=3), well)
    for n in range(4):
        e = n + 0.5
        x = np.sqrt(e)
        art.add(Line(pt(-x, e), pt(x, e), color=AMBER, stroke_width=6))
    art.add(Text("evenly spaced rungs", font=FONT, color=AMBER, font_size=30, weight=BOLD).next_to(pt(0, 4.4), UP, buff=0.15),
            Text("never zero", font=FONT, color=MINT, font_size=28, weight=BOLD).move_to([0, -h / 2 - 0.6, 0]),
            Arrow([0, -h / 2 - 0.35, 0], pt(0, 0.5), buff=0.05, color=MINT, stroke_width=4, max_tip_length_to_length_ratio=0.25))
    return art


def light_clock():
    """Chapter 4: a light clock at rest ticks straight up and back; the same clock moving makes the light zigzag."""
    top, bot = 1.6, -1.6
    art = VGroup()
    beam = lambda a, b: Arrow(a, b, buff=0, color=AMBER, stroke_width=6, max_tip_length_to_length_ratio=0.07)
    cx = -3.4
    for y in (top, bot):
        art.add(Line([cx - 0.8, y, 0], [cx + 0.8, y, 0], color=WHITE, stroke_width=8))
    art.add(beam([cx - 0.15, bot + 0.1, 0], [cx - 0.15, top - 0.1, 0]), beam([cx + 0.15, top - 0.1, 0], [cx + 0.15, bot + 0.1, 0]))
    xs = [-0.4, 2.0, 4.4]
    for i, x in enumerate(xs):
        for y in (top, bot):
            art.add(Line([x - 0.8, y, 0], [x + 0.8, y, 0], color=WHITE if i == 1 else SOFT, stroke_width=8,
                         stroke_opacity=1 if i == 1 else 0.4))
    art.add(beam([xs[0], bot + 0.1, 0], [xs[1], top - 0.1, 0]), beam([xs[1], top - 0.1, 0], [xs[2], bot + 0.1, 0]),
            Arrow([1.0, top + 0.6, 0], [3.0, top + 0.6, 0], buff=0, color=SKY, stroke_width=6, max_tip_length_to_length_ratio=0.18))
    art.add(Text("at rest", font=FONT, color=SOFT, font_size=30, weight=BOLD).move_to([cx, top + 0.6, 0]),
            Text("moving", font=FONT, color=SKY, font_size=30, weight=BOLD).move_to([2.0, top + 1.2, 0]),
            Text("longer path, same speed: slower tick", font=FONT, color=MINT, font_size=28, weight=BOLD).move_to([0.5, bot - 0.7, 0]))
    return art


def adding_arrows():
    """Chapter 2a: two amplitude arrows added head to tail; pointing the same way they reinforce, opposite they cancel."""
    art = VGroup()
    arrow = lambda a, b, c: Arrow(a, b, buff=0, color=c, stroke_width=8, max_tip_length_to_length_ratio=0.16)
    o = [-3.2, -0.6, 0]
    a_end = [-0.6, 1.0, 0]
    b_end = [2.6, -0.2, 0]
    art.add(arrow(o, a_end, SKY), arrow(a_end, b_end, AMBER), arrow(o, b_end, MINT))
    art.add(Text("a", font=FONT, color=SKY, font_size=36, weight=BOLD).move_to([-2.2, 0.55, 0]),
            Text("b", font=FONT, color=AMBER, font_size=36, weight=BOLD).move_to([1.2, 0.75, 0]),
            Text("a + b", font=FONT, color=MINT, font_size=36, weight=BOLD).move_to([-0.2, -0.95, 0]))
    y = -2.4
    art.add(arrow([-3.4, y, 0], [-2.2, y, 0], SKY), arrow([-2.2, y, 0], [-1.0, y, 0], AMBER),
            Text("reinforce", font=FONT, color=SOFT, font_size=28).move_to([-2.2, y - 0.55, 0]))
    art.add(arrow([1.0, y + 0.12, 0], [2.4, y + 0.12, 0], SKY), arrow([2.4, y - 0.12, 0], [1.0, y - 0.12, 0], AMBER),
            Text("cancel", font=FONT, color=SOFT, font_size=28).move_to([1.7, y - 0.55, 0]))
    return art


def bracket_to_commutator():
    """Chapter 2b: chapter 1's Poisson bracket of position with momentum becomes a commutator."""
    art = VGroup()
    top = MathTex(r"\{q,\,p\} = 1", color=SOFT).scale(2.2).move_to([0, 2.0, 0])
    down = Arrow([0, 1.2, 0], [0, 0.1, 0], buff=0, color=AMBER, stroke_width=8, max_tip_length_to_length_ratio=0.3)
    mid = MathTex(r"[\hat x,\,\hat p] = i\hbar", color=WHITE).scale(2.8).move_to([0, -0.9, 0])
    art.add(Text("chapter 1: the bracket", font=FONT, color=SOFT, font_size=26).next_to(top, UP, buff=0.3), top, down, mid,
            Text("the commutator", font=FONT, color=AMBER, font_size=30, weight=BOLD).next_to(mid, DOWN, buff=0.4))
    return art


COVERS = {
    "02b-first-quantization": {
        "kicker": "PHYZ  ·  CHAPTER 2B",
        "title": ["First", "Quantization"],
        "sub": "Operators, the commutator\nand the Schrodinger equation",
        "art": bracket_to_commutator,
    },
    "02a-quantum-ideas": {
        "kicker": "PHYZ  ·  CHAPTER 2A",
        "title": ["Quantum", "Ideas"],
        "sub": "Magnets, two slits,\nand amplitudes that add",
        "art": adding_arrows,
    },
    "01-classical-mechanics": {
        "kicker": "PHYZ  ·  CHAPTER 1",
        "title": ["Classical", "Mechanics"],
        "sub": "One motion, described three ways,\nready for quantum theory",
        "art": thrown_paths,
    },
    "03-harmonic-oscillator": {
        "kicker": "PHYZ  ·  CHAPTER 3",
        "title": ["Harmonic", "Oscillator"],
        "sub": "The quantum spring\nand its ladder of energies",
        "art": energy_ladder,
    },
    "04-special-relativity": {
        "kicker": "PHYZ  ·  CHAPTER 4",
        "title": ["Special", "Relativity"],
        "sub": "Light's speed is fixed,\nso time and space give way",
        "art": light_clock,
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

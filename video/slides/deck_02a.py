"""Slides for chapter two, part A, Quantum Ideas.

Every value comes from video/scripts/02a-quantum-ideas.txt or
docs/quantum-ideas.md. The figures follow docs/manim/page_diagrams.py
(SternGerlachSetup, MagnetsInRow, TiltCircle, SingleSlit, TwoSlitCounts,
PhaseAlongScreen, TwoRoutes), with the same geometry. The Stern-Gerlach,
magnets-in-a-row and two-slit drawings are carried over from the old, unsplit chapter 2 deck (deck_02.py, removed; see git history).

Colors: BLUE for states and amplitudes (state lists, the arrows
that draw complex numbers, wave functions) and for the particles that carry
them (atoms, electrons), TEAL for chances, probability densities and counts,
and for checks that pass, ORANGE for the step or quantity under discussion
(the pushes on an atom, the angle between two arrows, the jump of collapse,
light packets) and for the sideways magnet, PURPLE for Planck's constant h,
RED only for a prediction or picture that fails (the smear, a hidden coin,
chances that only add, real amplitudes for a front lean), MUTED and LINE for
apparatus, context and connectors.
"""
import re

from manim import *

from engine import *

STEM = "02a-quantum-ideas"
deck = Deck(f"scripts/{STEM}.txt")
slide = deck.slide


# ------------------------------------------------------------------ small helpers

def P(x, y):
    return np.array([float(x), float(y), 0.0])


def at(mob, x, y):
    return mob.move_to([x, y, 0])


def left_at(mob, x, y):
    """Place a mobject with its left edge at x."""
    return mob.move_to([x + mob.width / 2, y, 0])


def right_at(mob, x, y):
    return mob.move_to([x - mob.width / 2, y, 0])


def lab(text, size=24, color=MUTED, bold=False):
    return T(text, size, color, bold)


def words(text, chars=40, size=26, color=INK, align=LEFT):
    return W(text, chars, size, color, align=align)


def heq(text, size=30, color=INK, font=MONO):
    """Text in which Planck's constant (a standalone h) is PURPLE."""
    t2c = {f"[{m.start()}:{m.end()}]": PURPLE for m in re.finditer(r"\bh\b", text)}
    return Text(text, font=font, color=color, font_size=size, t2c=t2c)


def eq(text, size=28, color=INK):
    return heq(text, size, color)


def pieces(parts, size=26, color=INK, buff=0.14):
    """An equation built from separate pieces, so that one piece can be struck or boxed."""
    return VGroup(*[eq(p, size, color) if isinstance(p, str) else p for p in parts]).arrange(RIGHT, buff=buff)


def hold():
    """A step that adds nothing, so the next reveal waits for its sentence."""
    return [Wait()]


def tick(mob, color=TEAL, buff=0.2):
    return check(color).next_to(mob, RIGHT, buff=buff)


def num_pill(n, color=INK, size=22):
    return pill(str(n), color, size)


def uvec(t):
    return np.array([np.cos(t), np.sin(t), 0.0])


def varrow(a, b, color=BLUE, width=6, tip=0.22):
    return Arrow(a, b, buff=0, color=color, stroke_width=width, tip_length=tip,
                 max_tip_length_to_length_ratio=0.35, max_stroke_width_to_length_ratio=30)


# ------------------------------------------------------------------ shared drawings

def stripe_color(f):
    """Screen shading: dark (INK) where few electrons land, bright TEAL where many do."""
    return interpolate_color(ManimColor(INK), ManimColor(TEAL), float(np.clip(f, 0, 1)))


def phasor(c, ang=0.0, frac=1.0, r=0.45, color=BLUE, ring=True, width=4):
    """A complex number drawn as an arrow in a circle of radius r (length 1)."""
    c = np.array([c[0], c[1], 0.0])
    g = VGroup()
    if ring:
        g.add(Circle(radius=r, color=LINE, stroke_width=2).move_to(c))
    end = c + frac * r * np.array([np.cos(ang), np.sin(ang), 0])
    g.add(Arrow(c, end, buff=0, color=color, stroke_width=width, tip_length=0.13,
                max_tip_length_to_length_ratio=0.45, max_stroke_width_to_length_ratio=30))
    return g


def bar(x, base, frac, hmax=2.6, w=1.0, color=TEAL, label=None, size=24, opacity=0.8):
    """A chance bar rising from y = base, with its value on top."""
    h = max(hmax * frac, 0.02)
    r = Rectangle(width=w, height=h, stroke_width=0, fill_color=color, fill_opacity=opacity).move_to([x, base + h / 2, 0])
    g = VGroup(r)
    if label:
        g.add(T(label, size, color, True).next_to(r, UP, buff=0.1))
    return g


def bars(x, base, fracs, names, labels=None, hmax=1.4, w=0.7, gap=1.0, color=TEAL, size=22):
    """A small chart: one bar per result, names underneath, on a baseline."""
    g = VGroup(Line([x - 0.55, base, 0], [x + gap * (len(fracs) - 1) + 0.55, base, 0], color=LINE, stroke_width=2))
    for i, (f, n) in enumerate(zip(fracs, names)):
        g.add(bar(x + gap * i, base, f, hmax, w, color, labels[i] if labels else None, size))
        g.add(lab(n, 22, INK).move_to([x + gap * i, base - 0.27, 0]))
    return g


def magnet(name, x, y, w=1.9, h=0.85, color=INK, size=24):
    return at(card(name, w, h, color, size), x, y)


def vmag(x, y, w=1.9):
    return magnet("vertical", x, y, w)


def smag(x, y, w=1.9):
    return magnet("sideways", x, y, w, color=ORANGE)


def slot_arrow(a, b, color=INK):
    return Arrow(a, b, buff=0, color=color, stroke_width=4, tip_length=0.17)


def atom(c, d=UP, r=0.4, color=BLUE, width=5):
    """An atom as a small magnet: a circle with an arrow along its tilt."""
    c = P(c[0], c[1])
    d = np.array([d[0], d[1], 0.0], dtype=float)
    d = d / np.linalg.norm(d)
    return VGroup(Circle(radius=r, color=color, stroke_width=3).move_to(c),
                  Arrow(c - d * r * 0.78, c + d * r * 0.86, buff=0, color=color, stroke_width=width,
                        tip_length=min(0.17, r * 0.42), max_tip_length_to_length_ratio=0.5))


def coin(c, letter="", r=0.5, size=26):
    g = VGroup(Circle(radius=r, color=INK, stroke_width=3, fill_color=PALE, fill_opacity=1).move_to(P(c[0], c[1])),
               Circle(radius=r * 0.8, color=LINE, stroke_width=2).move_to(P(c[0], c[1])))
    if letter:
        g.add(T(letter, size, INK, True).move_to(P(c[0], c[1])))
    return g


def hand(c, w=1.6, h=1.25):
    box = RoundedRectangle(width=w, height=h, corner_radius=0.3, stroke_width=0, fill_color=MUTED, fill_opacity=0.92).move_to(P(c[0], c[1]))
    return VGroup(box, T("hand", 22, WHITE, True).move_to(box))


def alist(vals, names=None, size=26, color=BLUE, rowh=0.62, name_size=22, name_color=MUTED):
    """A state's list: values in square brackets, with the results named on the left."""
    cells = [code(v, size, color) if isinstance(v, str) else v for v in vals]
    n = len(cells)
    w = max(c.width for c in cells) + 0.42
    ys = [-(i - (n - 1) / 2) * rowh for i in range(n)]
    for c, y in zip(cells, ys):
        c.move_to([0, y, 0])
    h = rowh * n + 0.06
    lb = VMobject(color=color, stroke_width=3).set_points_as_corners([[-w / 2 + 0.13, h / 2, 0], [-w / 2, h / 2, 0], [-w / 2, -h / 2, 0], [-w / 2 + 0.13, -h / 2, 0]])
    rb = VMobject(color=color, stroke_width=3).set_points_as_corners([[w / 2 - 0.13, h / 2, 0], [w / 2, h / 2, 0], [w / 2, -h / 2, 0], [w / 2 - 0.13, -h / 2, 0]])
    g = VGroup(VGroup(lb, rb), VGroup(*cells))
    if names:
        g.add(VGroup(*[lab(nm, name_size, name_color).move_to([-w / 2 - 0.18, y, 0]).shift(LEFT * lab(nm, name_size).width / 2)
                       for nm, y in zip(names, ys)]))
    return g


def place(mob, x, y):
    """Move a state list so that its brackets (not its names) are centered at (x, y)."""
    br = mob[0]
    mob.shift(P(x, y) - br.get_center())
    return mob


def ph(deg, frac=1.0, r=0.28, ring=True, color=BLUE):
    return phasor([0, 0], np.radians(deg), frac, r=r, ring=ring, color=color, width=4)


def dial(c, tilt_deg, r=0.95, color=BLUE, name=None, arc_color=ORANGE, show_arc=True, size=22):
    """A magnet's tilt: a dashed vertical and an arrow tilted from it, positive to the right."""
    c = np.array([c[0], c[1], 0.0])
    t = np.radians(tilt_deg)
    g = VGroup(Circle(radius=r, color=LINE, stroke_width=2).move_to(c),
               DashedLine(c, c + UP * r, color=MUTED, stroke_width=2),
               Arrow(c, c + r * np.array([np.sin(t), np.cos(t), 0]), buff=0, color=color, stroke_width=5, tip_length=0.18))
    if show_arc and abs(tilt_deg) > 1:
        g.add(Arc(radius=r * 0.45, start_angle=PI / 2, angle=-t, arc_center=c, color=arc_color, stroke_width=4))
    if name:
        g.add(T(name, size, MUTED).next_to(g[0], DOWN, buff=0.15))
    return g


def two_out(x, y, up="", down="", color=INK, dx=1.0, dy=0.55, size=22):
    """Two outlets leaving a magnet's right edge, one rising and one falling."""
    a = Arrow([x, y, 0], [x + dx, y + dy, 0], buff=0, color=color, stroke_width=4, tip_length=0.15)
    b = Arrow([x, y, 0], [x + dx, y - dy, 0], buff=0, color=color, stroke_width=4, tip_length=0.15)
    g = VGroup(a, b)
    if up:
        g.add(lab(up, size, INK).next_to(a.get_end(), RIGHT, buff=0.08))
    if down:
        g.add(lab(down, size, INK).next_to(b.get_end(), RIGHT, buff=0.08))
    return g


R2 = "1/√2"


def schip(name, size=24):
    """A state, such as the up state, as a text chip (atoms keep the arrow icon)."""
    return chip(name, BLUE, size=size)


def underline(mob, color=ORANGE):
    """Mark a single sign by underlining it, so no box clips its neighbours."""
    return Line(mob.get_corner(DL) + DOWN * 0.1 + LEFT * 0.04, mob.get_corner(DR) + DOWN * 0.1 + RIGHT * 0.04, color=color, stroke_width=5)


# ================================================================== opening
deck.part("Chapter two, part A")


@slide("Chapter two, part A.", "Quantum Ideas")
def opening(s):
    c1 = at(card("Chapter 1\nClassical Mechanics", 5.0, 1.6, MUTED, 30), -4.0, 0.3)
    yield [FadeIn(c1)]
    c2 = at(card("Chapter 2a\nQuantum Ideas", 5.0, 1.6, INK, 30), 4.0, 0.3)
    yield [GrowArrow(arrow(c1, c2)), FadeIn(c2)]


# ================================================================== previously
deck.part("Previously")

PS_O = P(-6.3, -2.4)


@slide("Chapter one described a system at one instant", "Describing a system at one instant")
def prev(s):
    ax = VGroup(Arrow(PS_O, PS_O + RIGHT * 4.6, buff=0, color=MUTED, stroke_width=3, tip_length=0.18),
                Arrow(PS_O, PS_O + UP * 4.3, buff=0, color=MUTED, stroke_width=3, tip_length=0.18))
    pt = PS_O + P(2.9, 2.6)
    dot = Dot(pt, radius=0.13, color=BLUE)
    yield [Create(ax), FadeIn(dot, scale=2), FadeIn(lab("one point", 24, BLUE).next_to(dot, UR, buff=0.1))]
    names = VGroup(lab("position", 22).next_to(ax[0].get_end(), DOWN, buff=0.12).shift(LEFT * 0.5),
                   lab("momentum", 22).next_to(ax[1].get_end(), RIGHT, buff=0.15))
    proj = VGroup(DashedLine(pt, [pt[0], PS_O[1], 0], color=BLUE, stroke_width=2),
                  DashedLine(pt, [PS_O[0], pt[1], 0], color=BLUE, stroke_width=2))
    yield [FadeIn(names), Create(proj)]
    lst = place(alist([ph(30, 0.9, 0.36), ph(140, 0.6, 0.36), ph(250, 0.8, 0.36), ph(-20, 0.5, 0.36)], rowh=0.9), 3.6, 0.55)
    yield [GrowArrow(arrow(P(-1.0, 0.55), P(2.6, 0.55))), FadeIn(lst),
           FadeIn(at(words("quantum mechanics: a list of numbers called amplitudes", 26, 24, BLUE, ORIGIN), 3.6, -2.15))]
    yield [FadeIn(at(pill("this chapter: why", INK, 24), 3.6, -3.4))]


# ================================================================== the plan
deck.part("Chapter two, part A")

PLAN = ["an experiment with silver atoms and magnets", "the rules of quantum mechanics, checked against every result",
        "a tilted magnet: why amplitudes are complex", "an electron's position: the two-slit experiment", "its momentum"]
PLAN_Y = [2.1, 1.05, 0.25, -0.85, -1.65]


def plan_row(k, color=INK):
    return left_at(VGroup(num_pill(k + 1), T(PLAN[k], 26, color)).arrange(RIGHT, buff=0.22), -7.0, PLAN_Y[k])


def plan_note(k):
    if k == 0:
        return left_at(lab("a position and a momentum alone can't explain its results", 22, RED), -6.4, PLAN_Y[0] - 0.47)
    return left_at(lab("a spin's up or down says nothing about where an atom is, or how fast it moves", 22, MUTED), -6.4, PLAN_Y[2] - 0.47)


@slide("We'll start with an experiment on silver atoms", "The route through the chapter")
def plan1(s):
    yield [FadeIn(plan_row(0), shift=RIGHT * 0.15)]
    yield [FadeIn(plan_note(0))]
    yield [FadeIn(plan_row(1), shift=RIGHT * 0.15)]


@slide("A tilted magnet then shows why the amplitudes", "The route through the chapter")
def plan2(s):
    s.add(plan_row(0), plan_note(0), plan_row(1))
    yield [FadeIn(plan_row(2), shift=RIGHT * 0.15)]
    yield [FadeIn(plan_note(2))]
    yield [FadeIn(plan_row(3), shift=RIGHT * 0.15)]


@slide("And we end with its momentum.", "The route through the chapter")
def plan3(s):
    s.add(plan_row(0), plan_note(0), plan_row(1), plan_row(2), plan_note(2), plan_row(3))
    yield [FadeIn(plan_row(4), shift=RIGHT * 0.15)]
    a = at(card("this chapter: the ideas", 5.0, 0.85, INK, 26), -3.9, -2.95)
    yield [FadeIn(a)]
    b = at(card("next, First Quantization: the maths", 6.2, 0.85, MUTED, 26), 3.4, -2.95)
    yield [GrowArrow(arrow(a, b)), FadeIn(b)]


# ================================================================== magnets that sort atoms
deck.part("Magnets that sort atoms")


def sg_oven():
    oven = Rectangle(width=1.3, height=1.1, color=INK, fill_color=PALE, fill_opacity=1).move_to([-6.2, 0.3, 0])
    return VGroup(oven, lab("oven", 22).move_to([-6.2, -0.55, 0]))


def sg_names():
    return VGroup(left_at(T("1922: Otto Stern and Walther Gerlach", 24, INK), -7.0, -1.4),
                  left_at(T("heated silver in an oven", 24, BLUE), -7.0, -1.85))


def sg_poles():
    top = Polygon([-3.4, 1.55, 0], [-1.4, 1.55, 0], [-1.4, 0.85, 0], [-2.4, 0.55, 0], [-3.4, 0.85, 0], color=INK, fill_color=PALE, fill_opacity=1)
    bot = Polygon([-3.4, -0.25, 0], [-1.4, -0.25, 0], [-1.4, -0.95, 0], [-3.4, -0.95, 0], color=INK, fill_color=PALE, fill_opacity=1)
    return VGroup(top, bot, lab("magnet", 22).move_to([-2.4, 1.85, 0]))


def sg_beam():
    return VGroup(Line([-5.55, 0.3, 0], [-1.4, 0.3, 0], color=BLUE, stroke_width=4))


def sg_plate():
    return VGroup(Line([0.4, -1.6, 0], [0.4, 2.0, 0], color=MUTED, stroke_width=6), lab("glass plate", 22).move_to([0.4, -1.95, 0]))


def sg_rig():
    return VGroup(sg_oven(), sg_beam(), sg_poles(), sg_plate())


def sg_spin(k):
    if k == 0:
        return VGroup(atom([-6.7, -2.6], UP, 0.3), left_at(T("each silver atom: a tiny magnet", 24, BLUE), -6.2, -2.6))
    return left_at(T("from one of its electrons: we call it spin", 24, BLUE), -6.2, -3.1)


def sg_field():
    return at(T("field stronger near the top pole", 22, ORANGE), -2.4, 2.3)


@slide("Magnets that sort atoms.", "Silver atoms through a magnet")
def sg1(s):
    yield [FadeIn(sg_oven())]
    rng = np.random.default_rng(4)
    dots = VGroup(*[Dot([-5.3 + 0.32 * i, 0.3 + rng.uniform(-0.12, 0.12), 0], radius=0.07, color=BLUE) for i in range(5)])
    yield [FadeIn(sg_names()), LaggedStart(*[FadeIn(d, shift=RIGHT * 0.3) for d in dots], lag_ratio=0.2)]
    yield [FadeOut(dots), Create(sg_beam()), FadeIn(sg_poles()), FadeIn(sg_plate())]


@slide("Each silver atom is a tiny magnet itself.", "Each atom is a tiny magnet")
def sg2(s):
    s.add(sg_rig(), sg_names())
    yield [FadeIn(sg_spin(0))]
    yield [FadeIn(sg_spin(1))]
    yield [FadeIn(sg_field())]
    tip = Dot([-2.4, 0.55, 0], radius=0.09, color=ORANGE)
    yield [FadeIn(tip), Flash(tip, color=ORANGE, line_length=0.25)]


def field_panel(cx, uneven, cy=0.3):
    g = VGroup()
    for k in (-1.5, -0.5, 0.5, 1.5):
        top = cx + k * (0.25 if uneven else 0.55)
        g.add(Line([cx + k * 0.55, cy - 1.5, 0], [top, cy + 1.5, 0], color=LINE, stroke_width=3))
    g.add(lab("uneven field" if uneven else "even field", 24, INK).move_to([cx, cy + 2.0, 0]))
    return g


def field_atom(cx, cy=0.3):
    c = P(cx, cy)
    d = uvec(np.radians(60))
    return Arrow(c - d * 0.6, c + d * 0.6, buff=0, color=BLUE, stroke_width=7, tip_length=0.2), c + d * 0.6, c - d * 0.6


def pulls(top, bot, up_len, down_len):
    return VGroup(Arrow(top, top + UP * up_len, buff=0, color=ORANGE, stroke_width=5, tip_length=0.16),
                  Arrow(bot, bot + DOWN * down_len, buff=0, color=ORANGE, stroke_width=5, tip_length=0.16))


@slide("An even field would only twist each atom.", "An uneven field pushes")
def sg3(s):
    s.add(sg_rig(), sg_field())
    a, top, bot = field_atom(2.4)
    tw = CurvedArrow(P(2.4 + 0.75, 0.3 - 0.35), P(2.4 + 0.35, 0.3 + 0.8), angle=PI / 2.2, color=ORANGE, stroke_width=4, tip_length=0.15)
    yield [FadeIn(field_panel(2.4, False)), GrowArrow(a), FadeIn(pulls(top, bot, 0.6, 0.6)), Create(tw),
           FadeIn(lab("only twists", 22, INK).move_to([2.4, -1.55, 0]))]
    b, top2, bot2 = field_atom(5.6)
    yield [FadeIn(field_panel(5.6, True)), GrowArrow(b), FadeIn(pulls(top2, bot2, 0.95, 0.35)),
           FadeIn(words("one end is pulled harder than the other", 16, 22, INK, ORIGIN).move_to([5.6, -1.7, 0]))]
    push = Arrow(P(6.95, -0.2), P(6.95, 1.2), buff=0, color=ORANGE, stroke_width=8, tip_length=0.25)
    yield [GrowArrow(push), FadeIn(at(T("so the atom is pushed up or down", 24, INK, True), 4.0, -2.75))]


def push_atom(k):
    x = [2.0, 4.4, 6.6][k]
    d = [UP, DOWN, RIGHT][k]
    a = atom([x, 0.7], d, 0.45)
    text = ["straight up: pushed up the most", "straight down: pushed down the most", "sideways: not pushed at all"][k]
    g = VGroup(a, words(text, 14, 22, INK, ORIGIN).move_to([x, -1.0, 0]))
    if k < 2:
        g.add(Arrow(P(x + 0.75, 0.7 - 0.7 * d[1]), P(x + 0.75, 0.7 + 0.75 * d[1]), buff=0, color=ORANGE, stroke_width=6, tip_length=0.2))
    return g


@slide("How far depends on how the atom's own magnet", "The push depends on the tilt")
def sg4(s):
    s.add(sg_rig(), sg_field())
    yield [FadeIn(at(T("how far: set by the atom's own tilt", 26, INK, True), 4.3, 2.2))]
    yield [FadeIn(push_atom(0))]
    yield [FadeIn(push_atom(1))]
    yield [FadeIn(push_atom(2))]


def sg_fan():
    return VGroup(*[Line([-1.4, 0.3, 0], [0.35, y, 0], color=BLUE, stroke_width=2.5).set_opacity(0.7) for y in np.linspace(1.25, -0.65, 6)])


def tilted_atoms():
    rng = np.random.default_rng(7)
    g = VGroup()
    for i, x in enumerate((-5.1, -4.5, -3.9)):
        ang = rng.uniform(0, TAU)
        g.add(atom([x, 0.3 + (0.45 if i % 2 == 0 else -0.45)], uvec(ang), 0.2, width=4))
    return VGroup(g, lab("tilted every which way", 22, BLUE).move_to([-5.3, 1.35, 0]))


def expected_box():
    frame = RoundedRectangle(width=1.7, height=3.4, corner_radius=0.1, color=MUTED, stroke_width=2).move_to([3.3, 0.3, 0])
    smear = Line([3.3, -1.0, 0], [3.3, 1.6, 0], color=MUTED, stroke_width=12).set_opacity(0.6)
    return VGroup(frame, smear, lab("expected", 24, MUTED, True).move_to([3.3, 2.3, 0]),
                  words("a smear, one point for each tilt", 16, 22, MUTED, align=ORIGIN).move_to([3.3, -1.95, 0]))


def seen_box():
    frame = RoundedRectangle(width=1.7, height=3.4, corner_radius=0.1, color=MUTED, stroke_width=2).move_to([6.1, 0.3, 0])
    return VGroup(frame, Dot([6.1, 1.15, 0], radius=0.18, color=BLUE), Dot([6.1, -0.55, 0], radius=0.18, color=BLUE),
                  lab("seen", 24, BLUE, True).move_to([6.1, 2.3, 0]),
                  words("two spots, nothing in between", 16, 22, BLUE, align=ORIGIN).move_to([6.1, -1.95, 0]))


def two_beams():
    return VGroup(Line([-1.4, 0.3, 0], [0.35, 1.15, 0], color=BLUE, stroke_width=4),
                  Line([-1.4, 0.3, 0], [0.35, -0.55, 0], color=BLUE, stroke_width=4))


@slide("The atoms leave the oven tilted every which way.", "Expected versus seen")
def sg5(s):
    s.add(sg_rig())
    yield [FadeIn(tilted_atoms())]
    fan = sg_fan()
    yield [LaggedStart(*[Create(l) for l in fan], lag_ratio=0.1), FadeIn(expected_box())]
    yield [Create(cross(Square(1.0).move_to([3.3, 0.3, 0]), RED, 6))]
    yield [FadeIn(seen_box()), FadeOut(fan), Create(two_beams())]


ROW_Y = [1.75, 0.05, -1.65]
MAG_X = [-5.8, -2.4, 1.0]


def row_parts(r):
    """Magnets, connecting arrows with their 'keep' labels, and the result of row r."""
    y = ROW_Y[r]
    names = [["vertical", "vertical"], ["vertical", "sideways"], ["vertical", "sideways", "vertical"]][r]
    keeps = [["keep up"], ["keep up"], ["keep up", "keep right"]][r]
    result = ["all up again", "half right, half left", "half up, half down"][r]
    mags = [magnet(n, MAG_X[i], y, color=ORANGE if n == "sideways" else INK) for i, n in enumerate(names)]
    links = []
    for i, kp in enumerate(keeps):
        a = slot_arrow([MAG_X[i] + 1.05, y, 0], [MAG_X[i] + 2.35, y, 0])
        links.append(VGroup(a, lab(kp, 22, INK).next_to(a, UP, buff=0.08)))
    last = MAG_X[len(names) - 1]
    out = slot_arrow([last + 1.0, y, 0], [last + 1.7, y, 0])
    res = left_at(T(result, 28, TEAL, True), last + 1.85, y)
    return mags, links, VGroup(out, res)


def row_all(r):
    mags, links, res = row_parts(r)
    return VGroup(*mags, *links, res)


def no_predict():
    mags, links, res = row_parts(1)
    return words("nothing tells you which atom goes which way", 22, 22, ORANGE).next_to(res[1], RIGHT, buff=0.35)


@slide("Later experiments put magnets one after another.", "Magnets in a row")
def row0(s):
    mags, links, res = row_parts(0)
    yield [FadeIn(mags[0])]
    yield [FadeIn(links[0])]
    yield [FadeIn(mags[1], shift=RIGHT * 0.15), GrowArrow(res[0]), FadeIn(res[1])]


@slide("Send them through a sideways magnet instead", "Magnets in a row")
def row1(s):
    s.add(row_all(0))
    mags, links, res = row_parts(1)
    yield [FadeIn(mags[0]), FadeIn(links[0]), FadeIn(mags[1], shift=RIGHT * 0.15), GrowArrow(res[0]), FadeIn(res[1])]
    yield [FadeIn(no_predict())]


@slide("Now keep the ones that went right, and send", "Back to vertical")
def row2(s):
    s.add(row_all(0), row_all(1), no_predict())
    mags, links, res = row_parts(2)
    yield [FadeIn(mags[0]), FadeIn(links[0]), FadeIn(mags[1]), FadeIn(links[1]), FadeIn(mags[2], shift=RIGHT * 0.15)]
    yield [GrowArrow(res[0]), FadeIn(res[1])]
    yield [FadeIn(left_at(lab("keep the ones that went left instead: the same split", 22, INK), -6.85, -2.45))]
    yield [FadeIn(at(pill("idealized, the way textbooks present them", MUTED, 22), 0, -3.35))]


PUZ = ["the plate shows two spots instead of a smear", "an atom that went up goes up again",
       "atoms that all went up split half and half in a sideways magnet", "atoms found right have forgotten that they were up"]
PUZ_Y = [1.9, 0.9, -0.1, -1.6]


def puz_pill(k):
    return at(num_pill(k + 1, INK, 24), -6.5, PUZ_Y[k])


def puz_text(k):
    return left_at(T(PUZ[k], 28, INK), -5.95, PUZ_Y[k])


def puz_note():
    return left_at(lab("no vertical magnet can tell them apart, yet they give different results", 22, MUTED), -5.95, PUZ_Y[2] - 0.55)


@slide("So there are four things to explain.", "Four things to explain")
def puz1(s):
    yield [LaggedStart(*[FadeIn(puz_pill(k)) for k in range(4)], lag_ratio=0.15)]
    yield [FadeIn(puz_text(0), shift=RIGHT * 0.15)]
    yield [FadeIn(puz_text(1), shift=RIGHT * 0.15)]


@slide("Third, atoms that all went up split half and half", "Four things to explain")
def puz2(s):
    s.add(*[puz_pill(k) for k in range(4)], puz_text(0), puz_text(1))
    yield [FadeIn(puz_text(2), shift=RIGHT * 0.15)]
    yield [FadeIn(puz_note())]
    yield [FadeIn(puz_text(3), shift=RIGHT * 0.15)]


# ================================================================== the two rules
deck.part("The two rules")


def rule_cards():
    return (at(card("rule one", 4.2, 1.3, BLUE, 32), -3.4, 1.0), at(card("rule two", 4.2, 1.3, BLUE, 32), 3.4, 1.0))


@slide("The two rules.", "Two rules")
def rules1(s):
    a, b = rule_cards()
    yield [FadeIn(a, shift=UP * 0.15), FadeIn(b, shift=UP * 0.15),
           FadeIn(at(lab("explain all four results", 26, INK), 0, -0.3))]
    yield [FadeIn(at(lab("they sound strange: take them as given for now", 24, MUTED), 0, -1.1))]
    mags = VGroup(vmag(-2.2, -2.5), smag(2.2, -2.5))
    yield [FadeIn(mags), FadeIn(at(lab("then check them against the magnets", 24, INK), 0, -3.4))]


def r1_pill():
    return at(pill("rule one: the state", BLUE, 26), -3.8, 2.2)


def coin_parts():
    c = coin([-5.6, 0.6], "", 0.55)
    h, t = coin([-3.4, 0.6], "H", 0.45), coin([-2.0, 0.6], "T", 0.45)
    return (VGroup(c, lab("a coin", 22).move_to([-5.6, -0.2, 0])),
            VGroup(h, t, lab("heads or tails", 22, INK).move_to([-2.7, -0.2, 0])))


@slide("Rule one is about the state.", "Rule one: the state")
def coin1(s):
    yield [FadeIn(r1_pill())]
    a, b = coin_parts()
    yield [FadeIn(a)]
    yield [FadeIn(b, shift=RIGHT * 0.15)]


@slide("Before you look, it's already one or the other.", "Rule one: the state")
def coin2(s):
    a, b = coin_parts()
    s.add(r1_pill(), a, b)
    hd = hand([-5.6, 0.75])
    yield [FadeIn(hd, shift=DOWN * 0.3), FadeIn(left_at(words("before you look: already one or the other", 24, 24, INK), -6.6, -1.4))]
    yield [FadeIn(left_at(words("even hidden, while you don't know which", 24, 24, MUTED), -6.6, -2.45))]
    m = vmag(1.6, 0.6)
    yield [FadeIn(m), FadeIn(two_out(2.55, 0.6, "up", "down")),
           FadeIn(left_at(words("a spin in a vertical magnet: also only two results", 24, 24, INK), 0.6, -1.4))]
    frame = RoundedRectangle(width=1.4, height=2.4, corner_radius=0.1, color=MUTED, stroke_width=2).move_to([5.6, 0.6, 0])
    yield [FadeIn(frame), FadeIn(Dot([5.6, 1.2, 0], radius=0.16, color=BLUE)), FadeIn(Dot([5.6, 0.0, 0], radius=0.16, color=BLUE)),
           FadeIn(lab("the two spots", 22, BLUE).move_to([5.6, -0.9, 0]))]


def sp_head():
    return at(T("the difference comes before the measurement", 28, INK, True), 0, 2.2)


def sp_coin():
    return VGroup(coin([-6.2, 1.15], "H", 0.32, 22), left_at(lab("coin: already heads or tails", 24, MUTED), -5.6, 1.15))


def sp_spin():
    return VGroup(left_at(VGroup(schip("up"), T("+", 30, INK), schip("down")).arrange(RIGHT, buff=0.18), -6.75, 0.15),
                  left_at(lab("spin: a mix of up and down", 24, INK), -3.9, 0.15))


def sp_list(named=False):
    lst = alist([lab("amplitude", 26, BLUE), lab("amplitude", 26, BLUE)], ["up", "down"] if named else None, rowh=0.62)
    return place(lst, 2.6, -1.8)


@slide("The difference comes before the measurement.", "Superposition")
def sup1(s):
    yield [FadeIn(sp_head()), FadeIn(sp_coin())]
    yield [FadeIn(sp_spin()), FadeIn(left_at(pill("a superposition", BLUE, 24), 0.6, 0.15))]
    lst = sp_list()
    yield [FadeIn(lst), FadeIn(right_at(T("state =", 30, BLUE, True), 0.6, -1.8)),
           FadeIn(left_at(words("a number for each result, called an amplitude", 20, 22, INK), 4.0, -1.8))]
    yield [FadeIn(sp_list(True)[2]), Indicate(lst[1], color=BLUE)]


@slide("A spin in a superposition isn't secretly up", "Not secretly up or down")
def sup2(s):
    hd = hand([-5.2, 0.6], 1.9, 1.5)
    under = atom([-5.2, 0.6], UP, 0.35).set_opacity(0.0)
    q1 = left_at(lab("secretly up?", 26, RED), -3.6, 1.05)
    q2 = left_at(lab("secretly down?", 26, RED), -3.6, 0.15)
    yield [FadeIn(hd), FadeIn(under), FadeIn(lab("a spin in a superposition", 22, BLUE).move_to([-5.2, -0.5, 0])),
           FadeIn(q1), FadeIn(q2), Create(Line(q1.get_left(), q1.get_right(), color=RED, stroke_width=3)),
           Create(Line(q2.get_left(), q2.get_right(), color=RED, stroke_width=3))]
    yield [FadeIn(at(pill("the new idea", BLUE, 26), 3.4, 1.05)),
           FadeIn(VGroup(vmag(2.4, -0.15, 1.7), smag(4.4, -0.15, 1.7))),
           FadeIn(at(lab("the magnets give a way to check it", 22, INK), 3.4, -0.9))]
    yield [FadeIn(at(card("an amplitude is a complex number (why: later)", 9.0, 0.9, BLUE, 26), 0, -2.45))]


AR_O = P(-4.6, -0.7)
AR_R = 2.0
AR_T = np.radians(35)


def big_amp():
    ring = Circle(radius=AR_R, color=LINE, stroke_width=2).move_to(AR_O)
    a = Arrow(AR_O, AR_O + AR_R * 0.85 * uvec(AR_T), buff=0, color=BLUE, stroke_width=7, tip_length=0.25)
    ln = lab("length", 22, BLUE).move_to(AR_O + 0.75 * uvec(AR_T) + 0.42 * uvec(AR_T + PI / 2))
    ref = DashedLine(AR_O, AR_O + RIGHT * AR_R, color=MUTED, stroke_width=2)
    return VGroup(ring, ref, a, ln, Dot(AR_O, radius=0.05, color=INK))


def big_phase():
    return VGroup(Arc(radius=1.3, start_angle=0, angle=AR_T, arc_center=AR_O, color=ORANGE, stroke_width=5),
                  lab("phase", 24, ORANGE, True).move_to(AR_O + P(2.55, 0.3)))


def sum_eq(x0, y, scale=1.0):
    parts = [T("state =", 28, BLUE, True), phasor([0, 0], np.radians(40), 0.8, 0.42), T("×", 28, INK), schip("up"),
             T("+", 32, INK), phasor([0, 0], np.radians(120), 0.6, 0.42), T("×", 28, INK), schip("down")]
    g = VGroup(*parts).arrange(RIGHT, buff=0.22)
    l1 = words("up amplitude × up state", 13, 22, MUTED, ORIGIN).next_to(VGroup(parts[1], parts[3]), DOWN, buff=0.18)
    l2 = words("down amplitude × down state", 15, 22, MUTED, ORIGIN).next_to(VGroup(parts[5], parts[7]), DOWN, buff=0.18)
    full = VGroup(g, l1, l2).scale(scale)
    full.shift(P(x0 - g.get_left()[0], y - g.get_y()))
    return full


@slide("You can picture it as an arrow", "An amplitude as an arrow")
def arrow1(s):
    yield [FadeIn(big_amp()), FadeIn(at(lab("an amplitude: an arrow with a length and a direction", 24, INK), -3.9, 1.9))]
    yield [FadeIn(big_phase()), FadeIn(at(lab("its direction is its phase", 24, ORANGE), -4.6, -3.1))]
    yield [FadeIn(left_at(T("the state, written as a sum:", 26, INK, True), -0.3, 0.9))]
    yield [FadeIn(sum_eq(-0.3, -0.3))]


def state_lists(k):
    x = [-2.8, 4.4][k]
    lst = place(alist(["1", "0"] if k == 0 else ["0", "1"], ["up", "down"]), x, -1.4)
    icon = at(schip("up" if k == 0 else "down", 26), x - 2.5, -1.4)
    eqs = T("=", 30, INK).move_to([x - 1.65, -1.4, 0])
    return icon, VGroup(eqs, lst)


@slide("The up state is the one that's certainly up.", "The up and down states")
def states1(s):
    s.add(sum_eq(-3.6, 1.55))
    icon, lst = state_lists(0)
    yield [FadeIn(icon), FadeIn(at(lab("up state: certainly up", 24, INK), -4.6, -2.6))]
    yield [FadeIn(lst)]
    icon2, lst2 = state_lists(1)
    yield [FadeIn(icon2), FadeIn(lst2), FadeIn(at(lab("down state: the reverse", 24, INK), 2.6, -2.6))]


@slide("That plus sign doesn't add directions in space.", "Not directions in space")
def space1(s):
    se = sum_eq(-3.6, 1.55)
    s.add(se)
    plus = se[0][4]
    yield [Create(underline(plus)),
           FadeIn(at(lab("this plus does not add directions in space", 24, ORANGE), 0, -0.15))]
    o = P(-4.8, -1.8)
    up = Arrow(o, o + UP * 1.2, buff=0, color=MUTED, stroke_width=6, tip_length=0.2)
    dn = Arrow(o, o + DOWN * 1.2, buff=0, color=MUTED, stroke_width=6, tip_length=0.2)
    res = left_at(words("up and down added as directions in space: nothing", 20, 24, RED), -4.0, -1.8)
    yield [GrowArrow(up), GrowArrow(dn), FadeIn(res)]
    lst = place(alist([lab("how much", 24, BLUE), lab("how much", 24, BLUE)], ["up", "down"]), 3.9, -1.8)
    yield [FadeIn(lst), FadeIn(at(lab("two entries in the state's list", 24, BLUE), 3.6, -3.2))]


@slide("The sum only says how much amplitude goes with up", "A state in its own right")
def space2(s):
    lst = place(alist([ph(40, 0.8, 0.32), ph(120, 0.6, 0.32)], ["up", "down"], rowh=0.8), -4.4, 0.6)
    yield [FadeIn(lst), FadeIn(at(words("the sum only says how much amplitude goes with up, and how much with down", 30, 24, INK, ORIGIN), -4.0, -1.3))]
    yield [FadeIn(at(card("a superposition:\na state in its own right", 5.6, 1.4, BLUE, 28), 3.6, 1.0))]
    o = P(2.6, -2.4)
    tilt = Arrow(o, o + 1.4 * uvec(np.radians(60)), buff=0, color=RED, stroke_width=6, tip_length=0.2)
    t = left_at(words("not a spin pointing partly up and partly down", 18, 24, RED), 3.6, -1.7)
    yield [GrowArrow(tilt), FadeIn(t), Create(cross(VGroup(tilt).copy().scale(0.8), RED, 5))]


def r2_cards():
    a = at(card("1. it changes the state", 5.6, 1.1, INK, 28), -3.4, -0.4)
    b = at(card("2. it gives a result,\nwith a chance you can calculate", 6.4, 1.4, INK, 28), 3.4, -0.4)
    return a, b


@slide("Rule two is about measurement.", "Rule two: measurement")
def meas1(s):
    yield [FadeIn(at(pill("rule two: measurement", BLUE, 28), 0, 2.0))]
    yield [FadeIn(at(lab("a measurement does two things", 26, INK), 0, 1.1))]
    a, b = r2_cards()
    yield [FadeIn(a, shift=UP * 0.15), FadeIn(b, shift=UP * 0.15)]
    yield [a[0].animate.set_stroke(ORANGE, width=5), FadeIn(at(lab("first, the change", 26, ORANGE, True), -3.4, -1.6))]


def collapse_row():
    before = place(alist([ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)], ["up", "down"], rowh=0.78), -4.6, 0.6)
    bl = lab("before: a superposition", 22, BLUE).move_to([-5.0, -0.55, 0])
    m = vmag(-1.0, 0.6)
    a1 = slot_arrow([-3.6, 0.6, 0], [-2.05, 0.6, 0])
    after = place(alist(["1", "0"], ["up", "down"], rowh=0.78), 4.4, 0.6)
    a2 = Arrow([0.05, 0.6, 0], [3.1, 0.6, 0], buff=0, color=ORANGE, stroke_width=5, tip_length=0.2)
    al = lab("went up", 22, INK).next_to(a2, UP, buff=0.1)
    afl = words("after: the certain state of the result found", 20, 22, BLUE, ORIGIN).move_to([4.2, -0.75, 0])
    return VGroup(before, bl, a1, m), VGroup(a2, al), VGroup(after, afl)


@slide("Before a vertical magnet, the spin is in a superposition.", "First, the change")
def coll1(s):
    b, jump, after = collapse_row()
    yield [FadeIn(b)]
    yield [GrowArrow(jump[0]), FadeIn(jump[1]), FadeIn(after)]
    yield [FadeIn(at(T("went up: now in the up state, whatever it was before", 26, INK), 0, -2.3))]


@slide("We call this jump collapse.", "Collapse")
def coll2(s):
    b, jump, after = collapse_row()
    s.add(b, jump, after)
    yield [FadeIn(at(T("collapse", 30, ORANGE, True), 1.55, 1.6)), Indicate(jump[0], color=ORANGE)]
    yield [FadeIn(at(lab("the strangest part of the rules; we'll come back to it", 22, MUTED), 0, -1.8))]
    yield [FadeIn(left_at(T("collapse: what the state becomes", 26, INK), -6.6, -2.7))]
    yield [FadeIn(left_at(T("not which result you get", 26, ORANGE), 1.0, -2.7))]


BORN_Y = [0.35, -1.45]


def born_amp(k):
    y = BORN_Y[k]
    frac, ang, name, val = [(0.6, 40, "up", "0.6"), (0.8, 120, "down", "0.8")][k]
    p = phasor([-5.9, y], np.radians(ang), frac, r=0.75, width=6)
    return VGroup(p, left_at(T(f"{name} arrow: length {val}", 26, BLUE), -4.9, y))


def born_rule():
    r = left_at(VGroup(T("chance of a result =", 28, TEAL, True), T("(its amplitude's length)²", 28, TEAL)).arrange(RIGHT, buff=0.2), -6.8, 2.0)
    return r


def born_pill():
    return left_at(pill("the Born rule", TEAL, 24), 4.4, 2.0)


def born_chance(k):
    y = BORN_Y[k]
    return left_at(eq(["0.6² = 0.36", "0.8² = 0.64"][k], 28, TEAL), -0.3, y)


def born_bars(k):
    vals = [(4.4, 0.36, "0.36", "up"), (6.0, 0.64, "0.64", "down")][k]
    x, f, l, n = vals
    return VGroup(bar(x, -2.6, f, hmax=3.2, w=1.0, label=l), lab(n, 22, INK).move_to([x, -2.9, 0]))


def born_base_line():
    return Line([3.7, -2.6, 0], [6.7, -2.6, 0], color=LINE, stroke_width=2)


@slide("For that, the rule gives a chance.", "The Born rule")
def born1(s):
    yield [FadeIn(born_rule()[0])]
    yield [FadeIn(born_rule()[1]), FadeIn(born_pill())]
    yield [FadeIn(born_amp(0)), FadeIn(born_amp(1))]


@slide("Then a vertical magnet finds the spin up", "The Born rule")
def born2(s):
    s.add(born_rule(), born_pill(), born_amp(0), born_amp(1), born_base_line())
    yield [FadeIn(born_chance(0)), GrowFromEdge(born_bars(0)[0][0], DOWN), FadeIn(born_bars(0)[0][1]), FadeIn(born_bars(0)[1])]
    yield [FadeIn(born_chance(1)), GrowFromEdge(born_bars(1)[0][0], DOWN), FadeIn(born_bars(1)[0][1]), FadeIn(born_bars(1)[1])]
    yield [FadeIn(left_at(lab("the chances add to one, so the squared lengths do too", 24, INK), -6.8, -3.4))]


@slide("Here, zero point three six plus zero point six four is one.", "Only the lengths count")
def born3(s):
    s.add(born_rule(), born_pill(), born_base_line(), born_bars(0), born_bars(1), born_chance(0), born_chance(1))
    a0, a1 = born_amp(0), born_amp(1)
    s.add(a0, a1)
    sm = left_at(VGroup(eq("0.36 + 0.64 = 1", 28, TEAL), check()).arrange(RIGHT, buff=0.3), -6.8, -3.0)
    yield [FadeIn(sm)]
    yield [Rotate(a0[0][1], angle=2.2, about_point=P(-5.9, BORN_Y[0])), Rotate(a1[0][1], angle=-1.9, about_point=P(-5.9, BORN_Y[1])),
           FadeIn(at(lab("turn the arrows: the chances stay the same", 24, INK), -1.0, 1.2))]
    yield [FadeIn(at(lab("where the directions matter: later", 22, MUTED), 1.0, -3.0))]


def nh_coin():
    return VGroup(coin([-5.2, 0.4], "", 0.5), hand([-5.2, 0.55], 1.7, 1.3),
                  words("coin under your hand: the chance comes from not knowing", 18, 22, MUTED, ORIGIN).move_to([-5.0, -1.25, 0]))


@slide("The chance isn't there because the state is unknown.", "Nothing hidden")
def hidden1(s):
    yield [FadeIn(at(T("the chance isn't there because the state is unknown", 28, INK, True), 0, 2.15))]
    yield [FadeIn(nh_coin())]
    yield [FadeIn(at(card("standard quantum mechanics:\nthe state is the whole description", 7.4, 1.4, BLUE, 26), 2.8, 0.75))]
    l1 = place(alist([ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)], rowh=0.72), 1.4, -1.55)
    l2 = place(alist([ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)], rowh=0.72), 4.2, -1.55)
    yield [FadeIn(l1), FadeIn(l2), FadeIn(T("=", 34, INK).move_to([2.8, -1.55, 0])),
           FadeIn(at(lab("same amplitudes: exactly the same state, nothing hidden", 22, BLUE), 2.8, -2.85))]


TL_Y = 0.3


def timeline():
    st = place(alist([ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)], rowh=0.72), -6.0, TL_Y)
    ar = Arrow([-5.3, TL_Y, 0], [0.6, TL_Y, 0], buff=0, color=MUTED, stroke_width=4, tip_length=0.18)
    m = vmag(1.75, TL_Y, 2.0)
    out = Arrow([2.8, TL_Y, 0], [3.9, TL_Y, 0], buff=0, color=MUTED, stroke_width=4, tip_length=0.18)
    res = VGroup(Dot([4.4, TL_Y + 0.35, 0], radius=0.13, color=BLUE), Dot([4.4, TL_Y - 0.35, 0], radius=0.13, color=BLUE).set_opacity(0.25),
                 lab("one result", 22, BLUE).move_to([5.45, TL_Y, 0]))
    return VGroup(st, ar, m, out, res)


@slide("The chance only comes in when you measure.", "Where chance comes in")
def chance1(s):
    yield [FadeIn(timeline()), FadeIn(at(T("chance comes in only here", 24, ORANGE, True), 1.75, 1.35))]
    q = at(T("“everything is random”", 30, INK), 0, -1.6)
    yield [FadeIn(q)]
    yield [Create(strike(q)), FadeIn(at(lab("most of it isn't", 26, RED, True), 0, -2.4))]
    yield [FadeIn(at(lab("the state is definite", 24, BLUE, True), -2.4, 0.75))]


@slide("Between measurements, it changes in a fully predictable way", "Where chance comes in")
def chance2(s):
    s.add(timeline(), at(T("chance comes in only here", 24, ORANGE, True), 1.75, 1.35), at(lab("the state is definite", 24, BLUE, True), -2.4, 0.75))
    yield [FadeIn(at(words("between measurements: fully predictable (next chapter: the Schrödinger equation)", 26, 22, INK, ORIGIN), -2.4, -0.75))]
    yield [FadeIn(at(words("the amplitudes fix the chances exactly", 16, 22, TEAL, ORIGIN), 1.75, -0.85))]
    yield [FadeIn(at(words("only which result a single atom gives is chance", 16, 22, ORANGE, ORIGIN), 5.2, -0.95))]


def cert_row(y, vals, fr, names_txt, labels):
    lst = place(alist(vals, ["up", "down"], rowh=0.6), -4.6, y)
    m = vmag(-1.2, y, 1.9)
    a1 = slot_arrow([-3.85, y, 0], [-2.2, y, 0])
    a2 = slot_arrow([-0.2, y, 0], [1.0, y, 0])
    b = bars(1.8, y - 0.7, fr, ["up", "down"], labels, hmax=1.0, w=0.6, gap=1.1)
    return lst, VGroup(a1, m, a2), b


@slide("A result is certain only when the spin is already", "When a result is certain")
def cert1(s):
    lst, mm, b = cert_row(1.2, ["1", "0"], [1.0, 0.0], None, ["1", "0"])
    yield [FadeIn(lst), FadeIn(at(lab("already in the up state", 22, BLUE), -4.9, 0.25)), FadeIn(mm)]
    yield [Indicate(lst[1], color=BLUE), FadeIn(left_at(lab("lengths 1 and 0", 22, BLUE), 4.4, 1.2))]
    yield [FadeIn(b), FadeIn(left_at(eq("1² = 1: certain", 26, TEAL), 4.4, 0.6))]
    lst2, mm2, b2 = cert_row(-1.7, [ph(40, 0.6, 0.24), ph(120, 0.8, 0.24)], [0.36, 0.64], None, ["0.36", "0.64"])
    yield [FadeIn(lst2), FadeIn(mm2), FadeIn(b2), FadeIn(left_at(words("any other state: both results possible", 16, 22, TEAL), 4.4, -1.7))]


def side_out(x=-3.05, y=0.9, named=False):
    return two_out(x, y, "right" if named else "", "left" if named else "")


@slide("Now, other magnets.", "A sideways magnet")
def side1(s):
    m = smag(-4.1, 0.9, 2.1)
    yield [FadeIn(m), FadeIn(side_out())]
    yield [FadeIn(at(lab("its own two certain states", 24, INK), -4.0, -0.3)),
           FadeIn(at(lab("(its two outlets are drawn up and down here)", 22, MUTED), -4.0, -0.9))]
    r = VGroup(at(schip("right", 28), 1.6, 0.9), lab("certain right", 22, INK).move_to([1.6, 0.2, 0]))
    l = VGroup(at(schip("left", 28), 4.4, 0.9), lab("certain left", 22, INK).move_to([4.4, 0.2, 0]))
    yield [FadeIn(side_out(named=True)[2:]), FadeIn(r), FadeIn(l)]
    yield [FadeIn(at(lab("what they're made of: from experiment", 26, INK, True), 0, -2.0))]


def mix_row(k):
    y = [1.6, 0.0][k]
    keep = ["keep right", "keep left"][k]
    m1 = smag(-5.6, y, 1.9)
    a = slot_arrow([-4.55, y, 0], [-3.25, y, 0])
    m2 = vmag(-2.2, y, 1.9)
    out = slot_arrow([-1.15, y, 0], [-0.4, y, 0])
    res = left_at(T("half up, half down", 26, TEAL, True), -0.25, y)
    return VGroup(m1, a, lab(keep, 22, INK).next_to(a, UP, buff=0.08), m2, out, res)


@slide("Atoms found right split half up and half down", "Right and left are equal mixes")
def mix1(s):
    yield [FadeIn(mix_row(0)), FadeIn(mix_row(1))]
    yield [FadeIn(left_at(lab("each: an equal mix of up and down", 26, INK, True), -6.6, -1.2))]
    yield [FadeIn(left_at(words("a chance of 1/2 needs an amplitude of length 1/√2", 30, 26, BLUE), -6.6, -2.2))]
    yield [FadeIn(left_at(VGroup(eq("(1/√2)² = 1/2", 30, TEAL), check()).arrange(RIGHT, buff=0.3), 1.4, -2.2))]


def rl_eq(k, y=None):
    y = [1.5, -0.6][k] if y is None else y
    e = left_at(rl_text(k, 30), -6.6, y)
    lst = place(alist([R2, R2] if k == 0 else [R2, "−" + R2], ["up", "down"], rowh=0.62, size=24), 4.8, y)
    return e, lst


def rl_text(k, size=30):
    """'right = (up + down) / √2' or 'left = (up − down) / √2', with the sign as its own piece."""
    return pieces([["right = (up", "left  = (up"][k], ["+", "−"][k], "down) / √2"], size, BLUE, buff=0.22)


@slide("So the right state is up plus down", "Right and left")
def rl1(s):
    e, lst = rl_eq(0)
    yield [FadeIn(e), FadeIn(lst)]
    e2, lst2 = rl_eq(1)
    yield [FadeIn(e2), FadeIn(lst2)]


def minus_box():
    e, _ = rl_eq(1)
    return underline(e[1])


@slide("Notice that an equal mix of up and down turns out", "Right and left")
def rl2(s):
    for k in (0, 1):
        s.add(*rl_eq(k))
    yield [FadeIn(at(lab("an equal mix of up and down turns out to be a sideways state", 24, INK, True), 0, -1.9))]
    yield [FadeIn(at(lab("that comes from experiment, not from adding directions in space", 24, MUTED), 0, -2.6))]
    yield [Create(minus_box()), FadeIn(at(lab("where the minus sign comes from: later", 22, ORANGE), 0, -3.3))]


def deriv_lines():
    l1 = pieces(["right + left =", "(up", "+ down", ") / √2 + (up", "− down", ") / √2"], 26, buff=0.2)
    left_at(l1, -6.8, 1.9)
    x_eq = l1[0][-1].get_left()[0]  # the '=' of the first line
    l2 = left_at(eq("= 2 up / √2", 26), x_eq, 1.0)
    l3 = left_at(eq("= √2 up", 26), x_eq, 0.1)
    l4 = left_at(eq("divide by √2:  up = (right + left) / √2", 26, BLUE), -6.8, -1.1)
    return l1, l2, l3, l4


@slide("It works the other way round too.", "Up is a mix of right and left")
def back1(s):
    l1, l2, l3, l4 = deriv_lines()
    yield [FadeIn(l1)]
    yield [Create(strike(l1[2])), Create(strike(l1[4])), FadeIn(left_at(lab("the down parts cancel", 24, ORANGE), 3.0, 1.3))]
    yield [FadeIn(l2)]


@slide("That's the up state times the square root of two.", "Up is a mix of right and left")
def back2(s):
    l1, l2, l3, l4 = deriv_lines()
    s.add(l1, strike(l1[2]), strike(l1[4]), left_at(lab("the down parts cancel", 24, ORANGE), 3.0, 1.3), l2)
    yield [FadeIn(l3)]
    yield [FadeIn(l4)]
    lst = place(alist([R2, R2], ["right", "left"], size=24), 4.4, -2.5)
    yield [FadeIn(lst), FadeIn(right_at(lab("up: an equal mix of right and left", 24, BLUE, True), 2.8, -2.5))]


LIST_X = (-4.2, 4.2)


def two_views(stage):
    g = VGroup(magnet("vertical magnet", LIST_X[0], 1.6, 3.0), magnet("sideways magnet", LIST_X[1], 1.6, 3.0, color=ORANGE))
    if stage >= 1:
        vals = (["?", "?"], ["?", "?"]) if stage == 1 else (["1", "0"], [R2, R2])
        g.add(place(alist(vals[0], ["up", "down"], size=26), LIST_X[0], -0.3),
              place(alist(vals[1], ["right", "left"], size=24), LIST_X[1], -0.3))
    return g


def up_icon():
    return VGroup(at(schip("up", 28), 0, -0.3), lab("the up state", 22, BLUE).move_to([0, -1.0, 0]))


@slide("Both parts of rule two work the same way", "One state, two lists")
def views1(s):
    yield [FadeIn(two_views(0)), FadeIn(at(lab("rule two works the same way for any magnet", 24, INK), 0, 0.75))]
    yield [FadeIn(two_views(1)[2:]), FadeIn(at(lab("each magnet: its own list, one amplitude per result", 24, INK), 0, -2.0))]
    yield [FadeIn(up_icon())]


@slide("For a vertical magnet, its list is one for up", "One state, two lists")
def views2(s):
    s.add(two_views(0), up_icon(), at(lab("rule two works the same way for any magnet", 24, INK), 0, 0.75))
    full = two_views(2)
    yield [FadeIn(full[2])]
    yield [FadeIn(full[3])]
    yield [FadeIn(at(lab("nothing about the atom differs between the two lists", 26, INK, True), 0, -2.0))]
    yield [FadeIn(at(lab("one state, seen from two magnets' points of view", 26, BLUE), 0, -2.8))]


MAP_O = P(-4.4, -0.6)
MAP_SPOT = MAP_O + P(1.5, 1.0)


def map_grid(ang, color, dashed=False):
    g = VGroup()
    u, v = uvec(ang), uvec(ang + PI / 2)
    for k in np.arange(-2, 2.01, 0.8):
        for a, b in ((u, v), (v, u)):
            p0, p1 = MAP_O + k * a - 2.1 * b, MAP_O + k * a + 2.1 * b
            ln = DashedLine(p0, p1, color=color, stroke_width=1.5, dash_length=0.08) if dashed else Line(p0, p1, color=color, stroke_width=1.5)
            g.add(ln.set_opacity(0.6))
    g.add(Arrow(MAP_O - 2.2 * u, MAP_O + 2.3 * u, buff=0, color=color, stroke_width=3, tip_length=0.15),
          Arrow(MAP_O - 2.2 * v, MAP_O + 2.3 * v, buff=0, color=color, stroke_width=3, tip_length=0.15))
    return g


def map_proj(ang, color):
    u, v = uvec(ang), uvec(ang + PI / 2)
    d = MAP_SPOT - MAP_O
    return VGroup(DashedLine(MAP_SPOT, MAP_O + np.dot(d, u) * u, color=color, stroke_width=3),
                  DashedLine(MAP_SPOT, MAP_O + np.dot(d, v) * v, color=color, stroke_width=3))


@slide("Think of one spot on a map.", "One spot, two grids")
def map1(s):
    g1 = map_grid(0, MUTED)
    yield [FadeIn(g1), FadeIn(Dot(MAP_SPOT, radius=0.13, color=BLUE)), Create(map_proj(0, MUTED)),
           FadeIn(at(lab("one spot: one set of coordinates", 22, INK), -4.4, -3.15))]
    yield [g1.animate.set_opacity(0.25), FadeIn(map_grid(np.radians(30), ORANGE, dashed=True)), Create(map_proj(np.radians(30), ORANGE)),
           FadeIn(at(lab("turn the grid: different coordinates", 22, ORANGE), -4.4, -3.6))]
    lst = place(alist([R2, R2], ["right", "left"], size=24), 2.0, 1.2)
    b = bars(4.4, 0.6, [0.5, 0.5], ["right", "left"], ["1/2", "1/2"], hmax=1.2, w=0.7, gap=1.3)
    yield [FadeIn(lst), FadeIn(at(lab("sideways magnet: use the sideways list", 22, INK), 3.4, 2.3)),
           GrowArrow(slot_arrow([2.75, 1.2, 0], [3.7, 1.2, 0])), FadeIn(b), FadeIn(at(lab("square the lengths", 22, TEAL), 3.8, -0.3))]
    yield [FadeIn(VGroup(atom([2.6, -1.6], RIGHT, 0.35), lab("or", 22, INK).move_to([3.6, -1.6, 0]), atom([4.6, -1.6], LEFT, 0.35))),
           FadeIn(at(lab("afterwards: collapsed to right or to left", 22, BLUE), 3.6, -2.4))]


def rule_sum_cards():
    return [at(card("an unmeasured state is a superposition,\nwith an amplitude for each result", 11.4, 1.3, BLUE, 28), 0, 1.6),
            at(card("measuring collapses it to the result found", 11.4, 1.0, ORANGE, 28), 0, 0.0),
            at(card("the chance of that result is its amplitude's length squared", 11.4, 1.0, TEAL, 28), 0, -1.5)]


@slide("So an unmeasured state is a superposition", "The two rules, in short")
def rules_sum(s):
    for c in rule_sum_cards():
        yield [FadeIn(c, shift=UP * 0.15)]


# ================================================================== the rules solve the puzzle
deck.part("The rules solve the puzzle")


@slide("The rules solve the puzzle.", "Putting the rules to work")
def solve0(s):
    rows = [VGroup(puz_pill(k), puz_text(k)).set_y([1.9, 0.9, -0.1, -1.1][k]) for k in range(4)]
    yield [LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.15)]
    yield hold()
    yield [Create(SurroundingRectangle(rows[0], color=ORANGE, buff=0.15, corner_radius=0.1))]


def plate_two(x, y=0.4, h=2.6):
    frame = RoundedRectangle(width=1.5, height=h, corner_radius=0.1, color=MUTED, stroke_width=2).move_to([x, y, 0])
    return VGroup(frame, Dot([x, y + 0.6, 0], radius=0.16, color=BLUE), Dot([x, y - 0.6, 0], radius=0.16, color=BLUE))


@slide("The number of spots comes from experiment.", "First, the two spots")
def spots1(s):
    yield [FadeIn(plate_two(-5.4)), FadeIn(left_at(lab("how many spots: from experiment", 24, INK), -4.2, 1.0))]
    yield [FadeIn(left_at(words("so we gave a vertical magnet two results", 34, 24, INK), -4.2, 0.0))]
    frame = RoundedRectangle(width=1.5, height=2.6, corner_radius=0.1, color=MUTED, stroke_width=2).move_to([-5.4, -2.4, 0])
    smear = Line([-5.4, -3.4, 0], [-5.4, -1.4, 0], color=MUTED, stroke_width=12).set_opacity(0.6)
    yield [FadeIn(frame), FadeIn(smear), Create(cross(Square(1.0).move_to([-5.4, -2.4, 0]), RED, 6)),
           FadeIn(left_at(lab("what the rules explain: why there's no smear", 24, INK, True), -4.2, -2.4))]


def oven_states():
    g = VGroup()
    specs = [(40, 0.95, 120, 0.3), (10, 0.6, 200, 0.8), (70, 0.3, 300, 0.95)]
    for i, (a0, f0, a1, f1) in enumerate(specs):
        g.add(place(alist([ph(a0, f0, 0.3), ph(a1, f1, 0.3)], rowh=0.72), -6.2 + 1.35 * i, 0.4))
    return VGroup(g, words("atoms from the oven: all sorts of superpositions", 22, 22, BLUE, ORIGIN).move_to([-4.85, -1.55, 0]))


@slide("Atoms leave the oven in all sorts of superpositions", "First, the two spots")
def spots2(s):
    yield [FadeIn(oven_states())]
    m = vmag(-0.6, 0.4)
    yield [FadeIn(m), GrowArrow(slot_arrow([-2.95, 0.4, 0], [-1.65, 0.4, 0])), FadeIn(two_out(0.4, 0.4, dx=1.6, dy=0.6)),
           FadeIn(at(words("each one measured: only ever one of its results", 18, 22, INK, ORIGIN), -0.9, -1.4))]
    pl = plate_two(3.0, 0.4, 2.2)
    rng = np.random.default_rng(3)
    ys = [0.4 + 0.6 * (1 if rng.uniform() < 0.5 else -1) for _ in range(10)]
    dots = VGroup(*[Dot([3.0 + rng.uniform(-0.3, 0.3), y + rng.uniform(-0.08, 0.08), 0], radius=0.06, color=BLUE) for y in ys])
    yield [FadeIn(pl), LaggedStart(*[FadeIn(d, scale=2) for d in dots], lag_ratio=0.15),
           FadeIn(at(words("each atom lands in one of the two spots", 20, 22, BLUE, ORIGIN), 3.4, -1.4))]


@slide("What the old picture called an atom's tilt", "First, the two spots")
def spots3(s):
    t = atom([-5.8, 1.5], uvec(np.radians(60)), 0.45)
    lst = place(alist([ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)], ["up", "down"], rowh=0.72), -1.6, 1.5)
    yield [FadeIn(t), FadeIn(lab("old picture: a tilt", 22, MUTED).move_to([-5.8, 0.75, 0])),
           GrowArrow(slot_arrow([-5.1, 1.5, 0], [-3.4, 1.5, 0])), FadeIn(lst),
           FadeIn(left_at(lab("becomes its amplitudes", 22, BLUE), -0.6, 1.5))]
    p1, p2 = plate_two(-3.0, -1.4, 2.0), plate_two(3.0, -1.4, 2.0)
    yield [FadeIn(p1), FadeIn(p2), FadeIn(at(lab("amplitudes don't move the spots", 24, INK, True), 0, -0.1))]
    b1 = bars(-1.6, -2.2, [0.36, 0.64], ["up", "down"], ["0.36", "0.64"], hmax=1.0, w=0.55, gap=0.95)
    b2 = bars(4.4, -2.2, [1.0, 0.0], ["up", "down"], ["1", "0"], hmax=1.0, w=0.55, gap=0.95)
    yield [FadeIn(b1), FadeIn(b2), FadeIn(at(lab("they only change the chances", 24, TEAL, True), 0, -3.55))]


@slide("Second, up stays up.", "Second, up stays up")
def upup(s):
    m1 = vmag(-5.8, 0.8)
    a = slot_arrow([-4.75, 0.8, 0], [-3.4, 0.8, 0])
    lst = place(alist(["1", "0"], ["up", "down"]), -2.0, 0.8)
    a2 = slot_arrow([-1.3, 0.8, 0], [0.2, 0.8, 0])
    m2 = vmag(1.3, 0.8)
    yield [FadeIn(m1), GrowArrow(a), FadeIn(lab("went up", 22, INK).next_to(a, UP, buff=0.08))]
    yield [FadeIn(lst), FadeIn(at(lab("collapsed: up amplitude 1", 22, BLUE), -2.3, -0.2))]
    b = bars(3.6, 0.2, [1.0, 0.0], ["up", "down"], ["1", "0"], hmax=1.2, w=0.6, gap=1.1)
    yield [GrowArrow(a2), FadeIn(m2), GrowArrow(slot_arrow([2.35, 0.8, 0], [3.0, 0.8, 0])), FadeIn(b),
           FadeIn(at(VGroup(eq("Born rule: 1² = 1", 28, TEAL), lab("up every time", 24, TEAL, True), check()).arrange(RIGHT, buff=0.3), 0, -2.0))]


@slide("Third, half right and half left.", "Third, half right and half left")
def halves(s):
    yield [FadeIn(VGroup(at(schip("up"), -6.0, 1.6), lab("up state", 22, BLUE).move_to([-6.0, 0.95, 0]))),
           FadeIn(smag(-3.4, 1.6)), FadeIn(slot_arrow([-5.45, 1.6, 0], [-4.45, 1.6, 0]))]
    yield [FadeIn(left_at(words("a sideways magnet measures right or left, so write the state in right and left", 34, 24, INK), -1.9, 1.6))]
    e = left_at(eq("up = (right + left) / √2", 30, BLUE), -6.6, -0.6)
    lst = place(alist([R2, R2], ["right", "left"], size=24), 3.0, -0.6)
    yield [FadeIn(e), FadeIn(lst)]
    b = bars(5.2, -1.2, [0.5, 0.5], ["right", "left"], ["1/2", "1/2"], hmax=1.2, w=0.6, gap=1.1)
    yield [FadeIn(b), FadeIn(left_at(eq("(1/√2)² = 1/2", 28, TEAL), -6.6, -2.4))]


@slide("Notice what happened.", "What the rules added")
def added(s):
    yield [FadeIn(at(T("notice what happened", 28, INK, True), 0, 2.1))]
    a = at(card("put in, from experiment:\natoms found right split evenly\nbetween up and down", 6.2, 2.0, MUTED, 26), -3.6, 0.0)
    yield [FadeIn(a)]
    b = at(card("came out, from the rules:\natoms that went up split evenly\nbetween right and left", 6.2, 2.0, TEAL, 26), 3.6, 0.0)
    yield [GrowArrow(arrow(a, b)), FadeIn(b)]


@slide("And every atom here is in the same state", "Nothing decides")
def nodecide(s):
    ys = np.linspace(1.6, -1.6, 5)
    atoms = VGroup(*[atom([-5.8, y], UP, 0.3) for y in ys])
    tags = VGroup(*[left_at(eq("[1, 0]", 22, BLUE), -5.3, y) for y in ys])
    yield [FadeIn(atoms), FadeIn(tags), FadeIn(at(lab("every atom: the same up state", 22, BLUE), -5.0, -2.4))]
    yield [FadeIn(at(words("standard quantum mechanics: that state is the whole description", 26, 22, INK, ORIGIN), -5.0, -3.3))]
    m = smag(-1.2, 0.0)
    outs = VGroup(*[slot_arrow([-3.9, y, 0], [-2.25, 0.0 + 0.15 * (y / 1.6), 0]) for y in ys])
    picks = VGroup(*[Dot([1.6 + 0.4 * i, 0.9, 0], radius=0.11, color=BLUE) for i in range(3)],
                   *[Dot([1.6 + 0.4 * i, -0.9, 0], radius=0.11, color=BLUE) for i in range(2)])
    res = VGroup(lab("right", 24, INK).move_to([4.2, 0.9, 0]), lab("left", 24, INK).move_to([4.2, -0.9, 0]), two_out(-0.15, 0.0, dx=1.2, dy=0.9))
    yield [FadeIn(m), FadeIn(outs), FadeIn(res), LaggedStart(*[FadeIn(p, scale=2) for p in picks], lag_ratio=0.2),
           FadeIn(at(lab("nothing in any atom decides which way it goes", 24, ORANGE, True), 2.4, 2.1))]


def lost_atoms():
    dirs = [UP, DOWN, uvec(np.radians(150))]
    names = ["started up", "started down", "anything else"]
    g = VGroup()
    for i, (d, n) in enumerate(zip(dirs, names)):
        y = [1.6, 0.2, -1.2][i]
        g.add(VGroup(atom([-6.0, y], d, 0.34), lab(n, 22, MUTED).move_to([-6.0, y - 0.55, 0])))
    return g


@slide("Fourth, the lost up.", "Fourth, the lost up")
def lost1(s):
    yield [FadeIn(lost_atoms()), FadeIn(smag(-3.0, 0.2)), *[FadeIn(slot_arrow([-5.5, y, 0], [-4.05, 0.2 + 0.2 * (y - 0.2) / 1.4, 0])) for y in (1.6, 0.2, -1.2)]]
    yield [GrowArrow(Arrow([-1.95, 0.2, 0], [0.0, 0.2, 0], buff=0, color=ORANGE, stroke_width=5, tip_length=0.2)),
           FadeIn(lab("found right: collapsed", 22, ORANGE).move_to([-0.8, 0.75, 0])),
           FadeIn(VGroup(*[atom([1.0 + 1.0 * i, 0.2], RIGHT, 0.34) for i in range(3)])),
           FadeIn(left_at(eq("right state", 24, BLUE), 3.6, 0.2))]
    yield [FadeIn(at(lab("every atom found right: that same state, whatever it was before", 24, INK), 0.2, -2.3))]
    yield [FadeIn(at(lab("nothing in it records that the atom was once up", 24, ORANGE, True), 0.2, -3.1))]


@slide("That's why the up is lost for good.", "Fourth, the lost up")
def lost2(s):
    yield [FadeIn(at(pill("the up is lost for good", ORANGE, 26), 0, 2.1))]
    r = VGroup(atom([-5.8, 0.6], RIGHT, 0.36), lab("right state", 22, BLUE).move_to([-5.8, -0.05, 0]))
    m = vmag(-2.9, 0.6)
    res = left_at(T("half up, half down", 26, TEAL, True), -0.6, 0.6)
    yield [FadeIn(r), FadeIn(slot_arrow([-5.3, 0.6, 0], [-3.95, 0.6, 0])), FadeIn(m), FadeIn(slot_arrow([-1.85, 0.6, 0], [-0.75, 0.6, 0])), FadeIn(res),
           FadeIn(at(lab("the experiment we used to define the right state", 22, MUTED), -1.8, -0.5))]
    yield [FadeIn(tick(res)), FadeIn(left_at(lab("matches by design", 24, TEAL, True), 3.6, 0.6))]
    yield [FadeIn(at(card("what the rules add: the forgetting,\nbecause the collapse replaced the atom's state", 10.4, 1.4, ORANGE, 28), 0, -2.3))]


HC_X = (-3.6, 3.6)


def hc_heads():
    a = VGroup(atom([HC_X[0] - 1.2, 1.9], RIGHT, 0.34), left_at(lab("atoms found right", 24, BLUE, True), HC_X[0] - 0.7, 1.9))
    bag = VGroup(RoundedRectangle(width=1.0, height=0.8, corner_radius=0.3, color=INK, stroke_width=3).move_to([HC_X[1] - 1.5, 1.9, 0]),
                 coin([HC_X[1] - 1.72, 1.85], "", 0.2), coin([HC_X[1] - 1.28, 1.95], "", 0.2))
    b = VGroup(bag, left_at(words("a bag of coins, half heads, half tails", 20, 24, INK), HC_X[1] - 0.85, 1.9))
    return a, b


@slide("The magnets can also check that a superposition", "Not a hidden coin")
def coin_check1(s):
    a, b = hc_heads()
    yield [FadeIn(a), FadeIn(Line([0, 2.4, 0], [0, -3.4, 0], color=LINE, stroke_width=2))]
    m = vmag(HC_X[0] - 1.6, 0.4)
    bb = bars(HC_X[0] + 1.0, -0.2, [0.5, 0.5], ["up", "down"], ["1/2", "1/2"], hmax=1.1, w=0.6, gap=1.1)
    yield [FadeIn(m), GrowArrow(slot_arrow([HC_X[0] - 0.55, 0.4, 0], [HC_X[0] + 0.2, 0.4, 0])), FadeIn(bb)]
    look = at(card("look", 1.6, 0.85, INK, 24), HC_X[1] - 1.6, 0.4)
    bc = bars(HC_X[1] + 1.0, -0.2, [0.5, 0.5], ["heads", "tails"], ["1/2", "1/2"], hmax=1.1, w=0.6, gap=1.2)
    yield [FadeIn(b), FadeIn(look), GrowArrow(slot_arrow([HC_X[1] - 0.7, 0.4, 0], [HC_X[1] + 0.2, 0.4, 0])), FadeIn(bc),
           FadeIn(at(lab("the same split", 24, INK, True), 0, -2.3))]


def secret_bag(x=HC_X[1] - 0.3):
    bag = RoundedRectangle(width=2.6, height=1.0, corner_radius=0.35, color=INK, stroke_width=3).move_to([x, 1.9, 0])
    ats = VGroup(*[atom([x - 0.9 + 0.6 * i, 1.9], UP if i % 2 == 0 else DOWN, 0.2, width=4) for i in range(4)])
    return VGroup(bag, ats, lab("secretly up or secretly down", 22, INK).move_to([x, 1.1, 0]))


@slide("But send atoms found right through a second sideways magnet.", "Not a hidden coin")
def coin_check2(s):
    a, b = hc_heads()
    s.add(a, Line([0, 2.4, 0], [0, -3.4, 0], color=LINE, stroke_width=2))
    m = smag(HC_X[0] - 1.6, 0.4)
    bb = bars(HC_X[0] + 1.0, -0.2, [1.0, 0.0], ["right", "left"], ["all", ""], hmax=1.1, w=0.6, gap=1.1)
    yield [FadeIn(m), GrowArrow(slot_arrow([HC_X[0] - 0.55, 0.4, 0], [HC_X[0] + 0.2, 0.4, 0]))]
    yield [FadeIn(bb), FadeIn(VGroup(lab("every one goes right again,", 22, TEAL), lab("as experiment confirms", 22, TEAL)).arrange(DOWN, buff=0.08).move_to([HC_X[0], -1.35, 0]))]
    yield [FadeIn(secret_bag()), FadeIn(at(words("a bag of such atoms couldn't do that", 18, 24, RED, ORIGIN), HC_X[1], -0.4))]


BAG_X = 5.0


def bag_row(k):
    y = [1.6, 0.3][k]
    a = atom([-6.3, y], UP if k == 0 else DOWN, 0.3)
    nm = lab(["secretly up", "secretly down"][k], 22, INK).move_to([-6.3, y - 0.52, 0])
    m = smag(-4.2, y, 1.7)
    return VGroup(a, nm, slot_arrow([-5.9, y, 0], [-5.1, y, 0]), m), y


def bag_result(k):
    _, y = bag_row(k)
    return VGroup(slot_arrow([-3.3, y, 0], [-2.7, y, 0]), left_at(T("half right, half left", 24, TEAL, True), -2.6, y))


def down_lines():
    l1 = pieces(["right − left = (", "up", "+ down) / √2 − (", "up", "− down) / √2"], 24, buff=0.18)
    left_at(l1, -6.8, -1.2)
    l2 = left_at(eq("down = (right − left) / √2", 26, BLUE), -6.8, -2.6)
    return l1, l2


def cancel_note():
    return left_at(lab("the up parts cancel", 22, ORANGE), -6.8, -1.75)


@slide("The secretly up ones would split half right", "Not a hidden coin")
def coin_check3(s):
    s.add(secret_bag(BAG_X))
    r0, _ = bag_row(0)
    yield [FadeIn(r0), FadeIn(bag_result(0)), FadeIn(left_at(lab("as up = (right + left) / √2", 22, MUTED), -2.6, 1.05))]
    r1, _ = bag_row(1)
    yield [FadeIn(r1), FadeIn(at(T("?", 36, INK, True), -2.2, 0.3))]
    l1, l2 = down_lines()
    yield [FadeIn(l1), Create(strike(l1[1])), Create(strike(l1[3])), FadeIn(cancel_note())]


@slide("That leaves down as an equal mix of right and left too.", "Not a hidden coin")
def coin_check4(s):
    s.add(secret_bag(BAG_X))
    r0, _ = bag_row(0)
    r1, _ = bag_row(1)
    l1, l2 = down_lines()
    s.add(r0, bag_result(0), left_at(lab("as up = (right + left) / √2", 22, MUTED), -2.6, 1.05), r1,
          l1, strike(l1[1]), strike(l1[3]), cancel_note())
    yield [FadeIn(l2), FadeIn(left_at(lab("down: an equal mix of right and left too", 22, BLUE), -0.4, -2.6))]
    yield [FadeIn(bag_result(1))]


@slide("Either way, half the bag would go left.", "Not a hidden coin")
def coin_check5(s):
    pb = bars(-4.2, -0.5, [0.5, 0.5], ["right", "left"], ["1/2", "1/2"], hmax=1.4, w=0.7, gap=1.3, color=RED)
    mb = bars(2.6, -0.5, [1.0, 0.0], ["right", "left"], ["all", ""], hmax=1.4, w=0.7, gap=1.3)
    yield [FadeIn(pb), FadeIn(at(words("a bag of hidden ups and downs: half go left", 30, 24, RED, ORIGIN), -3.6, 1.9)),
           FadeIn(mb), FadeIn(at(words("atoms found right, sideways again: all go right", 30, 24, TEAL, ORIGIN), 3.2, 1.9))]
    yield [FadeIn(at(T("so atoms found right aren't a mix of up atoms and down atoms", 26, INK, True), 0, -1.5))]
    yield [FadeIn(at(VGroup(T("all in one state:", 28, BLUE, True), schip("right", 28)).arrange(RIGHT, buff=0.3), 0, -2.6))]


@slide("The natural next step is to ask why the rules", "Nobody knows why")
def why1(s):
    yield [FadeIn(at(T("why are the rules like this?", 32, INK, True), 0, 1.6))]
    yield [FadeIn(at(T("nobody knows", 32, ORANGE, True), 0, 0.6))]
    yield [FadeIn(at(lab("why there are amplitudes", 26, INK), -3.4, -0.6)), FadeIn(at(lab("what really happens in a collapse", 26, INK), 3.4, -0.6))]


@slide("Physicists agree on the rules, because every experiment", "Nobody knows why")
def why2(s):
    a = at(card("agree: the rules\nevery experiment so far matches them", 7.0, 1.5, TEAL, 26), -3.6, 1.2)
    b = at(card("disagree: what the rules mean\ndebated since the 1920s", 7.0, 1.5, MUTED, 26), 3.6, 1.2)
    yield [FadeIn(a)]
    yield [FadeIn(b)]
    yield [FadeIn(at(lab("like most physicists day to day:", 26, INK), 0, -1.1))]
    yield [FadeIn(at(pill("use the rules, leave the debate aside", INK, 26), 0, -2.0))]


@slide("So with two facts from experiment, the rules explain", "Two facts in, four results out")
def facts(s):
    r = at(card("the two rules", 3.6, 1.0, BLUE, 28), 0, 0.4)
    outs = VGroup(*[at(num_pill(k + 1, INK, 26), 3.6 + 0.75 * k, 0.4) for k in range(4)])
    yield [FadeIn(r), GrowArrow(arrow(r, outs[0])), FadeIn(outs), FadeIn(at(lab("all four results", 24, INK), 4.7, -0.3))]
    f1 = at(card("how many results\na magnet has", 4.2, 1.2, MUTED, 24), -5.0, 1.3)
    f2 = at(card("what right and left\nare made of", 4.2, 1.2, MUTED, 24), -5.0, -0.5)
    yield [FadeIn(f1), FadeIn(f2), GrowArrow(arrow(f1.get_right(), r.get_left() + UP * 0.2)), GrowArrow(arrow(f2.get_right(), r.get_left() + DOWN * 0.2)),
           FadeIn(at(lab("two facts from experiment", 24, INK), -5.0, -1.6))]


# ================================================================== why amplitudes are complex
deck.part("Why amplitudes are complex")


@slide("Why amplitudes are complex.", "One more experiment")
def cx1(s):
    yield [FadeIn(at(T("rule one: amplitudes are complex numbers", 30, BLUE, True), 0, 1.6))]
    yield [FadeIn(at(lab("but why?", 28, INK), 0, 0.8))]
    yield [FadeIn(at(lab("one more experiment gives the reason", 28, INK), 0, -0.4))]
    yield [FadeIn(at(T("rules with only positive and negative numbers couldn't explain it", 26, RED), 0, -1.6))]


def tilt_row():
    d = dial([-5.6, 0.7], 60, name="first magnet, tilted", r=0.85)
    k = slot_arrow([-4.5, 0.7, 0], [-3.0, 0.7, 0])
    kl = lab("keep up", 22, INK).next_to(k, UP, buff=0.08)
    v = vmag(-1.7, 0.7, 2.0)
    o = slot_arrow([-0.6, 0.7, 0], [0.4, 0.7, 0])
    return d, VGroup(k, kl), v, o


def tilt_bars():
    return bars(1.2, 0.0, [0.75, 0.25], ["up", "down"], None, hmax=1.3, w=0.6, gap=1.1)


@slide("Tilt the first magnet away from vertical", "A tilted first magnet")
def tilt1(s):
    d, k, v, o = tilt_row()
    yield [FadeIn(d), FadeIn(k)]
    yield [FadeIn(v)]
    yield [GrowArrow(o), FadeIn(tilt_bars()), FadeIn(left_at(lab("some up, some down", 24, TEAL), 3.6, 0.6))]


def mini_cone(c, n=8, R=1.3, r=0.42, h=1.5):
    c = P(c[0], c[1])
    top = c + UP * h
    g = VGroup(DashedLine(c, top + UP * 0.5, color=MUTED, stroke_width=2),
               Ellipse(width=2 * R, height=2 * r, color=MUTED, stroke_width=2).move_to(top))
    for k in range(n):
        t = TAU * k / n
        g.add(Arrow(c, top + np.array([R * np.cos(t), r * np.sin(t), 0]), buff=0, color=BLUE, stroke_width=3, tip_length=0.12))
    return g


@slide("How far you tilted the first magnet sets those chances.", "A tilted first magnet")
def tilt2(s):
    d, k, v, o = tilt_row()
    s.add(d, k, v, o, tilt_bars(), left_at(lab("some up, some down", 24, TEAL), 3.6, 0.6))
    yield [Indicate(d[3], color=ORANGE, scale_factor=1.6), FadeIn(at(lab("how far: sets the chances", 22, ORANGE), -5.6, 2.1))]
    lst = place(alist([ph(30, 0.87, 0.3), ph(30, 0.5, 0.3)], ["up", "down"], rowh=0.72), -4.6, -1.9)
    yield [FadeIn(lst), FadeIn(left_at(words("so it sets the lengths of the two amplitudes", 20, 22, BLUE), -3.8, -1.9))]
    yield [FadeIn(mini_cone([3.4, -2.9])), FadeIn(left_at(words("the same amount, in any direction", 14, 22, INK), 4.9, -2.0))]


TC_O = P(-4.6, -2.6)
TC_TOP = P(-4.6, 0.8)
TC_R, TC_r = 2.3, 0.8
LEANS = [(-25, "right"), (-75, "front"), (155, "left")]
TC_ROWS = [0.95, -0.75, -2.45]


def ring_pt(deg):
    return TC_TOP + np.array([TC_R * np.cos(np.radians(deg)), TC_r * np.sin(np.radians(deg)), 0])


def tc_base():
    return VGroup(DashedVMobject(Line(TC_O, TC_TOP + UP * 1.2, color=MUTED, stroke_width=3), num_dashes=18),
                  lab("vertical", 22, MUTED).move_to(TC_TOP + UP * 1.45))


def tc_arrow(k):
    deg, name = LEANS[k]
    q = ring_pt(deg)
    d = (q - TC_TOP) / np.linalg.norm(q - TC_TOP)
    pos = q + np.array([0.6 * d[0], 0.45 * d[1], 0]) if name != "front" else P(-3.82, -0.9)
    t = lab(name, 22 if name == "front" else 24, INK, True).move_to(pos)
    if name == "front":  # it sits between two arrows, so give it a white backing
        t.add_background_rectangle(color=WHITE, opacity=1, buff=0.05)
    return VGroup(Arrow(TC_O, q, buff=0, color=BLUE, stroke_width=6, max_tip_length_to_length_ratio=0.07), t)


def tc_ring():
    g = VGroup(Ellipse(width=2 * TC_R, height=2 * TC_r, color=ORANGE, stroke_width=3).move_to(TC_TOP))
    q = ring_pt(65)
    g.add(lab("back", 22, MUTED).move_to(q + UP * 0.3 + RIGHT * 0.2))
    return g


def tc_vbars(k):
    y = TC_ROWS[k]
    return VGroup(lab(LEANS[k][1], 22, INK).move_to([-0.55, y + 0.4, 0]), bars(0.4, y, [0.75, 0.25], ["up", "down"], None, hmax=0.95, w=0.55, gap=0.95))


def tc_sbars(k):
    y = TC_ROWS[k]
    vals = [[0.93, 0.07], [0.5, 0.5], [0.07, 0.93]][k]
    return bars(3.9, y, vals, ["right", "left"], None, hmax=0.95, w=0.55, gap=1.05)


def tc_heads(k):
    return [at(lab("vertical magnet", 22, INK), 0.9, 2.2), at(lab("sideways magnet", 22, ORANGE), 4.4, 2.2)][k]


@slide("Tilt it to the right, toward the front", "Same tilt, different directions")
def lean1(s):
    yield [FadeIn(tc_base()), *[GrowArrow(tc_arrow(k)[0]) for k in range(3)], *[FadeIn(tc_arrow(k)[1]) for k in range(3)]]
    yield [Create(tc_ring()[0]), FadeIn(tc_ring()[1]), FadeIn(at(lab("all the way round a circle", 22, ORANGE), -4.6, -3.2))]
    yield [FadeIn(tc_heads(0)), *[FadeIn(tc_vbars(k)) for k in range(3)], FadeIn(at(lab("the same chances", 22, TEAL, True), 0.9, -3.45))]


@slide("We'll say the atoms lean the way their first magnet", "A sideways magnet sees the lean",
       "The atoms lean the way their first magnet was tilted.")
def lean2(s):
    arrows = [tc_arrow(k) for k in range(3)]
    s.add(tc_base(), *arrows, tc_ring(), tc_heads(0), *[tc_vbars(k) for k in range(3)],
          at(lab("the same chances", 22, TEAL, True), 0.9, -3.45), at(lab("all the way round a circle", 22, ORANGE), -4.6, -3.2))
    yield [*[Indicate(a[0], color=BLUE, scale_factor=1.05) for a in arrows]]
    yield [FadeIn(tc_heads(1))]
    yield [FadeIn(tc_sbars(0)), FadeIn(tc_sbars(2)), FadeIn(left_at(lab("mostly right", 22, TEAL), 6.1, TC_ROWS[0] + 0.3)),
           FadeIn(left_at(lab("mostly left", 22, TEAL), 6.1, TC_ROWS[2] + 0.3))]
    yield [FadeIn(tc_sbars(1)), FadeIn(left_at(lab("half and half", 22, TEAL), 6.1, TC_ROWS[1] + 0.3)),
           FadeIn(at(lab("different", 22, TEAL, True), 4.4, -3.45))]


def real_line(c, sign, L=0.8, color=BLUE):
    c = P(c[0], c[1])
    return VGroup(Line(c + LEFT * 1.0, c + RIGHT * 1.0, color=LINE, stroke_width=2),
                  Arrow(c, c + RIGHT * L * sign, buff=0, color=color, stroke_width=5, tip_length=0.16))


def real_state(x, y, s_up, s_down, color=BLUE):
    return VGroup(lab("up", 22, MUTED).move_to([x - 1.5, y + 0.35, 0]), real_line([x, y + 0.35], s_up, 0.85, color),
                  lab("down", 22, MUTED).move_to([x - 1.55, y - 0.35, 0]), real_line([x, y - 0.35], s_down, 0.5, color))


@slide("So the state has to record which way round", "Ordinary numbers fall short")
def real1(s):
    yield [FadeIn(at(T("the state must record which way round the atom leans, not just how far", 26, INK, True), 0, 2.1))]
    yield [FadeIn(at(T("ordinary numbers can't do that", 28, RED, True), 0, 1.2))]
    yield [FadeIn(real_state(-3.0, -0.6, 1, 1)), FadeIn(real_state(3.0, -0.6, 1, -1)),
           FadeIn(at(lab("lengths fixed: only the signs are left", 24, INK), 0, -2.0))]


@slide("Flipping both signs together changes no chance", "Ordinary numbers fall short")
def real2(s):
    yield [FadeIn(real_state(-4.4, 1.1, 1, 1)), FadeIn(T("and", 24, MUTED).move_to([-2.4, 1.1, 0])), FadeIn(real_state(0.2, 1.1, -1, -1)),
           FadeIn(left_at(lab("flip both: no chance changes", 22, INK), 1.7, 1.1))]
    yield [FadeIn(at(lab("what counts: is down's sign the same as up's, or opposite?", 24, INK), 0, -0.3))]
    a = real_state(-3.4, -1.7, 1, 1)
    b = real_state(2.6, -1.7, 1, -1)
    yield [FadeIn(a), FadeIn(b), FadeIn(at(lab("two states", 24, INK, True), -0.4, -1.7))]
    yield [FadeIn(at(lab("leaning right", 22, BLUE), -3.4, -2.8)), FadeIn(at(lab("leaning left", 22, BLUE), 2.6, -2.8)),
           FadeIn(at(lab("front? nothing in between", 24, RED, True), 0, -3.5))]


CP_C = P(-3.6, -0.4)
CP_R = 1.6


def cp_frame():
    return VGroup(Circle(radius=CP_R, color=LINE, stroke_width=2).move_to(CP_C),
                  Arrow(CP_C + LEFT * 0.0, CP_C + RIGHT * CP_R * 0.95, buff=0, color=BLUE, stroke_width=6, tip_length=0.2).shift(UP * 2.6),
                  lab("up arrow", 22, BLUE).move_to(CP_C + UP * 2.6 + LEFT * 0.9),
                  lab("down arrow", 22, BLUE).move_to(CP_C + LEFT * 2.5))


def down_arrow(deg, frac=0.6):
    return Arrow(CP_C, CP_C + CP_R * frac * uvec(np.radians(deg)), buff=0, color=BLUE, stroke_width=6, tip_length=0.2)


@slide("A complex amplitude has a phase, so its arrow", "A phase for every lean")
def phase1(s):
    fr = cp_frame()
    da = down_arrow(60)
    yield [FadeIn(fr), GrowArrow(da)]
    yield [Rotate(da, angle=TAU, about_point=CP_C, run_time=1.0),
           FadeIn(left_at(words("the down arrow can point any way round the circle: one direction for every lean", 30, 24, INK), 0.2, 1.0))]


@slide("Careful, though, because these are two different pictures.", "Two different pictures")
def two_pictures(s):
    phi = 50
    yield [FadeIn(at(lab("two different pictures", 28, INK, True), 0, 2.7))]
    # left: the lean, a direction in space, seen from above as a ring of directions
    lc = P(-3.6, -0.2)
    ring = Ellipse(width=3.6, height=3.6, color=LINE, stroke_width=2).move_to(lc)
    lean = Arrow(lc, lc + 1.6 * uvec(np.radians(phi)), buff=0, color=INK, stroke_width=6, tip_length=0.22)
    ticks = VGroup(*[lab(n, 20, MUTED).move_to(lc + 2.15 * uvec(np.radians(a)))
                     for n, a in (("right", 0), ("front", 90), ("left", 180), ("back", 270))])
    yield [FadeIn(ring), FadeIn(ticks), GrowArrow(lean), FadeIn(at(lab("seen from above", 20, MUTED), -6.0, 1.7)),
           FadeIn(at(words("the lean: a direction in space", 30, 24, INK, ORIGIN), -3.6, -2.75))]
    # right: the phase, an arrow in the complex plane
    rc = P(3.4, -0.2)
    circ = Circle(radius=1.6, color=LINE, stroke_width=2).move_to(rc)
    axes = VGroup(DashedLine(rc + LEFT * 1.9, rc + RIGHT * 1.9, color=LINE, stroke_width=2),
                  DashedLine(rc + DOWN * 1.9, rc + UP * 1.9, color=LINE, stroke_width=2))
    ph = Arrow(rc, rc + 1.6 * 0.8 * uvec(np.radians(phi)), buff=0, color=BLUE, stroke_width=6, tip_length=0.22)
    yield [FadeIn(axes), FadeIn(circ), GrowArrow(ph),
           FadeIn(at(words("the phase: an arrow in the complex plane, just a drawing of a number", 30, 24, BLUE, ORIGIN), 3.4, -2.75))]
    a1 = Arc(radius=0.6, start_angle=0, angle=np.radians(phi), arc_center=lc, color=ORANGE, stroke_width=4)
    a2 = Arc(radius=0.6, start_angle=0, angle=np.radians(phi), arc_center=rc, color=ORANGE, stroke_width=4)
    link = Arrow(P(-1.3, 0.9), P(1.1, 0.9), buff=0, color=ORANGE, stroke_width=4, tip_length=0.2)
    yield [Create(a1), Create(a2), GrowArrow(link),
           FadeIn(at(lab("the rule links them: same angle", 24, ORANGE, True), 0, 1.4))]


@slide("Leaning right gives the down arrow the same direction", "A phase for every lean")
def phase1b(s):
    s.add(cp_frame())
    da = down_arrow(60)
    s.add(da)
    yield [Rotate(da, angle=-np.radians(60), about_point=CP_C),
           FadeIn(left_at(words("leaning right: the same direction as the up arrow", 30, 24, BLUE), 0.2, 1.0))]


@slide("Leaning left turns it halfway round.", "A phase for every lean")
def phase2(s):
    s.add(cp_frame(), left_at(words("leaning right: the same direction as the up arrow", 30, 24, MUTED), 0.2, 1.0))
    da = down_arrow(0)
    s.add(da)
    arc = Arc(radius=0.55, start_angle=0, angle=PI, arc_center=CP_C, color=ORANGE, stroke_width=4)
    yield [Rotate(da, angle=PI, about_point=CP_C), Create(arc),
           FadeIn(left_at(words("leaning left: turned halfway round", 30, 24, BLUE), 0.2, -0.4))]
    e1 = left_at(rl_text(1, 28), 0.2, -1.6)
    yield [FadeIn(e1), Create(underline(e1[1])),
           FadeIn(left_at(lab("halfway round: a minus sign", 22, ORANGE), 0.2, -2.25))]
    yield [FadeIn(left_at(rl_text(0, 28), 0.2, -3.0))]


def add_case(x, y, deg, name):
    o = P(x - 1.6, y)
    up = varrow(o, o + RIGHT * 1.6)
    lift = UP * 0.22 if deg == 180 else 0
    dn = varrow(o + RIGHT * 1.6 + lift, o + RIGHT * 1.6 + 0.95 * uvec(np.radians(deg)) + lift)
    tot = varrow(o + DOWN * 0.55, o + DOWN * 0.55 + (RIGHT * 1.6 + 0.95 * uvec(np.radians(deg))), color=INK, width=5)
    return VGroup(up, dn), tot, lab(name, 22, INK).move_to([x, y + 0.65, 0])


@slide("So a sideways magnet's amplitude for right adds", "The phase changes the sideways chances")
def phase3(s):
    yield [FadeIn(at(eq("amplitude for right = (up amplitude + down amplitude) / √2", 24, BLUE), 0, 2.1)),
           FadeIn(at(lab("adds the up and down amplitudes", 22, INK), 0, 1.5))]
    a, ta, la = add_case(-3.4, 0.2, 0, "leaning right: same direction")
    b, tb, lb = add_case(3.0, 0.2, 180, "leaning left: halfway round")
    yield [FadeIn(a), FadeIn(la), GrowArrow(ta), FadeIn(b), FadeIn(lb), GrowArrow(tb),
           FadeIn(at(lab("longer or shorter, depending on the angle between them", 24, INK), 0, -0.95))]
    yield [FadeIn(bars(-3.9, -3.2, [0.93, 0.07], ["right", "left"], None, hmax=1.1, w=0.6, gap=1.1)),
           FadeIn(bars(2.5, -3.2, [0.07, 0.93], ["right", "left"], None, hmax=1.1, w=0.6, gap=1.1)),
           FadeIn(at(lab("so the phase changes the sideways chances", 24, TEAL, True), 0, -1.6))]


@slide("That's why amplitudes are complex.", "Why amplitudes are complex")
def cx_sum(s):
    a = at(card("a vertical magnet misses\nwhich way an atom leans", 6.4, 1.4, MUTED, 28), -3.6, 1.2)
    b = at(card("a sideways magnet\nsees it", 6.4, 1.4, ORANGE, 28), 3.6, 1.2)
    yield [FadeIn(a)]
    yield [FadeIn(b)]
    c = at(card("so the state needs a phase,\nand only complex amplitudes have one", 9.0, 1.5, BLUE, 30), 0, -1.4)
    yield [FadeIn(c), GrowArrow(arrow(a.get_bottom(), c.get_top() + LEFT * 2.0)), GrowArrow(arrow(b.get_bottom(), c.get_top() + RIGHT * 2.0))]


# ================================================================== position: one slit
deck.part("Measuring position with one slit")


@slide("Measuring position with one slit.", "Still owed: position and momentum")
def pos0(s):
    yield hold()
    ax = VGroup(Arrow(P(-6.4, -1.6), P(-3.0, -1.6), buff=0, color=MUTED, stroke_width=3, tip_length=0.16),
                Arrow(P(-6.4, -1.6), P(-6.4, 1.5), buff=0, color=MUTED, stroke_width=3, tip_length=0.16),
                lab("position", 22).move_to([-3.6, -1.95, 0]), lab("momentum", 22).move_to([-6.0, 1.85, 0]),
                Dot(P(-4.6, 0.2), radius=0.12, color=BLUE), lab("chapter 1: a particle", 22, INK).move_to([-4.6, -2.6, 0]))
    yield [FadeIn(ax)]
    sp = VGroup(atom([0.6, 0.4], UP, 0.42), atom([1.8, 0.4], DOWN, 0.42), lab("a spin: neither", 24, INK).move_to([1.2, -0.6, 0]))
    yield [FadeIn(sp), FadeIn(at(lab("we still owe you those two", 24, ORANGE), 1.2, -1.4))]
    yield [FadeIn(at(pill("first: position", BLUE, 28), 5.0, 0.4))]


@slide("Every measurement so far had two possible results.", "From two results to a range")
def pos1(s):
    yield [FadeIn(VGroup(Dot([-4.6, 1.0, 0], radius=0.16, color=BLUE), Dot([-4.6, -0.6, 0], radius=0.16, color=BLUE))),
           FadeIn(at(lab("so far: two possible results", 24, INK), -4.6, -1.5))]
    ln = Line([0.8, 0.2, 0], [6.6, 0.2, 0], color=BLUE, stroke_width=8)
    yield [Create(ln), FadeIn(at(lab("position: anywhere along a line", 24, INK), 3.7, -1.5))]
    yield [GrowArrow(arrow(P(-3.4, 0.2), P(0.4, 0.2), color=ORANGE)),
           FadeIn(at(T("from a few separate results to a continuous range", 26, ORANGE, True), 0, -2.8))]


SS_BX, SS_SX = -4.8, -3.0


def ss_rig(barrier=True):
    g = VGroup(Line([SS_SX, -1.9, 0], [SS_SX, 2.3, 0], color=MUTED, stroke_width=6), lab("screen", 22).move_to([SS_SX, -2.3, 0]))
    if barrier:
        g.add(Dot([-6.6, 0.2, 0], radius=0.1, color=INK), lab("source", 22).move_to([-6.6, -0.35, 0]),
              Line([SS_BX, -1.9, 0], [SS_BX, 0.0, 0], color=INK, stroke_width=6), Line([SS_BX, 0.4, 0], [SS_BX, 2.3, 0], color=INK, stroke_width=6),
              lab("one slit", 22).move_to([SS_BX, -2.3, 0]), DashedLine([-6.5, 0.2, 0], [SS_BX, 0.2, 0], color=MUTED, stroke_width=2))
    return g


def ss_dots(n=45, seed=3):
    rng = np.random.default_rng(seed)
    return VGroup(*[Dot([SS_SX + 0.18, y, 0], radius=0.04, color=BLUE) for y in np.clip(rng.normal(0.2, 0.75, n), -1.8, 2.2)])


@slide("To find where a particle is, let it land on a screen.", "One slit")
def slit1(s):
    yield [FadeIn(ss_rig(False)), FadeIn(left_at(lab("to find where it is: let it land on a screen", 24, INK), -1.6, 1.9))]
    yield [FadeIn(ss_rig()[2:]), FadeIn(left_at(lab("fire electrons one at a time at a narrow slit", 24, INK), -1.6, 1.1))]
    yield [FadeIn(left_at(lab("record where each one lands", 24, INK), -1.6, 0.3))]
    d = ss_dots(3, seed=11)
    yield [LaggedStart(*[FadeIn(x, scale=3) for x in d], lag_ratio=0.4), FadeIn(left_at(lab("each electron: a single dot", 24, BLUE), -1.6, -0.5))]


def ss_axes():
    ax = Axes(x_range=[-3, 3, 1], y_range=[0, 1.2, 1], x_length=7.0, y_length=3.3, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([2.9, -0.35, 0])
    names = VGroup(lab("position on the screen", 22).next_to(ax.x_axis, DOWN, buff=0.2),
                   lab("number of electrons", 22).next_to(ax.y_axis, UP, buff=0.1).shift(RIGHT * 1.1))
    return ax, names


@slide("After many electrons, the dots pile up in a hump", "One slit")
def slit2(s):
    s.add(ss_rig(), ss_dots(3, seed=11))
    ax, names = ss_axes()
    yield [FadeIn(ss_dots()), Create(ax), FadeIn(names), Create(ax.plot(lambda y: np.exp(-y ** 2 / 1.6), x_range=[-3, 3], color=TEAL, stroke_width=5))]
    yield [FadeIn(at(lab("the hump alone doesn't look strange yet", 24, INK), 2.9, -2.95))]
    yield [FadeIn(at(pill("the baseline for the next experiment", MUTED, 24), 2.9, -3.6))]


XS = np.linspace(-5.8, 5.8, 15)


def amp_row_line(y, angs, lens, r=0.4, color=BLUE):
    return VGroup(*[phasor([x, y], a, l, r=r, color=color, ring=False, width=4) if l > 0.08 else Dot([x, y, 0], radius=0.05, color=color)
                    for x, a, l in zip(XS, angs, lens)])


def screen_axis(y):
    ax = Arrow([-6.6, y, 0], [6.8, y, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.18)
    return VGroup(ax, lab("position across the screen", 22).next_to(ax.get_end(), DOWN, buff=0.15).shift(LEFT * 1.6))


@slide("The rules still apply, with many more results.", "One amplitude for every position")
def wf1(s):
    yield [FadeIn(at(T("the rules still apply, with many more results", 26, INK, True), 0, 2.2))]
    lst = place(alist([ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)], ["up", "down"], rowh=0.72), -4.8, 0.9)
    yield [FadeIn(lst), FadeIn(left_at(lab("spin: two results, two amplitudes", 24, BLUE), -3.9, 0.9))]
    yield [FadeIn(screen_axis(-2.3)), FadeIn(at(lab("an electron can land anywhere across the screen", 24, INK), -1.0, -3.0))]
    row = amp_row_line(-0.6, 0.9 * XS, np.exp(-XS ** 2 / 30), r=0.42)
    yield [LaggedStart(*[FadeIn(p) for p in row], lag_ratio=0.05),
           FadeIn(at(lab("one amplitude for every position: infinitely many", 24, BLUE), 0, -1.55))]


WF_AX = dict(x_range=[-3.2, 3.2, 1], y_range=[0, 1.1, 1], x_length=11.0, y_length=2.3, tips=False, axis_config={"color": LINE, "include_ticks": False})


def wf_row():
    return amp_row_line(1.15, 0.9 * XS, np.exp(-XS ** 2 / 12), r=0.45)


@slide("Together they form a complex function of position", "The wave function")
def wf2(s):
    yield [FadeIn(wf_row()), FadeIn(left_at(T("together: the wave function, a complex function of position", 26, BLUE, True), -6.6, 2.2))]
    yield [FadeIn(at(words("infinitely many positions share a total chance of one: any single point gets zero", 46, 24, INK, ORIGIN), 0, -0.4))]
    yield [FadeIn(at(T("so the Born rule gives a chance per metre", 28, TEAL, True), 0, -1.7))]


@slide("That's the squared length of the wave function", "The probability density")
def dens(s):
    s.add(wf_row())
    ax = Axes(**WF_AX).move_to([0.0, -1.5, 0])
    f = lambda x: np.exp(-x ** 2 / 1.3)
    d = ax.plot(f, x_range=[-3.2, 3.2], color=TEAL, stroke_width=5)
    yield [Create(ax), Create(d), FadeIn(left_at(lab("squared length: the probability density", 24, TEAL, True), -6.6, 0.4)),
           FadeIn(right_at(lab("chance per metre", 22, MUTED), -0.15, 0.0)), FadeIn(lab("position", 22).move_to([5.0, -2.95, 0]))]
    area = ax.get_area(d, x_range=[-0.5, 0.9], color=TEAL, opacity=0.45)
    note = left_at(words("chance between two points: the area between them", 24, 22, INK), 3.0, -0.35)
    yield [FadeIn(area), FadeIn(note), GrowArrow(arrow(note.get_left() + LEFT * 0.1, ax.c2p(0.3, 0.55), color=MUTED))]
    full = ax.get_area(d, x_range=[-3.2, 3.2], color=TEAL, opacity=0.15)
    yield [FadeIn(full), FadeIn(lab("total area = 1", 24, TEAL, True).move_to([5.2, -1.8, 0]))]
    yield [FadeIn(at(lab("behind one slit, the density is that hump", 24, INK), -0.5, -3.3))]


# ================================================================== two slits
deck.part("Two slits make stripes")

SRC = np.array([-6.7, 0.2, 0])
SLIT_Y = (0.9, -0.5)          # slit A (upper) and slit B (lower)
BARRIER_X, SCREEN_X = -5.0, -3.2


def two_slit_rig(second=True):
    pieces_ = ((-1.9, -0.65), (-0.35, 0.75), (1.05, 2.3)) if second else ((-1.9, 0.75), (1.05, 2.3))
    bars_ = VGroup(*[Line([BARRIER_X, a, 0], [BARRIER_X, b, 0], color=INK, stroke_width=6) for a, b in pieces_])
    g = VGroup(Dot(SRC, radius=0.1, color=INK), lab("source", 22).move_to(SRC + DOWN * 0.45), bars_,
               lab("A", 24, INK, True).move_to([BARRIER_X - 0.35, SLIT_Y[0], 0]),
               *[DashedLine(SRC, [BARRIER_X, y, 0], color=MUTED, stroke_width=2) for y in (SLIT_Y if second else SLIT_Y[:1])])
    if second:
        g.add(lab("B", 24, INK, True).move_to([BARRIER_X - 0.35, SLIT_Y[1], 0]))
    scr = VGroup(Line([SCREEN_X, -1.9, 0], [SCREEN_X, 2.3, 0], color=MUTED, stroke_width=6), lab("screen", 22).move_to([SCREEN_X, -2.3, 0]))
    return g, scr


def slit_a(y):
    return np.exp(-(y - 0.35) ** 2 / 2.6)


def slit_b(y):
    return np.exp(-(y + 0.35) ** 2 / 2.6)


def both_open(y):
    a, b = slit_a(y), slit_b(y)
    return a + b + 2 * np.sqrt(a * b) * np.cos(4.2 * y)


def screen_dots(n, seed=1):
    """Arrival points on the screen, drawn from the both-open pattern."""
    rng = np.random.default_rng(seed)
    out = []
    while len(out) < n:
        u = rng.uniform(-3, 3)
        if rng.uniform(0, 4.2) < both_open(u):
            out.append(Dot([SCREEN_X + 0.16 + rng.uniform(0, 0.25), 0.2 + 0.6 * u, 0], radius=0.045, color=BLUE))
    return VGroup(*out)


def count_axes():
    ax = Axes(x_range=[-3, 3, 1], y_range=[0, 4.2, 1], x_length=7.0, y_length=3.3, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([2.9, -0.55, 0])
    names = VGroup(lab("position on the screen", 22).next_to(ax.x_axis, DOWN, buff=0.2).align_to(ax.x_axis, RIGHT),
                   lab("electrons counted", 22).next_to(ax.y_axis, UP, buff=0.1).shift(RIGHT * 0.9))
    return ax, names


def curves(ax):
    a = ax.plot(slit_a, x_range=[-3, 3], color=MUTED, stroke_width=3)
    b = ax.plot(slit_b, x_range=[-3, 3], color=MUTED, stroke_width=3)
    sm = DashedVMobject(ax.plot(lambda y: slit_a(y) + slit_b(y), x_range=[-3, 3], color=INK, stroke_width=3), num_dashes=60)
    both = ax.plot(both_open, x_range=[-3, 3], color=TEAL, stroke_width=5)
    return a, b, sm, both


def legend_item(text, color, dashed=False, x=0.0, y=0.0, width=4):
    ln = Line([x, y, 0], [x + 0.5, y, 0], color=color, stroke_width=width)
    if dashed:
        ln = DashedLine([x, y, 0], [x + 0.5, y, 0], color=color, stroke_width=width, dash_length=0.1)
    return VGroup(ln, T(text, 22, color).next_to(ln, RIGHT, buff=0.15))


def legends():
    return (legend_item("only A, or only B, open", MUTED, x=-0.6, y=2.35, width=3),
            legend_item("A + B, if chances added", INK, True, x=-0.6, y=1.85, width=3),
            legend_item("both open, measured", TEAL, x=3.4, y=2.35, width=5))


@slide("Two slits make stripes.", "Open a second slit")
def ts1(s):
    rig1, scr = two_slit_rig(False)
    yield [FadeIn(rig1), FadeIn(scr)]
    rig, _ = two_slit_rig()
    yield [FadeOut(rig1), FadeIn(rig)]
    spot = P(SCREEN_X, 1.4)
    yield [Create(VGroup(*[Line([BARRIER_X, y, 0], spot, color=BLUE, stroke_width=3) for y in SLIT_Y])), FadeIn(Dot(spot, radius=0.09, color=INK)),
           FadeIn(left_at(words("the simplest case where an electron can reach a spot in two ways", 30, 24, INK), -1.6, 1.4))]


def three_runs():
    items = ["only slit A open", "only slit B open", "both open"]
    return VGroup(*[left_at(VGroup(num_pill(k + 1), T(t, 26, INK)).arrange(RIGHT, buff=0.2), -1.4, 0.6 - 0.75 * k) for k, t in enumerate(items)])


@slide("Keep firing them one at a time, so no electron", "Three runs")
def ts2(s):
    rig, scr = two_slit_rig()
    s.add(rig, scr)
    yield [FadeIn(screen_dots(4, seed=3)), FadeIn(left_at(lab("one at a time: no electron ever meets another", 24, INK), -1.6, 2.0))]
    yield [FadeIn(left_at(lab("run it three times, and count where they land", 24, INK), -1.6, 1.3))]
    yield [LaggedStart(*[FadeIn(r, shift=RIGHT * 0.15) for r in three_runs()], lag_ratio=0.3)]


def ts_base(s, stage):
    rig, scr = two_slit_rig()
    ax, names = count_axes()
    a, b, sm, both = curves(ax)
    la, ls, lb = legends()
    s.add(rig, scr, ax, names)
    if stage >= 1:
        s.add(a, b, la)
    if stage >= 2:
        s.add(sm, ls)
    return ax, (a, b, sm, both), (la, ls, lb)


@slide("Each slit on its own gives a hump", "What adding would give")
def ts3(s):
    rig, scr = two_slit_rig()
    s.add(rig, scr)
    ax, names = count_axes()
    a, b, sm, both = curves(ax)
    la, ls, lb = legends()
    yield [Create(ax), FadeIn(names), Create(a), Create(b), FadeIn(la)]
    routes = VGroup(*[Line([BARRIER_X, y, 0], [SCREEN_X, 1.4, 0], color=BLUE, stroke_width=3) for y in SLIT_Y])
    yield [Create(routes), FadeIn(at(lab("suppose each electron went through one slit or the other", 22, INK), -0.5, -3.3))]
    yield [Create(sm), FadeIn(ls), FadeIn(at(lab("then both open would just add the two humps", 22, INK), -0.5, -3.75))]


@slide("Instead the counts form stripes.", "Stripes")
def ts4(s):
    ax, (a, b, sm, both), (la, ls, lb) = ts_base(s, 2)
    yield [FadeIn(lb), FadeIn(screen_dots(160, seed=5)), Create(both)]
    dark = -np.pi / 4.2
    pt = ax.c2p(dark, both_open(dark))
    yield [FadeIn(Dot(pt, radius=0.08, color=INK)), GrowArrow(arrow([pt[0] - 0.9, -2.95, 0], pt + DOWN * 0.05, color=INK)),
           FadeIn(T("fewer with both open than with only one", 22, INK).move_to([2.4, -3.15, 0]))]
    yield [sm.animate.set_color(RED), ls[0].animate.set_color(RED), ls[1].animate.set_color(RED),
           FadeIn(T("adding chances can't do that: chances are never negative", 22, RED).move_to([0.6, -3.65, 0]))]


@slide("And the stripes are the same when you wait", "One electron at a time")
def ts5(s):
    rig, scr = two_slit_rig()
    s.add(rig, scr)
    yield [FadeIn(left_at(words("the same stripes with a wait between one electron and the next", 30, 26, INK), -1.6, 1.6))]
    yield [FadeIn(left_at(words("so they don't come from electrons meeting each other", 30, 26, INK), -1.6, 0.1))]
    d = screen_dots(140, seed=8)
    yield [LaggedStart(*[FadeIn(x, scale=2) for x in d], lag_ratio=0.03),
           FadeIn(left_at(lab("they build up from single electrons, dot by dot", 26, BLUE, True), -1.6, -1.5))]


HB_X = -1.8
HB_G = (P(HB_X, 0.9), P(HB_X, -0.9))
HB_L = 0.8


def circ_int(c1, r1, c2, r2):
    d = np.linalg.norm(c2 - c1)
    a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    h = np.sqrt(max(r1 ** 2 - a ** 2, 0))
    u = (c2 - c1) / d
    v = np.array([u[1], -u[0], 0]) if u[1] < 0 else np.array([-u[1], u[0], 0])
    p = c1 + a * u
    return p + h * np.array([1, 0, 0]) if abs(u[0]) < 1e-9 else p + h * v


def harbour():
    wall = VGroup(Line([HB_X, 2.4, 0], [HB_X, 1.15, 0], color=INK, stroke_width=8), Line([HB_X, 0.65, 0], [HB_X, -0.65, 0], color=INK, stroke_width=8),
                  Line([HB_X, -1.15, 0], [HB_X, -3.0, 0], color=INK, stroke_width=8))
    inc = VGroup(*[Line([x, 2.3, 0], [x, -2.9, 0], color=MUTED, stroke_width=3) for x in np.arange(-6.6, HB_X - 0.2, HB_L)])
    arcs = VGroup()
    for g in HB_G:
        for k in range(1, 6):
            R = k * HB_L
            hi = np.arcsin(np.clip((2.3 - g[1]) / R, -1, 1))
            lo = np.arcsin(np.clip((-2.9 - g[1]) / R, -1, 1))
            arcs.add(Arc(radius=R, start_angle=lo, angle=hi - lo, arc_center=g, color=MUTED, stroke_width=3))
            Rt = (k + 0.5) * HB_L
            hi = np.arcsin(np.clip((2.3 - g[1]) / Rt, -1, 1))
            lo = np.arcsin(np.clip((-2.9 - g[1]) / Rt, -1, 1))
            arcs.add(DashedVMobject(Arc(radius=Rt, start_angle=lo, angle=hi - lo, arc_center=g, color=LINE, stroke_width=2.5), num_dashes=int(14 * Rt)))
    return VGroup(wall, inc, lab("harbour wall: two gaps", 22, INK).move_to([HB_X, -3.3, 0]),
                  left_at(lab("solid: crests, dashed: troughs", 22, MUTED), 3.4, -2.6)), arcs


def hb_points(kind):
    pts = []
    G1, G2 = HB_G
    pairs = [(3, 3), (4, 4), (4, 3), (3, 4), (5, 4), (4, 5)] if kind == "add" else [(3, 3.5), (3.5, 3), (4, 4.5), (4.5, 4)]
    for n1, n2 in pairs:
        p = circ_int(G1, n1 * HB_L, G2, n2 * HB_L)
        if p[0] > HB_X:
            pts.append(p)
    return VGroup(*[Dot(p, radius=0.11, color=TEAL if kind == "add" else INK) for p in pts])


@slide("The pattern looks just like water waves", "Like water waves")
def water(s):
    base, arcs = harbour()
    yield [FadeIn(base), Create(arcs)]
    yield [FadeIn(hb_points("add")), FadeIn(left_at(words("crest meets crest: they add up", 18, 24, TEAL), 3.4, 1.3))]
    yield [FadeIn(hb_points("cancel")), FadeIn(left_at(words("crest meets trough: they cancel", 18, 24, INK), 3.4, 0.0))]


def buildup_panel(x, n, seed):
    frame = Rectangle(width=1.6, height=4.2, color=MUTED, stroke_width=2).move_to([x, 0.1, 0])
    rng = np.random.default_rng(seed)
    pts = []
    while len(pts) < n:
        u = rng.uniform(-3, 3)
        if rng.uniform(0, 4.2) < both_open(u):
            pts.append(Dot([x + rng.uniform(-0.7, 0.7), 0.1 + 0.66 * u, 0], radius=0.03, color=BLUE))
    return VGroup(frame, VGroup(*pts))


@slide("In nineteen eighty-nine, Akira Tonomura's team", "Watching it build up")
def tonomura(s):
    panels = [buildup_panel(-5.6 + 2.2 * k, n, k + 2) for k, n in enumerate((15, 120, 900))]
    yield [LaggedStart(*[FadeIn(p) for p in panels], lag_ratio=0.5),
           FadeIn(left_at(words("1989: Akira Tonomura's team watched the pattern build up one electron at a time", 24, 26, INK), 1.2, 1.0))]
    yield [FadeIn(left_at(words("using a device that acts like two slits", 24, 24, MUTED), 1.2, -0.8))]


def detector():
    box = RoundedRectangle(width=0.8, height=0.6, corner_radius=0.1, stroke_color=ORANGE, stroke_width=3, fill_color=ORANGE, fill_opacity=0.2).move_to([BARRIER_X - 0.75, 1.75, 0])
    return VGroup(box, lab("detector", 22, ORANGE).next_to(box, UP, buff=0.08),
                  DashedLine(box.get_bottom() + RIGHT * 0.1, [BARRIER_X - 0.05, SLIT_Y[0] + 0.05, 0], color=ORANGE, stroke_width=2))


@slide("There's one more observation.", "Watching which slit")
def det1(s):
    ax, (a, b, sm, both), (la, ls, lb) = ts_base(s, 2)
    s.add(both, lb)
    yield hold()
    yield [FadeIn(detector()), FadeIn(at(lab("a detector records which slit each electron takes", 22, ORANGE), 0.4, -3.3))]
    sm2 = ax.plot(lambda y: slit_a(y) + slit_b(y), x_range=[-3, 3], color=TEAL, stroke_width=5)
    yield [Transform(both, sm2), Transform(lb, legend_item("both open, with detector", TEAL, x=3.4, y=2.35, width=5)),
           FadeIn(at(lab("the stripes disappear: the two humps added together", 22, TEAL, True), 0.4, -3.75))]


# ================================================================== two ways, so add
deck.part("Two ways, so add")

MINI_SRC = np.array([-6.9, -0.4, 0])
MINI_BX, MINI_SX = -5.6, -3.9
MINI_SPOT = P(MINI_SX, 0.9)


def mini_rig():
    bars_ = VGroup(*[Line([MINI_BX, a, 0], [MINI_BX, b, 0], color=INK, stroke_width=5) for a, b in ((-2.6, -1.0), (-0.75, -0.05), (0.2, 1.8))])
    feeds = VGroup(*[DashedLine(MINI_SRC, [MINI_BX, sy, 0], color=MUTED, stroke_width=2) for sy in (0.075, -0.875)])
    return VGroup(Dot(MINI_SRC, radius=0.09, color=INK), feeds, bars_, Line([MINI_SX, -2.6, 0], [MINI_SX, 1.8, 0], color=MUTED, stroke_width=5),
                  lab("A", 22, INK, True).move_to([MINI_BX - 0.3, 0.075, 0]), lab("B", 22, INK, True).move_to([MINI_BX - 0.3, -0.875, 0]),
                  lab("screen", 22).move_to([MINI_SX, -2.95, 0]))


def mini_routes(spot=MINI_SPOT):
    return VGroup(Line([MINI_BX, 0.075, 0], spot, color=BLUE, stroke_width=3), Line([MINI_BX, -0.875, 0], spot, color=BLUE, stroke_width=3),
                  Dot(spot, radius=0.08, color=INK))


@slide("Two ways, so add.", "Two ways to each spot")
def tw1(s):
    yield [FadeIn(mini_rig())]
    yield [FadeIn(left_at(T("the two rules already explain the stripes", 28, INK, True), -2.8, 1.9))]
    yield [FadeIn(left_at(lab("both slits open: nothing records which slit the electron takes", 24, INK), -2.8, 1.0))]
    yield [Create(mini_routes()), FadeIn(left_at(lab("so it can reach each spot in two ways", 24, BLUE), -2.8, 0.2))]


def wf_parts():
    a = left_at(T("wave function = part A + part B", 30, BLUE, True), -2.8, 0.0)
    pa = left_at(lab("part A: the wave function with only slit A open", 24, BLUE), -2.8, -0.9)
    pb = left_at(lab("part B: the one with only slit B open", 24, BLUE), -2.8, -1.6)
    return a, pa, pb


def sup_lines():
    return (left_at(T("its state: a mix of through A and through B", 26, INK), -2.8, 1.9),
            left_at(lab("a superposition, just as right was a mix of up and down", 24, MUTED), -2.8, 1.2))


@slide("Its state is a mix of through A and through B.", "A superposition of two routes")
def tw2(s):
    s.add(mini_rig(), mini_routes())
    l1, l2 = sup_lines()
    yield [FadeIn(l1)]
    yield [FadeIn(l2)]
    a, pa, pb = wf_parts()
    yield [FadeIn(a)]
    yield [FadeIn(pa)]


@slide("The other is the one with only slit B open.", "A superposition of two routes")
def tw3(s):
    s.add(mini_rig(), mini_routes(), *sup_lines())
    a, pa, pb = wf_parts()
    s.add(a, pa)
    yield [FadeIn(pb)]
    yield [FadeIn(left_at(lab("the sum is scaled so the total chance stays one", 24, MUTED), -2.8, -2.4))]
    yield [FadeIn(left_at(VGroup(T("not a new rule: rule one again", 26, TEAL, True), check()).arrange(RIGHT, buff=0.3), -2.8, -3.3))]


TO = P(-7.0, -2.5)
TA, TB = 3.6, 2.8
DA, DB = np.radians(10), np.radians(70)
TJ = TO + TA * uvec(DA)
TE = TJ + TB * uvec(DB)
TB0 = TO + TB * uvec(DB)


def tri_a():
    return VGroup(varrow(TO, TJ), lab("a", 26, BLUE, True).move_to(TO + 0.5 * (TJ - TO) + DOWN * 0.35))


def tri_b(head=False):
    o = TJ if head else TO
    e = TE if head else TB0
    off = RIGHT * 0.32 if head else LEFT * 0.32
    return VGroup(varrow(o, e), lab("b", 26, BLUE, True).move_to(o + 0.5 * (e - o) + off))


def alpha_tail():
    return VGroup(Arc(radius=0.8, start_angle=DA, angle=DB - DA, arc_center=TO, color=ORANGE, stroke_width=4),
                  T("α", 26, ORANGE, True).move_to(TO + 1.15 * uvec((DA + DB) / 2)))


def alpha_head():
    return VGroup(DashedLine(TJ, TJ + 1.3 * uvec(DA), color=MUTED, stroke_width=2),
                  Arc(radius=0.6, start_angle=DA, angle=DB - DA, arc_center=TJ, color=ORANGE, stroke_width=4),
                  T("α", 26, ORANGE, True).move_to(TJ + 0.95 * uvec((DA + DB) / 2)))


def tri_sum():
    return VGroup(varrow(TO, TE, INK, 5), lab("a + b", 24, INK, True).move_to(TO + 0.45 * (TE - TO) + UP * 0.35 + LEFT * 0.45))


def tri_corner():
    mid = (DB + PI + DA) / 2
    return VGroup(Arc(radius=0.45, start_angle=DB, angle=PI + DA - DB, arc_center=TJ, color=INK, stroke_width=5),
                  T("180° − α", 22, INK, True).move_to(TJ + 1.02 * uvec(mid)))


EX = -1.4  # left edge of the equation column


def ceq(k):
    lines = ["",
             "|a + b|² = |a|² + |b|² + one more term",
             "one more term = 2 |a| |b| cos α"]
    cols = [TEAL, INK, ORANGE]
    return left_at(eq(lines[k], 26, cols[k]), EX, [2.1, 1.2, 0.4][k])


@slide("The density is the squared length of this sum.", "Adding two arrows")
def cos1(s):
    yield [FadeIn(left_at(lab("density = squared length of the sum", 22, TEAL), EX, 2.1))]
    yield [GrowArrow(tri_a()[0]), FadeIn(tri_a()[1]), GrowArrow(tri_b()[0]), FadeIn(tri_b()[1]),
           FadeIn(left_at(words("a: part A's arrow, b: part B's arrow, at one spot", 26, 22, BLUE), -6.9, 1.6)),
           FadeIn(left_at(eq("= |a + b|²", 26, TEAL), 3.9, 2.1))]
    yield [FadeIn(ceq(1))]
    yield [FadeIn(ceq(2)), Create(alpha_tail()[0]), FadeIn(alpha_tail()[1]),
           FadeIn(left_at(lab("α: the angle between the arrows", 22, ORANGE), EX, -0.3))]


def full_eq(y=2.1, size=26):
    return left_at(pieces(["|a + b|² =", "|a|² + |b|²", "+ 2|a||b| cos α"], size, buff=0.25), EX, y)


def school_eq():
    return left_at(pieces(["|a+b|² = |a|² + |b|²", "−", "2|a||b| cos(corner)"], 24, buff=0.25), EX, 0.55)


@slide("It's the cosine rule from school", "The cosine rule from school")
def cos2(s):
    fe = full_eq()
    s.add(fe, tri_a())
    b0 = tri_b()
    al = alpha_tail()
    s.add(b0, al)
    yield [Transform(b0, tri_b(True)), FadeOut(al), FadeIn(alpha_head()), GrowArrow(tri_sum()[0]), FadeIn(tri_sum()[1]),
           FadeIn(left_at(lab("the cosine rule from school, for the triangle:", 22, INK), EX, 1.2)), FadeIn(school_eq())]
    sc = school_eq()
    yield [Create(underline(sc[1])), Create(underline(fe[2][0])),
           FadeIn(left_at(lab("its minus sign turns into a plus here", 22, ORANGE), EX, -0.15))]
    yield [Create(tri_corner()[0]), FadeIn(tri_corner()[1]), FadeIn(left_at(eq("corner = 180° − α", 26, INK), EX, -0.95))]
    yield [FadeIn(left_at(eq("cos(180° − α) = − cos α", 26, INK), EX, -1.75)),
           FadeIn(left_at(VGroup(eq("so − 2|a||b| cos(corner) = + 2|a||b| cos α", 22, TEAL), check()).arrange(RIGHT, buff=0.25), EX, -2.6))]


def case_arrows(x, y, b_len, back):
    o = P(x - 1.4, y)
    a = varrow(o, o + RIGHT * 1.6)
    e = o + RIGHT * 1.6 + (LEFT if back else RIGHT) * b_len
    b = varrow(o + RIGHT * 1.6 + UP * 0.25 * back, e + UP * 0.25 * back)
    tot = o + DOWN * 0.6
    tend = e + DOWN * 0.6
    sm = varrow(tot, tend, INK, 5) if np.linalg.norm(tend - tot) > 0.2 else VGroup(Dot(tot, radius=0.09, color=INK), lab("0", 24, INK, True).next_to(tot, RIGHT, buff=0.1))
    return VGroup(a, b), sm


@slide("The first two terms are the two humps", "Reinforce or cancel")
def intf1(s):
    fe = full_eq()
    s.add(fe)
    b1 = Brace(fe[1], DOWN, color=MUTED)
    b2 = Brace(fe[2], DOWN, color=ORANGE)
    yield [FadeIn(b1), FadeIn(lab("the two humps", 22, MUTED).next_to(b1, DOWN, buff=0.08)), FadeIn(b2), FadeIn(lab("extra", 22, ORANGE).next_to(b2, DOWN, buff=0.08))]
    ar, sm = case_arrows(-3.6, -0.6, 1.2, False)
    yield [FadeIn(ar), GrowArrow(sm), FadeIn(at(lab("same way: cos α = 1", 24, INK, True), -3.6, 0.3))]
    yield [FadeIn(at(words("the spot gets more than the two humps together", 22, 24, TEAL, ORIGIN), -3.6, -2.2))]


@slide("Where they point opposite ways, the cosine is minus one.", "Reinforce or cancel")
def intf2(s):
    fe = full_eq()
    b1 = Brace(fe[1], DOWN, color=MUTED)
    b2 = Brace(fe[2], DOWN, color=ORANGE)
    ar, sm = case_arrows(-3.6, -0.6, 1.2, False)
    s.add(fe, b1, lab("the two humps", 22, MUTED).next_to(b1, DOWN, buff=0.08), b2, lab("extra", 22, ORANGE).next_to(b2, DOWN, buff=0.08),
          ar, sm, at(lab("same way: cos α = 1", 24, INK, True), -3.6, 0.3), at(words("the spot gets more than the two humps together", 22, 24, TEAL, ORIGIN), -3.6, -2.2))
    ar2, sm2 = case_arrows(3.2, -0.6, 1.0, True)
    yield [FadeIn(ar2), FadeIn(sm2), FadeIn(at(lab("opposite ways: cos α = −1", 24, INK, True), 3.2, 0.3))]
    ar3, sm3 = case_arrows(3.2, -0.6, 1.6, True)
    yield [Transform(ar2, ar3), Transform(sm2, sm3), FadeIn(at(words("fewer, and none at all if the arrows are equally long", 24, 24, TEAL, ORIGIN), 3.2, -2.2))]
    yield [FadeIn(at(pill("interference: add the amplitudes before squaring", BLUE, 26), 0, -3.4))]


@slide("We've seen a phase change a chance before.", "A phase changes a chance")
def seen_before(s):
    yield [FadeIn(at(T("a phase changing a chance: we've seen it before", 28, INK, True), 0, 2.1))]
    l = VGroup(atom([-5.4, 0.4], uvec(np.radians(30)), 0.4), lab("lean right", 22, INK).move_to([-5.4, -0.3, 0]),
               atom([-3.6, 0.4], uvec(np.radians(150)), 0.4), lab("lean left", 22, INK).move_to([-3.6, -0.3, 0]),
               bars(-6.0, -2.4, [0.93, 0.07], ["right", "left"], None, hmax=1.0, w=0.45, gap=0.8),
               bars(-4.2, -2.4, [0.07, 0.93], ["right", "left"], None, hmax=1.0, w=0.45, gap=0.8))
    yield [FadeIn(l), FadeIn(at(lab("the lean changed the sideways split", 22, INK), -4.5, 1.3))]
    o = P(2.0, -0.4)
    pr = VGroup(varrow(o, o + 1.6 * uvec(0)), varrow(o, o + 1.4 * uvec(np.radians(110))),
                Arc(radius=0.55, start_angle=0, angle=np.radians(110), arc_center=o, color=ORANGE, stroke_width=4),
                T("α", 24, ORANGE, True).move_to(o + 0.85 * uvec(np.radians(55))))
    yield [FadeIn(pr), FadeIn(at(words("here: the angle between the two arrows at each spot decides", 22, 22, ORANGE, ORIGIN), 3.0, -1.9))]


@slide("The detector fits too.", "The detector fits too")
def det2(s):
    rig, scr = two_slit_rig()
    yield [FadeIn(rig), FadeIn(scr), FadeIn(detector())]
    yield [FadeIn(left_at(words("recording which slit is a measurement, even if nobody ever reads the detector", 30, 24, INK), -1.6, 1.4))]
    route = VGroup(Line([BARRIER_X, SLIT_Y[0], 0], [SCREEN_X, 0.4, 0], color=BLUE, stroke_width=4))
    gone = DashedLine([BARRIER_X, SLIT_Y[1], 0], [SCREEN_X, 0.4, 0], color=LINE, stroke_width=2)
    yield [Create(route), FadeIn(gone), FadeIn(left_at(words("rule two collapses the electron onto one route", 30, 24, ORANGE), -1.6, -0.3))]


@slide("Its wave function is then one part or the other", "No sum, no extra term")
def det3(s):
    yield [FadeIn(left_at(T("wave function: part A or part B, never their sum", 28, BLUE, True), -6.8, 2.1))]
    fe = full_eq(1.2)
    left_at(fe, -6.8, 1.2)
    yield [FadeIn(fe), Create(strike(fe[2])), FadeIn(left_at(lab("no extra term", 24, ORANGE), 2.4, 1.2))]
    ax = Axes(x_range=[-3, 3, 1], y_range=[0, 2.2, 1], x_length=7.0, y_length=2.4, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([-2.4, -1.3, 0])
    axn = VGroup(lab("position on the screen", 22).next_to(ax.x_axis, DOWN, buff=0.15).align_to(ax.x_axis, RIGHT),
                 lab("electrons counted", 22).next_to(ax.y_axis, UP, buff=0.08).shift(RIGHT * 0.9))
    yield [Create(ax), FadeIn(axn), Create(ax.plot(slit_a, x_range=[-3, 3], color=MUTED, stroke_width=3)), Create(ax.plot(slit_b, x_range=[-3, 3], color=MUTED, stroke_width=3)),
           Create(ax.plot(lambda y: slit_a(y) + slit_b(y), x_range=[-3, 3], color=TEAL, stroke_width=5)),
           FadeIn(left_at(words("about half through each: the counts add the two humps", 18, 24, TEAL), 1.6, -0.9))]
    yield [FadeIn(at(lab("the same collapse that made the atoms forget they were up", 24, INK), 0, -3.4))]


@slide("That leaves one question.", "One question left")
def oneq(s):
    s.add(mini_rig())
    yield [FadeIn(at(T("one question left", 28, INK, True), 1.6, 2.1))]
    g = VGroup()
    for k, (y, ang) in enumerate(((1.4, 0), (0.4, 70), (-0.6, 180), (-1.6, 260))):
        spot = P(MINI_SX, y)
        o = P(-1.6 + 0 * k, y)
        g.add(Dot(spot, radius=0.06, color=INK), DashedLine(spot + RIGHT * 0.15, o + LEFT * 0.3, color=LINE, stroke_width=2),
              varrow(o + UP * 0.12, o + UP * 0.12 + RIGHT * 0.9, width=5),
              varrow(o + DOWN * 0.12, o + DOWN * 0.12 + 0.9 * uvec(np.radians(ang)), width=5))
    yield [FadeIn(g), FadeIn(left_at(words("why does the angle between the two arrows change from spot to spot?", 24, 26, ORANGE), 0.4, -0.1))]


# ================================================================== matter waves
deck.part("Matter waves set the phase")

RT_Y = 0.2
RT_L = 4.0  # wavelength in screen units


def route_line():
    return VGroup(Line([-6.4, RT_Y, 0], [6.6, RT_Y, 0], color=LINE, stroke_width=3),
                  Arrow([5.8, RT_Y - 0.6, 0], [6.8, RT_Y - 0.6, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.15),
                  lab("along the route", 22).move_to([6.0, RT_Y - 0.95, 0]))


def route_arrows():
    xs = np.arange(-6.0, 6.01, 0.5)
    return VGroup(*[phasor([x, RT_Y], 2 * PI * (x + 6.0) / RT_L + PI / 2, 1.0, r=0.3, ring=False, width=4) for x in xs])


@slide("Matter waves set the phase.", "The arrow turns along the route")
def mw1(s):
    yield hold()
    yield [FadeIn(at(T("a fact from experiment, not a third rule", 28, INK, True), 0, 2.1))]
    p = Dot([-6.0, RT_Y, 0], radius=0.14, color=BLUE)
    yield [Create(route_line()), FadeIn(p), p.animate.move_to([5.0, RT_Y, 0]),
           FadeIn(at(lab("follow a particle along its route", 24, BLUE), 0, 1.2))]


@slide("As you follow it, its amplitude's arrow keeps turning.", "The arrow turns along the route")
def mw2(s):
    s.add(route_line())
    ar = route_arrows()
    yield [LaggedStart(*[FadeIn(a) for a in ar], lag_ratio=0.05), FadeIn(at(lab("its amplitude's arrow keeps turning", 24, BLUE), 0, 1.6))]
    br = BraceBetweenPoints([-6.0, RT_Y - 0.5, 0], [-6.0 + RT_L, RT_Y - 0.5, 0], direction=DOWN, color=ORANGE)
    yield [FadeIn(br), FadeIn(lab("one wavelength: one full turn", 24, ORANGE).next_to(br, DOWN, buff=0.1))]
    yield [FadeIn(at(lab("this turning is the amplitude's phase; it has nothing to do with spin", 24, INK), 0, -2.6))]


@slide("The particle's momentum sets the wavelength.", "The wavelength")
def mw3(s):
    yield [FadeIn(at(lab("the particle's momentum sets the wavelength", 28, INK), 0, 1.8))]
    yield [FadeIn(at(VGroup(T("wavelength =", 30, BLUE, True), heq("h / momentum", 32, BLUE)).arrange(RIGHT, buff=0.25), 0, 0.6)),
           FadeIn(at(lab("h: Planck's constant", 24, PURPLE), 0, -0.2))]
    yield [FadeIn(at(heq("h = 6.63 × 10⁻³⁴ joule-seconds", 32, PURPLE), 0, -1.4)), FadeIn(at(lab("tiny", 26, PURPLE, True), 0, -2.2))]


def packet(c, L=1.6, lam=0.35, color=ORANGE):
    c = P(c[0], c[1])
    f = lambda t: c + RIGHT * (t - L / 2) + UP * 0.25 * np.sin(2 * PI * t / lam) * np.exp(-((t - L / 2) / (L / 3.2)) ** 2)
    return ParametricFunction(f, t_range=[0, L], color=color, stroke_width=4)


@slide("Louis de Broglie proposed this rule in nineteen twenty-four", "Borrowed from light")
def mw4(s):
    yield [FadeIn(left_at(T("1924: Louis de Broglie, borrowing from light", 28, INK, True), -6.8, 2.1))]
    yield [FadeIn(packet([-5.4, 0.8])), FadeIn(packet([-3.4, 0.8])), FadeIn(left_at(lab("light comes in packets", 24, ORANGE), -6.4, 0.0)),
           FadeIn(left_at(heq("momentum = h / wavelength", 28, ORANGE), -6.4, -0.6))]
    yield [GrowArrow(arrow(P(-0.6, 0.3), P(0.8, 0.3), color=MUTED)), FadeIn(left_at(lab("read the other way round, for matter", 24, BLUE), 1.0, 0.9)),
           FadeIn(left_at(heq("wavelength = h / momentum", 28, BLUE), 1.0, 0.3))]
    k = PI / 0.45
    band = VGroup(*[Rectangle(width=0.22, height=0.9, stroke_width=0, fill_color=stripe_color((np.cos(k * x) + 1) / 2), fill_opacity=1).move_to([x - 4.0, -2.3, 0])
                    for x in np.arange(-2.4, 2.45, 0.22)])
    yield [FadeIn(band), FadeIn(left_at(VGroup(lab("check: the two-slit stripe spacing matches", 24, TEAL), check()).arrange(RIGHT, buff=0.2), -1.2, -2.3))]


PA_BX, PA_SX, PA_LAM = -5.4, -1.6, 0.55
PA_YS = np.linspace(-2.0, 2.0, 9)


def pa_rig():
    return VGroup(Line([PA_BX, 2.3, 0], [PA_BX, 0.15, 0], color=INK, stroke_width=6), Line([PA_BX, -0.15, 0], [PA_BX, -2.3, 0], color=INK, stroke_width=6),
                  Line([PA_SX, 2.3, 0], [PA_SX, -2.3, 0], color=MUTED, stroke_width=4),
                  lab("one slit", 22).move_to([PA_BX, -2.7, 0]), lab("screen", 22).move_to([PA_SX, -2.7, 0]))


def pa_arrows():
    g = VGroup()
    for y in PA_YS:
        d = np.hypot(PA_SX - PA_BX, y)
        ang = 2 * np.pi * d / PA_LAM
        L = 0.9 * np.exp(-y ** 2 / 3.0)
        o = P(PA_SX + 0.75, y)
        v = uvec(ang) * L
        g.add(Dot([PA_SX, y, 0], radius=0.04, color=INK), varrow(o - v / 2, o + v / 2, width=5, tip=0.16))
    return g


def pa_lines():
    g = VGroup()
    for y in PA_YS:
        d = np.hypot(PA_SX - PA_BX, y)
        u = np.array([PA_SX - PA_BX, y, 0]) / d
        g.add(DashedVMobject(Line(P(PA_BX, 0) + 0.3 * u, [PA_SX, y, 0], color=MUTED, stroke_width=1.5), num_dashes=12))
    return g


@slide("With one slit, you can't see the turning.", "One slit hides the turning")
def ph1(s):
    yield [FadeIn(pa_rig()), FadeIn(at(lab("one slit: the turning can't be seen", 24, INK, True), 3.4, 2.2))]
    yield [FadeIn(pa_arrows()), FadeIn(left_at(lab("each spot: an arrow pointing its own way", 22, BLUE), 0.0, 1.3))]
    yield [Create(pa_lines()), FadeIn(left_at(lab("its direction: set by the spot's distance from the slit", 22, INK), 0.0, 0.7))]


@slide("But the chance only uses the arrow's length.", "One slit hides the turning")
def ph2(s):
    s.add(pa_rig(), pa_arrows(), pa_lines(), at(lab("one slit: the turning can't be seen", 24, INK, True), 3.4, 2.2))
    ax = Axes(x_range=[0, 1.2, 1], y_range=[-2.2, 2.2, 1], x_length=2.6, y_length=4.0, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([2.2, -0.2, 0])
    hump = lambda y: np.exp(-y ** 2 / 3.0)
    yield [Create(ax), Create(ax.plot_parametric_curve(lambda t: np.array([hump(t) ** 2, t, 0]), t_range=[-2.2, 2.2], color=TEAL, stroke_width=5)),
           FadeIn(lab("chance per metre: only the lengths", 22, TEAL).move_to([2.4, -2.65, 0]))]
    yield [FadeIn(at(words("like the vertical magnet that couldn't see which way an atom leaned", 20, 22, MUTED, ORIGIN), 5.7, -1.0))]


TR_BX, TR_SX = -4.6, -0.6
TR_A, TR_B = P(TR_BX, 0.75), P(TR_BX, -0.75)
TR_BRIGHT, TR_DARK = P(TR_SX, 0.0), P(TR_SX, 1.9)
TR_LAM = 2 * (np.linalg.norm(TR_DARK - TR_B) - np.linalg.norm(TR_DARK - TR_A))
TR_MID = P(TR_SX, 1.0)


def tr_rig():
    return VGroup(Dot([-6.6, 0, 0], radius=0.09, color=INK), lab("source", 22).move_to([-6.6, -0.4, 0]),
                  DashedLine([-6.5, 0, 0], TR_A, color=MUTED, stroke_width=2), DashedLine([-6.5, 0, 0], TR_B, color=MUTED, stroke_width=2),
                  Line([TR_BX, 2.6, 0], [TR_BX, 0.95, 0], color=INK, stroke_width=6), Line([TR_BX, 0.55, 0], [TR_BX, -0.55, 0], color=INK, stroke_width=6),
                  Line([TR_BX, -0.95, 0], [TR_BX, -2.6, 0], color=INK, stroke_width=6), Line([TR_SX, 2.6, 0], [TR_SX, -2.6, 0], color=MUTED, stroke_width=4),
                  lab("A", 22, INK, True).move_to(TR_A + LEFT * 0.3 + UP * 0.2), lab("B", 22, INK, True).move_to(TR_B + LEFT * 0.3 + DOWN * 0.2),
                  lab("screen", 22).move_to([TR_SX, -2.95, 0]))


def start_arrows():
    return VGroup(*[varrow(p + RIGHT * 0.1 + UP * 0.0, p + RIGHT * 0.1 + 0.6 * uvec(PI / 2) , width=4, tip=0.14).shift(LEFT * 0.0) for p in (TR_A + LEFT * 0.0, TR_B)])


def end_pair(spot, x, y, label_text):
    dA, dB = np.linalg.norm(spot - TR_A), np.linalg.norm(spot - TR_B)
    angA = PI / 2 + 2 * PI * dA / TR_LAM
    angB = PI / 2 + 2 * PI * dB / TR_LAM
    o = P(x, y)
    vA, vB = 0.8 * uvec(angA), 0.8 * uvec(angB)
    oB = o + RIGHT * 1.6
    g = VGroup(varrow(o - vA / 2, o + vA / 2, width=5), lab("via A", 22, BLUE).move_to(o + DOWN * 0.7),
               varrow(oB - vB / 2, oB + vB / 2, width=5), lab("via B", 22, BLUE).move_to(oB + DOWN * 0.7),
               left_at(lab(label_text, 22, INK, True), 0.6, y + 0.85))
    return g


@slide("With two slits, both routes start from the same source", "Two routes, two turns")
def tr1(s):
    yield [FadeIn(tr_rig()), FadeIn(start_arrows()), FadeIn(left_at(lab("both routes start with the same arrow", 22, BLUE), 0.4, 2.2))]
    yield [Create(Line(TR_A, TR_MID, color=BLUE, stroke_width=3)), Create(DashedLine(TR_B, TR_MID, color=BLUE, stroke_width=3)),
           FadeIn(Dot(TR_MID, radius=0.09, color=INK)), FadeIn(left_at(lab("the two routes to a spot have different lengths", 22, INK), 0.4, 1.5))]
    yield [FadeIn(end_pair(TR_MID, 2.0, -0.6, "at this spot: turned by different amounts"))]


@slide("Where one route is a whole number of wavelengths longer", "Bright and dark")
def tr2(s):
    s.add(tr_rig())
    yield [Create(Line(TR_A, TR_BRIGHT, color=BLUE, stroke_width=3)), Create(Line(TR_B, TR_BRIGHT, color=BLUE, stroke_width=3)),
           FadeIn(Dot(TR_BRIGHT, radius=0.1, color=TEAL)), FadeIn(lab("bright", 22, TEAL, True).move_to(TR_BRIGHT + RIGHT * 0.65)),
           FadeIn(end_pair(TR_BRIGHT, 2.2, 0.6, "whole number of wavelengths: arrows match")),
           FadeIn(left_at(lab("bright", 24, TEAL, True), 4.6, 0.6))]
    yield [Create(DashedLine(TR_A, TR_DARK, color=BLUE, stroke_width=3)), Create(DashedLine(TR_B, TR_DARK, color=BLUE, stroke_width=3)),
           FadeIn(Dot(TR_DARK, radius=0.1, color=INK)), FadeIn(lab("dark", 22, INK, True).move_to(TR_DARK + RIGHT * 0.55)),
           FadeIn(end_pair(TR_DARK, 2.2, -1.9, "half a wavelength: arrows opposite")),
           FadeIn(left_at(lab("dark", 24, INK, True), 4.6, -1.9))]


def stripe_band(x0, x1, y, period, h=0.7):
    k = 2 * PI / period
    w = 0.12
    return VGroup(*[Rectangle(width=w + 0.01, height=h, stroke_width=0, fill_color=stripe_color((np.cos(k * (x - x0)) + 1) / 2), fill_opacity=1).move_to([x, y, 0])
                    for x in np.arange(x0, x1, w)])


@slide("Move along the screen, and the difference in route lengths", "Stripes")
def stripes2(s):
    band = stripe_band(-6.0, 6.0, 1.0, 2.4)
    ticks = VGroup()
    for k, t in enumerate(["0", "½", "1", "1½", "2", "2½"]):
        x = -6.0 + 1.2 * k
        ticks.add(lab(t, 24, INK, True).move_to([x, 1.75, 0]))
    yield [FadeIn(ticks), FadeIn(left_at(lab("route difference, in wavelengths: grows steadily along the screen", 22, INK), -6.4, 2.25))]
    yield [FadeIn(band), FadeIn(at(lab("bright and dark alternate in stripes", 24, TEAL, True), 0, 0.15))]
    slow = stripe_band(-6.0, -0.4, -1.6, 1.6, 0.6)
    fast = stripe_band(0.6, 6.2, -1.6, 0.8, 0.6)
    yield [FadeIn(slow), FadeIn(fast), FadeIn(at(lab("slower: longer wavelength", 22, INK), -3.2, -2.3)),
           FadeIn(at(lab("faster: shorter wavelength, closer stripes", 22, INK), 3.4, -2.3))]


# ================================================================== momentum
deck.part("Momentum, how fast the phase turns")


@slide("Momentum, how fast the phase turns.", "Position, found")
def mo1(s):
    yield hold()
    yield [FadeIn(at(pill("position", BLUE, 28), -2.0, 1.8)), FadeIn(at(pill("momentum", BLUE, 28), 2.0, 1.8)),
           FadeIn(at(lab("what we set out to find", 24, INK), 0, 2.4))]
    row = amp_row_line(-0.2, 0.9 * XS, np.exp(-XS ** 2 / 12), r=0.42)
    ax = Arrow([-6.6, -1.2, 0], [6.8, -1.2, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.18)
    yield [FadeIn(row), FadeIn(ax), FadeIn(lab("position", 22).next_to(ax.get_end(), DOWN, buff=0.12).shift(LEFT * 0.5)),
           FadeIn(at(lab("position: the variable of the wave function", 26, BLUE, True), 0, -2.3)), Create(check().next_to(at(pill("position", BLUE, 28), -2.0, 1.8), RIGHT, buff=0.15))]


@slide("On the screen, that was the position across the screen.", "Position, then momentum")
def mo2(s):
    yield [FadeIn(left_at(lab("on the screen: the position across the screen", 24, INK), -6.6, 2.1))]
    yield [FadeIn(left_at(lab("in general: wherever the particle might be", 24, INK), -6.6, 1.4))]
    yield [FadeIn(at(VGroup(T("wavelength =", 30, BLUE, True), heq("h / momentum", 32, BLUE)).arrange(RIGHT, buff=0.25), 0, 0.0)),
           FadeIn(at(lab("de Broglie's rule", 22, MUTED), 0, -0.7))]
    yield [FadeIn(at(VGroup(T("momentum =", 30, BLUE, True), heq("h / wavelength", 32, BLUE)).arrange(RIGHT, buff=0.25), 0, -1.8)),
           FadeIn(at(lab("read the other way round", 22, MUTED), 0, -2.5))]


def turn_row(y, lam, x0=-5.0, x1=6.4, step=0.35, r=0.28):
    xs = np.arange(x0, x1 + 0.01, step)
    return VGroup(*[phasor([x, y], 2 * PI * (x - x0) / lam + PI / 2, 1.0, r=r, ring=False, width=4) for x in xs])


@slide("So take a particle with a definite momentum.", "A definite momentum")
def mo3(s):
    row = turn_row(0.3, 4.0, -6.0, 6.4, 0.5, 0.3)
    yield [FadeIn(at(lab("a particle with a definite momentum", 26, INK, True), 0, 2.0)), LaggedStart(*[FadeIn(a) for a in row], lag_ratio=0.03)]
    yield [GrowArrow(Arrow([-6.0, -1.0, 0], [6.4, -1.0, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.2)),
           FadeIn(at(lab("its phase turns steadily along its direction of travel", 24, BLUE), 0, -1.6))]


@slide("Its momentum is Planck's constant times the number of turns", "Turns per metre")
def mo4(s):
    yield [FadeIn(at(VGroup(T("momentum =", 30, BLUE, True), heq("h × (turns per metre)", 32, BLUE)).arrange(RIGHT, buff=0.25), 0, 2.0))]
    r1 = turn_row(0.4, 2.7, -1.2, 6.6, 0.45, 0.27)
    yield [FadeIn(r1), FadeIn(left_at(words("short wavelength: many turns per metre, a large momentum", 22, 22, INK), -7.0, 0.4))]
    r2 = turn_row(-1.8, 8.1, -1.2, 6.6, 0.45, 0.27)
    yield [FadeIn(r2), FadeIn(left_at(words("long wavelength: few turns, a small momentum", 22, 22, INK), -7.0, -1.8))]


@slide("In chapter one, momentum was mass times velocity.", "Two numbers become one wave function")
def mo5(s):
    yield [FadeIn(left_at(VGroup(T("chapter 1:", 28, INK, True), T("momentum = mass × velocity", 28, INK)).arrange(RIGHT, buff=0.25), -6.6, 1.8))]
    pt = VGroup(T("(position, momentum)", 30, MUTED), lab("a second number, listed beside the position", 22, MUTED))
    pt.arrange(DOWN, buff=0.2)
    o = P(2.2, -2.4)
    ps = VGroup(Arrow(o, o + RIGHT * 3.6, buff=0, color=MUTED, stroke_width=3, tip_length=0.16),
                Arrow(o, o + UP * 3.0, buff=0, color=MUTED, stroke_width=3, tip_length=0.16),
                lab("position", 22).move_to(o + RIGHT * 3.3 + DOWN * 0.3), lab("momentum", 22).move_to(o + UP * 3.25 + RIGHT * 0.3),
                Dot(o + P(2.2, 1.8), radius=0.12, color=BLUE),
                DashedLine(o + P(2.2, 1.8), o + P(2.2, 0), color=BLUE, stroke_width=2), DashedLine(o + P(2.2, 1.8), o + P(0, 1.8), color=BLUE, stroke_width=2))
    yield [FadeIn(left_at(pt, -6.6, 0.4)), FadeIn(ps)]


@slide("In quantum mechanics, both live in the one wave function.", "Two numbers become one wave function")
def mo6(s):
    yield [FadeIn(at(T("quantum mechanics: both live in the one wave function", 28, BLUE, True), 0, 2.1))]
    xs = np.arange(-4.0, 6.41, 0.45)
    r1 = VGroup(*[phasor([x, 0.7], 2 * PI * x / 3.6, float(np.exp(-((x - 1.2) / 1.6) ** 2)), r=0.27, ring=False, width=4)
                  if np.exp(-((x - 1.2) / 1.6) ** 2) > 0.12 else Dot([x, 0.7, 0], radius=0.04, color=BLUE) for x in xs])
    yield [FadeIn(r1), FadeIn(left_at(words("position: where the amplitudes are", 14, 24, INK), -7.0, 0.7))]
    r2 = turn_row(-1.6, 3.6, -4.0, 6.4, 0.45, 0.27)
    yield [FadeIn(r2), FadeIn(left_at(words("a definite momentum: how fast their phase turns", 14, 24, INK), -7.0, -1.6))]


# ================================================================== where this goes next
deck.part("Where this goes next")


@slide("Where this goes next.", "Summing up")
def end1(s):
    yield hold()
    yield [FadeIn(at(card("a state is a list of amplitudes:\narrows with a length and a phase", 10.6, 1.4, BLUE, 28), 0, 1.4))]
    yield [FadeIn(at(card("measuring collapses the state,\nand the Born rule gives the chances", 10.6, 1.4, TEAL, 28), 0, -0.4))]


@slide("Two ways that nothing tells apart add their amplitudes", "Summing up")
def end2(s):
    s.add(at(card("a state is a list of amplitudes:\narrows with a length and a phase", 10.6, 1.4, BLUE, 28), 0, 1.4),
          at(card("measuring collapses the state,\nand the Born rule gives the chances", 10.6, 1.4, TEAL, 28), 0, -0.4))
    yield [FadeIn(at(card("two ways that nothing tells apart add their amplitudes,\nso they can interfere", 10.6, 1.2, INK, 26), 0, -2.0))]
    yield [FadeIn(at(card("the phase turns along a particle's route, at a rate set by its momentum", 12.4, 0.8, ORANGE, 26), 0, -3.3))]


@slide("The next chapter, First Quantization, turns these ideas", "Next: First Quantization")
def end3(s):
    yield [FadeIn(at(card("Chapter 2b: First Quantization\nthese ideas, as maths", 7.4, 1.4, INK, 30), 0, 1.6))]
    rows = [("position and momentum", "operators, acting on the wave function"),
            ("chapter 1's Poisson bracket", "its quantum version, the commutator"),
            ("chapter 1's Hamiltonian", "moves the state forward in time, through the Schrödinger equation")]
    for k, (a, b) in enumerate(rows):
        y = 0.0 - 1.05 * k
        l = left_at(T(a, 24, INK, True), -7.0, y)
        r = left_at(words(b, 34, 24, BLUE), -0.6, y)
        yield [FadeIn(l), GrowArrow(Arrow([-1.6, y, 0], [-0.8, y, 0], buff=0, color=MUTED, stroke_width=4, tip_length=0.15)), FadeIn(r)]

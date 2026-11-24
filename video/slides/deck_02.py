"""Slides for chapter two, First Quantization.

Every value comes from video/scripts/02-first-quantization.txt or
docs/first-quantization.md. The figures follow docs/manim/page_diagrams.py
(SternGerlachSetup, MagnetsInRow, TwoSlitCounts, EigenbasisProbabilities,
BornDensity, PhotoelectricEffect, ComptonScattering, DavissonGermer,
FourierUncertainty), with the same geometry and numbers.

Colors: BLUE for states and amplitudes (state arrows, wave functions, the
arrows that draw complex numbers) and for the particles that carry them (atoms,
electrons), TEAL for chances, probability densities and counts, and for checks
that pass, ORANGE for light and X-ray packets and for the step under discussion,
PURPLE for operators, commutators, brackets, the Hamiltonian and h-bar, RED only
for a prediction that fails (the smeared line, chances that only add, real
amplitudes, a wave moving backwards, hidden local details), MUTED and LINE for
apparatus, context and connectors.
"""
import re

from manim import *

from engine import *

STEM = "02-first-quantization"
deck = Deck(f"scripts/{STEM}.txt")
slide = deck.slide


def at(mob, x, y):
    return mob.move_to([x, y, 0])


def lab(text, size=24, color=MUTED, bold=False):
    return T(text, size, color, bold)


def eq(text, size=30, color=INK):
    return heq(text, size, color)


def left_at(mob, x, y):
    """Place a mobject with its left edge at x."""
    return mob.move_to([x + mob.width / 2, y, 0])


def words(text, chars=40, size=26, color=INK, align=LEFT):
    return W(text, chars, size, color, align=align)


def pts(first, title, items, sub=None, chars=56, size=30, y=None, gap=0.42, dots=BLUE):
    """A slide whose points arrive one at a time."""
    @slide(first, title, sub)
    def build(s):
        rows = bullets(items, chars, size, gap=gap, dot=dots)
        rows.move_to([-7.0 + rows.width / 2, 0 if y is None else y, 0])
        for row in rows:
            yield [FadeIn(row, shift=RIGHT * 0.15)]
    return build


def heq(text, size=30, color=INK, font=MONO):
    """Text in which Planck's constant (a standalone h) and h-bar are PURPLE.

    Manim's t2c matches plain substrings, so the keys are index slices found with a regex.
    """
    t2c = {f"[{m.start()}:{m.end()}]": PURPLE for m in re.finditer(r"\bh\b|ħ", text)}
    return Text(text, font=font, color=color, font_size=size, t2c=t2c)


def tick(mob, color=TEAL, buff=0.2):
    return check(color).next_to(mob, RIGHT, buff=buff)


def xmark(mob, size=0.42, buff=0.2, color=RED):
    box = Square(size).next_to(mob, RIGHT, buff=buff)
    return cross(box, color, 6)


def num_pill(n, color=INK, size=22):
    return pill(str(n), color, size)


# ------------------------------------------------------------------ shared drawings

def stripe_color(f):
    """Screen shading: dark (INK) where few electrons land, bright TEAL where many do."""
    return interpolate_color(ManimColor(INK), ManimColor(TEAL), float(np.clip(f, 0, 1)))


def phasor(c, ang=0.0, frac=1.0, r=0.45, color=BLUE, ring=True, width=4):
    """A complex number drawn as an arrow in a circle of radius r (size 1)."""
    c = np.array([c[0], c[1], 0.0])
    g = VGroup()
    if ring:
        g.add(Circle(radius=r, color=LINE, stroke_width=2).move_to(c))
    end = c + frac * r * np.array([np.cos(ang), np.sin(ang), 0])
    g.add(Arrow(c, end, buff=0, color=color, stroke_width=width, tip_length=0.13,
                max_tip_length_to_length_ratio=0.45, max_stroke_width_to_length_ratio=30))
    return g


def bar(x, base, frac, hmax=2.6, w=1.0, color=TEAL, label=None, size=24, opacity=0.8):
    """A probability bar rising from y = base, with its percentage on top."""
    h = max(hmax * frac, 0.02)
    r = Rectangle(width=w, height=h, stroke_width=0, fill_color=color, fill_opacity=opacity).move_to([x, base + h / 2, 0])
    g = VGroup(r)
    if label:
        g.add(T(label, size, color, True).next_to(r, UP, buff=0.12))
    return g


def mat(rows, size=26, color=INK, colw=None, rowh=0.55, bcolor=None):
    """A matrix or column drawn from text cells between square brackets."""
    ncol = len(rows[0])
    cells = [[code(c, size, color) if isinstance(c, str) else c for c in r] for r in rows]
    colw = colw or max(c.width for r in cells for c in r) + 0.45
    g = VGroup()
    for i, r in enumerate(cells):
        for j, c in enumerate(r):
            c.move_to([(j - (ncol - 1) / 2) * colw, -(i - (len(rows) - 1) / 2) * rowh, 0])
            g.add(c)
    h = rowh * len(rows) + 0.1
    w = colw * ncol
    bc = bcolor or color
    lb = VMobject(color=bc, stroke_width=3).set_points_as_corners([[-w / 2 + 0.12, h / 2, 0], [-w / 2, h / 2, 0], [-w / 2, -h / 2, 0], [-w / 2 + 0.12, -h / 2, 0]])
    rb = VMobject(color=bc, stroke_width=3).set_points_as_corners([[w / 2 - 0.12, h / 2, 0], [w / 2, h / 2, 0], [w / 2, -h / 2, 0], [w / 2 - 0.12, -h / 2, 0]])
    return VGroup(lb, rb, g)


def dial(c, tilt_deg, r=0.95, color=BLUE, name=None, arc_color=ORANGE, show_arc=True, size=24):
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


def spin_plane(o, r=3.0, neg=False, up="up amplitude", down="down amplitude", size=22):
    """Axes for a spin state: the up amplitude across, the down amplitude upward."""
    o = np.array([o[0], o[1], 0.0])
    lo = o + DOWN * (r * 0.8 if neg else 0)
    g = VGroup(Arrow(o, o + RIGHT * (r + 0.4), buff=0, color=MUTED, stroke_width=3, tip_length=0.18),
               Arrow(lo, o + UP * (r + 0.4), buff=0, color=MUTED, stroke_width=3, tip_length=0.18))
    g.add(T(up, size, MUTED).next_to(g[0].get_end(), DOWN, buff=0.12))
    g.add(T(down, size, MUTED).next_to(g[1].get_end(), UP, buff=0.08))
    return g


def state_arrow(o, r, a_up, a_down, color=BLUE, width=6):
    o = np.array([o[0], o[1], 0.0])
    return Arrow(o, o + r * np.array([a_up, a_down, 0]), buff=0, color=color, stroke_width=width, tip_length=0.22)


def magnet(name, x, y, w=1.9, h=0.85, color=INK, size=24):
    return at(card(name, w, h, color, size), x, y)


def slot_arrow(a, b, color=INK):
    return Arrow(a, b, buff=0, color=color, stroke_width=4, tip_length=0.17)


# ------------------------------------------------------------------ opening
deck.part("Chapter two")


@slide("Chapter two.", "First Quantization")
def opening(s):
    c1 = at(card("Chapter 1\nClassical Mechanics", 5.0, 1.6, MUTED, 30), -4.0, 0.9)
    ax = VGroup(Line([-5.2, -1.9, 0], [-2.8, -1.9, 0], color=LINE, stroke_width=3),
                Line([-5.2, -1.9, 0], [-5.2, -0.6, 0], color=LINE, stroke_width=3))
    dot = Dot([-3.9, -1.2, 0], radius=0.11, color=BLUE)
    pt_ = VGroup(ax, dot, T("a point (q, p)", 24, BLUE).next_to(dot, RIGHT, buff=0.15))
    yield [FadeIn(c1), FadeIn(pt_)]
    c2 = at(card("Chapter 2\nFirst Quantization", 5.0, 1.6, INK, 30), 3.9, 0.9)
    rowp = VGroup(*[phasor([2.2 + 1.15 * k, -1.2], ang, frac, r=0.48) for k, (ang, frac) in
                    enumerate(((0.3, 0.9), (1.4, 0.6), (2.6, 0.8), (-0.9, 0.5)))])
    yield [GrowArrow(arrow(c1, c2)), FadeIn(c2), FadeIn(rowp),
           FadeIn(lab("a list of amplitudes", 24, BLUE).next_to(rowp, DOWN, buff=0.2))]


# ------------------------------------------------------------------ previously
deck.part("Previously")


def promise_rows(compact=False):
    p1 = at(pill("promise 1", INK, 24), -6.2, 1.6)
    h = at(eq("H = p²/2m + V", 34, PURPLE), -2.9, 1.6)
    hl = lab("the energy, written with position q and momentum p", 22).next_to(h, DOWN, buff=0.15)
    p2 = at(pill("promise 2", INK, 24), -6.2, -1.0)
    return p1, h, hl, p2


def time_move():
    a = at(card("state now", 2.4, 0.8, BLUE, 24), 2.5, 1.6)
    b = at(card("state later", 2.4, 0.8, BLUE, 24), 6.0, 1.6)
    ar = arrow(a, b, color=PURPLE)
    return VGroup(a, b, ar, lab("H moves it forward in time", 22, PURPLE).next_to(VGroup(a, b), DOWN, buff=0.2))


def bracket_move():
    b = at(eq("{q, p} = 1", 34, PURPLE), -3.2, -1.0)
    c = at(card("a commutator", 3.2, 0.8, PURPLE, 26), 1.6, -1.0)
    return VGroup(b, arrow(b, c, color=PURPLE), c, lab("the Poisson bracket", 22).next_to(b, DOWN, buff=0.15))


def order_pipes(y=-2.6):
    def pipe(first, second, x):
        a = at(card(first, 1.1, 0.6, PURPLE, 24), x, y)
        b = at(card(second, 1.1, 0.6, PURPLE, 24), x + 1.6, y)
        return VGroup(a, b, arrow(a, b))
    p = pipe("A", "B", -1.2)
    q = pipe("B", "A", 3.0)
    ne = at(T("vs", 26, MUTED), 2.1, y)
    return VGroup(p, ne, q, lab("does the order matter, and by how much?", 22).move_to([2.1, y - 0.65, 0]))


@slide("The last chapter ended with two promises.", "Two promises from chapter 1")
def promises1(s):
    p1, h, hl, p2 = promise_rows()
    yield [FadeIn(p1), FadeIn(p2)]
    yield [FadeIn(h), FadeIn(hl), FadeIn(lab("keeps its job", 24, INK, True).next_to(h, UP, buff=0.2))]
    yield [FadeIn(time_move(), shift=RIGHT * 0.15)]


@slide("And the Poisson bracket of position with momentum would become", "Two promises from chapter 1")
def promises2(s):
    p1, h, hl, p2 = promise_rows()
    s.add(p1, h, hl, p2, lab("keeps its job", 24, INK, True).next_to(h, UP, buff=0.2), time_move())
    yield [FadeIn(bracket_move(), shift=RIGHT * 0.15)]
    yield [FadeIn(order_pipes())]


deck.part("Chapter two")


@slide("This chapter keeps both promises.", "First, a new kind of state")
def new_state(s):
    a = at(VGroup(eq("H moves the state", 26, PURPLE), tick(Dot(), buff=0)).arrange(RIGHT, buff=0.25), -3.6, 2.1)
    b = at(VGroup(eq("{q, p} → commutator", 26, PURPLE), tick(Dot(), buff=0)).arrange(RIGHT, buff=0.25), 3.4, 2.1)
    yield [FadeIn(a), FadeIn(b), FadeIn(lab("this chapter keeps both", 24).move_to([0, 1.45, 0]))]
    ax = VGroup(Arrow([-6.4, -2.2, 0], [-3.4, -2.2, 0], buff=0, color=LINE, stroke_width=3, tip_length=0.15),
                Arrow([-6.4, -2.2, 0], [-6.4, 0.6, 0], buff=0, color=LINE, stroke_width=3, tip_length=0.15),
                lab("q", 22).move_to([-3.3, -2.5, 0]), lab("p", 22).move_to([-6.7, 0.5, 0]))
    dot = Dot([-4.9, -0.9, 0], radius=0.13, color=BLUE)
    first = at(T("first: change what a state is", 28, ORANGE, True), -3.9, 1.0)
    yield [FadeIn(ax), FadeIn(dot), FadeIn(first)]
    atoms = VGroup(*[Dot([0.3 + 0.45 * k, -0.4 + 0.25 * np.sin(k), 0], radius=0.09, color=BLUE) for k in range(6)])
    note = words("atoms and electrons in a few experiments: no single (q, p) describes them", 30, 26, INK).move_to([3.6, -0.6, 0])
    atoms.next_to(note, UP, buff=0.3)
    yield [FadeIn(atoms), FadeIn(note), Create(cross(VGroup(dot).copy().scale(2.4), RED, 5))]
    ex = at(card("experiment", 2.8, 0.75, INK, 24), 1.4, -2.6)
    ru = at(card("new rule", 2.8, 0.75, ORANGE, 24), 5.4, -2.6)
    yield [FadeIn(ex), GrowArrow(arrow(ex, ru)), FadeIn(ru), FadeIn(lab("forces", 22).move_to([3.4, -2.25, 0]))]


# ------------------------------------------------------------------ at a glance
deck.part("The chapter at a glance")

GX = (-5.95, -2.0, 3.8)   # label, classical and quantum column centers
GW = (2.8, 4.6, 6.8)
GY = [1.55, 0.55, -0.45, -1.45, -2.45]
GLANCE = [
    ("the state", "a point (q, p)", ["a list of complex numbers called amplitudes,", "one for each possible outcome"]),
    ("a measurable quantity", "a number computed from the point", ["an operator: a matrix whose eigenvalues", "are the possible results"]),
    ("a measurement gives", "the value, exactly", ["one of those results, at random", "chance = (size of its amplitude)²"]),
    ("what moves the state", "Hamilton's equations", ["the Schrödinger equation,", "built from the same energy H"]),
    ("position with momentum", "the bracket {q, p} = 1", ["a commutator, equal to i ħ", "ħ (h-bar): a tiny constant"]),
]


def glance_frame():
    heads = VGroup(at(T("classical (chapter 1)", 26, MUTED, True), GX[1], 2.35), at(T("quantum (this chapter)", 26, INK, True), GX[2], 2.35))
    boxes = VGroup()
    for y in GY:
        for x, w in zip(GX[1:], GW[1:]):
            boxes.add(at(card(None, w, 0.88, LINE), x, y))
    return heads, boxes


def glance_label(k):
    return at(words(GLANCE[k][0], 14, 23, MUTED, align=RIGHT), GX[0], GY[k]).align_to([GX[0] + GW[0] / 2, 0, 0], RIGHT)


def glance_classic(k):
    return at(words(GLANCE[k][1], 26, 23, INK, align=ORIGIN), GX[1], GY[k])


def glance_quantum(k, part=None):
    lines = GLANCE[k][2]
    color = PURPLE if k in (1, 4) else BLUE if k == 0 else TEAL if k == 2 else PURPLE
    g = VGroup(*[T(t, 23, color if i == 0 else INK) for i, t in enumerate(lines)]).arrange(DOWN, buff=0.1)
    at(g, GX[2], GY[k])
    return g if part is None else g[part]


def glance_base(s, upto):
    heads, boxes = glance_frame()
    s.add(heads, boxes)
    for k in range(upto):
        s.add(glance_label(k), glance_classic(k), glance_quantum(k))


@slide("The chapter at a glance.", "Each classical idea gets a quantum version")
def glance1(s):
    heads, boxes = glance_frame()
    yield [FadeIn(heads), LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.05)]
    yield [FadeIn(glance_label(0)), FadeIn(glance_classic(0))]
    yield [FadeIn(glance_quantum(0), shift=LEFT * 0.15)]


@slide("Classically, a measurable quantity is a number", "Each classical idea gets a quantum version")
def glance2(s):
    glance_base(s, 1)
    yield [FadeIn(glance_label(1)), FadeIn(glance_classic(1))]
    yield [FadeIn(glance_quantum(1), shift=LEFT * 0.15)]


@slide("Classically, a measurement gives the value exactly.", "Each classical idea gets a quantum version")
def glance3(s):
    glance_base(s, 2)
    yield [FadeIn(glance_label(2)), FadeIn(glance_classic(2))]
    yield [FadeIn(glance_quantum(2, 0), shift=LEFT * 0.15)]
    yield [FadeIn(glance_quantum(2, 1), shift=LEFT * 0.15)]


@slide("Hamilton's equations moved the classical point.", "Each classical idea gets a quantum version")
def glance4(s):
    glance_base(s, 3)
    yield [FadeIn(glance_label(3)), FadeIn(glance_classic(3))]
    yield [FadeIn(glance_quantum(3), shift=LEFT * 0.15)]
    yield [FadeIn(glance_label(4)), FadeIn(glance_classic(4))]
    yield [FadeIn(glance_quantum(4), shift=LEFT * 0.15)]


EXP_Y = [2.0, 1.1, 0.2, -0.7, -1.6, -2.5]
EXPS = [("1", "magnets sort atoms", "outcomes are random: the theory predicts chances"),
        ("2", "electrons through two slits", "the chances come from amplitudes that can cancel"),
        ("3", "light frees electrons from a metal", "light's energy comes in packets, set by frequency"),
        ("4", "X-rays bounce off electrons", "each packet carries momentum, set by wavelength"),
        (None, "de Broglie, a proposal", "the same two rules for matter"),
        ("5", "electrons bounce off a crystal", "matter has de Broglie's wavelength")]


def exp_row(k):
    n, name, lesson = EXPS[k]
    y = EXP_Y[k]
    if n is None:
        c = at(T(name, 24, MUTED, True), -4.2, y)
        les = left_at(T(lesson, 24, MUTED), -1.3, y)
        return VGroup(c, les)
    c = at(card(name, 5.4, 0.72, INK, 24), -4.2, y)
    p = at(num_pill(n), -7.2, y)
    les = left_at(T(lesson, 24, TEAL if k < 2 else ORANGE if k < 4 else BLUE), -1.3, y)
    return VGroup(p, c, les)


@slide("Five experiments drive these changes.", "Five experiments")
def five1(s):
    yield [FadeIn(lab("each experiment, and what it shows", 24).move_to([0, 2.55, 0]))]
    yield [FadeIn(exp_row(0), shift=RIGHT * 0.15)]
    yield [FadeIn(exp_row(1), shift=RIGHT * 0.15)]


@slide("Light knocking electrons out of a metal shows", "Five experiments")
def five2(s):
    s.add(lab("each experiment, and what it shows", 24).move_to([0, 2.55, 0]), exp_row(0), exp_row(1))
    yield [FadeIn(exp_row(2), shift=RIGHT * 0.15)]
    yield [FadeIn(exp_row(3), shift=RIGHT * 0.15)]
    yield [FadeIn(exp_row(4), shift=RIGHT * 0.15)]


@slide("And electrons bouncing off a crystal show", "Five experiments")
def five3(s):
    rows = [exp_row(k) for k in range(5)]
    s.add(lab("each experiment, and what it shows", 24).move_to([0, 2.55, 0]), *rows)
    r5 = exp_row(5)
    yield [FadeIn(r5, shift=RIGHT * 0.15)]
    mo = at(card("momentum operator", 2.9, 0.7, PURPLE, 24), 5.95, EXP_Y[5])
    yield [GrowArrow(arrow(r5[2], mo, color=PURPLE)), FadeIn(mo)]
    se = at(card("Schrödinger\nequation", 2.6, 0.95, PURPLE, 24), 6.15, EXP_Y[4] + 0.1)
    link = arrow(rows[4][1], se, color=PURPLE)
    yield [rows[4][1].animate.set_color(INK), FadeIn(se), GrowArrow(link)]


@slide("Replacing classical quantities by operators like this", "First quantization")
def first_q(s):
    q = at(chip("position q", BLUE, size=28, h=0.8), -5.0, 1.6)
    p = at(chip("momentum p", BLUE, size=28, h=0.8), -5.0, 0.4)
    ops = at(card("operators", 3.4, 1.0, PURPLE, 30), 0.4, 1.0)
    name = at(T("first quantization", 36, PURPLE, True), 4.8, 1.0)
    yield [FadeIn(q), FadeIn(p), GrowArrow(arrow([-3.4, 1.0, 0], ops)), FadeIn(ops), FadeIn(name)]
    part = at(card("this chapter: particles", 5.4, 0.9, BLUE, 28), -3.2, -1.4)
    yield [FadeIn(part), FadeIn(lab("“first”: it quantizes particles", 24, INK).move_to([-3.2, -2.25, 0]))]
    fld = at(card("a later chapter: fields", 5.4, 0.9, MUTED, 28), 3.4, -1.4)
    yield [GrowArrow(arrow(part, fld)), FadeIn(fld), FadeIn(lab("the same rule, applied to fields", 24, INK).move_to([3.4, -2.25, 0]))]


# ------------------------------------------------------------------ experiments
deck.part("Experiments that force a new state")


def sg_piece(k):
    """The pieces of the Stern-Gerlach figure, in the order the narration adds them."""
    if k == 0:
        oven = Rectangle(width=1.3, height=1.1, color=INK, fill_color=PALE, fill_opacity=1).move_to([-6.2, 0.3, 0])
        return VGroup(oven, lab("oven", 22).move_to([-6.2, -0.55, 0]))
    if k == 1:
        rng = np.random.default_rng(4)
        dots = VGroup(*[Dot([-5.3 + 0.35 * i, 0.3 + rng.uniform(-0.12, 0.12), 0], radius=0.07, color=BLUE) for i in range(5)])
        return VGroup(dots, left_at(T("1922: Otto Stern and Walther Gerlach", 22, INK), -7.0, -1.25),
                      left_at(T("silver atoms boiled off a hot oven", 22, BLUE), -7.0, -1.6))
    if k == 2:
        top = Polygon([-3.4, 1.55, 0], [-1.4, 1.55, 0], [-1.4, 0.85, 0], [-2.4, 0.55, 0], [-3.4, 0.85, 0], color=INK, fill_color=PALE, fill_opacity=1)
        bot = Polygon([-3.4, -0.25, 0], [-1.4, -0.25, 0], [-1.4, -0.95, 0], [-3.4, -0.95, 0], color=INK, fill_color=PALE, fill_opacity=1)
        beam = Line([-5.55, 0.3, 0], [-1.4, 0.3, 0], color=BLUE, stroke_width=4)
        return VGroup(beam, top, bot, lab("magnet", 22).move_to([-2.4, 1.85, 0]))
    if k == 3:
        c = np.array([-6.75, -2.25, 0])
        icon = VGroup(Circle(radius=0.3, color=BLUE, stroke_width=3).move_to(c),
                      Arrow(c + DOWN * 0.22, c + UP * 0.25, buff=0, color=BLUE, stroke_width=5, tip_length=0.13))
        return VGroup(icon, left_at(T("each atom is a tiny magnet: spin", 24, BLUE), -6.3, -2.25))
    if k == 4:
        return at(T("field stronger near the top pole", 22, ORANGE), -2.4, 2.3)
    if k == 5:
        fan = VGroup(*[Line([-1.4, 0.3, 0], [0.35, y, 0], color=BLUE, stroke_width=2.5).set_opacity(0.7)
                       for y in np.linspace(1.25, -0.65, 6)])
        push = DoubleArrow([-0.7, -0.35, 0], [-0.7, 1.0, 0], buff=0, color=ORANGE, stroke_width=3, tip_length=0.14)
        return VGroup(VGroup(fan, push), T("pushed up or down, depending on the atom's tilt", 22, INK).move_to([-1.0, -2.85, 0]))
    if k == 11:
        return VGroup(Line([-1.4, 0.3, 0], [0.35, 1.15, 0], color=BLUE, stroke_width=4),
                      Line([-1.4, 0.3, 0], [0.35, -0.55, 0], color=BLUE, stroke_width=4))
    if k == 6:
        return VGroup(Line([0.4, -1.6, 0], [0.4, 2.0, 0], color=MUTED, stroke_width=6), lab("glass plate", 22).move_to([0.4, -1.95, 0]))
    if k == 7:
        rng = np.random.default_rng(7)
        g = VGroup()
        for i, x in enumerate((-5.1, -4.5, -3.9)):
            ang = rng.uniform(0, TAU)
            c = np.array([x, 0.3 + (0.42 if i % 2 == 0 else -0.42), 0])
            d = 0.2 * np.array([np.cos(ang), np.sin(ang), 0])
            g.add(Circle(radius=0.2, color=BLUE, stroke_width=2).move_to(c), Arrow(c - d, c + d, buff=0, color=BLUE, stroke_width=4, tip_length=0.1))
        return VGroup(g, lab("tilted every which way", 22, BLUE).move_to([-5.4, 1.3, 0]))
    if k == 8:
        frame = RoundedRectangle(width=1.7, height=3.4, corner_radius=0.1, color=MUTED, stroke_width=2).move_to([3.3, 0.3, 0])
        smear = Line([3.3, -1.0, 0], [3.3, 1.6, 0], color=MUTED, stroke_width=12).set_opacity(0.6)
        return VGroup(frame, smear, lab("expected", 24, MUTED, True).move_to([3.3, 2.3, 0]),
                      words("a smeared line, top to bottom", 16, 22, MUTED, align=ORIGIN).move_to([3.3, -1.95, 0]))
    if k == 9:
        frame = RoundedRectangle(width=1.7, height=3.4, corner_radius=0.1, color=MUTED, stroke_width=2).move_to([6.1, 0.3, 0])
        return VGroup(frame, Dot([6.1, 1.15, 0], radius=0.18, color=BLUE), Dot([6.1, -0.55, 0], radius=0.18, color=BLUE),
                      lab("seen", 24, BLUE, True).move_to([6.1, 2.3, 0]),
                      words("two spots, nothing in between", 16, 22, BLUE, align=ORIGIN).move_to([6.1, -1.95, 0]))
    return at(T("The tilt along the field takes only two values.", 30, INK, True), 0, -3.5)


def sg_base(s, upto):
    for k in range(upto):
        s.add(sg_piece(k))


@slide("Experiments that force a new state.", "Magnets that sort atoms")
def sg1(s):
    yield [FadeIn(sg_piece(0))]
    p = sg_piece(1)
    yield [FadeIn(p[1]), FadeIn(p[2]), LaggedStart(*[FadeIn(d, shift=RIGHT * 0.3) for d in p[0]], lag_ratio=0.2)]


@slide("The atoms flew as a beam between the poles", "Magnets that sort atoms")
def sg2(s):
    sg_base(s, 2)
    yield [FadeIn(sg_piece(2))]
    yield [FadeIn(sg_piece(3), shift=DOWN * 0.15)]


@slide("The magnet's field is stronger near one pole.", "Magnets that sort atoms")
def sg3(s):
    sg_base(s, 4)
    yield [FadeIn(sg_piece(4))]
    p = sg_piece(5)
    yield [LaggedStart(*[Create(l) for l in p[0][0]], lag_ratio=0.1), GrowFromCenter(p[0][1]), FadeIn(p[1])]
    yield [FadeIn(sg_piece(6))]


@slide("The atoms leave the oven tilted every which way.", "Expected versus seen")
def sg4(s):
    for k in range(7):
        if k != 5:
            s.add(sg_piece(k))
    fan = sg_piece(5)
    s.add(fan)
    yield [FadeIn(sg_piece(7))]
    yield [FadeIn(sg_piece(8))]
    yield [FadeIn(sg_piece(9)), Create(cross(Square(1.0).move_to([3.3, 0.3, 0]), RED, 6)),
           FadeOut(fan[0]), Create(sg_piece(11))]
    yield [FadeIn(sg_piece(10), shift=UP * 0.15)]


ROW_Y = [1.75, 0.05, -1.65]
MAG_X = [-5.8, -2.4, 1.0]


def row_parts(r, upto=None):
    """Magnets, connecting arrows with their 'keep' labels, the result and the takeaway of row r."""
    y = ROW_Y[r]
    names = [["vertical", "vertical"], ["vertical", "sideways"], ["vertical", "sideways", "vertical"]][r]
    keeps = [["keep up"], ["keep up"], ["keep up", "keep right"]][r]
    result = ["all up again", "half right, half left", "half up, half down"][r]
    take = ["A measurement can leave a state that repeats.",
            "Identical atoms, different results: the theory predicts chances.",
            "The sideways measurement erased the earlier up."][r]
    mags = [magnet(n, MAG_X[i], y, color=ORANGE if n == "sideways" else INK) for i, n in enumerate(names)]
    links = []
    for i, kp in enumerate(keeps):
        a = slot_arrow([MAG_X[i] + 1.05, y, 0], [MAG_X[i] + 2.35, y, 0])
        links.append(VGroup(a, lab(kp, 22, INK).next_to(a, UP, buff=0.08)))
    last = MAG_X[len(names) - 1]
    out = slot_arrow([last + 1.0, y, 0], [last + 1.7, y, 0])
    res = left_at(T(result, 28, TEAL, True), last + 1.85, y)
    tk = left_at(T(take, 24, INK), -6.85, y - 0.72)
    return mags, links, VGroup(out, res), tk


def row_all(r):
    mags, links, res, tk = row_parts(r)
    return VGroup(*mags, *links, res, tk)


@slide("Later experiments put magnets in a row.", "Magnets in a row")
def row0(s):
    mags, links, res, tk = row_parts(0)
    yield [FadeIn(mags[0]), FadeIn(links[0])]
    yield [FadeIn(at(pill("an idealized version", MUTED, 22), 5.3, 2.4))]


@slide("Keep the atoms that went up, and send", "Magnets in a row")
def row1(s):
    mags, links, res, tk = row_parts(0)
    s.add(mags[0], links[0], at(pill("an idealized version", MUTED, 22), 5.3, 2.4))
    yield [FadeIn(mags[1], shift=RIGHT * 0.15)]
    yield [GrowArrow(res[0]), FadeIn(res[1])]
    yield [FadeIn(tk, shift=UP * 0.1)]


@slide("Now send those same atoms through a magnet turned sideways.", "Magnets in a row")
def row2(s):
    s.add(row_all(0), at(pill("an idealized version", MUTED, 22), 5.3, 2.4))
    mags, links, res, tk = row_parts(1)
    yield [FadeIn(mags[0]), FadeIn(links[0]), FadeIn(mags[1], shift=RIGHT * 0.15)]
    q = VGroup(lab("which atom goes where?", 22, ORANGE), lab("no way to predict", 22, ORANGE)).arrange(DOWN, buff=0.06)
    q.next_to(res[1], RIGHT, buff=0.35)
    yield [GrowArrow(res[0]), FadeIn(res[1]), FadeIn(q)]
    yield [FadeIn(tk, shift=UP * 0.1)]


@slide("Finally, keep the atoms that went right,", "Back to vertical")
def row3(s):
    s.add(row_all(0), row_all(1), at(pill("an idealized version", MUTED, 22), 5.3, 2.4))
    mags, links, res, tk = row_parts(2)
    yield [FadeIn(mags[0]), FadeIn(links[0]), FadeIn(mags[1]), FadeIn(links[1]), FadeIn(mags[2], shift=RIGHT * 0.15)]
    yield [GrowArrow(res[0]), FadeIn(res[1])]
    yield [FadeIn(tk.set_color(ORANGE), shift=UP * 0.1)]
    yield [FadeIn(at(T("Measuring changes the state.", 30, ORANGE, True), 0, -3.35), shift=UP * 0.15)]


SRC = np.array([-6.7, 0.2, 0])
SLIT_Y = (0.9, -0.5)          # first (upper) and second (lower) slit
BARRIER_X, SCREEN_X = -5.0, -3.2


def two_slit_rig(show_screen=True):
    bars = VGroup(*[Line([BARRIER_X, a, 0], [BARRIER_X, b, 0], color=INK, stroke_width=6) for a, b in ((-1.9, -0.65), (-0.35, 0.75), (1.05, 2.3))])
    g = VGroup(Dot(SRC, radius=0.1, color=INK), lab("source", 22).move_to(SRC + DOWN * 0.45), bars,
               lab("first", 22, INK).move_to([BARRIER_X + 0.55, 1.25, 0]), lab("second", 22, INK).move_to([BARRIER_X + 0.65, -0.85, 0]),
               *[DashedLine(SRC, [BARRIER_X, y, 0], color=MUTED, stroke_width=2) for y in SLIT_Y],
               lab("two slits", 22).move_to([BARRIER_X, -2.3, 0]))
    scr = VGroup(Line([SCREEN_X, -1.9, 0], [SCREEN_X, 2.3, 0], color=MUTED, stroke_width=6), lab("screen", 22).move_to([SCREEN_X, -2.3, 0]))
    return g, scr


def one_slit(y):
    return np.exp(-(y - 0.35) ** 2 / 2.6)


def two_slit(y):
    return np.exp(-(y + 0.35) ** 2 / 2.6)


def both_open(y):
    a, b = one_slit(y), two_slit(y)
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
    a = ax.plot(one_slit, x_range=[-3, 3], color=MUTED, stroke_width=3)
    b = ax.plot(two_slit, x_range=[-3, 3], color=MUTED, stroke_width=3)
    sm = DashedVMobject(ax.plot(lambda y: one_slit(y) + two_slit(y), x_range=[-3, 3], color=INK, stroke_width=3), num_dashes=60)
    both = ax.plot(both_open, x_range=[-3, 3], color=TEAL, stroke_width=5)
    return a, b, sm, both


def legend_item(text, color, dashed=False, x=0.0, y=0.0, width=4):
    ln = Line([x, y, 0], [x + 0.5, y, 0], color=color, stroke_width=width)
    if dashed:
        ln = DashedLine([x, y, 0], [x + 0.5, y, 0], color=color, stroke_width=width, dash_length=0.1)
    return VGroup(ln, T(text, 22, color).next_to(ln, RIGHT, buff=0.15))


def legends():
    return (legend_item("one slit open (each)", MUTED, x=-0.6, y=2.35, width=3),
            legend_item("both open, if chances added", INK, True, x=-0.6, y=1.85, width=3),
            legend_item("both open, measured", TEAL, x=3.9, y=2.35, width=5))


@slide("Now fire electrons at a barrier with two narrow", "Electrons through two slits")
def slits1(s):
    rig, scr = two_slit_rig()
    yield [FadeIn(rig)]
    yield [FadeIn(scr), FadeIn(lab("count where they land", 24, INK).move_to([2.4, 1.6, 0]))]
    d = screen_dots(5, seed=3)
    yield [LaggedStart(*[FadeIn(x, scale=2) for x in d], lag_ratio=0.4),
           FadeIn(lab("each electron: a single dot", 24, BLUE).move_to([2.4, 0.9, 0]))]


def even_dots(n, seed=6):
    """A few arrivals spread over the screen with no pattern yet."""
    rng = np.random.default_rng(seed)
    return VGroup(*[Dot([SCREEN_X + 0.16 + rng.uniform(0, 0.25), y, 0], radius=0.045, color=BLUE)
                    for y in np.linspace(-1.7, 2.1, n) + rng.uniform(-0.08, 0.08, n)])


def three_ways():
    items = ["only the first slit open", "only the second slit open", "both slits open"]
    return VGroup(*[left_at(VGroup(num_pill(k + 1), T(t, 26, INK)).arrange(RIGHT, buff=0.2), 0.0, 1.9 - 0.65 * k) for k, t in enumerate(items)])


@slide("Run it three ways, with only the first", "Electrons through two slits")
def slits2(s):
    rig, scr = two_slit_rig()
    s.add(rig, scr, screen_dots(5, seed=3))
    yield [LaggedStart(*[FadeIn(r, shift=RIGHT * 0.15) for r in three_ways()], lag_ratio=0.3)]
    yield [FadeIn(left_at(T("1961: Claus Jönsson, first with electrons", 24, INK), 0.0, -0.6))]
    yield [FadeIn(even_dots(20)),
           FadeIn(left_at(words("1989: Akira Tonomura's group watches the pattern build up one electron at a time", 46, 24, INK), 0.0, -1.55))]
    yield [FadeIn(left_at(T("using a device that acts like a pair of slits", 24, MUTED), 0.0, -2.45))]


def expect_base(s, stage):
    rig, scr = two_slit_rig()
    ax, names = count_axes()
    a, b, sm, both = curves(ax)
    la, ls, lb = legends()
    s.add(rig, scr, ax, names)
    if stage >= 1:
        s.add(a, b, sm, la, ls)
    return ax, (a, b, sm, both), (la, ls, lb)


@slide("First, what should we expect?", "What to expect")
def expect1(s):
    rig, scr = two_slit_rig()
    s.add(rig, scr)
    ax, names = count_axes()
    a, b, sm, both = curves(ax)
    la, ls, lb = legends()
    yield [Create(ax), FadeIn(names)]
    routes = VGroup(*[Line([BARRIER_X, y, 0], [SCREEN_X, 0.75, 0], color=BLUE, stroke_width=3) for y in SLIT_Y])
    note = lab("each electron through one slit or the other?", 22, INK).move_to([-4.4, 2.6, 0])
    yield [Create(routes), FadeIn(note)]
    yield [Create(a), FadeIn(la)]
    yield [Create(b), Create(sm), FadeIn(ls), FadeIn(at(T("chance = through first + through second", 24, INK), 2.9, -2.95))]


@slide("Chances are never negative.", "What to expect")
def expect2(s):
    ax, (a, b, sm, both), (la, ls, lb) = expect_base(s, 1)
    s.add(at(T("chance = through first + through second", 24, INK), 2.9, -2.95))
    yield [FadeIn(at(T("chances are never negative", 24, INK, True), -4.6, -2.9))]
    ups = VGroup(*[Arrow(ax.c2p(u, one_slit(u)), ax.c2p(u, one_slit(u) + two_slit(u)), buff=0.03, color=ORANGE,
                         stroke_width=4, tip_length=0.14, max_tip_length_to_length_ratio=0.4) for u in (-1.6, -0.75, 0.6, 1.5)])
    yield [LaggedStart(*[GrowArrow(u) for u in ups], lag_ratio=0.2),
           FadeIn(left_at(T("so opening the second slit can only add", 22, ORANGE), -7.1, -3.45))]


@slide("That's not what happens.", "What happens")
def stripes(s):
    ax, (a, b, sm, both), (la, ls, lb) = expect_base(s, 1)
    yield [FadeIn(lb), FadeIn(screen_dots(160, seed=5))]
    yield [Create(both)]
    dark = -np.pi / 4.2
    pt = ax.c2p(dark, both_open(dark))
    note = T("almost zero here, though each slit alone sends plenty", 22, INK).move_to([2.4, -3.1, 0])
    yield [FadeIn(Dot(pt, radius=0.08, color=INK)), GrowArrow(arrow([pt[0] - 0.9, -2.95, 0], pt + DOWN * 0.05, color=INK)),
           FadeIn(note), sm.animate.set_color(RED), ls[0].animate.set_color(RED), ls[1].animate.set_color(RED)]


MINI_SRC = np.array([-6.9, -0.4, 0])
MINI_BX, MINI_SX = -5.6, -3.9
BRIGHT_Y, DARK_Y = 1.2, -1.2


def mini_rig():
    bars = VGroup(*[Line([MINI_BX, a, 0], [MINI_BX, b, 0], color=INK, stroke_width=5) for a, b in ((-2.6, -1.0), (-0.75, -0.05), (0.2, 1.8))])
    k = PI / (BRIGHT_Y - DARK_Y)
    stripes_ = VGroup(*[Rectangle(width=0.22, height=0.3, stroke_width=0, fill_color=stripe_color((np.cos(k * (y - BRIGHT_Y)) + 1) / 2),
                                  fill_opacity=1).move_to([MINI_SX + 0.16, y, 0])
                        for y in np.arange(-2.4, 1.85, 0.3)])
    feeds = VGroup(*[DashedLine(MINI_SRC, [MINI_BX, sy, 0], color=MUTED, stroke_width=2) for sy in (0.075, -0.875)])
    g = VGroup(Dot(MINI_SRC, radius=0.09, color=INK), feeds, bars, Line([MINI_SX, -2.6, 0], [MINI_SX, 1.8, 0], color=MUTED, stroke_width=5),
               stripes_, lab("screen", 22).move_to([MINI_SX, -2.95, 0]))
    return g


def mini_routes(y):
    return VGroup(*[Line([MINI_BX, sy, 0], [MINI_SX, y, 0], color=BLUE, stroke_width=3) for sy in (0.075, -0.875)])


def polar(r, deg):
    return r * np.array([np.cos(np.radians(deg)), np.sin(np.radians(deg)), 0])


AMP_X = dict(a=-1.6, plus=-0.45, b=0.05, eq=1.25, s=1.75, bar=5.4)


def amp_row(y, b_deg, name):
    """Two route amplitudes, their sum and its chance, for one spot on the screen."""
    kw = dict(buff=0, stroke_width=5, tip_length=0.17, max_tip_length_to_length_ratio=0.35)
    a = polar(0.8, 25)
    b = polar(0.8, b_deg)
    tot = a + b
    o1, o2, o3 = (np.array([AMP_X[k] + w, y, 0]) - v / 2 for k, w, v in (("a", 0.4, a), ("b", 0.4, b), ("s", 0.75, tot)))
    first = VGroup(Dot(o1, radius=0.05, color=INK), Arrow(o1, o1 + a, color=BLUE, **kw), lab("via first", 22, BLUE).move_to([AMP_X["a"] + 0.4, y - 0.62, 0]))
    second = VGroup(Dot(o2, radius=0.05, color=INK), Arrow(o2, o2 + b, color=BLUE, **kw), lab("via second", 22, BLUE).move_to([AMP_X["b"] + 0.45, y - 0.62, 0]))
    if np.linalg.norm(tot) > 0.2:
        sm = VGroup(Dot(o3, radius=0.05, color=INK), Arrow(o3, o3 + tot, color=BLUE, **kw))
    else:
        sm = VGroup(Dot(o3, radius=0.09, color=INK), lab("0", 26, INK, True).next_to(o3, UR, buff=0.08))
    signs = VGroup(at(T("+", 34, INK), AMP_X["plus"], y), at(T("=", 34, INK), AMP_X["eq"], y))
    frac = (np.linalg.norm(tot) / 1.6) ** 2
    ch = bar(AMP_X["bar"], y - 0.55, frac, hmax=1.0, w=0.9, label="chance ≈ 0" if frac < 0.05 else "large chance", size=22)
    sq = Arrow([AMP_X["s"] + 1.55, y, 0], [AMP_X["bar"] - 0.7, y, 0], buff=0, color=TEAL, stroke_width=4, tip_length=0.15)
    tag = lab(name, 22, INK, True).move_to([-2.5, y + 0.75, 0])
    return dict(first=first, second=second, signs=signs, sum=sm, sq=sq, chance=ch, tag=tag)


def amp_heads(k):
    return [at(T("add the amplitudes first", 24, INK, True), 0.0, 2.45),
            at(T("then square the size", 24, TEAL, True), AMP_X["bar"], 2.45)][k]


def needed():
    return at(T("needed: numbers that can cancel when added", 26, INK, True), 0.4, -3.65)


def route_note():
    return left_at(T("each route: a complex amplitude", 22, BLUE), -7.0, 2.4)


@slide("So the theory needs numbers that can cancel", "Amplitudes that can cancel")
def amps1(s):
    s.add(mini_rig())
    yield [FadeIn(needed())]
    r = amp_row(BRIGHT_Y, 50, "bright spot")
    yield [Create(mini_routes(BRIGHT_Y)), FadeIn(r["first"]), FadeIn(r["second"]), FadeIn(r["tag"]), FadeIn(route_note())]
    yield [FadeIn(r["signs"]), FadeIn(r["sum"]), FadeIn(amp_heads(0))]


@slide("Then it squares the size of the sum", "Amplitudes that can cancel")
def amps2(s):
    nd = needed()
    r = amp_row(BRIGHT_Y, 50, "bright spot")
    s.add(mini_rig(), mini_routes(BRIGHT_Y), nd, amp_heads(0), route_note(), *[r[k] for k in ("first", "second", "signs", "sum", "tag")])
    yield [GrowArrow(r["sq"]), FadeIn(r["chance"]), FadeIn(amp_heads(1))]
    d = amp_row(DARK_Y, 205, "dark spot")
    yield [Create(mini_routes(DARK_Y)), *[FadeIn(d[k]) for k in ("first", "second", "signs", "sum", "tag", "chance")], GrowArrow(d["sq"]),
           FadeIn(lab("opposite arrows cancel", 22, BLUE).move_to([-0.6, DARK_Y - 1.1, 0]))]
    yield [FadeOut(nd), FadeIn(at(pill("interference: add first, then square", BLUE, 26), 0.4, -3.65))]


@slide("So outcomes are random, and their chances", "What the experiments force")
def exp_summary(s):
    a = at(card("outcomes are random,\nso the theory predicts chances", 6.6, 1.5, TEAL, 28), -3.6, 1.0)
    b = at(card("the chances come from\namplitudes that can cancel", 6.6, 1.5, BLUE, 28), 3.6, 1.0)
    yield [FadeIn(a, shift=UP * 0.15), FadeIn(b, shift=UP * 0.15)]
    nxt = at(card("next: build a state out of amplitudes,\nusing the silver atom's spin", 8.0, 1.5, INK, 28), 0, -1.6)
    yield [FadeIn(nxt, shift=UP * 0.15), GrowArrow(arrow(a.get_bottom(), nxt.get_top() + LEFT * 1.5)),
           GrowArrow(arrow(b.get_bottom(), nxt.get_top() + RIGHT * 1.5))]


# ------------------------------------------------------------------ a state is a list of amplitudes
deck.part("A state is a list of amplitudes")


def spin_icon(c, up=True, r=0.42, color=BLUE):
    c = np.array([c[0], c[1], 0.0])
    d = UP if up else DOWN
    return VGroup(Circle(radius=r, color=color, stroke_width=3).move_to(c),
                  Arrow(c - d * r * 0.75, c + d * r * 0.85, buff=0, color=color, stroke_width=6, tip_length=0.16))


def field_lines(x0=-6.6, x1=-3.4, y0=-2.6, y1=1.9, n=5):
    return VGroup(*[Arrow([x, y0, 0], [x, y1, 0], buff=0, color=LINE, stroke_width=3, tip_length=0.18) for x in np.linspace(x0, x1, n)])


@slide("A state is a list of amplitudes.", "Spin up and spin down")
def spin1(s):
    fl = field_lines()
    yield [LaggedStart(*[GrowArrow(a) for a in fl], lag_ratio=0.1), FadeIn(lab("vertical magnetic field", 24).move_to([-5.0, 2.35, 0]))]
    atom = VGroup(Circle(radius=0.55, color=BLUE, stroke_width=3, fill_color=WHITE, fill_opacity=1).move_to([-5.0, -0.35, 0]),
                  left_at(lab("silver atom", 24, BLUE), -3.1, -0.35))
    yield [FadeIn(atom, scale=0.8)]
    u, d = spin_icon([0.6, 0.3], True, 0.6), spin_icon([4.2, 0.3], False, 0.6)
    yield [FadeIn(u), FadeIn(d), FadeIn(at(T("up", 30, BLUE, True), 0.6, -0.75)), FadeIn(at(T("down", 30, BLUE, True), 4.2, -0.75)),
           FadeIn(at(T("two orientations along the field", 26, INK), 2.4, 1.7))]


@slide("A compass needle's energy depends", "Two slightly different energies")
def spin2(s):
    c = np.array([-4.2, 0.0, 0])
    fl = field_lines(-6.4, -2.0, -2.4, 1.9, 4)
    ang = 0.6
    tipv = np.array([-np.sin(ang), np.cos(ang), 0])
    side = np.array([np.cos(ang), np.sin(ang), 0]) * 0.17
    needle = VGroup(Polygon(c + tipv * 1.3, c + side, c - side, color=ORANGE, fill_color=ORANGE, fill_opacity=0.85, stroke_width=1),
                    Polygon(c - tipv * 1.3, c + side, c - side, color=MUTED, fill_color=MUTED, fill_opacity=0.6, stroke_width=1),
                    Dot(c, radius=0.07, color=INK))
    arc = Arc(radius=0.9, start_angle=PI / 2, angle=ang, arc_center=c, color=ORANGE, stroke_width=4)
    yield [FadeIn(fl), FadeIn(needle), Create(arc), FadeIn(lab("angle", 22, ORANGE).move_to(c + [-0.6, 1.25, 0])),
           FadeIn(words("a compass needle: its energy depends on its angle to the field", 24, 24, INK).move_to([-4.2, -2.95, 0]))]
    lo = Line([1.6, -1.2, 0], [4.6, -1.2, 0], color=BLUE, stroke_width=5)
    hi = Line([1.6, -0.75, 0], [4.6, -0.75, 0], color=BLUE, stroke_width=5)
    en = Arrow([0.9, -2.2, 0], [0.9, 1.6, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.18)
    yield [GrowArrow(en), FadeIn(lab("energy", 22).next_to(en, UP, buff=0.1)), Create(lo), Create(hi),
           FadeIn(spin_icon([5.3, -1.35], True, 0.25)), FadeIn(spin_icon([5.3, -0.6], False, 0.25)),
           FadeIn(lab("up", 22, BLUE).move_to([6.0, -1.35, 0])), FadeIn(lab("down", 22, BLUE).move_to([6.15, -0.6, 0])),
           FadeIn(words("the spin's two orientations: slightly different energies", 22, 24, INK).move_to([3.4, 0.9, 0]))]


def amp_column(x=-0.6, y=0.0, up=(0.5, 0.85), down=(2.3, 0.55)):
    rows = VGroup(VGroup(T("up", 28, INK), phasor([0, 0], up[0], up[1], r=0.55, width=5)).arrange(RIGHT, buff=0.35),
                  VGroup(T("down", 28, INK), phasor([0, 0], down[0], down[1], r=0.55, width=5)).arrange(RIGHT, buff=0.35)).arrange(DOWN, buff=0.35, aligned_edge=RIGHT)
    rows.move_to([x, y, 0])
    h = rows.height + 0.3
    l, r = rows.get_left()[0] - 0.2, rows.get_right()[0] + 0.2
    lb = VMobject(color=BLUE, stroke_width=3).set_points_as_corners([[l + 0.15, y + h / 2, 0], [l, y + h / 2, 0], [l, y - h / 2, 0], [l + 0.15, y - h / 2, 0]])
    rb = VMobject(color=BLUE, stroke_width=3).set_points_as_corners([[r - 0.15, y + h / 2, 0], [r, y + h / 2, 0], [r, y - h / 2, 0], [r - 0.15, y - h / 2, 0]])
    return VGroup(lb, rb, rows)


@slide("A general state mixes the two.", "A state: two complex amplitudes")
def spin3(s):
    u, d = spin_icon([-5.6, 1.5], True, 0.4), spin_icon([-3.2, 1.5], False, 0.4)
    yield [FadeIn(u), FadeIn(d), FadeIn(at(T("+", 34, INK), -4.4, 1.5)), FadeIn(lab("a general state mixes up and down", 24, INK).move_to([-4.4, 0.65, 0]))]
    col = amp_column(1.6, 0.6)
    yield [FadeIn(col), FadeIn(at(T("state =", 30, BLUE, True), -0.6, 0.6)),
           FadeIn(left_at(words("two complex numbers, one for up and one for down", 22, 24, INK), 3.3, 0.6))]
    yield [FadeIn(at(T("its amplitudes", 32, BLUE, True), 1.6, -1.2)), Indicate(col[2], color=BLUE)]
    yield [FadeIn(caption("A complex number has a size and a direction, so it is drawn as an arrow.", y=-2.6, color=MUTED, size=24))]


def born_rows():
    r1 = VGroup(T("chance of up", 28, TEAL, True), T("=", 28), eq("|up amplitude|²", 30, BLUE)).arrange(RIGHT, buff=0.25)
    r2 = VGroup(T("chance of down", 28, TEAL, True), T("=", 28), eq("|down amplitude|²", 30, BLUE)).arrange(RIGHT, buff=0.25)
    left_at(r1, -1.4, 1.4)
    left_at(r2, -1.4, 0.3)
    key = left_at(lab("|…|²: the squared size", 22), -1.4, -0.4)
    return r1, r2, key


def born_magnet():
    m = magnet("vertical", -5.2, 0.85, w=2.0)
    a = Arrow([-4.1, 0.85, 0], [-3.0, 1.45, 0], buff=0, color=INK, stroke_width=4, tip_length=0.15)
    b = Arrow([-4.1, 0.85, 0], [-3.0, 0.25, 0], buff=0, color=INK, stroke_width=4, tip_length=0.15)
    return VGroup(m, a, b, lab("up", 22, INK).next_to(a.get_end(), UP, buff=0.05), lab("down", 22, INK).next_to(b.get_end(), DOWN, buff=0.05))


@slide("Measure it with a vertical magnet.", "The Born rule")
def born1(s):
    r1, r2, key = born_rows()
    yield [FadeIn(born_magnet())]
    yield [FadeIn(r1), FadeIn(key)]
    yield [FadeIn(r2)]


@slide("This is called the Born rule.", "The Born rule")
def born2(s):
    r1, r2, key = born_rows()
    s.add(born_magnet(), r1, r2, key)
    box = SurroundingRectangle(VGroup(r1, r2), color=TEAL, buff=0.25, corner_radius=0.12)
    yield [Create(box), FadeIn(pill("the Born rule", TEAL, 26).next_to(box, UP, buff=0.15).align_to(box, RIGHT))]
    tot = at(VGroup(eq("chance of up + chance of down = 1", 28, TEAL), eq("|up amplitude|² + |down amplitude|² = 1", 28, BLUE)).arrange(DOWN, buff=0.3), 0, -2.3)
    yield [FadeIn(tot[0])]
    yield [FadeIn(tot[1])]


def prep_row(tilt=None, y=0.9):
    d = dial([-5.6, y], tilt if tilt is not None else 50, name="first magnet, tilted", r=0.85)
    k = slot_arrow([-4.5, y, 0], [-2.9, y, 0])
    kl = lab("keep up", 22, INK).next_to(k, UP, buff=0.08)
    v = magnet("vertical", -1.6, y, w=2.1)
    o = slot_arrow([-0.5, y, 0], [0.6, y, 0])
    f = left_at(VGroup(T("chance of up =", 26, TEAL, True), eq("cos²(tilt / 2)", 28, TEAL)).arrange(RIGHT, buff=0.2), 0.8, y)
    return d, VGroup(k, kl), v, o, f


@slide("Here's how to prepare a state.", "Preparing a state")
def prep1(s):
    d, k, v, o, f = prep_row()
    yield [FadeIn(at(lab("prepare atoms, then measure them", 24, INK), 0, 2.4))]
    yield [FadeIn(d), FadeIn(k), FadeIn(lab("tilt", 22, ORANGE).move_to([-5.15, 1.45, 0]))]
    yield [FadeIn(v)]
    yield [GrowArrow(o), FadeIn(f), FadeIn(lab("found by experiment", 22).next_to(f, DOWN, buff=0.15))]


def cos_chart():
    ax = Axes(x_range=[0, 180, 90], y_range=[0, 1, 0.5], x_length=8.4, y_length=2.0, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([0.2, -2.15, 0])
    names = VGroup(lab("tilt of the first magnet", 22).next_to(ax.x_axis, DOWN, buff=0.45),
                   lab("chance of up", 22, TEAL).next_to(ax.y_axis, LEFT, buff=0.2))
    for v in (0, 90, 180):
        names.add(lab(f"{v}°", 22).next_to(ax.c2p(v, 0), DOWN, buff=0.12))
    return ax, names


CHART_PTS = [(0, 1.0, "no tilt: all of them", UR), (90, 0.5, "90°: half, as in the magnet rows", UR), (180, 0.0, "upside down: none", UR)]


def chart_point(ax, k):
    t, v, text, side = CHART_PTS[k]
    d = Dot(ax.c2p(t, v), radius=0.09, color=TEAL)
    return VGroup(d, T(text, 22, INK).next_to(d, side, buff=0.12))


def prep_done(s, with_label=True):
    d, k, v, o, f = prep_row()
    s.add(d, k, v, o, f, lab("tilt", 22, ORANGE).move_to([-5.15, 1.45, 0]))
    if with_label:
        s.add(lab("found by experiment", 22).next_to(f, DOWN, buff=0.15))


@slide("With no tilt, that's all of them.", "Preparing a state")
def prep2(s):
    prep_done(s)
    ax, names = cos_chart()
    yield [Create(ax), FadeIn(names), FadeIn(chart_point(ax, 0))]
    yield [FadeIn(chart_point(ax, 1))]
    yield [FadeIn(chart_point(ax, 2)), Create(ax.plot(lambda t: np.cos(np.radians(t) / 2) ** 2, x_range=[0, 180], color=TEAL, stroke_width=4))]


@slide("So we choose the amplitudes to be the cosine", "Choosing the amplitudes")
def prep3(s):
    prep_done(s)
    a = left_at(VGroup(T("up amplitude", 28, BLUE, True), eq("= cos(tilt / 2)", 30, BLUE)).arrange(RIGHT, buff=0.25), -6.6, -1.0)
    b = left_at(VGroup(T("down amplitude", 28, BLUE, True), eq("= sin(tilt / 2)", 30, BLUE)).arrange(RIGHT, buff=0.25), -6.6, -1.8)
    yield [FadeIn(a), FadeIn(b), FadeIn(lab("their squares: cos² for up, sin² for down", 22, TEAL).move_to([-3.4, -2.5, 0]))]
    dl = dial([2.4, -1.6], -90, r=0.8, name="90° to the left")
    yield [FadeIn(dl), FadeIn(left_at(words("tilt to the left: the down amplitude flips sign", 24, 24, INK), 3.5, -1.6))]


RUN_O = np.array([-2.7, -2.55, 0])
RUN_R = 3.5


def run_dial():
    return VGroup(dial([-5.7, 1.35], 60, r=0.85), lab("first magnet: 60° to the right", 22).move_to([-5.0, 0.2, 0]))


def run_parts():
    plane = spin_plane(RUN_O, RUN_R)
    c, sn = np.cos(PI / 6), np.sin(PI / 6)
    arr = state_arrow(RUN_O, RUN_R, c, sn)
    tip = RUN_O + RUN_R * np.array([c, sn, 0])
    half = VGroup(Arc(radius=1.1, start_angle=0, angle=PI / 6, arc_center=RUN_O, color=ORANGE, stroke_width=4),
                  T("30°", 24, ORANGE).move_to(RUN_O + 1.45 * np.array([np.cos(PI / 12), np.sin(PI / 12), 0])))
    upc = VGroup(DashedLine(tip, [tip[0], RUN_O[1], 0], color=BLUE, stroke_width=3),
                 T("0.866", 26, BLUE, True).move_to([RUN_O[0] + RUN_R * c / 2, RUN_O[1] - 0.35, 0]))
    dnc = VGroup(DashedLine(tip, [RUN_O[0], tip[1], 0], color=BLUE, stroke_width=3),
                 T("1/2", 26, BLUE, True).move_to([RUN_O[0] - 0.4, RUN_O[1] + RUN_R * sn / 2, 0]))
    return plane, arr, half, upc, dnc


def run_eqs():
    a = left_at(eq("up amplitude   = cos 30° ≈ 0.866", 26, BLUE), 1.4, 2.2)
    b = left_at(eq("down amplitude = sin 30° = 1/2", 26, BLUE), 1.4, 1.6)
    return a, b


def run_bars():
    base = RUN_O[1]
    b1 = bar(3.4, base, 0.75, hmax=2.6, w=1.1, label="75%")
    b2 = bar(5.6, base, 0.25, hmax=2.6, w=1.1, label="25%")
    names = VGroup(lab("up", 24, INK).move_to([3.4, base - 0.3, 0]), lab("down", 24, INK).move_to([5.6, base - 0.3, 0]),
                   Line([2.6, base, 0], [6.4, base, 0], color=LINE, stroke_width=2))
    return b1, b2, names


@slide("Our running example is a tilt of sixty degrees", "The running example: 60° to the right")
def run1(s):
    plane, arr, half, upc, dnc = run_parts()
    a, b = run_eqs()
    yield [FadeIn(run_dial()), Create(plane)]
    yield [GrowArrow(arr), Create(half[0]), FadeIn(half[1]), FadeIn(lab("half of 60° is 30°", 24, ORANGE).move_to([-0.2, 0.2, 0]))]
    yield [Create(upc[0]), FadeIn(upc[1]), FadeIn(a)]


@slide("The down amplitude is the sine, one half.", "The running example: 60° to the right")
def run2(s):
    plane, arr, half, upc, dnc = run_parts()
    a, b = run_eqs()
    s.add(run_dial(), plane, arr, half, upc, a, lab("half of 60° is 30°", 24, ORANGE).move_to([-0.2, 0.2, 0]))
    yield [Create(dnc[0]), FadeIn(dnc[1]), FadeIn(b)]
    b1, b2, names = run_bars()
    yield [FadeIn(names), GrowFromEdge(b1[0], DOWN), FadeIn(b1[1]), GrowFromEdge(b2[0], DOWN), FadeIn(b2[1]),
           FadeIn(at(eq("0.866² = 0.75,  (1/2)² = 0.25", 24, TEAL), 4.5, -3.4))]


def side_magnet():
    m = magnet("sideways", -5.2, 1.0, w=2.1, color=ORANGE)
    a = Arrow([-4.1, 1.0, 0], [-3.0, 1.55, 0], buff=0, color=INK, stroke_width=4, tip_length=0.15)
    b = Arrow([-4.1, 1.0, 0], [-3.0, 0.45, 0], buff=0, color=INK, stroke_width=4, tip_length=0.15)
    return VGroup(m, a, b, lab("right", 22, INK).next_to(a.get_end(), RIGHT, buff=0.08), lab("left", 22, INK).next_to(b.get_end(), RIGHT, buff=0.08))


def side_dials():
    r = VGroup(dial([-5.6, -1.6], 90, r=0.75), VGroup(lab("tilted 90° right", 22, INK), lab("certain: right", 22, INK)).arrange(DOWN, buff=0.06).move_to([-5.6, -2.95, 0]))
    l = VGroup(dial([-2.4, -1.6], -90, r=0.75), VGroup(lab("tilted 90° left", 22, INK), lab("certain: left", 22, INK)).arrange(DOWN, buff=0.06).move_to([-2.4, -2.95, 0]))
    return r, l


@slide("Amplitudes can be complex, and their phase", "A sideways magnet")
def side1(s):
    yield [FadeIn(at(words("Complex amplitudes have a phase, and it can matter even when the up and down chances stay the same.",
                           64, 24, INK, align=ORIGIN), 0, 2.3))]
    yield [FadeIn(side_magnet())]
    yield [FadeIn(lab("each result has a state that gives it for certain", 22, INK).move_to([-4.0, -0.35, 0]))]
    r, l = side_dials()
    yield [FadeIn(r), FadeIn(l)]


SIDE_O = np.array([2.4, -1.0, 0])
SIDE_R = 2.0


def side_base(s):
    s.add(at(words("Complex amplitudes have a phase, and it can matter even when the up and down chances stay the same.",
                   64, 24, INK, align=ORIGIN), 0, 2.3), side_magnet(), lab("each result has a state that gives it for certain", 22, INK).move_to([-4.0, -0.35, 0]))
    s.add(*side_dials())


@slide("Right has both amplitudes equal,", "The sideways states")
def side2(s):
    side_base(s)
    plane = spin_plane(SIDE_O, SIDE_R, neg=True)
    k = 1 / np.sqrt(2)
    ra = state_arrow(SIDE_O, SIDE_R, k, k, BLUE)
    la = state_arrow(SIDE_O, SIDE_R, k, -k, BLUE)
    yield [Create(plane), GrowArrow(ra), FadeIn(left_at(eq("right: (1/√2, 1/√2)", 24, BLUE), SIDE_O[0] + 1.2, SIDE_O[1] + 1.95))]
    yield [GrowArrow(la), FadeIn(left_at(eq("left: (1/√2, −1/√2)", 24, BLUE), SIDE_O[0] + 1.2, SIDE_O[1] - 1.95)),
           FadeIn(at(lab("amplitudes, not directions in space", 22, MUTED), SIDE_O[0] + 1.2, -3.6))]


RW_O = np.array([-4.6, -0.8, 0])
RW_R = 2.4


def rewrite_plane():
    plane = spin_plane(RW_O, RW_R, neg=True, size=22)
    k = 1 / np.sqrt(2)
    axes = VGroup(DashedLine(RW_O - RW_R * 0.8 * np.array([k, k, 0]), RW_O + RW_R * 1.15 * np.array([k, k, 0]), color=MUTED, stroke_width=3),
                  DashedLine(RW_O - RW_R * 0.5 * np.array([k, -k, 0]), RW_O + RW_R * 1.0 * np.array([k, -k, 0]), color=MUTED, stroke_width=3))
    names = VGroup(lab("right", 22, MUTED).move_to(RW_O + RW_R * 1.25 * np.array([k, k, 0])),
                   lab("left", 22, MUTED).move_to(RW_O + RW_R * 1.1 * np.array([k, -k, 0]) + RIGHT * 0.3))
    st = state_arrow(RW_O, RW_R, np.cos(PI / 6), np.sin(PI / 6))
    return plane, axes, names, st


def rewrite_eqs():
    a = left_at(eq("right amplitude = (up + down) / √2", 28, BLUE), -1.0, 1.9)
    b = left_at(eq("left amplitude  = (up − down) / √2", 28, BLUE), -1.0, 1.1)
    return a, b


@slide("To get the sideways chances, rewrite the state", "Rewriting the state in right and left")
def rewrite1(s):
    plane, axes, names, st = rewrite_plane()
    yield [Create(plane), GrowArrow(st), Create(axes), FadeIn(names), FadeIn(lab("our state, measured along right and left", 22).move_to([-4.6, -3.55, 0]))]
    a, b = rewrite_eqs()
    yield [FadeIn(a), FadeIn(lab("up, down: the two amplitudes", 22).move_to([2.6, 2.55, 0]))]
    yield [FadeIn(b)]


def cross_rows():
    r = VGroup(eq("|up + down|²", 28, TEAL), eq("=", 28), eq("|up|² + |down|²", 28, INK)).arrange(RIGHT, buff=0.2)
    left_at(r, -1.0, -0.2)
    r.add(eq("+ cross term", 28, ORANGE).next_to(r, DOWN, buff=0.3).align_to(r[2], LEFT))
    return r


@slide("Squaring a sum gives the two squares,", "Rewriting the state in right and left")
def rewrite2(s):
    plane, axes, names, st = rewrite_plane()
    a, b = rewrite_eqs()
    s.add(plane, axes, names, st, a, b, lab("our state, measured along right and left", 22).move_to([-4.6, -3.55, 0]),
          lab("up, down: the two amplitudes", 22).move_to([2.6, 2.55, 0]))
    r = cross_rows()
    yield [FadeIn(r)]
    br = Brace(r[3], DOWN, color=ORANGE)
    yield [FadeIn(br), FadeIn(words("mixes the two amplitudes: interference lives here", 24, 24, ORANGE, align=ORIGIN).next_to(br, DOWN, buff=0.15))]


@slide("For our atoms, both amplitudes are positive.", "The cross term for our atoms")
def right_left(s):
    a = left_at(eq("up = 0.866,  down = 1/2: both positive", 26, BLUE), -6.8, 2.2)
    yield [FadeIn(a)]
    yield [FadeIn(left_at(eq("cross term = 2 × 0.866 × 1/2 = 0.866", 24, ORANGE), -6.8, 1.55)),
           FadeIn(left_at(lab("it helps on the right and hurts on the left", 22, ORANGE), -6.8, 1.1)),
           FadeIn(left_at(eq("right: (1 + cross term) / 2", 26, INK), -6.8, 0.45)),
           FadeIn(left_at(eq("left:  (1 − cross term) / 2", 26, INK), -6.8, -0.15))]
    base = -2.9
    b1 = bar(-4.6, base, 0.933, hmax=1.5, w=1.1, label="93.3%")
    b2 = bar(-2.4, base, 0.067, hmax=1.5, w=1.1, label="6.7%")
    names = VGroup(lab("right", 24, INK).move_to([-4.6, base - 0.3, 0]), lab("left", 24, INK).move_to([-2.4, base - 0.3, 0]),
                   Line([-5.6, base, 0], [-1.4, base, 0], color=LINE, stroke_width=2))
    yield [FadeIn(names), GrowFromEdge(b1[0], DOWN), FadeIn(b1[1]), GrowFromEdge(b2[0], DOWN), FadeIn(b2[1]),
           FadeIn(left_at(eq("= 93.3%", 26, TEAL), -1.1, 0.45)), FadeIn(left_at(eq("= 6.7%", 26, TEAL), -1.1, -0.15))]
    k = PI / 1.2
    stripes_ = VGroup(*[Rectangle(width=0.32, height=1.6, stroke_width=0, fill_color=stripe_color((np.cos(k * x) + 1) / 2),
                                  fill_opacity=1).move_to([3.9 + x, -2.3, 0]) for x in np.arange(-1.8, 1.85, 0.3)])
    yield [FadeIn(stripes_), FadeIn(at(words("the near-cancellation on the left is what makes the dark stripes", 36, 24, INK, align=ORIGIN), 3.9, -0.75)),
           GrowArrow(arrow(b2[1].get_right() + RIGHT * 0.1, stripes_.get_left() + LEFT * 0.1 + UP * 0.2, color=MUTED))]


@slide("The cosine squared rule agrees.", "The tilt rule agrees")
def tilt_check(s):
    c = np.array([-3.8, -0.9, 0])
    r = 2.2
    base = VGroup(Circle(radius=r, color=LINE, stroke_width=2).move_to(c), DashedLine(c, c + UP * r, color=MUTED, stroke_width=2),
                  lab("vertical", 22).move_to(c + UP * (r + 0.3)))
    yield [FadeIn(base), FadeIn(at(T("chance = cos²(half the angle between the magnets)", 26, TEAL), 2.4, 2.3))]
    first = Arrow(c, c + r * np.array([np.sin(PI / 3), np.cos(PI / 3), 0]), buff=0, color=BLUE, stroke_width=6, tip_length=0.2)
    side = Arrow(c, c + r * RIGHT, buff=0, color=ORANGE, stroke_width=6, tip_length=0.2)
    yield [GrowArrow(first), GrowArrow(side), FadeIn(lab("first magnet: 60°", 22, BLUE).next_to(first.get_end(), UR, buff=0.08)),
           FadeIn(lab("sideways: 90°", 22, ORANGE).next_to(side.get_end(), DOWN, buff=0.15))]
    gap = Arc(radius=1.3, start_angle=0, angle=PI / 6, arc_center=c, color=ORANGE, stroke_width=5)
    yield [Create(gap), FadeIn(T("30° apart", 24, ORANGE, True).move_to(c + 1.75 * np.array([np.cos(PI / 12), np.sin(PI / 12), 0]) + RIGHT * 0.55))]
    res = left_at(VGroup(eq("half: 15°,  cos² 15° = 93.3%", 28, TEAL), check()).arrange(RIGHT, buff=0.3), 0.2, 0.0)
    yield [FadeIn(res)]


FRONT_O = np.array([-4.2, -0.9, 0])
U_UP = np.array([0, 1, 0])
U_RIGHT = np.array([1, 0, 0])
U_FRONT = np.array([-0.766, -0.643, 0])


def front_axes():
    L = 2.6
    g = VGroup(*[Arrow(FRONT_O, FRONT_O + u * L, buff=0, color=MUTED, stroke_width=3, tip_length=0.18) for u in (U_UP, U_RIGHT, U_FRONT)])
    g.add(lab("up", 22).next_to(g[0].get_end(), UP, buff=0.08), lab("right", 22).next_to(g[1].get_end(), RIGHT, buff=0.08),
          lab("front", 22).next_to(g[2].get_end(), DOWN, buff=0.08))
    return g


def tilt_vec(u, deg=60, L=2.2):
    t = np.radians(deg)
    return FRONT_O + L * (np.cos(t) * U_UP + np.sin(t) * u)


def right_tag():
    return words("60° toward the right", 11, 22, MUTED).next_to(tilt_vec(U_RIGHT), RIGHT, buff=0.1)


def drops():
    """Dashed lines from each tilted arrow's tip down to the horizontal plane, landing on its axis."""
    L, t = 2.2, np.radians(60)
    return VGroup(*[DashedLine(tilt_vec(u), FRONT_O + L * np.sin(t) * u, color=c, stroke_width=2)
                    for u, c in ((U_RIGHT, MUTED), (U_FRONT, BLUE))])


def front_tag():
    return words("60° toward the front", 11, 22, BLUE, align=RIGHT).move_to([-6.4, -0.45, 0])


@slide("Now a second experiment.", "Tilted toward the front")
def front1(s):
    yield [FadeIn(front_axes())]
    rt = Arrow(FRONT_O, tilt_vec(U_RIGHT), buff=0, color=MUTED, stroke_width=5, tip_length=0.18)
    ft = Arrow(FRONT_O, tilt_vec(U_FRONT), buff=0, color=BLUE, stroke_width=6, tip_length=0.2)
    yield [GrowArrow(rt), FadeIn(right_tag()), GrowArrow(ft), FadeIn(front_tag()), Create(drops())]
    arc = ParametricFunction(lambda t: FRONT_O + 1.3 * (np.cos(t) * U_RIGHT + np.sin(t) * U_FRONT), t_range=[0, PI / 2], color=ORANGE, stroke_width=4)
    yield [Create(arc), FadeIn(lab("a quarter turn", 22, ORANGE).move_to(FRONT_O + [0.95, -1.35, 0]))]


def front_done():
    return VGroup(front_axes(), Arrow(FRONT_O, tilt_vec(U_RIGHT), buff=0, color=MUTED, stroke_width=5, tip_length=0.18),
                  Arrow(FRONT_O, tilt_vec(U_FRONT), buff=0, color=BLUE, stroke_width=6, tip_length=0.2),
                  right_tag(), front_tag(), drops(),
                  ParametricFunction(lambda t: FRONT_O + 1.3 * (np.cos(t) * U_RIGHT + np.sin(t) * U_FRONT), t_range=[0, PI / 2], color=ORANGE, stroke_width=4),
                  lab("a quarter turn", 22, ORANGE).move_to(FRONT_O + [0.95, -1.35, 0]))


FX = 0.6  # left edge of the reasoning column


def front_lines():
    return [left_at(eq("vertical magnet: 75% up, as before", 24, TEAL), FX, 2.1),
            left_at(eq("so |down amplitude| = 1/2", 24, BLUE), FX, 1.45),
            left_at(eq("if real: down = +1/2 or −1/2", 24, RED), FX, 0.6),
            left_at(eq("then sideways: 93.3% right, or 6.7%", 24, RED), FX, -0.05),
            left_at(eq("measured: 50% right, 50% left", 26, TEAL), FX, -0.95)]


@slide("A vertical magnet still gives seventy-five percent up.", "Tilted toward the front")
def front2(s):
    s.add(front_done())
    ln = front_lines()
    yield [FadeIn(ln[0])]
    yield [FadeIn(ln[1])]


@slide("If amplitudes were real, it would be plus", "Tilted toward the front")
def front3(s):
    s.add(front_done())
    ln = front_lines()
    s.add(ln[0], ln[1])
    yield [FadeIn(ln[2])]
    yield [FadeIn(ln[3])]
    yield [FadeIn(ln[4]), Create(cross(VGroup(ln[2], ln[3]).copy().scale(1.02), RED, 4).set_opacity(0.7))]


@slide("The tilt rule agrees.", "Tilted toward the front")
def front4(s):
    s.add(front_done())
    ln = front_lines()
    s.add(ln[0], ln[1], ln[4])
    yield [FadeIn(left_at(eq("tilt rule: cos²(half the angle)", 24, TEAL), FX, 0.6))]
    yield [FadeIn(left_at(eq("front-tilted vs sideways: 90° apart", 24, INK), FX, -0.05)),
           Indicate(front_done()[2], color=BLUE)]
    yield [FadeIn(left_at(VGroup(eq("half: 45°,  cos² 45° = 1/2", 26, TEAL), check()).arrange(RIGHT, buff=0.3), FX, -1.85))]


def imag_lines():
    return [left_at(T("An even split needs the cross term to vanish.", 26, INK, True), -6.9, 2.1),
            left_at(eq("cross term = 2 × up × (real part of down)", 24, ORANGE), -6.9, 1.2),
            left_at(eq("up = 0.866: fixed and real", 24, BLUE), -6.9, 0.4),
            left_at(eq("so down has no real part", 24, BLUE), -6.9, -0.4)]


CP_O = np.array([3.6, -0.6, 0])
CP_U = 2.4  # length of a unit amplitude in the complex plane


def complex_plane():
    g = VGroup(Arrow(CP_O + LEFT * 1.0, CP_O + RIGHT * 2.9, buff=0, color=MUTED, stroke_width=3, tip_length=0.16),
               Arrow(CP_O + DOWN * 2.2, CP_O + UP * 2.2, buff=0, color=MUTED, stroke_width=3, tip_length=0.16))
    g.add(lab("real part", 22).next_to(g[0].get_end(), DOWN, buff=0.12).shift(LEFT * 0.4),
          lab("imaginary part", 22).next_to(g[1].get_end(), RIGHT, buff=0.12))
    return g


def cp_arrow(re, im, color=BLUE, width=6):
    return Arrow(CP_O, CP_O + CP_U * np.array([re, im, 0]), buff=0, color=color, stroke_width=width, tip_length=0.2)


@slide("An even split needs the cross term to vanish.", "Making the cross term vanish")
def imag1(s):
    ln = imag_lines()
    for l in ln:
        yield [FadeIn(l, shift=RIGHT * 0.1)]


@slide("So it's plus or minus i over two.", "The down amplitude has no real part")
def imag2(s):
    s.add(*imag_lines())
    cp = complex_plane()
    up = cp_arrow(0.866, 0)
    yield [FadeIn(cp), GrowArrow(up), FadeIn(lab("up: 0.866", 22, BLUE).next_to(up, DOWN, buff=0.12)),
           FadeIn(left_at(eq("down = + i/2 or − i/2", 26, BLUE), -6.9, -1.3))]
    dp, dm = cp_arrow(0, 0.5), cp_arrow(0, -0.5)
    sq = VMobject(color=INK, stroke_width=2).set_points_as_corners([CP_O + RIGHT * 0.25, CP_O + RIGHT * 0.25 + UP * 0.25, CP_O + UP * 0.25])
    yield [GrowArrow(dp), GrowArrow(dm), Create(sq), FadeIn(lab("at right angles to up", 22, INK).move_to(CP_O + [-1.5, 0.35, 0]))]
    yield [dm.animate.set_opacity(0.25), FadeIn(lab("+ i/2: front (a convention)", 22, BLUE).next_to(dp.get_end(), RIGHT, buff=0.3)),
           FadeIn(left_at(eq("we pick down = + i/2", 26, BLUE), -6.9, -2.1))]


TBL_X = (-4.2, 0.5, 4.6)
TBL_Y = [1.9, 1.0, 0.0, -1.0]


def tbl_cell(text, k, row, color=INK, size=26):
    return at(eq(text, size, color) if row > 0 else T(text, 24, MUTED, True), TBL_X[k], TBL_Y[row])


def front_table(upto):
    g = VGroup(tbl_cell("tilted 60° toward", 0, 0), tbl_cell("the right", 1, 0), tbl_cell("the front", 2, 0),
               at(lab("amplitudes (up, down)", 24, INK), TBL_X[0], TBL_Y[1]), tbl_cell("(0.866, 1/2)", 1, 1, BLUE), tbl_cell("(0.866, i/2)", 2, 1, BLUE))
    if upto >= 1:
        g.add(at(lab("vertical: up / down", 24, INK), TBL_X[0], TBL_Y[2]), tbl_cell("75% / 25%", 1, 2, TEAL), tbl_cell("75% / 25%", 2, 2, TEAL),
              at(T("same", 24, TEAL, True), 6.6, TBL_Y[2]))
    if upto >= 2:
        g.add(at(lab("sideways: right", 24, INK), TBL_X[0], TBL_Y[3]), tbl_cell("93.3%", 1, 3, TEAL), tbl_cell("50%", 2, 3, TEAL),
              at(T("differ", 24, ORANGE, True), 6.6, TBL_Y[3]))
    return g


@slide("The vertical magnet can't tell the right-tilted", "Same chances up and down, different sideways")
def phases(s):
    lines = VGroup(*[Line([-6.8, y, 0], [7.2, y, 0], color=LINE, stroke_width=2) for y in (1.45, 0.5, -0.5)])
    s.add(lines, front_table(0))
    yield [FadeIn(front_table(1)[6:])]
    yield [FadeIn(front_table(2)[10:])]
    yield [FadeIn(at(card("The state is the list of amplitudes, phases included,\nnot just a list of chances.", 11.0, 1.4, BLUE, 30), 0, -2.6),
                  shift=UP * 0.15)]


OV_Y = [1.2, 0.3]


def ov_cols():
    rt = mat([["1/√2"], ["1/√2"]], 28, ORANGE)
    at(rt, -4.6, 0.75)
    ours = mat([["0.866"], ["1/2"]], 28, BLUE)
    at(ours, -1.4, 0.75)
    return VGroup(rt, lab("right", 24, ORANGE).next_to(rt, UP, buff=0.2)), VGroup(ours, lab("our atoms", 24, BLUE).next_to(ours, UP, buff=0.2))


def ov_sum():
    return left_at(VGroup(eq("1/√2 × 0.866", 28, INK), eq("+", 28), eq("1/√2 × 1/2", 28, INK)).arrange(RIGHT, buff=0.25), 0.7, 0.75)


@slide("There's a shortcut for finding an amplitude.", "The overlap")
def ov1(s):
    yield [FadeIn(at(lab("a shortcut for the right amplitude", 26, INK), 0, 2.4))]
    rt, ours = ov_cols()
    yield [FadeIn(rt), FadeIn(ours)]
    yield [FadeIn(lab("conjugate each: real numbers stay the same", 22, ORANGE).move_to([-4.0, -0.75, 0])), Indicate(rt[0][2], color=ORANGE)]
    yield [FadeIn(ov_sum()), FadeIn(lab("multiply matching entries, then add", 22, INK).move_to([3.2, 1.6, 0]))]


def ov_base(s):
    rt, ours = ov_cols()
    s.add(at(lab("a shortcut for the right amplitude", 26, INK), 0, 2.4), rt, ours,
          lab("conjugate each: real numbers stay the same", 22, ORANGE).move_to([-4.0, -0.75, 0]), ov_sum(),
          lab("multiply matching entries, then add", 22, INK).move_to([3.2, 1.6, 0]))


@slide("We call this sum the overlap.", "The overlap")
def ov2(s):
    ov_base(s)
    yield [FadeIn(at(pill("the overlap", BLUE, 26), 3.2, -0.05))]
    yield [FadeIn(left_at(eq("≈ 0.966", 32, BLUE), 0.7, -1.0))]
    yield [FadeIn(left_at(VGroup(eq("0.966² ≈ 93.3%", 30, TEAL), check()).arrange(RIGHT, buff=0.3), 0.7, -1.9)),
           FadeIn(left_at(lab("the chance of right, from before", 22, TEAL), 0.7, -2.45))]


@slide("Its other name is the inner product.", "The overlap")
def ov3(s):
    ov_base(s)
    s.add(at(pill("the overlap", BLUE, 26), 3.2, -0.05), left_at(eq("≈ 0.966", 32, BLUE), 0.7, -1.0))
    yield [FadeIn(lab("also called the inner product", 22, BLUE).move_to([3.2, -0.55, 0]))]
    yield [FadeIn(left_at(eq("with itself: 0.866² + (1/2)² = 0.75 + 0.25 = 1", 26, BLUE), -6.6, -2.0)),
           FadeIn(left_at(lab("the squared length, one", 22, BLUE), -6.6, -2.5))]
    yield [FadeIn(at(card("chance of a result = |overlap with that result's certain state|²", 12.6, 0.85, TEAL, 26), 0, -3.45))]


# ------------------------------------------------------------------ particle on a line
deck.part("A particle on a line")

LINE_Y = -2.0
XS = np.linspace(-5.6, 5.6, 13)


def screen_axis(y=LINE_Y):
    ax = Arrow([-6.6, y, 0], [6.8, y, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.18)
    return VGroup(ax, lab("position on the screen", 22).next_to(ax.get_end(), DOWN, buff=0.15).shift(LEFT * 1.2))


def amp_row_line(y, angs, lens, r=0.4, color=BLUE):
    return VGroup(*[phasor([x, y], a, l, r=r, color=color, ring=False, width=4) if l > 0.08 else Dot([x, y, 0], radius=0.05, color=color)
                    for x, a, l in zip(XS, angs, lens)])


@slide("A particle on a line.", "One amplitude for every position")
def line1(s):
    yield [FadeIn(screen_axis())]
    rng = np.random.default_rng(2)
    dots = VGroup(*[Dot([x, LINE_Y + 0.25, 0], radius=0.06, color=BLUE) for x in rng.uniform(-6, 6, 9)])
    yield [LaggedStart(*[FadeIn(d, scale=2) for d in dots], lag_ratio=0.2), FadeIn(lab("it can land at any position", 24, INK).move_to([0, -1.1, 0]))]
    angs = 0.9 * XS
    lens = np.exp(-XS ** 2 / 30)
    row = amp_row_line(0.8, angs, lens, r=0.45)
    yield [LaggedStart(*[FadeIn(p) for p in row], lag_ratio=0.05), FadeIn(lab("one amplitude for every position", 24, BLUE).move_to([0, 1.8, 0]))]


@slide("That list is a complex function called the wave function.", "The wave function")
def line2(s):
    s.add(screen_axis())
    k = 0.7
    row0 = amp_row_line(1.9, k * XS, np.ones_like(XS) * 0.8, r=0.42)
    title = left_at(T("the wave function", 28, BLUE, True), -6.9, 2.5)
    desc = left_at(lab("a complex function: an amplitude at each position", 22, BLUE), -3.2, 2.5)
    yield [FadeIn(row0), FadeIn(title), FadeIn(desc)]
    row2 = amp_row_line(0.75, -k * XS, np.ones_like(XS) * 0.8, r=0.42)
    tag1 = left_at(lab("part from the first slit", 22, BLUE), -6.9, 2.5)
    tag2 = left_at(lab("part from the second slit", 22, BLUE), -6.9, 1.35)
    sm = np.cos(k * XS)
    row3 = amp_row_line(-0.6, np.where(sm >= 0, 0, PI), np.abs(sm) * 1.6, r=0.42, color=BLUE)
    sum_tag = left_at(T("their sum: the wave function at the screen", 24, BLUE, True), -6.9, 0.05)
    yield [FadeOut(desc), ReplacementTransform(title, sum_tag), FadeIn(tag1), FadeIn(row2), FadeIn(tag2), FadeIn(row3)]
    xs = np.linspace(-6.0, 6.0, 49)
    band = VGroup(*[Rectangle(width=0.25, height=0.35, stroke_width=0, fill_color=stripe_color(np.cos(k * x) ** 2), fill_opacity=1)
                    .move_to([x, LINE_Y + 0.3, 0]) for x in xs])
    yield [FadeIn(band), FadeIn(lab("dark stripes where the two parts cancel", 22, INK).move_to([-2.0, LINE_Y - 0.9, 0]))]


def gen_wave(x):
    return np.exp(-x ** 2 / 3.0) * (1 + 0.55 * np.sin(1.7 * x + 0.4))


@slide("The Born rule turns the wave function into a probability", "Chance from area")
def density(s):
    a1 = Axes(x_range=[-3.5, 3.5, 1], y_range=[-0.6, 1.6, 1], x_length=9.0, y_length=1.9, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([0.6, 1.35, 0])
    a2 = Axes(x_range=[-3.5, 3.5, 1], y_range=[0, 2.4, 1], x_length=9.0, y_length=2.4, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([0.6, -1.85, 0])
    w = a1.plot(gen_wave, x_range=[-3.5, 3.5], color=BLUE, stroke_width=4)
    d = a2.plot(lambda x: gen_wave(x) ** 2, x_range=[-3.5, 3.5], color=TEAL, stroke_width=4)
    s.add(a1, w, left_at(lab("the wave function", 24, BLUE), -6.9, 1.35))
    yield [Create(a2), Create(d), FadeIn(left_at(lab("its squared size:", 24, TEAL), -6.9, -1.5)),
           FadeIn(left_at(lab("the probability density", 24, TEAL), -6.9, -1.9))]
    area = a2.get_area(d, x_range=[-0.6, 0.9], color=TEAL, opacity=0.4)
    yield [FadeIn(area), FadeIn(lab("chance between two points = area", 24, INK).move_to([3.6, -0.3, 0])),
           FadeIn(lab("a", 22, INK).next_to(a2.c2p(-0.6, 0), DOWN, buff=0.1)), FadeIn(lab("b", 22, INK).next_to(a2.c2p(0.9, 0), DOWN, buff=0.1))]
    full = a2.get_area(d, x_range=[-3.5, 3.5], color=TEAL, opacity=0.18)
    yield [FadeIn(full), FadeIn(lab("whole area = 1", 24, TEAL, True).move_to([4.6, -2.6, 0]))]


BOX_L = (-6.4, -0.6, 5.2, 3.2)    # first axes: center x, center y, width, height
BOX_R = (3.4, -0.9, 6.4, 3.4)


def box_axes(spec, ymax):
    cx, cy, w, h = spec
    ax = Axes(x_range=[0, 1, 0.25], y_range=[0, ymax, 0.5], x_length=w, y_length=h, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([cx + w / 2, cy, 0] if cx < 0 else [cx, cy, 0])
    names = VGroup(lab("position (m)", 22).next_to(ax.x_axis, DOWN, buff=0.45))
    for v in (0, 0.25, 0.5, 0.75, 1):
        names.add(lab(f"{v:g}", 22).next_to(ax.c2p(v, 0), DOWN, buff=0.1))
    return ax, names


def walls(ax, h):
    return VGroup(*[Line(ax.c2p(v, 0), ax.c2p(v, 0) + UP * h, color=INK, stroke_width=7) for v in (0, 1)])


@slide("Let's try one.", "A particle between 0 and 1 metre")
def box1(s):
    ax, names = box_axes(BOX_L, 1.6)
    yield [Create(ax), FadeIn(names), FadeIn(walls(ax, 3.2)), FadeIn(lab("confined between 0 and 1 metre", 24, INK).move_to([-3.8, 2.35, 0]))]
    w = ax.plot(lambda x: np.sqrt(2) * np.sin(PI * x), x_range=[0, 1], color=BLUE, stroke_width=5)
    yield [Create(w), FadeIn(lab("wave function: one hump of a sine wave", 22, BLUE).move_to([-3.8, 1.85, 0]))]
    yield [FadeIn(lab("zero at the walls", 22, INK).move_to([-3.8, -3.3, 0])),
           FadeIn(lab("largest in the middle", 22, INK).next_to(ax.c2p(0.5, np.sqrt(2)), UP, buff=0.12))]


QUARTERS = [(0, 0.25, "9.1%"), (0.25, 0.5, "40.9%"), (0.5, 0.75, "40.9%"), (0.75, 1, "9.1%")]


@slide("Split the interval into quarters.", "Chance in each quarter")
def box2(s):
    ax1, n1 = box_axes(BOX_L, 1.6)
    w = ax1.plot(lambda x: np.sqrt(2) * np.sin(PI * x), x_range=[0, 1], color=BLUE, stroke_width=5)
    s.add(ax1, n1, walls(ax1, 3.2), w, lab("wave function", 22, BLUE).move_to([-3.8, 1.85, 0]))
    ax2, n2 = box_axes(BOX_R, 2.2)
    d = ax2.plot(lambda x: 2 * np.sin(PI * x) ** 2, x_range=[0, 1], color=TEAL, stroke_width=5)
    areas = [ax2.get_area(d, x_range=[a, b], color=TEAL, opacity=0.35 if k % 2 == 0 else 0.18) for k, (a, b, _) in enumerate(QUARTERS)]
    divs = VGroup(*[DashedLine(ax2.c2p(v, 0), ax2.c2p(v, 2.1), color=LINE, stroke_width=2) for v in (0.25, 0.5, 0.75)])
    yield [Create(ax2), FadeIn(n2), Create(d), Create(divs), FadeIn(lab("density: squared size", 22, TEAL).move_to([3.4, 1.45, 0]))]

    def pct(k):
        a, b, t = QUARTERS[k]
        return T(t, 26, TEAL if k in (0, 3) else INK, True).move_to(ax2.c2p((a + b) / 2, 0.55 if k in (1, 2) else 0.55) + UP * (0.0 if k in (1, 2) else 0.55))
    yield [FadeIn(areas[0]), FadeIn(areas[3]), FadeIn(pct(0)), FadeIn(pct(3))]
    yield [FadeIn(areas[1]), FadeIn(areas[2]), FadeIn(pct(1)), FadeIn(pct(2))]
    yield [FadeIn(at(eq("9.1 + 40.9 + 40.9 + 9.1 = 100%", 28, TEAL), -1.6, -3.6)),
           FadeIn(lab("certainly somewhere inside", 22, INK).move_to([4.9, -3.6, 0]))]


# ------------------------------------------------------------------ operators
deck.part("Measured quantities become operators")


def needs_cards():
    a = at(card(None, 6.4, 4.0, INK), -3.6, -0.5)
    b = at(card(None, 6.4, 4.0, BLUE), 3.6, -0.5)
    ta = at(T("1. its possible values", 28, INK, True), -3.6, 1.0)
    tb = at(T("2. for each value, a state", 28, BLUE, True), 3.6, 1.15)
    tb2 = at(T("that gives it for certain", 28, BLUE, True), 3.6, 0.7)
    return a, b, ta, VGroup(tb, tb2)


@slide("Measured quantities become operators.", "What a measured quantity needs")
def needs(s):
    a, b, ta, tb = needs_cards()
    yield [FadeIn(at(T("a measurable quantity now needs two things", 28, INK), 0, 2.3)), FadeIn(a), FadeIn(b), FadeIn(ta), FadeIn(tb)]
    vals = VGroup(chip("up", INK, size=30, h=0.8), chip("down", INK, size=30, h=0.8)).arrange(RIGHT, buff=0.6)
    at(vals, -3.6, -0.8)
    yield [FadeIn(vals, shift=UP * 0.15)]
    st = VGroup(VGroup(spin_icon([0, 0], True, 0.45), lab("certain up", 22, BLUE)).arrange(DOWN, buff=0.15),
                VGroup(spin_icon([0, 0], False, 0.45), lab("certain down", 22, BLUE)).arrange(DOWN, buff=0.15)).arrange(RIGHT, buff=0.9)
    at(st, 3.6, -0.9)
    yield [FadeIn(st, shift=UP * 0.15)]


EV_O = np.array([-2.0, -2.9, 0])


def eig_picture(stage):
    g = VGroup()
    u = np.array([np.cos(0.5), np.sin(0.5), 0])
    if stage >= 1:
        g.add(DashedLine(EV_O - u * 1.0, EV_O + u * 4.2, color=LINE, stroke_width=2),
              Arrow(EV_O, EV_O + u * 1.6, buff=0, color=BLUE, stroke_width=7, tip_length=0.22),
              lab("a certain state", 22, BLUE).next_to(EV_O + u * 0.8, DR, buff=0.12))
    if stage >= 2:
        g.add(Arrow(EV_O, EV_O + u * 3.4, buff=0, color=PURPLE, stroke_width=3, tip_length=0.2).set_opacity(0.9),
              left_at(lab("matrix applied: same line, rescaled by its value", 22, PURPLE), (EV_O + u * 3.4)[0] + 0.25, (EV_O + u * 3.4)[1]))
    return g


def gen_matrix():
    m = mat([["·", "·"], ["·", "·"]], 34, PURPLE, colw=0.8, rowh=0.7)
    return at(m, -5.4, 0.9)


@slide("A matrix holds both.", "A matrix holds both")
def matrix1(s):
    m = gen_matrix()
    yield [FadeIn(m), FadeIn(lab("a matrix", 24, PURPLE).next_to(m, DOWN, buff=0.2))]
    r1 = left_at(VGroup(T("eigenvectors", 28, BLUE, True), T("= the certain states", 28, INK)).arrange(RIGHT, buff=0.2), -3.6, 1.6)
    r2 = left_at(VGroup(T("eigenvalues", 28, INK, True), T("= the matching values", 28, INK)).arrange(RIGHT, buff=0.2), -3.6, 0.8)
    yield [FadeIn(r1), FadeIn(r2)]
    yield [FadeIn(left_at(lab("eigenvectors are also called eigenstates", 24, BLUE), -3.6, 0.1))]
    yield [FadeIn(eig_picture(1)), FadeIn(eig_picture(2)[3:])]


@slide("Such a matrix is called an operator.", "Operators")
def matrix2(s):
    m = gen_matrix()
    s.add(m, left_at(VGroup(T("eigenvectors", 28, BLUE, True), T("= the certain states", 28, INK)).arrange(RIGHT, buff=0.2), -3.6, 1.6),
          left_at(VGroup(T("eigenvalues", 28, INK, True), T("= the matching values", 28, INK)).arrange(RIGHT, buff=0.2), -3.6, 0.8),
          left_at(lab("eigenvectors are also called eigenstates", 24, BLUE), -3.6, 0.1))
    yield [FadeIn(pill("an operator", PURPLE, 28).next_to(m, DOWN, buff=0.3))]
    ax = Axes(x_range=[0, 6, 1], y_range=[-1.2, 1.2, 1], x_length=3.4, y_length=1.3, tips=False, axis_config={"color": LINE, "include_ticks": False})
    w1 = VGroup(ax, ax.plot(lambda x: np.exp(-(x - 3) ** 2 / 2) * np.cos(2 * x), x_range=[0, 6], color=BLUE, stroke_width=4))
    at(w1, -4.8, -2.4)
    box = at(card("operator", 2.4, 0.9, PURPLE, 26), 0.0, -2.4)
    ax2 = ax.copy()
    w2 = VGroup(ax2, ax2.plot(lambda x: np.exp(-(x - 3) ** 2 / 2) * np.cos(2 * x) * (x - 3) / 1.5, x_range=[0, 6], color=BLUE, stroke_width=4))
    at(w2, 4.8, -2.4)
    yield [FadeIn(w1), GrowArrow(arrow(w1, box)), FadeIn(box), GrowArrow(arrow(box, w2)), FadeIn(w2),
           FadeIn(at(lab("for a particle: an operation on wave functions", 24, INK), 0, -1.4))]


def energy_op(x=-4.2, y=0.7):
    m = mat([["E₀", "0"], ["0", "E₁"]], 30, PURPLE, colw=1.1, rowh=0.65)
    at(m, x, y)
    return VGroup(m, lab("energy operator", 24, PURPLE, True).next_to(m, UP, buff=0.25))


def swap_op(x=3.4, y=0.7):
    m = mat([["0", "1"], ["1", "0"]], 30, PURPLE, colw=0.9, rowh=0.65)
    at(m, x, y)
    return VGroup(m, lab("sideways operator: swaps the amplitudes", 24, PURPLE, True).next_to(m, UP, buff=0.25))


def energy_notes():
    return VGroup(lab("eigenstates: up and down", 24, BLUE), lab("values: the two energies, E₀ and E₁", 24, INK)).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to([-4.2, -1.1, 0])


def side_notes():
    return VGroup(lab("eigenstates: right and left", 24, ORANGE), lab("values: +1 for right, −1 for left", 24, INK)).arrange(DOWN, buff=0.15, aligned_edge=LEFT)


@slide("For the spin, the energy operator has up", "Two operators for the spin")
def spin_ops1(s):
    yield [FadeIn(energy_op()), FadeIn(energy_notes())]
    sn = side_notes().move_to([3.4, 0.9, 0])
    yield [FadeIn(at(T("the sideways magnet", 26, ORANGE, True), 3.4, 2.0)), FadeIn(sn[0])]
    yield [FadeIn(sn[1])]


@slide("Its operator swaps the two amplitudes.", "Two operators for the spin")
def spin_ops2(s):
    s.add(energy_op(), energy_notes())
    so = swap_op(3.4, 1.0)
    sn = side_notes().move_to([3.4, -0.35, 0])
    yield [FadeIn(so), FadeIn(sn)]
    r = left_at(VGroup(eq("swap (1/√2, 1/√2) = (1/√2, 1/√2)", 22, ORANGE), T("+1", 28, INK, True)).arrange(RIGHT, buff=0.3), -0.2, -1.65)
    yield [FadeIn(r)]
    l = left_at(VGroup(eq("swap (1/√2, −1/√2) = −(1/√2, −1/√2)", 22, ORANGE), T("−1", 28, INK, True)).arrange(RIGHT, buff=0.3), -0.2, -2.45)
    yield [FadeIn(l)]


def fit_cards():
    a = at(card(None, 6.6, 4.2, INK), -3.6, -0.6)
    b = at(card(None, 6.6, 4.2, BLUE), 3.6, -0.6)
    return a, b


@slide("Two conditions make an operator fit", "Fit for a measurement")
def fit1(s):
    a, b = fit_cards()
    yield [FadeIn(a), FadeIn(b), FadeIn(at(T("two conditions", 28, INK), 0, 2.2))]
    ta = at(VGroup(T("its values are real", 28, INK, True), lab("they are measured numbers", 24, INK)).arrange(DOWN, buff=0.2), -3.6, 0.8)
    yield [FadeIn(ta), FadeIn(at(eq("+1, −1, E₀, E₁", 30, INK), -3.6, -1.0))]
    tb = at(VGroup(T("its certain states don't overlap", 28, BLUE, True)), 3.6, 1.0)
    o = np.array([3.0, -1.9, 0])
    k = 1 / np.sqrt(2)
    rr = Arrow(o, o + 1.6 * np.array([k, k, 0]), buff=0, color=ORANGE, stroke_width=6, tip_length=0.2)
    ll = Arrow(o, o + 1.6 * np.array([k, -k, 0]), buff=0, color=ORANGE, stroke_width=6, tip_length=0.2)
    sq = VMobject(color=INK, stroke_width=2).set_points_as_corners([o + 0.3 * np.array([k, k, 0]), o + 0.3 * np.array([2 * k, 0, 0]), o + 0.3 * np.array([k, -k, 0])])
    yield [FadeIn(tb), GrowArrow(rr), GrowArrow(ll), Create(sq), FadeIn(lab("right", 22, ORANGE).next_to(rr.get_end(), RIGHT, buff=0.1)),
           FadeIn(lab("left", 22, ORANGE).next_to(ll.get_end(), RIGHT, buff=0.1)), FadeIn(lab("overlap 0", 24, BLUE, True).move_to([4.9, -1.9, 0]))]
    yield [FadeIn(at(lab("certain of one value: never gives another", 24, INK), 3.6, 0.35))]


@slide("Matrices equal to their own conjugate transpose", "Hermitian operators and observables")
def herm(s):
    m1 = at(mat([["0", "1"], ["1", "0"]], 30, PURPLE, colw=0.9, rowh=0.65), -5.6, 1.2)
    m2 = at(mat([["0", "1"], ["1", "0"]], 30, PURPLE, colw=0.9, rowh=0.65), -1.6, 1.2)
    diag = DashedLine(m1.get_corner(UL) + [0.25, -0.1, 0], m1.get_corner(DR) + [-0.25, 0.1, 0], color=ORANGE, stroke_width=2)
    yield [FadeIn(m1), Create(diag), GrowArrow(arrow(m1, m2)), FadeIn(m2),
           FadeIn(lab("flip across the diagonal, conjugate each entry", 22, ORANGE).move_to([-3.6, 2.35, 0])),
           FadeIn(lab("the same matrix", 24, TEAL, True).next_to(m2, RIGHT, buff=0.3)),
           FadeIn(lab("the energy operator too", 22, INK).move_to([-3.6, 0.0, 0]))]
    hp = at(pill("Hermitian", PURPLE, 30), -3.6, -1.1)
    yield [FadeIn(hp), FadeIn(at(lab("the quantity it represents: an observable", 24, INK), -3.6, -1.85))]
    o = np.array([2.6, -2.2, 0])
    k = 1 / np.sqrt(2)
    R = 3.0
    st = R * np.array([np.cos(PI / 6), np.sin(PI / 6), 0])
    rdir, ldir = np.array([k, k, 0]), np.array([k, -k, 0])
    pr, pl = np.dot(st, rdir) * rdir, np.dot(st, ldir) * ldir
    g = VGroup(DashedLine(o, o + rdir * 3.6, color=BLUE, stroke_width=2), DashedLine(o, o + ldir * 1.4, color=BLUE, stroke_width=2),
               Arrow(o, o + pr, buff=0, color=BLUE, stroke_width=4, tip_length=0.16), Arrow(o, o + pl, buff=0, color=BLUE, stroke_width=4, tip_length=0.16),
               DashedLine(o + pr, o + st, color=LINE, stroke_width=2), DashedLine(o + pl, o + st, color=LINE, stroke_width=2),
               Arrow(o, o + st, buff=0, color=BLUE, stroke_width=6, tip_length=0.2),
               lab("any state", 22, BLUE).next_to(o + st, RIGHT, buff=0.1), lab("= a sum of certain states", 22, BLUE).move_to(o + [1.9, 2.75, 0]))
    yield [FadeIn(g)]


HIST_O = np.array([-3.75, -2.6, 0])  # value 0 on the axis


def hx(v):
    return HIST_O + RIGHT * 1.9 * v


def hist_base():
    axis = Line(hx(-1.6), hx(1.6), color=LINE, stroke_width=3)
    ticks = VGroup(*[lab(t, 24, INK).next_to(hx(v), DOWN, buff=0.15) for v, t in ((-1, "−1"), (0, "0"), (1, "+1"))])
    return VGroup(axis, ticks, lab("sideways result", 22).next_to(hx(0), DOWN, buff=0.6))


def hist_bars():
    b1 = bar(hx(1)[0], HIST_O[1], 0.933, hmax=3.0, w=1.0)
    b1.add(T("93.3%", 24, TEAL, True).next_to(b1[0], RIGHT, buff=0.12).align_to(b1[0], UP))
    b2 = bar(hx(-1)[0], HIST_O[1], 0.067, hmax=3.0, w=1.0, label="6.7%")
    return b1, b2


def avg_mark():
    x = hx(0.866)
    ln = DashedLine(x, x + UP * 4.1, color=ORANGE, stroke_width=4)
    return VGroup(ln, T("average 0.866", 24, ORANGE, True).next_to(ln.get_end(), LEFT, buff=0.12))


AV_X = 0.6


def av_rows():
    return [left_at(eq("average = (+1)(0.933) + (−1)(0.067)", 24, INK), AV_X, 2.0),
            left_at(eq("        = 0.866", 26, ORANGE), AV_X, 1.45),
            left_at(T("the expectation value", 26, ORANGE, True), AV_X, 0.85)]


@slide("Repeat a measurement on many identical atoms,", "Average and spread")
def avg1(s):
    yield [FadeIn(hist_base()), FadeIn(left_at(lab("many identical atoms: an average and a spread", 24, INK), -7.0, 2.4))]
    yield [FadeIn(left_at(lab("our tilted atoms, sideways magnet", 24, BLUE), -7.0, 1.95))]
    b1, b2 = hist_bars()
    yield [GrowFromEdge(b1[0], DOWN), FadeIn(b1[1]), GrowFromEdge(b2[0], DOWN), FadeIn(b2[1])]


def avg_done(s):
    b1, b2 = hist_bars()
    s.add(hist_base(), left_at(lab("many identical atoms: an average and a spread", 24, INK), -7.0, 2.4),
          left_at(lab("our tilted atoms, sideways magnet", 24, BLUE), -7.0, 1.95), b1, b2)


@slide("The average is zero point eight six six.", "Average and spread")
def avg2(s):
    avg_done(s)
    rows = av_rows()
    yield [FadeIn(rows[0]), FadeIn(rows[1]), Create(avg_mark()[0]), FadeIn(avg_mark()[1])]
    yield [FadeIn(rows[2])]


def sd_rows():
    return [left_at(eq("1. average of squared results", 24, INK), AV_X, 0.2),
            left_at(eq("   every result² = 1, so: 1", 24, INK), AV_X, -0.3),
            left_at(eq("2. square the average: 0.866²", 24, INK), AV_X, -0.85),
            left_at(eq("   = 0.75", 24, INK), AV_X, -1.35),
            left_at(eq("3. √(1 − 0.75)", 24, INK), AV_X, -1.9),
            left_at(eq("   = 0.5, the spread", 26, ORANGE), AV_X, -2.45)]


def av_compact():
    return VGroup(left_at(eq("average = 0.866", 26, ORANGE), AV_X, 2.0), left_at(T("the expectation value", 26, ORANGE, True), AV_X, 1.45))


def sd_head():
    return left_at(T("the spread (standard deviation)", 26, ORANGE, True), AV_X, 0.8)


@slide("For the spread, the standard deviation,", "Average and spread")
def sd1(s):
    avg_done(s)
    s.add(av_compact(), avg_mark())
    r = sd_rows()
    yield [FadeIn(sd_head()), FadeIn(r[0])]
    yield [FadeIn(r[1])]
    yield [FadeIn(r[2])]


@slide("Zero point eight six six squared is zero point seven five.", "Average and spread")
def sd2(s):
    avg_done(s)
    s.add(av_compact(), avg_mark(), sd_head())
    r = sd_rows()
    s.add(*r[:3])
    yield [FadeIn(r[3])]
    yield [FadeIn(r[4])]
    sp = DoubleArrow(hx(0.366) + DOWN * 1.05, hx(1.366) + DOWN * 1.05, buff=0, color=ORANGE, stroke_width=4, tip_length=0.15)
    yield [FadeIn(r[5]), GrowFromCenter(sp), FadeIn(lab("standard deviation: 0.5", 22, ORANGE, True).next_to(sp, RIGHT, buff=0.15))]


@slide("The average also comes straight from the operator.", "The average from the operator")
def avg_op(s):
    yield [FadeIn(at(T("apply the operator, then take the overlap with the state", 28, INK), 0, 2.2))]
    st = at(mat([["0.866"], ["1/2"]], 30, BLUE), -5.6, 0.4)
    sw = at(card("swap", 1.6, 0.8, PURPLE, 26), -3.4, 0.4)
    out = at(mat([["1/2"], ["0.866"]], 30, BLUE), -1.2, 0.4)
    ov = left_at(eq("0.866 × 1/2 + 1/2 × 0.866", 30, INK), 0.6, 0.4)
    yield [FadeIn(st), GrowArrow(arrow(st, sw)), FadeIn(sw), GrowArrow(arrow(sw, out)), FadeIn(out),
           FadeIn(lab("overlap with the state:", 22).next_to(ov, UP, buff=0.2))]
    res = left_at(VGroup(eq("≈ 0.866", 34, ORANGE), lab("the same average", 26, ORANGE), check()).arrange(RIGHT, buff=0.3), 0.6, -0.8)
    yield [FadeIn(ov), FadeIn(res)]


def two_pipes(first_a, y1=0.9, y2=-0.7, labels=True):
    def pipe(a, b, y):
        st = at(chip("state", BLUE, size=24, h=0.6), -5.4, y)
        p = at(card(a if labels else "", 1.0, 0.7, PURPLE, 28), -3.4, y)
        q = at(card(b if labels else "", 1.0, 0.7, PURPLE, 28), -1.6, y)
        return VGroup(st, arrow(st, p), p, arrow(p, q), q)
    return pipe("B", "A", y1), pipe("A", "B", y2)


@slide("With ordinary numbers, the order of multiplying", "Order can matter")
def order1(s):
    yield [FadeIn(at(VGroup(eq("a × b = b × a", 36, INK), lab("ordinary numbers", 24)).arrange(DOWN, buff=0.2), -3.6, 1.8))]
    p1, p2 = two_pipes(True, 0.0, -1.3, labels=False)
    yield [FadeIn(p1), FadeIn(p2), FadeIn(at(T("operators: the order can matter", 28, PURPLE, True), 3.4, -0.65))]
    yield [FadeIn(at(T("the commutator measures how much", 28, PURPLE), 3.4, -1.5))]
    q1, q2 = two_pipes(True, 0.0, -1.3)
    yield [Transform(p1, q1), Transform(p2, q2), FadeIn(at(lab("two operators, A and B", 24, INK), -3.5, -2.3))]


@slide("Apply B and then A.", "The commutator")
def order2(s):
    p1, p2 = two_pipes(True, 1.4, -0.2)
    r1 = left_at(eq("A B (state)", 30, PURPLE), -0.6, 1.4)
    yield [FadeIn(p1), GrowArrow(arrow(p1[4], r1)), FadeIn(r1), FadeIn(lab("B first, then A", 22).next_to(p1[2:], UP, buff=0.15))]
    r2 = left_at(eq("B A (state)", 30, PURPLE), -0.6, -0.2)
    yield [FadeIn(p2), GrowArrow(arrow(p2[4], r2)), FadeIn(r2), FadeIn(at(T("−", 40, INK), 3.2, 0.6)),
           FadeIn(lab("subtract", 22).move_to([3.2, 0.15, 0]))]
    c = at(VGroup(eq("[A, B] = A B − B A", 40, PURPLE), lab("the commutator of A with B", 26, PURPLE)).arrange(DOWN, buff=0.25), 0, -2.3)
    yield [FadeIn(c, shift=UP * 0.15)]


EUP, EDN = "E₀", "E₁"


def ham_cols():
    st = at(mat([["up"], ["down"]], 26, BLUE, colw=1.2), -5.6, 0.2)
    e = at(mat([["E₀ up"], ["E₁ down"]], 26, BLUE, colw=1.9), -2.6, 0.2)
    return st, e


@slide("Take the energy and the sideways operators.", "Energy and sideways in both orders")
def ops_order1(s):
    eo = energy_op(-4.6, 1.75)
    so = swap_op(3.0, 1.75)
    so[1].become(lab("sideways: swap", 24, PURPLE, True).next_to(so[0], UP, buff=0.25))
    yield [FadeIn(eo), FadeIn(so)]
    st, e = ham_cols()
    yield [FadeIn(st), GrowArrow(arrow(st, e, color=PURPLE)), FadeIn(e), FadeIn(lab("energy", 22, PURPLE).move_to([-4.15, 0.55, 0])),
           FadeIn(lab("up, down: the amplitudes", 22).move_to([-4.1, -1.05, 0]))]
    r1 = left_at(VGroup(T("energy, then swap:", 24, INK), eq("(E₁ down, E₀ up)", 26, BLUE)).arrange(RIGHT, buff=0.2), 0.2, 0.55)
    r2 = left_at(VGroup(T("swap, then energy:", 24, INK), eq("(E₀ down, E₁ up)", 26, BLUE)).arrange(RIGHT, buff=0.2), 0.2, -0.25)
    yield [FadeIn(r1), FadeIn(r2), FadeIn(left_at(lab("swap first: each amplitude gets the other one's energy", 22, ORANGE), 0.2, -0.95))]


@slide("So the two orders agree only if the energies match.", "Energy and sideways in both orders")
def ops_order2(s):
    r1 = left_at(VGroup(T("energy, then swap:", 24, INK), eq("(E₁ down, E₀ up)", 26, BLUE)).arrange(RIGHT, buff=0.2), -4.0, 1.9)
    r2 = left_at(VGroup(T("swap, then energy:", 24, INK), eq("(E₀ down, E₁ up)", 26, BLUE)).arrange(RIGHT, buff=0.2), -4.0, 1.1)
    s.add(r1, r2)
    yield [FadeIn(at(eq("equal only if E₀ = E₁", 30, INK), 0, 0.1))]
    c = at(VGroup(eq("[energy, sideways] =", 30, PURPLE), mat([["0", "E₀ − E₁"], ["E₁ − E₀", "0"]], 26, PURPLE, colw=2.0, rowh=0.6)).arrange(RIGHT, buff=0.3), 0, -1.5)
    yield [FadeIn(c), FadeIn(at(T("the energies differ, so this is not zero", 26, ORANGE, True), 0, -2.85))]


def axes_two(o, r=2.3):
    o = np.array([o[0], o[1], 0.0])
    k = 1 / np.sqrt(2)
    g = VGroup(Line(o + LEFT * r * 0.4, o + RIGHT * r, color=MUTED, stroke_width=3), Line(o + DOWN * r * 0.9, o + UP * r, color=MUTED, stroke_width=3),
               DashedLine(o - r * 0.6 * np.array([k, k, 0]), o + r * np.array([k, k, 0]), color=MUTED, stroke_width=3),
               DashedLine(o - r * 0.4 * np.array([k, -k, 0]), o + r * np.array([k, -k, 0]), color=MUTED, stroke_width=3))
    g.add(lab("up amplitude", 22, MUTED).next_to(o + RIGHT * r, DOWN, buff=0.12), lab("down amplitude", 22, MUTED).next_to(o + UP * r, UP, buff=0.08),
          lab("right", 22, MUTED).next_to(o + r * np.array([k, k, 0]), UR, buff=0.05), lab("left", 22, MUTED).next_to(o + r * np.array([k, -k, 0]), DR, buff=0.05))
    return g


SH_O = np.array([3.4, -0.9, 0])


@slide("If two operators shared a full set of certain states,", "Shared certain states")
def shared(s):
    a = left_at(T("shared certain states: both orders agree on each", 24, INK), -7.0, 2.2)
    yield [FadeIn(a)]
    b = left_at(eq("→ commutator = 0", 26, PURPLE), -7.0, 1.55)
    yield [FadeIn(b)]
    c = left_at(T("not commuting: no shared set", 24, INK, True), -7.0, 0.5)
    yield [FadeIn(c), FadeIn(axes_two(SH_O)), FadeIn(lab("energy: up, down", 22, INK).move_to([-4.6, -0.2, 0])),
           FadeIn(lab("sideways: right, left", 22, INK).move_to([-4.4, -0.65, 0]))]
    k = 1 / np.sqrt(2)
    R = 2.3 * 0.85
    tip = SH_O + R * np.array([k, k, 0])
    st = VGroup(Arrow(SH_O, tip, buff=0, color=BLUE, stroke_width=7, tip_length=0.22),
                DashedLine(tip, [tip[0], SH_O[1], 0], color=BLUE, stroke_width=3), DashedLine(tip, [SH_O[0], tip[1], 0], color=BLUE, stroke_width=3))
    yield [FadeIn(st), FadeIn(words("certain to go right, yet spread over up and down", 26, 24, INK).move_to([-4.0, -1.9, 0]))]


@slide("The magnets in a row showed this.", "Shared certain states")
def shared2(s):
    s.add(axes_two(SH_O))
    k = 1 / np.sqrt(2)
    R = 2.3 * 0.85
    tip = SH_O + R * np.array([k, k, 0])
    s.add(Arrow(SH_O, tip, buff=0, color=BLUE, stroke_width=7, tip_length=0.22),
          DashedLine(tip, [tip[0], SH_O[1], 0], color=BLUE, stroke_width=3), DashedLine(tip, [SH_O[0], tip[1], 0], color=BLUE, stroke_width=3))
    a = at(card("atoms certain\nto go right", 2.8, 1.1, ORANGE, 24), -5.6, 1.4)
    m = magnet("vertical", -2.2, 1.4, w=2.0)
    yield [FadeIn(a), GrowArrow(arrow(a, m)), FadeIn(m)]
    b1 = bar(-5.0, -2.9, 0.5, hmax=2.4, w=1.0, label="50%")
    b2 = bar(-3.0, -2.9, 0.5, hmax=2.4, w=1.0, label="50%")
    yield [FadeIn(b1), FadeIn(b2), FadeIn(lab("up", 24, INK).move_to([-5.0, -3.2, 0])), FadeIn(lab("down", 24, INK).move_to([-3.0, -3.2, 0])),
           FadeIn(lab("half up, half down", 26, TEAL, True).move_to([-4.0, 0.2, 0]))]


# ------------------------------------------------------------------ matter waves
deck.part("Matter waves")


def wave_between(a, b, wavelength, amp=0.18, color=ORANGE, width=3):
    a = np.array([a[0], a[1], 0.0])
    b = np.array([b[0], b[1], 0.0])
    d = b - a
    L = np.linalg.norm(d)
    u = d / L
    n = np.array([-u[1], u[0], 0.0])
    return ParametricFunction(lambda t: a + u * t + n * amp * np.sin(2 * np.pi * t / wavelength), t_range=[0, L], color=color, stroke_width=width)


@slide("Matter waves.", "Three more experiments")
def mw1(s):
    goal = at(card("wanted: a particle's momentum operator", 7.6, 1.0, PURPLE, 30), 0, 1.9)
    yield [FadeIn(goal)]
    names = ["light on a metal", "X-rays on electrons", "electrons on a crystal"]
    cs = VGroup(*[at(card(f"{k + 1}. {n}", 4.4, 1.0, INK, 26), x, -0.4) for k, (n, x) in enumerate(zip(names, (-4.8, 0, 4.8)))])
    yield [LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in cs], lag_ratio=0.25)]
    yield [cs[0][0].animate.set_fill(ORANGE, opacity=0.15).set_stroke(ORANGE),
           FadeIn(at(lab("first: light", 26, ORANGE, True), -4.8, -1.4))]


PE_METAL_X = -3.8


def pe_rig(n_e=2, packets=False):
    metal = Rectangle(width=0.5, height=3.0, color=INK, fill_color=PALE, fill_opacity=1).move_to([PE_METAL_X, 0.0, 0])
    g = VGroup(metal, lab("metal", 22).move_to([PE_METAL_X, -1.85, 0]))
    for y in (1.0, 0.0, -1.0):
        if packets:
            g.add(wave_between((-6.4, y + 0.75), (-5.2, y + 0.4), 0.3, 0.12), wave_between((-5.0, y + 0.35), (PE_METAL_X - 0.3, y), 0.3, 0.12))
        else:
            g.add(wave_between((-7.0, y + 0.9), (PE_METAL_X - 0.3, y), 0.35, 0.12))
    g.add(lab("light", 22, ORANGE).move_to([-6.3, 2.0, 0]))
    ys = [(0.8, 0.5), (-0.4, -0.3), (0.2, 0.1), (-1.0, -0.5), (1.2, 0.6)][:n_e]
    for y, dy in ys:
        g.add(Dot([PE_METAL_X + 0.5, y, 0], radius=0.09, color=BLUE), arrow([PE_METAL_X + 0.6, y, 0], [PE_METAL_X + 1.8, y + dy, 0], color=BLUE))
    g.add(lab("electrons", 22, BLUE).move_to([PE_METAL_X + 1.3, 1.95, 0]))
    return g


PE_X = 0.1


def pe_expect():
    head = left_at(T("if light were a smooth wave:", 26, MUTED, True), PE_X, 2.0)
    a = left_at(T("brighter light → faster electrons", 26, INK), PE_X, 1.1)
    b = left_at(T("dim light of any colour → some, eventually", 26, INK), PE_X, 0.3)
    return head, a, b


@slide("Shine light on a clean metal, and it knocks electrons out.", "Light knocks electrons out of a metal")
def pe1(s):
    yield [FadeIn(pe_rig())]
    head, a, b = pe_expect()
    yield [FadeIn(head), FadeIn(a)]
    yield [FadeIn(b)]


PE_AX = dict(x_range=[0, 12, 2], y_range=[0, 3, 1], x_length=6.0, y_length=3.2)
F0 = 5.56
H_EV = 0.41357  # eV per 10^14 Hz


def pe_axes():
    ax = Axes(**PE_AX, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([3.6, -0.7, 0])
    names = VGroup(lab("light frequency (10¹⁴ Hz)", 22).next_to(ax.x_axis, DOWN, buff=0.45),
                   lab("energy of the fastest electrons (eV, a small energy unit)", 22).next_to(ax.y_axis, UP, buff=0.15).shift(RIGHT * 2.3))
    for v in (0, 4, 8, 12):
        names.add(lab(str(v), 22).next_to(ax.c2p(v, 0), DOWN, buff=0.12))
    for v in (1, 2, 3):
        names.add(lab(str(v), 22).next_to(ax.c2p(0, v), LEFT, buff=0.12))
    return ax, names


def pe_line(ax):
    return ax.plot(lambda f: H_EV * (f - F0), x_range=[F0, 12], color=BLUE, stroke_width=5)


def pe_flat(ax):
    return VGroup(Line(ax.c2p(0, 0), ax.c2p(F0, 0), color=BLUE, stroke_width=6), Dot(ax.c2p(F0, 0), radius=0.08, color=INK))


@slide("Neither happens.", "Light knocks electrons out of a metal")
def pe2(s):
    rig = pe_rig()
    head, a, b = pe_expect()
    s.add(rig, head, a, b)
    xa, xb = xmark(a), xmark(b)
    yield [Create(xa), Create(xb), a.animate.set_color(MUTED), b.animate.set_color(MUTED)]
    more = pe_rig(5)
    brighter = left_at(T("brighter light: more electrons, not faster ones", 24, BLUE, True), PE_X, -0.9)
    yield [FadeIn(more[10:16]), FadeIn(brighter)]
    ax, names = pe_axes()
    yield [FadeOut(VGroup(head, a, b, brighter, xa, xb)), FadeOut(more[10:16]),
           Create(ax), FadeIn(names), Create(pe_flat(ax)),
           FadeIn(left_at(lab("below a threshold frequency: none, however bright", 22, INK), -7.0, -2.6))]
    yield [Create(pe_line(ax)), FadeIn(left_at(lab("above it: the energy grows in step with the frequency", 22, BLUE), -7.0, -3.05))]


def pe3_done(s):
    ax, names = pe_axes()
    s.add(ax, names, pe_flat(ax), pe_line(ax))
    return ax


def packet_eq(final=True):
    if final:
        return left_at(VGroup(T("packet energy =", 26, ORANGE, True), heq("h × frequency", 28, ORANGE)).arrange(RIGHT, buff=0.2), -7.0, -2.75)
    return left_at(VGroup(T("packet energy =", 26, ORANGE, True), eq("constant × frequency", 28, ORANGE)).arrange(RIGHT, buff=0.2), -7.0, -2.75)


@slide("Einstein explained this in nineteen oh five.", "Light comes in packets")
def pe4(s):
    ax = pe3_done(s)
    yield [FadeIn(pe_rig(packets=True)), FadeIn(left_at(lab("Einstein, 1905: light arrives in packets", 24, INK, True), -7.0, -2.25))]
    pe = packet_eq(False)
    yield [FadeIn(pe)]
    yield [Transform(pe, packet_eq(True)), FadeIn(left_at(lab("h: Planck's constant", 24, PURPLE), -7.0, -3.3))]
    yield [FadeIn(left_at(lab("introduced by Max Planck in 1900", 22), -3.6, -3.3))]


def pe4_done(s):
    ax = pe3_done(s)
    s.add(pe_rig(packets=True), left_at(lab("Einstein, 1905: light arrives in packets", 24, INK, True), -7.0, -2.25), packet_eq(True),
          left_at(lab("h: Planck's constant", 24, PURPLE), -7.0, -3.3), left_at(lab("introduced by Max Planck in 1900", 22), -3.6, -3.3))
    return ax


def slope_tri(ax):
    a, b = ax.c2p(8, H_EV * (8 - F0)), ax.c2p(10, H_EV * (8 - F0))
    c = ax.c2p(10, H_EV * (10 - F0))
    return VGroup(DashedLine(a, b, color=PURPLE, stroke_width=3), DashedLine(b, c, color=PURPLE, stroke_width=3),
                  T("slope h", 26, PURPLE, True).next_to(b, DR, buff=0.08))


@slide("Each packet frees at most one electron.", "One packet, one electron")
def pe5(s):
    ax = pe4_done(s)
    yield [FadeIn(at(lab("one packet frees at most one electron", 24, INK), 3.6, 2.45))]
    yield [FadeIn(left_at(T("electron energy = packet energy − energy to free it", 22, INK), -0.3, 2.0))]
    yield [Create(slope_tri(ax)), Indicate(pe_line(ax), color=PURPLE)]


@slide("Robert Millikan measured that line", "Millikan measures the line")
def pe6(s):
    ax = pe4_done(s)
    s.add(slope_tri(ax), left_at(T("electron energy = packet energy − energy to free it", 22, INK), -0.3, 2.0))
    yield [FadeIn(at(lab("Robert Millikan, 1916: measured the line", 24, INK, True), 3.6, 2.45))]
    yield [FadeIn(at(lab("its slope: within 1% of Planck's value", 22, PURPLE), 3.3, 0.45))]
    th = ax.c2p(F0, 0)
    note = VGroup(lab("sodium: starts with green light,", 22, ORANGE), lab("5.6 × 10¹⁴ Hz", 22, ORANGE)).arrange(DOWN, buff=0.08)
    at(note, 2.2, -0.9)
    yield [Flash(th, color=ORANGE), FadeIn(note),
           GrowArrow(Arrow(note.get_bottom() + DOWN * 0.05 + RIGHT * 0.6, th + UP * 0.12, buff=0, color=ORANGE, stroke_width=3, tip_length=0.14))]


@slide("Light also carries momentum.", "Light carries momentum")
def lp(s):
    plate = Rectangle(width=0.35, height=2.6, color=INK, fill_color=PALE, fill_opacity=1).move_to([-2.4, 0.4, 0])
    waves = VGroup(*[wave_between((-6.8, y), (-2.65, y), 0.35, 0.12) for y in (1.2, 0.4, -0.4)])
    yield [FadeIn(plate), FadeIn(waves), FadeIn(lab("light", 22, ORANGE).move_to([-6.3, 1.85, 0]))]
    yield [FadeIn(left_at(VGroup(T("momentum =", 26, ORANGE, True), eq("energy / speed of light", 26, ORANGE)).arrange(RIGHT, buff=0.2), -0.6, 1.6)),
           FadeIn(left_at(lab("from electromagnetism", 22), -0.6, 1.0))]
    push = Arrow([-2.0, 0.4, 0], [-0.8, 0.4, 0], buff=0, color=ORANGE, stroke_width=7, tip_length=0.24)
    yield [GrowArrow(push), plate.animate.shift(RIGHT * 0.15), FadeIn(lab("it pushes on what it hits", 22, INK).move_to([-4.2, -1.4, 0]))]
    yield [FadeIn(left_at(T("one packet:", 26, INK, True), -0.6, 0.0)),
           FadeIn(left_at(heq("(h × frequency) / (frequency × wavelength)", 24, INK), -0.6, -0.6)),
           FadeIn(left_at(heq("= h / wavelength", 34, ORANGE), -0.6, -1.4)),
           FadeIn(left_at(lab("using speed of light = frequency × wavelength", 22), -0.6, -2.1))]


CO_E = np.array([-1.2, -0.3, 0])
CO_ANG = np.radians(40)


def compton_parts():
    inc = wave_between((-6.8, CO_E[1]), (CO_E[0] - 0.2, CO_E[1]), 0.42, 0.18)
    e = VGroup(Dot(CO_E, radius=0.15, color=BLUE), lab("electron", 22, BLUE).move_to(CO_E + [-0.75, -0.45, 0]))
    u = np.array([np.cos(CO_ANG), np.sin(CO_ANG)])
    same = DashedVMobject(wave_between(CO_E[:2] + 0.2 * u, CO_E[:2] + 3.8 * u, 0.42, 0.18, MUTED), num_dashes=40)
    longer = wave_between(CO_E[:2] + 0.2 * u, CO_E[:2] + 3.8 * u, 0.75, 0.2, ORANGE, 4)
    u2 = np.array([np.cos(np.radians(75)), np.sin(np.radians(75))])
    longer2 = wave_between(CO_E[:2] + 0.2 * u2, CO_E[:2] + 2.4 * u2, 1.0, 0.2, ORANGE, 4)
    recoil = arrow(CO_E + [0.15, -0.15, 0], CO_E + [2.0, -1.5, 0], color=BLUE)
    ang = VGroup(DashedLine(CO_E, CO_E + RIGHT * 2.8, color=MUTED, stroke_width=2),
                 Arc(radius=1.1, start_angle=0, angle=CO_ANG, arc_center=CO_E, color=MUTED, stroke_width=3),
                 T("angle", 22, MUTED).move_to(CO_E + [1.55, 0.4, 0]))
    return inc, e, same, longer, longer2, recoil, ang


@slide("In nineteen twenty-three, Arthur Compton bounced X-rays", "X-rays bounce off electrons")
def co1(s):
    inc, e, same, longer, longer2, recoil, ang = compton_parts()
    yield [Create(inc), FadeIn(e), FadeIn(lab("X-rays", 22, ORANGE).move_to([-5.6, 0.35, 0])),
           FadeIn(left_at(lab("Arthur Compton, 1923: X-rays on the electrons in carbon", 24, INK, True), -7.0, 2.4))]
    yield [FadeIn(left_at(lab("a smooth wave would shake the electron at the wave's own frequency", 24, MUTED), -7.0, -2.6))]
    yield [Create(same), FadeIn(ang), FadeIn(left_at(lab("and the electron would re-radiate the same wavelength", 24, MUTED), -7.0, -3.1))]


@slide("Instead, the scattered X-rays came out with a longer", "X-rays bounce off electrons")
def co2(s):
    inc, e, same, longer, longer2, recoil, ang = compton_parts()
    s.add(inc, e, lab("X-rays", 22, ORANGE).move_to([-5.6, 0.35, 0]), ang,
          left_at(lab("Arthur Compton, 1923: X-rays on the electrons in carbon", 24, INK, True), -7.0, 2.4))
    s.add(same)
    smooth_caps = VGroup(left_at(lab("a smooth wave would shake the electron at the wave's own frequency", 24, MUTED), -7.0, -2.6),
                         left_at(lab("and the electron would re-radiate the same wavelength", 24, MUTED), -7.0, -3.1))
    s.add(smooth_caps)
    yield [same.animate.set_color(RED).set_opacity(0.3), smooth_caps.animate.set_color(RED), Create(longer), GrowArrow(recoil), FadeIn(lab("electron recoils", 22, BLUE).next_to(recoil.get_end(), RIGHT, buff=0.1)),
           FadeIn(left_at(T("measured: a longer wavelength", 24, ORANGE, True), 2.1, 1.6))]
    yield [Create(longer2), FadeIn(left_at(lab("larger angle: longer still", 24, ORANGE), 2.1, 1.0)),
           FadeIn(left_at(VGroup(*[heq(t, 24, INK, FONT) for t in ("exactly what a collision with", "a packet of momentum", "h / wavelength predicts")]).arrange(DOWN, buff=0.1, aligned_edge=LEFT), 2.1, 0.0))]


@slide("In nineteen twenty-four, Louis de Broglie proposed", "de Broglie: matter as a wave")
def db(s):
    yield [FadeIn(left_at(lab("Louis de Broglie, 1924: matter works the same way", 26, INK, True), -7.0, 2.3))]
    p = Dot([-5.6, 0.6, 0], radius=0.16, color=BLUE)
    mom = Arrow([-5.4, 0.6, 0], [-4.2, 0.6, 0], buff=0, color=BLUE, stroke_width=5, tip_length=0.2)
    w = wave_between((-2.6, 0.6), (3.2, 0.6), 1.2, 0.45, BLUE, 5)
    yield [FadeIn(p), GrowArrow(mom), FadeIn(lab("momentum", 22, BLUE).next_to(mom, UP, buff=0.1)), GrowArrow(arrow([-3.9, 0.6, 0], [-2.8, 0.6, 0])), Create(w)]
    br = BraceBetweenPoints([-2.6 + 0.3, 1.2, 0], [-2.6 + 1.5, 1.2, 0], direction=UP, color=BLUE)
    yield [FadeIn(br), FadeIn(lab("wavelength", 22, BLUE).next_to(br, UP, buff=0.08)),
           FadeIn(at(VGroup(T("wavelength =", 28, BLUE, True), heq("h / momentum", 30, BLUE)).arrange(RIGHT, buff=0.2), -2.6, -1.3))]
    yield [FadeIn(at(VGroup(T("frequency =", 28, BLUE, True), heq("energy / h", 30, BLUE)).arrange(RIGHT, buff=0.2), -2.6, -2.3)),
           FadeIn(lab("the same two rules as for light, now for matter", 24, INK).move_to([0, -3.3, 0]))]


DG_D = 1.0
DG_XS = [-6.4 + DG_D * i for i in range(6)]
DG_Y = -1.6
DG_TH = np.radians(50)


def dg_geometry(stage):
    g = VGroup()
    a1, a2 = np.array([DG_XS[2], DG_Y, 0]), np.array([DG_XS[3], DG_Y, 0])
    u = np.array([-np.sin(DG_TH), np.cos(DG_TH), 0])
    if stage >= 0:
        g.add(*[Dot([x, DG_Y, 0], radius=0.14, color=INK) for x in DG_XS], left_at(lab("nickel crystal", 22), -7.0, DG_Y - 0.6))
    if stage >= 1:
        g.add(*[Arrow([a[0], 2.1, 0], [a[0], DG_Y + 0.18, 0], buff=0, color=BLUE, stroke_width=3, tip_length=0.15) for a in (a1, a2)],
              lab("electrons, straight down", 22, BLUE).move_to([(a1[0] + a2[0]) / 2 + 0.1, 2.4, 0]))
    if stage >= 2:
        L = 2.6
        g.add(*[Arrow(a, a + u * L, buff=0.1, color=BLUE, stroke_width=3, tip_length=0.16) for a in (a1, a2)])
    if stage >= 3:
        foot = a2 + np.dot(a1 - a2, u) * u
        g.add(DashedLine(a1, foot, color=MUTED, stroke_width=2), Line(a2, foot, color=ORANGE, stroke_width=7),
              left_at(lab("extra path", 22, ORANGE), a2[0] + 0.15, foot[1] + 0.1),
              BraceBetweenPoints(a1 + DOWN * 0.08, a2 + DOWN * 0.08, direction=DOWN, color=MUTED),
              lab("row spacing d", 22).move_to((a1 + a2) / 2 + DOWN * 0.95 + RIGHT * 0.9),
              Arc(radius=0.8, start_angle=PI / 2, angle=DG_TH, arc_center=a1, color=MUTED, stroke_width=3),
              T("θ", 24, MUTED).move_to(a1 + [-0.4, 1.05, 0]), left_at(lab("θ: exit angle", 22), -7.0, 0.6))
    return g


DG_AX = dict(x_range=[0, 90, 30], y_range=[0, 1.2, 0.5], x_length=5.4, y_length=2.6)


def dg_axes():
    ax = Axes(**DG_AX, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([3.9, -0.55, 0])
    names = VGroup(lab("electrons counted", 22).next_to(ax.y_axis, UP, buff=0.12).shift(RIGHT * 0.8),
                   lab("angle from the beam", 22).next_to(ax.x_axis, DOWN, buff=0.5))
    for v in (0, 30, 90):
        names.add(lab(f"{v}°", 22).next_to(ax.c2p(v, 0), DOWN, buff=0.12))
    return ax, names


def dg_count(g):
    return 0.35 * np.exp(-g / 60) + 0.75 * np.exp(-((g - 50) / 7) ** 2)


@slide("The third experiment tests that wavelength.", "Electrons bounce off a crystal")
def dg1(s):
    yield [FadeIn(dg_geometry(0))]
    yield [FadeIn(dg_geometry(1)[-3:]), FadeIn(left_at(lab("Davisson and Germer, 1927", 24, INK, True), 0.6, 2.45))]
    yield [FadeIn(left_at(lab("all with the same energy", 24, BLUE), 0.6, 2.0))]
    ax, names = dg_axes()
    yield [FadeIn(dg_geometry(2)[-2:]), Create(ax), FadeIn(names), FadeIn(left_at(lab("count them at each angle", 24, TEAL), 0.6, 1.55))]


def dg1_done(s):
    ax, names = dg_axes()
    s.add(dg_geometry(2), ax, names, left_at(lab("Davisson and Germer, 1927", 24, INK, True), 0.6, 2.45),
          left_at(lab("all with the same energy", 24, BLUE), 0.6, 2.0), left_at(lab("count them at each angle", 24, TEAL), 0.6, 1.55))
    return ax


def dg_peak(ax):
    return VGroup(ax.plot(dg_count, x_range=[2, 88], color=TEAL, stroke_width=5), DashedLine(ax.c2p(50, 0), ax.c2p(50, dg_count(50)), color=INK))


@slide("Particles bouncing off a rough surface would spread", "Electrons bounce off a crystal")
def dg2(s):
    ax = dg1_done(s)
    smooth = DashedVMobject(ax.plot(lambda g: 0.55 * np.exp(-g / 70), x_range=[2, 88], color=MUTED, stroke_width=3), num_dashes=30)
    cap = at(VGroup(lab("particles off a", 22, MUTED), lab("rough surface", 22, MUTED)).arrange(DOWN, buff=0.05), ax.c2p(78, 0)[0], ax.c2p(0, 0.5)[1])
    yield [Create(smooth), FadeIn(cap)]
    yield [Create(dg_peak(ax)), smooth.animate.set_color(RED), cap.animate.set_color(RED), FadeIn(lab("a clear peak", 24, TEAL, True).next_to(ax.c2p(50, dg_count(50)), RIGHT, buff=0.2))]


def dg2_done(s):
    ax = dg1_done(s)
    s.add(dg_peak(ax), lab("a clear peak", 24, TEAL, True).next_to(ax.c2p(50, dg_count(50)), RIGHT, buff=0.2))
    return ax


@slide("That's what a wave does when it bounces off evenly", "Waves from neighbouring rows")
def dg3(s):
    ax = dg2_done(s)
    yield [FadeIn(left_at(lab("a wave off evenly spaced rows of atoms", 22, INK), -7.0, -3.05)), Indicate(dg_geometry(0)[:6], color=INK)]
    yield [FadeIn(left_at(lab("neighbouring rows: different distances out", 22, INK), -7.0, -3.5))]
    yield [FadeIn(dg_geometry(3)[-8:])]


def dg3_done(s):
    ax = dg2_done(s)
    s.add(dg_geometry(3), left_at(lab("a wave off evenly spaced rows of atoms", 22, INK), -7.0, -3.05),
          left_at(lab("neighbouring rows: different distances out", 22, INK), -7.0, -3.5))
    return ax


@slide("When it equals one wavelength, the waves reinforce.", "Waves from neighbouring rows")
def dg4(s):
    ax = dg3_done(s)
    yield [FadeIn(at(T("extra path = one wavelength: they reinforce", 24, TEAL, True), 3.9, -3.1))]
    yield [FadeIn(at(T("most other angles: they cancel", 24, INK), 3.9, -3.5))]
    yield [FadeIn(at(T("peak angle + known spacing → wavelength", 24, BLUE, True), 3.9, -3.9)), Indicate(dg_peak(ax)[0], color=TEAL)]


def dg_table():
    rows = [("electron energy", "54 eV", INK), ("de Broglie: h / momentum", "0.167 nm", BLUE),
            ("peak at 50°: 0.215 nm × sin 50°", "0.165 nm", TEAL)]
    out = []
    for k, (a, b, c) in enumerate(rows):
        y = 0.9 - 1.0 * k
        out.append(VGroup(left_at(heq(a, 26, INK, FONT), -0.7, y), left_at(eq(b, 32, c), 5.1, y)))
    return out


@slide("The numbers match.", "The numbers match")
def dg5(s):
    s.add(dg_geometry(3))
    yield [FadeIn(left_at(T("Davisson and Germer, 1927", 28, INK, True), -0.7, 2.1))]
    t = dg_table()
    yield [FadeIn(t[0]), FadeIn(left_at(lab("an electron volt: a small energy unit", 22), -0.7, 0.45))]
    yield [FadeIn(t[1])]
    yield [FadeIn(t[2]), FadeIn(left_at(lab("row spacing d = 0.215 nm, known from X-ray diffraction", 22), -0.7, -1.65)), FadeIn(tick(t[2][1]))]


@slide("So matter really has a wavelength set by its momentum.", "Matter waves")
def dg6(s):
    a = at(VGroup(T("wavelength =", 32, BLUE, True), heq("h / momentum", 34, BLUE), check()).arrange(RIGHT, buff=0.3), 0, 1.0)
    yield [FadeIn(a), FadeIn(at(lab("confirmed by electrons on a crystal", 24, TEAL), 0, 0.2))]
    b = at(VGroup(T("frequency =", 32, BLUE, True), heq("energy / h", 34, BLUE)).arrange(RIGHT, buff=0.3), 0, -1.3)
    yield [FadeIn(b), FadeIn(at(lab("de Broglie's other rule", 24, INK), 0, -2.1))]


# ------------------------------------------------------------------ position and momentum operators
deck.part("Position and momentum operators")

PX_Y = -1.4


def x_axis(y=PX_Y, x0=-6.6, x1=6.6, name="position x"):
    ax = Arrow([x0, y, 0], [x1, y, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.18)
    return VGroup(ax, lab(name, 22).next_to(ax.get_end(), DOWN, buff=0.12).shift(LEFT * 0.6))


def spike(x, y=PX_Y, h=2.6, color=BLUE):
    pts_ = [[x - 0.6, y, 0], [x - 0.08, y, 0], [x, y + h, 0], [x + 0.08, y, 0], [x + 0.6, y, 0]]
    return VMobject(color=color, stroke_width=5).set_points_as_corners(pts_)


@slide("Position and momentum operators.", "The position operator")
def pos1(s):
    yield [FadeIn(x_axis()), FadeIn(at(T("start with position", 28, INK, True), -4.4, 2.2))]
    sp = spike(-2.0)
    yield [Create(sp), FadeIn(lab("a", 24, BLUE, True).next_to([-2.0, PX_Y, 0], DOWN, buff=0.15)),
           FadeIn(at(lab("its certain states: spikes at a single point", 24, BLUE), 2.4, 1.6))]


def pos_eq():
    return left_at(VGroup(T("position operator:", 26, PURPLE, True), eq("wave function → x × wave function", 26, PURPLE)).arrange(RIGHT, buff=0.25), -6.8, 2.3)


@slide("So the position operator multiplies the wave function", "The position operator")
def pos2(s):
    s.add(x_axis(), spike(-2.0), lab("a", 24, BLUE, True).next_to([-2.0, PX_Y, 0], DOWN, buff=0.15))
    yield [FadeIn(pos_eq()), FadeIn(left_at(lab("x: the position", 22), -6.8, 1.75))]
    sp2 = spike(-2.0, h=2.6 * 1.25, color=BLUE)
    yield [Create(sp2), FadeIn(left_at(VGroup(eq("x ×", 26, PURPLE), eq("spike at a  =  a × spike at a", 26, BLUE)).arrange(RIGHT, buff=0.15), 0.4, 0.4)),
           FadeIn(left_at(lab("its value is a", 26, INK, True), 0.4, -0.3))]


def cos_wave(ax, k=2.0):
    return ax.plot(lambda x: np.cos(k * x), x_range=[-3.2, 3.2], color=BLUE, stroke_width=4)


def wave_axes(y, h=1.4, yr=(-1.3, 1.3)):
    return Axes(x_range=[-3.2, 3.2, 1], y_range=[yr[0], yr[1], 1], x_length=9.0, y_length=h, tips=False,
                axis_config={"color": LINE, "include_ticks": False}).move_to([1.6, y, 0])


@slide("Now momentum.", "A wave of definite momentum")
def mom1(s):
    yield [FadeIn(at(T("now momentum", 28, INK, True), -5.6, 2.3))]
    a1 = wave_axes(1.1)
    w = cos_wave(a1)
    br = BraceBetweenPoints(a1.c2p(0, 1.05), a1.c2p(PI, 1.05), direction=UP, color=BLUE)
    yield [Create(a1), Create(w), FadeIn(br), FadeIn(lab("de Broglie's wavelength", 22, BLUE).next_to(br, UP, buff=0.05)),
           FadeIn(left_at(lab("a real wave, like a cosine", 22, BLUE), -6.9, 1.1))]
    a2 = wave_axes(-1.7, 1.4, (0, 1.2))
    d = a2.plot(lambda x: np.cos(2 * x) ** 2, x_range=[-3.2, 3.2], color=TEAL, stroke_width=4)
    yield [Create(a2), Create(d), FadeIn(left_at(lab("its density: crests and troughs", 22, TEAL), -6.9, -1.7))]
    peaks = VGroup(*[Dot(a2.c2p(x, 1), radius=0.08, color=ORANGE) for x in (-PI, -PI / 2, 0, PI / 2, PI)])
    yield [FadeIn(peaks), FadeIn(at(lab("the particle would prefer these places", 24, ORANGE), 1.0, -3.0))]


def complex_row(y, k=2.0, t=0.0, n=17, r=0.36, color=BLUE):
    xs = np.linspace(-3.2, 3.2, n)
    return VGroup(*[phasor([1.6 + x * 9.0 / 6.4, y], k * x - t, 1.0, r=r, color=color, ring=False, width=4) for x in xs])


@slide("But nothing about a free particle favours one place.", "A wave of definite momentum")
def mom2(s):
    a1 = wave_axes(1.1)
    a2 = wave_axes(-1.7, 1.4, (0, 1.2))
    d = a2.plot(lambda x: np.cos(2 * x) ** 2, x_range=[-3.2, 3.2], color=TEAL, stroke_width=4)
    cosw = VGroup(a1, cos_wave(a1), left_at(lab("a real wave, like a cosine", 22, BLUE), -6.9, 1.1))
    dens = VGroup(a2, d, left_at(lab("its density: crests and troughs", 22, TEAL), -6.9, -1.7))
    s.add(at(T("now momentum", 28, INK, True), -5.6, 2.3), cosw, dens)
    x_d = cross(d, RED, 4)
    yield [FadeIn(at(T("a free particle favours no place", 26, INK, True), 2.6, 2.3)), Create(x_d)]
    row = complex_row(1.1)
    yield [FadeOut(cosw), FadeIn(row), FadeIn(left_at(lab("a complex wave instead", 22, BLUE), -6.9, 1.1))]
    flat = a2.plot(lambda x: 0.8, x_range=[-3.2, 3.2], color=TEAL, stroke_width=5)
    yield [FadeOut(dens), FadeOut(x_d), Create(a2), Create(flat), FadeIn(left_at(lab("size one everywhere: flat density", 22, TEAL), -6.9, -0.95)),
           FadeIn(at(lab("its phase turns steadily along the line", 24, BLUE), 1.0, 0.1))]


def mom2_done(s):
    a2 = wave_axes(-1.7, 1.4, (0, 1.2))
    s.add(complex_row(1.1), left_at(lab("a complex wave", 22, BLUE), -6.9, 1.1), a2,
          a2.plot(lambda x: 0.8, x_range=[-3.2, 3.2], color=TEAL, stroke_width=5), left_at(lab("flat density", 22, TEAL), -6.9, -0.95))


@slide("It turns at a rate equal to the momentum divided", "h-bar")
def hbar1(s):
    mom2_done(s)
    yield [FadeIn(left_at(VGroup(T("rate of turning =", 26, BLUE, True), eq("momentum / ħ", 28, BLUE)).arrange(RIGHT, buff=0.2), -6.9, 2.35))]
    yield [FadeIn(left_at(VGroup(T("ħ, “h-bar” =", 26, PURPLE, True), eq("h / 2π", 28, PURPLE)).arrange(RIGHT, buff=0.2), 1.6, 2.35))]
    a1 = wave_axes(1.1)
    br = BraceBetweenPoints(a1.c2p(0, -0.45), a1.c2p(PI, -0.45), direction=DOWN, color=BLUE)
    yield [FadeIn(br), FadeIn(lab("one full turn, 2π: one de Broglie wavelength", 22, BLUE).next_to(br, DOWN, buff=0.05))]
    yield [FadeIn(at(VGroup(eq("ħ ≈ 1.055 × 10⁻³⁴ J s", 32, PURPLE)), 1.0, -3.4))]


def mom_need():
    return left_at(VGroup(T("needed:", 26, INK, True), eq("momentum operator (wave) = momentum × wave", 26, PURPLE)).arrange(RIGHT, buff=0.25), -6.9, 2.3)


@slide("The momentum operator has to give back this same wave,", "The momentum operator")
def pop1(s):
    yield [FadeIn(mom_need())]
    rows = VGroup(*[complex_row(y, k, r=0.3) for y, k in ((1.1, 1.2), (0.1, 2.0), (-0.9, 3.0))])
    tags = VGroup(*[left_at(lab(t, 22, BLUE), -6.9, y) for t, y in (("small momentum", 1.1), ("medium", 0.1), ("large", -0.9))])
    yield [FadeIn(rows), FadeIn(tags), FadeIn(at(lab("one operator for every momentum", 24, INK), 1.0, -1.75))]
    yield [FadeIn(at(T("taking the slope does it", 30, PURPLE, True), 1.0, -2.8))]


@slide("The slope of this wave is the wave itself,", "The momentum operator")
def pop2(s):
    s.add(mom_need())
    r1 = left_at(eq("slope of the wave  = i × (momentum / ħ) × wave", 28, BLUE), -6.9, 1.2)
    yield [FadeIn(r1)]
    r2 = left_at(eq("−i ħ × slope       = momentum × wave", 28, BLUE), -6.9, 0.2)
    yield [FadeIn(r2), FadeIn(tick(r2)), FadeIn(left_at(lab("(−i) × i = 1, and ħ cancels", 22), -6.9, -0.4))]
    box = at(card("momentum operator  =  −i ħ × (slope)", 9.0, 1.1, PURPLE, 32), 0, -2.0)
    yield [FadeIn(box, shift=UP * 0.15)]


@slide("Any wave function is a sum of such waves.", "The momentum operator")
def pop3(s):
    s.add(at(card("momentum operator  =  −i ħ × (slope)", 9.0, 1.1, PURPLE, 32), 0, 2.0))
    rows = VGroup(*[complex_row(y, k, r=0.3) for y, k in ((0.9, 1.2), (0.0, 2.0), (-0.9, 3.0))])
    tags = VGroup(*[left_at(lab(t, 22, BLUE), -6.9, y) for t, y in (("one momentum", 0.9), ("+ another", 0.0), ("+ another", -0.9))])
    yield [FadeIn(rows), FadeIn(tags), FadeIn(at(lab("any wave function: a sum of such waves", 24, BLUE), 0.6, -1.8))]
    yield [FadeIn(at(T("the operator acts on each term, so it works on every wave function", 26, PURPLE), 0, -2.7))]


COMM_ROWS = [("momentum first, then position", "−i ħ × slope of x² = −2i ħ x", "× x:  −2i ħ x²"),
             ("position first, then momentum", "x × x² = x³", "−i ħ × slope:  −3i ħ x²")]


def comm_row(k, part):
    y = (1.1, -0.3)[k]
    a, b, c = COMM_ROWS[k]
    return [left_at(T(a, 24, INK, True), -6.9, y + 0.35), left_at(eq(b, 26, BLUE), -6.9, y - 0.2),
            left_at(eq(c, 26, BLUE), 1.6, y - 0.2)][part]


@slide("Now the commutator.", "The commutator of position and momentum")
def comm1(s):
    yield [FadeIn(left_at(VGroup(T("try both orders on a test function:", 26, INK), eq("x²", 30, BLUE), lab("(position squared)", 22)).arrange(RIGHT, buff=0.25), -6.9, 2.35))]
    yield [FadeIn(comm_row(0, 0)), FadeIn(comm_row(0, 1)), FadeIn(comm_row(0, 2))]
    yield [FadeIn(comm_row(1, 0)), FadeIn(comm_row(1, 1)), FadeIn(comm_row(1, 2))]


def comm_base(s):
    s.add(left_at(VGroup(T("try both orders on a test function:", 26, INK), eq("x²", 30, BLUE), lab("(position squared)", 22)).arrange(RIGHT, buff=0.25), -6.9, 2.35),
          *[comm_row(k, p) for k in (0, 1) for p in (0, 1, 2)])


@slide("Subtract the second result from the first.", "The commutator of position and momentum")
def comm2(s):
    comm_base(s)
    yield [FadeIn(left_at(eq("−2i ħ x² − (−3i ħ x²)", 28, INK), -6.9, -1.4))]
    yield [FadeIn(left_at(VGroup(eq("= i ħ x²", 30, BLUE), lab("i ħ times the function we started with", 22, INK)).arrange(RIGHT, buff=0.3), -0.4, -1.4))]
    yield [FadeIn(left_at(lab("the same happens for every function", 24, INK), -6.9, -2.25))]
    yield [FadeIn(at(card("[position, momentum]  =  i ħ", 7.6, 1.0, PURPLE, 34), 0, -3.3), shift=UP * 0.15)]


@slide("Compare this with the last chapter.", "Bracket and commutator")
def cmp1(s):
    l = at(card(None, 6.6, 4.4, MUTED), -3.6, -0.4)
    r = at(card(None, 6.6, 4.4, PURPLE), 3.6, -0.4)
    yield [FadeIn(l), FadeIn(r), FadeIn(at(T("chapter 1", 28, MUTED, True), -3.6, 1.35)), FadeIn(at(T("this chapter", 28, PURPLE, True), 3.6, 1.35))]
    yield [FadeIn(at(eq("{q, p} = 1", 40, PURPLE), -3.6, 0.3)), FadeIn(at(lab("for every system", 24, INK), -3.6, -0.4))]
    yield [FadeIn(at(lab("every other bracket follows from it", 24, INK), -3.6, -1.5))]
    yield [FadeIn(at(eq("[x, p] = i ħ × 1", 40, PURPLE), 3.6, 0.3)), FadeIn(at(lab("the same 1, times i ħ", 24, INK), 3.6, -0.4))]


@slide("That suggests a rule for every quantity.", "The quantization rule")
def rule1(s):
    yield [FadeIn(at(T("a rule for every quantity", 28, INK), 0, 2.3))]
    r = at(VGroup(eq("{f, g}", 40, PURPLE), T("→", 40, INK), eq("[f, g] / (i ħ)", 40, PURPLE)).arrange(RIGHT, buff=0.4), 0, 1.2)
    yield [FadeIn(r), FadeIn(at(lab("bracket → commutator divided by i ħ", 24, INK), 0, 0.35))]
    yield [FadeIn(left_at(VGroup(eq("[A, B] = i × (an observable)", 28, PURPLE), lab("for two observables A and B", 22)).arrange(RIGHT, buff=0.3), -6.0, -1.0))]
    yield [FadeIn(left_at(VGroup(eq("÷ i  →  an observable", 28, TEAL), lab("real values, like a bracket's", 22, TEAL), check()).arrange(RIGHT, buff=0.3), -6.0, -1.9))]


@slide("And h-bar fixes the units.", "The quantization rule")
def rule2(s):
    s.add(at(T("a rule for every quantity", 28, INK), 0, 2.3),
          at(VGroup(eq("{f, g}", 40, PURPLE), T("→", 40, INK), eq("[f, g] / (i ħ)", 40, PURPLE)).arrange(RIGHT, buff=0.4), 0, 1.2))
    rows = [left_at(eq("[x, p]: position × momentum", 28, INK), -5.0, -0.4),
            left_at(eq("ħ:      J s = m × kg m/s, the same", 28, PURPLE), -5.0, -1.2),
            left_at(eq("{q, p}: no units", 28, INK), -5.0, -2.0)]
    yield [FadeIn(at(T("ħ fixes the units", 28, PURPLE, True), 0, 0.35)), FadeIn(rows[0])]
    yield [FadeIn(rows[1]), FadeIn(tick(rows[1]))]
    yield [FadeIn(rows[2])]


# ------------------------------------------------------------------ the energy moves the state
deck.part("The energy moves the state")


def spin_dial(c, ang, frac, r=0.75, color=BLUE, name=None):
    g = phasor(c, ang, frac, r=r, color=color, width=6)
    if name:
        g.add(T(name, 24, INK).next_to(g[0], DOWN, buff=0.15))
    return g


@slide("The energy moves the state.", "Split into definite energies")
def emove1(s):
    st = at(card("a state", 2.4, 0.9, BLUE, 28), -5.6, 0.4)
    yield [FadeIn(st)]
    parts = VGroup(*[spin_dial([-1.6 + 2.6 * k, 0.4], a, f, r=0.7, name=f"energy {k + 1}") for k, (a, f) in enumerate(((0.4, 0.8), (1.9, 0.6), (-0.8, 0.5)))])
    plus = VGroup(*[at(T("+", 34, INK), -0.3 + 2.6 * k, 0.4) for k in range(2)])
    yield [GrowArrow(arrow(st, parts[0])), FadeIn(parts), FadeIn(plus), FadeIn(at(lab("any state: a sum of states of definite energy", 24, INK), 0.6, 1.9))]
    yield [FadeIn(at(T("to move the state: learn how each one changes in time", 26, ORANGE, True), 0.0, -1.8))]


def turn_row_time(y, n=7, ang0=0.0, step=-0.7, r=0.36):
    xs = np.linspace(-1.2, 6.4, n)
    return VGroup(*[phasor([x, y], ang0 + step * i, 1.0, r=r, ring=True) for i, x in enumerate(xs)])


@slide("De Broglie's second rule says a state of definite energy", "A definite energy turns the phase in time")
def emove2(s):
    yield [FadeIn(left_at(VGroup(T("frequency =", 26, BLUE, True), heq("energy / h", 28, BLUE)).arrange(RIGHT, buff=0.2), -6.9, 2.35))]
    ang = ValueTracker(0.0)
    big = always_redraw(lambda: phasor([-5.0, 0.4], ang.get_value(), 1.0, r=0.9, width=6))
    yield [FadeIn(big), ang.animate.set_value(-2 * PI), FadeIn(left_at(VGroup(T("its phase turns at", 26, BLUE), eq("energy / ħ", 28, BLUE)).arrange(DOWN, buff=0.15, aligned_edge=LEFT), -6.9, -1.1))]
    sp = complex_row(1.6, 2.0, r=0.3)
    yield [FadeIn(sp), FadeIn(left_at(lab("definite momentum: phase turns along the line", 22, BLUE), -1.9, 0.95))]
    tr = turn_row_time(-0.6)
    tax = Arrow([-2.3, -1.3, 0], [6.6, -1.3, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.16)
    yield [FadeIn(tr), FadeIn(tax), FadeIn(lab("time", 22).next_to(tax.get_end(), DOWN, buff=0.1)),
           FadeIn(left_at(lab("definite energy: phase turns in time", 22, BLUE), -1.9, -1.8))]


@slide("A free particle with a definite momentum also has", "The free wave")
def free1(s):
    yield [FadeIn(at(T("a free particle with a definite momentum", 26, INK), 0, 2.35))]
    yield [FadeIn(at(VGroup(T("its energy =", 26, BLUE, True), eq("momentum² / (2 × mass)", 28, BLUE)).arrange(RIGHT, buff=0.2), 0, 1.65))]
    rows = VGroup(*[complex_row(y, 2.0, t=1.1 * i, r=0.3) for i, y in enumerate((0.6, -0.5, -1.6))])
    tags = VGroup(*[left_at(lab(t, 22), -6.9, y) for t, y in (("now", 0.6), ("a moment later", -0.5), ("later still", -1.6))])
    yield [FadeIn(rows), FadeIn(tags), FadeIn(at(lab("it turns in both space and time", 24, BLUE), 1.0, -2.45))]
    yield [FadeIn(at(pill("the free wave", BLUE, 28), 1.0, -3.3))]


def track_rows(t_val, sign):
    """Phasors along the line at time t, with phase k x - sign * w t, and the point of fixed phase."""
    k, w = 2.0, 1.0
    y = 0.5 if sign > 0 else -1.6
    xs = np.linspace(-3.2, 3.2, 17)
    row = VGroup(*[phasor([1.6 + x * 9.0 / 6.4, y], k * x - sign * w * t_val, 1.0, r=0.3, ring=False, width=4) for x in xs])
    x0 = (PI / 2 + sign * w * t_val) / k
    x0 = (x0 + PI) % (2 * PI) - PI if abs(x0) > 3.2 else x0
    mk = Dot([1.6 + x0 * 9.0 / 6.4, y + 0.6, 0], radius=0.11, color=ORANGE if sign > 0 else RED)
    return VGroup(row, mk)


@slide("Which way the phase turns in time is our choice", "Which way it turns in time")
def dir1(s):
    yield [FadeIn(at(T("which way does the phase turn in time?", 26, INK), 0, 2.35)),
           FadeIn(at(CurvedArrow(np.array([-1.3, 1.1, 0]), np.array([-2.3, 1.1, 0]), angle=PI, color=ORANGE), -1.8, 1.1)),
           FadeIn(at(CurvedArrow(np.array([1.3, 1.1, 0]), np.array([2.3, 1.1, 0]), angle=-PI, color=ORANGE), 1.8, 1.1)),
           FadeIn(at(lab("one way", 22), -1.8, 0.35)), FadeIn(at(lab("or the other", 22), 1.8, 0.35)),
           FadeIn(at(lab("a choice, at first", 22, INK), 0, -0.3))]
    yield [FadeIn(at(T("once the turn along the line is fixed, the two must turn opposite ways", 26, ORANGE, True), 0, -1.6))]


@slide("Follow a point where the phase stays fixed.", "Which way it turns in time")
def dir2(s):
    mom = Arrow([-6.8, 2.35, 0], [-5.2, 2.35, 0], buff=0, color=BLUE, stroke_width=6, tip_length=0.2)
    t1 = ValueTracker(0.0)
    t2 = ValueTracker(0.0)
    r1 = always_redraw(lambda: track_rows(t1.get_value(), 1))
    r2 = always_redraw(lambda: track_rows(t2.get_value(), -1))
    yield [GrowArrow(mom), FadeIn(lab("momentum", 22, BLUE).next_to(mom, RIGHT, buff=0.15)), FadeIn(r1), FadeIn(r2),
           FadeIn(left_at(lab("opposite turns", 24, INK, True), -6.9, 1.35)), FadeIn(left_at(lab("matching turns", 24, INK, True), -6.9, -0.75)),
           FadeIn(at(lab("follow the dot: a point of fixed phase", 22, ORANGE), 2.6, 2.35))]
    yield [t1.animate(rate_func=linear).set_value(2.0), FadeIn(left_at(lab("it moves the way the momentum points", 24, TEAL), -1.5, -0.25)),
           FadeIn(check().move_to([-2.0, -0.25, 0]))]
    yield [t2.animate(rate_func=linear).set_value(2.0), FadeIn(left_at(lab("it would move backwards", 24, RED), -1.5, -2.35)),
           FadeIn(cross(Square(0.35).move_to([-2.0, -2.35, 0]), RED, 5))]


@slide("A state of definite energy changes only by this overall phase.", "Stationary states")
def stat1(s):
    ang = ValueTracker(0.0)
    ph = always_redraw(lambda: phasor([-5.0, 0.6], ang.get_value(), 1.0, r=1.0, width=6))
    yield [FadeIn(ph), ang.animate.set_value(-3 * PI / 2), FadeIn(at(lab("only an overall phase turns", 24, BLUE), -5.0, -0.8))]
    ax = Axes(x_range=[0, 6, 1], y_range=[0, 1.2, 1], x_length=6.4, y_length=2.4, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([2.6, 0.4, 0])
    curve = ax.plot(lambda x: 0.9 * np.exp(-(x - 3) ** 2 / 1.5), x_range=[0, 6], color=TEAL, stroke_width=5)
    yield [Create(ax), Create(curve), FadeIn(lab("its density: the same at every time", 24, TEAL).next_to(ax, UP, buff=0.15)),
           FadeIn(at(lab("so every chance stays fixed", 24, INK), 2.6, -1.3))]
    yield [FadeIn(at(pill("stationary states", BLUE, 30), 0, -2.7))]


@slide("Next, the energy operator.", "The energy operator")
def eop(s):
    yield [FadeIn(at(T("the energy operator", 28, PURPLE, True), 0, 2.35))]
    h = left_at(VGroup(T("chapter 1:", 26, MUTED), eq("H = p² / 2m + V", 34, PURPLE)).arrange(RIGHT, buff=0.3), -6.4, 1.35)
    yield [FadeIn(h), FadeIn(left_at(lab("momentum² over twice the mass, plus the potential energy V", 24), -6.4, 0.75))]
    p = left_at(VGroup(eq("p  →  −i ħ × slope", 30, PURPLE), lab("put in the momentum operator", 24)).arrange(RIGHT, buff=0.3), -6.4, -0.3)
    yield [FadeIn(p)]
    r = left_at(eq("energy operator = −(ħ² / 2m) × (slope of the slope) + V", 26, PURPLE), -6.4, -1.5)
    yield [FadeIn(r), FadeIn(left_at(lab("applied twice: (−i ħ)² = −ħ²", 24, INK), -6.4, -2.15))]


@slide("Now we want an equation for the state.", "What the equation must do")
def want(s):
    yield [FadeIn(at(T("an equation for the state", 28, INK), 0, 2.2))]
    a = at(card("one rate of change in time,\nlike Hamilton's:\nthe state now fixes its future", 6.4, 2.2, BLUE, 28), -3.6, -0.2)
    yield [FadeIn(a, shift=UP * 0.15)]
    b = at(card("linear:\nsums of solutions\nare solutions", 6.4, 2.2, PURPLE, 28), 3.6, -0.2)
    yield [FadeIn(b, shift=UP * 0.15)]


SE_ROWS = [("i ħ × rate of change in time of the free wave", "= energy × wave", BLUE),
           ("energy operator on the free wave", "= (momentum² / 2m) × wave", PURPLE)]


def se_row(k, part):
    a, b, c = SE_ROWS[k]
    y = (1.6, 0.2)[k]
    return [left_at(T(a, 26, c, True), -6.9, y + 0.3), left_at(eq(b, 28, c), -6.9, y - 0.3)][part]


@slide("Take the free wave's rate of change in time,", "Building the Schrödinger equation")
def se1(s):
    yield [FadeIn(se_row(0, 0))]
    yield [FadeIn(se_row(0, 1))]
    yield [FadeIn(se_row(1, 0)), FadeIn(se_row(1, 1))]
    yield [FadeIn(left_at(VGroup(T("they agree, because energy = momentum² / 2m for a free particle", 24, TEAL), check()).arrange(RIGHT, buff=0.3), -6.9, -1.2))]


@slide("The equation that sets them equal is the Schrodinger", "The Schrödinger equation")
def se2(s):
    e = at(eq("i ħ × (rate of change of the state)  =  energy operator (state)", 26, PURPLE), 0, 1.4)
    yield [FadeIn(e), FadeIn(at(T("the Schrödinger equation", 34, PURPLE, True), 0, 2.3))]
    yield [FadeIn(at(eq("i ħ ∂Ψ/∂t = Ĥ Ψ", 30, PURPLE), 0, 0.75)), FadeIn(at(lab("one rate of change in time, and linear", 24, INK), 0, 0.1))]
    yield [FadeIn(at(lab("with a potential: the same equation, with V inside the energy operator", 24, INK), 0, -0.7))]
    yield [FadeIn(at(card("an assumption, which experiment has confirmed ever since", 10.4, 0.9, TEAL, 28), 0, -2.0))]


PROP_X = [-4.85, 0.0, 4.85]


def prop_frame(k):
    titles = ["1. linear", "2. keeps the total chance at one", "3. averages follow the bracket rule"]
    c = at(card(None, 4.6, 5.5, [BLUE, TEAL, PURPLE][k]), PROP_X[k], -0.6)
    t = at(words(titles[k], 18, 26, [BLUE, TEAL, PURPLE][k], align=ORIGIN), PROP_X[k], 1.6)
    return VGroup(c, t)


def prop_body(k, part):
    x = PROP_X[k]
    if k == 0:
        return [VGroup(*[phasor([x - 1.3 + 1.3 * i, 0.3], a, 0.8, r=0.45) for i, a in enumerate((0.3, 1.8, -1.0))],
                       lab("split into definite energies", 22, INK).move_to([x, -0.55, 0])),
                VGroup(lab("move each one,", 22, INK).move_to([x, -1.2, 0]), lab("then add them back", 22, INK).move_to([x, -1.6, 0]),
                       *[CurvedArrow(np.array([x - 1.3 + 1.3 * i + 0.5, 0.55, 0]), np.array([x - 1.3 + 1.3 * i - 0.05, 0.85, 0]), color=ORANGE, tip_length=0.12) for i in range(3)])][part]
    if k == 1:
        return [VGroup(phasor([x - 0.9, 0.3], 0.3, 0.9, r=0.55), phasor([x + 0.9, 0.3], -0.6, 0.9, r=0.55),
                       lab("each part's phase turns", 22, INK).move_to([x, -0.6, 0]), lab("its size never changes", 22, INK).move_to([x, -1.0, 0])),
                lab("no amplitude grows or shrinks", 22, TEAL).move_to([x, -1.6, 0]),
                VGroup(pill("unitary", TEAL, 26).move_to([x, -2.15, 0]), lab("keeps lengths and overlaps", 22).move_to([x, -2.65, 0]))][part]
    return [VGroup(lab("average of A changes at", 22, INK).move_to([x, 0.6, 0]), eq("⟨[A, energy]⟩ / iħ", 22, PURPLE).move_to([x, 0.15, 0])),
            VGroup(lab("position, momentum:", 22, INK).move_to([x, -0.6, 0]), lab("Hamilton's equations", 22, INK).move_to([x, -1.0, 0])),
            VGroup(lab("force averaged", 22, ORANGE).move_to([x, -1.8, 0]), lab("over the state", 22, ORANGE).move_to([x, -2.2, 0]))][part]


@slide("The equation has three properties.", "Three properties")
def props1(s):
    yield [FadeIn(prop_frame(0)[0]), FadeIn(prop_frame(1)[0]), FadeIn(prop_frame(2)[0])]
    yield [FadeIn(prop_frame(0)[1]), FadeIn(prop_body(0, 0))]
    yield [FadeIn(prop_body(0, 1))]


@slide("Second, it keeps the total chance at one.", "Three properties")
def props2(s):
    s.add(prop_frame(0), prop_frame(1)[0], prop_frame(2)[0], prop_body(0, 0), prop_body(0, 1))
    yield [FadeIn(prop_frame(1)[1])]
    yield [FadeIn(prop_body(1, 0))]
    yield [FadeIn(prop_body(1, 1))]
    yield [FadeIn(prop_body(1, 2))]


@slide("Third, averages follow the last chapter's bracket rule.", "Three properties")
def props3(s):
    s.add(prop_frame(0), prop_frame(1), prop_frame(2)[0], prop_body(0, 0), prop_body(0, 1), *[prop_body(1, i) for i in range(3)])
    yield [FadeIn(prop_frame(2)[1])]
    yield [FadeIn(prop_body(2, 0))]
    yield [FadeIn(prop_body(2, 1))]
    yield [FadeIn(prop_body(2, 2))]


UP_C = np.array([-5.4, 0.9, 0])
DN_C = np.array([-2.6, 0.9, 0])
SR = 1.0


def spin_pair(au, ad, labels=True):
    g = VGroup(phasor(UP_C, au, 0.866, r=SR, width=6), phasor(DN_C, ad, 0.5, r=SR, width=6))
    if labels:
        g.add(T("up", 26, INK, True).next_to(g[0][0], DOWN, buff=0.15), T("down", 26, INK, True).next_to(g[1][0], DOWN, buff=0.15))
    return g


@slide("Let's watch the tilted spin in time.", "The tilted spin in time")
def sit1(s):
    au = ValueTracker(0.0)
    up = always_redraw(lambda: phasor(UP_C, au.get_value(), 0.866, r=SR, width=6))
    pair = spin_pair(0, 0)
    yield [FadeIn(up), FadeIn(pair[1:]), FadeIn(left_at(lab("our tilted atoms: up 0.866, down 1/2", 24, BLUE), -6.9, 2.4))]
    yield [FadeIn(field_lines(2.4, 6.4, -2.6, 1.9, 4)), FadeIn(at(lab("left in the vertical field", 24), 4.4, 2.4))]
    yield [au.animate(rate_func=linear).set_value(-2 * PI), FadeIn(left_at(lab("up turns at a rate set by its energy", 22, BLUE), -6.9, -0.9))]


@slide("Its down part turns at a rate set by the other.", "The tilted spin in time")
def sit2(s):
    s.add(left_at(lab("our tilted atoms: up 0.866, down 1/2", 24, BLUE), -6.9, 2.4), field_lines(2.4, 6.4, -2.6, 1.9, 4),
          at(lab("left in the vertical field", 24), 4.4, 2.4), left_at(lab("up turns at a rate set by its energy", 22, BLUE), -6.9, -0.9),
          T("up", 26, INK, True).next_to(Circle(radius=SR).move_to(UP_C), DOWN, buff=0.15),
          T("down", 26, INK, True).next_to(Circle(radius=SR).move_to(DN_C), DOWN, buff=0.15))
    au, ad = ValueTracker(0.0), ValueTracker(0.0)
    pair = always_redraw(lambda: spin_pair(au.get_value(), ad.get_value(), labels=False))
    s.add(pair)
    yield [au.animate(rate_func=linear).set_value(-PI), ad.animate(rate_func=linear).set_value(-1.6 * PI),
           FadeIn(left_at(lab("down turns at a rate set by the other energy", 22, BLUE), -6.9, -1.35))]
    yield [au.animate.set_value(-PI + 1.2), ad.animate.set_value(-1.6 * PI + 1.2),
           FadeIn(left_at(lab("turning both by the same phase changes no chance", 22, INK), -6.9, -1.85))]
    yield [au.animate.set_value(0.0), ad.animate.set_value(-2 * PI),
           FadeIn(left_at(lab("only the difference matters: hold up fixed, turn down", 22, ORANGE, True), -6.9, -2.4))]


TT_AX = dict(x_range=[0, 1, 0.25], y_range=[0, 1, 0.25], x_length=5.4, y_length=3.2)
TIMES = [(0, "1/2", 0.933, "93.3%"), (0.25, "−i/2", 0.5, "50%"), (0.5, "−1/2", 0.067, "6.7%"), (0.75, "i/2", 0.5, "50%"), (1.0, "1/2", 0.933, "93.3%")]


def tt_axes():
    ax = Axes(**TT_AX, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([3.3, -0.6, 0])
    names = VGroup(lab("time, in turns of the down amplitude", 22).next_to(ax.x_axis, DOWN, buff=0.45),
                   lab("chance", 22, TEAL).next_to(ax.c2p(0, 0.45), LEFT, buff=0.2))
    for v, t in ((0, "0"), (0.25, "¼"), (0.5, "½"), (0.75, "¾"), (1, "1")):
        names.add(lab(t, 22).next_to(ax.c2p(v, 0), DOWN, buff=0.12))
    up = DashedLine(ax.c2p(0, 0.75), ax.c2p(1, 0.75), color=TEAL, stroke_width=4)
    return ax, names, VGroup(up, lab("up: 75%", 22, TEAL).next_to(ax.c2p(1, 0.75), RIGHT, buff=0.1))


def tt_point(ax, k):
    t, _, v, lbl = TIMES[k]
    d = Dot(ax.c2p(t, v), radius=0.09, color=TEAL)
    label = T(lbl, 22, TEAL, True)
    if v < 0.2:
        label.move_to(ax.c2p(t, 0.3))
    else:
        label.next_to(d, {0: UR, 0.25: DL, 0.75: DR, 1.0: UL}[t], buff=0.08)
    return VGroup(d, label)


def tt_down(k):
    t, val, _, _ = TIMES[k]
    return VGroup(phasor(DN_C, -2 * PI * t, 0.5, r=SR, width=6), T(val, 26, BLUE, True).next_to(Circle(radius=SR).move_to(DN_C), UP, buff=0.1))


def tt_left(k):
    return VGroup(phasor(UP_C, 0, 0.866, r=SR, width=6), T("up", 26, INK, True).next_to(Circle(radius=SR).move_to(UP_C), DOWN, buff=0.15),
                  T("down", 26, INK, True).next_to(Circle(radius=SR).move_to(DN_C), DOWN, buff=0.15),
                  T("0.866", 26, BLUE, True).next_to(Circle(radius=SR).move_to(UP_C), UP, buff=0.1), tt_down(k))


@slide("Follow the down amplitude through one full turn", "One full turn of the down amplitude")
def turn1(s):
    yield [FadeIn(tt_left(0)), FadeIn(left_at(lab("down, relative to up", 22, BLUE), -6.9, 2.45))]
    yield [FadeIn(left_at(VGroup(T("one full turn takes", 24, INK), eq("h / (energy gap)", 26, PURPLE)).arrange(RIGHT, buff=0.2), -6.9, -0.9))]
    ax, names, up = tt_axes()
    yield [Create(ax), FadeIn(names), Create(up[0]), FadeIn(up[1]), FadeIn(tt_point(ax, 0)),
           FadeIn(left_at(lab("start: 75% up, 93.3% right", 22, TEAL), -6.9, -1.45))]


def turn_base(s, upto):
    ax, names, up = tt_axes()
    s.add(left_at(lab("down, relative to up", 22, BLUE), -6.9, 2.45), ax, names, up,
          left_at(VGroup(T("one full turn takes", 24, INK), eq("h / (energy gap)", 26, PURPLE)).arrange(RIGHT, buff=0.2), -6.9, -0.9),
          *[tt_point(ax, k) for k in range(upto + 1)], lab("right", 22, TEAL).next_to(ax.c2p(0, 0.933), LEFT, buff=0.15))
    return ax


TURN_TXT = ["start: 75% up, 93.3% right", "a quarter turn: 75% up, 50% right", "half a turn: 75% up, 6.7% right",
            "three quarters: 50% right again", "a full turn: back where it started"]


@slide("A quarter turn later, it's still seventy-five percent up,", "One full turn of the down amplitude")
def turn2(s):
    ax = turn_base(s, 0)
    left = tt_left(0)
    t = ValueTracker(0.0)
    down = always_redraw(lambda: phasor(DN_C, -2 * PI * t.get_value(), 0.5, r=SR, width=6))
    val = left[4][1]
    s.add(left[:4], val, down, left_at(lab(TURN_TXT[0], 22, TEAL), -6.9, -1.45))
    for k in range(1, 5):
        yield [t.animate(rate_func=linear).set_value(TIMES[k][0]), Transform(val, tt_down(k)[1]), FadeIn(tt_point(ax, k)),
               FadeIn(left_at(lab(TURN_TXT[k], 22, TEAL), -6.9, -1.45 - 0.45 * k))]


@slide("The up and down chances never change,", "Size and phase")
def turn3(s):
    ax = turn_base(s, 4)
    s.add(tt_left(4))
    yield [Indicate(tt_axes()[2], color=TEAL), FadeIn(left_at(lab("up and down: depend only on the sizes", 22, TEAL, True), -6.9, -1.6))]
    curve = ax.plot(lambda t: 0.5 + 0.433 * np.cos(2 * PI * t), x_range=[0, 1], color=TEAL, stroke_width=5)
    yield [Create(curve), FadeIn(left_at(lab("sideways: swings with the relative phase", 22, TEAL, True), -6.9, -2.1))]


PR_O = np.array([-3.2, -1.6, 0])


def prec_tip(phi, L=2.6):
    t = np.radians(60)
    h = np.cos(phi) * U_RIGHT - np.sin(phi) * U_FRONT * 0.75
    return PR_O + L * (np.cos(t) * U_UP + np.sin(t) * h)


@slide("Physically, the spin's tilt swings around the field,", "Like a spinning top")
def prec(s):
    axes = VGroup(Arrow(PR_O, PR_O + UP * 3.6, buff=0, color=MUTED, stroke_width=3, tip_length=0.18), lab("field", 22).next_to(PR_O + UP * 3.6, UP, buff=0.08),
                  Arrow(PR_O, PR_O + U_RIGHT * 2.8, buff=0, color=LINE, stroke_width=3, tip_length=0.15), lab("right", 22).next_to(PR_O + U_RIGHT * 2.8, RIGHT, buff=0.08),
                  Arrow(PR_O, PR_O + U_FRONT * 2.4, buff=0, color=LINE, stroke_width=3, tip_length=0.15), lab("front", 22).next_to(PR_O + U_FRONT * 2.4, DOWN, buff=0.08))
    ring = ParametricFunction(lambda p: prec_tip(p), t_range=[0, TAU], color=LINE, stroke_width=3)
    phi = ValueTracker(0.0)
    tip = always_redraw(lambda: Arrow(PR_O, prec_tip(phi.get_value()), buff=0, color=BLUE, stroke_width=7, tip_length=0.22))
    drop = always_redraw(lambda: DashedLine(prec_tip(phi.get_value()), prec_tip(phi.get_value()) - 2.6 * np.cos(np.radians(60)) * U_UP,
                                            color=BLUE, stroke_width=2))
    yield [FadeIn(axes), Create(ring), FadeIn(tip), FadeIn(drop), phi.animate(rate_func=linear).set_value(TAU),
           FadeIn(left_at(lab("the tilt swings around the field", 24, BLUE), 1.4, 1.6))]
    yield [phi.animate(rate_func=linear).set_value(TAU + 1.5 * PI), FadeIn(left_at(lab("at three quarters: toward the front", 24, BLUE), 1.4, 0.9))]
    yield [FadeIn(left_at(VGroup(T("the front-tilted state:", 24, INK), eq("(0.866, i/2)", 26, BLUE)).arrange(RIGHT, buff=0.2), 1.4, 0.2))]


@slide("That turning is also why amplitudes must be complex.", "Why amplitudes are complex")
def why_c(s):
    yield [FadeIn(at(T("turning at a fixed size needs complex amplitudes", 28, INK), 0, 2.3))]
    c1 = np.array([-3.6, 0.2, 0])
    line = Line(c1 + LEFT * 1.6, c1 + RIGHT * 1.6, color=LINE, stroke_width=3)
    a = Arrow(c1, c1 + RIGHT * 1.2, buff=0, color=BLUE, stroke_width=6, tip_length=0.2)
    b = Arrow(c1, c1 + LEFT * 1.2, buff=0, color=BLUE, stroke_width=6, tip_length=0.2).set_opacity(0.4)
    yield [Create(line), GrowArrow(a), FadeIn(b), FadeIn(at(lab("real: it can only flip its sign", 24, INK), -3.6, -1.0))]
    c2 = np.array([3.6, 0.2, 0])
    ang = ValueTracker(0.3)
    ring = Circle(radius=1.2, color=LINE, stroke_width=3).move_to(c2)
    ar = always_redraw(lambda: Arrow(c2, c2 + 1.2 * np.array([np.cos(ang.get_value()), np.sin(ang.get_value()), 0]), buff=0, color=BLUE, stroke_width=6, tip_length=0.2))
    yield [Create(ring), FadeIn(ar), ang.animate.set_value(0.3 + 1.5 * PI), FadeIn(at(lab("complex: keeps its size and turns", 24, INK), 3.6, -1.4))]
    yield [FadeIn(at(card("The Hamiltonian now moves a list of amplitudes, instead of a point.", 13.0, 0.9, PURPLE, 28), 0, -2.8))]


# ------------------------------------------------------------------ uncertainty
deck.part("Position and momentum can't both be sharp")


def sharp_icons():
    ax = Axes(x_range=[-3, 3, 1], y_range=[0, 1.1, 1], x_length=4.0, y_length=1.6, tips=False, axis_config={"color": LINE, "include_ticks": False})
    sp = VGroup(ax, ax.plot(lambda x: np.exp(-x * x / 0.03), x_range=[-3, 3], color=TEAL, stroke_width=4))
    at(sp, -4.6, 0.6)
    return sp


@slide("Position and momentum can't both be sharp.", "Sharp means certain")
def sharp1(s):
    sp = sharp_icons()
    yield [FadeIn(sp), FadeIn(at(lab("sharp: certain to give one value", 24, INK, True), -4.6, 2.1))]
    sup = at(card("suppose: sharp position a\nand sharp momentum b, at once", 7.0, 1.6, ORANGE, 28), 3.0, 0.6)
    yield [FadeIn(sup, shift=UP * 0.15)]


def sharp_sup():
    return at(card("suppose: sharp position a\nand sharp momentum b, at once", 7.0, 1.6, ORANGE, 28), 3.0, 0.6)


@slide("Then both orders of the two operators would give", "Sharp means certain")
def sharp2(s):
    sp, sup = sharp_icons(), sharp_sup()
    s.add(sp, at(lab("sharp: certain to give one value", 24, INK, True), -4.6, 2.1), sup)
    r1 = left_at(eq("either order gives a × b times the state", 26, INK), -6.6, -1.0)
    yield [FadeIn(r1)]
    r2 = left_at(eq("so the commutator would give 0", 26, INK), -6.6, -1.7)
    yield [FadeIn(r2)]
    r3 = left_at(eq("but [position, momentum] = i ħ, not 0", 26, PURPLE), -6.6, -2.4)
    yield [FadeIn(r3), Indicate(r2, color=RED)]
    yield [Create(cross(sup, RED, 6).set_opacity(0.5)), FadeIn(at(T("no such state exists", 28, RED, True), 4.6, -0.8))]


def bell(ax, w, color):
    return ax.plot(lambda x: np.exp(-x * x / (2 * w * w)), x_range=[-4, 4], color=color, stroke_width=5)


def bell_names(a1, a2):
    return VGroup(lab("position", 22).next_to(a1, DOWN, buff=0.08), lab("momentum", 22).next_to(a2, DOWN, buff=0.08))


def bell_axes(x, y, name):
    ax = Axes(x_range=[-4, 4, 1], y_range=[0, 1.15, 1], x_length=5.6, y_length=1.9, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([x, y, 0])
    return ax, lab(name, 24, INK).next_to(ax, UP, buff=0.1)


def spread_bar(ax, w, color):
    return DoubleArrow(ax.c2p(-w, 0.6), ax.c2p(w, 0.6), buff=0, color=color, stroke_width=3, tip_length=0.12)


@slide("The best a state can do is keep both spreads small.", "The uncertainty relation")
def unc1(s):
    a1, n1 = bell_axes(-3.6, 0.9, "position density")
    a2, n2 = bell_axes(3.6, 0.9, "momentum density")
    yield [FadeIn(a1), FadeIn(n1), FadeIn(a2), FadeIn(n2), FadeIn(bell_names(a1, a2)), Create(bell(a1, 0.9, TEAL)), Create(bell(a2, 1.1, TEAL)),
           FadeIn(spread_bar(a1, 0.9, PURPLE)), FadeIn(spread_bar(a2, 1.1, PURPLE)),
           FadeIn(at(lab("keep both spreads small", 24, INK), 0, -0.55))]
    yield [FadeIn(at(lab("the commutator sets how small", 24, PURPLE), 0, -1.05))]
    yield [FadeIn(at(eq("position spread × momentum spread ≥ ħ / 2", 30, PURPLE), 0, -2.0)),
           FadeIn(at(T("the Heisenberg uncertainty relation", 26, PURPLE, True), 0, -2.7))]


@slide("Narrowing one spread forces the other to widen.", "The uncertainty relation")
def unc2(s):
    a1, n1 = bell_axes(-3.6, 0.9, "position density")
    a2, n2 = bell_axes(3.6, 0.9, "momentum density")
    w = ValueTracker(0.9)
    c1 = always_redraw(lambda: VGroup(bell(a1, w.get_value(), TEAL), spread_bar(a1, w.get_value(), PURPLE)))
    c2 = always_redraw(lambda: VGroup(bell(a2, 1.0 / w.get_value(), TEAL), spread_bar(a2, 1.0 / w.get_value(), PURPLE)))
    s.add(a1, n1, a2, n2, bell_names(a1, a2), c1, c2, at(eq("position spread × momentum spread ≥ ħ / 2", 30, PURPLE), 0, -2.0),
          at(T("the Heisenberg uncertainty relation", 26, PURPLE, True), 0, -2.7))
    yield [w.animate.set_value(0.4), FadeIn(at(lab("narrow one, and the other widens", 24, INK), 0, -0.6))]
    yield [FadeIn(at(lab("any two observables: a similar bound, set by their commutator", 24, INK), 0, -3.45))]


@slide("The bound is tiny in everyday units,", "An electron and a ball")
def unc3(s):
    yield [FadeIn(at(lab("tiny in everyday units: chapter 1 never needed it", 24, INK), 0, 2.35))]
    c = np.array([-4.2, 0.2, 0])
    atom = VGroup(Circle(radius=1.5, color=LINE, stroke_width=3).move_to(c), Dot(c, radius=0.12, color=INK))
    yield [FadeIn(atom), FadeIn(at(lab("an electron held within an atom", 24, BLUE), -4.2, -1.65)),
           FadeIn(left_at(eq("position spread: 0.1 nm", 28, BLUE), -1.6, 1.0))]
    yield [FadeIn(left_at(eq("velocity spread ≥ about 580 km/s", 28, ORANGE), -1.6, 0.2))]
    rng = np.random.default_rng(9)
    cloud = VGroup(*[Dot(c + 0.6 * np.array([a, b, 0]), radius=0.045, color=BLUE).set_opacity(0.6) for a, b in rng.normal(size=(90, 2)).clip(-2.2, 2.2)])
    yield [FadeIn(cloud), FadeIn(left_at(lab("so it can't be pictured as a little ball on a path", 26, INK, True), -1.6, -0.7))]


@slide("Now take the one kilogram ball from the last chapter,", "An electron and a ball")
def unc4(s):
    ball = Dot([-4.2, 0.4, 0], radius=0.45, color=BLUE)
    yield [FadeIn(ball), FadeIn(at(lab("the 1 kg ball from chapter 1", 24, BLUE), -4.2, -0.5)),
           FadeIn(left_at(eq("located to a micrometre", 28, BLUE), -1.6, 1.4))]
    yield [FadeIn(left_at(eq("velocity spread ≥ 5.3 × 10⁻²⁹ m/s", 28, ORANGE), -1.6, 0.6))]
    yield [FadeIn(left_at(lab("far below anything we could measure", 26, INK, True), -1.6, -0.2))]
    path = VMobject(color=LINE, stroke_width=3).set_points_smoothly([[-6.5, -2.9, 0], [-4.0, -1.6, 0], [-1.0, -1.3, 0], [2.0, -1.8, 0], [4.5, -3.0, 0]])
    b2 = Dot([-6.5, -2.9, 0], radius=0.14, color=BLUE)
    yield [Create(path), FadeIn(b2), MoveAlongPath(b2, path), FadeIn(left_at(lab("its state stays narrow as it moves", 24, BLUE), 0.2, -3.55))]


@slide("Across such a narrow state, the force barely changes.", "Why chapter 1 still works")
def unc5(s):
    ax = Axes(x_range=[-3, 3, 1], y_range=[0, 4.5, 1], x_length=7.0, y_length=4.0, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([-2.8, -0.6, 0])
    v = ax.plot(lambda x: 0.45 * x * x + 0.3, x_range=[-3, 3], color=MUTED, stroke_width=4)
    pk = ax.plot(lambda x: 0.3 + 0.45 * 1.4 * 1.4 + 1.2 * np.exp(-(x - 1.4) ** 2 / 0.004), x_range=[1.2, 1.6], color=BLUE, stroke_width=4)
    tan = Line(ax.c2p(0.9, 0.45 * 0.81 + 0.3 + 0.0), ax.c2p(1.9, 0.45 * 3.61 + 0.3), color=ORANGE, stroke_width=4)
    yield [Create(ax), Create(v), FadeIn(lab("potential energy", 22, MUTED).next_to(ax.c2p(-3, 4.35), RIGHT, buff=0.1)), FadeIn(pk),
           FadeIn(lab("a narrow state", 22, BLUE).next_to(ax.c2p(1.4, 2.4), UP, buff=0.4)),
           FadeIn(left_at(words("across it, the force, set by the slope of the potential, barely changes", 30, 24, ORANGE), 1.6, 1.0))]
    yield [Create(tan), FadeIn(left_at(words("averaged force = force at its center, so the averages obey chapter 1's equations", 30, 24, INK), 1.6, -0.8))]


@slide("A bell-shaped wave function shows the trade-off.", "The trade-off for a bell shape")
def fourier(s):
    yield [FadeIn(at(lab("position density", 26, INK, True), -3.8, 2.35)), FadeIn(at(lab("momentum density", 26, INK, True), 3.8, 2.35))]
    rows = []
    for y, sig, tag in ((1.0, 0.48, "narrow in position"), (-1.4, 1.2, "broad in position")):
        a1 = Axes(x_range=[-4, 4, 1], y_range=[0, 1.2, 1], x_length=5.6, y_length=1.5, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([-3.8, y, 0])
        a2 = a1.copy().move_to([3.8, y, 0])
        rows.append(VGroup(a1, a1.plot(lambda u, w=sig: np.exp(-u * u / (2 * w * w)), x_range=[-4, 4], color=TEAL, stroke_width=4),
                           a2, a2.plot(lambda u, w=1 / sig: np.exp(-u * u / (2 * w * w)), x_range=[-4, 4], color=TEAL, stroke_width=4),
                           left_at(lab(tag, 22, INK), -7.0, y + 0.95)))
    yield [FadeIn(rows[1][:2]), FadeIn(rows[1][4]), FadeIn(lab("position", 22).next_to(rows[1][0], DOWN, buff=0.08)),
           FadeIn(lab("momentum", 22).next_to(rows[1][2], DOWN, buff=0.08))]
    waves = VGroup(*[rows[1][0].plot(lambda u, k=k: 0.5 + 0.35 * np.cos(k * u), x_range=[-4, 4], color=BLUE, stroke_width=2).set_opacity(0.6)
                     for k in (0.8, 1.6, 2.4)])
    split = at(lab("split it into momentum waves", 22, BLUE), -3.8, -0.4)
    yield [FadeIn(waves), FadeIn(split)]
    yield [FadeOut(waves), FadeOut(split), FadeIn(rows[1][2:4]), FadeIn(rows[0]),
           FadeIn(at(lab("squeezed: a wider range of momentum waves", 22, INK), 3.8, -0.2))]
    yield [FadeIn(at(eq("for this shape: spread × spread = ħ / 2 exactly, the smallest allowed", 24, PURPLE), 0, -3.35))]


# ------------------------------------------------------------------ measurement
deck.part("What a measurement does")


@slide("What a measurement does.", "One more rule")
def meas1(s):
    yield [FadeIn(left_at(VGroup(T("so far: the chance of each outcome", 28, INK), check()).arrange(RIGHT, buff=0.3), -6.6, 1.9))]
    yield [FadeIn(left_at(T("one more rule: what happens afterwards?", 28, ORANGE, True), -6.6, 1.0))]
    mags, links, res, tk = row_parts(0)
    row = VGroup(*mags, *links, res)
    row.move_to([-0.5, -1.2, 0])
    yield [FadeIn(row), FadeIn(at(lab("the magnets in a row already showed it", 24, INK), -0.5, -2.3))]


CL_O = np.array([-3.4, -2.4, 0])
CL_R = 3.4


def cl_plane():
    return spin_plane(CL_O, CL_R)


@slide("After an ideal measurement, the state becomes", "Collapse")
def coll1(s):
    plane = cl_plane()
    st = state_arrow(CL_O, CL_R, np.cos(PI / 6), np.sin(PI / 6))
    s.add(plane, st)
    found = state_arrow(CL_O, CL_R, 1, 0, BLUE)
    yield [Transform(st, found), FadeIn(left_at(words("after an ideal measurement: the certain state of the result found", 30, 24, INK), 1.6, 1.6)),
           FadeIn(left_at(lab("result: up", 24, ORANGE, True), 1.6, 0.4))]
    yield [FadeIn(left_at(lab("measure again at once: up again", 24, INK), 1.6, -0.3))]
    yield [FadeIn(at(pill("collapse", ORANGE, 30), 3.6, -1.6))]


@slide("Take our tilted atoms to a sideways magnet.", "Collapse in the running example")
def coll2(s):
    o = np.array([-4.2, -1.6, 0])
    plane = spin_plane(o, 2.8)
    st = state_arrow(o, 2.8, np.cos(PI / 6), np.sin(PI / 6))
    yield [FadeIn(plane), GrowArrow(st), FadeIn(magnet("sideways", 0.6, 1.6, w=2.1, color=ORANGE)),
           FadeIn(left_at(lab("our tilted atoms: (0.866, 1/2)", 22, BLUE), -6.9, 2.4))]
    yield [FadeIn(left_at(T("93.3% go right", 28, TEAL, True), 2.0, 1.6))]
    k = 1 / np.sqrt(2)
    yield [Transform(st, state_arrow(o, 2.8, k, k, BLUE)), FadeIn(left_at(eq("now: right = (1/√2, 1/√2)", 26, BLUE), -0.6, 0.6)),
           FadeIn(left_at(lab("an even mix of up and down", 22, BLUE), -0.6, 0.05))]
    b1 = bar(1.0, -2.9, 0.5, hmax=2.0, w=0.9, label="50%")
    b2 = bar(2.6, -2.9, 0.5, hmax=2.0, w=0.9, label="50%")
    yield [FadeIn(b1), FadeIn(b2), FadeIn(lab("up", 22, INK).move_to([1.0, -3.2, 0])), FadeIn(lab("down", 22, INK).move_to([2.6, -3.2, 0])),
           FadeIn(left_at(words("vertical magnet now: 50% up, not the 75% from before", 18, 24, INK), 3.6, -1.6))]


@slide("The sideways measurement changed the state.", "Collapse versus the Schrödinger equation")
def coll3(s):
    yield [FadeIn(at(T("the sideways measurement changed the state", 26, INK), 0, 2.35))]
    l = at(card("Schrödinger equation:\nturns phases, keeps every\nlength and overlap", 5.6, 1.8, PURPLE, 26), -3.8, 0.6)
    r = at(card("collapse:\nloses information", 5.6, 1.8, ORANGE, 26), 3.8, 0.6)
    yield [FadeIn(l), FadeIn(r)]
    o = np.array([3.0, -3.1, 0])
    k = 1 / np.sqrt(2)
    many = VGroup(*[Arrow(o + 0.0 * RIGHT, o + 1.6 * np.array([np.cos(a), np.sin(a), 0]), buff=0, color=BLUE, stroke_width=4, tip_length=0.14).set_opacity(0.45)
                    for a in (0.2, 0.55, 1.1, 1.35)])
    res = Arrow(o + RIGHT * 2.8, o + RIGHT * 2.8 + 1.6 * np.array([k, k, 0]), buff=0, color=BLUE, stroke_width=6, tip_length=0.2)
    yield [FadeIn(many), GrowArrow(arrow(o + RIGHT * 1.7 + UP * 0.6, o + RIGHT * 2.6 + UP * 0.6)), GrowArrow(res),
           FadeIn(left_at(words("many states before, the same right after: you can't recover which", 34, 24, INK), -6.6, -2.3))]


@slide("These rules are enough to calculate every prediction", "What the rules mean")
def interp1(s):
    rules = at(card("state = amplitudes · operators · Born rule ·\nSchrödinger equation · collapse", 11.0, 1.4, BLUE, 28), 0, 1.5)
    yield [FadeIn(rules), FadeIn(at(lab("enough to calculate every prediction in this book", 24, TEAL), 0, 0.45))]
    yield [FadeIn(at(T("what they mean is still debated", 28, INK, True), 0, -0.7))]
    yield [FadeIn(at(card("Copenhagen view: the chances are fundamental", 9.0, 0.9, MUTED, 28), 0, -2.0))]


def bell_chart(stage):
    g = VGroup()
    base = -2.9
    g.add(Line([0.4, base, 0], [6.6, base, 0], color=LINE, stroke_width=3), Line([0.4, base, 0], [0.4, base + 3.2, 0], color=LINE, stroke_width=3),
          lab("a quantity Bell bounds", 22).rotate(PI / 2).move_to([0.05, base + 1.6, 0]))
    lim = DashedLine([0.4, base + 2.0, 0], [6.6, base + 2.0, 0], color=RED, stroke_width=4)
    if stage >= 1:
        g.add(lim, at(VGroup(lab("Bell's limit for", 22, RED), lab("local hidden details", 22, RED)).arrange(DOWN, buff=0.06), 6.0, base + 2.5))
    if stage >= 2:
        g.add(bar(1.4, base, 0.95, hmax=3.0, w=1.0, color=MUTED, opacity=0.6), lab("quantum mechanics", 22, MUTED).move_to([1.4, base - 0.3, 0]))
    if stage >= 3:
        g.add(bar(4.0, base, 0.93, hmax=3.0, w=1.0, color=TEAL), lab("experiments", 22, TEAL).move_to([4.0, base - 0.3, 0]))
    return g


@slide("It's tempting to think the chances hide some detail", "Hidden variables and Bell's limits")
def interp2(s):
    c = np.array([-4.6, 0.6, 0])
    atom = VGroup(Circle(radius=0.9, color=BLUE, stroke_width=3).move_to(c), T("?", 48, ORANGE, True).move_to(c))
    yield [FadeIn(atom), FadeIn(at(words("hidden details that fix each outcome?", 20, 24, INK, align=ORIGIN), -4.6, -0.9))]
    yield [FadeIn(at(pill("a hidden-variable theory", ORANGE, 26), -4.6, -2.0))]
    yield [FadeIn(bell_chart(1)), FadeIn(left_at(lab("Bell: limits any local hidden-variable theory must obey", 22, INK), -0.4, 2.3))]


@slide("Quantum mechanics predicts results that break those limits.", "Hidden variables and Bell's limits")
def interp3(s):
    c = np.array([-4.6, 0.6, 0])
    s.add(VGroup(Circle(radius=0.9, color=BLUE, stroke_width=3).move_to(c), T("?", 48, ORANGE, True).move_to(c)),
          at(words("hidden details that fix each outcome?", 20, 24, INK, align=ORIGIN), -4.6, -0.9), at(pill("a hidden-variable theory", ORANGE, 26), -4.6, -2.0),
          bell_chart(1), left_at(lab("Bell: limits any local hidden-variable theory must obey", 22, INK), -0.4, 2.3))
    yield [FadeIn(bell_chart(2)[-2:])]
    yield [FadeIn(bell_chart(3)[-2:])]
    yield [FadeIn(at(words("ruled out: hidden details that act only locally, given Bell's assumptions about locality and independence",
                           44, 22, RED, align=ORIGIN), 3.4, 1.15))]


@slide("They don't rule out every hidden-variable theory.", "Hidden variables and Bell's limits")
def interp4(s):
    yield [FadeIn(at(T("not every hidden-variable theory is ruled out", 28, INK), 0, 1.6))]
    yield [FadeIn(at(T("still open: hidden-variable theories whose details act at a distance", 26, ORANGE), 0, 0.6))]
    yield [FadeIn(at(card("Nobel Prize 2022: Aspect, Clauser and Zeilinger, for those experiments", 12.4, 1.0, TEAL, 28), 0, -1.1))]


# ------------------------------------------------------------------ where these tools come back
deck.part("Where these tools come back")


def ladder(x=3.4, y0=-2.6, n=6, gap=0.75, w=3.0):
    return VGroup(*[Line([x - w / 2, y0 + gap * k, 0], [x + w / 2, y0 + gap * k, 0], color=BLUE, stroke_width=5) for k in range(n)])


def spring_icon(x, y):
    wall = Line([x - 1.4, y - 0.5, 0], [x - 1.4, y + 0.5, 0], color=INK, stroke_width=5)
    pts_ = [[x - 1.4, y, 0]] + [[x - 1.2 + 0.18 * i, y + (0.18 if i % 2 == 0 else -0.18), 0] for i in range(8)] + [[x + 0.3, y, 0]]
    spr = VMobject(color=MUTED, stroke_width=3).set_points_as_corners(pts_)
    block = Square(0.6, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to([x + 0.6, y, 0])
    return VGroup(wall, spr, block)


@slide("Where these tools come back.", "Next: the harmonic oscillator")
def back1(s):
    yield [FadeIn(at(T("the next chapter: the harmonic oscillator", 28, INK, True), 0, 2.35))]
    yield [FadeIn(spring_icon(-4.6, 0.6)), FadeIn(at(lab("the spring from chapter 1", 24, BLUE), -4.6, -0.3))]
    yield [FadeIn(stat_note())]
    ld = ladder()
    yield [LaggedStart(*[Create(l) for l in ld], lag_ratio=0.15), FadeIn(lab("energies, evenly spaced", 24, BLUE).next_to(ld, UP, buff=0.2))]


def stat_note():
    return at(VGroup(lab("its stationary states,", 24, PURPLE), lab("from the commutator alone", 24, PURPLE)).arrange(DOWN, buff=0.08), -4.6, -1.15)


@slide("For that spring, the spacing is two point one", "Next: the harmonic oscillator")
def back2(s):
    ld = ladder()
    s.add(at(T("the next chapter: the harmonic oscillator", 28, INK, True), 0, 2.35), spring_icon(-4.6, 0.6), at(lab("the spring from chapter 1", 24, BLUE), -4.6, -0.3),
          stat_note(), ld, lab("energies, evenly spaced", 24, BLUE).next_to(ld, UP, buff=0.2))
    br = BraceBetweenPoints(ld[0].get_left() + LEFT * 0.1, ld[1].get_left() + LEFT * 0.1, direction=LEFT, color=PURPLE)
    yield [FadeIn(br), FadeIn(eq("2.1 × 10⁻³⁴ J", 26, PURPLE).next_to(br, LEFT, buff=0.15))]
    yield [FadeIn(left_at(eq("total energy: 2 J", 28, INK), -6.6, -2.3))]
    yield [FadeIn(left_at(lab("far too small to notice: the spring looks classical", 24, INK, True), -6.6, -3.3))]


@slide("The rule that turns a bracket into a commutator comes back", "Fields and time evolution")
def back3(s):
    r = at(VGroup(eq("{ , }", 34, PURPLE), T("→", 34, INK), eq("[ , ] / (i ħ)", 34, PURPLE), T("→ fields", 30, INK, True)).arrange(RIGHT, buff=0.35), 0, 1.9)
    yield [FadeIn(r)]
    pts_ = VGroup(*[Dot([x, -0.4, 0], radius=0.08, color=BLUE) for x in np.linspace(-5.6, 5.6, 9)])
    pairs = VGroup(*[eq("x, p", 22, PURPLE).next_to(d, UP, buff=0.12) for d in pts_])
    yield [FadeIn(Line([-6.2, -0.4, 0], [6.2, -0.4, 0], color=LINE, stroke_width=3)), FadeIn(pts_), FadeIn(pairs),
           FadeIn(at(lab("one pair of operators at every point of space", 24, INK), 0, -1.1))]
    yield [FadeIn(at(card("unitary time evolution → quantum field theory", 9.0, 0.9, TEAL, 28), 0, -2.6))]


@slide("So the Hamiltonian keeps its job,", "Two promises kept")
def finale(s):
    a = at(VGroup(eq("the Hamiltonian moves the state", 28, PURPLE), check()).arrange(RIGHT, buff=0.3), 0, 1.6)
    b = at(VGroup(eq("[position, momentum] = i ħ", 28, PURPLE), lab("they no longer commute", 24, INK), check()).arrange(RIGHT, buff=0.3), 0, 0.6)
    h = at(chip("H", PURPLE, size=34, h=0.9), -3.0, -0.8)
    amps = VGroup(*[phasor([-0.6 + 1.3 * k, -0.8], ang, f, r=0.5) for k, (ang, f) in enumerate(((0.3, 0.9), (1.6, 0.6), (-0.7, 0.7), (2.6, 0.5)))])
    yield [FadeIn(a), FadeIn(b), FadeIn(h), GrowArrow(arrow(h, amps)), FadeIn(amps),
           FadeIn(lab("a list of amplitudes, not a point", 22, BLUE).next_to(amps, DOWN, buff=0.15))]
    yield [FadeIn(at(pill("next: the harmonic oscillator, the spring made quantum", INK, 30), 0, -2.9))]

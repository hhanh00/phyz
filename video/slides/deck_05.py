"""Slides for chapter five, Relativistic Quantum Mechanics.

Every value comes from video/scripts/05-relativistic-qm.txt or
docs/relativistic-qm.md. The narration does not read formulas aloud, so each
formula is shown at the sentence that states it in words, in the page's
notation, set with MathTex (LaTeX). The drawings redraw the chapter's figures in
docs/manim/ (positron-track, relativistic-energy-solutions, dirac-sea-hole) as
animations, with the same geometry.

Colors: BLUE for positive energies and what has them (the upper energy curve,
+mc², the positive-energy wave and its arrow, an ordinary electron, the
positive-energy states), ORANGE for negative energies and what comes out of
them (the lower energy curve, −mc², the negative-energy wave and its arrow, the
sea, the hole, the trail the hole's particle left in Anderson's chamber, the
positron and other antiparticles), PURPLE for alpha and beta and the matrices
that stand for them (Z-hat, S-hat, the four matrices in space), TEAL for a
chance that works (never negative, total kept at one) and for checks that pass,
RED only for what fails or is ruled out (a negative chance, the endless fall, a
term that has to vanish, a rejected candidate), INK for equations and for the
sum of the two arrows, MUTED and LINE for apparatus, axes, packets of light,
context and connectors.
"""
from manim import *

from engine import *

STEM = "05-relativistic-qm"
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
    """Place a mobject with its right edge at x."""
    return mob.move_to([x - mob.width / 2, y, 0])


def lab(text, size=24, color=MUTED, bold=False):
    return T(text, size, color, bold)


def words(text, chars=40, size=26, color=INK, align=LEFT, bold=False):
    return W(text, chars, size, color, bold, align=align)


def mt(*tex, size=40, color=INK):
    """A formula in LaTeX. Several strings give parts that can be colored or revealed one by one."""
    return MathTex(*tex, color=color, font_size=size)


def ab(tex, size=40, color=INK):
    """A formula in which every alpha and beta is PURPLE."""
    m = MathTex(tex, substrings_to_isolate=[r"\alpha", r"\beta"], color=color, font_size=size)
    m.set_color_by_tex(r"\alpha", PURPLE)
    m.set_color_by_tex(r"\beta", PURPLE)
    return m


def paint(m, color, *parts):
    """Color some parts of a formula."""
    for k in parts:
        m[k].set_color(color)
    return m


def mix(*items, size=24, color=INK, buff=0.16, bold=False):
    """Words and formulas on one line."""
    return VGroup(*[T(i, size, color, bold) if isinstance(i, str) else i for i in items]).arrange(RIGHT, buff=buff)


def hold():
    """A step that adds nothing, so the next reveal waits for its sentence."""
    return [Wait()]


def tick(mob, color=TEAL, buff=0.2):
    return check(color).next_to(mob, RIGHT, buff=buff)


def xmark(mob, size=0.42, buff=0.2):
    return cross(Square(size).next_to(mob, RIGHT, buff=buff), RED, 6)


def hollow():
    """An invisible placeholder, so a redrawn group is never empty."""
    return Dot(ORIGIN, radius=0.001, fill_opacity=0, stroke_width=0)


def clock(s, rate=1.0):
    """Time that keeps running during holds, so the things drawn from it keep moving."""
    t = ValueTracker(0.0)
    t.rate = rate
    t.add_updater(lambda m, dt: m.increment_value(m.rate * dt))
    s.add(t)
    return t


def gated_clock(s, gate):
    """Time that runs at the rate held by the tracker `gate`, so a step can start it."""
    t = ValueTracker(0.0)
    t.add_updater(lambda m, dt: m.increment_value(gate.get_value() * dt))
    s.add(gate, t)
    return t


def note(mob, text, color=MUTED, direction=DOWN, size=24, buff=0.12, chars=30):
    """A brace on one side of a part of a formula, with a label."""
    b = Brace(mob, direction, color=color, buff=buff)
    t = words(text, chars, size, color, align=ORIGIN).next_to(b, direction, buff=0.12)
    return VGroup(b, t)


def frame(mob, color=PURPLE, buff=0.14, width=3):
    return SurroundingRectangle(mob, color=color, buff=buff, stroke_width=width, corner_radius=0.1)


def varrow(a, b, color=MUTED, width=4, tip=0.2):
    return Arrow(a, b, buff=0, color=color, stroke_width=width, tip_length=tip,
                 max_tip_length_to_length_ratio=0.4, max_stroke_width_to_length_ratio=30)


def wiggle(a, b, color=MUTED, amp=0.12, waves=5, width=4):
    """A packet of light: a wavy line from a to b, ending in an arrow tip."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    d = b - a
    L = np.linalg.norm(d)
    u = d / L
    n = np.array([-u[1], u[0], 0.0])
    body = L - 0.3
    pts = [a + u * body * f + n * amp * np.sin(TAU * waves * f) for f in np.linspace(0, 1, 70)]
    line = VMobject(color=color, stroke_width=width).set_points_smoothly(pts)
    return VGroup(line, varrow(pts[-1], b, color, width, 0.18))


def grid(rows, cols, cell=0.5, color=PURPLE, fill=0.08):
    """A table of numbers drawn as empty cells."""
    g = VGroup(*[Square(cell, stroke_color=color, stroke_width=2.5, fill_color=color, fill_opacity=fill)
                 .move_to(P((c - (cols - 1) / 2) * cell, ((rows - 1) / 2 - r) * cell))
                 for r in range(rows) for c in range(cols)])
    return g


def bump(x0, x1, y, amp, color, c=0.0, w=1.0, fill=0.25, width=4):
    """A bell-shaped curve on the line y, with the area under it shaded."""
    xs = np.linspace(x0, x1, 80)
    pts = [P(x, y + amp * np.exp(-((x - c) / w) ** 2)) for x in xs]
    curve = VMobject(color=color, stroke_width=width).set_points_smoothly(pts)
    area = Polygon(P(x0, y), *pts, P(x1, y), stroke_width=0, fill_color=color, fill_opacity=fill)
    return VGroup(area, curve)


def xaxis(x0, x1, y, text="position x", color=MUTED):
    ax = Arrow(P(x0, y), P(x1, y), buff=0, color=color, stroke_width=3, tip_length=0.16, max_tip_length_to_length_ratio=0.2)
    return VGroup(ax, lab(text, 22, color).next_to(ax, DOWN, buff=0.12).align_to(ax, RIGHT))


def electron(x, y, color=BLUE, r=0.13):
    return Dot(P(x, y), radius=r, color=color)


# ------------------------------------------------------------------ the formulas, as the page writes them

WAVE = r"\psi(x, t) = e^{i(px - Et)/\hbar}"
E_OP = r"i\hbar\,\frac{\partial}{\partial t}"
P_OP = r"-i\hbar\,\frac{\partial}{\partial x}"
P2_OP = r"-\hbar^2\,\frac{\partial^2}{\partial x^2}"
SLOW = r"E = p^2/2m"
REL = r"E^2 = (pc)^2 + (mc^2)^2"
KG1 = r"-\hbar^2\,\frac{\partial^2\psi}{\partial t^2} = -\hbar^2c^2\,\frac{\partial^2\psi}{\partial x^2} + m^2c^4\,\psi"
KG = r"\frac{1}{c^2}\frac{\partial^2\psi}{\partial t^2} - \frac{\partial^2\psi}{\partial x^2} + \frac{m^2c^2}{\hbar^2}\,\psi = 0"
ROOT = r"\sqrt{(pc)^2 + (mc^2)^2}"
RHO = r"\rho = \frac{E}{mc^2}\,\lvert\psi\rvert^2"
PSI2 = r"\lvert\psi\rvert^2"
LIN = r"E = \alpha\,pc + \beta\,mc^2"
ZHAT = r"\hat Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}"
SHAT = r"\hat S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}"
COL2 = r"\psi = \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}"
COL4 = r"\psi = \begin{pmatrix} \psi_1 \\ \psi_2 \\ \psi_3 \\ \psi_4 \end{pmatrix}"
REL3 = r"E^2 = (p_xc)^2 + (p_yc)^2 + (p_zc)^2 + (mc^2)^2"
SUM4 = r"\lvert\psi\rvert^2 = \lvert\psi_1\rvert^2 + \lvert\psi_2\rvert^2 + \lvert\psi_3\rvert^2 + \lvert\psi_4\rvert^2"
DT1 = r"\frac{\partial\psi}{\partial t}"
DT2 = r"\frac{\partial^2\psi}{\partial t^2}"


def schr(size=44):
    """The free Schrödinger equation in three parts: the time side, the equals sign, the space side."""
    return mt(r"i\hbar\,\frac{\partial\psi}{\partial t}", "=", r"-\frac{\hbar^2}{2m}\,\frac{\partial^2\psi}{\partial x^2}", size=size)


def rel(size=44):
    """The relativistic rule in parts: E², =, (pc)², +, (mc²)²."""
    return mt("E^2", "=", "(pc)^2", "+", "(mc^2)^2", size=size)


def kg(size=44):
    """The Klein–Gordon equation in parts: the time term, the minus sign, the space term, the mass term."""
    return mt(r"\frac{1}{c^2}\frac{\partial^2\psi}{\partial t^2}", "-", r"\frac{\partial^2\psi}{\partial x^2}",
              r"+ \frac{m^2c^2}{\hbar^2}\,\psi = 0", size=size)


def lin(size=44):
    """The straight-line rule in parts: E =, alpha, pc +, beta, mc²."""
    return paint(mt("E =", r"\alpha", r"\,pc", "+", r"\beta", r"\,mc^2", size=size), PURPLE, 1, 4)


def lin3(size=44):
    """The straight-line rule in space; parts 1, 3, 5 and 7 are the four matrices."""
    return paint(mt("E =", r"\alpha_x", r"\,p_xc +", r"\alpha_y", r"\,p_yc +", r"\alpha_z", r"\,p_zc +", r"\beta", r"\,mc^2",
                    size=size), PURPLE, 1, 3, 5, 7)


def squared(size=44):
    """The square of the straight-line rule; parts 1, 3 and 5 are its three terms."""
    m = mt("E^2 =", r"\alpha^2\,(pc)^2", "+", r"\beta^2\,(mc^2)^2", "+", r"(\alpha\beta + \beta\alpha)\,(pc)(mc^2)", size=size)
    m[1][0].set_color(PURPLE)
    m[3][0].set_color(PURPLE)
    for k in (1, 2, 4, 5):
        m[5][k].set_color(PURPLE)
    return m


def dirac(size=44):
    """The Dirac equation on a line; part 0 is the time side, parts 2 to 4 the slope term, parts 6 and 7 the mass term."""
    return paint(mt(r"i\hbar\,\frac{\partial\psi}{\partial t}", "=", r"-i\hbar c\,", r"\alpha", r"\,\frac{\partial\psi}{\partial x}",
                    "+", r"\beta", r"\,mc^2\,\psi", size=size), PURPLE, 3, 6)


def conditions(size=40):
    """The three conditions on alpha and beta, as three formulas in a row."""
    return VGroup(ab(r"\alpha^2 = 1", size), ab(r"\beta^2 = 1", size), ab(r"\alpha\beta + \beta\alpha = 0", size)).arrange(RIGHT, buff=0.9)


def cond_row(y=2.15, size=36):
    row = conditions(size)
    boxes = VGroup(*[frame(c, PURPLE, 0.18, 2) for c in row])
    return at(VGroup(row, boxes), 0, y)


def split_rows(m, top, bottom):
    """Color a column's entries by row: the upper half one color, the lower half the other. Tall brackets keep their color."""
    mid = m.get_center()[1]
    for g in m.family_members_with_points():
        if g.height > 0.6 * m.height:
            continue
        g.set_color(top if g.get_center()[1] > mid else bottom)
    return m


# ------------------------------------------------------------------ Anderson's chamber (docs/manim positron-track)

CH = (-3.6, -0.35)
CR = 2.6


def chamber(c=CH, R=CR):
    return Circle(radius=R, color=MUTED, stroke_width=3).move_to(P(*c))


def plate(c=CH, R=CR):
    return Rectangle(width=2 * R - 0.5, height=0.22, stroke_width=0, fill_color=INK, fill_opacity=0.85).move_to(P(*c))


def trail_low(c=CH, R=CR, color=ORANGE, side=1):
    """Below the plate: more energy, gently curved."""
    k = R / 2.75
    r = 6.0 * k
    p0 = P(c[0] + 0.55 * k * side, c[1] - 0.11)
    if side > 0:
        return Arc(radius=r, start_angle=-0.42, angle=0.42, arc_center=p0 + LEFT * r, color=color, stroke_width=5)
    return Arc(radius=r, start_angle=PI + 0.42, angle=-0.42, arc_center=p0 + RIGHT * r, color=color, stroke_width=5)


def trail_up(c=CH, R=CR, color=ORANGE, side=1):
    """Above the plate: less energy, tightly curved."""
    k = R / 2.75
    r = 2.1 * k
    p1 = P(c[0] + 0.55 * k * side, c[1] + 0.11)
    if side > 0:
        return Arc(radius=r, start_angle=0, angle=1.02, arc_center=p1 + LEFT * r, color=color, stroke_width=5)
    return Arc(radius=r, start_angle=PI, angle=-1.02, arc_center=p1 + RIGHT * r, color=color, stroke_width=5)


def trail_tip(up, color=ORANGE):
    tip, pre = up.point_from_proportion(1.0), up.point_from_proportion(0.9)
    return Arrow(pre, tip, buff=0, color=color, stroke_width=5, max_tip_length_to_length_ratio=1.2)


def sketch(c=CH, R=CR):
    """Anderson's photograph, sketched: the chamber, the plate and the trail."""
    up = trail_up(c, R)
    return VGroup(chamber(c, R), plate(c, R), trail_low(c, R), up, trail_tip(up))


# ------------------------------------------------------------------ energy against momentum (docs/manim relativistic-energy-solutions)

GO = (-2.9, -0.35)   # the graph's origin
GU = (1.2, 0.95)     # screen units for one unit of momentum and for one mc² of energy


def g2p(p, e, o=GO):
    return P(o[0] + GU[0] * p, o[1] + GU[1] * e)


def energy(p, sign=1):
    return sign * np.sqrt(1 + p * p)


def g_axes(o=GO):
    return VGroup(Line(g2p(-2.6, 0, o), g2p(2.6, 0, o), color=LINE, stroke_width=3),
                  Line(g2p(0, -2.8, o), g2p(0, 2.8, o), color=LINE, stroke_width=3),
                  right_at(lab("energy", 22), g2p(0, 0, o)[0] - 0.2, g2p(0, 2.62, o)[1]),
                  right_at(lab("momentum", 22), g2p(2.6, 0, o)[0], g2p(0, 0, o)[1] - 0.28))


def g_marks(o=GO, plus=True, minus=True):
    g = VGroup()
    if plus:
        g.add(DashedLine(g2p(-2.6, 1, o), g2p(2.6, 1, o), color=MUTED, stroke_width=2),
              right_at(mt("+mc^2", size=34, color=BLUE), g2p(-2.6, 1, o)[0] - 0.15, g2p(0, 1, o)[1]))
    if minus:
        g.add(DashedLine(g2p(-2.6, -1, o), g2p(2.6, -1, o), color=MUTED, stroke_width=2),
              right_at(mt("-mc^2", size=34, color=ORANGE), g2p(-2.6, -1, o)[0] - 0.15, g2p(0, -1, o)[1]))
    return g


def g_gap(o=GO, color=PALE, opacity=0.9):
    return Polygon(g2p(-2.6, 1, o), g2p(2.6, 1, o), g2p(2.6, -1, o), g2p(-2.6, -1, o), stroke_width=0, fill_color=color, fill_opacity=opacity)


def g_curve(sign, a=-2.5, b=2.5, o=GO, color=None, width=5):
    ps = np.linspace(a, b, 50)
    return VMobject(color=color or (BLUE if sign > 0 else ORANGE), stroke_width=width).set_points_smoothly(
        [g2p(p, energy(p, sign), o) for p in ps])


def g_dot(p, sign, o=GO, color=None, r=0.13):
    return Dot(g2p(p, energy(p, sign), o), radius=r, color=color or (BLUE if sign > 0 else ORANGE))


def g_ends(o=GO):
    """Arrowheads on the lower curve: it goes down without end."""
    return VGroup(*[Arrow(g2p(s * 2.15, energy(2.15, -1), o), g2p(s * 2.5, energy(2.5, -1), o), buff=0, color=ORANGE, stroke_width=5,
                          max_tip_length_to_length_ratio=0.6) for s in (-1, 1)])


def g_base(gap=True, lower=True, o=GO):
    g = VGroup()
    if gap:
        g.add(g_gap(o))
    g.add(g_axes(o), g_marks(o), g_curve(1, o=o))
    if lower:
        g.add(g_curve(-1, o=o), g_ends(o))
    return g


# ------------------------------------------------------------------ the sea (docs/manim dirac-sea-hole)

SX = (-5.0, 0.8)        # left and right edges of the two bands
TOPB = (0.7, 2.4)       # the positive-energy states, from +mc² up
SEAB = (-3.1, -0.8)     # the negative-energy states, from −mc² down
SEA_ROWS = (-1.1, -1.45, -1.8, -2.15, -2.5, -2.85)
HOLE = (0, 8)           # row and column of the electron that is lifted out


def sea_xy(r, c):
    return P(SX[0] + 0.35 + c * (SX[1] - SX[0] - 0.7) / 11, SEA_ROWS[r])


HX = sea_xy(*HOLE)[0]
EY = 1.5                # height of the ordinary electron in the upper band


def sea_bands():
    x0, x1 = SX
    top = Rectangle(width=x1 - x0, height=TOPB[1] - TOPB[0], stroke_color=BLUE, stroke_width=2, fill_color=PALE,
                    fill_opacity=0.5).move_to(P((x0 + x1) / 2, sum(TOPB) / 2))
    low = Rectangle(width=x1 - x0, height=SEAB[1] - SEAB[0], stroke_color=ORANGE, stroke_width=2, fill_color=ORANGE,
                    fill_opacity=0.12).move_to(P((x0 + x1) / 2, sum(SEAB) / 2))
    ax = Arrow(P(x0 - 0.6, -3.2), P(x0 - 0.6, 2.65), buff=0, color=MUTED, stroke_width=3, tip_length=0.18, max_tip_length_to_length_ratio=0.1)
    return VGroup(top, low, ax,
                  right_at(lab("energy", 22), x0 - 0.8, 2.45),
                  Line(P(x0 - 0.75, TOPB[0]), P(x0 - 0.45, TOPB[0]), color=MUTED, stroke_width=3),
                  Line(P(x0 - 0.75, SEAB[1]), P(x0 - 0.45, SEAB[1]), color=MUTED, stroke_width=3),
                  right_at(mt("+mc^2", size=34, color=BLUE), x0 - 0.9, TOPB[0]),
                  right_at(mt("-mc^2", size=34, color=ORANGE), x0 - 0.9, SEAB[1]))


def sea_dots(hole=False):
    return VGroup(*[Dot(sea_xy(r, c), radius=0.09, color=ORANGE) for r in range(6) for c in range(12) if not (hole and (r, c) == HOLE)])


def hole_ring():
    return Circle(radius=0.13, color=ORANGE, stroke_width=3.5).move_to(sea_xy(*HOLE))


def sea_base(hole=False):
    """The filled sea; with hole=True one electron has been lifted into the upper band."""
    g = VGroup(sea_bands(), sea_dots(hole))
    if hole:
        g.add(hole_ring(), electron(HX, EY), varrow(P(HX, SEA_ROWS[0] + 0.22), P(HX, EY - 0.22), INK))
    return g


# ------------------------------------------------------------------ chapter 3's ladder

def ladder(x, y0, n=5, gap=0.62, w=1.7, color=INK):
    return VGroup(*[Line(P(x - w / 2, y0 + k * gap), P(x + w / 2, y0 + k * gap), color=color, stroke_width=4) for k in range(n)])


def magnet(x, y, vertical=True, s=0.5):
    """Two pole pieces with a gap between them, standing for chapter 2a's magnet."""
    a = Rectangle(width=2.2 * s, height=0.7 * s, stroke_color=MUTED, stroke_width=3, fill_color=LINE, fill_opacity=1)
    b = a.copy()
    g = VGroup(a.shift(UP * 0.75 * s), b.shift(DOWN * 0.75 * s), varrow(P(0, -0.3 * s), P(0, 0.3 * s), MUTED, 3, 0.12))
    if not vertical:
        g.rotate(-PI / 2)
    return g.move_to(P(x, y))


# ================================================================== opening
deck.part("Chapter five")


@slide("Chapter five.", "Relativistic Quantum Mechanics")
def opening(s):
    c = (0.0, -0.35)
    up = trail_up(c)
    yield [FadeIn(chamber(c)), FadeIn(plate(c))]
    yield [Succession(Create(trail_low(c)), Create(up), GrowArrow(trail_tip(up)))]


# ================================================================== previously
deck.part("Previously")


@slide("The last chapter put the Schrodinger equation", "Relativity's test")
def prev(s):
    eq = at(schr(48), -2.2, 1.2)
    test = at(card("relativity's test", 3.4, 1.1, INK, 26), 4.2, 1.2)
    yield [FadeIn(at(lab("the Schrödinger equation", 24), -2.2, 2.35)), FadeIn(eq), GrowArrow(arrow(eq, test)), FadeIn(test),
           Create(xmark(test))]
    yield [FadeIn(note(eq[0], "one rate of change in time", INK, chars=16)), FadeIn(note(eq[2], "two slopes in space", INK, chars=16)),
           FadeIn(at(lab("time and space treated differently: only for slow particles", 24, RED), 0, -1.75))]
    yield [FadeIn(at(T("this chapter: the quantum equation for fast particles", 30, INK, True), 0, -2.85))]


# ================================================================== the chapter at a glance
deck.part("Chapter five")


def road_first():
    c = at(card("the first try", 3.2, 1.2, INK, 28), -5.2, 0.0)
    return VGroup(c, at(lab("quick to write down", 22), -5.2, -0.95))


def road_wrong(k):
    y = (1.3, -1.3)[k]
    c = at(card("something wrong", 3.3, 1.0, RED, 24), -0.6, y)
    return VGroup(c, varrow(P(-3.5, 0.3 * (1 - 2 * k)), c.get_left() + LEFT * 0.1))


def road_end(k):
    y = (1.3, -1.3)[k]
    text, color = (("fixed: 1928, Paul Dirac's\nnew equation", TEAL), ("stayed: it predicts a kind of\nmatter nobody had seen", ORANGE))[k]
    c = at(card(text, 4.6, 1.3, color, 24), 4.9, y)
    return VGroup(c, varrow(P(1.15, y), c.get_left() + LEFT * 0.1))


@slide("The first try is quick to write down", "Where the chapter goes")
def road1(s):
    yield [FadeIn(road_first())]
    yield [FadeIn(road_wrong(0), shift=RIGHT * 0.15), FadeIn(road_wrong(1), shift=RIGHT * 0.15)]
    yield [FadeIn(road_end(0), shift=RIGHT * 0.15)]


@slide("The other problem stayed.", "Where the chapter goes")
def road2(s):
    s.add(road_first(), road_wrong(0), road_wrong(1), road_end(0))
    yield [Indicate(road_wrong(1)[0], color=RED, scale_factor=1.05)]
    yield [FadeIn(road_end(1), shift=RIGHT * 0.15)]


# ------------------------------------------------------------------ the three equations side by side

TAB_Y = (1.5, 0.55, -0.4, -1.35, -2.3)
TAB_X = (-2.75, 1.25, 5.25)
TAB_NAMES = ("built from", "fast particles", "chance per metre", "the state", "energies")
TAB_HEADS = ("Schrödinger", "Klein–Gordon", "Dirac")
TAB_CELLS = ((("the low-speed energy", INK), ("the relativistic energy,\nsquared", INK), ("the relativistic energy,\nnot squared", INK)),
             (("fails", RED), ("works", TEAL), ("works", TEAL)),
             (("never negative", TEAL), ("can be negative", RED), ("never negative", TEAL)),
             (("one wave function", INK), ("one wave function", INK), ("four wave functions", PURPLE)),
             (("positive", BLUE), ("positive and negative", ORANGE), ("positive and negative", ORANGE)))


def tab_heads():
    return VGroup(*[at(T(h, 28, INK, True), x, 2.35) for h, x in zip(TAB_HEADS, TAB_X)])


def tab_name(r):
    return right_at(lab(TAB_NAMES[r], 22, MUTED), -4.85, TAB_Y[r])


def tab_cell(r, c):
    text, color = TAB_CELLS[r][c]
    if color == PURPLE:
        color = INK
    box = at(card(None, 3.8, 0.82, LINE), TAB_X[c], TAB_Y[r])
    lines = VGroup(*[T(t, 22, color) for t in text.split("\n")]).arrange(DOWN, buff=0.08).move_to(box)
    return VGroup(box, lines)


def tab_cells(pairs):
    return [FadeIn(tab_cell(r, c), shift=DOWN * 0.1) for r, c in pairs]


def tab_all(pairs, names):
    return VGroup(tab_heads(), *[tab_name(r) for r in names], *[tab_cell(r, c) for r, c in pairs])


@slide("Here's where we end up", "Three equations")
def tab1(s):
    yield [FadeIn(tab_heads())]
    yield [FadeIn(tab_name(0)), FadeIn(tab_name(1)), *tab_cells([(0, 0), (1, 0)])]


@slide("The Klein-Gordon equation works for fast", "Three equations")
def tab2(s):
    s.add(tab_all([(0, 0), (1, 0)], (0, 1)))
    yield tab_cells([(0, 1), (1, 1)])
    yield [FadeIn(tab_name(2)), *tab_cells([(2, 0), (2, 1)])]


@slide("Dirac's works for fast particles", "Three equations")
def tab3(s):
    s.add(tab_all([(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (2, 1)], (0, 1, 2)))
    yield tab_cells([(0, 2), (1, 2), (2, 2)])
    yield [FadeIn(tab_name(3)), *tab_cells([(3, 0), (3, 1), (3, 2)])]


@slide("And both relativistic equations allow", "Three equations")
def tab4(s):
    s.add(tab_all([(r, c) for r in range(4) for c in range(3)], (0, 1, 2, 3)))
    yield [FadeIn(tab_name(4)), *tab_cells([(4, 0), (4, 1), (4, 2)])]
    yield [FadeIn(caption("We start with the photograph that found the new matter.", -3.45))]


# ================================================================== a trail that bends the wrong way
deck.part("A trail that bends the wrong way")


@slide("A trail that bends the wrong way.", "Cosmic rays")
def cosmic(s):
    t = clock(s)
    starts = ((-5.5, 0.0), (-2.6, 0.45), (0.4, 0.2), (3.0, 0.7), (5.6, 0.35))

    def rays():
        g = VGroup(hollow())
        for x, ph in starts:
            f = (0.45 * t.get_value() + ph) % 1.0
            head = P(x + 1.2 * f, 2.6 - 4.3 * f)
            tail = P(x + 1.2 * max(f - 0.25, 0), 2.6 - 4.3 * max(f - 0.25, 0))
            g.add(Line(tail, head, color=LINE, stroke_width=6), Dot(head, radius=0.09, color=INK))
        return g
    ground = Line(P(-7.3, -1.85), P(7.3, -1.85), color=LINE, stroke_width=5)
    yield [FadeIn(at(T("1932: Carl Anderson", 32, INK, True), 0, -2.5)), FadeIn(ground)]
    s.add(always_redraw(rays))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(at(lab("cosmic rays: fast particles from space", 26, INK), 0, -3.15))]
    yield [FadeIn(at(lab("they also make chapter 4's muons", 24), 0, -3.7))]


@slide("He used a cloud chamber.", "A cloud chamber")
def cloud(s):
    f = ValueTracker(0.0)
    a, b = P(CH[0] - 1.9, CH[1] - 1.5), P(CH[0] + 1.7, CH[1] + 1.7)

    def drops():
        g = VGroup(hollow())
        n = int(26 * f.get_value())
        for k in range(n):
            g.add(Dot(a + (b - a) * k / 26 + P(0.05 * np.sin(7 * k), 0.05 * np.cos(5 * k)), radius=0.05, color=MUTED))
        if 0 < f.get_value() < 1:
            g.add(Dot(a + (b - a) * f.get_value(), radius=0.11, color=INK))
        return g
    s.add(f)
    yield [FadeIn(chamber()), FadeIn(left_at(T("a cloud chamber", 30, INK, True), 0.6, 1.3)),
           FadeIn(left_at(lab("a box of damp gas", 26, INK), 0.6, 0.6))]
    s.add(always_redraw(drops))  # added, not faded in: a redrawn object changes shape between frames
    yield [f.animate.set_value(1.0),
           FadeIn(left_at(words("a charged particle leaves a trail of droplets", 28, 26), 0.6, -0.7))]


def bend(side, color=INK):
    """A trail from the bottom of the chamber that bends to one side."""
    r = 3.0
    p0 = P(CH[0] + 0.45 * side, CH[1] - 2.2)
    if side > 0:
        return Arc(radius=r, start_angle=PI, angle=-1.0, arc_center=p0 + RIGHT * r, color=color, stroke_width=5)
    return Arc(radius=r, start_angle=0, angle=1.0, arc_center=p0 + LEFT * r, color=color, stroke_width=5)


@slide("A magnet around the chamber bent the trails.", "Reading a trail")
def magnet_bend(s):
    l, r = bend(-1), bend(1)
    yield [FadeIn(chamber()), FadeIn(left_at(words("a magnet around the chamber bends the trails", 34, 26), 0.6, 1.9))]
    yield [Create(l), Create(r), FadeIn(at(T("+", 40, INK, True), CH[0] - 1.5, CH[1] + 1.2)), FadeIn(at(T("−", 40, INK, True), CH[0] + 1.5, CH[1] + 1.2)),
           FadeIn(left_at(words("positive and negative charges bend opposite ways", 34, 26), 0.6, 0.6))]
    yield [FadeIn(left_at(words("so the bend tells the sign of the charge", 34, 26), 0.6, -0.7)),
           FadeIn(left_at(words("as long as you know which way the particle went", 34, 26, MUTED), 0.6, -1.9))]


@slide("To settle that, Anderson put a lead plate", "A lead plate")
def lead(s):
    low, up = trail_low(color=INK, side=-1), trail_up(color=INK, side=-1)
    yield [FadeIn(chamber()), FadeIn(plate()), FadeIn(at(lab("lead plate", 22, INK), CH[0] - 1.4, CH[1] + 0.4))]
    yield [Succession(Create(low), Create(up)), FadeIn(left_at(words("a particle loses energy in the lead", 36, 26), 0.6, 1.4)),
           FadeIn(left_at(words("with less energy, it bends more", 36, 26), 0.6, 0.5))]
    yield [GrowArrow(trail_tip(up, INK)),
           FadeIn(left_at(words("the tighter half of a trail is where the particle came out", 30, 26, INK, bold=True), 0.6, -1.3))]


def sketch_labels():
    cx, cy = CH
    rows = (("leaves with less energy:\ntighter curve", 1.3, (cx + 0.45, cy + 1.2)),
            ("loses energy in the lead", -0.35, (cx + CR - 0.2, cy)),
            ("enters with more energy:\ngentle curve", -2.0, (cx + 0.75, cy - 1.4)))
    g = VGroup()
    for text, y, tip in rows:
        t = left_at(VGroup(*[T(x, 24, INK) for x in text.split("\n")]).arrange(DOWN, buff=0.08, aligned_edge=LEFT), 1.0, y)
        g.add(VGroup(t, Line(P(*tip), P(0.8, y), color=MUTED, stroke_width=2)))
    return g


@slide("One photograph showed a trail that crossed", "The odd trail")
def odd(s):
    up = trail_up()
    labels = sketch_labels()
    yield [FadeIn(chamber()), FadeIn(plate()), FadeIn(at(lab("lead plate", 22, INK), CH[0] - 1.4, CH[1] + 0.4)),
           Succession(Create(trail_low()), Create(up), GrowArrow(trail_tip(up)))]
    yield [FadeIn(labels, lag_ratio=0.2)]
    yield [FadeIn(at(T("the bend of a positive charge", 28, INK, True), 4.3, 2.3))]


def known_particles():
    e = VGroup(electron(-3.6, 0.9, BLUE, 0.1), at(T("electron", 28, INK, True), -3.6, -0.3), at(lab("light, negative", 24, INK), -3.6, -0.9))
    p = VGroup(Circle(radius=0.85, color=MUTED, stroke_width=3, fill_color=LINE, fill_opacity=1).move_to(P(3.2, 0.9)),
               at(T("proton", 28, INK, True), 3.2, -0.3), at(lab("positive, about 1,800 times heavier", 24, INK), 3.2, -0.9))
    return e, p


@slide("As far as anyone knew then, matter held", "Two charged particles")
def known(s):
    e, p = known_particles()
    yield [FadeIn(at(lab("matter, as far as anyone knew in 1932: two kinds of charged particle", 24), 0, 2.3))]
    yield [FadeIn(e), FadeIn(at(T("−", 34, INK, True), -3.0, 0.9))]
    yield [FadeIn(p), FadeIn(at(T("+", 34, INK, True), 4.5, 0.9))]


def small_sketch():
    return sketch()


@slide("So a positive trail should have been a proton.", "A proton?")
def proton(s):
    s.add(small_sketch())
    up = trail_up()
    stub = Arc(radius=up.radius, start_angle=0, angle=0.102, arc_center=up.get_arc_center(), color=RED, stroke_width=10)
    out = np.array([np.cos(0.102), np.sin(0.102), 0.0])
    stop = VGroup(Line(stub.get_end() - 0.16 * out, stub.get_end() + 0.16 * out, color=RED, stroke_width=5),
                  Line(stub.get_end() + 0.25 * out, P(0.45, -1.75), color=RED, stroke_width=2))
    yield [FadeIn(left_at(T("positive, so a proton?", 28, INK, True), 0.6, 2.1))]
    yield [FadeIn(left_at(words("a proton is very heavy", 30, 26), 0.6, 1.1)),
           FadeIn(left_at(words("to bend that tightly, it would have to be slow", 36, 26), 0.6, 0.1))]
    yield [Create(stub), Create(stop),
           FadeIn(left_at(words("the gas stops a slow proton after about a tenth of the trail's length", 36, 26, RED), 0.6, -2.1))]


@slide("So the particle was positive, but far too light", "No known particle fits")
def nofit(s):
    s.add(small_sketch())
    a = left_at(T("positive", 28, INK, True), 0.6, 1.9)
    b = left_at(T("far too light to be a proton", 28, INK, True), 0.6, 1.1)
    yield [FadeIn(a), FadeIn(b)]
    c1 = left_at(chip("electron: negative", INK, size=24, h=0.7), 0.6, -0.3)
    c2 = left_at(chip("proton: too heavy", INK, size=24, h=0.7), 0.6, -1.3)
    yield [FadeIn(c1), FadeIn(c2), Create(xmark(c1)), Create(xmark(c2)),
           FadeIn(left_at(T("no known particle fit", 30, RED, True), 0.6, -2.5))]


@slide("So the puzzle is where a light, positive", "The puzzle")
def puzzle(s):
    q = VGroup(Circle(radius=0.5, color=ORANGE, stroke_width=4).move_to(P(-4.6, 0.6)), at(T("?", 40, ORANGE, True), -4.6, 0.6))
    paper = VGroup(Rectangle(width=2.6, height=3.3, stroke_color=INK, stroke_width=3, fill_color=PALE, fill_opacity=1).move_to(P(3.9, 0.2)),
                   *[Line(P(3.0, y), P(4.8, y), color=LINE, stroke_width=4) for y in (1.3, 0.85, 0.4, -0.05, -0.5, -0.95)])
    yield [FadeIn(q), FadeIn(at(words("where does a light, positive particle come from?", 24, 26, INK, ORIGIN), -4.6, -0.9))]
    yield [GrowArrow(varrow(P(-1.9, 0.3), P(2.3, 0.3))), FadeIn(paper), FadeIn(at(lab("the answer was already on paper", 26, INK, True), 3.9, -1.9))]
    yield [FadeIn(at(lab("it had come out the year before", 24), 3.9, -2.5))]


@slide("It came from an attempt to make quantum", "The attempt")
def attempt(s):
    a = at(card("quantum mechanics", 4.0, 1.3, INK, 28), -4.6, 0.9)
    b = at(card("relativity", 4.0, 1.3, INK, 28), 4.6, 0.9)
    j = at(card("an attempt to make them agree", 5.6, 1.2, INK, 26), 0, -1.2)
    yield [FadeIn(a), FadeIn(b)]
    yield [a.animate.shift(RIGHT * 2.2), b.animate.shift(LEFT * 2.2), FadeIn(j, shift=DOWN * 0.2)]
    yield [FadeIn(at(lab("the rest of this chapter follows that attempt", 26, INK), 0, -2.6))]


# ================================================================== an energy rule becomes an equation
deck.part("An energy rule becomes an equation")


def uvec(a):
    return np.array([np.cos(a), np.sin(a), 0.0])


def phasor(c, ang, r=0.5, color=BLUE, ring=True, width=5):
    """A complex number drawn as an arrow from c, in a circle of radius r."""
    c = P(*c)
    g = VGroup()
    if ring:
        g.add(Circle(radius=r, color=LINE, stroke_width=2).move_to(c))
    g.add(Arrow(c, c + r * uvec(ang), buff=0, color=color, stroke_width=width, tip_length=0.14,
                max_tip_length_to_length_ratio=0.45, max_stroke_width_to_length_ratio=30))
    return g


ROW_X = np.arange(-6.0, 6.01, 1.5)
ROW_Y = 1.55


def phase_row(t, y=ROW_Y, k=0.9, w=1.6, r=0.5):
    """The wave of a free particle: one arrow at each position, all turning in time."""
    return always_redraw(lambda: VGroup(*[phasor((x, y), k * x - w * t.get_value(), r) for x in ROW_X]))


def row_axis(y=ROW_Y - 0.8):
    return xaxis(-6.9, 7.0, y)


@slide("An energy rule becomes an equation.", "The recipe")
def recipe(s):
    a = at(card("a rule connecting\nenergy and momentum", 4.2, 1.5, INK, 26), -4.9, 0.9)
    r = at(card("the recipe", 2.6, 1.1, INK, 26, fill=PALE), 0, 0.9)
    b = at(card("a wave equation", 3.6, 1.5, INK, 26), 4.9, 0.9)
    yield [FadeIn(a), GrowArrow(arrow(a, r)), FadeIn(r), GrowArrow(arrow(r, b)), FadeIn(b)]
    yield [FadeIn(at(lab("chapter 2b built the Schrödinger equation this way", 26, INK), 0, -1.0))]
    yield [FadeIn(at(T("this chapter uses the recipe twice", 28, INK, True), 0, -2.2))]


@slide("Take a free particle with a definite momentum", "A free particle is a wave")
def freewave(s):
    t = clock(s)
    yield [FadeIn(row_axis()), FadeIn(at(lab("a free particle: a definite momentum p and a definite energy E", 26, INK), 0, -0.6))]
    yield [FadeIn(phase_row(t)), FadeIn(at(T("a wave whose phase turns steadily", 28, INK, True), 0, -1.6))]


@slide("The momentum sets how many turns it makes per metre", "A free particle is a wave")
def freewave2(s):
    t = clock(s)
    s.add(row_axis(), phase_row(t))
    yield [FadeIn(at(mix(mt("p/h", size=40), "turns per metre along the line", size=26), -3.4, -0.35))]
    yield [FadeIn(at(mix(mt("E/h", size=40), "turns per second in time", size=26), 3.7, -0.35))]
    w = at(mt(WAVE, size=52), 0, -2.1)
    yield [FadeIn(w), Create(frame(w, INK, 0.25, 2.5))]


def pull_row(k):
    y = (0.45, -1.5)[k]
    name, op, out, what = (("a rate of change in time", (r"i\hbar", r"\,\frac{\partial}{\partial t}"), "E", "the energy"),
                           ("a slope along the line", (r"-i\hbar", r"\,\frac{\partial}{\partial x}"), "p", "the momentum"))[k]
    o = at(mt(*op, size=48), -0.4, y)
    res = at(mt(out, size=60), 3.9, y)
    return VGroup(left_at(lab(name, 26, INK), -7.0, y), o, varrow(P(1.0, y), P(3.2, y)), at(lab("pulls out", 22), 2.0, y + 0.3), res,
                  left_at(lab(what, 26, INK), 4.6, y))


@slide("That earlier chapter found two operations", "Two operations")
def pull(s):
    w = at(mt(WAVE, size=40), 0, 2.15)
    yield [FadeIn(w), FadeIn(left_at(lab("the wave", 24), -7.0, 2.15))]
    r0, r1 = pull_row(0), pull_row(1)
    yield [FadeIn(r0, shift=RIGHT * 0.15)]
    yield [FadeIn(r1, shift=RIGHT * 0.15)]
    yield [Create(frame(r0[1][0], MUTED, 0.1, 2.5)), Create(frame(r1[1][0], MUTED, 0.1, 2.5)),
           FadeIn(at(lab("each comes with a constant factor", 24), -0.9, -2.75))]


OPS = (("E", E_OP), ("p", P_OP), ("p^2", P2_OP))
OPS_Y = (1.0, -0.55, -2.1)


def ops_heads():
    return VGroup(at(T("In the energy rule", 26, MUTED, True), -3.6, 2.3), at(T("In the wave equation", 26, MUTED, True), 2.4, 2.3))


def ops_left(k):
    y = OPS_Y[k]
    return VGroup(at(card(None, 4.6, 1.3, LINE), -3.6, y), at(mt(OPS[k][0], size=52), -3.6, y))


def ops_right(k):
    y = OPS_Y[k]
    return VGroup(varrow(P(-1.15, y), P(-0.05, y)), at(card(None, 4.6, 1.3, LINE), 2.4, y), at(mt(OPS[k][1], size=44), 2.4, y))


@slide("So here's the recipe.", "The recipe")
def ops1(s):
    yield [FadeIn(ops_heads())]
    yield [LaggedStart(*[FadeIn(ops_left(k), shift=DOWN * 0.1) for k in range(3)], lag_ratio=0.2)]
    yield [FadeIn(caption("swap each letter for its operation", -3.3, INK))]


@slide("Where the rule has the energy, write", "The recipe")
def ops2(s):
    s.add(ops_heads(), *[ops_left(k) for k in range(3)])
    yield [FadeIn(ops_right(0), shift=RIGHT * 0.15)]
    yield [FadeIn(ops_right(1), shift=RIGHT * 0.15)]
    yield [FadeIn(ops_right(2), shift=RIGHT * 0.15), FadeIn(left_at(lab("the slope, twice", 24), 4.95, OPS_Y[2]))]


def slow_rule(size=52):
    return mt("E", "=", "p^2", "/2m", size=size)


@slide("For example, take the slow free particle", "The free Schrödinger equation")
def example(s):
    rule = at(slow_rule(56), 0, 1.55)
    yield [FadeIn(at(lab("chapter 1: a slow free particle", 26, INK), 0, 2.45)), FadeIn(rule)]
    sw = VGroup(at(mt(r"E \;\to\; " + E_OP, size=38), -3.4, 0.0), at(mt(r"p^2 \;\to\; " + P2_OP, size=38), 3.4, 0.0))
    yield [FadeIn(sw), FadeIn(at(lab("the recipe", 24), 0, 0.0))]
    eq = at(schr(52), 0, -1.75)
    yield [TransformFromCopy(rule, eq), Create(frame(eq, INK, 0.25, 2.5)), FadeIn(at(lab("the free Schrödinger equation", 26, INK, True), 0, -3.1))]


@slide("It has one rate of change in time, and two", "One and two")
def mismatch(s):
    eq = at(schr(52), -3.2, 1.5)
    rule = at(slow_rule(56), 4.0, 1.5)
    s.add(eq)
    yield [FadeIn(note(eq[0], "one rate of change in time", INK, chars=14)), FadeIn(note(eq[2], "two slopes in space", INK, chars=14))]
    yield [FadeIn(rule), FadeIn(note(rule[0], "one power of the energy", INK, UP, chars=24)),
           FadeIn(note(rule[2], "two of the momentum", INK, chars=24))]
    m = at(T("that mismatch failed relativity's test", 30, RED, True), -0.3, -2.4)
    yield [FadeIn(m), Create(xmark(m))]


# ================================================================== the Klein–Gordon equation
deck.part("The Klein–Gordon equation")


@slide("The Klein-Gordon equation.", "The rule at any speed")
def anyspeed(s):
    r = at(rel(64), 0, 0.1)
    yield [FadeIn(at(lab("chapter 4: the rule that holds at any speed", 26, INK), 0, 2.45)), FadeIn(r)]
    yield [FadeIn(note(r[0], "the energy, squared", INK, UP, chars=24)), FadeIn(note(r[2], "the momentum, squared", INK, chars=24))]


@slide("Put it through the recipe.", "Through the recipe")
def kg_build(s):
    r = at(rel(44), 0, 2.2)
    k1 = at(mt(KG1, size=44), 0, 0.35)
    k2 = at(mt(KG, size=48), 0, -2.3)
    yield [FadeIn(r), GrowArrow(varrow(P(0, 1.75), P(0, 1.15))), FadeIn(left_at(lab("the recipe", 24), 0.25, 1.45))]
    yield [FadeIn(k1), FadeIn(right_at(mix("the time operation, twice:", mt(r"i\hbar \times i\hbar = -\hbar^2", size=36), size=24, color=MUTED), -0.3, 1.45))]
    yield [GrowArrow(varrow(P(-4.6, -0.5), P(-4.6, -1.3))),
           FadeIn(left_at(mix("divide by", mt(r"-\hbar^2c^2", size=36), "and move everything to one side", size=24, color=MUTED), -4.3, -0.9)),
           FadeIn(k2)]


@slide("This is the Klein-Gordon equation.", "The Klein–Gordon equation")
def kg_name(s):
    eq = at(kg(60), 0, 0.5)
    yield [FadeIn(eq), Create(frame(eq, INK, 0.35, 2.5)), FadeIn(at(T("the Klein–Gordon equation", 32, INK, True), 0, 2.2))]
    yield [FadeIn(at(lab("Oskar Klein and Walter Gordon, 1926", 28, INK), 0, -1.7))]


@slide("It passes the test.", "It passes the test")
def kg_test(s):
    eq = at(kg(56), 0, 1.0)
    yield [FadeIn(eq)]
    yield [FadeIn(note(eq[0], "two rates of change in time", INK, chars=14)), FadeIn(note(eq[2], "two slopes in space", INK, chars=14))]
    yield [Create(Circle(radius=0.3, color=TEAL, stroke_width=4).move_to(eq[1])),
           FadeIn(at(lab("a minus sign between them, like chapter 4's interval", 24, TEAL), -1.6, 2.35))]
    m = at(T("it keeps its form for every observer moving at a steady speed", 28, TEAL, True), -0.3, -2.7)
    yield [FadeIn(m), Create(tick(m))]


@slide("And it has the right waves.", "It has the right waves")
def kg_waves(s):
    w = at(mt(r"e^{i(px - Et)/\hbar}", size=48), -5.3, 1.3)
    box = at(card("the Klein–Gordon\nequation", 3.4, 1.5, INK, 26), -1.0, 1.3)
    r = at(rel(44), 4.6, 1.3)
    yield [FadeIn(w), FadeIn(at(lab("our wave", 24), -5.3, 2.2)), GrowArrow(arrow(w, box)), FadeIn(box)]
    yield [GrowArrow(varrow(P(0.85, 1.3), P(1.9, 1.3))), FadeIn(r), FadeIn(at(lab("holds exactly when", 24, INK), 4.6, 2.2))]
    a = at(card("a wave that fits the rule\nsolves it", 5.0, 1.4, TEAL, 26), -3.4, -1.6)
    b = at(card("a wave that doesn't fit\ndoesn't solve it", 5.0, 1.4, RED, 26), 3.2, -1.6)
    yield [FadeIn(a), Create(tick(a)), FadeIn(b)]


@slide("That all works.", "Two things wrong")
def kg_but(s):
    box = at(card("the Klein–Gordon\nequation", 3.8, 1.6, INK, 28), -4.6, 0.6)
    a = left_at(lab("passes relativity's test", 26, INK), -1.9, 1.1)
    b = left_at(lab("has the right waves", 26, INK), -1.9, 0.2)
    yield [FadeIn(box), FadeIn(a), Create(tick(a)), FadeIn(b), Create(tick(b))]
    yield [FadeIn(at(T("but two things are wrong with this equation", 28, INK, True), 0, -1.3)),
           FadeIn(at(card("first problem", 3.6, 1.0, RED, 26), -2.3, -2.5)), FadeIn(at(card("second problem", 3.6, 1.0, RED, 26), 2.3, -2.5))]


# ================================================================== first problem: negative energies
deck.part("First problem: negative energies")


@slide("First problem, negative energies.", "Two square roots")
def roots(s):
    r = at(rel(56), 0, 1.6)
    yield [FadeIn(r), Create(frame(r[0], INK, 0.12, 2.5))]
    yield [FadeIn(at(mix("the rule fixes", mt("E^2", size=40), ", not", mt("E", size=40), size=28), 0, 0.3))]
    yield [FadeIn(at(lab("a square has two square roots", 28, INK), 0, -0.8))]
    yield [FadeIn(at(mt(r"3^2 = 9", size=52), -2.6, -2.2)), FadeIn(at(mt(r"(-3)^2 = 9", size=52), 2.6, -2.2))]


@slide("So for every momentum, two energies fit", "Two energies")
def two_e(s):
    a = at(mt("E = +" + ROOT, size=52, color=BLUE), -1.2, 0.9)
    b = at(mt("E = -" + ROOT, size=52, color=ORANGE), -1.2, -1.5)
    yield [FadeIn(at(lab("for every momentum, two energies fit the rule", 26, INK), 0, 2.3)), FadeIn(a), FadeIn(at(lab("or", 26), -1.2, -0.3)), FadeIn(b)]
    yield [FadeIn(left_at(T("positive", 30, BLUE, True), 3.6, 0.9)), FadeIn(left_at(T("negative", 30, ORANGE, True), 3.6, -1.5))]


TXT = 1.5   # left edge of the text beside the graph


@slide("Take a particle at rest.", "A particle at rest")
def rest(s):
    yield [FadeIn(g_axes()), FadeIn(left_at(words("a particle at rest: its momentum is zero", 34, 26), TXT, 2.0))]
    yield [FadeIn(g_marks(minus=False)), FadeIn(g_dot(0, 1)),
           FadeIn(left_at(mix("the rule allows its rest energy,", mt("mc^2", size=38, color=BLUE), size=26), TXT, 0.6))]
    yield [FadeIn(g_marks(plus=False)), FadeIn(g_dot(0, -1)),
           FadeIn(left_at(mix("it also allows", mt("-mc^2", size=38, color=ORANGE), size=26), TXT, -1.3))]


@slide("Now give the particle some momentum.", "With some momentum")
def moving(s):
    p = ValueTracker(0.0)

    def draw():
        v = p.get_value()
        g = VGroup(g_dot(v, 1), g_dot(v, -1))
        if v > 0.05:
            g.add(g_curve(1, 0, v), g_curve(-1, 0, v))
        return g
    s.add(g_axes(), g_marks(), p, always_redraw(draw))
    yield [p.animate.set_value(1.1), FadeIn(left_at(lab("give the particle some momentum", 26, INK), TXT, 2.2))]
    yield [p.animate.set_value(2.5), FadeIn(left_at(lab("the positive energy goes up", 26, BLUE), TXT, 0.9)),
           FadeIn(left_at(lab("the negative one goes further down", 26, ORANGE), TXT, -1.6))]
    yield [Create(g_curve(1, 0, -2.5)), Create(g_curve(-1, 0, -2.5))]


def g_text(k):
    if k == 0:
        return VGroup(at(T("positive energies", 28, BLUE, True), 4.6, 1.75), at(lab("start at the rest energy and climb", 24, BLUE), 4.6, 1.2))
    return VGroup(at(T("negative energies", 28, ORANGE, True), 4.6, -1.7),
                  at(words("start at minus the rest energy and go down without end", 30, 24, ORANGE, ORIGIN), 4.6, -2.45))


def g_gaptext():
    return at(VGroup(lab("no energy allowed", 22), lab("in between", 22)).arrange(DOWN, buff=0.08), -4.5, 0.0)


@slide("The positive energies start at the rest energy", "Two curves and a gap")
def curves(s):
    s.add(g_axes(), g_marks(), g_curve(1), g_curve(-1))
    yield [FadeIn(g_text(0))]
    yield [FadeIn(g_text(1)), FadeIn(g_ends())]
    yield [FadeIn(g_gap().set_z_index(-1)), FadeIn(g_gaptext())]


def side_text(text, y, color=INK, bold=False, chars=34, size=25):
    return left_at(words(text, chars, size, color, bold=bold), TXT, y)


@slide("In classical physics, nobody worries.", "A thrown ball")
def classical(s):
    t = clock(s)
    low = VGroup(g_curve(-1), g_ends())
    s.add(g_base(lower=False), low)
    ball = always_redraw(lambda: g_dot(1.7 * np.sin(0.9 * t.get_value()), 1, color=INK, r=0.15))
    yield [FadeIn(ball), FadeIn(side_text("classical physics: the same rule holds for a thrown ball", 2.0))]
    yield [low[0].animate.set_stroke(opacity=0.2), low[1].animate.set_opacity(0.2),
           FadeIn(side_text("there we throw the negative root away", 0.8))]
    yield [FadeIn(side_text("that's safe: a classical particle's energy changes smoothly", -0.45))]
    wall = g_gap(color=RED, opacity=0.12)
    yield [FadeIn(wall), FadeIn(side_text("to reach a negative energy, it would have to pass through the forbidden gap", -2.0, RED))]


LAD = (-4.2, -2.3, 0.95)   # the ladder's centre x, its lowest rung, and the gap between rungs


def lad_y(k):
    return LAD[1] + k * LAD[2]


@slide("A quantum particle can jump.", "A whole rung at a time")
def jump(s):
    lad = ladder(LAD[0], LAD[1], 5, LAD[2], 2.4)
    m = Dot(P(LAD[0], lad_y(3) + 0.2), radius=0.15, color=INK)
    yield [FadeIn(lad), FadeIn(m), FadeIn(left_at(lab("chapter 3: a molecule's bond", 26, INK), -1.6, 2.0))]
    yield [m.animate(path_arc=-1.2).move_to(P(LAD[0], lad_y(2) + 0.2)),
           FadeIn(left_at(lab("its energy changed a whole rung at a time", 26, INK), -1.6, 0.9))]
    yield [FadeIn(left_at(lab("nothing in between was needed", 26, INK), -1.6, -0.1))]
    yield [Create(wiggle(P(LAD[0] + 0.6, lad_y(2) - 0.25), P(-1.9, -1.55))),
           FadeIn(left_at(words("anything that can lose energy by giving off light sooner or later does", 40, 26), -1.6, -1.7))]


@slide("So an electron with positive energy could drop", "One jump down")
def drop(s):
    s.add(g_base())
    e = g_dot(0.9, 1)
    yield [FadeIn(e), Flash(e, color=BLUE), FadeIn(side_text("an electron with positive energy", 2.0, BLUE))]
    mid = g2p(0.9, 0)
    yield [e.animate.move_to(g2p(0.9, energy(0.9, -1))).set_color(ORANGE), Create(wiggle(mid + P(0.25, 0.3), mid + P(1.9, 0.75))),
           FadeIn(side_text("it could drop to a negative-energy state in one jump, giving off the difference as a packet of light", 0.2))]
    yield [e.animate.move_to(g2p(1.9, energy(1.9, -1))), Create(wiggle(g2p(1.5, -1.7) + RIGHT * 0.3, g2p(1.5, -1.7) + P(1.9, 0.4))),
           FadeIn(side_text("then it could drop again, to a state lower still", -2.0))]


@slide("The spring's ladder has a lowest rung", "No lowest rung")
def nofloor(s):
    t = clock(s)
    lad = ladder(-4.2, -2.2, 5, 0.8, 2.4)
    floor = VGroup(Line(P(-5.6, -2.55), P(-2.8, -2.55), color=MUTED, stroke_width=6))
    m = Dot(P(-4.2, 1.2), radius=0.15, color=INK)
    yield [FadeIn(lad), FadeIn(floor), FadeIn(m), m.animate.move_to(P(-4.2, -2.0)),
           FadeIn(at(words("the spring's ladder has a lowest rung, so its fall has to stop", 34, 26, INK, ORIGIN), -4.2, 2.1))]
    ys = np.arange(1.2, -2.61, -0.55)
    rungs = VGroup(*[Line(P(2.6, y), P(5.0, y), color=ORANGE, stroke_width=4).set_opacity(1 - 0.1 * k) for k, y in enumerate(ys)])
    more = VGroup(varrow(P(3.8, -2.75), P(3.8, -3.45), ORANGE, 5))
    faller = always_redraw(lambda: Dot(P(3.8, ys[int(1.5 * t.get_value()) % len(ys)] + 0.2), radius=0.14, color=ORANGE))
    yield [FadeIn(rungs), FadeIn(more), FadeIn(faller), FadeIn(at(T("here there's no lowest rung", 28, ORANGE, True), 3.8, 2.1))]


@slide("So every electron in the world should keep falling", "Falling forever")
def forever(s):
    t = clock(s)
    s.add(g_base())
    steps = (0.3, 0.7, 1.1, 1.5, 1.9, 2.3)

    def draw():
        k = int(1.6 * t.get_value()) % (len(steps) + 1)
        g = VGroup(g_dot(0.3, 1) if k == 0 else g_dot(steps[k - 1], -1))
        for j in range(k):
            a = g2p(steps[j], 0.35 if j == 0 else energy(steps[j], -1) + 0.25) + RIGHT * 0.2
            g.add(wiggle(a, a + P(0.9, 0.3), amp=0.07, waves=3, width=3))
        return g
    s.add(always_redraw(draw))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(side_text("every electron in the world should keep falling, giving off light forever", 2.0, RED))]
    atom = VGroup(Circle(radius=0.7, color=MUTED, stroke_width=3).move_to(P(2.5, -0.9)), Dot(P(2.5, -0.9), radius=0.14, color=MUTED),
                  electron(3.2, -0.9))
    yield [FadeIn(atom), Create(cross(atom, RED, 5)), FadeIn(left_at(T("no atom would last", 28, RED, True), 3.7, -0.9))]
    yield [FadeIn(side_text("that doesn't happen", -2.6, INK, True, size=30))]


@slide("You might want to declare the negative energies", "Forbid them?")
def forbid(s):
    s.add(g_base())
    zone = DashedVMobject(Polygon(g2p(-2.6, -1.0), g2p(2.6, -1.0), g2p(2.6, -2.8), g2p(-2.6, -2.8), color=RED, stroke_width=4), num_dashes=50)
    yield [Create(zone), FadeIn(side_text("declare the negative energies forbidden?", 2.0))]
    yield [FadeIn(side_text("the equation won't let us", 0.9, INK, True, size=28))]
    w = left_at(VGroup(lab("a negative-energy", 22, ORANGE, True), lab("wave", 22, ORANGE, True)).arrange(DOWN, buff=0.08, aligned_edge=LEFT), TXT, -0.6)
    box = at(card("the Klein–Gordon\nequation", 2.6, 1.3, INK, 24), 6.15, -0.6)
    m = side_text("a negative-energy wave is a solution like any other", -2.3, ORANGE)
    yield [FadeIn(w), GrowArrow(arrow(w, box)), FadeIn(box), FadeIn(m), Create(tick(m[-1]))]


# ================================================================== second problem: a negative chance
deck.part("Second problem: a negative chance")

CHY = -1.7   # the axis under the chance curves


def chance_axis(y=CHY):
    return xaxis(-6.8, 1.4, y)


def chance_bump(c=-3.4, color=TEAL, y=CHY, amp=2.6):
    return bump(-6.6, 1.2, y, amp, color, c, 1.1)


def psi2_label(x=-3.4, y=1.35, color=TEAL):
    return at(mt(PSI2, size=48, color=color), x, y)


def right_text(text, y, color=INK, bold=False, chars=28, size=25):
    return left_at(words(text, chars, size, color, bold=bold), 2.3, y)


@slide("Second problem, a negative chance.", "What the wave function is for")
def chance1(s):
    b = chance_bump()
    yield [FadeIn(chance_axis()), Create(b[1]), FadeIn(b[0])]
    yield [FadeIn(psi2_label()), FadeIn(right_text("the squared length of the wave function", 1.2))]
    yield [FadeIn(right_text("is the chance per metre of finding the particle", -0.3, TEAL, True))]


@slide("Two things make that work.", "Why it works as a chance")
def chance2(s):
    b = chance_bump()
    one = at(lab("total = 1", 26, TEAL, True), -3.4, -0.9)
    s.add(chance_axis(), b, psi2_label())
    a = right_text("it's never negative", 1.6)
    yield [FadeIn(a), Create(tick(a[-1]))]
    c = right_text("its total over all positions is one, and stays one", 0.4)
    yield [FadeIn(one), FadeIn(c), Create(tick(c[-1]))]
    yield [VGroup(b, one).animate.shift(RIGHT * 0.6), FadeIn(right_text("the Schrödinger equation keeps that total at one", -1.1, TEAL, True))]


def two_waves(t, r=0.8):
    return always_redraw(lambda: VGroup(phasor((-4.2, 0.5), -1.3 * t.get_value(), r, BLUE, width=6),
                                        phasor((4.2, 0.5), 1.3 * t.get_value(), r, ORANGE, width=6)))


@slide("The Klein-Gordon equation doesn't have to.", "Two waves, one momentum")
def twowaves(s):
    t = clock(s)
    yield [FadeIn(at(T("the Klein–Gordon equation doesn't have to keep the total at one", 28, RED, True), 0, 2.3))]
    yield [FadeIn(two_waves(t)), FadeIn(at(mt(r"e^{i(px - Et)/\hbar}", size=44, color=BLUE), -4.2, -1.0)),
           FadeIn(at(lab("a positive-energy wave", 24, BLUE), -4.2, -1.75)),
           FadeIn(at(mt(r"e^{i(px + Et)/\hbar}", size=44, color=ORANGE), 4.2, -1.0)),
           FadeIn(at(lab("the negative-energy wave", 24, ORANGE), 4.2, -1.75)), FadeIn(at(lab("the same momentum p", 24, INK), 0, 0.5))]
    m = at(T("the equation accepts both", 28, INK, True), 0, -2.9)
    yield [FadeIn(m), Create(tick(m))]


SUMX = (-5.4, -1.8, 1.8, 5.4)


def parrow(a, b, color, width=5):
    return Arrow(a, b, buff=0, color=color, stroke_width=width, tip_length=0.14, max_tip_length_to_length_ratio=0.45,
                 max_stroke_width_to_length_ratio=30)


def pair(c, a, th, r=0.65):
    """Two arrows tip to tail, turned by a ∓ th, and their sum from the same starting point."""
    c = P(*c)
    tip1 = c + r * uvec(a - th)
    tip2 = tip1 + r * uvec(a + th)
    g = VGroup(Circle(radius=2 * r, color=LINE, stroke_width=2).move_to(c), Dot(c, radius=0.05, color=MUTED))
    if np.linalg.norm(tip2 - c) > 0.12:
        g.add(parrow(c, tip2, INK, 11))
    g.add(parrow(c, tip1, BLUE, 6), parrow(tip1, tip2, ORANGE, 6))
    return g


def sum_row(t, y=0.55, k=0.45, w=1.3, r=0.65):
    """At each position the positive-energy arrow (BLUE), the negative-energy arrow (ORANGE) and their sum (INK)."""
    return always_redraw(lambda: VGroup(*[pair((x, y), k * x, w * t.get_value(), r) for x in SUMX]))


def sum_formula(y=2.25):
    return at(paint(paint(mt(r"\psi =", r"e^{i(px - Et)/\hbar}", "+", r"e^{i(px + Et)/\hbar}", size=44), BLUE, 1), ORANGE, 3), 0, y)


def sum_legend(y=-3.35):
    return at(VGroup(lab("positive-energy wave", 22, BLUE), lab("negative-energy wave", 22, ORANGE), lab("their sum", 22, INK, True)).arrange(RIGHT, buff=0.7), 0, y)


@slide("And when two waves each solve it, so does their sum.", "The sum of the two")
def sum1(s):
    gate = ValueTracker(0.0)
    t = gated_clock(s, gate)
    yield [FadeIn(sum_formula()), FadeIn(left_at(lab("their sum solves it too", 24), 3.9, 2.25))]
    yield [FadeIn(xaxis(-6.9, 7.0, -1.0)), FadeIn(sum_row(t)), FadeIn(sum_legend()),
           FadeIn(at(lab("along the line, both arrows turn the same way", 26, INK), -3.3, -1.95))]
    yield [gate.animate.set_value(1.0), FadeIn(at(lab("in time, they turn opposite ways: the energies have opposite signs", 26, INK), 0, -2.65))]


def inset(x, y, same):
    a = P(x - 0.9, y)
    if same:
        return VGroup(parrow(a, a + RIGHT * 0.9, BLUE, 6), parrow(a + RIGHT * 0.9, a + RIGHT * 1.8, ORANGE, 6))
    return VGroup(parrow(a, a + RIGHT * 0.9, BLUE, 6), parrow(a + P(0.9, -0.18), a + P(0.0, -0.18), ORANGE, 6))


@slide("At some moments they point the same way", "Adding and cancelling")
def sum2(s):
    t = clock(s)
    s.add(sum_formula(), xaxis(-6.9, 7.0, -1.0), sum_row(t))
    yield [FadeIn(inset(-5.6, -2.1, True)), FadeIn(left_at(lab("same way: they add", 26, INK, True), -4.4, -2.1))]
    yield [FadeIn(inset(1.2, -2.1, False)), FadeIn(left_at(lab("opposite ways: they cancel", 26, INK, True), 2.4, -2.15))]
    yield [FadeIn(at(lab("the momentum is the same, so that happens at every position at once", 26, INK), 0, -3.2))]


@slide("So the total of the squared length rises and falls.", "Rising and falling")
def sum3(s):
    t = clock(s)
    s.add(xaxis(-6.9, 7.0, 0.05), sum_row(t, 1.45, r=0.6))
    x0, y, full = -1.4, -1.7, 7.6

    def gauge():
        w = max(full * np.cos(1.3 * t.get_value()) ** 2, 0.02)
        return Rectangle(width=w, height=0.6, stroke_width=0, fill_color=INK, fill_opacity=0.85).move_to(P(x0 + w / 2, y))
    box = Rectangle(width=full, height=0.6, color=MUTED, stroke_width=2.5).move_to(P(x0 + full / 2, y))
    yield [FadeIn(box), FadeIn(always_redraw(gauge)), FadeIn(right_at(mix("the total of", mt(PSI2, size=40), size=26), x0 - 0.3, y))]
    m = at(T("it rises and falls, so it can't be the chance", 30, RED, True), -0.3, -3.0)
    yield [FadeIn(m), Create(xmark(m))]


def keeps_heads(y=2.3):
    return VGroup(at(T("Schrödinger", 28, INK, True), -3.7, y), at(T("Klein–Gordon", 28, INK, True), 3.7, y))


@slide("The equation does keep the total of a different quantity.", "What it does keep")
def keeps(s):
    a = at(card(None, 6.4, 1.2, TEAL), -3.7, -1.1)
    b = at(card(None, 6.4, 1.2, INK), 3.7, -1.1)
    yield [FadeIn(keeps_heads()), FadeIn(a), FadeIn(at(mix("keeps the total of", mt(PSI2, size=40), size=24), -3.7, -1.1)),
           FadeIn(b), FadeIn(at(lab("keeps the total of a different quantity", 24, INK), 3.7, -1.1))]
    d1, d2 = at(mt(DT1, size=52), -5.4, 0.9), at(mt(DT2, size=52), 1.9, 0.9)
    yield [FadeIn(d1), FadeIn(left_at(words("one rate of change in time", 16, 24), -4.5, 0.9)),
           FadeIn(d2), FadeIn(left_at(words("two rates of change in time", 16, 24), 2.9, 0.9))]
    yield [GrowArrow(varrow(P(3.7, 0.1), P(3.7, -0.4))),
           FadeIn(at(words("that puts a rate of change in time into the quantity it keeps", 36, 24, INK, ORIGIN), 3.7, -2.55))]


def rho(size=52):
    """The quantity the Klein–Gordon equation keeps, in parts: rho =, E over mc², the squared length."""
    return mt(r"\rho =", r"\frac{E}{mc^2}", r"\,\lvert\psi\rvert^2", size=size)


@slide("For a wave with a definite energy, that quantity is on screen.", "The quantity it keeps")
def rho1(s):
    eq = at(rho(84), 0, 0.3)
    yield [FadeIn(eq), FadeIn(at(lab("for a wave with a definite energy E", 26, INK), 0, 2.4))]
    yield [FadeIn(note(eq[2], "the squared length", INK, UP, chars=24, buff=0.25)),
           FadeIn(note(eq[1], "the wave's energy over its rest energy", INK, chars=40))]


RHY = -2.2


@slide("The rate of change in time is what brings in the energy", "The sign of the energy")
def rho2(s):
    eq = at(rho(56), -4.6, 1.75)
    yield [FadeIn(eq), Create(frame(eq[1][0], INK, 0.1, 2.5)), FadeIn(left_at(lab("the energy, and with it the energy's sign", 24, INK), -2.4, 2.05))]
    b = chance_bump(color=BLUE, y=RHY, amp=2.3)
    yield [FadeIn(chance_axis(RHY)), FadeIn(b), FadeIn(at(mt(r"\rho", size=48, color=BLUE), -3.4, 0.45)),
           FadeIn(right_text("a positive-energy wave: the quantity is positive", 0.7, BLUE))]
    yield [FadeIn(left_at(mix("a slow particle:", mt("E", size=36), "is close to", mt("mc^2", size=36), size=24), 2.3, -0.8))]
    ghost = DashedVMobject(chance_bump(color=TEAL, y=RHY, amp=2.15)[1], num_dashes=40)
    yield [FadeIn(ghost), FadeIn(left_at(mix("so there it's almost", mt(PSI2, size=36, color=TEAL), size=24), 2.3, -1.9))]


@slide("But for a negative-energy wave, it's negative.", "A negative chance")
def rho3(s):
    y = 0.9
    b = chance_bump(color=ORANGE, y=y, amp=-2.3)
    s.add(at(rho(56), -4.6, 2.1))
    yield [FadeIn(chance_axis(y).shift(UP * 0.0)), FadeIn(b), FadeIn(at(mt(r"\rho", size=48, color=ORANGE), -3.4, -1.9)),
           FadeIn(right_text("a negative-energy wave: the quantity is negative", 1.2, ORANGE))]
    m = left_at(T("a chance of −30%", 32, RED, True), 2.3, -1.0)
    yield [FadeIn(m), Create(xmark(m)), FadeIn(left_at(lab("means nothing", 26, INK), 2.3, -1.8))]


CMP_Y = (1.05, -0.35, -1.75)
CMP_X = (-0.7, 4.5)


def cmp_heads():
    return VGroup(at(T("Schrödinger", 28, INK, True), CMP_X[0], 2.3), at(T("Klein–Gordon", 28, INK, True), CMP_X[1], 2.3))


def cmp_row(k):
    y = CMP_Y[k]
    if k == 0:
        name, left, right = lab("rates of change in time", 24), lab("one", 26, INK), lab("two", 26, INK)
    elif k == 1:
        name = mix("total of", mt(PSI2, size=36, color=MUTED), size=24, color=MUTED)
        left, right = lab("stays at one", 26, TEAL), lab("can change", 26, RED)
    else:
        name = VGroup(lab("the quantity whose", 24), lab("total stays constant", 24)).arrange(DOWN, buff=0.08, aligned_edge=RIGHT)
        left = mix(mt(PSI2, size=38, color=TEAL), ", never negative", size=26, color=TEAL)
        right = mix(mt(r"\rho", size=38, color=RED), ", which can be negative", size=26, color=RED)
    return VGroup(right_at(name, -3.5, y), at(card(None, 4.9, 1.15, LINE), CMP_X[0], y), at(left, CMP_X[0], y),
                  at(card(None, 4.9, 1.15, LINE), CMP_X[1], y), at(right, CMP_X[1], y))


@slide("So neither one works as a chance.", "Neither works as a chance")
def neither(s):
    yield [FadeIn(cmp_heads()), FadeIn(cmp_row(0), shift=DOWN * 0.1)]
    yield [FadeIn(cmp_row(1), shift=DOWN * 0.1)]
    yield [FadeIn(cmp_row(2), shift=DOWN * 0.1)]
    yield [FadeIn(caption("The Klein–Gordon wave function can't be read as a chance.", -3.2, RED, 28))]


# ================================================================== Dirac's idea
deck.part("Dirac's idea")

GOAL_X = (-0.9, 2.5, 5.9)
GOAL_Y = (0.7, -0.7)


def goal_col(k):
    name = ("Schrödinger", "Klein–Gordon", "Dirac's goal")[k]
    marks = ((False, True), (True, False), (True, True))[k]
    g = VGroup(at(T(name, 26, INK, True), GOAL_X[k], 1.9))
    for ok, y in zip(marks, GOAL_Y):
        g.add(check().move_to(P(GOAL_X[k], y)) if ok else cross(Square(0.4).move_to(P(GOAL_X[k], y)), RED, 6))
    return g


@slide("Dirac's idea.", "What Dirac wanted")
def idea(s):
    names = VGroup(right_at(lab("works for fast particles", 24, INK), -2.6, GOAL_Y[0]), right_at(lab("a chance that's never negative", 24, INK), -2.6, GOAL_Y[1]))
    yield [FadeIn(at(T("1928: Paul Dirac, 25", 30, INK, True), 0, -2.3)), FadeIn(names), FadeIn(goal_col(0)), FadeIn(goal_col(1))]
    g = goal_col(2)
    yield [FadeIn(g), Create(frame(g, TEAL, 0.25))]


@slide("He started from where the trouble came from.", "Where the trouble came from")
def trouble(s):
    a = at(card("a chance that\ncan be negative", 3.4, 1.4, RED, 26), -5.4, 1.2)
    b = at(card("two rates of\nchange in time", 3.4, 1.4, INK, 26), 0, 1.2)
    c = at(card("the squared energy\nin the rule", 3.4, 1.4, INK, 26), 5.4, 1.2)
    yield [FadeIn(a)]
    yield [GrowArrow(varrow(P(-3.5, 1.2), P(-1.9, 1.2))), FadeIn(at(lab("came from", 22), -2.7, 1.55)), FadeIn(b), FadeIn(at(mt(DT2, size=52), 0, -0.6))]
    r = at(rel(44), 4.9, -0.6)
    yield [GrowArrow(varrow(P(1.9, 1.2), P(3.5, 1.2))), FadeIn(at(lab("came from", 22), 2.7, 1.55)), FadeIn(c), FadeIn(r),
           Create(frame(r[0], RED, 0.1, 3))]


@slide("So Dirac wanted an equation built from the energy itself.", "The energy itself")
def itself(s):
    e2 = at(mt("E^2", size=96), -5.4, 0.7)
    e1 = at(mt("E", size=96), -2.2, 0.7)
    yield [FadeIn(e2), Create(cross(e2, RED, 6)), GrowArrow(varrow(P(-4.4, 0.7), P(-3.1, 0.7))), FadeIn(e1),
           FadeIn(at(lab("built from the energy itself", 26, INK), -3.8, -0.9))]
    yield [GrowArrow(varrow(P(-1.3, 0.7), P(0.9, 0.7))), FadeIn(at(mt(r"i\hbar\,\frac{\partial\psi}{\partial t}", size=72), 3.6, 0.7)),
           FadeIn(at(words("a single rate of change in time, like Schrödinger's", 30, 26, INK, ORIGIN), 3.6, -1.1))]


def balance(ang, left, right):
    """A beam on a pivot with a block on each end; the blocks' opacities are `left` and `right`."""
    def draw():
        pivot, half = P(0, -0.9), 3.9
        u = uvec(ang.get_value())
        a, b = pivot - half * u, pivot + half * u
        g = VGroup(Line(a, b, color=INK, stroke_width=7),
                   Polygon(pivot, pivot + P(-0.5, -1.0), pivot + P(0.5, -1.0), color=INK, stroke_width=3, fill_color=PALE, fill_opacity=1))
        for end, text, op in ((a, "time:\none rate of change", left), (b, "space:\none slope", right)):
            c = card(text, 3.5, 1.3, INK, 26).move_to(end + UP * 0.72)
            c[0].set_stroke(opacity=op.get_value()).set_fill(opacity=0.08 * op.get_value())
            c[1].set_opacity(op.get_value())
            g.add(c)
        return g
    return always_redraw(draw)


@slide("Relativity then forces something more.", "Time and space alike")
def alike(s):
    ang, left, right = ValueTracker(0.0), ValueTracker(0.0), ValueTracker(0.0)
    s.add(ang, left, right)
    yield [FadeIn(balance(ang, left, right)), FadeIn(at(T("an equation has to treat time and space alike", 28, INK, True), 0, 2.3))]
    yield [left.animate.set_value(1.0), ang.animate.set_value(0.14)]
    yield [right.animate.set_value(1.0), ang.animate.set_value(0.0), FadeIn(check().move_to(P(0, -2.9)))]


def slot_rule(size=80, y=0.5):
    m = at(lin(size), 0, y)
    slots = VGroup(*[DashedVMobject(Square(0.6, color=PURPLE, stroke_width=4), num_dashes=16).move_to(m[k]) for k in (1, 4)])
    m[1].set_opacity(0)
    m[4].set_opacity(0)
    return m, slots


@slide("The energy rule behind the equation has to be a straight-line one.", "A straight-line rule")
def straight(s):
    m, slots = slot_rule()
    yield [FadeIn(m), FadeIn(slots), FadeIn(at(T("a straight-line energy rule", 30, INK, True), 0, 2.3))]
    yield [FadeIn(at(lab("the energy and the momentum each appear to the first power", 26, INK), 0, -1.6)),
           FadeIn(at(lab("two places still to fill", 24, PURPLE), 0, -0.6))]


@slide("That rule is on screen.", "Alpha and beta")
def alphabeta(s):
    m = at(lin(80), 0, 0.5)
    yield [FadeIn(m)]
    yield [Indicate(VGroup(m[1], m[4]), color=PURPLE), FadeIn(at(mix("two fixed quantities,", ab(r"\alpha", 44), "and", ab(r"\beta", 44), size=26), 0, 2.3))]
    yield [FadeIn(note(VGroup(m[1], m[2]), "in front of the momentum", PURPLE, chars=16)),
           FadeIn(note(VGroup(m[4], m[5]), "in front of the mass", PURPLE, chars=16))]
    yield [FadeIn(at(lab("the same for every particle, and we still have to find them", 26, INK), 0, -2.9))]


@slide("This new rule mustn't contradict relativity.", "It must agree with relativity")
def agree(s):
    m = at(lin(56), 0, 1.7)
    r = at(rel(56), 0, -1.6)
    yield [FadeIn(m), FadeIn(left_at(lab("the new rule", 24), 3.3, 1.7))]
    yield [FadeIn(r), Create(frame(r, TEAL, 0.25)), FadeIn(left_at(lab("the relativistic rule", 24, TEAL), 3.9, -1.6))]
    yield [GrowArrow(varrow(P(0, 1.05), P(0, -0.75))), FadeIn(left_at(lab("squaring it has to give this back", 26, INK), 0.3, 0.15))]


@slide("We don't know yet what kind of thing alpha and beta are.", "Keep the order")
def order(s):
    top = at(ab(r"E^2 = (\alpha\,pc + \beta\,mc^2)(\alpha\,pc + \beta\,mc^2)", 52), 0, 1.6)
    yield [FadeIn(top), FadeIn(at(lab("we don't know yet what kind of thing they are", 26, INK), 0, 0.45))]
    a, b = at(ab(r"\alpha\beta", 84), -2.6, -1.2), at(ab(r"\beta\alpha", 84), 2.6, -1.2)
    yield [FadeIn(a), FadeIn(b), FadeIn(at(lab("kept apart", 24), 0, -1.2)),
           FadeIn(at(lab("we don't swap their order, in case the order matters", 26, INK, True), 0, -2.7))]


@slide("The square has three terms, and it's on screen.", "Three terms")
def three(s):
    m = at(squared(48), 0, 1.6)
    yield [FadeIn(m)]
    r = rel(48)
    r.shift(m[1].get_center() - r[2].get_center() + DOWN * 1.5)
    r[4].move_to(P(m[3].get_center()[0], r[4].get_center()[1]))
    r[3].move_to(P(m[2].get_center()[0], r[3].get_center()[1]))
    c = at(VGroup(ab(r"\alpha^2 = 1", 52), ab(r"\beta^2 = 1", 52)).arrange(RIGHT, buff=1.4), 0, -2.3)
    yield [Create(frame(m[1], TEAL, 0.1)), Create(frame(m[3], TEAL, 0.1)), FadeIn(r),
           FadeIn(left_at(lab("the relativistic rule", 24, TEAL), r.get_right()[0] + 0.4, r.get_center()[1])),
           FadeIn(at(lab("the first two terms match if", 24, INK), 0, -1.3)), FadeIn(c)]


@slide("The third term mixes the momentum with the mass.", "The third term")
def third(s):
    m = at(squared(48), 0, 1.6)
    s.add(m)
    yield [Create(frame(m[5], RED, 0.1)), FadeIn(note(m[5], "mixes the momentum with the mass", RED, chars=40, buff=0.22))]
    r = at(rel(48), 0, -1.3)
    yield [FadeIn(r), FadeIn(left_at(lab("no such term here", 24, INK), 2.9, -1.3)), FadeIn(at(T("so the third term has to vanish", 28, RED, True), 0, -2.6))]


@slide("That term holds alpha and beta multiplied in both orders.", "Three conditions")
def conds(s):
    m = at(paint(mt(r"\alpha\beta", "+", r"\beta\alpha", size=84), PURPLE, 0, 2), -0.9, 1.5)
    yield [FadeIn(m), FadeIn(note(m[0], "one order", PURPLE)), FadeIn(note(m[2], "the other order", PURPLE))]
    z = mt("= 0", size=84).next_to(m, RIGHT, buff=0.3)
    yield [FadeIn(z), FadeIn(left_at(words("the two orders have to cancel each other", 14, 24), 4.2, 1.5))]
    yield [FadeIn(cond_row(-2.1, 44), lag_ratio=0.2), FadeIn(at(lab("three conditions", 26, INK, True), 0, -1.0))]


@slide("Numbers can't meet them.", "Ordinary numbers?")
def numbers1(s):
    s.add(cond_row())
    yield [FadeIn(at(mix("could", ab(r"\alpha", 44), "and", ab(r"\beta", 44), "be ordinary numbers?", size=28), 0, 0.8))]
    yield [FadeIn(at(lab("for ordinary numbers, the order doesn't matter", 26, INK), 0, -0.3))]
    yield [FadeIn(at(ab(r"\alpha\beta = \beta\alpha", 72), 0, -1.6)), FadeIn(at(lab("the two orders give the same product", 24), 0, -2.6))]


@slide("Adding them gives twice that product.", "Numbers can't do it")
def numbers2(s):
    row = cond_row()
    s.add(row)
    yield [FadeIn(at(ab(r"\alpha\beta + \beta\alpha = 2\alpha\beta", 64), 0, 0.6))]
    yield [FadeIn(at(mix("zero only if", ab(r"\alpha = 0", 48), "or", ab(r"\beta = 0", 48), size=28), 0, -0.8))]
    m = at(mix("and then its square isn't", mt("1", size=48, color=RED), size=28, color=RED, bold=True), 0, -2.1)
    yield [FadeIn(m), Create(frame(row[1][0], RED, 0.07, 4)), Create(frame(row[1][1], RED, 0.07, 4)),
           FadeIn(right_at(lab("one of these fails", 24, RED, True), row.get_left()[0] - 0.35, row.get_center()[1]))]


# ================================================================== the Dirac equation
deck.part("The Dirac equation")


def purple(tex, size=48):
    return mt(tex, size=size, color=PURPLE)


@slide("The Dirac equation.", "Not numbers")
def notnum(s):
    a = at(ab(r"\alpha,\ \beta", 84), -5.0, 0.8)
    yield [FadeIn(a), FadeIn(at(lab("can't be numbers", 26, RED, True), -5.0, -0.4))]
    one = grid(1, 1, 0.9).move_to(P(-0.4, 0.8))
    yield [FadeIn(one), FadeIn(at(lab("a single number", 24, INK), -0.4, -0.4))]
    tab = grid(2, 2, 0.9).move_to(P(4.6, 0.8))
    yield [GrowArrow(varrow(P(0.6, 0.8), P(3.2, 0.8))), TransformFromCopy(one, tab), FadeIn(at(lab("next: a table of numbers, called a matrix", 24, INK), 4.2, -0.75)),
           FadeIn(at(lab("the next thing to try", 22), 1.9, 1.15))]


@slide("When we multiply two matrices, the order can matter.", "The order can matter")
def ordermatters(s):
    def prod(first, y):
        a, b = grid(2, 2, 0.6, PURPLE, 0.08), grid(2, 2, 0.6, PURPLE, 0.45)
        pairs = (a, b) if first else (b, a)
        return at(VGroup(pairs[0], T("×", 32, INK), pairs[1]).arrange(RIGHT, buff=0.3), -3.6, y)
    yield [FadeIn(prod(True, 1.5)), FadeIn(prod(False, -0.4)), FadeIn(left_at(words("multiply two matrices in the two orders", 26, 26), -0.9, 1.5)),
           FadeIn(left_at(words("the results can differ: the order can matter", 26, 26, INK, bold=True), -0.9, -0.4))]
    c = at(ab(r"\alpha\beta + \beta\alpha = 0", 52), -1.0, -2.4)
    yield [FadeIn(c), Create(frame(c, PURPLE, 0.2, 2)), FadeIn(left_at(lab("just what the third condition needs", 24, INK), 2.1, -2.4))]


@slide("Dirac didn't have to invent any.", "Pauli's matrices")
def pauli(s):
    e = VGroup(electron(-5.0, 0.6, BLUE, 0.22), varrow(P(-5.0, 0.0), P(-5.0, 1.6), BLUE, 5))
    yield [FadeIn(e), FadeIn(at(lab("the electron's spin", 24, INK), -5.0, -0.6)), FadeIn(at(T("the year before: Wolfgang Pauli", 28, INK, True), 0, 2.3))]
    gs = VGroup(grid(2, 2, 0.7), grid(2, 2, 0.7)).arrange(RIGHT, buff=0.6).move_to(P(0.6, 0.6))
    yield [GrowArrow(varrow(P(-3.8, 0.6), P(-1.6, 0.6))), FadeIn(gs), FadeIn(at(lab("described with small matrices", 24, INK), 0.6, -0.6))]
    yield [FadeIn(at(words("chapter 2b met two of them as operators", 22, 26, INK, ORIGIN), 5.3, 0.6)), GrowArrow(varrow(P(2.3, 0.6), P(3.2, 0.6)))]


def two_ops(y=2.0, size=64):
    return VGroup(at(purple(r"\hat Z", size), -5.6, y), left_at(lab("the vertical operator", 26, INK), -4.8, y),
                  at(purple(r"\hat S", size), 1.6, y), left_at(lab("the sideways operator", 26, INK), 2.4, y))


@slide("There we called them the vertical operator and the sideways operator.", "Two operators")
def zs(s):
    yield [FadeIn(two_ops())]
    yield [FadeIn(magnet(-5.6, 0.5)), FadeIn(left_at(lab("the up-and-down magnet", 24), -4.8, 0.5)),
           FadeIn(magnet(1.6, 0.5, False)), FadeIn(left_at(lab("the sideways magnet", 24), 2.4, 0.5))]
    yield [FadeIn(at(purple(ZHAT, 60), -3.6, -1.7)), FadeIn(at(purple(SHAT, 60), 3.6, -1.7))]


def mats(y=2.0, size=44):
    return VGroup(at(purple(ZHAT, size), -3.6, y), at(purple(SHAT, size), 3.6, y))


ONE = r"\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}"


@slide("These two meet all three conditions.", "Checking the squares")
def squares(s):
    yield [FadeIn(mats()), FadeIn(at(lab("do they meet all three conditions?", 26, INK), 0, 0.8))]
    a = at(mt(r"\hat Z^2 =", ONE, size=52), -4.0, -0.7)
    b = at(mt(r"\hat S^2 =", ONE, size=52), 3.2, -0.7)
    yield [FadeIn(a), FadeIn(b), FadeIn(at(lab("each one, multiplied by itself: the matrix that changes nothing", 24, INK), 0, -1.9))]
    a1, b1 = mt("= 1", size=52).next_to(a, RIGHT, buff=0.25), mt("= 1", size=52).next_to(b, RIGHT, buff=0.25)
    yield [FadeIn(a1), FadeIn(b1), Create(tick(a1)), Create(tick(b1)), FadeIn(at(lab("that matrix plays the part of the number 1", 26, INK, True), 0, -2.8))]


@slide("Multiply the two together, and the two orders give opposite results.", "The two orders")
def twoorders(s):
    a = at(mt(r"\hat Z\hat S = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}", size=56), -3.6, 1.3)
    b = at(mt(r"\hat S\hat Z = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}", size=56), 3.6, 1.3)
    yield [FadeIn(a), FadeIn(b), FadeIn(at(lab("the two orders give opposite results", 26, INK, True), 0, -0.1))]
    c = at(mt(r"\hat Z\hat S + \hat S\hat Z = 0", size=60), 0, -1.4)
    yield [FadeIn(c), Create(tick(c)), FadeIn(at(lab("chapter 2b saw this when it applied both orders to up", 24), 0, -2.6))]


@slide("We say that two such matrices anticommute.", "Anticommute")
def anti(s):
    yield [FadeIn(at(T("anticommute", 48, PURPLE, True), 0, 1.9)), FadeIn(at(lab("two matrices whose two orders give opposite results", 26, INK), 0, 0.9))]
    a = at(paint(mt(r"\alpha", "=", r"\hat S", size=80), PURPLE, 0, 2), -3.4, -1.0)
    b = at(paint(mt(r"\beta", "=", r"\hat Z", size=80), PURPLE, 0, 2), 3.4, -1.0)
    yield [FadeIn(a), FadeIn(at(lab("the sideways matrix", 24, INK), -3.4, -2.2)), FadeIn(b), FadeIn(at(lab("the vertical matrix", 24, INK), 3.4, -2.2))]


@slide("There's a cost.", "The cost")
def cost(s):
    g = grid(2, 2, 0.9).move_to(P(-4.4, 0.6))
    col = grid(2, 1, 0.9, INK).move_to(P(-2.3, 0.6))
    yield [FadeIn(g), FadeIn(at(lab("a two-by-two matrix", 24, INK), -4.6, -0.8))]
    yield [FadeIn(col), FadeIn(at(lab("acts on a column of two entries", 24, INK), -3.4, -1.5))]
    yield [GrowArrow(varrow(P(-1.4, 1.5), P(-1.4, -0.3))), FadeIn(left_at(words("a column: our list of amplitudes, written top to bottom", 30, 26), -0.6, 0.6))]


@slide("So the state can't be a single wave function any more.", "A column of two wave functions")
def column(s):
    one = at(mt(r"\psi", size=110), -4.4, 0.6)
    yield [FadeIn(one), FadeIn(at(lab("a single wave function", 24, INK), -4.4, -0.8)), Create(xmark(one, 0.5))]
    col = at(mt(COL2, size=84), 2.6, 0.6)
    yield [GrowArrow(varrow(P(-2.4, 0.6), P(-0.1, 0.6))), FadeIn(col),
           FadeIn(at(mix("a column of two wave functions, for", ab(r"\alpha", 40), "and", ab(r"\beta", 40), "to act on", size=24), 1.6, -1.6))]


@slide("We're only borrowing the arithmetic of the spin matrices here.", "Not a spin")
def notspin(s):
    col = at(mt(COL2, size=84), -4.2, 0.4)
    s.add(col)
    yield [FadeIn(left_at(words("we're only borrowing the arithmetic of the spin matrices", 32, 26), 0.0, 1.8))]
    mg = magnet(0.8, 0.0)
    yield [FadeIn(mg), Create(cross(mg, RED, 5)), FadeIn(left_at(lab("this column isn't a spin", 26, INK, True), 1.8, 0.0))]
    yield [FadeIn(left_at(lab("what are its two entries? we'll see shortly", 26, INK), 0.0, -1.8)),
           FadeIn(at(T("?", 40, MUTED, True), -1.9, 0.85)), FadeIn(at(T("?", 40, MUTED, True), -1.9, -0.05))]


@slide("Now put the straight-line rule through the recipe.", "The Dirac equation on a line")
def dirac_build(s):
    m = at(lin(56), 0, 2.0)
    sw = VGroup(at(mt(r"E \;\to\; " + E_OP, size=38), -3.6, 0.55), at(mt(r"p \;\to\; " + P_OP, size=38), 3.6, 0.55))
    yield [FadeIn(m), FadeIn(sw), GrowArrow(varrow(P(0, 1.35), P(0, -0.25))), FadeIn(left_at(lab("the recipe", 24), 0.25, 0.55))]
    d = at(dirac(60), 0, -1.35)
    yield [TransformFromCopy(m, d), Create(frame(d, INK, 0.3, 2.5)), FadeIn(at(T("the Dirac equation, for motion along a line", 28, INK, True), 0, -2.95))]


@slide("It has one rate of change in time, and one slope in space.", "One and one")
def dirac_alike(s):
    d = at(dirac(64), 0, 1.2)
    s.add(d)
    yield [FadeIn(note(d[0], "one rate of change in time", INK, chars=16)), FadeIn(note(VGroup(d[2], d[3], d[4]), "one slope in space", INK, chars=16))]
    m = at(T("it treats time and space alike, as chapter 4 asks", 28, TEAL, True), -0.3, -2.5)
    yield [FadeIn(m), Create(tick(m))]


# ================================================================== four matrices in space
deck.part("Four matrices in space")


@slide("Four matrices in space.", "From a line to space")
def tospace(s):
    line = Line(P(-6.8, 0.3), P(-1.6, 0.3), color=LINE, stroke_width=4)
    pa = varrow(P(-5.4, 0.3), P(-3.0, 0.3), INK, 6)
    yield [FadeIn(line), GrowArrow(pa), FadeIn(at(mt("p", size=52), -4.2, 0.85)), FadeIn(at(lab("along a line: one momentum", 24, INK), -4.2, -0.7))]
    o = P(3.6, -0.5)
    ends = (o + P(2.5, 0), o + P(0, 2.4), o + P(-1.5, -1.3))
    axes = VGroup(*[Line(o, o + 1.2 * (e - o), color=LINE, stroke_width=3) for e in ends])
    arrows = [varrow(o, e, INK, 6) for e in ends]
    labels = VGroup(mt("p_x", size=48).next_to(ends[0], DOWN, buff=0.2), mt("p_y", size=48).next_to(ends[1], RIGHT, buff=0.25),
                    mt("p_z", size=48).next_to(ends[2], RIGHT, buff=0.3))
    yield [FadeIn(axes), *[GrowArrow(a) for a in arrows], FadeIn(labels)]
    yield [FadeIn(at(lab("in space: three parts, one for each direction", 24, INK), 3.6, -2.7))]


@slide("On the line, each matrix had its own job.", "One matrix for each part")
def jobs(s):
    m = at(lin(72), -1.0, 1.9)
    yield [FadeIn(m), FadeIn(note(VGroup(m[1], m[2]), "momentum", PURPLE)), FadeIn(note(VGroup(m[4], m[5]), "mass", PURPLE))]
    m3 = at(lin3(60), 0, -1.0)
    yield [FadeIn(m3[0]), FadeIn(VGroup(*m3[1:7])), FadeIn(note(VGroup(*m3[1:7]), "each part of the momentum needs its own matrix", PURPLE, chars=26))]
    yield [FadeIn(VGroup(m3[7], m3[8])), FadeIn(note(VGroup(m3[7], m3[8]), "mass", PURPLE))]
    yield [FadeIn(at(pill("four matrices", PURPLE, 26), 5.3, 1.9))]


@slide("The four must all be different, and here's why.", "Square the rule again")
def square3(s):
    m3 = at(lin3(44), 0, 2.1)
    yield [FadeIn(m3), FadeIn(at(lab("the four must all be different", 24, INK), 2.6, 1.3))]
    r = at(mt(REL3, size=48), 0, 0.0)
    yield [GrowArrow(varrow(P(-5.4, 1.6), P(-5.4, 0.5))), FadeIn(left_at(lab("its square must give", 24), -5.2, 1.0)), FadeIn(r)]
    c = at(ab(r"\alpha_x^2 = 1 \qquad \alpha_y^2 = 1 \qquad \alpha_z^2 = 1 \qquad \beta^2 = 1", 48), 0, -1.7)
    yield [FadeIn(c), FadeIn(at(lab("each matrix's own square gives one of these four terms, so each must square to 1", 24, INK), 0, -2.7))]


@slide("And every pair of matrices gives a mixed term that we don't want.", "Mixed terms")
def mixed(s):
    m = at(ab(r"(\alpha_x\alpha_y + \alpha_y\alpha_x)\,(p_xc)(p_yc)", 60), 0, 1.1)
    yield [FadeIn(m), Create(frame(m, RED, 0.2)), FadeIn(at(lab("every pair of matrices gives a mixed term, such as", 24, INK), 0, 2.3)),
           FadeIn(at(lab("the relativistic rule has no such term", 24, RED), 0, 0.1))]
    c = at(ab(r"\alpha_x\alpha_y + \alpha_y\alpha_x = 0", 60), 0, -1.4)
    yield [FadeIn(c), FadeIn(at(T("so every pair must anticommute", 28, INK, True), 0, -2.6))]


@slide("That rules out using one matrix twice.", "No matrix twice")
def twice(s):
    yield [FadeIn(at(mix("one matrix used twice?", ab(r"\alpha_y = \alpha_x", 52), size=28), 0, 1.9))]
    m = at(ab(r"\alpha_x\alpha_x + \alpha_x\alpha_x = 2\alpha_x^2 = 2", 68), 0, 0.2)
    n = at(T("two, not zero", 32, RED, True), -0.3, -1.6)
    yield [FadeIn(m), FadeIn(n), Create(xmark(n))]


NODES = ((-5.6, 1.5, r"\alpha_x"), (-1.8, 1.5, r"\alpha_y"), (-1.8, -1.9, r"\alpha_z"), (-5.6, -1.9, r"\beta"))


def node(k):
    x, y, name = NODES[k]
    return VGroup(Circle(radius=0.6, color=PURPLE, stroke_width=3.5, fill_color=WHITE, fill_opacity=1).move_to(P(x, y)), at(purple(name, 48), x, y))


def edges():
    g = VGroup()
    for i in range(4):
        for j in range(i + 1, 4):
            a, b = P(*NODES[i][:2]), P(*NODES[j][:2])
            u = (b - a) / np.linalg.norm(b - a)
            g.add(Line(a + 0.65 * u, b - 0.65 * u, color=PURPLE, stroke_width=3))
    return g


@slide("So we need four different matrices.", "Four different matrices")
def four(s):
    yield [LaggedStart(*[FadeIn(node(k)) for k in range(4)], lag_ratio=0.2), FadeIn(left_at(T("four different matrices", 28, INK, True), 1.2, 1.5))]
    yield [FadeIn(left_at(lab("each squares to 1", 26, INK), 1.2, 0.2))]
    yield [Create(edges()), FadeIn(left_at(lab("every pair anticommutes", 26, PURPLE, True), 1.2, -1.1))]


SLOT_Y = (1.65, 0.45, -0.75, -1.95)


def slot(k):
    name = (mt("p_x", size=44), mt("p_y", size=44), mt("p_z", size=44), lab("the mass", 24, INK))[k]
    box = DashedVMobject(RoundedRectangle(width=2.2, height=0.95, corner_radius=0.12, color=PURPLE, stroke_width=3), num_dashes=30).move_to(P(4.6, SLOT_Y[k]))
    return VGroup(box, right_at(name, 3.2, SLOT_Y[k]))


def chip2(k):
    inner = (purple(r"\hat S", 44), lab("one more", 24, PURPLE, True), purple(r"\hat Z", 44))[k]
    box = RoundedRectangle(width=2.0, height=0.8, corner_radius=0.12, stroke_color=PURPLE, stroke_width=2.5, fill_color=WHITE, fill_opacity=1)
    return VGroup(box, inner.move_to(box)).move_to(P(-4.6, SLOT_Y[k]))


@slide("Two-by-two matrices aren't enough.", "Two-by-two isn't enough")
def notenough(s):
    yield [LaggedStart(*[FadeIn(slot(k)) for k in range(4)], lag_ratio=0.15), FadeIn(at(lab("four places to fill", 24), 4.2, 2.5))]
    chips = [chip2(k) for k in range(3)]
    yield [FadeIn(chips[0]), FadeIn(chips[2]), FadeIn(at(lab("two-by-two: only three that all anticommute", 24, INK), -3.6, 2.5))]
    yield [FadeIn(chips[1])]
    empty = slot(3)[0]
    yield [*[c.animate.move_to(P(4.6, SLOT_Y[k])) for k, c in enumerate(chips)], Create(xmark(empty)),
           FadeIn(at(lab("none left for the mass", 26, RED, True), 3.9, -2.9))]


def size_grid(n, x, cell):
    return VGroup(grid(n, n, cell).move_to(P(x, 0.7)), at(lab(("", "", "two-by-two", "three-by-three", "four-by-four")[n], 24, INK), x, -0.95))


@slide("Three-by-three doesn't work either.", "Only even sizes")
def even(s):
    g2, g3, g4 = size_grid(2, -4.8, 0.8), size_grid(3, 0, 0.62), size_grid(4, 4.8, 0.52)
    yield [FadeIn(g2), FadeIn(at(lab("only three", 22, RED), -4.8, -1.5)), FadeIn(g3), Create(cross(g3[0], RED, 5))]
    yield [FadeIn(at(T("matrices like these only come in even sizes", 28, INK, True), 0, -2.6))]
    yield [FadeIn(g4), Create(CurvedArrow(P(-4.8, 1.65), P(4.8, 1.75), angle=-0.3, color=MUTED, stroke_width=4, tip_length=0.2)),
           FadeIn(at(lab("after two comes four", 24, INK), 0, 2.55))]


@slide("Four-by-four matrices do offer the four we need.", "Four-by-four")
def fourbyfour(s):
    g = grid(4, 4, 0.7).move_to(P(-3.8, 0.7))
    names = at(ab(r"\alpha_x,\ \alpha_y,\ \alpha_z,\ \beta", 52), -3.8, -1.5)
    yield [FadeIn(g), FadeIn(names), Create(tick(names)), FadeIn(at(lab("four-by-four matrices offer the four we need", 24, INK), -3.8, -2.4))]
    col = at(mt(COL4, size=60), 3.6, 0.4)
    yield [FadeIn(col), FadeIn(at(lab("they act on a column of four wave functions", 24, INK), 3.6, -2.4))]


@slide("So that's the Dirac equation.", "The Dirac equation")
def dirac_sum(s):
    d = at(dirac(52), 0, 1.75)
    yield [FadeIn(d), Create(frame(d, INK, 0.22, 2.5))]
    yield [Indicate(VGroup(d[3], d[6]), color=PURPLE, scale_factor=1.5), FadeIn(at(lab("its coefficients are matrices", 26, PURPLE, True), 0, 0.5))]
    yield [FadeIn(at(mt(COL2, size=52), -3.2, -1.7)), FadeIn(right_at(lab("on a line: two", 26, INK), -4.9, -1.7)),
           FadeIn(at(mt(COL4, size=44), 4.6, -1.7)), FadeIn(right_at(lab("in space: four", 26, INK), 2.9, -1.7)),
           FadeIn(at(lab("its state is a column of wave functions", 24), 0, -0.2))]


# ================================================================== a chance that is never negative
deck.part("A chance that is never negative")


def col4(size=52, colored=False):
    m = mt(r"\psi =", r"\begin{pmatrix} \psi_1 \\ \psi_2 \\ \psi_3 \\ \psi_4 \end{pmatrix}", size=size)
    if colored:
        split_rows(m[1], BLUE, ORANGE)
    return m


@slide("A chance that is never negative.", "The squared length of a column")
def length4(s):
    c = at(col4(56), -5.2, 0.4)
    yield [FadeIn(c), FadeIn(at(lab("four wave functions", 24, INK), -5.2, -1.7))]
    yield [FadeIn(at(mix("the squared length", mt(PSI2, size=44, color=TEAL), "is again the chance of finding the particle", size=24, color=TEAL), 1.9, 1.9))]
    yield [FadeIn(at(mt(SUM4, size=40), 1.9, 0.4)), FadeIn(at(lab("for a column: the sum of its entries' squared lengths", 24, INK), 1.9, -0.7))]


BARS = (0.9, 0.4, 1.3, 0.7)
BAR_X = (-5.6, -4.3, -3.0, -1.7)
BASE = -2.4


def sq_bar(k, x=None, y=None):
    h = BARS[k]
    return Rectangle(width=0.8, height=h, stroke_color=TEAL, stroke_width=2.5, fill_color=TEAL, fill_opacity=0.35).move_to(
        P(BAR_X[k] if x is None else x, (BASE if y is None else y) + h / 2))


@slide("A sum of squares is never negative.", "Never negative")
def never(s):
    s.add(at(mt(SUM4, size=40), 0, 2.15))
    bars = [sq_bar(k) for k in range(4)]
    names = VGroup(*[at(mt(r"\lvert\psi_%d\rvert^2" % (k + 1), size=36), BAR_X[k], BASE - 0.45) for k in range(4)])
    yield [FadeIn(Line(P(-6.4, BASE), P(2.6, BASE), color=MUTED, stroke_width=3)), *[GrowFromEdge(b, DOWN) for b in bars], FadeIn(names)]
    stack, y = [], BASE
    for k in range(4):
        stack.append(sq_bar(k, 0.6, y))
        y += BARS[k]
    m = left_at(words("a sum of squares is never negative", 22, 28, TEAL, bold=True), 1.7, 0.3)
    yield [*[TransformFromCopy(b, c) for b, c in zip(bars, stack)], FadeIn(at(mt(PSI2, size=36, color=TEAL), 0.6, BASE - 0.45)), FadeIn(m), Create(tick(m[-1]))]
    yield [FadeIn(left_at(words("and the Dirac equation keeps its total constant", 28, 26), 1.7, -1.3))]


@slide("The equation has the single rate of change in time that Dirac asked for.", "The second problem, solved")
def solved2(s):
    heads = VGroup(at(T("Klein–Gordon", 28, INK, True), -3.7, 2.3), at(T("Dirac", 28, INK, True), 3.7, 2.3))
    yield [FadeIn(heads), FadeIn(at(mt(DT2, size=52), -5.4, 1.1)), FadeIn(left_at(words("two rates of change in time", 16, 24), -4.5, 1.1)),
           FadeIn(at(mt(DT1, size=52), 2.0, 1.1)), FadeIn(left_at(words("a single rate of change in time", 18, 24), 2.9, 1.1))]
    a = at(card(None, 6.4, 1.2, RED), -3.7, -0.8)
    b = at(card(None, 6.4, 1.2, TEAL), 3.7, -0.8)
    yield [FadeIn(a), FadeIn(at(mix("keeps", mt(r"\rho", size=40), ", with a rate of change in time in it", size=22), -3.7, -0.8)),
           FadeIn(b), FadeIn(at(mix("keeps", mt(PSI2, size=40), ": no rate of change in time in it", size=22), 3.7, -0.8))]
    yield [FadeIn(at(lab("so it carries the energy's sign", 24, RED), -3.7, -1.8)), FadeIn(at(lab("and no energy sign gets in with it", 24, TEAL), 3.7, -1.8))]
    m = at(T("that solves the second problem", 30, TEAL, True), -0.3, -2.9)
    yield [FadeIn(m), Create(tick(m))]


# ================================================================== the negative energies predict antimatter
deck.part("The negative energies predict antimatter")


@slide("The negative energies predict antimatter.", "The first problem is still there")
def still(s):
    a = at(card("second problem:\na negative chance", 4.6, 1.5, TEAL, 28), -3.6, 0.8)
    b = at(card("first problem:\nnegative energies", 4.6, 1.5, ORANGE, 28), 3.6, 0.8)
    m = at(lab("solved", 28, TEAL, True), -3.9, -0.6)
    yield [FadeIn(a), FadeIn(m), Create(tick(m)), FadeIn(b)]
    yield [FadeIn(at(lab("still there", 28, RED, True), 3.6, -0.6)), Create(frame(b, RED, 0.15, 3))]


@slide("Dirac's rule has the energy to the first power.", "One energy for each momentum?")
def onee(s):
    m = at(lin(80), 0, 1.2)
    yield [FadeIn(m), Create(frame(m[0][0], INK, 0.12, 2.5)), FadeIn(at(lab("the energy to the first power", 24, INK), -3.4, 2.4))]
    q = at(T("so one energy for each momentum?", 30, INK, True), -0.3, -1.0)
    yield [FadeIn(q)]
    yield [Create(xmark(q)), FadeIn(at(T("it doesn't", 30, RED, True), 0, -2.1))]


def rest_rule(size=72):
    """The rule for a particle at rest, in parts: E =, beta, mc²."""
    return paint(mt("E =", r"\beta", r"\,mc^2", size=size), PURPLE, 1)


@slide("To see why, go back to the simpler case of motion along a line.", "A particle at rest")
def atrest(s):
    c = at(mt(COL2, size=64), -5.0, 0.6)
    yield [FadeIn(c), FadeIn(at(words("motion along a line: just two wave functions", 22, 24, INK, ORIGIN), -5.0, -1.2))]
    m = at(lin(64), 2.6, 1.3)
    yield [FadeIn(m), FadeIn(at(lab("a particle at rest: its momentum is zero", 26, INK), 2.6, 2.4))]
    gone = VGroup(m[1], m[2])
    yield [Create(Line(gone.get_corner(DL) + P(-0.1, -0.1), gone.get_corner(UR) + P(0.1, 0.1), color=RED, stroke_width=6)),
           FadeIn(at(rest_rule(80), 2.6, -1.4)), GrowArrow(varrow(P(2.6, 0.55), P(2.6, -0.55)))]


def chain_card(k):
    x = (-4.9, 0.0, 4.9)[k]
    if k == 0:
        inner = VGroup(lab("a matrix", 26, PURPLE, True), lab("it acts on the state", 24, INK)).arrange(DOWN, buff=0.12)
    elif k == 1:
        inner = VGroup(lab("so it's an operator,", 24, INK), mix("like chapter 2b's", mt(r"\hat H", size=40), size=24)).arrange(DOWN, buff=0.1)
    else:
        inner = VGroup(lab("its eigenvalues: the results", 22, INK), lab("a measurement can give", 22, INK)).arrange(DOWN, buff=0.12)
    return VGroup(at(card(None, 4.2, 1.5, INK), x, -0.5), at(inner, x, -0.5))


@slide("The right side is now a matrix.", "A matrix on the right")
def eigen(s):
    m = at(rest_rule(72), 0, 1.8)
    s.add(m)
    yield [Create(frame(VGroup(m[1], m[2]), PURPLE, 0.15)), FadeIn(chain_card(0))]
    yield [GrowArrow(varrow(P(-2.75, -0.5), P(-2.15, -0.5))), FadeIn(chain_card(1))]
    yield [GrowArrow(varrow(P(2.15, -0.5), P(2.75, -0.5))), FadeIn(chain_card(2))]
    yield [FadeIn(at(T("so the allowed energies are this matrix's eigenvalues", 28, INK, True), 0, -2.5))]


REST = (r"\beta", r"\,mc^2\,\psi =", r"mc^2", r"\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}", r"\begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix}", "=",
        r"\begin{pmatrix} +mc^2\,\psi_1 \\ -mc^2\,\psi_2 \end{pmatrix}")


def rest_eq(size=54):
    m = paint(mt(*REST, size=size), PURPLE, 0, 3)
    split_rows(m[6], BLUE, ORANGE)
    return m


@slide("Beta is the vertical matrix.", "Beta applied to the column")
def apply(s):
    m = at(rest_eq(), 0, 0.3)
    head = at(paint(mt(r"\beta", "=", r"\hat Z", size=52), PURPLE, 0, 2), -1.9, 2.2)
    yield [FadeIn(head), FadeIn(left_at(lab("the vertical matrix", 26, INK), -0.6, 2.2)), FadeIn(VGroup(*m[0:5]))]
    yield [FadeIn(note(m[3], "the top entry times +1, the bottom entry times −1", PURPLE, chars=26))]
    yield [FadeIn(VGroup(m[5], m[6]))]


@slide("So the top wave function gets the rest energy with a plus sign.", "One entry for each sign")
def signs(s):
    res = at(split_rows(mt(REST[6], size=84), BLUE, ORANGE), -4.0, 0.6)
    s.add(res)
    yield [GrowArrow(varrow(P(-1.5, 1.15), P(-0.3, 1.15), BLUE)),
           FadeIn(left_at(mix("the top wave function: energy", mt("+mc^2", size=40, color=BLUE), size=26, color=BLUE), 0.0, 1.15))]
    yield [GrowArrow(varrow(P(-1.5, 0.05), P(-0.3, 0.05), ORANGE)),
           FadeIn(left_at(mix("the bottom one: energy", mt("-mc^2", size=40, color=ORANGE), size=26, color=ORANGE), 0.0, 0.05))]
    yield [FadeIn(at(T("for a particle at rest, the column's two entries: one for each sign of the energy", 26, INK, True), 0, -2.3))]


@slide("In space, the column has four wave functions", "Two and two")
def twotwo(s):
    c = at(col4(72, True), -4.6, 0.3)
    yield [FadeIn(c), FadeIn(at(lab("in space: four wave functions", 24, INK), -4.6, -2.2))]
    yield [FadeIn(left_at(mix("two get", mt("+mc^2", size=44, color=BLUE), size=28, color=BLUE), -2.3, 1.15)),
           FadeIn(left_at(mix("two get", mt("-mc^2", size=44, color=ORANGE), size=28, color=ORANGE), -2.3, -0.55))]
    yield [FadeIn(left_at(words("the next chapter says what tells the two of each sign apart", 24, 24, MUTED), 2.6, 0.3))]
    yield [FadeIn(at(T("either way, the negative energies are still in the equation", 28, ORANGE, True), 0, -3.1))]


STX = 1.5   # left edge of the text beside the sea


def sea_text(text, y, color=INK, bold=False, chars=32, size=25):
    return left_at(words(text, chars, size, color, bold=bold), STX, y)


@slide("Dirac's own answer came in nineteen thirty.", "Dirac's own answer")
def answer(s):
    t = clock(s)
    s.add(sea_bands())

    def faller():
        k = int(1.6 * t.get_value()) % (len(SEA_ROWS) + 1)
        return Dot(P(-2.0, EY if k == 0 else SEA_ROWS[k - 1]), radius=0.13, color=BLUE if k == 0 else ORANGE)
    s.add(always_redraw(faller))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(sea_text("1930: Dirac's own answer", 1.9, INK, True, size=28))]
    yield [FadeIn(sea_text("it isn't the one physicists use today", 0.7))]
    yield [FadeIn(sea_text("but it led to the right prediction, so we follow it", -0.7))]


@slide("It starts from a fact that chemistry had already taught.", "The exclusion principle")
def exclusion(s):
    box = at(card(None, 1.5, 1.1, INK), -4.2, 1.4)
    inside = electron(-4.2, 1.4)
    other = electron(-6.8, 1.4)
    yield [FadeIn(box), FadeIn(inside), FadeIn(at(lab("one state", 22), -4.2, 2.3)), FadeIn(other), other.animate.move_to(P(-5.5, 1.4))]
    stop = cross(Square(0.4).move_to(P(-5.15, 1.4)), RED, 5)
    yield [Create(stop), FadeIn(left_at(T("no two electrons can be in the same state", 28, INK, True), -2.6, 1.7)),
           FadeIn(left_at(lab("Pauli's exclusion principle", 26, INK), -2.6, 1.0))]
    levels = VGroup(*[Line(P(-6.2, y), P(-3.4, y), color=INK, stroke_width=4) for y in (-2.7, -1.9, -1.1)])
    dots = VGroup(*[electron(x, y + 0.2) for y, xs in ((-2.7, (-4.8,)), (-1.9, (-4.8,)), (-1.1, (-4.8,))) for x in xs])
    yield [FadeIn(levels), LaggedStart(*[FadeIn(d, shift=DOWN * 0.3) for d in dots], lag_ratio=0.25),
           FadeIn(left_at(words("that's why the electrons in an atom stack up in shells, and don't all sit in the lowest one", 40, 26), -2.6, -1.8))]


def blocked():
    """An ordinary electron above the full sea, and the fall it can't make."""
    x = HX + 1.4
    a = varrow(P(x, EY - 0.22), P(x, SEAB[1] + 0.12), INK)
    return VGroup(electron(x, EY), a, cross(Square(0.34).move_to(P(x + 0.45, SEAB[1] + 0.45)), RED, 5))


@slide("Suppose, said Dirac, that every negative-energy state is already taken.", "A filled sea")
def filled(s):
    s.add(sea_bands())
    rows = [VGroup(*[Dot(sea_xy(r, c), radius=0.09, color=ORANGE) for c in range(12)]) for r in range(6)]
    yield [LaggedStart(*[FadeIn(r) for r in reversed(rows)], lag_ratio=0.25),
           FadeIn(sea_text("suppose every negative-energy state is already taken", 2.0))]
    b = blocked()
    yield [FadeIn(b[0]), GrowArrow(b[1]), Create(b[2]), FadeIn(sea_text("then an ordinary electron can't fall: there's no room below it", 0.7))]
    yield [FadeIn(sea_text("Dirac called this full set of states the sea", -0.8, ORANGE, True))]
    yield [FadeIn(sea_text("it's the same everywhere, so nobody would notice it", -2.2, MUTED))]


@slide("That looks like a trick, and in a way it is one.", "A trick?")
def trick(s):
    s.add(sea_base(), blocked())
    yield [FadeIn(sea_text("that looks like a trick, and in a way it is one", 2.0))]
    yield [FadeIn(sea_text("nobody has seen the sea", 0.8)), FadeIn(sea_text("Dirac brought it in only to block the fall", -0.3))]
    yield [FadeIn(sea_text("what matters is what follows from it", -1.8, INK, True, size=28))]


@slide("Now let a packet of light give one electron in the sea", "Lifting an electron out")
def lift(s):
    e = Dot(sea_xy(*HOLE), radius=0.09, color=ORANGE)
    s.add(sea_bands(), sea_dots(True), e)
    yield [Create(wiggle(P(-4.6, 0.3), P(HX - 0.3, SEAB[1] + 0.2))), FadeIn(left_at(lab("a packet of light", 24), -2.6, 0.32))]
    gap = DoubleArrow(P(SX[1] + 0.3, SEAB[1]), P(SX[1] + 0.3, TOPB[0]), buff=0, color=MUTED, stroke_width=4, tip_length=0.18)
    yield [FadeIn(gap), FadeIn(left_at(mix("to cross the gap: at least", mt("2mc^2", size=40), size=25), STX, -0.05))]
    yield [e.animate.move_to(P(HX, EY)).set_color(BLUE).scale(1.45), FadeIn(sea_text("it becomes an ordinary electron with positive energy", 1.6, BLUE))]


def lifted():
    return VGroup(sea_bands(), sea_dots(True), electron(HX, EY), varrow(P(HX, SEA_ROWS[0] + 0.22), P(HX, EY - 0.22), INK))


def hole_callout(text="the hole it leaves", bold=False):
    return VGroup(Line(sea_xy(*HOLE) + RIGHT * 0.2, P(STX - 0.15, -1.1), color=ORANGE, stroke_width=2), sea_text(text, -1.1, ORANGE, bold))


@slide("And it leaves behind a hole.", "A hole in the sea")
def hole(s):
    s.add(lifted())
    ring = hole_ring()
    yield [Create(ring), Flash(ring, color=ORANGE), FadeIn(hole_callout())]
    yield [FadeIn(Line(P(HX + 0.2, EY), P(STX - 0.15, 1.5), color=BLUE, stroke_width=2)), FadeIn(sea_text("the electron, lifted out", 1.5, BLUE)),
           FadeIn(caption("The electron and the hole appear together.", -3.65))]


@slide("Think about how the hole would look to us.", "How the hole looks")
def looks(s):
    s.add(sea_base(True))
    yield [FadeIn(sea_text("how would the hole look to us?", 2.1, INK, True, size=28))]
    yield [FadeIn(sea_text("the sea is missing one electron's negative charge", 0.8))]
    yield [FadeIn(hole_callout("so the hole looks like a positive charge", True)), Flash(hole_ring(), color=ORANGE)]


@slide("The sea is also missing a negative energy.", "A particle with positive energy")
def looks2(s):
    s.add(sea_base(True), hole_callout("the hole: a positive charge", True))
    yield [FadeIn(sea_text("the sea is also missing a negative energy", 2.0))]
    yield [FadeIn(sea_text("so the hole has positive energy", 0.8, ORANGE, True))]
    c = at(card("the hole behaves like a particle\nwith the electron's mass\nand the opposite charge", 5.6, 1.7, ORANGE, 24), 4.5, -2.5)
    yield [FadeIn(c)]


@slide("In nineteen thirty-one, Dirac predicted that such a particle exists.", "Dirac's prediction")
def predict(s):
    e = VGroup(electron(-3.2, 0.6, BLUE, 0.3), at(T("−", 36, INK, True), -2.5, 0.6), at(lab("the electron", 26, INK), -3.2, -0.5))
    p = VGroup(electron(3.2, 0.6, ORANGE, 0.3), at(T("+", 36, INK, True), 3.9, 0.6))
    yield [FadeIn(at(T("1931: Dirac predicts that such a particle exists", 28, INK, True), 0, 2.3)), FadeIn(e), FadeIn(p),
           FadeIn(at(lab("the same mass, the opposite charge", 26, INK), 0, -1.7)),
           FadeIn(DashedLine(P(-2.0, 0.6), P(2.6, 0.6), color=MUTED, stroke_width=2.5))]
    yield [FadeIn(at(T("the anti-electron", 32, ORANGE, True), 3.2, -0.5))]


@slide("Now back to the trail.", "Back to the trail")
def back(s):
    up = trail_up()
    yield [FadeIn(chamber()), FadeIn(plate()), Succession(Create(trail_low()), Create(up), GrowArrow(trail_tip(up)))]
    m = left_at(lab("a light particle with a positive charge", 26, INK, True), 0.6, 1.9)
    yield [FadeIn(m), FadeIn(left_at(words("exactly what Anderson photographed the next year, 1932", 34, 26), 0.6, 0.9))]
    yield [FadeIn(left_at(lab("he hadn't been looking for it", 26, INK), 0.6, -0.3))]
    name = left_at(T("the positron", 44, ORANGE, True), 0.6, -1.7)
    yield [FadeIn(name), FadeIn(Line(P(CH[0] + 0.5, CH[1] + 1.3), name.get_left() + LEFT * 0.15, color=ORANGE, stroke_width=2))]


PAIR_Y = (1.3, 0.1, -1.4)
PAIR_R = (0.13, 0.26, 0.42)


@slide("Other particles turned out to have such partners too", "Antimatter")
def antimatter(s):
    left = VGroup(*[Circle(radius=r, color=INK, stroke_width=3, fill_color=LINE, fill_opacity=1).move_to(P(-5.0, y)) for y, r in zip(PAIR_Y, PAIR_R)])
    right = VGroup(*[Circle(radius=r, color=ORANGE, stroke_width=3, fill_color=ORANGE, fill_opacity=0.35).move_to(P(-1.8, y)) for y, r in zip(PAIR_Y, PAIR_R)])
    links = VGroup(*[DashedLine(P(-4.3, y), P(-2.5, y), color=MUTED, stroke_width=2.5) for y in PAIR_Y])
    yield [FadeIn(at(lab("particle", 24, INK), -5.0, 2.3)), FadeIn(at(lab("partner", 24, ORANGE), -1.8, 2.3)), FadeIn(left), FadeIn(links), FadeIn(right),
           FadeIn(left_at(words("other particles have such partners too: the same mass, the opposite charge", 30, 26), 0.6, 1.5))]
    yield [FadeIn(left_at(mix("each partner:", T("an antiparticle", 28, ORANGE, True), size=26), 0.6, -0.2))]
    yield [Create(frame(right, ORANGE, 0.3, 3)), FadeIn(left_at(mix("together:", T("antimatter", 34, ORANGE, True), size=26), 0.6, -1.5))]


# ================================================================== one particle isn't enough
deck.part("One particle isn't enough")


def sea_struck():
    x0, x1 = SX
    return VGroup(sea_base(True), Line(P(x0, SEAB[0]), P(x1, TOPB[1]), color=RED, stroke_width=6))


@slide("One particle isn't enough.", "Why the sea was dropped")
def dropped(s):
    g = sea_struck()
    yield [FadeIn(g[0]), FadeIn(sea_text("the sea gave the right prediction", 2.0))]
    yield [Create(g[1]), FadeIn(sea_text("but physicists dropped it, for two reasons", 0.9, RED, True))]
    yield [FadeIn(sea_text("it asks us to believe in infinitely many electrons that nobody can see", -0.6))]


@slide("And it depends on the exclusion principle", "Why the sea was dropped")
def dropped2(s):
    s.add(sea_struck(), sea_text("physicists dropped the sea, for two reasons", 2.1, RED, True),
          sea_text("it asks us to believe in infinitely many electrons that nobody can see", 0.8))
    yield [FadeIn(sea_text("it depends on the exclusion principle, which not every particle obeys", -0.8))]
    yield [FadeIn(sea_text("yet the particles that don't obey it have antiparticles too", -2.3, INK, True))]


def pair_made():
    o = P(-0.6, 0.4)
    a, b = P(4.4, 1.9), P(4.4, -1.1)
    return VGroup(Line(o, a, color=LINE, stroke_width=4), Line(o, b, color=LINE, stroke_width=4), electron(a[0], a[1], BLUE, 0.2),
                  electron(b[0], b[1], ORANGE, 0.2), left_at(lab("an electron", 26, BLUE), 4.8, 1.9), left_at(lab("a positron", 26, ORANGE), 4.8, -1.1))


def light_in():
    return VGroup(wiggle(P(-6.6, 0.4), P(-0.8, 0.4), amp=0.16, waves=8), at(lab("a packet of light goes in", 26, INK), -3.8, 1.2))


@slide("Dirac's hole points at the real issue.", "The real issue")
def issue(s):
    g = light_in()
    yield [Create(g[0]), FadeIn(g[1])]
    p = pair_made()
    yield [Create(p[0]), Create(p[1]), FadeIn(VGroup(*p[2:]))]
    yield [FadeIn(at(T("the number of particles changed", 34, INK, True), 0, -2.6))]


@slide("The last chapter allows that.", "Energy becomes mass")
def allows(s):
    s.add(light_in(), pair_made())
    yield [FadeIn(at(T("chapter 4: mass is a form of energy", 28, INK, True), 0, -2.0))]
    yield [FadeIn(at(lab("enough energy can become the mass of new particles", 26, INK), 0, -2.9)),
           Flash(P(-0.6, 0.4), color=MUTED, flash_radius=0.5)]


def one_particle_wave():
    xs = np.linspace(-6.6, 1.2, 100)
    wave = VMobject(color=INK, stroke_width=4).set_points_smoothly(
        [P(x, -0.3 + 1.5 * np.exp(-((x + 2.7) / 1.5) ** 2) * np.cos(3.2 * (x + 2.7))) for x in xs])
    return VGroup(xaxis(-6.8, 1.4, -0.3), wave, at(mt(r"\psi", size=56), -5.6, 1.4))


@slide("A wave function can't describe that.", "One particle only")
def onlyone(s):
    yield [FadeIn(one_particle_wave()), FadeIn(right_text("a wave function gives one amplitude for each position", 1.6))]
    yield [FadeIn(right_text("of one particle", 0.5, INK, True, size=30))]
    m = right_text("nothing in it can say that there are now two more", -1.2, RED)
    yield [FadeIn(m), Create(xmark(m[-1]))]


@slide("Every equation in this chapter describes a fixed number of particles.", "A fixed number")
def fixedn(s):
    cards = VGroup(*[at(card(n, 3.6, 1.2, INK, 28), x, 1.3) for n, x in zip(("Schrödinger", "Klein–Gordon", "Dirac"), (-4.6, 0, 4.6))])
    dots = VGroup(*[electron(x, 0.2, INK, 0.16) for x in (-4.6, 0, 4.6)])
    yield [FadeIn(cards), FadeIn(dots), FadeIn(at(T("each describes a fixed number of particles", 28, INK, True), 0, -0.8))]
    yield [LaggedStart(*[Indicate(c, color=INK, scale_factor=1.06) for c in cards], lag_ratio=0.3)]
    m = at(T("at high energy, the number isn't fixed", 30, RED, True), -0.3, -2.3)
    yield [FadeIn(m), Create(xmark(m))]


def count_ladder(x=-4.4):
    lad = ladder(x, LAD[1], 5, LAD[2], 2.4)
    nums = VGroup(*[at(T(str(k), 26, MUTED), x - 1.7, lad_y(k)) for k in range(5)])
    return VGroup(lad, nums)


@slide("We already have the tool for counting.", "The tool for counting")
def counting(s):
    t = clock(s)
    marker = always_redraw(lambda: Dot(P(-4.4, lad_y(int(1.2 * t.get_value()) % 5) + 0.2), radius=0.15, color=INK))
    g = count_ladder()
    yield [FadeIn(g[0]), FadeIn(marker), FadeIn(left_at(lab("chapter 3: the spring's energy came in rungs", 26, INK), -1.8, 1.2))]
    yield [FadeIn(g[1]), FadeIn(left_at(lab("the rung number counted its quanta", 26, INK, True), -1.8, -0.3))]


def field_line(t, x0=0.6, x1=7.0, y=0.4, n=17):
    def draw():
        g = VGroup(Line(P(x0, y), P(x1, y), color=LINE, stroke_width=3))
        for x in np.linspace(x0 + 0.2, x1 - 0.2, n):
            h = 1.0 * np.sin(1.3 * x - 2.0 * t.get_value())
            g.add(Dot(P(x, y), radius=0.05, color=MUTED))
            if abs(h) > 0.12:
                g.add(Arrow(P(x, y), P(x, y + h), buff=0, color=INK, stroke_width=3.5, tip_length=0.12, max_tip_length_to_length_ratio=0.5,
                            max_stroke_width_to_length_ratio=30))
        return g
    return always_redraw(draw)


@slide("The coming chapters change what the wave function is.", "From a wave function to a field")
def tofield(s):
    t = clock(s)
    psi = at(mt(r"\psi", size=120), -5.0, 0.7)
    old = at(lab("one particle's wave function", 26, INK), -4.4, -0.8)
    yield [FadeIn(psi), FadeIn(old)]
    yield [Create(Line(old.get_left() + LEFT * 0.1, old.get_right() + RIGHT * 0.1, color=RED, stroke_width=4))]
    yield [FadeIn(at(T("it becomes a field", 32, INK, True), -4.4, -1.8)), GrowArrow(varrow(P(-3.6, 0.7), P(0.2, 0.7)))]
    s.add(field_line(t))  # a redrawn object is added, not faded in
    yield [FadeIn(at(words("a value at every point of space, like the electric field", 34, 26, INK, ORIGIN), 3.8, -1.7))]


@slide("Each wave of the field is a spring.", "Rungs count particles")
def rungs(s):
    t = clock(s)
    n = ValueTracker(1.0)
    xs = np.linspace(-7.0, -3.2, 60)
    wave = always_redraw(lambda: VMobject(color=INK, stroke_width=4).set_points_smoothly(
        [P(x, 0.6 + 0.6 * np.sin(2.6 * x - 2.0 * t.get_value())) for x in xs]))
    lx = 0.2
    lad = VGroup(ladder(lx, LAD[1], 5, LAD[2], 2.2), *[at(T(str(k), 26, MUTED), lx - 1.6, lad_y(k)) for k in range(5)])
    marker = always_redraw(lambda: Dot(P(lx, lad_y(n.get_value()) + 0.2), radius=0.15, color=INK))

    def made():
        k = int(round(n.get_value()))
        return VGroup(hollow(), *[electron(3.0 + 0.6 * j, -1.0, INK, 0.17) for j in range(k)])
    s.add(n, wave, marker)  # redrawn objects are added, not faded in
    yield [FadeIn(at(lab("one wave of the field", 24, INK), -5.1, -0.6)), GrowArrow(varrow(P(-2.9, 0.6), P(-1.9, 0.6))), FadeIn(lad),
           FadeIn(at(lab("is a spring", 24, INK), 0.2, 2.4))]
    s.add(always_redraw(made))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(left_at(words("its rung: the number of particles with that wave's momentum", 26, 24), 2.5, 0.6))]
    yield [n.animate.set_value(3.0), FadeIn(left_at(words("up a rung creates a particle, down a rung removes one", 26, 24, INK, bold=True), 2.5, -2.3))]


@slide("The coming chapters show that in that theory", "The negative energies, read again")
def reread(s):
    xs = np.linspace(-6.8, -3.4, 60)
    wave = VMobject(color=ORANGE, stroke_width=4).set_points_smoothly([P(x, 1.2 + 0.5 * np.sin(3.2 * x)) for x in xs])
    yield [FadeIn(wave), FadeIn(at(lab("the negative-energy waves", 26, ORANGE, True), -5.1, 0.1)),
           FadeIn(at(lab("in that theory, the negative energies stop being a problem", 24), 0, 2.45))]
    bad = at(card("particles with\nnegative energy", 4.2, 1.3, RED, 26), 3.4, 1.2)
    yield [GrowArrow(varrow(P(-3.0, 1.2), P(1.1, 1.2))), FadeIn(bad), Create(cross(bad, RED, 5)), FadeIn(at(lab("don't describe", 22), -1.0, 1.55))]
    good = at(card("the creation of antiparticles,\nwhose energy is positive", 5.4, 1.4, ORANGE, 26), 3.4, -1.0)
    yield [GrowArrow(varrow(P(-3.0, 0.9), P(0.5, -0.9))), FadeIn(good), FadeIn(at(lab("they describe", 22), -2.3, -0.5))]
    m = at(T("so nothing falls", 32, TEAL, True), -0.3, -2.7)
    yield [FadeIn(m), Create(tick(m))]


@slide("And the Klein-Gordon quantity that could be negative", "The quantity that could be negative")
def charge(s):
    eq = at(rho(64), -4.4, 0.9)
    yield [FadeIn(eq), FadeIn(at(lab("the Klein–Gordon quantity", 24), -4.4, 2.2)), GrowArrow(varrow(P(-2.2, 0.9), P(0.0, 0.9))),
           FadeIn(left_at(T("electric charge", 40, INK, True), 0.5, 0.9))]
    yield [FadeIn(VGroup(electron(-2.6, -1.3, BLUE, 0.2), left_at(lab("particles: one sign", 26, INK), -2.1, -1.3))),
           FadeIn(VGroup(electron(-2.6, -2.3, ORANGE, 0.2), left_at(lab("antiparticles: the opposite sign", 26, ORANGE), -2.1, -2.3)))]


@slide("The Klein-Gordon equation comes back", "Both equations come back")
def comeback(s):
    a = at(card("the Klein–Gordon equation", 5.2, 1.3, INK, 26), -4.0, 1.2)
    b = at(card("the Dirac equation", 5.2, 1.3, INK, 26), -4.0, -1.2)
    yield [FadeIn(a), GrowArrow(varrow(P(-1.2, 1.2), P(0.2, 1.2))),
           FadeIn(left_at(words("the equation for fields whose particles have no spin", 30, 26), 0.6, 1.2))]
    yield [FadeIn(b), GrowArrow(varrow(P(-1.2, -1.2), P(0.2, -1.2))), FadeIn(left_at(words("the equation for the electron's field", 30, 26), 0.6, -1.2))]


# ================================================================== where this leads
deck.part("Where this leads")

RECAP_Y = (1.9, 0.85, -0.2, -1.25, -2.3)
RECAP = (("the relativistic energy rule gives the Klein–Gordon equation", INK, INK),
         ("it has negative energies, and its chance can be negative", RED, INK),
         ("Dirac's equation uses matrices, and its chance is never negative", TEAL, INK),
         ("its negative energies predicted the positron", ORANGE, INK),
         ("a single wave function can't count particles that come and go", MUTED, INK))


def recap_row(k):
    text, dot, color = RECAP[k]
    return VGroup(Dot(P(-6.6, RECAP_Y[k]), radius=0.12, color=dot), left_at(lab(text, 28, color), -6.2, RECAP_Y[k]))


@slide("Where this leads.", "Where we've got to")
def recap1(s):
    yield hold()
    yield [FadeIn(recap_row(0), shift=RIGHT * 0.15)]
    yield [FadeIn(recap_row(1), shift=RIGHT * 0.15)]


@slide("Dirac's equation uses matrices, and its chance is never negative.", "Where we've got to")
def recap2(s):
    s.add(recap_row(0), recap_row(1))
    yield [FadeIn(recap_row(2), shift=RIGHT * 0.15)]
    yield [FadeIn(recap_row(3), shift=RIGHT * 0.15)]
    yield [FadeIn(recap_row(4), shift=RIGHT * 0.15)]


@slide("The next chapter looks at the Dirac equation piece by piece.", "Next: the Dirac equation")
def nxt(s):
    c = at(card("the next chapter:\nThe Dirac Equation", 5.0, 1.8, INK, 30), -3.8, 0.4)
    yield [FadeIn(c), FadeIn(at(lab("the equation, piece by piece", 26, INK), -3.8, -1.2))]
    col = at(col4(64), 3.4, 0.4)
    yield [GrowArrow(varrow(P(-1.1, 0.4), P(1.2, 0.4))), FadeIn(col), FadeIn(at(lab("what its four wave functions do", 26, INK, True), 3.4, -2.3))]

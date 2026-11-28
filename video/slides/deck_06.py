"""Slides for chapter six, The Dirac Equation.

Every value comes from video/scripts/06-dirac-equation.txt or
docs/dirac-equation.md. The narration does not read formulas aloud, so each
formula is shown at the sentence that states it in words, in the page's
notation, set with MathTex (LaTeX). The drawings redraw the chapter's figures in
docs/manim/ (magnet-twice-too-strong, angular-momentum-parts, rest-spinor-basis,
half-angle-state, neutron-full-turn) as animations, with the same geometry. The
Stern-Gerlach rig follows deck_02a.

Colors: BLUE for positive energy and what has it (+mc², the upper pair of the
column, an electron) and for the list of two amplitudes that the upper pair is
(a spin state, the arrow that draws it, the neutron's wave), PURPLE for the
matrices (alpha, beta, the spin matrices S-hat, Y-hat, Z-hat, Sigma) and for
the spin they turn out to be (its arrow in space, its values, its name), TEAL
for the momentum along y and each term that carries it, ORANGE for the momentum
along x and each term that carries it, RED only for what fails or is ruled out
(a check that fails, a rule's wrong prediction, a struck-out term), INK for
equations, for what was measured and for what is kept, MUTED and LINE for
negative energy and the lower pair of the column, which this chapter sets
aside, and for apparatus, axes, context and connectors.
"""
from manim import *

from engine import *

STEM = "06-dirac-equation"
deck = Deck(f"scripts/{STEM}.txt")
slide = deck.slide

LOW = MUTED   # negative energy and the lower pair
PX = ORANGE   # the momentum along x
PY = TEAL     # the momentum along y


# ------------------------------------------------------------------ small helpers

def P(x, y, z=0.0):
    """A point on the slide, from two coordinates (or from a point's three)."""
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


def paint(m, color, *parts):
    """Color some parts of a formula."""
    for k in parts:
        m[k].set_color(color)
    return m


def purple(tex, size=48):
    return mt(tex, size=size, color=PURPLE)


def mix(*items, size=24, color=INK, buff=0.16, bold=False):
    """Words and formulas on one line."""
    return VGroup(*[T(i, size, color, bold) if isinstance(i, str) else i for i in items]).arrange(RIGHT, buff=buff)


def hold():
    """A step that adds nothing, so the next reveal waits for its sentence."""
    return [Wait()]


def tick(mob, color=INK, buff=0.2):
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
    """Time that runs at the rate held by the tracker `gate`, so a step can start it or speed it up."""
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


def under(mob, color=INK, gap=0.1, width=4):
    """A line under a part of a formula, to point at it without boxing it in."""
    return Line(mob.get_corner(DL) + DOWN * gap, mob.get_corner(DR) + DOWN * gap, color=color, stroke_width=width)


def varrow(a, b, color=MUTED, width=4, tip=0.2):
    return Arrow(a, b, buff=0, color=color, stroke_width=width, tip_length=tip,
                 max_tip_length_to_length_ratio=0.4, max_stroke_width_to_length_ratio=30)


def uvec(a):
    return np.array([np.cos(a), np.sin(a), 0.0])


def grid(rows, cols, cell=0.5, color=PURPLE, fill=0.08):
    """A table of numbers drawn as empty cells."""
    return VGroup(*[Square(cell, stroke_color=color, stroke_width=2.5, fill_color=color, fill_opacity=fill)
                    .move_to(P((c - (cols - 1) / 2) * cell, ((rows - 1) / 2 - r) * cell))
                    for r in range(rows) for c in range(cols)])


def electron(x, y, color=BLUE, r=0.13):
    return Dot(P(x, y), radius=r, color=color)


def spin_arrow(x, y, up=True, L=1.0, color=PURPLE, width=6):
    """The spin, drawn as an arrow centred on a point."""
    d = (1 if up else -1) * L / 2
    return varrow(P(x, y - d), P(x, y + d), color, width, 0.2)


def espin(x, y, up=True, L=1.1, r=0.17):
    """An electron with its spin."""
    return VGroup(spin_arrow(x, y, up, L), electron(x, y, BLUE, r))


def mat(rows, size=40, color=INK, h=1.0, v=0.75):
    """A matrix whose entries can be picked out with get_entries()."""
    m = Matrix(rows, left_bracket="(", right_bracket=")", h_buff=h, v_buff=v, bracket_h_buff=0.16, bracket_v_buff=0.2,
               element_to_mobject_config={"font_size": size})
    m.set_color(color)
    return m


def named(tex, m, size=40, color=INK):
    """A matrix with its name and an equals sign in front."""
    return VGroup(mt(tex + " =", size=size, color=color), m).arrange(RIGHT, buff=0.2)


def col4m(size=48, v=0.8, colored=True):
    """The column of four wave functions; the upper pair is BLUE and the lower pair is LOW."""
    m = mat([[r"\psi_1"], [r"\psi_2"], [r"\psi_3"], [r"\psi_4"]], size, v=v)
    if colored:
        for k, e in enumerate(m.get_entries()):
            e.set_color(BLUE if k < 2 else LOW)
    return m


# ------------------------------------------------------------------ the formulas, as the page writes them

E4M = r"\frac{e\hbar}{4m}"
E2M = r"\frac{e\hbar}{2m}"
HB2 = r"\hbar/2"
S_ROWS = [["0", "1"], ["1", "0"]]
Y_ROWS = [["0", "-i"], ["i", "0"]]
Z_ROWS = [["1", "0"], ["0", "-1"]]
AVG = (r"\frac{d\langle A\rangle}{dt}", "=", r"\frac{1}{i\hbar}", r"\,\langle", r"[\hat A,\ \hat H]", r"\rangle")
LZ = ("L_z", "=", r"x\,p_y", "-", r"y\,p_x")
LZ_HAT = (r"\hat L_z", "=", r"\hat x\,\hat p_y", "-", r"\hat y\,\hat p_x")
E_UP = r"E_{\text{up}} = E_0 - \frac{q\hbar}{2m}\,B"
E_DOWN = r"E_{\text{down}} = E_0 + \frac{q\hbar}{2m}\,B"


def rule(size=56):
    """The rule for a spinning charge: mu, =, q over 2m, times, and the words."""
    m = mt(r"\mu", "=", r"\frac{q}{2m}", r"\times", size=size)
    return VGroup(m, T("angular momentum", size * 0.62, INK)).arrange(RIGHT, buff=0.22 * size / 56)


def lin3(size=44):
    """Chapter 5's straight-line rule in space; parts 1, 3, 5 and 7 are the four matrices."""
    return paint(mt("E =", r"\alpha_x", r"\,p_xc +", r"\alpha_y", r"\,p_yc +", r"\alpha_z", r"\,p_zc +", r"\beta", r"\,mc^2",
                    size=size), PURPLE, 1, 3, 5, 7)


def dirac3(size=56):
    """The Dirac equation: the time side, =, H-hat, psi."""
    return mt(r"i\hbar\,\frac{\partial\psi}{\partial t}", "=", r"\hat H", r"\psi", size=size)


def ham(size=48):
    """The energy operator. Parts 2, 5, 8 and 12 are the matrices; 3, 6 and 9 the momenta; 12 and 13 the mass term."""
    return paint(mt(r"\hat H =", r"c\,\bigl(", r"\alpha_x", r"\,\hat p_x", "+", r"\alpha_y", r"\,\hat p_y", "+", r"\alpha_z", r"\,\hat p_z",
                    r"\bigr)", "+", r"\beta", r"\,mc^2", size=size), PURPLE, 2, 5, 8, 12)


def bracket(lhs, pref, size=48):
    """A commutator's result, pref (alpha_x p_y - alpha_y p_x). Parts 2 and 5 are the matrices, 3 and 6 the momenta."""
    m = mt(lhs, pref + r"\bigl(", r"\alpha_x", r"\,\hat p_y", "-", r"\alpha_y", r"\,\hat p_x", r"\bigr)", size=size)
    paint(m, PURPLE, 2, 5)
    m[3].set_color(PY)
    m[6].set_color(PX)
    return m


def leftover(size=48):
    return bracket(r"[\hat L_z,\ \hat H] =", r"i\hbar c\,", size)


def requirement(size=48):
    return bracket(r"[\hat T,\ \hat H] =", r"-\,i\hbar c\,", size)


def lz(size=48, hats=False):
    m = mt(*(LZ_HAT if hats else LZ), size=size)
    m[2].set_color(PY)
    m[4].set_color(PX)
    return m


def total(size=56):
    """The kept total: [L_z + (h-bar/2) Sigma_z, H] = 0. Part 1 is the motion's term, part 3 the spin's."""
    return paint(mt(r"\Bigl[", r"\hat L_z", "+", r"\frac{\hbar}{2}\,\Sigma_z", r",\ \hat H\Bigr]", "= 0", size=size), PURPLE, 3)


def strength(tex, size=64, color=INK):
    return mt(r"\mu", "=", tex, size=size, color=color)


# ------------------------------------------------------------------ the table of results

TAB_X = (-4.2, 0.0, 4.2)
TAB_Y = (1.1, 0.2, -0.7, -1.6)
TAB_SPIN = ("up", "down", "up", "down")


def tab_head():
    return VGroup(*[at(T(h, 24, MUTED, True), x, 2.2) for h, x in zip(("entry of the column", "energy", "spin"), TAB_X)],
                  Line(P(-6.4, 1.72), P(6.4, 1.72), color=LINE, stroke_width=3))


def tab_row(k):
    up = k % 2 == 0
    spin = VGroup(T(TAB_SPIN[k], 28, PURPLE, True), spin_arrow(0, 0, up, 0.6, width=5)).arrange(RIGHT, buff=0.25)
    return VGroup(at(mt(r"\psi_%d" % (k + 1), size=48, color=BLUE if k < 2 else LOW), TAB_X[0], TAB_Y[k]),
                  at(mt("+mc^2" if k < 2 else "-mc^2", size=44, color=BLUE if k < 2 else LOW), TAB_X[1], TAB_Y[k]),
                  at(spin, TAB_X[2], TAB_Y[k]))


def tab_full():
    return VGroup(tab_head(), *[tab_row(k) for k in range(4)])


# ------------------------------------------------------------------ a ring of charge

RC = (-4.2, 0.2)


def ring(c=RC, w=3.6, h=1.3):
    return Ellipse(width=w, height=h, color=MUTED, stroke_width=4).move_to(P(*c))


def ring_dots(t, c=RC, w=3.6, h=1.3, n=6, rate=1.5):
    """Bits of charge going round the ring."""
    def draw():
        a = rate * t.get_value()
        return VGroup(*[Dot(P(c[0] + w / 2 * np.cos(a + TAU * k / n), c[1] + h / 2 * np.sin(a + TAU * k / n)), radius=0.1, color=INK)
                        for k in range(n)])
    return always_redraw(draw)


def ring_magnet(c=RC):
    return VGroup(varrow(P(c[0], c[1] - 0.2), P(c[0], c[1] + 1.9), INK, 8, 0.26), at(lab("magnet", 24, INK, True), c[0] + 0.85, c[1] + 1.65))


def ring_text(text, y, color=INK, bold=False, chars=32, size=26):
    return left_at(words(text, chars, size, color, bold=bold), -1.3, y)


def pendulum(t, pivot, L=1.9, swing=0.5):
    def draw():
        a = swing * np.sin(2.2 * t.get_value())
        bob = pivot + L * np.array([np.sin(a), -np.cos(a), 0.0])
        return VGroup(Line(pivot, bob, color=MUTED, stroke_width=4), Dot(pivot, radius=0.07, color=INK), Dot(bob, radius=0.2, color=INK))
    return always_redraw(draw)


# ------------------------------------------------------------------ the Stern-Gerlach rig (deck_02a)

def sg_oven():
    oven = Rectangle(width=1.3, height=1.1, color=INK, fill_color=PALE, fill_opacity=1).move_to([-6.2, 0.3, 0])
    return VGroup(oven, lab("oven", 22).move_to([-6.2, -0.55, 0]))


def sg_poles():
    top = Polygon([-3.4, 1.55, 0], [-1.4, 1.55, 0], [-1.4, 0.85, 0], [-2.4, 0.55, 0], [-3.4, 0.85, 0], color=INK, fill_color=PALE, fill_opacity=1)
    bot = Polygon([-3.4, -0.25, 0], [-1.4, -0.25, 0], [-1.4, -0.95, 0], [-3.4, -0.95, 0], color=INK, fill_color=PALE, fill_opacity=1)
    return VGroup(top, bot, lab("magnet", 22).move_to([-2.4, 1.85, 0]))


def sg_beam():
    return VGroup(Line([-5.55, 0.3, 0], [-1.4, 0.3, 0], color=INK, stroke_width=4))


def sg_plate():
    return VGroup(Line([0.4, -1.6, 0], [0.4, 2.0, 0], color=MUTED, stroke_width=6), lab("glass plate", 22).move_to([0.4, -1.95, 0]))


def sg_rig():
    return VGroup(sg_oven(), sg_beam(), sg_poles(), sg_plate())


def sg_split(g=0.85):
    """The two beams after the magnet and their two spots, a distance 2g apart."""
    return VGroup(Line([-1.4, 0.3, 0], [0.35, 0.3 + g, 0], color=INK, stroke_width=4), Line([-1.4, 0.3, 0], [0.35, 0.3 - g, 0], color=INK, stroke_width=4),
                  Dot([0.4, 0.3 + g, 0], radius=0.14, color=INK), Dot([0.4, 0.3 - g, 0], radius=0.14, color=INK))


def sg_text(text, y, color=INK, bold=False, chars=30, size=26):
    return left_at(words(text, chars, size, color, bold=bold), 1.5, y)


def plate(x, y, ys, color=INK, w=1.9, h=2.6):
    """The glass plate seen face on, with its spots of silver."""
    g = VGroup(Rectangle(width=w, height=h, stroke_color=INK, stroke_width=3, fill_color=PALE, fill_opacity=0.7).move_to(P(x, y)))
    for dy in ys:
        g.add(Ellipse(width=1.1, height=0.26, stroke_width=0, fill_color=color, fill_opacity=0.9).move_to(P(x, y + dy)))
    return g


def gap_arrow(x, y, g, color=INK):
    return DoubleArrow(P(x, y - g), P(x, y + g), buff=0, color=color, stroke_width=4, tip_length=0.16)


# ------------------------------------------------------------------ results in steps of h-bar

AX = -3.4     # the axis of results
STEP = 1.3    # one h-bar, in screen units


def am_axis(y0=-3.1, y1=2.6):
    ax = Arrow(P(AX, y0), P(AX, y1), buff=0, color=MUTED, stroke_width=3, tip_length=0.18, max_tip_length_to_length_ratio=0.1)
    return VGroup(ax, right_at(words("angular momentum along a chosen direction", 16, 22, MUTED, align=RIGHT), AX - 0.5, 1.9))


def am_mark(y, color=INK):
    return VGroup(Line(P(AX - 0.3, y), P(AX + 0.3, y), color=color, stroke_width=4), Dot(P(AX, y), radius=0.13, color=color))


def am_zero(y):
    return VGroup(DashedLine(P(AX - 1.0, y), P(AX + 0.5, y), color=MUTED, stroke_width=2.5), right_at(lab("zero", 22), AX - 1.15, y))


def am_pair(y, o):
    """Two results one step apart, with the lower one at y + o; they follow the tracker o."""
    g = VGroup(am_mark(y), am_mark(y + STEP), gap_arrow(AX + 0.75, y + STEP / 2, STEP / 2, MUTED),
               left_at(mt(r"\hbar", size=40, color=MUTED), AX + 0.95, y + STEP / 2))
    c0 = g.get_center()
    g.add_updater(lambda m: m.move_to(c0 + UP * o.get_value()))
    return g


def am_text(text, y, color=INK, bold=False, chars=34, size=26):
    return left_at(words(text, chars, size, color, bold=bold), 0.3, y)


# ================================================================== opening
deck.part("Chapter six")


@slide("Chapter six.", "The Dirac Equation")
def opening(s):
    c = at(col4m(64, 0.95, False), -3.2, -0.3)
    yield [FadeIn(c)]
    e = espin(3.2, -0.3, True, 2.2, 0.26)
    yield [FadeIn(e[1]), GrowArrow(e[0])]


# ================================================================== previously
deck.part("Previously")


def prev_col(x=-4.6, y=-0.2, size=64):
    return at(col4m(size, 0.95), x, y)


def prev_signs(c):
    e = c.get_entries()
    return VGroup(left_at(mix("two have positive energy", size=26, color=BLUE), -2.6, (e[0].get_y() + e[1].get_y()) / 2),
                  left_at(mix("two have negative energy", size=26, color=LOW), -2.6, (e[2].get_y() + e[3].get_y()) / 2))


@slide("The last chapter ended with the Dirac equation", "Four wave functions")
def prev1(s):
    c = prev_col()
    yield [FadeIn(at(card("the Dirac equation", 4.4, 1.0, INK, 28), 3.6, 2.0)), FadeIn(c),
           FadeIn(at(lab("its state: four wave functions", 24, INK), -4.6, -2.75))]
    yield [FadeIn(prev_signs(c), lag_ratio=0.3)]


@slide("That left a question open.", "A question left open")
def prev2(s):
    c = prev_col()
    signs = prev_signs(c)
    s.add(c, signs, at(lab("its state: four wave functions", 24, INK), -4.6, -2.75))
    yield [FadeIn(at(T("a question left open", 30, INK, True), 4.6, 2.0))]
    q = VGroup(*[left_at(T("what tells these two apart?", 26, INK, True), 2.8, signs[k].get_y()) for k in range(2)])
    marks = VGroup(*[at(T("?", 44, INK, True), 2.25, signs[k].get_y()) for k in range(2)])
    yield [FadeIn(marks), FadeIn(q)]


# ================================================================== the chapter at a glance
deck.part("Chapter six")


@slide("This chapter answers it.", "The answer is the spin")
def glance1(s):
    e = espin(-4.4, 0.2, True, 2.4, 0.26)
    yield [FadeIn(e[1]), GrowArrow(e[0]), FadeIn(left_at(T("the answer: the electron's spin", 34, PURPLE, True), -2.6, 0.9))]
    yield [FadeIn(left_at(lab("nobody put it into the equation", 28, INK), -2.6, -0.3))]


@slide("Two more results come with it.", "Two more results")
def glance2(s):
    a = at(card("the strength of the\nelectron's magnet", 5.6, 1.7, INK, 28), -3.6, 0.7)
    b = at(card("turning an electron once round\ndoesn't bring its state back", 6.4, 1.7, INK, 26), 3.6, 0.7)
    yield [FadeIn(at(lab("two more results come with the spin", 26, INK), 0, 2.3))]
    yield [FadeIn(a, shift=DOWN * 0.15), FadeIn(at(lab("it had puzzled physicists for years", 24), -3.6, -0.6))]
    yield [FadeIn(b, shift=DOWN * 0.15)]


@slide("Here's where we end up, for a particle at rest.", "Where we end up")
def glance3(s):
    yield [FadeIn(VGroup(electron(-1.9, -3.1, BLUE, 0.16), left_at(lab("for a particle at rest", 26, INK), -1.5, -3.1)))]
    yield [FadeIn(tab_head()), LaggedStart(*[FadeIn(tab_row(k), shift=DOWN * 0.1) for k in range(4)], lag_ratio=0.15)]


@slide("The first two wave functions have positive energy.", "Where we end up")
def glance4(s):
    rows = [tab_row(k) for k in range(4)]
    s.add(tab_head(), *rows)
    yield [Create(frame(VGroup(rows[0][0], rows[0][1], rows[1][1]), BLUE, 0.16))]
    yield [Create(frame(VGroup(rows[0][2], rows[1][2]), PURPLE, 0.16))]
    yield [Create(frame(VGroup(rows[2][0], rows[2][1], rows[3][1]), LOW, 0.16)), Create(frame(VGroup(rows[2][2], rows[3][2]), PURPLE, 0.16))]
    yield [FadeIn(caption("We start with the magnet.", -3.2, INK, 28))]


# ================================================================== a magnet twice too strong
deck.part("A magnet twice too strong")


@slide("A magnet twice too strong.", "Silver atoms through a magnet")
def sg1(s):
    yield [FadeIn(sg_oven()), FadeIn(sg_poles()), FadeIn(sg_plate()), FadeIn(sg_text("chapter 2a opened with silver atoms flying through a magnet", 1.6))]
    dots = VGroup(*[Dot([-5.4 + 0.3 * i, 0.3, 0], radius=0.08, color=INK) for i in range(4)])
    yield [FadeIn(dots), dots.animate.shift(RIGHT * 2.6), Create(sg_beam()), Create(sg_split())]


@slide("Each atom is a tiny magnet itself.", "Each atom is a tiny magnet")
def sg2(s):
    s.add(sg_rig(), sg_split())
    a = VGroup(Circle(radius=0.34, color=INK, stroke_width=3, fill_color=PALE, fill_opacity=1).move_to(P(-6.3, -2.7)),
               varrow(P(-6.3, -3.1), P(-6.3, -2.2), INK, 6, 0.18))
    yield [FadeIn(a), FadeIn(left_at(lab("each silver atom: a tiny magnet", 26, INK), -5.6, -2.7))]
    yield [FadeIn(sg_text("it comes from a property of one of its electrons", 1.6)), FadeIn(left_at(T("spin", 44, PURPLE, True), 1.5, 0.2))]


@slide("We used the spin there without saying what it is.", "Two questions")
def twoq(s):
    e = espin(-5.2, 0.0, True, 2.0, 0.24)
    s.add(e)
    a = at(card("what is the spin?", 6.4, 1.2, INK, 28), 1.6, 1.4)
    b = at(card("how strong is the electron's magnet?", 6.4, 1.2, INK, 26), 1.6, -0.3)
    yield [FadeIn(a, shift=RIGHT * 0.15)]
    yield [FadeIn(b, shift=RIGHT * 0.15)]
    yield [FadeIn(at(lab("both questions have a history", 26, INK, True), 1.6, -1.9))]


@slide("Start with a fact from ordinary physics.", "A current in a loop")
def loop1(s):
    t = clock(s)
    yield [FadeIn(ring()), FadeIn(ring_text("a fact from ordinary physics", 1.9, MUTED))]
    s.add(ring_dots(t))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(ring_text("charge going round a circle", 0.7)), FadeIn(ring_text("is an electric current in a loop", -0.3, INK, True))]


@slide("And a current in a loop is a magnet", "A spinning charge is a magnet")
def loop2(s):
    t = clock(s)
    s.add(ring(), ring_dots(t))
    m = ring_magnet()
    yield [GrowArrow(m[0]), FadeIn(m[1]), FadeIn(ring_text("a current in a loop is a magnet, as in an electromagnet", 1.2))]
    yield [FadeIn(ring_text("so anything charged that spins is a magnet", -0.8, INK, True, size=28))]


@slide("Anything with mass that spins also has angular momentum.", "Angular momentum")
def loop3(s):
    t = clock(s)
    s.add(ring(), ring_dots(t), ring_magnet())
    yield [FadeIn(ring_text("anything with mass that spins also has angular momentum", 1.9, INK, True))]
    yield [FadeIn(ring_text("the amount of turning motion it carries", 0.5))]
    s.add(pendulum(t, P(5.6, 0.2)))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(at(lab("chapter 1: the pendulum", 24), 5.0, -2.3))]


BAR_X = (0.6, 4.2)
BAR_Y = -2.2


def twin_bars(w):
    def draw():
        h = 1.1 * w.get_value()
        return VGroup(*[Rectangle(width=1.3, height=h, stroke_color=INK, stroke_width=2.5, fill_color=INK, fill_opacity=0.25)
                        .move_to(P(x, BAR_Y + h / 2)) for x in BAR_X])
    return always_redraw(draw)


@slide("Now spin the body twice as fast.", "Twice as fast")
def loop4(s):
    w = ValueTracker(1.0)
    t = gated_clock(s, w)
    s.add(ring(), ring_dots(t), ring_magnet(), twin_bars(w), Line(P(-0.5, BAR_Y), P(5.3, BAR_Y), color=MUTED, stroke_width=3),
          at(words("the magnet's strength", 12, 24, INK, ORIGIN), BAR_X[0], BAR_Y - 0.6), at(words("the angular momentum", 12, 24, INK, ORIGIN), BAR_X[1], BAR_Y - 0.6))
    yield [FadeIn(at(lab("spin the body twice as fast", 26, INK), -4.2, -1.6))]
    yield [w.animate.set_value(2.0), FadeIn(at(T("both double", 28, INK, True), 2.4, 2.3))]
    yield [FadeIn(at(T("so their ratio is fixed", 28, INK, True), -4.2, -2.6))]


@slide("The rule is on screen.", "The rule for a spinning charge")
def rule1(s):
    r = at(rule(80), 1.0, 0.4)
    mu = r[0][0]
    yield [FadeIn(r)]
    name = right_at(words("the strength of the magnet", 12, 24, INK, align=RIGHT), mu.get_left()[0] - 0.75, mu.get_y())
    yield [FadeIn(name), Create(Line(name.get_right() + RIGHT * 0.12, mu.get_left() + LEFT * 0.12, color=MUTED, stroke_width=2))]
    yield [FadeIn(note(r[0][2], "a fixed number: the charge over twice the mass", INK, chars=24, buff=0.2))]
    yield [FadeIn(caption("It holds when the charge is spread through the body the same way as the mass.", -3.6))]


@slide("Now for what was measured.", "What was measured")
def meas1(s):
    yield [FadeIn(sg_rig())]
    yield [FadeIn(sg_text("the experiment with silver atoms measures the magnet directly", 1.7))]
    pushes = VGroup(varrow(P(-2.9, 0.4), P(-2.9, 0.8), INK, 5, 0.14), varrow(P(-1.9, 0.2), P(-1.9, -0.2), INK, 5, 0.14))
    yield [FadeIn(at(lab("an uneven field", 22, INK), -2.4, 2.35)), FadeIn(pushes), Create(sg_split()),
           FadeIn(sg_text("the uneven field pushes each atom up or down", -0.2))]


@slide("The stronger the atom's magnet, the harder the push.", "The gap gives the strength")
def meas2(s):
    g = ValueTracker(0.35)
    s.add(sg_rig(), g, always_redraw(lambda: sg_split(g.get_value())))
    yield [g.animate.set_value(1.1), FadeIn(sg_text("the stronger the atom's magnet, the harder the push", 1.7))]
    yield [FadeIn(gap_arrow(0.95, 0.3, 1.1)), FadeIn(sg_text("so the gap between the two spots gives the strength", -0.2, INK, True))]


@slide("Otto Stern and Walther Gerlach's gap gave the value on screen", "The measured strength")
def meas3(s):
    pl = VGroup(plate(-5.4, 0.0, (0.9, -0.9)), gap_arrow(-4.1, 0.0, 0.9))
    m = at(strength(E2M, 96), 0.6, 0.0)
    yield [FadeIn(pl), FadeIn(m), FadeIn(at(lab("Otto Stern and Walther Gerlach's gap gave", 26, INK), 0.4, 2.45)),
           FadeIn(at(lab("to within ten percent", 26, INK, True), 0.6, -1.7))]
    e, mm = m[2][0], m[2][-1]
    le = right_at(words("the size of the electron's charge", 20, 24, align=RIGHT), e.get_left()[0] - 0.5, e.get_top()[1] + 0.55)
    lm = left_at(words("the electron's mass", 20, 24), 3.8, -0.9)
    yield [FadeIn(le), Create(Line(e.get_corner(UL) + P(-0.06, 0.06), le.get_corner(DR) + P(0.1, 0.0), color=MUTED, stroke_width=2)),
           FadeIn(lm), Create(Line(mm.get_right() + RIGHT * 0.12, lm.get_left() + LEFT * 0.15, color=MUTED, stroke_width=2))]
    yield [FadeIn(caption("The silver atom's magnet is the magnet of one of its electrons.", -3.1, INK, 26))]


@slide("The plate also gives a count.", "The plate also gives a count")
def count1(s):
    pl = plate(-4.4, 0.0, (1.0, -1.0), INK, 2.4, 3.4)
    yield [FadeIn(pl), FadeIn(left_at(T("a count: two spots", 30, INK, True), -2.2, 1.0))]
    yield [FadeIn(DashedVMobject(Rectangle(width=1.7, height=1.1, color=MUTED, stroke_width=2.5).move_to(P(-4.4, 0.0)), num_dashes=24)),
           FadeIn(left_at(lab("and nothing between them", 26, INK), -2.2, 0.0))]
    yield [FadeIn(left_at(lab("that count says something about angular momentum", 26, INK), -2.2, -1.6))]


@slide("By nineteen twenty-five, physicists had learned a rule", "Results come in steps")
def steps1(s):
    ys = [-2.5 + STEP * k for k in range(4)]
    yield [FadeIn(am_axis()), FadeIn(am_text("by 1925: a rule learned from the light of atoms", 1.9))]
    yield [LaggedStart(*[FadeIn(am_mark(y)) for y in ys], lag_ratio=0.2), FadeIn(am_text("measure angular momentum along a chosen direction: the results come in steps", 0.3))]
    yield [*[FadeIn(VGroup(gap_arrow(AX + 0.75, (a + b) / 2, STEP / 2, MUTED), left_at(mt(r"\hbar", size=40, color=MUTED), AX + 0.95, (a + b) / 2)))
             for a, b in zip(ys, ys[1:])], FadeIn(left_at(mix("each step is one", mt(r"\hbar", size=44), size=28, bold=True), 0.3, -1.5))]


AMZ = -0.9   # where zero sits on the axis of results


@slide("The steps fix the spacing between the results.", "Spacing, not starting point")
def steps2(s):
    o = ValueTracker(0.7)
    s.add(am_axis(), am_zero(AMZ), o, am_pair(AMZ, o))
    yield [FadeIn(am_text("the steps fix the spacing between the results", 1.9))]
    yield [o.animate.set_value(-1.4), FadeIn(am_text("they don't fix where the results start", 0.8, INK, True))]
    yield [o.animate.set_value(0.0), FadeIn(left_at(mix("they could be zero and one", mt(r"\hbar", size=40), ", say,", size=26), 0.3, -0.6)),
           FadeIn(am_text("or any two values one step apart", -1.3))]


@slide("But nothing makes up differ from down.", "Evenly either side of zero")
def steps3(s):
    o = ValueTracker(0.0)
    s.add(am_axis(), am_zero(AMZ), o, am_pair(AMZ, o))
    yield [FadeIn(am_text("nothing makes up differ from down", 2.1))]
    yield [o.animate.set_value(-STEP / 2), FadeIn(am_text("so the results sit evenly on either side of zero", 1.0))]
    yield [FadeIn(am_text("two results, one step apart, evenly either side of zero", -0.5, MUTED))]
    yield [FadeIn(left_at(mt(r"+\hbar/2", size=56, color=PURPLE), 0.3, -2.0)), FadeIn(left_at(lab("and", 26, INK), 2.4, -2.0)),
           FadeIn(left_at(mt(r"-\hbar/2", size=56, color=PURPLE), 3.3, -2.0))]


@slide("In nineteen twenty-five, George Uhlenbeck and Samuel Goudsmit", "Uhlenbeck and Goudsmit")
def ug(s):
    e = espin(-5.0, -0.2, True, 2.2, 0.24)
    yield [FadeIn(at(T("1925: George Uhlenbeck and Samuel Goudsmit", 30, INK, True), 0, 2.2)), FadeIn(e[1]), GrowArrow(e[0]),
           FadeIn(left_at(mix("an angular momentum of size", mt(HB2, size=48, color=PURPLE), size=28), -3.4, 0.7))]
    yield [FadeIn(left_at(words("it belongs to the electron itself, whether or not the electron moves round anything", 44, 26), -3.4, -0.6))]
    yield [FadeIn(left_at(mix("they called it", T("spin", 44, PURPLE, True), size=28), -3.4, -2.2))]


@slide("Now look at the gap again.", "What the gap says")
def gap1(s):
    r = at(rule(44), 0, 2.1)
    yield [FadeIn(r), FadeIn(right_at(lab("the rule for a spinning charge", 22), r.get_left()[0] - 0.4, 2.1))]
    put = at(mt(r"\mu", "=", r"\frac{e}{2m}", r"\times", r"\frac{\hbar}{2}", size=56), 0, 0.5)
    put[4].set_color(PURPLE)
    yield [FadeIn(put), FadeIn(left_at(mix("put", mt(HB2, size=36, color=PURPLE), "into the rule", size=24, color=MUTED), put.get_right()[0] + 0.5, 0.5))]
    a = at(strength(E4M, 72, RED), -3.6, -1.8)
    yield [FadeIn(a), FadeIn(at(lab("by the rule", 24, RED), -3.6, -3.0))]
    b = at(strength(E2M, 72), 3.6, -1.8)
    yield [FadeIn(b), FadeIn(at(lab("measured", 24, INK, True), 3.6, -3.0)), GrowArrow(varrow(P(-1.5, -1.8), P(1.5, -1.8), INK)),
           FadeIn(at(T("twice that", 28, INK, True), 0, -1.4))]


def three_results(x=-4.4, y=-0.9):
    g = VGroup(Line(P(x, y - 1.6), P(x, y + 1.6), color=MUTED, stroke_width=3))
    for k, tex in ((1, r"+\hbar"), (0, "0"), (-1, r"-\hbar")):
        g.add(Dot(P(x, y + 1.1 * k), radius=0.13, color=INK), left_at(mt(tex, size=44), x + 0.4, y + 1.1 * k))
    return g


@slide("Try it the other way round.", "The other way round")
def gap2(s):
    m = at(strength(E2M, 56), -5.0, 1.9)
    yield [FadeIn(m), FadeIn(at(lab("the measured strength", 24, INK, True), -5.0, 0.95))]
    back = at(mt(r"\frac{e\hbar}{2m}", "=", r"\frac{e}{2m}", r"\times", r"\hbar", size=56), 1.0, 1.9)
    yield [GrowArrow(varrow(P(-3.4, 1.9), P(-1.5, 1.9))), FadeIn(back), Create(frame(back[4], INK, 0.12, 2.5)),
           FadeIn(left_at(VGroup(mix("by the rule: a whole", mt(r"\hbar", size=36), size=24), lab("of angular momentum", 24, INK)).arrange(DOWN, buff=0.1, aligned_edge=LEFT), 3.6, 1.9))]
    yield [FadeIn(three_results()), FadeIn(at(lab("three results", 24, INK, True), -4.0, -3.0))]
    pl = plate(1.6, -0.9, (1.0, 0, -1.0), MUTED, 1.9, 2.9)
    yield [GrowArrow(varrow(P(-2.3, -0.9), P(0.4, -0.9))), FadeIn(pl), Create(cross(pl, RED, 5)),
           FadeIn(left_at(words("three spots on the plate, and there are two", 18, 26, RED, bold=True), 3.2, -0.9))]


PLATES = ((-5.0, (0.45, -0.45), HB2, E4M, "right count, gap too small", MUTED),
          (0.0, (0.9, 0.0, -0.9), r"\hbar", E2M, "right gap, one spot too many", MUTED),
          (5.0, (0.9, -0.9), None, E2M, "two spots, wide apart", INK))
PLY = 0.35


def plate_case(k):
    x, ys, am, form, text, color = PLATES[k]
    if am:
        head = VGroup(mix("angular momentum", mt(am, size=34), size=22), lab("by the rule", 22, INK)).arrange(DOWN, buff=0.08)
    else:
        head = lab("measured", 26, INK, True)
    g = max(ys)
    return VGroup(at(head, x, 2.3), plate(x - 0.9, PLY, ys, color, 1.9, 2.5), gap_arrow(x + 0.4, PLY, g, color),
                  at(mt(r"\mu=" + form, size=34, color=color if k == 2 else INK), x + 1.45, PLY),
                  at(lab(text, 22, color, k == 2), x, -1.35))


@slide("Three plates are on screen, two predicted and one measured.", "The puzzle")
def plates(s):
    cases = [plate_case(k) for k in range(3)]
    yield [LaggedStart(*[FadeIn(c) for c in cases], lag_ratio=0.2)]
    yield [Indicate(VGroup(*cases[0][1][1:]), color=INK, scale_factor=1.15), Indicate(VGroup(*cases[2][1][1:]), color=INK, scale_factor=1.15),
           FadeIn(at(mix("two spots mean an angular momentum of", mt(HB2, size=38), size=26), 0, -2.05))]
    yield [Indicate(cases[1][2], color=INK, scale_factor=1.15), Indicate(cases[2][2], color=INK, scale_factor=1.15),
           FadeIn(at(mix("but they are as far apart as a whole", mt(r"\hbar", size=38), "would put them", size=26), 0, -2.7))]
    yield [FadeIn(at(T("the rule for a spinning charge can't produce both", 28, RED, True), 0, -3.4))]


@slide("In nineteen twenty-seven, Wolfgang Pauli wrote an equation", "Pauli's equation")
def pauli(s):
    c = at(card("an equation for a\nslow electron with spin", 5.0, 1.6, INK, 26), 2.6, 0.5)
    yield [FadeIn(at(T("1927: Wolfgang Pauli", 30, INK, True), 0, 2.2)), FadeIn(c)]
    a = at(card("the spin", 3.4, 0.9, PURPLE, 26), -4.4, 1.2)
    b = at(card("the factor of two", 3.4, 0.9, INK, 26), -4.4, -0.2)
    yield [FadeIn(a), GrowArrow(varrow(P(-2.6, 1.2), P(0.0, 0.8))), FadeIn(at(lab("an assumption", 22), -1.4, 1.45))]
    yield [FadeIn(b), GrowArrow(varrow(P(-2.6, -0.2), P(0.0, 0.2))), FadeIn(at(lab("an assumption", 22), -1.4, -0.55))]
    yield [FadeIn(at(T("nobody could say where either came from", 28, INK, True), 0, -2.3))]


@slide("So that's the puzzle, and it has two parts.", "The puzzle, in two parts")
def puzzle(s):
    ca, cb = at(card(None, 6.6, 1.5, PURPLE), -3.7, 0.9), at(card(None, 6.6, 1.5, INK), 3.7, 0.9)
    yield [FadeIn(ca), FadeIn(cb)]
    yield [FadeIn(at(mix("why a spin of", mt(HB2, size=44, color=PURPLE), "?", size=28), -3.7, 0.9))]
    yield [FadeIn(at(VGroup(lab("why is its magnet twice as strong", 24, INK), lab("as a spinning charge's?", 24, INK)).arrange(DOWN, buff=0.1), 3.7, 0.9))]
    d = at(card("the Dirac equation answers both", 6.4, 1.1, INK, 28, fill=PALE), 0, -1.9)
    yield [FadeIn(d), GrowArrow(varrow(P(-1.5, -1.25), P(-3.2, 0.05))), GrowArrow(varrow(P(1.5, -1.25), P(3.2, 0.05)))]


# ================================================================== four wave functions and one question
deck.part("Four wave functions and one question")


def ab(tex, size=40, color=INK):
    """A formula in which every alpha and beta is PURPLE."""
    m = MathTex(tex, substrings_to_isolate=[r"\alpha", r"\beta"], color=color, font_size=size)
    m.set_color_by_tex(r"\alpha", PURPLE)
    m.set_color_by_tex(r"\beta", PURPLE)
    return m


def magnet(x, y, vertical=True, s=0.5):
    """Two pole pieces with a gap between them, standing for chapter 2a's magnet."""
    a = Rectangle(width=2.2 * s, height=0.7 * s, stroke_color=MUTED, stroke_width=3, fill_color=LINE, fill_opacity=1)
    b = a.copy()
    g = VGroup(a.shift(UP * 0.75 * s), b.shift(DOWN * 0.75 * s), varrow(P(0, -0.3 * s), P(0, 0.3 * s), MUTED, 3, 0.12))
    if not vertical:
        g.rotate(-PI / 2)
    return g.move_to(P(x, y))


def magnet_fb(x, y, s=0.5):
    """A magnet whose poles are in front of and behind the beam: one pole piece drawn behind the other."""
    a = Rectangle(width=1.5 * s, height=1.5 * s, stroke_color=MUTED, stroke_width=3, fill_color=LINE, fill_opacity=1)
    back, front = a.copy().shift(P(0.5 * s, 0.5 * s)), a.copy().shift(P(-0.5 * s, -0.5 * s))
    return VGroup(back, front, varrow(P(-0.3 * s, -0.3 * s), P(0.45 * s, 0.45 * s), MUTED, 3, 0.12).set_z_index(2)).move_to(P(x, y))


def phasor(c, ang, r=0.5, color=BLUE, width=5):
    """A complex number drawn as an arrow from c, in a circle of radius r."""
    c = P(*c)
    return VGroup(Circle(radius=r, color=LINE, stroke_width=2).move_to(c),
                  Arrow(c, c + r * uvec(ang), buff=0, color=color, stroke_width=width, tip_length=0.14,
                        max_tip_length_to_length_ratio=0.45, max_stroke_width_to_length_ratio=30))


def xaxis(x0, x1, y, text="position", color=MUTED):
    ax = Arrow(P(x0, y), P(x1, y), buff=0, color=color, stroke_width=3, tip_length=0.16, max_tip_length_to_length_ratio=0.2)
    return VGroup(ax, lab(text, 22, color).next_to(ax, DOWN, buff=0.12).align_to(ax, RIGHT))


@slide("Four wave functions and one question.", "The column of four")
def col1(s):
    yield [FadeIn(at(T("let's bring the equation back", 30, INK, True), 0, 2.2))]
    c = at(col4m(64, 0.95, False), -3.6, -0.4)
    yield [FadeIn(c), FadeIn(left_at(words("the last chapter: in space, the state is a column of four wave functions", 30, 26), -1.6, -0.4))]
    yield hold()


@slide("The energy rule needs four matrices.", "Four matrices")
def four1(s):
    r = at(lin3(56), 0, 1.2)
    yield [FadeIn(r), FadeIn(at(lab("the energy rule", 24), -5.6, 2.3)), FadeIn(at(pill("four matrices", PURPLE, 26), 4.6, 2.3))]
    yield [FadeIn(note(VGroup(*r[1:7]), "one for each part of the momentum", PURPLE, chars=44)),
           FadeIn(note(VGroup(r[7], r[8]), "one for the mass", PURPLE, chars=8))]
    yield [GrowArrow(varrow(P(0, -0.7), P(0, -1.9))), FadeIn(left_at(lab("through the last chapter's recipe", 24), 0.3, -1.3)),
           FadeIn(at(T("the Dirac equation", 30, INK, True), 0, -2.5))]





@slide("It's on screen.", "The Dirac equation")
def dirac2(s):
    eq, h = at(dirac3(56), -3.6, 1.9), at(ham(52), 0, 0.1)
    yield [FadeIn(eq), FadeIn(h)]
    yield [Create(under(eq[2])), Create(under(h[0][:-1])), FadeIn(left_at(T("the energy operator", 28, INK, True), -1.2, 2.1)),
           FadeIn(note(VGroup(*h[1:11]), "the momentum terms", INK)), FadeIn(note(VGroup(h[12], h[13]), "the mass term", INK))]
    yield [FadeIn(left_at(lab("it plays the same part as in chapter 2b", 24), -1.2, 1.55))]
    yield hold()
    yield [FadeIn(at(mix(mt(r"\hat p_x = -i\hbar\,\frac{\partial}{\partial x}", size=48), "each part of the momentum: a slope along one direction", size=24), 0, -2.6))]
    yield hold()


NODE_X = (-4.8, -1.6, 1.6, 4.8)
NODE_NAMES = (r"\alpha_x", r"\alpha_y", r"\alpha_z", r"\beta")


def node(k, y=0.7):
    return VGroup(Circle(radius=0.75, color=PURPLE, stroke_width=3.5, fill_color=WHITE, fill_opacity=1).move_to(P(NODE_X[k], y)),
                  at(purple(NODE_NAMES[k], 56), NODE_X[k], y))


@slide("The last chapter said four such matrices exist.", "Four matrices, not yet shown")
def four2(s):
    yield [LaggedStart(*[FadeIn(node(k)) for k in range(4)], lag_ratio=0.15), FadeIn(at(lab("the last chapter said four such matrices exist", 26, INK), 0, 2.3))]
    yield [FadeIn(VGroup(*[at(T("?", 40, MUTED, True), x, -0.7) for x in NODE_X])), FadeIn(at(lab("it didn't show them", 26, INK), 0, -1.6))]
    yield [FadeIn(at(T("this chapter works with them, so let's look", 28, INK, True), 0, -2.6))]


@slide("Each one is a table of four rows and four columns.", "Tables built from blocks")
def blocks1(s):
    g = grid(4, 4, 0.8).move_to(P(-3.6, -0.2))
    yield [FadeIn(g), FadeIn(left_at(words("each one is a table of four rows and four columns", 28, 26), 0.2, 1.0))]
    yield [*[g[4 * r + c].animate.shift(P(0.22 * (1 if c > 1 else -1), 0.22 * (-1 if r > 1 else 1))) for r in range(4) for c in range(4)],
           FadeIn(left_at(words("built from smaller blocks of two rows and two columns", 28, 26, INK, bold=True), 0.2, -1.2))]


SPIN_X = (-4.8, 0.0, 4.8)
SPIN_NAMES = (r"\hat S", r"\hat Y", r"\hat Z")
SPIN_ROWS = (S_ROWS, Y_ROWS, Z_ROWS)
SPIN_WORDS = ("a sideways magnet", "a front-to-back magnet", "an up-and-down magnet")


def spin_icon(k, y):
    return (magnet(SPIN_X[0], y, False), magnet_fb(SPIN_X[1], y), magnet(SPIN_X[2], y))[k]


def spin_card(k):
    return VGroup(at(purple(SPIN_NAMES[k], 84), SPIN_X[k], 1.2), spin_icon(k, -0.4), at(lab(SPIN_WORDS[k], 24, INK), SPIN_X[k], -1.5))


@slide("The blocks are three spin matrices, and we've met two of them.", "Three spin matrices")
def spins1(s):
    yield [FadeIn(at(lab("the blocks are three spin matrices", 26, INK), 0, 2.4))]
    yield [FadeIn(spin_card(0)), FadeIn(spin_card(2)), FadeIn(at(lab("met in chapter 2b", 22), SPIN_X[0], -2.1)), FadeIn(at(lab("met in chapter 2b", 22), SPIN_X[2], -2.1))]
    yield [FadeIn(spin_card(1)), FadeIn(at(pill("new", PURPLE, 24), SPIN_X[1], -2.2))]


def spin_mat(k, size=48):
    return named(SPIN_NAMES[k], mat(SPIN_ROWS[k], size, PURPLE, 0.95, 0.8), size + 8, PURPLE)


@slide("All three are on screen.", "Three spin matrices")
def spins2(s):
    ms = [at(spin_mat(k), SPIN_X[k], 0.9) for k in range(3)]
    yield [*[FadeIn(m) for m in ms], *[FadeIn(at(lab(SPIN_WORDS[k], 24, INK), SPIN_X[k], -0.5)) for k in range(3)],
           FadeIn(at(pill("new", PURPLE, 24), SPIN_X[1], 2.3))]
    e = ms[1][1].get_entries()
    yield [Create(frame(e[1], PURPLE, 0.1)), Create(frame(e[2], PURPLE, 0.1)),
           FadeIn(at(mix("the new one has", mt("i", size=40, color=PURPLE), "and", mt("-i", size=40, color=PURPLE), "for entries", size=26), 0, -1.6))]
    yield [FadeIn(at(mix("its measurement still gives", mt("+1", size=40), "or", mt("-1", size=40), ", like the other two", size=26), 0, -2.6))]


BIG_X = (-5.4, -1.8, 1.8, 5.4)
BIG_ROWS = ([["0", r"\hat S"], [r"\hat S", "0"]], [["0", r"\hat Y"], [r"\hat Y", "0"]], [["0", r"\hat Z"], [r"\hat Z", "0"]], [["1", "0"], ["0", "-1"]])


def big(k, size=40):
    return named(NODE_NAMES[k], mat(BIG_ROWS[k], size, PURPLE, 0.85, 0.75), size + 4, PURPLE)


def big4(y=1.5, size=40):
    return [at(big(k, size), BIG_X[k], y) for k in range(4)]


def big_goes(y=0.35):
    return VGroup(*[at(mix("with", mt(tex, size=38), size=24, color=MUTED), BIG_X[k], y) for k, tex in enumerate(("p_x", "p_y", "p_z"))])


@slide("The four big matrices are on screen now.", "The four matrices")
def big1(s):
    ms = big4()
    yield [LaggedStart(*[FadeIn(m) for m in ms], lag_ratio=0.15)]
    yield [FadeIn(big_goes()), FadeIn(at(lab("three of them go with the three parts of the momentum", 26, INK), -1.8, -0.5))]
    yield [*[Create(frame(m[1].get_entries()[j], PURPLE, 0.08, 2.5)) for m in ms[:3] for j in (1, 2)],
           FadeIn(at(lab("each has a spin matrix in two of its corners, and zeros in the other two", 26, INK, True), 0, -1.7))]


def beta_full(size=34, v=0.55):
    rows = [["1", "0", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "-1", "0"], ["0", "0", "0", "-1"]]
    return mat(rows, size, PURPLE, 0.75, v)


@slide("The fourth goes with the mass.", "The mass matrix")
def big2(s):
    ms = big4()
    s.add(*ms, big_goes())
    yield [Create(frame(ms[3], PURPLE, 0.15)), FadeIn(at(lab("with the mass", 24, INK, True), BIG_X[3], 0.35))]
    full = at(named(r"\beta", beta_full(), 44, PURPLE), -2.6, -1.8)
    e = full[1].get_entries()
    yield [FadeIn(full), FadeIn(at(lab("written out in full", 22), -5.9, -1.3)),
           Create(frame(VGroup(e[0], e[5]), BLUE, 0.1, 2.5)), Create(frame(VGroup(e[10], e[15]), LOW, 0.1, 2.5)),
           FadeIn(left_at(lab("ones in its top half", 26, BLUE), 0.6, -1.3)), FadeIn(left_at(lab("minus ones in its bottom half", 26, LOW), 0.6, -2.3))]


@slide("They meet the last chapter's conditions.", "The conditions")
def big3(s):
    s.add(*big4(1.7))
    c1 = at(ab(r"\alpha_x^2 = 1 \qquad \alpha_y^2 = 1 \qquad \alpha_z^2 = 1 \qquad \beta^2 = 1", 44), 1.2, -0.5)
    yield [FadeIn(at(lab("the last chapter's conditions", 24), 0, 0.4)), FadeIn(c1), FadeIn(right_at(lab("each squares to 1", 24, INK, True), c1.get_left()[0] - 0.4, -0.5)),
           Create(tick(c1))]
    c2 = at(ab(r"\alpha_x\alpha_y + \alpha_y\alpha_x = 0", 48), 1.2, -2.0)
    yield [FadeIn(c2), FadeIn(right_at(lab("every pair anticommutes", 24, INK, True), c2.get_left()[0] - 0.4, -2.0)), Create(tick(c2)),
           FadeIn(left_at(lab("for example", 22), c2.get_right()[0] + 0.9, -2.0))]


def pair_brace(c, upper, text=None, side=RIGHT):
    """A brace beside one pair of a column's entries, set clear of the column's bracket."""
    e = c.get_entries()
    grp = VGroup(e[0], e[1]) if upper else VGroup(e[2], e[3])
    color = BLUE if upper else LOW
    b = Brace(grp, side, color=color, buff=0)
    if side[0] > 0:
        b.set_x(c.get_right()[0] + 0.16 + b.width / 2)
    else:
        b.set_x(c.get_left()[0] - 0.16 - b.width / 2)
    g = VGroup(b)
    if text is not False:
        g.add(T(text or ("the upper pair" if upper else "the lower pair"), 28, color, True).next_to(b, side, buff=0.2))
    return g


@slide("Here's the useful way to think of the column.", "Two pairs")
def pairs1(s):
    c = at(col4m(72, 1.0), -3.6, -0.3)
    yield [FadeIn(c), FadeIn(at(lab("a useful way to think of the column", 26, INK), 0, 2.4))]
    yield [FadeIn(at(T("it's two pairs", 34, INK, True), 3.6, -0.3))]
    yield [FadeIn(pair_brace(c, True)), FadeIn(pair_brace(c, False))]


PB_Y = (0.75, -1.25)


def pair_in(x, upper):
    y = PB_Y[0 if upper else 1]
    color = BLUE if upper else LOW
    box = RoundedRectangle(width=1.6, height=1.7, corner_radius=0.12, stroke_color=color, stroke_width=3, fill_color=color, fill_opacity=0.12).move_to(P(x, y))
    names = (r"\psi_1", r"\psi_2") if upper else (r"\psi_3", r"\psi_4")
    return VGroup(box, at(mt(names[0], size=40, color=color), x, y + 0.38), at(mt(names[1], size=40, color=color), x, y - 0.38))


def pair_out(x, slot_upper, from_upper):
    """What lands in a slot of the result: a pair's box, colored by the pair it came from."""
    y = PB_Y[0 if slot_upper else 1]
    color = BLUE if from_upper else LOW
    box = RoundedRectangle(width=1.6, height=1.7, corner_radius=0.12, stroke_color=color, stroke_width=3, fill_color=color, fill_opacity=0.12).move_to(P(x, y))
    text = VGroup(lab("from the", 22, color), lab("upper pair" if from_upper else "lower pair", 22, color)).arrange(DOWN, buff=0.08).move_to(box)
    return VGroup(box, text)


def pair_panel(x0, x1, swap):
    ins = [pair_in(x0, True), pair_in(x0, False)]
    outs = [pair_out(x1, True, not swap), pair_out(x1, False, swap)]   # the upper slot, then the lower slot
    arrows = []
    for upper in (True, False):
        ya = PB_Y[0 if upper else 1]
        yb = PB_Y[(0 if upper else 1) ^ (1 if swap else 0)]
        arrows.append(varrow(P(x0 + 0.95, ya), P(x1 - 0.95, yb), BLUE if upper else LOW))
    moves = [(ins[0], outs[1 if swap else 0]), (ins[1], outs[0 if swap else 1])]
    return ins, outs, arrows, moves


@slide("The mass matrix keeps each pair to itself.", "Keeping the pairs, swapping the pairs")
def pairs2(s):
    ins, outs, arrows, moves = pair_panel(-6.0, -2.4, False)
    yield [FadeIn(at(mix(mt(r"\beta", size=52, color=PURPLE), "keeps each pair to itself", size=26), -4.2, 2.3)), *[FadeIn(i) for i in ins],
           *[GrowArrow(a) for a in arrows], *[TransformFromCopy(a[0], b[0]) for a, b in moves], *[FadeIn(b[1]) for _, b in moves]]
    ins2, outs2, arrows2, moves2 = pair_panel(1.4, 5.0, True)
    yield [FadeIn(at(mix("each", mt(r"\alpha", size=52, color=PURPLE), "does the opposite", size=26), 3.2, 2.3)), *[FadeIn(i) for i in ins2]]
    yield [*[GrowArrow(a) for a in arrows2], *[TransformFromCopy(a[0], b[0]) for a, b in moves2], *[FadeIn(b[1]) for _, b in moves2],
           FadeIn(at(lab("the upper pair goes to the lower, and the lower to the upper", 24, INK), 0, -2.9))]


WAVE_X = np.arange(-6.0, 6.01, 1.5)


@slide("Now take a particle at rest.", "A particle at rest")
def rest1(s):
    t = clock(s)
    yield [FadeIn(electron(-5.6, 2.0, BLUE, 0.2)), FadeIn(left_at(T("a particle at rest", 30, INK, True), -5.1, 2.0))]
    yield [FadeIn(left_at(lab("its momentum is zero", 28, INK), 0.6, 2.0))]
    s.add(always_redraw(lambda: VGroup(*[phasor((x, -0.2), -1.6 * t.get_value(), 0.55) for x in WAVE_X])))  # added, not faded in
    yield [FadeIn(xaxis(-6.9, 7.0, -1.1)), FadeIn(at(T("its wave function is the same at every point", 28, INK, True), 0, -2.5))]


@slide("So every slope is zero, and the momentum terms drop out.", "Only the mass term is left")
def rest2(s):
    h = at(ham(56), 0, 1.4)
    s.add(h)
    gone = VGroup(*h[1:11])
    yield [Create(Line(gone.get_corner(DL) + P(-0.1, -0.1), gone.get_corner(UR) + P(0.1, 0.1), color=RED, stroke_width=6)),
           FadeIn(at(lab("every slope is zero, so the momentum terms drop out", 24, RED), gone.get_x(), 0.3))]
    left = at(paint(mt(r"\hat H =", r"\beta", r"\,mc^2", size=84), PURPLE, 1), 0, -1.6)
    yield [Create(frame(VGroup(h[12], h[13]), INK, 0.12, 2.5)), FadeIn(left), FadeIn(at(lab("only the mass term is left", 26, INK, True), 0, -2.8))]


def rest_result(size=40, v=0.62):
    m = mat([[r"+mc^2\,\psi_1"], [r"+mc^2\,\psi_2"], [r"-mc^2\,\psi_3"], [r"-mc^2\,\psi_4"]], size, v=v)
    for k, e in enumerate(m.get_entries()):
        e.set_color(BLUE if k < 2 else LOW)
    return m


def rest_eq(v=0.72):
    """H psi = mc² (the diagonal 1, 1, -1, -1) (the column) = (the result). Parts: 0 left side, 1 matrix, 2 column, 3 =, 4 result."""
    return VGroup(mt(r"\hat H\psi = mc^2", size=44), beta_full(36, v), col4m(40, v), mt("=", size=44), rest_result(40, v)).arrange(RIGHT, buff=0.22)


@slide("The result is on screen.", "At rest")
def rest3(s):
    m = at(rest_eq().scale(1.1), -1.05, 0.5)
    yield [FadeIn(m)]
    yield [FadeIn(pair_brace(m[4], True, False)), FadeIn(left_at(mt("+mc^2", size=44, color=BLUE), m[4].get_right()[0] + 0.6, m[4].get_entries()[0].get_y() - 0.4)),
           FadeIn(at(lab("the upper pair has the rest energy", 26, BLUE, True), 0, -2.3))]
    yield [FadeIn(pair_brace(m[4], False, False)), FadeIn(left_at(mt("-mc^2", size=44, color=LOW), m[4].get_right()[0] + 0.6, m[4].get_entries()[2].get_y() - 0.4)),
           FadeIn(at(lab("the lower pair has minus that", 26, LOW, True), 0, -3.0))]


@slide("On a line, the last chapter found one wave function with each sign", "Each sign appears twice")
def rest4(s):
    two = mat([[r"+mc^2\,\psi_1"], [r"-mc^2\,\psi_2"]], 52, v=0.9)
    two.get_entries()[0].set_color(BLUE)
    two.get_entries()[1].set_color(LOW)
    yield [FadeIn(at(two, -3.8, 0.2)), FadeIn(at(T("on a line", 28, INK, True), -3.8, 2.2)), FadeIn(at(lab("one wave function with each sign", 24, INK), -3.8, -1.6))]
    yield [FadeIn(at(rest_result(52, 0.9), 3.8, 0.2)), FadeIn(at(T("in space", 28, INK, True), 3.8, 2.3)), FadeIn(at(T("each sign appears twice", 26, INK, True), 3.8, -2.6))]


@slide("And that's the question.", "The question")
def question(s):
    xs = (-0.8, 3.4)
    heads = VGroup(*[at(mt(r"\psi_%d" % (k + 1), size=72, color=BLUE), x, 1.6) for k, x in enumerate(xs)])
    yield [FadeIn(heads), FadeIn(at(lab("the first two wave functions", 24, INK), 1.3, 2.5))]
    rows = VGroup(right_at(lab("energy", 26, INK), -3.0, 0.3), *[at(mt("+mc^2", size=48, color=BLUE), x, 0.3) for x in xs],
                  right_at(lab("momentum", 26, INK), -3.0, -0.8), *[at(lab("zero", 28, INK), x, -0.8) for x in xs],
                  left_at(lab("the same", 24), 5.0, 0.3), left_at(lab("the same", 24), 5.0, -0.8))
    yield [FadeIn(rows)]
    yield [FadeIn(at(T("so measuring energy and momentum can't tell them apart", 28, INK, True), 0, -2.4))]


@slide("We've met two states like that before.", "Like spin up and spin down")
def like(s):
    a, b = espin(-6.3, 1.9, True, 0.9, 0.13), espin(-6.3, 0.5, False, 0.9, 0.13)
    yield [FadeIn(a), FadeIn(b), FadeIn(left_at(lab("chapter 2a: spin up and spin down", 24, INK), -5.7, 2.45))]
    d1, d2 = Dot(P(-5.6, 1.9), radius=0.1, color=INK), Dot(P(-5.6, 0.5), radius=0.1, color=INK)
    scr = Line(P(-0.8, -0.1), P(-0.8, 2.3), color=MUTED, stroke_width=6)
    yield [FadeIn(magnet(-3.4, 1.2)), FadeIn(scr), FadeIn(d1), FadeIn(d2), d1.animate.move_to(P(-0.85, 1.95)), d2.animate.move_to(P(-0.85, 0.3)),
           FadeIn(left_at(words("alike, until a vertical magnet sent them to different spots", 28, 26), -0.2, 1.2))]
    q = VGroup(DashedVMobject(RoundedRectangle(width=1.6, height=1.3, corner_radius=0.12, color=MUTED, stroke_width=3), num_dashes=30).move_to(P(-3.4, -1.7)),
               at(T("?", 40, MUTED, True), -3.4, -1.7))
    yield [FadeIn(at(mt(r"\psi_1", size=48, color=BLUE), -6.3, -1.3)), FadeIn(at(mt(r"\psi_2", size=48, color=BLUE), -6.3, -2.1)), FadeIn(q),
           GrowArrow(varrow(P(-5.6, -1.7), P(-4.4, -1.7))),
           FadeIn(left_at(words("we need a measurement that does the same for these two", 30, 26, INK, bold=True), -0.2, -1.7))]
    yield [FadeIn(caption("The next two sections find it.", -3.5, INK, 26))]


# ================================================================== angular momentum that isn't kept
deck.part("Angular momentum that isn't kept")


def glider(t, y=1.2, color=INK, arrow=True):
    """A free particle: a dot that keeps moving in a straight line."""
    def draw():
        x = -6.0 + (1.6 * t.get_value()) % 11.0
        g = VGroup(Dot(P(x, y), radius=0.16, color=color))
        if arrow:
            g.add(varrow(P(x + 0.25, y), P(x + 1.3, y), INK, 5, 0.16))
        return g
    return always_redraw(draw)


@slide("Angular momentum that isn't kept.", "A check")
def check1(s):
    t = clock(s)
    s.add(Line(P(-6.6, 1.2), P(6.6, 1.2), color=LINE, stroke_width=3), glider(t))
    yield [FadeIn(at(lab("a free particle", 24), -5.4, 1.9))]
    yield [FadeIn(at(lab("the missing quantity turns up in a check", 28, INK), 0, -0.4))]
    yield [FadeIn(at(card("a free particle's angular momentum\nshould never change", 7.6, 1.6, INK, 28), 0, -2.0))]


@slide("We'll run that check on the Dirac equation.", "The check fails")
def check2(s):
    a = at(card("the check", 3.2, 1.1, INK, 28), -4.8, 1.4)
    b = at(card("the Dirac equation", 4.4, 1.1, INK, 28), 0.6, 1.4)
    yield [FadeIn(a), GrowArrow(varrow(P(-3.1, 1.4), P(-1.7, 1.4))), FadeIn(b)]
    f = left_at(T("it fails", 32, RED, True), 3.4, 1.4)
    yield [FadeIn(f), Create(xmark(f))]
    c = at(card("the term that repairs it", 5.0, 1.1, INK, 28, fill=PALE), 0.6, -1.3)
    yield [GrowArrow(varrow(P(0.6, 0.75), P(0.6, -0.65))), FadeIn(c), FadeIn(at(lab("is the quantity we're after", 26, INK, True), 0.6, -2.4))]


def avg(size=64):
    return mt(*AVG, size=size)


@slide("First, we need to know what stays constant.", "What stays constant")
def avg1(s):
    yield [FadeIn(at(T("what stays constant?", 34, INK, True), 0, 1.2))]
    yield [FadeIn(at(lab("chapter 2b gave a rule for how an average changes in time", 28, INK), 0, -0.4))]


@slide("It's on screen.", "How an average changes")
def avg2(s):
    f = at(avg(56), -3.2, 1.6)
    yield [FadeIn(f)]
    yield [Create(frame(f[4], INK, 0.12)), FadeIn(left_at(T("a commutator", 30, INK, True), 0.6, 1.6))]
    d = at(mt(r"[\hat A,\ \hat H]", "=", r"\hat A\hat H", "-", r"\hat H\hat A", size=64), 0, -0.6)
    yield [FadeIn(d), FadeIn(note(d[2], "one order", INK)), FadeIn(note(d[4], "the other order", INK, UP))]
    yield [FadeIn(at(mix(mt(r"\hat A", size=44), "the quantity's own operator", size=24), -3.6, -2.9)),
           FadeIn(at(mix(mt(r"\hat H", size=44), "the energy operator", size=24), 3.4, -2.9))]


@slide("So suppose the two orders agree.", "Kept")
def kept(s):
    s.add(at(avg(44), 0, 2.05))
    a = at(mt(r"\hat A\hat H = \hat H\hat A", size=52), -4.2, 0.6)
    yield [FadeIn(a), FadeIn(at(lab("suppose the two orders agree", 24, INK), -4.2, -0.15))]
    b = at(mt(r"[\hat A,\ \hat H] = 0", size=52), 0.3, 0.6)
    c = at(mt(r"\frac{d\langle A\rangle}{dt} = 0", size=52), 4.8, 0.6)
    yield [GrowArrow(varrow(P(-2.2, 0.6), P(-1.5, 0.6))), FadeIn(b), GrowArrow(varrow(P(2.2, 0.6), P(2.9, 0.6))), FadeIn(c),
           FadeIn(at(lab("the quantity never changes, whatever the state", 24, INK), 2.6, -0.5))]
    k = at(T("kept", 56, INK, True), 1.6, -1.75)
    yield [FadeIn(k), Create(frame(k, INK, 0.25, 3)), FadeIn(right_at(lab("we'll say a quantity like that is", 26, INK), 0.2, -1.75))]
    m = at(lab("a free particle's momentum is kept, for example", 26, INK), -0.3, -3.1)
    yield [FadeIn(m), Create(tick(m))]


@slide("Next, angular momentum.", "Angular momentum of a pendulum")
def pend(s):
    t = clock(s)
    s.add(Line(P(-5.4, 2.4), P(-2.6, 2.4), color=MUTED, stroke_width=5), pendulum(t, P(-4.0, 2.4), 3.6, 0.4))
    yield [FadeIn(left_at(lab("chapter 1's pendulum", 24), -0.6, 2.0))]
    yield [FadeIn(left_at(T("angular momentum", 30, INK, True), -0.6, 0.7)), FadeIn(left_at(lab("= the bob's momentum", 28, INK), -0.6, -0.2)),
           FadeIn(left_at(lab("× its distance from the pivot", 28, INK), -0.6, -1.0))]


OC = (-4.0, -0.4)


def orbit(t):
    def draw():
        a = 1.2 * t.get_value()
        p = P(OC[0] + 2.2 * np.cos(a), OC[1] + 0.75 * np.sin(a))
        return VGroup(Line(P(*OC), p, color=INK, stroke_width=3), Dot(p, radius=0.16, color=INK))
    return always_redraw(draw)


@slide("A particle anywhere in space has the same thing about the vertical axis.", "About the vertical axis")
def about(s):
    t = clock(s)
    axis = VGroup(Line(P(OC[0], -2.9), P(OC[0], 2.3), color=MUTED, stroke_width=4), at(lab("the vertical axis", 22), OC[0], 2.55))
    path = Ellipse(width=4.4, height=1.5, color=LINE, stroke_width=3).move_to(P(*OC))
    yield [FadeIn(axis), FadeIn(path), FadeIn(left_at(words("a particle anywhere in space has the same thing about the vertical axis", 30, 26), -0.6, 1.5))]
    s.add(orbit(t))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(left_at(T("angular momentum", 30, INK, True), -0.6, -0.3)), FadeIn(left_at(lab("= the momentum that carries it round the axis", 26, INK), -0.6, -1.1)),
           FadeIn(left_at(lab("× its distance from the axis", 26, INK), -0.6, -1.8))]


LZ_C = (-4.0, 4.0)
LZ_Y = 0.25


def lz_base(k):
    o = P(LZ_C[k], LZ_Y)
    return VGroup(Arrow(o + P(-2.3, 0), o + P(2.5, 0), buff=0, color=LINE, stroke_width=3, tip_length=0.16, max_tip_length_to_length_ratio=0.1),
                  Arrow(o + P(0, -1.7), o + P(0, 1.8), buff=0, color=LINE, stroke_width=3, tip_length=0.16, max_tip_length_to_length_ratio=0.1),
                  mt("x", size=34, color=MUTED).move_to(o + P(2.75, 0)), mt("y", size=34, color=MUTED).move_to(o + P(-0.3, 1.75)),
                  Dot(o, radius=0.11, color=INK), lab("axis", 22).move_to(o + P(-0.6, -0.35)))


def lz_part(k):
    """One way to go round: [arm and particle, the momentum, the arc of its turning, the words]."""
    o = P(LZ_C[k], LZ_Y)
    color = (PY, PX)[k]
    pos, mom = ((P(1.7, 0), P(0, 1.3)), (P(0, 1.3), P(1.4, 0)))[k]
    p = o + pos
    arm = VGroup(Line(o, p, color=INK, stroke_width=5), Dot(p, radius=0.15, color=color))
    if k == 0:
        arm.add(mt("x", size=40).move_to(o + P(0.85, -0.33)))
        name = mt("p_y", size=40, color=color).move_to(p + P(0.5, 0.75))
        arc = Arc(radius=1.0, start_angle=0.35, angle=1.5, arc_center=o, color=color, stroke_width=4)
    else:
        arm.add(mt("y", size=40).move_to(o + P(-0.33, 0.65)))
        name = mt("p_x", size=40, color=color).move_to(p + P(0.8, 0.4))
        arc = Arc(radius=1.0, start_angle=PI / 2 - 0.35, angle=-1.5, arc_center=o, color=color, stroke_width=4)
    arc.add_tip(tip_length=0.2, tip_width=0.2)
    arrow_ = VGroup(varrow(p, p + mom, color, 7, 0.24), name)
    word = at(lab(("goes round anticlockwise", "goes round clockwise")[k], 24, color), LZ_C[k], -1.95)
    return [arm, arrow_, arc, word]


def lz_counts(k):
    return at(mix("counts as", mt((r"+\,x\,p_y", r"-\,y\,p_x")[k], size=44, color=(PY, PX)[k]), size=26, color=(PY, PX)[k]), LZ_C[k], 2.4)


@slide("Look down from above, as on screen.", "Seen from above")
def above1(s):
    yield [FadeIn(lz_base(0)), FadeIn(lz_base(1)), FadeIn(at(lab("seen from above, with the vertical axis at the centre", 24), 0, -2.5))]
    yield [FadeIn(at(T("two ways to go round", 30, INK, True), 0, -3.25))]


@slide("A particle out along x, moving along y, goes round anticlockwise.", "Anticlockwise")
def above2(s):
    s.add(lz_base(0), lz_base(1))
    arm, mom, arc, word = lz_part(0)
    yield [FadeIn(arm), GrowArrow(mom[0]), FadeIn(mom[1]), Create(arc), FadeIn(word)]
    yield [FadeIn(lz_counts(0))]


@slide("A particle out along y, moving along x, goes round clockwise.", "Clockwise")
def above3(s):
    s.add(lz_base(0), lz_base(1), *lz_part(0), lz_counts(0))
    arm, mom, arc, word = lz_part(1)
    yield [FadeIn(arm), GrowArrow(mom[0]), FadeIn(mom[1]), Create(arc), FadeIn(word)]
    yield [FadeIn(lz_counts(1))]


@slide("Add the two parts, and we have the angular momentum about the vertical.", "Angular momentum about the vertical")
def above4(s):
    c0, c1 = lz_counts(0), lz_counts(1)
    s.add(lz_base(0), lz_base(1), *lz_part(0), *lz_part(1), c0, c1)
    f = at(lz(60), 0, -2.75)
    yield [TransformFromCopy(c0[1], f[2]), TransformFromCopy(c1[1], VGroup(f[3], f[4])), FadeIn(VGroup(f[0], f[1]))]
    yield [FadeIn(caption("It ought to be kept.", -3.65, INK, 28))]


@slide("Nothing pushes a free particle, so its momentum stays the same.", "A free particle")
def free(s):
    t = clock(s)
    s.add(Line(P(-6.6, 1.5), P(6.6, 1.5), color=LINE, stroke_width=3), glider(t, 1.5))
    yield [FadeIn(at(lab("nothing pushes a free particle, so its momentum stays the same", 26, INK), 0, 0.2))]
    yield [FadeIn(at(lab("nothing twists it either", 26, INK), 0, -0.8))]
    m = at(T("so its angular momentum should stay the same too", 28, INK, True), 0, -2.1)
    yield [FadeIn(m)]


SK = (-3.8, -0.4)


def skater(ang, r):
    """A skater seen from above: the body, and two arms that reach out to a distance r."""
    def draw():
        c = P(*SK)
        u = uvec(ang.get_value())
        g = VGroup(Circle(radius=2.1, color=LINE, stroke_width=2).move_to(c))
        for sgn in (1, -1):
            hand = c + sgn * r.get_value() * u
            g.add(Line(c, hand, color=INK, stroke_width=9), Dot(hand, radius=0.16, color=INK))
        g.add(Circle(radius=0.5, color=INK, stroke_width=3, fill_color=PALE, fill_opacity=1).move_to(c))
        return g
    return always_redraw(draw)


@slide("A spinning skater shows this.", "A spinning skater")
def skate(s):
    r, ang = ValueTracker(2.0), ValueTracker(0.0)
    ang.add_updater(lambda m, dt: m.increment_value(1.3 * (2.0 / r.get_value()) ** 2 * dt))
    s.add(r, ang, skater(ang, r))
    yield [FadeIn(left_at(T("a spinning skater, seen from above", 28, INK, True), 0.0, 1.6))]
    yield [FadeIn(left_at(words("with nothing to twist them, their angular momentum can't change", 32, 26), 0.0, 0.2))]
    yield [r.animate.set_value(0.9), FadeIn(left_at(words("so when they pull their arms in, they spin faster", 32, 26, INK, bold=True), 0.0, -1.6))]


@slide("Now the check.", "The check")
def check3(s):
    a = at(lz(52), 0, 2.0)
    yield [FadeIn(a)]
    b = at(lz(60, hats=True), 0, 0.6)
    yield [TransformFromCopy(a, b), FadeIn(left_at(words("positions and momenta become operators, as in chapter 2b", 22, 22, MUTED), 3.4, 0.6))]
    q = at(mt(r"[\hat L_z,\ \hat H] = \ ?", size=72), 0, -1.2)
    yield [FadeIn(q), FadeIn(at(lab("its commutator with Dirac's energy operator", 24, INK), 0, -2.2)), FadeIn(at(ham(44), 0, -3.0))]


@slide("The result is on screen, and it isn't zero.", "The leftover")
def left1(s):
    m = at(leftover(64), 0, 0.6)
    z = at(T("it isn't zero", 30, RED, True), 0, 2.2)
    yield [FadeIn(m), FadeIn(z), Create(xmark(z))]
    yield [FadeIn(note(VGroup(*m[1:]), "the leftover", INK, size=32, buff=0.25))]


def left_top(y=2.15, size=40):
    m = at(leftover(size), 0.6, y)
    return VGroup(m, right_at(lab("the leftover", 24, INK, True), m.get_left()[0] - 0.4, y))


@slide("So take a free electron, with nothing twisting it.", "It shouldn't happen")
def left2(s):
    t = clock(s)
    s.add(left_top(), Line(P(-6.6, 0.8), P(6.6, 0.8), color=LINE, stroke_width=3), glider(t, 0.8, BLUE, False))
    yield [FadeIn(at(lab("a free electron, with nothing twisting it", 24, INK), 0, 0.25))]
    yield [FadeIn(at(mt(r"\frac{d\langle L_z\rangle}{dt} \neq 0", size=64), -3.6, -1.5)),
           FadeIn(left_at(words("the angular momentum of its motion changes in time", 28, 26), -1.0, -1.5))]
    m = at(T("that shouldn't happen", 30, RED, True), -0.3, -3.1)
    yield [FadeIn(m), Create(xmark(m))]


SHARE_X = (-5.2, -2.6, 0.6)
SHARE_Y = -2.3


def shares(t, other, tot):
    """The motion's share rises and falls; another share and their total fade in with the trackers other and tot."""
    def draw():
        a = 1.5 + 0.7 * np.sin(1.4 * t.get_value())
        b = 3.0 - a
        g = VGroup(Rectangle(width=1.4, height=a, stroke_color=INK, stroke_width=2.5, fill_color=INK, fill_opacity=0.25).move_to(P(SHARE_X[0], SHARE_Y + a / 2)))
        o, w = other.get_value(), tot.get_value()
        g.add(Rectangle(width=1.4, height=b, stroke_color=PURPLE, stroke_width=2.5, fill_color=PURPLE, fill_opacity=0.25).move_to(P(SHARE_X[1], SHARE_Y + b / 2))
              .set_stroke(opacity=o).set_fill(opacity=0.25 * o))
        g.add(Rectangle(width=1.4, height=a, stroke_color=INK, stroke_width=2.5, fill_color=INK, fill_opacity=0.25).move_to(P(SHARE_X[2], SHARE_Y + a / 2))
              .set_stroke(opacity=w).set_fill(opacity=0.25 * w))
        g.add(Rectangle(width=1.4, height=b, stroke_color=PURPLE, stroke_width=2.5, fill_color=PURPLE, fill_opacity=0.25).move_to(P(SHARE_X[2], SHARE_Y + a + b / 2))
              .set_stroke(opacity=w).set_fill(opacity=0.25 * w))
        return g
    return always_redraw(draw)


@slide("Angular momentum can't come from nowhere.", "A second share")
def share(s):
    t = clock(s)
    other, tot = ValueTracker(0.0), ValueTracker(0.0)
    s.add(other, tot, shares(t, other, tot), Line(P(-6.4, SHARE_Y), P(1.8, SHARE_Y), color=MUTED, stroke_width=3),
          at(words("the motion's share", 12, 22, INK, ORIGIN), SHARE_X[0], SHARE_Y - 0.55))
    yield [FadeIn(left_at(words("angular momentum can't come from nowhere", 24, 26), 2.6, 1.7))]
    yield [other.animate.set_value(1.0), FadeIn(at(words("carried somewhere else", 12, 22, PURPLE, ORIGIN), SHARE_X[1], SHARE_Y - 0.55)),
           FadeIn(left_at(words("if the motion's share changes, the electron must carry more of it somewhere else", 24, 26), 2.6, 0.0))]
    yield [tot.animate.set_value(1.0), FadeIn(at(lab("the total", 22, INK, True), SHARE_X[2], SHARE_Y - 0.4)),
           FadeIn(left_at(words("then the total could still stay the same", 24, 26, INK, bold=True), 2.6, -1.8))]


@slide("So we need a second term.", "A second term")
def second(s):
    a = at(card(None, 6.4, 1.3, INK), -3.6, 0.9)
    ta = at(mix(mt(r"[\hat L_z,\ \hat H]", size=44), "=", "the leftover", size=26), -3.6, 0.9)
    s.add(a, ta)
    yield [FadeIn(at(mix("a second term, call it", mt(r"\hat T", size=52), size=28, bold=True), 0, 2.3))]
    b = at(card(None, 6.4, 1.3, INK), 3.6, 0.9)
    yield [FadeIn(b), FadeIn(at(mix(mt(r"[\hat T,\ \hat H]", size=44), "=", "minus the leftover", size=26), 3.6, 0.9)),
           FadeIn(at(lab("its commutator with the energy operator: exactly minus the first one", 24, INK), 0, -0.4))]
    yield [FadeIn(at(mix("the leftover", "+", "minus the leftover", "=", mt("0", size=52), size=28), 0, -1.7)),
           FadeIn(at(T("then the two cancel", 28, INK, True), 0, -2.7))]


@slide("That requirement is on screen, and it tells us what to look for.", "The requirement")
def req1(s):
    s.add(left_top())
    m = at(requirement(64), 0, 0.2)
    sign = m[1][0]
    sign.set_stroke(INK, width=5)   # the minus sign, drawn heavier than the rest
    yield [FadeIn(m), FadeIn(at(lab("the requirement: minus the leftover", 24, INK, True), 0, 1.2))]
    yield [FadeIn(at(T("first: the term can be a matrix", 30, INK, True), 0, -2.0))]


@slide("The leftover on screen has matrices and momenta in it, and no position.", "It can be a matrix")
def req2(s):
    m = at(leftover(64), 0, 1.5)
    s.add(m)
    nopos = at(mt(r"\hat x,\ \hat y", size=64), 2.9, -0.45)
    yield [FadeIn(note(VGroup(*m[2:7]), "matrices and momenta", INK, chars=30, size=26)),
           FadeIn(nopos), Create(Line(nopos.get_corner(DL) + P(-0.15, 0.05), nopos.get_corner(UR) + P(0.15, -0.05), color=RED, stroke_width=3)),
           FadeIn(left_at(lab("no position", 26, INK, True), 4.3, -0.45))]
    yield [FadeIn(at(mix("so the new term", mt(r"\hat T", size=44), "needs no position either", size=26), -2.4, -1.7))]
    g = grid(4, 4, 0.36).move_to(P(4.6, -2.3))
    yield [FadeIn(g), FadeIn(right_at(lab("a matrix of plain numbers will do", 26, INK, True), 3.6, -2.9))]


@slide("A matrix of plain numbers doesn't care which side of a momentum it sits on.", "Either side of a momentum")
def req3(s):
    g = grid(4, 4, 0.36).move_to(P(-1.7, 1.5))
    p = at(mt(r"\hat p_x", size=72, color=PX), 0, 1.5)
    yield [FadeIn(g), FadeIn(p), g.animate(path_arc=-2.0).move_to(P(1.7, 1.5)),
           FadeIn(at(lab("a matrix of plain numbers doesn't care which side of a momentum it sits on", 24, INK), 0, 0.2))]
    yield [FadeIn(at(lab("so its commutator leaves the momenta as they are", 26, INK), 0, -0.8))]
    ex = at(mt(r"\alpha_x", r"\,\hat p_x", size=84), -4.0, -2.4)
    ex[0].set_color(PURPLE)
    ex[1].set_color(PX)
    yield [FadeIn(ex), Create(frame(ex[0], PURPLE, 0.1)), FadeIn(left_at(T("it can only change the matrices beside them", 28, INK, True), -2.4, -2.4))]


# ------------------------------------------------------------------ the swap: the energy operator beside the requirement

SW_Y = (1.2, -0.5)     # the energy operator's row, the requirement's row
SW_X = (-1.3, 1.7)     # the column of the x-momentum terms, the column of the y-momentum terms
SW_S = 46
SW_PAD = 0.22          # how far a column's band reaches past its terms


def swap_parts():
    """Both rows, with the terms that carry the same momentum under each other.

    Returns a dict: 'ax', 'ay' the energy operator's two terms, 'bx', 'by' the requirement's, each with its matrix
    as part 'm' (found below), and 'rest' everything else.
    """
    ya, yb = SW_Y
    ax = at(mt(r"\alpha_x", r"\,\hat p_x", size=SW_S), SW_X[0], ya)
    ay = at(mt(r"\alpha_y", r"\,\hat p_y", size=SW_S), SW_X[1], ya)
    bx = at(mt(r"\alpha_y", r"\,\hat p_x", size=SW_S), SW_X[0], yb)
    by = at(mt("-", r"\alpha_x", r"\,\hat p_y", size=SW_S), SW_X[1], yb)
    bx.shift(RIGHT * (ax[1].get_x() - bx[1].get_x()))
    by.shift(RIGHT * (ay[1].get_x() - by[2].get_x()))
    for cell, mk, pk, color in ((ax, 0, 1, PX), (ay, 0, 1, PY), (bx, 0, 1, PX), (by, 1, 2, PY)):
        cell[mk].set_color(PURPLE)
        cell[pk].set_color(color)
    x0, x1 = VGroup(ax, bx).get_left()[0] - SW_PAD, VGroup(ax, bx).get_right()[0] + SW_PAD   # the x band's edges
    y0, y1 = VGroup(ay, by).get_left()[0] - SW_PAD, VGroup(ay, by).get_right()[0] + SW_PAD   # the y band's edges
    plus = at(mt("+", size=SW_S), (x1 + y0) / 2, ya)
    pa = right_at(mt(r"c\,\bigl(", size=SW_S), x0 - 0.1, ya)
    la = right_at(mt(r"\hat H =", size=SW_S), pa.get_left()[0] - 0.2, ya)
    ra = left_at(mt(r"+\ \alpha_z\,\hat p_z\bigr) + \beta\,mc^2", size=SW_S, color=MUTED), y1 + 0.12, ya)
    pb = right_at(mt(r"i\hbar c\,\bigl(", size=SW_S), x0 - 0.1, yb)
    lb = right_at(mt(r"[\hat T,\ \hat H] =", size=SW_S), pb.get_left()[0] - 0.2, yb)
    rb = left_at(mt(r"\bigr)", size=SW_S), y1 + 0.1, yb)
    names = VGroup(left_at(lab("the energy operator", 24, INK, True), -7.0, ya + 0.8), left_at(lab("the requirement", 24, INK, True), -7.0, yb + 0.75))
    return {"ax": ax, "ay": ay, "bx": bx, "by": by, "am": (ax[0], ay[0]), "bm": (bx[0], VGroup(by[0], by[1])),
            "row_a": VGroup(la, pa, ax, plus, ay, ra), "row_b": VGroup(lb, pb, bx, by, rb), "names": names, "bands": ((x0, x1), (y0, y1))}


def swap_band(d, k, strong=False):
    color = (PX, PY)[k]
    a, b = d["bands"][k]
    x, w = (a + b) / 2, b - a
    mid = sum(SW_Y) / 2
    box = RoundedRectangle(width=w, height=SW_Y[0] - SW_Y[1] + 1.15, corner_radius=0.15, stroke_color=color, stroke_width=6 if strong else 2,
                           fill_color=color, fill_opacity=0.0 if strong else 0.1).move_to(P(x, mid))
    if strong:
        return box
    head = at(lab(("along x", "along y")[k], 22, color, True), x, SW_Y[0] + 0.95)
    return VGroup(box, head)


def swap_board():
    d = swap_parts()
    return d, VGroup(swap_band(d, 0), swap_band(d, 1), d["row_a"], d["row_b"], d["names"])


SWAP_TO = ((r"\alpha_x", r"\;\to\;", r"\alpha_y"), (r"\alpha_y", r"\;\to\;", r"-\,\alpha_x"))


def swap_to(k, size=60):
    m = at(mt(*SWAP_TO[k], size=size, color=PURPLE), (-3.3, 3.3)[k], -2.35)
    m[1].set_color(INK)
    return m


def swap_tag(k):
    return at(lab(("in the term along x", "in the term along y")[k], 22, (PX, PY)[k], True), (-3.3, 3.3)[k], -3.05)


@slide("Second, look at what the matrix has to do.", "Beside the requirement")
def swap1(s):
    orig = at(requirement(56), 0, 0.4)
    ask = at(T("second: what does the matrix have to do?", 30, INK, True), 0, 2.2)
    was = at(lab("the requirement", 24, INK, True), 0, 1.35)
    yield [FadeIn(orig), FadeIn(ask), FadeIn(was)]
    d, board = swap_board()
    yield [FadeOut(ask), FadeOut(was), orig.animate.scale(0.62).move_to(P(1.2, -3.0)), FadeIn(board),
           FadeIn(right_at(lab("the requirement, as it was:", 22), -2.3, -3.0)),
           FadeIn(at(lab("the same requirement, with its minus sign multiplied through", 22), 0.3, -2.15))]


@slide("Look at the term with the momentum along x.", "The term along x")
def swap2(s):
    d, board = swap_board()
    s.add(board)
    yield [Create(swap_band(d, 0, True))]
    m = swap_to(0)
    yield [Indicate(d["am"][0], color=PURPLE, scale_factor=1.5), TransformFromCopy(d["am"][0], m[0]), FadeIn(swap_tag(0))]
    yield [Indicate(d["bm"][0], color=PURPLE, scale_factor=1.5), FadeIn(m[1]), TransformFromCopy(d["bm"][0], m[2])]


@slide("Now the term with the momentum along y.", "The term along y")
def swap3(s):
    d, board = swap_board()
    a, b = swap_to(0), swap_to(1)
    s.add(board, swap_band(d, 0, True), a, swap_tag(0))
    yield [Create(swap_band(d, 1, True))]
    yield [Indicate(d["am"][1], color=PURPLE, scale_factor=1.5), Indicate(d["bm"][1], color=PURPLE, scale_factor=1.5),
           TransformFromCopy(d["am"][1], b[0]), FadeIn(b[1]), TransformFromCopy(d["bm"][1], b[2]), FadeIn(swap_tag(1))]
    yield [Create(frame(VGroup(a, b), PURPLE, 0.22)), FadeIn(caption("The new term has to swap those two matrices, with one change of sign.", -3.7, INK, 24))]


@slide("The spin matrices do exactly that to each other.", "The spin matrices")
def spins3(s):
    names = [at(purple(SPIN_NAMES[k], 96), SPIN_X[k], 0.6) for k in range(3)]
    yield [*[FadeIn(n) for n in names], *[FadeIn(at(lab(w.split(" ", 1)[1].replace(" magnet", ""), 24, INK), SPIN_X[k], -0.6)) for k, w in enumerate(SPIN_WORDS)],
           FadeIn(at(lab("the spin matrices do exactly that to each other", 26, INK), 0, 2.3))]
    yield [Create(frame(names[2], PURPLE, 0.25)), FadeIn(at(T("take the up-and-down one", 28, INK, True), 0, -2.2))]


def comm(k, size=64):
    tex = ((r"[\hat Z,\ \hat S]", "=", r"2i\,", r"\hat Y"), (r"[\hat Z,\ \hat Y]", "=", r"-2i\,", r"\hat S"))[k]
    return mt(*tex, size=size, color=PURPLE)


@slide("Its commutator with the sideways one gives a multiple of the front-to-back one.", "What Z-hat does to the other two")
def comms(s):
    a, b = at(comm(0), -3.6, 1.6), at(comm(1), 3.6, 1.6)
    yield [FadeIn(a), FadeIn(at(lab("sideways  →  front-to-back", 24, INK), -3.6, 0.7))]
    yield [FadeIn(b), FadeIn(at(lab("front-to-back  →  minus sideways", 24, INK), 3.6, 0.7))]
    ms = [at(big(0, 40), -3.6, -1.4), at(big(1, 40), 3.6, -1.4)]
    yield [*[FadeIn(m) for m in ms], *[Create(frame(m[1].get_entries()[j], PURPLE, 0.08, 2.5)) for m in ms for j in (1, 2)],
           FadeIn(at(lab("the momentum matrices for x and y are built from those two", 24, INK, True), 0, -2.9))]


SIGMA_ROWS = [[r"\hat Z", "0"], ["0", r"\hat Z"]]


def sigma(size=56):
    return named(r"\Sigma_z", mat(SIGMA_ROWS, size, PURPLE, 1.1, 0.95), size + 4, PURPLE)


@slide("So the matrix to try is built from the up-and-down spin matrix.", "The matrix to try")
def sig1(s):
    z = at(spin_mat(2, 52), -4.2, 0.3)
    yield [FadeIn(z), FadeIn(at(lab("the up-and-down spin matrix", 24, INK), -4.2, -1.3)), FadeIn(at(lab("the matrix to try is built from", 24), -4.2, 1.9))]
    c = at(col4m(60, 0.95), 4.6, -0.3)
    e = c.get_entries()
    copies = [at(purple(r"\hat Z", 60), 2.0, (e[2 * k].get_y() + e[2 * k + 1].get_y()) / 2) for k in range(2)]
    yield [FadeIn(c), FadeIn(pair_brace(c, True, False, LEFT)), FadeIn(pair_brace(c, False, False, LEFT)), *[TransformFromCopy(z[0][0][:2], m) for m in copies],
           FadeIn(at(lab("twice: once for each pair of the column", 26, INK, True), 3.4, 2.4))]


@slide("You can see it on screen.", "Not the momentum matrix")
def sig2(s):
    m = at(sigma(), -3.6, 0.9)
    e = m[1].get_entries()
    yield [FadeIn(m), Create(frame(e[0], PURPLE, 0.1)), Create(frame(e[3], PURPLE, 0.1)),
           FadeIn(at(VGroup(mix(mt(r"\hat Z", size=40, color=PURPLE), "on the diagonal:", size=24), lab("once for each pair", 24, INK)).arrange(DOWN, buff=0.1), -3.6, -1.1))]
    az = at(big(2, 56), 3.6, 0.9)
    f = az[1].get_entries()
    no = at(T("it isn't this one", 26, RED, True), 3.4, -2.3)
    yield [FadeIn(az), Create(frame(f[1], PURPLE, 0.1)), Create(frame(f[2], PURPLE, 0.1)),
           FadeIn(at(VGroup(mix(mt(r"\hat Z", size=40, color=PURPLE), "off the diagonal:", size=24), lab("it swaps the pairs", 24, INK)).arrange(DOWN, buff=0.1), 3.6, -1.1)),
           FadeIn(no), Create(xmark(no))]


def with_pref(lhs, pref, size=44):
    """A commutator with H: the left side, the number in front (part 1), the bracket (parts 2 to 8)."""
    m = mt(lhs, pref, r"\,\bigl(", r"\alpha_x", r"\,\hat p_y", "-", r"\alpha_y", r"\,\hat p_x", r"\bigr)", size=size)
    paint(m, PURPLE, 3, 6)
    m[4].set_color(PY)
    m[7].set_color(PX)
    return m


@slide("It works, apart from the number in front.", "The number in front")
def sig3(s):
    got, need = at(with_pref(r"[\Sigma_z,\ \hat H] =", "-2ic", 48), 0.8, 1.9), at(with_pref(r"[\hat T,\ \hat H] =", r"-i\hbar c", 48), 0.8, 0.6)
    need.shift(RIGHT * (got[2].get_x() - need[2].get_x()))
    yield [FadeIn(got), FadeIn(need), Create(frame(got[1], INK, 0.08, 2.5)), Create(frame(need[1], INK, 0.08, 2.5)),
           FadeIn(right_at(lab("the matrix gives", 24, INK), -3.8, 1.9)), FadeIn(right_at(lab("the requirement", 24, INK), -3.8, 0.6))]
    t = at(paint(mt(r"\hat T =", r"\frac{\hbar}{2}", r"\,\Sigma_z", size=64), PURPLE, 1, 2), 3.0, -1.2)
    yield [FadeIn(at(mt(r"-2ic \times \frac{\hbar}{2} = -i\hbar c", size=44), -3.2, -1.2)), GrowArrow(varrow(P(-0.5, -1.2), P(0.9, -1.2))), FadeIn(t)]
    yield [FadeIn(at(T("with that factor, the sum is kept", 28, INK, True), 0, -2.8))]


@slide("The total on screen never changes.", "The total is kept")
def sig4(s):
    tot = at(total(64), 0, 1.5)
    yield [FadeIn(tot), Create(frame(tot, INK, 0.22, 2.5))]
    yield [Create(frame(tot[3][:3], PURPLE, 0.1)), FadeIn(at(mix(mt(HB2, size=48, color=PURPLE), "wasn't a choice", size=28, bold=True), 0, -0.2))]
    yield [FadeIn(at(lab("it's the one number that makes the two cancel", 26, INK), 0, -1.2))]
    yield [FadeIn(at(mix("the other two axes work the same way, with", mt(r"\hat S", size=44, color=PURPLE), "and", mt(r"\hat Y", size=44, color=PURPLE), "in place of",
                         mt(r"\hat Z", size=44, color=PURPLE), size=24), 0, -2.6))]


def sum_terms(size=84):
    return paint(mt(r"\hat L_z", "+", r"\frac{\hbar}{2}\,\Sigma_z", size=size), PURPLE, 2)


@slide("Here's what the new term is.", "The new term")
def new1(s):
    m = at(sum_terms(), 0, 0.3)
    yield [FadeIn(m), FadeIn(note(m[2], "the new term", PURPLE, UP, size=26, buff=0.2))]
    yield [FadeIn(note(m[0], "the angular momentum of the motion", INK, chars=16)), FadeIn(left_at(words("the total never changes", 14, 26), 3.4, 0.3))]
    yield [FadeIn(at(T("so the new term is angular momentum too", 30, INK, True), 0, -2.9))]


@slide("But it's a matrix.", "A matrix, acting on the column")
def new2(s):
    m = at(VGroup(mt(r"\frac{\hbar}{2}", size=56, color=PURPLE), mat(SIGMA_ROWS, 52, PURPLE, 1.1, 0.95)).arrange(RIGHT, buff=0.2), -4.4, 0.7)
    yield [FadeIn(m), FadeIn(at(T("but it's a matrix", 28, INK, True), -4.4, 2.3))]
    c = at(col4m(48, 0.8), 0.2, 0.7)
    yield [GrowArrow(varrow(P(-2.2, 0.7), P(-0.8, 0.7), PURPLE)), FadeIn(c), FadeIn(at(words("it acts on the column of four wave functions", 24, 24, INK, ORIGIN), -2.0, -1.6))]
    a = at(card("where the electron is", 4.2, 0.9, INK, 24), 4.3, 1.3)
    b = at(card("how it moves", 4.2, 0.9, INK, 24), 4.3, 0.1)
    yield [FadeIn(a), FadeIn(b), Create(xmark(a, 0.36, 0.15)), Create(xmark(b, 0.36, 0.15)), FadeIn(at(lab("it doesn't act on these", 24, INK), 4.6, -1.0))]


@slide("The electron has it even at rest, when the angular momentum of its motion is zero.", "That's the spin")
def new3(s):
    e = espin(-4.6, 0.3, True, 2.6, 0.26)
    yield [FadeIn(e[1]), FadeIn(left_at(mix("at rest:", mt("L_z = 0", size=48), size=28), -2.6, 1.5)),
           FadeIn(left_at(mix("and it still has", mt(r"\frac{\hbar}{2}\,\Sigma_z", size=48, color=PURPLE), size=28), -2.6, 0.2))]
    yield [GrowArrow(e[0]), FadeIn(left_at(T("that's the spin", 52, PURPLE, True), -2.6, -1.6))]


@slide("Dirac asked for two things only.", "Nobody put it in")
def new4(s):
    yield [FadeIn(at(lab("Dirac asked for two things only", 26, INK), -3.6, 2.3))]
    a = at(card("an equation that agrees\nwith relativity", 5.6, 1.4, INK, 26), -3.6, 1.0)
    yield [FadeIn(a, shift=DOWN * 0.15)]
    b = at(card("a single rate of\nchange in time", 5.6, 1.4, INK, 26), -3.6, -0.9)
    yield [FadeIn(b, shift=DOWN * 0.15)]
    e = espin(4.4, 0.3, True, 2.2, 0.24)
    yield [GrowArrow(varrow(P(-0.5, 0.05), P(2.6, 0.05))), FadeIn(e[1]), GrowArrow(e[0]),
           FadeIn(at(T("the spin came out without his putting it in", 28, PURPLE, True), 0, -2.7))]


# ================================================================== spin up and spin down
deck.part("Spin up and spin down")


def spin_op(size=72):
    return mt(r"\frac{\hbar}{2}\,\Sigma_z", size=size, color=PURPLE)


@slide("Spin up and spin down.", "What the spin can be")
def read1(s):
    yield [FadeIn(at(lab("let's read off what the spin can be", 26, INK), 0, 2.3))]
    a = at(card("a measurement", 3.8, 1.1, INK, 28), -4.4, 0.8)
    b = at(card("one of the eigenvalues\nof its operator", 5.2, 1.4, INK, 26), 2.4, 0.8)
    yield [FadeIn(a), GrowArrow(varrow(P(-2.4, 0.8), P(-0.3, 0.8))), FadeIn(at(lab("gives", 22), -1.35, 1.1)), FadeIn(b)]
    yield [FadeIn(at(mix("the spin's operator:", spin_op(72), size=28), -0.6, -1.6)), FadeIn(left_at(VGroup(mix("half of", mt(r"\hbar", size=36, color=MUTED), ", times", size=24, color=MUTED), lab("the matrix we found", 24)).arrange(DOWN, buff=0.1, aligned_edge=LEFT), 3.2, -1.6))]


def sigma_full(size=34, v=0.6):
    rows = [["1", "0", "0", "0"], ["0", "-1", "0", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "-1"]]
    return mat(rows, size, PURPLE, 0.75, v)


def spin_result(size=40, v=1.0):
    m = mat([[r"+\frac{\hbar}{2}\,\psi_1"], [r"-\frac{\hbar}{2}\,\psi_2"], [r"+\frac{\hbar}{2}\,\psi_3"], [r"-\frac{\hbar}{2}\,\psi_4"]], size, v=v)
    for k, e in enumerate(m.get_entries()):
        e[0][:4].set_color(PURPLE)
        e[0][4:].set_color(BLUE if k < 2 else LOW)
    return m


def spin_eq(v=1.0):
    """(h-bar/2) Sigma_z psi = (h-bar/2) (the diagonal 1, -1, 1, -1) (the column) = (the result). Part 5 is the result."""
    lhs = paint(mt(r"\frac{\hbar}{2}\,\Sigma_z", r"\,\psi =", size=48), PURPLE, 0)
    return VGroup(lhs, mt(r"\frac{\hbar}{2}", size=48, color=PURPLE), sigma_full(40, v), col4m(44, v), mt("=", size=48), spin_result(34, v)).arrange(RIGHT, buff=0.22)


@slide("It's on screen, acting on the column.", "The spin's operator on the column")
def read2(s):
    m = at(spin_eq(), 0, 0.45)
    res = m[5]
    e = res.get_entries()
    yield [FadeIn(VGroup(*m[:4])), FadeIn(at(mix("the entries of", mt(r"\hat Z", size=38, color=PURPLE), ", twice down the diagonal", size=22, color=MUTED), m[2].get_x(), -2.25))]
    yield [FadeIn(m[4]), FadeIn(res.get_brackets()), FadeIn(e[0])]
    yield [FadeIn(e[1])]
    yield [FadeIn(e[2]), FadeIn(e[3]), FadeIn(at(lab("the third and fourth go the same way", 24, INK), 0, -3.05))]


@slide("So the spin along the vertical has two possible results.", "Two results")
def read3(s):
    yield [FadeIn(at(lab("the spin along the vertical: two possible results", 26, INK), 0, 2.3)), FadeIn(at(mt(r"+\hbar/2", size=84, color=PURPLE), -3.2, 0.8)),
           FadeIn(at(mt(r"-\hbar/2", size=84, color=PURPLE), 3.6, 0.8))]
    a, b = espin(-5.6, 0.8, True, 1.8, 0.2), espin(1.2, 0.8, False, 1.8, 0.2)
    yield [FadeIn(a[1]), GrowArrow(a[0]), FadeIn(b[1]), GrowArrow(b[0]), FadeIn(at(T("spin up", 40, PURPLE, True), -3.2, -1.2)),
           FadeIn(at(T("spin down", 40, PURPLE, True), 3.6, -1.2))]


UNIT_Y = (1.5, -0.6)


def unit_row(k, part):
    """A result as chapter 2b named it, times the unit, giving the result in h-bar. part 0: the number, 1: the open unit, 2: the unit and the product."""
    y = UNIT_Y[k]
    sign = "+-"[k]
    if part == 0:
        return at(mt(sign + "1", size=64), -4.6, y)
    if part == 1:
        return VGroup(at(mt(r"\times", size=52), -3.4, y),
                      DashedVMobject(RoundedRectangle(width=1.3, height=1.55, corner_radius=0.12, color=MUTED, stroke_width=3), num_dashes=30).move_to(P(-2.0, y)))
    return VGroup(at(mt(r"\frac{\hbar}{2}", size=52, color=PURPLE), -2.0, y), at(mt("=", size=52), -0.6, y),
                  at(mt(sign + r"\frac{\hbar}{2}", size=60, color=PURPLE), 0.7, y))


@slide("The chapter on first quantization called these results plus one and minus one.", "The unit")
def unit(s):
    yield [FadeIn(unit_row(0, 0)), FadeIn(unit_row(1, 0)), FadeIn(left_at(lab("chapter 2b's names", 24), -7.0, 2.5))]
    left_open = at(lab("the unit: left open", 24), -2.0, -1.8)
    yield [FadeIn(unit_row(0, 1)), FadeIn(unit_row(1, 1)), FadeIn(left_open)]
    yield [FadeOut(left_open), FadeIn(unit_row(0, 2)), FadeIn(unit_row(1, 2)),
           FadeIn(left_at(mix("now we know the unit:", mt(HB2, size=48, color=PURPLE), size=28, bold=True), 2.4, 0.45))]
    yield [FadeIn(at(lab("the size Uhlenbeck and Goudsmit proposed", 28, INK), 0, -2.8))]


@slide("And because it's half of h-bar, physicists say the electron has spin one half.", "Spin one half")
def half(s):
    yield [FadeIn(at(T("spin one half", 60, PURPLE, True), 0, 1.7)), FadeIn(at(mix("because its size is half of", mt(r"\hbar", size=44), size=26), 0, 0.6))]
    e = espin(-5.4, -1.6, True, 1.8, 0.2)
    line = DashedLine(P(-5.4, -3.0), P(-5.4, -0.2), color=MUTED, stroke_width=2.5)
    yield [FadeIn(line), FadeIn(e), FadeIn(left_at(words("the next section: the electron's magnet lies along the same line as this spin", 28, 24), -4.6, -1.6))]
    pl = plate(3.2, -1.6, (0.75, -0.75), INK, 1.7, 2.4)
    yield [FadeIn(pl), FadeIn(left_at(mt(r"+\hbar/2", size=36, color=PURPLE), 4.3, -0.85)), FadeIn(left_at(mt(r"-\hbar/2", size=36, color=PURPLE), 4.3, -2.35)),
           FadeIn(left_at(words("the two spots on the plate", 14, 24, INK, bold=True), 4.3, -1.6))]


@slide("That answers the question about the four wave functions.", "The answer")
def answer(s):
    c = at(col4m(72, 1.05), -4.0, -0.3)
    yield [FadeIn(c), FadeIn(pair_brace(c, True, False)), FadeIn(pair_brace(c, False, False)),
           FadeIn(at(lab("that answers the question about the four wave functions", 26, INK), 0, 2.4))]
    e = c.get_entries()
    tags = VGroup()
    for k in range(4):
        y = e[k].get_y()
        tags.add(VGroup(spin_arrow(-2.2, y, k % 2 == 0, 0.7, width=5), left_at(T(TAB_SPIN[k], 30, PURPLE, True), -1.8, y)))
    yield [LaggedStart(*[FadeIn(t) for t in tags], lag_ratio=0.2),
           FadeIn(left_at(words("in each pair, the first is spin up and the second is spin down", 26, 26), 1.2, -0.3))]


SOL_X = (-5.4, -1.8, 1.8, 5.4)
SOL_TOP = 1.3


def solution(k):
    """One solution for a particle at rest: its column, with one entry filled, and its spin."""
    color = BLUE if k < 2 else LOW
    g = VGroup()
    for i in range(4):
        on = i == k
        y = SOL_TOP - 0.7 * i
        g.add(Square(0.65, stroke_color=color, stroke_width=3, fill_color=color if on else PALE, fill_opacity=0.85 if on else 0.4).move_to(P(SOL_X[k], y)),
              at(mt("1" if on else "0", size=36, color=WHITE if on else MUTED), SOL_X[k], y))
    return g


def sol_spin(k):
    return at(T("spin " + TAB_SPIN[k], 28, PURPLE, True), SOL_X[k], 2.3)


def sol_energy(k):
    color, x = ((BLUE, -3.6), (LOW, 3.6))[k]
    return VGroup(Line(P(x - 2.6, -1.35), P(x + 2.6, -1.35), color=color, stroke_width=3),
                  at(mix("energy", mt(("+mc^2", "-mc^2")[k], size=44, color=color), size=28, color=color), x, -1.85),
                  at(lab(("upper pair of entries", "lower pair of entries")[k], 22), x, -2.45))


@slide("The four solutions for a particle at rest are on screen.", "Four solutions at rest")
def four_sol(s):
    spins = VGroup(*[sol_spin(k) for k in range(4)])
    energies = VGroup(sol_energy(0), sol_energy(1))
    yield [LaggedStart(*[FadeIn(solution(k)) for k in range(4)], lag_ratio=0.15), FadeIn(spins), FadeIn(energies)]
    yield [Indicate(energies[0][1], color=BLUE, scale_factor=1.15), Indicate(energies[1][1], color=LOW, scale_factor=1.15),
           FadeIn(at(lab("the energy tells the pairs apart", 24, INK, True), 0, -3.05))]
    yield [Indicate(spins, color=PURPLE, scale_factor=1.1), FadeIn(at(lab("the spin tells the two members of a pair apart", 24, INK, True), 0, -3.6))]


@slide("Nothing is special about the vertical.", "Any direction")
def anydir(s):
    t = clock(s)
    c = P(-4.2, -0.3)

    def draw():
        u = uvec(PI / 2 - 0.5 * t.get_value())
        return VGroup(DashedLine(c - 2.3 * u, c + 2.3 * u, color=MUTED, stroke_width=2.5), varrow(c, c - 1.7 * u, PURPLE, 6, 0.2).set_opacity(0.3),
                      varrow(c, c + 1.7 * u, PURPLE, 6, 0.2), Dot(c, radius=0.2, color=BLUE))
    s.add(always_redraw(draw))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(left_at(lab("nothing is special about the vertical", 28, INK), -0.6, 1.2))]
    yield [FadeIn(left_at(lab("measure the spin along any other direction:", 26, INK), -0.6, -0.2)),
           FadeIn(left_at(mix("again", mt(r"+\hbar/2", size=52, color=PURPLE), "or", mt(r"-\hbar/2", size=52, color=PURPLE), size=28), -0.6, -1.3))]


# ================================================================== the strength of the magnet
deck.part("The strength of the magnet")


@slide("The strength of the magnet.", "The puzzle again")
def again(s):
    yield [FadeIn(at(lab("back to the puzzle", 26, INK), 0, 2.3))]
    r = at(card("the rule for a\nspinning charge", 4.2, 1.4, INK, 26), -1.6, 0.6)
    a = at(mt(E4M, size=72, color=RED), 2.8, 0.6)
    yield [FadeIn(at(mt(HB2, size=64, color=PURPLE), -5.6, 0.6)), GrowArrow(varrow(P(-4.7, 0.6), P(-3.9, 0.6))), FadeIn(r), GrowArrow(varrow(P(0.7, 0.6), P(1.9, 0.6))), FadeIn(a)]
    b = at(mt(E2M, size=72), 2.8, -1.8)
    yield [FadeIn(b), FadeIn(right_at(lab("Stern and Gerlach measured", 26, INK), 1.7, -1.8)), FadeIn(left_at(T("twice that", 28, INK, True), 3.9, -1.8))]


@slide("The equation has just given the spin its size.", "Ask the equation")
def ask(s):
    e = espin(-5.6, 0.6, True, 1.8, 0.2)
    m = left_at(mt(HB2, size=72, color=PURPLE), -4.8, 0.6)
    yield [FadeIn(e), FadeIn(m), Create(tick(m)), FadeIn(at(words("the equation has just given the spin its size", 24, 24, INK, ORIGIN), -4.4, -1.0))]
    c = at(card("the Dirac equation", 4.0, 1.1, INK, 26), 1.0, 0.6)
    yield [FadeIn(c), GrowArrow(varrow(P(3.1, 0.6), P(4.1, 0.6))), FadeIn(at(mt(r"\mu = \ ?", size=72), 5.6, 0.6)),
           FadeIn(at(words("so let's ask it for the strength of the magnet", 26, 26, INK, ORIGIN, True), 3.2, -1.0))]


def field_arrows(xs, y0, y1, label_at=None):
    g = VGroup(*[varrow(P(x, y0), P(x, y1), LINE, 4, 0.18) for x in xs])
    if label_at:
        g.add(at(lab("magnetic field", 22), *label_at))
    return g


def needle(x, y, up=True, L=1.0, color=INK):
    """A magnet drawn as an arrow, like a compass needle."""
    d = (1 if up else -1) * L / 2
    return varrow(P(x, y - d), P(x, y + d), color, 8, 0.24)


@slide("Here's how to ask.", "What the strength of a magnet means")
def means(s):
    yield [FadeIn(field_arrows((-6.4, -5.2, -4.0), -2.2, 1.6, (-5.2, 2.1))), FadeIn(needle(-5.8, -0.3, True, 1.4)),
           FadeIn(left_at(words("chapter 2b: an atom in a magnetic field was like a compass needle", 34, 24), -2.8, 2.0))]
    yield hold()
    hi = VGroup(Line(P(-2.6, 0.5), P(0.6, 0.5), color=INK, stroke_width=5), needle(-1.0, 1.0, False, 0.7), left_at(lab("pointing down", 24, INK), 1.0, 0.5))
    lo = VGroup(Line(P(-2.6, -1.3), P(0.6, -1.3), color=INK, stroke_width=5), needle(-1.0, -0.8, True, 0.7), left_at(lab("pointing up", 24, INK), 1.0, -1.3))
    yield [FadeIn(hi), FadeIn(lo), FadeIn(at(lab("slightly different energies", 24), -1.0, -2.0))]
    yield [FadeIn(DoubleArrow(P(-2.9, -1.3), P(-2.9, 0.5), buff=0, color=INK, stroke_width=4, tip_length=0.16)),
           FadeIn(at(T("that difference is what the strength of a magnet means", 28, INK, True), 0.4, -3.0))]


LV = (-3.4, 3.4)   # the two cases: lined up with the field, and against it


def level_base(k):
    x = LV[k]
    return VGroup(DashedLine(P(x - 1.6, 0.3), P(x + 1.6, 0.3), color=MUTED, stroke_width=2.5), field_arrows((x - 2.6,), -1.0, 1.6),
                  needle(x - 2.0, 0.3, k == 0, 1.2), at(lab(("lined up with the field", "lined up against the field")[k], 24, INK), x - 0.4, 2.3))


def level_line(k):
    return Line(P(LV[k] - 1.6, 0.3), P(LV[k] + 1.6, 0.3), color=INK, stroke_width=6)


@slide("Line a magnet up with the field, and its energy goes down.", "Lowered or raised")
def levels(s):
    s.add(level_base(0))
    a = level_line(0)
    s.add(a)
    yield [a.animate.shift(DOWN * 1.1), FadeIn(at(lab("its energy goes down", 24, INK), LV[0], -1.4))]
    yield [FadeIn(DoubleArrow(P(LV[0] + 1.9, -0.8), P(LV[0] + 1.9, 0.3), buff=0, color=MUTED, stroke_width=4, tip_length=0.16)),
           FadeIn(left_at(mt(r"\mu B", size=48), LV[0] + 2.1, -0.25)),
           FadeIn(at(mix("the drop: the magnet's strength", mt(r"\mu", size=40), "times the field", mt("B", size=40), size=24), -2.6, -2.4))]
    b = level_line(1)
    yield [FadeIn(level_base(1)), FadeIn(b), b.animate.shift(UP * 1.1), FadeIn(at(lab("its energy goes up by the same amount", 24, INK), LV[1] - 0.3, -1.4)),
           FadeIn(left_at(mt(r"\mu B", size=48), LV[1] + 2.1, 0.85)),
           FadeIn(DoubleArrow(P(LV[1] + 1.9, 0.3), P(LV[1] + 1.9, 1.4), buff=0, color=MUTED, stroke_width=4, tip_length=0.16))]


@slide("So we put the electron in a field that points up.", "A field that points up")
def fieldup(s):
    f = field_arrows((-6.0, -4.6, -3.2, 3.2, 4.6, 6.0), -1.8, 1.8)
    yield [FadeIn(f), FadeIn(at(mix("a field", mt("B", size=44), "that points up", size=26), 0, 2.3)), FadeIn(espin(-1.6, 0.3, True, 1.8, 0.2)), FadeIn(espin(1.6, 0.3, False, 1.8, 0.2))]
    yield [FadeIn(at(mt(r"E_{\text{up}}", size=56), -1.6, -1.6)), FadeIn(at(mt(r"E_{\text{down}}", size=56), 1.6, -1.6)), FadeIn(at(T("?", 40, MUTED, True), 0, -1.6)),
           FadeIn(at(lab("compare the energies of spin up and spin down", 26, INK, True), 0, -2.8))]


@slide("A magnetic field goes into the equation of a charged particle in a standard way.", "A slow particle in a field")
def slow(s):
    a = at(card("a magnetic field goes into the equation\nof a charged particle in a standard way", 8.4, 1.5, INK, 26), -2.6, 1.7)
    yield [FadeIn(a)]
    yield [FadeIn(left_at(lab("we won't derive it here", 24), 2.0, 1.7))]
    c = at(col4m(52, 0.8), -5.0, -1.5)
    yield [FadeIn(c), FadeIn(left_at(lab("a slow particle with positive energy", 26, INK), -3.4, -0.5))]
    e = c.get_entries()
    yield [e[2].animate.scale(0.5).set_opacity(0.45), e[3].animate.scale(0.5).set_opacity(0.45), Create(frame(VGroup(e[0], e[1]), BLUE, 0.14)),
           FadeIn(left_at(lab("its lower pair is tiny", 26, LOW), -3.4, -1.5)),
           FadeIn(left_at(lab("the equation reduces to one for the upper pair alone", 26, BLUE, True), -3.4, -2.5))]


@slide("And that upper pair is something we know.", "The upper pair")
def upper(s):
    m = mat([[r"\psi_1"], [r"\psi_2"]], 84, v=1.3)
    m.get_entries().set_color(BLUE)
    at(m, -4.4, 0.0)
    yield [FadeIn(m), FadeIn(at(lab("the upper pair", 26, BLUE, True), -4.4, 2.1))]
    yield [FadeIn(left_at(lab("chapter 2a's list of two amplitudes", 28, INK, True), -2.4, 2.1))]
    e = m.get_entries()
    rows = VGroup(*[VGroup(varrow(P(-3.0, e[k].get_y()), P(-2.0, e[k].get_y())), spin_arrow(-1.4, e[k].get_y(), k == 0, 0.8, width=5),
                           left_at(lab(("the amplitude for spin up", "the amplitude for spin down")[k], 26, INK), -0.9, e[k].get_y())) for k in range(2)])
    yield [FadeIn(rows, lag_ratio=0.3)]


def energy_eq(k, size=60):
    """E_up or E_down in parts: the name, =, E_0, the sign, the shift."""
    return mt((r"E_{\text{up}}", r"E_{\text{down}}")[k], "=", "E_0", "-+"[k], r"\frac{q\hbar}{2m}\,B", size=size)


def energies(x, ys, size=60):
    a, b = at(energy_eq(0, size), x, ys[0]), at(energy_eq(1, size), x, ys[1])
    b.shift(RIGHT * (a[1].get_x() - b[1].get_x()))
    return a, b


@slide("The equation gives the two their energies, and they're on screen.", "The two energies")
def twoe(s):
    a, b = energies(-1.0, (1.3, -0.7), 68)
    yield [FadeIn(a), FadeIn(b)]
    yield [Create(under(a[2], INK, 0.12, 5)), Create(under(b[2], INK, 0.12, 5)), FadeIn(at(lab("part of the energy: the same for both", 24, INK), -1.4, -2.0))]
    yield [VGroup(a[3], a[4]).animate.set_color(PURPLE), VGroup(b[3], b[4]).animate.set_color(PURPLE),
           FadeIn(left_at(lab("spin up: shifted one way", 24, PURPLE), 3.0, 1.3)), FadeIn(left_at(lab("spin down: the other way", 24, PURPLE), 3.0, -0.7))]


@slide("Compare that with a magnet in a field.", "The strength of the magnet")
def compare(s):
    a, b = energies(-3.6, (2.1, 0.9), 48)
    s.add(a, b)
    yield [FadeIn(at(mt(r"-\,\mu B", size=56), 2.6, 2.1)), FadeIn(at(mt(r"+\,\mu B", size=56), 2.6, 0.9)), FadeIn(left_at(lab("a magnet in a field", 24), 4.0, 1.5)),
           GrowArrow(varrow(P(0.6, 2.1), P(1.5, 2.1))), GrowArrow(varrow(P(0.6, 0.9), P(1.5, 0.9)))]
    m = at(mt(r"\mu", "=", r"\frac{q\hbar}{2m}", size=72), -3.6, -2.15)
    yield [FadeIn(m), Create(frame(m, INK, 0.22, 2.5)), FadeIn(at(lab("the particle is a magnet, of strength", 24, INK), -3.6, -0.6))]
    yield [FadeIn(Dot(P(1.4, -1.8), radius=0.2, color=INK)), GrowArrow(spin_arrow(1.4, -1.8, True, 1.9)), GrowArrow(needle(2.1, -1.8, True, 1.5)),
           FadeIn(left_at(lab("spin", 22, PURPLE, True), 0.2, -1.2)), FadeIn(left_at(lab("magnet", 22, INK, True), 2.5, -1.2)),
           FadeIn(left_at(words("for a positive charge, the magnet points along the spin", 20, 24), 4.2, -2.3))]


@slide("For the electron, that strength is the measured value.", "The measured value")
def measured(s):
    a = at(mt(r"\frac{q\hbar}{2m}", size=84), -4.2, 0.7)
    b = at(mt(E2M, size=96), 1.2, 0.7)
    v = left_at(T("the measured value", 30, INK, True), 2.4, 0.7)
    yield [FadeIn(a), GrowArrow(varrow(P(-3.0, 0.7), P(-0.2, 0.7))), FadeIn(at(lab("for the electron", 24), -1.6, 1.05)), FadeIn(b), FadeIn(v), Create(tick(v))]
    yield [FadeIn(at(lab("one detail is worth adding", 26, INK), 0, -1.9))]


@slide("The electron's charge is negative.", "Opposite to the spin")
def opposite(s):
    yield [FadeIn(at(mt("q = -e", size=84), -4.6, 1.3)), FadeIn(at(lab("the electron's charge is negative", 24, INK), -4.6, 0.3))]
    yield [FadeIn(electron(-5.4, -1.8, BLUE, 0.2)), GrowArrow(spin_arrow(-5.4, -1.8, True, 1.9)), GrowArrow(needle(-4.6, -1.8, False, 1.5)),
           FadeIn(left_at(lab("spin", 22, PURPLE, True), -6.6, -1.2)), FadeIn(left_at(lab("magnet", 22, INK, True), -4.2, -2.4)),
           FadeIn(left_at(words("so its magnet points opposite to its spin", 18, 24), -3.0, -1.5))]
    hi = VGroup(Line(P(3.0, 1.2), P(5.6, 1.2), color=INK, stroke_width=5), left_at(lab("spin up", 24, PURPLE, True), 5.9, 1.2), spin_arrow(4.3, 1.7, True, 0.7, width=5))
    lo = VGroup(Line(P(3.0, -0.6), P(5.6, -0.6), color=INK, stroke_width=5), left_at(lab("spin down", 24, PURPLE, True), 5.9, -0.6), spin_arrow(4.3, -0.1, False, 0.7, width=5))
    yield [FadeIn(field_arrows((2.2,), -1.0, 1.9)), FadeIn(at(mt("B", size=40, color=MUTED), 2.2, -1.35)), FadeIn(hi), FadeIn(lo), FadeIn(at(lab("energy, in a field that points up", 22), 4.6, 2.4)),
           FadeIn(at(words("spin up has the higher energy", 30, 26, INK, ORIGIN, True), 4.6, -2.2))]


def ratio(size=64):
    """mu over spin = (q h-bar / 2m) divided by (h-bar / 2) = q / m. Parts 0 to 4 are the division, 5 and 6 the result."""
    m = mt(r"\frac{\mu}{\text{spin}}", "=", r"\frac{q\hbar}{2m}", r"\div", r"\frac{\hbar}{2}", "=", r"\frac{q}{m}", size=size)
    m[4].set_color(PURPLE)
    return m


@slide("Now divide the strength by the angular momentum, which is half of h-bar.", "Strength over spin")
def divide(s):
    m = at(ratio(72), 0, 1.0)
    yield [FadeIn(VGroup(*m[:5])), FadeIn(at(lab("the strength, divided by the angular momentum", 24, INK), 0, 2.4))]
    yield [FadeIn(VGroup(m[5], m[6])), Create(frame(m[6], INK, 0.15, 2.5)), FadeIn(note(m[6], "the charge over the mass", INK, chars=12, buff=0.3))]
    r = at(mt(r"\frac{q}{2m}", size=72, color=RED), -1.0, -2.3)
    yield [FadeIn(r), FadeIn(right_at(lab("the rule for a spinning charge gave", 24, RED), r.get_left()[0] - 0.4, -2.3))]


@slide("So the spin makes a magnet twice as strong as the rule allows.", "Twice the rule")
def twice(s):
    m = at(mt(r"\frac{q}{m}", "=", "2", r"\times", r"\frac{q}{2m}", size=96), 0, 0.9)
    yield [FadeIn(m), Create(frame(m[2], INK, 0.15, 3)), FadeIn(note(m[0], "the spin's magnet", INK, chars=12)), FadeIn(note(m[4], "the rule for a spinning charge", INK, chars=16))]
    a = at(T("that's the answer to the puzzle", 32, INK, True), -0.3, -2.7)
    yield [FadeIn(a), Create(tick(a))]


@slide("And nobody put the factor of two in.", "Nobody put the two in")
def nobody(s):
    d = at(card("the Dirac equation", 4.2, 1.2, INK, 28, fill=PALE), 0.6, 0.2)
    out = left_at(T("the factor of two", 28, INK, True), 4.2, 0.2)
    yield [FadeIn(d), GrowArrow(varrow(P(2.8, 0.2), P(4.0, 0.2))), FadeIn(out), FadeIn(at(lab("nobody put the factor of two in", 26, INK), 0, 2.3))]
    a = at(card("the energy rule\nof relativity", 4.0, 1.3, INK, 26), -4.8, 1.1)
    yield [FadeIn(a), GrowArrow(varrow(P(-2.7, 1.0), P(-1.6, 0.5)))]
    b = at(card("the field, put in as for\nany charged particle", 4.6, 1.3, INK, 24), -4.8, -0.9)
    yield [FadeIn(b), GrowArrow(varrow(P(-2.4, -0.8), P(-1.6, -0.2)))]


# ================================================================== one full turn flips the sign
deck.part("One full turn flips the sign")


def space_dial(c, th, r=1.0, dot=True):
    """A spin in space, tilted from the vertical toward the right by the angle th."""
    c = P(*c)
    g = VGroup(DashedLine(c + DOWN * (r + 0.2), c + UP * (r + 0.2), color=LINE, stroke_width=2.5),
               varrow(c, c + r * np.array([np.sin(th), np.cos(th), 0.0]), PURPLE, 6, 0.2))
    if dot:
        g.add(Dot(c, radius=0.09, color=BLUE))
    return g


def state_axes(c, r=1.0):
    c = P(*c)
    return VGroup(Line(c + LEFT * r, c + RIGHT * r, color=LINE, stroke_width=2.5), Line(c + DOWN * r, c + UP * r, color=LINE, stroke_width=2.5))


def state_dial(c, a, r=1.0):
    """A state drawn as an arrow on the page, at the angle a from the across direction."""
    return VGroup(state_axes(c, r), varrow(P(*c), P(*c) + r * uvec(a), BLUE, 7, 0.22))


def pair_tex(tex, size=56):
    return mt(tex, size=size, color=BLUE)


@slide("One full turn flips the sign.", "One more consequence")
def turn0(s):
    e = espin(-4.6, 0.0, True, 2.4, 0.26)
    yield [FadeIn(e)]
    yield [FadeIn(left_at(T("spin one half has one more consequence", 30, INK, True), -2.8, 0.7))]
    yield [FadeIn(left_at(lab("it follows from something we've used since chapter 2a", 26, INK), -2.8, -0.5))]


@slide("That chapter wrote a spin state as a list of two amplitudes.", "A list of two amplitudes")
def lists(s):
    box = at(card(None, 8.6, 1.0, BLUE), 0, 1.6)
    yield [FadeIn(box), FadeIn(at(mix("( amplitude for up ,  amplitude for down )", size=28, color=BLUE), 0, 1.6)), FadeIn(at(lab("a spin state", 24), 0, 2.45))]
    yield [FadeIn(espin(-4.8, -0.3, True, 1.4, 0.18)), FadeIn(left_at(T("spin up", 30, PURPLE, True), -4.2, -0.3)), FadeIn(at(pair_tex(r"(1,\ 0)", 84), 1.6, -0.3))]
    yield [FadeIn(espin(-4.8, -2.3, False, 1.4, 0.18)), FadeIn(left_at(T("spin down", 30, PURPLE, True), -4.2, -2.3)), FadeIn(at(pair_tex(r"(0,\ 1)", 84), 1.6, -2.3))]


PG = (-3.8, -0.5)   # the centre of the page's axes
PR = 2.2


def page_axes():
    return state_axes(PG, PR + 0.4)


def page_arrow(k):
    c = P(*PG)
    tip = c + PR * (RIGHT if k == 0 else UP)
    tex = pair_tex((r"(1,\ 0)", r"(0,\ 1)")[k], 44)
    tex.move_to(tip + (P(0.1, -0.5) if k == 0 else P(0.95, 0.0)))
    return VGroup(varrow(c, tip, BLUE, 8, 0.26), tex)


@slide("Now draw each list as a single arrow on a page.", "An arrow on a page")
def page1(s):
    yield [FadeIn(page_axes()), FadeIn(left_at(lab("draw each list as a single arrow on a page", 26, INK), 0.2, 1.6))]
    c = P(*PG)
    yield [FadeIn(left_at(lab("across: the first amplitude", 24, BLUE), 0.2, 0.4)), FadeIn(left_at(lab("upward: the second amplitude", 24, BLUE), 0.2, -0.4)),
           GrowArrow(varrow(c + P(0.2, -0.4), c + P(1.6, -0.4), MUTED, 3, 0.14)), GrowArrow(varrow(c + P(-0.4, 0.2), c + P(-0.4, 1.6), MUTED, 3, 0.14))]
    yield [FadeIn(left_at(words("careful: these are directions on the page, not in space", 30, 26, INK, bold=True), 0.2, -2.1))]


@slide("The arrow for spin up lies flat, pointing right.", "At right angles")
def page2(s):
    s.add(page_axes())
    a, b = page_arrow(0), page_arrow(1)
    yield [GrowArrow(a[0]), FadeIn(a[1]), FadeIn(left_at(lab("spin up: flat, pointing right", 26, INK), 0.8, 1.2))]
    yield [GrowArrow(b[0]), FadeIn(b[1]), FadeIn(left_at(lab("spin down: upright", 26, INK), 0.8, 0.2))]
    c = P(*PG)
    corner = VMobject(color=INK, stroke_width=3).set_points_as_corners([c + P(0.4, 0), c + P(0.4, 0.4), c + P(0, 0.4)])
    yield [Create(corner), FadeIn(left_at(T("the two arrows are at right angles", 28, INK, True), 0.8, -1.4))]


@slide("Think about what that says.", "Opposite in space, at right angles in the state")
def angles(s):
    cs, cp = P(-3.8, -0.6), P(2.6, -1.3)
    yield [FadeIn(at(T("in space", 28, PURPLE, True), -3.8, 2.3)), FadeIn(at(T("in the state", 28, BLUE, True), 3.6, 2.3))]
    yield [GrowArrow(varrow(cs, cs + UP * 1.6, PURPLE, 6)), GrowArrow(varrow(cs, cs + DOWN * 1.6, PURPLE, 6)), FadeIn(Dot(cs, radius=0.12, color=BLUE)),
           FadeIn(at(lab("up", 24, PURPLE), -3.8, 1.3)), FadeIn(at(lab("down", 24, PURPLE), -3.8, -2.5)), FadeIn(left_at(lab("opposite", 26, INK), -6.6, -0.6))]
    yield [Create(Arc(radius=0.7, start_angle=PI / 2, angle=-PI, arc_center=cs, color=INK, stroke_width=3)), FadeIn(left_at(T("180° apart", 30, INK, True), -2.8, -0.6))]
    corner = VMobject(color=INK, stroke_width=3).set_points_as_corners([cp + P(0.4, 0), cp + P(0.4, 0.4), cp + P(0, 0.4)])
    yield [FadeIn(state_axes(cp, 2.2)), GrowArrow(varrow(cp, cp + RIGHT * 1.9, BLUE, 7)), GrowArrow(varrow(cp, cp + UP * 1.9, BLUE, 7)), Create(corner),
           FadeIn(left_at(T("90° apart", 30, INK, True), 3.4, -0.3)), FadeIn(at(lab("up", 24, BLUE), 4.4, -1.65)), FadeIn(at(lab("down", 24, BLUE), 2.6, 1.15))]


TH = np.radians(50)      # the tilt used as the example
TC = (-5.0, 0.0)         # the tilted spin's centre
HALF = (r"\Bigl(", r"\cos", r"\frac{\theta}{2}", r",\ ", r"\sin", r"\frac{\theta}{2}", r"\Bigr)")


def half_formula(size=64):
    return mt(*HALF, size=size, color=BLUE)


def tilt(c=TC, th=TH, r=1.7):
    """A tilted spin in space, with its angle from the vertical marked."""
    return VGroup(space_dial(c, th, r), Arc(radius=0.75, start_angle=PI / 2, angle=-th, arc_center=P(*c), color=INK, stroke_width=3),
                  mt(r"\theta", size=40).move_to(P(*c) + 1.05 * uvec(PI / 2 - th / 2)))


@slide("That holds for every angle, not only this one.", "Any tilt")
def tilt1(s):
    yield [FadeIn(at(lab("that holds for every angle, not only this one", 26, INK), 0, 2.4))]
    yield [FadeIn(tilt()), FadeIn(at(words("a spin tilted away from the vertical", 20, 24, INK, ORIGIN), -5.0, -2.6)),
           FadeIn(left_at(lab("chapter 2a's page works out its state", 24), -2.4, 1.2))]
    f = at(half_formula(72), 1.8, -0.2)
    yield [FadeIn(f), Create(frame(f, BLUE, 0.25, 2.5)), FadeIn(at(lab("the result, taken as given", 24), 1.8, -1.5))]


@slide("The amplitudes are the cosine and the sine of half the tilt.", "Half the tilt")
def tilt2(s):
    f = at(half_formula(72), 1.8, 1.3)
    s.add(tilt(), f)
    yield [f[2].animate.set_color(INK), f[5].animate.set_color(INK), FadeIn(at(lab("the cosine and the sine of half the tilt", 24, INK), 1.8, -0.05))]
    c = (0.6, -1.9)
    d = VGroup(state_dial(c, TH / 2, 1.3), Arc(radius=0.8, start_angle=0, angle=TH / 2, arc_center=P(*c), color=INK, stroke_width=3),
               mt(r"\theta/2", size=34).move_to(P(*c) + P(1.45, 0.25)))
    yield [FadeIn(d), FadeIn(left_at(words("so an angle in space shows up as half that angle in the state", 22, 26, INK, bold=True), 2.6, -1.9))]


def swept(c, th, r):
    """The angle a tilting spin has gone through, as an arc from the vertical."""
    return Arc(radius=r, start_angle=PI / 2, angle=-max(th, 0.02), arc_center=P(*c), color=MUTED, stroke_width=3)


@slide("Now carry the tilt once round.", "Once round")
def round1(s):
    th = ValueTracker(TH)
    c = (-3.6, -0.4)
    s.add(th, always_redraw(lambda: VGroup(swept(c, th.get_value(), 0.8), space_dial(c, th.get_value(), 2.2))))
    yield [FadeIn(left_at(lab("now carry the tilt once round", 26, INK), 0.2, 1.6))]
    yield [th.animate.set_value(TAU), FadeIn(left_at(words("past down, all the way round, and back to up", 28, 26), 0.2, 0.2))]
    yield [FadeIn(left_at(mt(r"\theta = 360^\circ", size=72), 0.2, -1.6))]


@slide("Half of that is a hundred and eighty degrees.", "Half of a full turn")
def round2(s):
    s.add(at(half_formula(52), -3.4, 2.0), left_at(mt(r"\theta = 360^\circ", size=52), 0.6, 2.0))
    yield [FadeIn(at(mt(r"\frac{\theta}{2} = 180^\circ", size=64), 0, 0.5))]
    yield [FadeIn(at(mt(r"\cos 180^\circ = -1", size=52), -3.2, -0.9)), FadeIn(at(mt(r"\sin 180^\circ = 0", size=52), 3.2, -0.9))]
    r = at(mt(r"\bigl(\cos 180^\circ,\ \sin 180^\circ\bigr) =", r"(-1,\ 0)", size=60), 0, -2.5)
    r[1].set_color(BLUE)
    yield [FadeIn(r), Create(frame(r[1], BLUE, 0.15))]


TURN_X = (-3.4, 3.4)


def before_after(k, state=True):
    x = TURN_X[k]
    g = VGroup(at(lab(("at the start", "after one full turn")[k], 24, INK, True), x, 2.4), space_dial((x - 1.6, 0.6), 0.0, 1.1))
    if state:
        g.add(state_dial((x + 1.2, 0.6), PI * k, 1.1), at(pair_tex((r"(1,\ 0)", r"(-1,\ 0)")[k], 52), x + 1.2, -1.1))
    return g


@slide("So the spin points up, as it did at the start.", "Up again, with a minus sign")
def minus(s):
    yield [FadeIn(before_after(0, False)), FadeIn(before_after(1, False)), FadeIn(at(lab("the spin points up, as it did at the start", 24, PURPLE), -0.3, -2.1))]
    a, b = before_after(0), before_after(1)
    yield [FadeIn(VGroup(*a[2:])), FadeIn(VGroup(*b[2:])), FadeIn(at(T("but the state is minus what it was", 30, BLUE, True), 0, -3.0))]


@slide("A full turn in space is only a half turn in the state.", "A half turn in the state")
def halfturn(s):
    cs, cp = P(-4.6, 0.6), P(-0.6, 0.6)
    full = Arc(radius=1.2, start_angle=PI / 2, angle=-TAU + 0.25, arc_center=cs, color=PURPLE, stroke_width=5)
    full.add_tip(tip_length=0.22, tip_width=0.22)
    semi = Arc(radius=1.2, start_angle=0, angle=PI, arc_center=cp, color=BLUE, stroke_width=5)
    semi.add_tip(tip_length=0.22, tip_width=0.22)
    yield [Create(full), FadeIn(at(lab("in space", 24, PURPLE, True), cs[0], cs[1])), FadeIn(at(lab("a full turn", 24, PURPLE), cs[0], -1.1)),
           Create(semi), FadeIn(at(lab("in the state", 24, BLUE, True), cp[0], cp[1] + 0.4)), FadeIn(at(lab("only a half turn", 24, BLUE), cp[0], -1.1))]
    yield [FadeIn(left_at(lab("two full turns", 28, INK, True), 2.2, 1.3)), FadeIn(left_at(mt(r"720^\circ", size=64), 2.2, 0.4)),
           FadeIn(left_at(mix("bring the state back to", pair_tex(r"(1,\ 0)", 48), size=26), 2.2, -0.7))]


FIG_X = (-2.3, 0.4, 3.1, 5.8)
FIG = ((0, r"0^\circ", r"(1,\ 0)", "up"), (180, r"180^\circ", r"(0,\ 1)", "down"), (360, r"360^\circ", r"(-1,\ 0)", "up, with a minus sign"), (720, r"720^\circ", r"(1,\ 0)", "up"))
FIG_Y = (1.05, -1.0)    # the row of spins in space, the row of state arrows
LIVE_X = -5.6


def fig_col(k):
    deg, tex, pair, word = FIG[k]
    x = FIG_X[k]
    return VGroup(at(mix("tilted by", mt(tex, size=34), size=22), x, 2.4), space_dial((x, FIG_Y[0]), np.radians(deg), 0.7),
                  state_dial((x, FIG_Y[1]), np.radians(deg) / 2, 0.75), at(pair_tex(pair, 40), x, -2.25), at(lab(word, 22, INK), x, -2.8))


def fig_labels():
    return VGroup(at(lab("in space", 24, PURPLE, True), LIVE_X, 2.4), at(lab("in the state", 24, BLUE, True), LIVE_X, -2.25),
                  Line(P(-3.9, -3.0), P(-3.9, 2.6), color=LINE, stroke_width=2))


@slide("The figure on screen shows both.", "Half as fast")
def figure(s):
    gate = ValueTracker(0.0)
    t = gated_clock(s, gate)

    def live():
        th = (1.3 * t.get_value()) % (2 * TAU)
        return VGroup(space_dial((LIVE_X, FIG_Y[0]), th, 0.95), state_dial((LIVE_X, FIG_Y[1]), th / 2, 0.95))
    labels = fig_labels()
    s.add(always_redraw(live))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(labels), LaggedStart(*[FadeIn(fig_col(k)) for k in range(4)], lag_ratio=0.15)]
    yield [gate.animate.set_value(1.0), Indicate(labels[0], color=PURPLE, scale_factor=1.2)]
    yield [Indicate(labels[1], color=BLUE, scale_factor=1.2), FadeIn(caption("The arrow for the state turns half as fast.", -3.5, INK, 26))]


@slide("The half comes from the size of the spin.", "Where the half comes from")
def whence(s):
    h = at(mt(r"\frac{\hbar}{2}", size=120, color=PURPLE), -4.8, 0.6)
    yield [FadeIn(h), Create(frame(h[0][-1], INK, 0.12, 3)), FadeIn(left_at(lab("the half comes from the size of the spin", 28, INK), -3.2, 1.5))]
    yield [FadeIn(left_at(lab("how much the state turns depends on the size of the spin", 26, INK), -3.2, 0.3))]
    f = at(mt(r"\frac{\text{spin}}{\hbar}", size=84), -2.2, -1.9)
    yield [FadeIn(f), FadeIn(left_at(words("the fraction of the turn the state makes", 24, 26, INK, bold=True), -0.8, -1.9))]


FR_Y = (1.1, -1.5)


def frac_row(k):
    y = FR_Y[k]
    name = lab("the electron", 26, INK, True) if k == 0 else mix("a whole", mt(r"\hbar", size=40), "of spin", size=26, bold=True)
    tex = (r"\frac{\hbar/2}{\hbar} = \frac{1}{2}", r"\frac{\hbar}{\hbar} = 1")[k]
    return VGroup(left_at(name, -6.8, y), at(mt(tex, size=60), -1.4, y))


def frac_dials(t, k):
    """A spin turning in space and, beside it, how far its state has turned. Only the electron's state is drawn as a list of two amplitudes."""
    def draw():
        a = 1.2 * t.get_value()
        g = VGroup(space_dial((2.2, FR_Y[k]), a, 0.85))
        if k == 0:
            g.add(state_dial((5.2, FR_Y[k]), a / 2, 0.85))
        else:
            c = P(5.2, FR_Y[k])
            g.add(Circle(radius=0.85, color=LINE, stroke_width=2.5).move_to(c), varrow(c, c + 0.85 * np.array([np.sin(a), np.cos(a), 0.0]), BLUE, 7, 0.22))
        return g
    return always_redraw(draw)


@slide("For the electron, it's one half.", "One half, or one")
def fractions(s):
    t = clock(s)
    heads = VGroup(at(lab("in space", 22, PURPLE, True), 2.2, 2.5), at(lab("in the state", 22, BLUE, True), 5.2, 2.5))
    s.add(frac_dials(t, 0))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(frac_row(0)), FadeIn(heads)]
    s.add(frac_dials(t, 1))  # added, not faded in
    yield [FadeIn(frac_row(1)), FadeIn(at(lab("turns by the whole angle", 22, BLUE), 5.2, FR_Y[1] - 1.15))]
    yield [FadeIn(caption("That particle's state comes back after a single turn.", -3.4, INK, 26))]


@slide("The minus sign doesn't show on one electron alone.", "No measurement shows it")
def noshow(s):
    yield [FadeIn(at(T("the minus sign doesn't show on one electron alone", 28, INK, True), 0, 2.3))]
    yield [FadeIn(space_dial((-5.6, 0.2), 0.0, 1.2)), FadeIn(space_dial((-3.6, 0.2), 0.0, 1.2)), GrowArrow(varrow(P(-5.1, 0.2), P(-4.1, 0.2))),
           FadeIn(at(words("after a full turn, the spin points where it did", 24, 24, INK, ORIGIN), -4.6, -2.0))]
    yield [FadeIn(left_at(words("so a measurement of its direction finds nothing new", 28, 26), -1.8, 0.6))]
    yield [FadeIn(left_at(mix(pair_tex(r"(1,\ 0)", 48), "and", pair_tex(r"(-1,\ 0)", 48), ": the same chances", size=26), -1.8, -1.2)),
           FadeIn(left_at(mix("multiplying a whole state by", mt("-1", size=40), "changes no chance", size=24, color=MUTED), -1.8, -2.2))]
    yield hold()


BS = dict(src=P(-6.6, -0.6), S=P(-4.6, -0.6), top=P(-2.2, 1.0), bot=P(-2.2, -2.2), R=P(0.2, -0.6), out=P(1.8, -0.6))


def beam(a, b):
    return Line(BS[a], BS[b], color=BLUE, stroke_width=5)


@slide("But a phase counts as soon as we add one state to another.", "The test")
def test1(s):
    yield [FadeIn(at(lab("a phase counts as soon as we add one state to another", 26, INK), 0, 2.4))]
    yield [FadeIn(left_at(T("so here's the test", 30, INK, True), 2.6, 0.9))]
    yield [Create(beam("src", "S")), Succession(Wait(0.3), AnimationGroup(Create(beam("S", "top")), Create(beam("S", "bot")))),
           FadeIn(left_at(lab("split a beam in two", 26, INK), 2.6, -0.3))]


def turn_mark():
    """A loop for one full turn, set above the upper path with a thin line down to it."""
    mid = (BS["S"] + BS["top"]) / 2
    c = mid + P(-0.9, 1.35)
    arc = Arc(radius=0.42, start_angle=PI / 2, angle=-TAU + 0.5, arc_center=c, color=PURPLE, stroke_width=4)
    arc.add_tip(tip_length=0.16, tip_width=0.16)
    edge = arc.get_center() + 0.5 * arc.width * uvec(-0.9)   # the point of the loop nearest the path
    return VGroup(arc, left_at(lab("a full turn", 22, PURPLE, True), arc.get_right()[0] + 0.25, arc.get_center()[1] + 0.3),
                  Line(edge + 0.08 * uvec(-0.9), mid + P(-0.08, 0.14), color=MUTED, stroke_width=2))


def phase_pair(x, y, cancel):
    """Two halves of the beam as arrows: head to tail when they add, opposite when they cancel."""
    a = P(x, y)
    if cancel:
        return VGroup(varrow(a, a + RIGHT * 1.0, BLUE, 6), varrow(a + P(1.0, -0.22), a + P(0.0, -0.22), BLUE, 6))
    return VGroup(varrow(a, a + RIGHT * 1.0, BLUE, 6), varrow(a + RIGHT * 1.0, a + RIGHT * 2.0, BLUE, 6))


@slide("Turn the spins in one half through a full turn, and leave the other half alone.", "Turn one half")
def test2(s):
    s.add(beam("src", "S"), beam("S", "top"), beam("S", "bot"))
    yield [FadeIn(turn_mark()), FadeIn(at(lab("left alone", 22), -4.4, -1.9))]
    yield [Create(beam("top", "R")), Create(beam("bot", "R")), Create(beam("R", "out")), FadeIn(at(lab("brought together", 22), 1.3, -0.15))]
    yield [FadeIn(left_at(lab("before: they added", 24, INK), 3.0, 2.4)), FadeIn(phase_pair(3.0, 1.85, False)),
           FadeIn(left_at(words("if the turned half comes back with a minus sign:", 24, 24), 3.0, 0.6)), FadeIn(phase_pair(3.0, -0.35, True)),
           FadeIn(left_at(lab("they cancel", 26, INK, True), 3.0, -1.2))]


@slide("In nineteen seventy-five, two groups did this.", "Two groups, 1975")
def groups(s):
    yield [FadeIn(at(T("1975: two groups did this", 32, INK, True), 0, 2.1))]
    yield [FadeIn(at(card("Helmut Rauch\nfrom Vienna", 5.2, 1.7, INK, 28), -3.4, 0.0), shift=DOWN * 0.15)]
    yield [FadeIn(at(card("Samuel Werner\nin the United States", 5.2, 1.7, INK, 28), 3.4, 0.0), shift=DOWN * 0.15)]


def neutron(c, ang, r=0.3):
    c = P(*c)
    return VGroup(varrow(c - 0.75 * uvec(ang), c + 0.75 * uvec(ang), PURPLE, 6, 0.2), Circle(radius=r, color=INK, stroke_width=3, fill_color=LINE, fill_opacity=1).move_to(c))


@slide("They used neutrons, which have spin one half like the electron.", "Neutrons")
def neutrons(s):
    t = clock(s)
    yield [FadeIn(neutron((-5.6, 1.4), PI / 2)), FadeIn(left_at(lab("neutrons: spin one half, like the electron", 26, INK), -4.6, 1.4))]
    yield [FadeIn(left_at(T("no charge", 28, INK, True), 2.6, 1.4))]
    zone = VGroup(Rectangle(width=6.0, height=2.2, stroke_color=MUTED, stroke_width=2.5, fill_color=PALE, fill_opacity=1).move_to(P(0.5, -1.5)),
                  at(lab("magnetic field", 22), 0.5, -0.65), Line(P(-6.6, -1.6), P(6.6, -1.6), color=LINE, stroke_width=3))

    def fly():
        x = -6.0 + (2.0 * t.get_value()) % 12.0
        inside = min(max(x + 2.5, 0.0), 6.0)
        return neutron((x, -1.6), PI / 2 - 1.3 * inside, 0.26)
    s.add(zone, always_redraw(fly))  # added, not faded in: a redrawn object changes shape between frames
    yield [FadeIn(caption("A magnetic field turns its spin without bending its path.", -3.3, INK, 26))]


N_SRC, N_S, N_TOP, N_BOT, N_R, N_DET = P(-7.0, -0.4), P(-5.6, -0.4), P(-3.6, 1.2), P(-3.6, -2.0), P(-1.6, -0.4), P(-0.4, -0.4)


def n_line(a, b):
    return Line(a, b, color=BLUE, stroke_width=4)


def n_beams():
    return [n_line(N_SRC, N_S), VGroup(n_line(N_S, N_TOP), n_line(N_S, N_BOT)), VGroup(n_line(N_TOP, N_R), n_line(N_BOT, N_R)),
            Arrow(N_R, N_DET, buff=0, color=BLUE, stroke_width=4, max_tip_length_to_length_ratio=0.25)]


def n_plates():
    return VGroup(*[Line(p + P(0, -0.45), p + P(0, 0.45), color=INK, stroke_width=7) for p in (N_S, N_R)],
                  Line(N_TOP + P(-0.5, 0.02), N_TOP + P(0.5, 0.02), color=INK, stroke_width=7), Line(N_BOT + P(-0.5, -0.02), N_BOT + P(0.5, -0.02), color=INK, stroke_width=7))


def n_magnet():
    return Rectangle(width=1.0, height=0.75, stroke_color=MUTED, stroke_width=3, fill_color=LINE, fill_opacity=0.6).rotate(np.arctan2(1.6, 2.0)).move_to((N_S + N_TOP) / 2)


def n_counter():
    return VGroup(Rectangle(width=0.5, height=0.9, color=INK, fill_color=INK, fill_opacity=1).move_to(N_DET + P(0.25, 0)), at(lab("counter", 22), N_DET[0] + 0.3, N_DET[1] - 0.8),
                  at(lab("neutrons", 22), N_SRC[0] + 0.55, N_SRC[1] + 0.4))


def n_setup():
    return VGroup(*n_beams(), n_plates(), n_magnet(), n_counter())


def n_magnet_label():
    m = (N_S + N_TOP) / 2
    return VGroup(lab("magnet: turns", 22, INK, True), lab("the spin", 22, INK, True)).arrange(DOWN, buff=0.08).move_to(P(m[0] - 1.5, m[1] + 1.15))


def n_text(text, y, color=INK, bold=False, chars=28, size=26):
    return left_at(words(text, chars, size, color, bold=bold), 1.3, y)


@slide("The setup is on screen.", "The neutron experiment")
def setup1(s):
    b = n_beams()
    yield [FadeIn(n_plates()), FadeIn(n_counter()), Succession(Create(b[0]), Create(b[1]), Create(b[2]), GrowArrow(b[3])), FadeIn(n_magnet().set_z_index(-1)),
           FadeIn(n_text("the setup, sketched", 2.0, MUTED))]
    yield [FadeIn(n_text("a crystal of silicon split each neutron's wave onto two paths", 0.8))]
    yield [FadeIn(n_text("then it brought them together again, as the two slits did for an electron", -1.0))]


@slide("One path ran through a magnetic field.", "One path through a field")
def setup2(s):
    s.add(n_setup())
    yield [Create(frame(n_magnet(), INK, 0.12)), FadeIn(n_magnet_label()), FadeIn(n_text("one path ran through a magnetic field", 1.8)),
           FadeIn(at(VGroup(lab("this path is", 22), lab("left alone", 22)).arrange(DOWN, buff=0.08), -5.4, -2.2))]
    c = (2.6, -1.4)
    d = VGroup(space_dial(c, np.radians(130), 1.2), swept(c, np.radians(130), 0.6))
    yield [FadeIn(d), FadeIn(left_at(words("the field turned the spin, by an angle set by the field's strength", 22, 26), 3.9, -1.4))]


def n_axes():
    return Axes(x_range=[0, 720, 180], y_range=[0, 1.15, 1], x_length=5.6, y_length=2.9,
                axis_config={"color": MUTED, "stroke_width": 2, "include_tip": False}).move_to([4.2, -0.5, 0])


def n_count(d):
    return 0.5 * (1 + np.cos(np.radians(d) / 2))


def n_graph(ax):
    g = VGroup(ax, at(lab("count at the counter", 22, INK, True), 4.2, 1.45), at(lab("angle the spin was turned through", 22), 4.2, -2.85))
    for d, tex in ((0, r"0^\circ"), (360, r"360^\circ"), (720, r"720^\circ")):
        q = ax.c2p(d, 0)
        g.add(at(mt(tex, size=34), q[0], q[1] - 0.35))
    return g


@slide("As the field went up, the count of neutrons rose and fell.", "The count")
def count2(s):
    ax = n_axes()
    d = ValueTracker(1.0)

    def draw():
        v = d.get_value()
        return VGroup(ax.plot(n_count, x_range=[0, v, 3], color=INK, stroke_width=5), Dot(ax.c2p(v, n_count(v)), radius=0.1, color=INK))
    s.add(n_setup(), n_magnet_label(), n_graph(ax), d, always_redraw(draw))  # the curve is added, not faded in: it changes shape between frames
    yield [d.animate.set_value(250.0)]
    q = ax.c2p(360, 0)
    yield [d.animate.set_value(360.0), FadeIn(at(lab("the two paths cancel", 22, INK, True), 4.2, 0.3)), Create(Line(P(4.2, 0.05), q + P(0, 0.15), color=INK, stroke_width=2))]
    yield [d.animate.set_value(720.0), FadeIn(caption("The count came back only at 720°.", -3.55, INK, 26))]


@slide("One last point ties this to the Dirac equation.", "Back to the column")
def tie(s):
    c = at(col4m(72, 1.05), -4.4, -0.3)
    yield [FadeIn(c), FadeIn(at(lab("one last point ties this to the Dirac equation", 26, INK), 0, 2.4))]
    yield [FadeIn(pair_brace(c, True, "a list of two amplitudes")), FadeIn(pair_brace(c, False, "a list of two amplitudes"))]
    yield [FadeIn(left_at(words("so the column's entries turn at half the angle too", 22, 26, INK, bold=True), 2.6, -0.3))]


@slide("Physicists call a column like that a spinor.", "A spinor")
def spinor(s):
    c = at(col4m(56, 0.85), -5.0, 0.3)
    yield [FadeIn(c), FadeIn(left_at(T("spinor", 84, PURPLE, True), -3.2, 0.9)), FadeIn(left_at(lab("a column whose entries turn at half the angle", 26, INK), -3.2, -0.4))]
    yield [FadeIn(left_at(lab("chapter 2b said this minus sign would come back with spinors", 24, INK), -3.2, -1.6))]
    yield [FadeIn(left_at(T("this is where", 28, INK, True), -3.2, -2.5))]


# ================================================================== where we've got to
deck.part("Chapter six")

RECAP_Y = (1.9, 0.85, -0.2, -1.25, -2.3)
RECAP_DOT = (RED, PURPLE, PURPLE, INK, BLUE)


def recap_body(k):
    if k == 0:
        return lab("the angular momentum of a free electron's motion isn't kept", 26, INK)
    if k == 1:
        return mix("a matrix term of", mt(HB2, size=40, color=PURPLE), "repairs it, and that term is the spin", size=26)
    if k == 2:
        return lab("in each pair of the column: one spin up, the other spin down", 26, INK)
    if k == 3:
        return lab("the electron's magnet: twice a spinning charge's, as Stern and Gerlach measured", 26, INK)
    return mix("one full turn in space multiplies the state by", mt("-1", size=40), size=26)


def recap_row(k):
    return VGroup(Dot(P(-6.8, RECAP_Y[k]), radius=0.12, color=RECAP_DOT[k]), left_at(recap_body(k), -6.45, RECAP_Y[k]))


@slide("Here's where we've got to.", "Where we've got to")
def recap1(s):
    yield [FadeIn(recap_row(0), shift=RIGHT * 0.15)]
    yield [FadeIn(recap_row(1), shift=RIGHT * 0.15)]


@slide("In each pair of the column, one wave function is spin up", "Where we've got to")
def recap2(s):
    s.add(recap_row(0), recap_row(1))
    yield [FadeIn(recap_row(2), shift=RIGHT * 0.15)]
    yield [FadeIn(recap_row(3), shift=RIGHT * 0.15)]
    yield [FadeIn(recap_row(4), shift=RIGHT * 0.15)]


@slide("The electron has stayed at rest, or slow, through all of this.", "Next: fields")
def nxt(s):
    e = espin(-4.6, 0.8, True, 1.6, 0.2)
    yield [FadeIn(e), FadeIn(at(lab("at rest, or slow, through all of this", 24, INK), -4.6, -0.5))]
    yield [FadeIn(at(T("that was enough", 30, INK, True), 2.4, 1.0)),
           FadeIn(at(lab("the particles in these experiments\nmove far slower than light", 26, INK), 2.4, 0.1))]
    yield [FadeIn(at(lab("next: what the two negative-energy wave functions describe", 26, LOW, True), 0, -2.2))]

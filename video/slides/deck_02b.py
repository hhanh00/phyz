"""Slides for chapter two, part B, First Quantization.

Every value comes from video/scripts/02b-first-quantization.txt or
docs/first-quantization.md. The narration does not read formulas aloud, so each
formula is shown at the sentence that states it in words, in the page's
notation. Formulas are set with MathTex (LaTeX), with the state names inside
brackets upright. The two figures follow docs/manim/page_diagrams.py (WaveSum,
SpinPrecession), with the same geometry. The helpers, state chips, amplitude
lists, phasors and magnet boxes come from deck_02a.py, and the operator pipes,
the result chart, the bell curves and the electron and ball slides are carried
over from the old, unsplit chapter 2 deck (deck_02.py, removed; see git history).

Colors, as in deck_02a: BLUE for states and amplitudes (state chips, kets, the
arrows that draw complex numbers, wave functions) and for the particles that
carry them, TEAL for chances and for checks that pass, ORANGE for the step or
quantity under discussion (a sign, an extra term, a spread, the angle between
two arrows, sound) and for the sideways magnet, PURPLE for Planck's constant
and for the operators, commutators and equations built with it, RED only for an
expectation or a supposed state that fails, MUTED and LINE for chapter 1's
classical side, apparatus, context and connectors.
"""
import re

from manim import *

from engine import *

STEM = "02b-first-quantization"
deck = Deck(f"scripts/{STEM}.txt")
slide = deck.slide


# ------------------------------------------------------------------ small helpers (from deck_02a)

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


def mt(*tex, size=44, color=INK):
    """A formula in LaTeX. Several strings give parts that can be colored or revealed one by one."""
    return MathTex(*tex, color=color, font_size=size)


def ket(name):
    """A state in bracket notation, with its name upright."""
    return r"\lvert\text{%s}\rangle" % name


KU, KD, KR, KL = ket("up"), ket("down"), ket("right"), ket("left")


def mix(*items, size=24, color=INK, buff=0.16, bold=False):
    """Words and formulas on one line."""
    return VGroup(*[T(i, size, color, bold) if isinstance(i, str) else i for i in items]).arrange(RIGHT, buff=buff)


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


def schip(name, size=24):
    """A state, such as the up state, as a text chip."""
    return chip(name, BLUE, size=size)


def ring(mob, color=ORANGE, buff=0.16):
    """Mark a bare plus or minus sign with a soft disc behind it.

    An underline would turn it into = or ±, and an outlined ring would turn it into the symbols ⊖ or ⊕.
    """
    return Circle(radius=max(mob.width, mob.height) / 2 + buff, stroke_width=0, fill_color=color, fill_opacity=0.2).move_to(mob)


def underline(mob, color=ORANGE):
    """Underline a number, a symbol or a state. Never a bare plus or minus sign: use ring()."""
    return Line(mob.get_corner(DL) + DOWN * 0.1 + LEFT * 0.04, mob.get_corner(DR) + DOWN * 0.1 + RIGHT * 0.04, color=color, stroke_width=5)


def opbox(tex, x, y, w=1.2, h=0.9, size=40, color=PURPLE):
    """An operator as a box that a state passes through."""
    box = card(None, w, h, color)[0]
    return at(VGroup(box, mt(tex, size=size, color=color).move_to(box)), x, y)


def op_eq(op, name, val, size=44):
    """An operator on one of its eigenstates, such as Z-hat on up."""
    m = mt(r"\hat %s" % op, ket(name), "=", val + r"\,", ket(name), size=size)
    m[0].set_color(PURPLE)
    m[1].set_color(BLUE)
    m[4].set_color(BLUE)
    return m


def note_to(text, mob, x, y, color=INK, size=22, chars=40):
    """A note at (x, y) with a thin arrow up to the part of a formula it explains."""
    t = at(words(text, chars, size, color, ORIGIN), x, y)
    return VGroup(t, Arrow(t.get_top() + UP * 0.05, mob.get_bottom() + DOWN * 0.08, buff=0, color=color, stroke_width=3, tip_length=0.13))


XS = np.linspace(-5.8, 5.8, 15)


def amp_row_line(y, angs, lens, r=0.4, color=BLUE, xs=XS):
    return VGroup(*[phasor([x, y], a, l, r=r, color=color, ring=False, width=4) if l > 0.08 else Dot([x, y, 0], radius=0.05, color=color)
                    for x, a, l in zip(xs, angs, lens)])


def turn_row(y, lam, x0=-5.0, x1=6.4, step=0.35, r=0.28):
    """A wave of definite momentum: arrows of one length, turning steadily along the line."""
    xs = np.arange(x0, x1 + 0.01, step)
    return VGroup(*[phasor([x, y], 2 * PI * (x - x0) / lam + PI / 2, 1.0, r=r, ring=False, width=4) for x in xs])


def x_axis(y, x0=-6.6, x1=6.6, name="position"):
    ax = Arrow([x0, y, 0], [x1, y, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.18)
    return VGroup(ax, lab(name, 22).next_to(ax.get_end(), DOWN, buff=0.12).shift(LEFT * 0.6))


def spike(x, y, h=2.2, color=BLUE):
    """A wave function squeezed onto one point."""
    pts_ = [[x - 0.7, y, 0], [x - 0.08, y, 0], [x, y + h, 0], [x + 0.08, y, 0], [x + 0.7, y, 0]]
    return VMobject(color=color, stroke_width=5).set_points_as_corners(pts_)


# ================================================================== opening
deck.part("Chapter two, part B")


@slide("Chapter two, part B.", "First Quantization")
def opening(s):
    c1 = at(card("Chapter 2a\nQuantum Ideas", 5.0, 1.6, MUTED, 30), -4.0, 0.3)
    yield [FadeIn(c1)]
    c2 = at(card("Chapter 2b\nFirst Quantization", 5.0, 1.6, INK, 30), 4.0, 0.3)
    yield [GrowArrow(arrow(c1, c2)), FadeIn(c2)]


# ================================================================== previously
deck.part("Previously")


@slide("The last chapter gave the rules of quantum mechanics in words.", "The rules, in words")
def prev1(s):
    yield [FadeIn(at(lab("the last chapter: the rules of quantum mechanics, in words", 26, INK), 0, 2.2))]
    lst = place(alist([ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)], ["up", "down"], rowh=0.72), -4.6, 0.5)
    yield [FadeIn(lst), FadeIn(at(words("a state is a list of amplitudes", 18, 24, BLUE, ORIGIN), -4.9, -1.0))]
    yield [FadeIn(vmag(-0.4, 0.5)), FadeIn(two_out(0.55, 0.5, "up", "down")),
           FadeIn(at(words("a measurement collapses it", 18, 24, ORANGE, ORIGIN), 0.0, -1.0)),
           FadeIn(bars(4.6, 0.0, [0.36, 0.64], ["up", "down"], ["0.36", "0.64"], hmax=1.4, w=0.7, gap=1.2)),
           FadeIn(at(words("the Born rule gives the chances", 18, 24, TEAL, ORIGIN), 5.2, -1.0))]
    yield [FadeIn(at(pill("this chapter: maths we can calculate with", INK, 26), 0, -2.7))]


@slide("It also keeps two promises from chapter one.", "Two promises from chapter 1")
def prev2(s):
    yield [FadeIn(at(lab("two promises from chapter 1", 26, INK), 0, 2.2))]
    a = at(card("the Hamiltonian", 5.0, 1.0, MUTED, 28), -3.8, 0.9)
    b = at(card("keeps its job: moving the state\nforward in time", 6.2, 1.3, PURPLE, 26), 3.6, 0.9)
    yield [FadeIn(a), GrowArrow(arrow(a, b)), FadeIn(b)]
    c = at(card("the Poisson bracket of\nposition with momentum", 5.0, 1.3, MUTED, 26), -3.8, -1.2)
    d = at(card("gets a quantum version", 6.2, 1.0, PURPLE, 26), 3.6, -1.2)
    yield [FadeIn(c), GrowArrow(arrow(c, d)), FadeIn(d)]


# ================================================================== where we end up
deck.part("Chapter two, part B")

GL = [("a measurable quantity", "a number", "an operator"),
      ("the bracket", "the Poisson bracket", "a commutator"),
      ("what moves the state", "Hamilton's equations,\nfrom the Hamiltonian", "the Schrödinger equation,\nfrom the same Hamiltonian")]
GL_Y = [0.8, -0.7, -2.2]


def gl_head():
    return VGroup(at(lab("chapter 1", 24, MUTED, True), -1.2, 2.0), at(lab("this chapter", 24, PURPLE, True), 4.8, 2.0))


def gl_row(k):
    a, b, c = GL[k]
    y = GL_Y[k]
    l = at(card(b, 4.0, 1.1, MUTED, 24), -1.2, y)
    r = at(card(c, 5.0, 1.1, PURPLE, 24), 4.8, y)
    return VGroup(left_at(lab(a, 24, INK), -7.1, y), l, arrow(l, r), r)


@slide("Here's where we'll end up.", "Where we'll end up")
def glance(s):
    yield [FadeIn(gl_head())]
    for k in range(3):
        yield [FadeIn(gl_row(k), shift=RIGHT * 0.15)]


@slide("Turning classical quantities into operators like this", "First quantization")
def first_q(s):
    a = at(card("classical quantities", 4.6, 1.0, MUTED, 28), -3.6, 1.5)
    b = at(card("operators", 3.4, 1.0, PURPLE, 28), 2.4, 1.5)
    yield [FadeIn(a), GrowArrow(arrow(a, b)), FadeIn(b), FadeIn(at(pill("first quantization", PURPLE, 28), 0, -0.1))]
    yield [FadeIn(at(lab("“first” because it comes first", 24, INK), 0, -0.95))]
    yield [FadeIn(at(card("this chapter:\nthe motion of particles", 5.4, 1.3, INK, 26), -3.4, -2.5))]
    yield [FadeIn(at(card("a later chapter:\nthe same, for fields", 5.4, 1.3, MUTED, 26), 3.4, -2.5))]


# ================================================================== operators
deck.part("Measured quantities become operators")


def vm_rig():
    return VGroup(vmag(-5.4, 0.6, 2.2), two_out(-4.3, 0.6, "up", "down"),
                  at(lab("the vertical magnet", 24, INK), -5.0, 1.75), at(lab("two results", 22, MUTED), -4.6, -0.75))


def cert_state(k):
    y = (1.15, 0.05)[k]
    name = ("up", "down")[k]
    return VGroup(at(schip(name, 28), -0.4, y), left_at(lab(f"always gives {name}", 24, INK), 0.6, y))


@slide("Measured quantities become operators.", "The vertical magnet")
def op1(s):
    yield hold()
    rig = vm_rig()
    yield [FadeIn(rig[0]), FadeIn(rig[2])]
    yield [FadeIn(rig[1]), FadeIn(rig[3])]


@slide("Each result has a state that gives it for certain.", "A certain state for each result")
def op2(s):
    s.add(vm_rig())
    yield [FadeIn(at(lab("for each result: a state that gives it for certain", 24, BLUE), 2.0, 2.2))]
    yield [FadeIn(cert_state(0)), FadeIn(cert_state(1))]


def num_tag(k):
    y = (1.15, 0.05)[k]
    return VGroup(Arrow(P(4.0, y), P(4.9, y), buff=0, color=MUTED, stroke_width=4, tip_length=0.15),
                  at(mt(("+1", "-1")[k], size=52), 5.6, y))


@slide("To calculate with results, we give each one a number.", "A number for each result")
def op3(s):
    s.add(vm_rig(), cert_state(0), cert_state(1))
    yield [FadeIn(at(lab("to calculate with results: a number for each one", 24, INK), 2.6, 2.2))]
    yield [FadeIn(num_tag(0)), FadeIn(num_tag(1))]
    yield [FadeIn(at(pill("these numbers are our choice of units", ORANGE, 26), 2.6, -1.6))]


UN_X = -5.6
UN_Y = (1.3, -0.9)


def un_axis():
    ax = Arrow(P(UN_X, -2.1), P(UN_X, 2.5), buff=0, color=MUTED, stroke_width=3, tip_length=0.18)
    spots = VGroup(*[Dot(P(UN_X, y), radius=0.15, color=BLUE) for y in UN_Y])
    names = VGroup(right_at(lab("up", 24, INK), UN_X - 0.3, UN_Y[0]), right_at(lab("down", 24, INK), UN_X - 0.3, UN_Y[1]))
    return VGroup(ax, spots, names, at(words("the amount of spin along the magnet", 20, 22, MUTED, ORIGIN), UN_X + 0.4, -2.9))


def un_scale(x, head, vals, color):
    g = VGroup(Line(P(x, -1.8), P(x, 2.0), color=color, stroke_width=3), at(lab(head, 24, color, True), x + 0.5, 2.4))
    for y, v in zip(UN_Y, vals):
        g.add(Line(P(x - 0.15, y), P(x + 0.15, y), color=color, stroke_width=3),
              left_at(lab(v, 22, color) if isinstance(v, str) else v, x + 0.3, y))
    return g


def un_links(x):
    return VGroup(*[DashedLine(P(UN_X + 0.25, y), P(x - 0.2, y), color=LINE, stroke_width=2) for y in UN_Y])


@slide("The magnet measures the amount of spin along it.", "A choice of units")
def op4(s):
    yield [FadeIn(un_axis())]
    yield [Create(un_links(-2.6)), FadeIn(un_scale(-2.6, "our units", [mt("+1", size=48), mt("-1", size=48)], INK))]
    yield [FadeIn(un_scale(0.4, "other units", ["another number", "another number"], MUTED))]
    st = VGroup(at(schip("up", 28), 5.2, UN_Y[0]), at(schip("down", 28), 5.2, UN_Y[1]))
    yield [FadeIn(st), FadeIn(at(words("the up and down states don't depend on that choice", 22, 22, BLUE, ORIGIN), 5.2, 0.2))]


def rule_pipe():
    a = at(chip("a state", BLUE, size=24), -3.4, 1.9)
    box = opbox(r"\hat Z", 0, 1.9, 1.4, 1.0, 48)
    b = at(chip("a state", BLUE, size=24), 3.4, 1.9)
    return VGroup(box, a, arrow(a, box), arrow(box, b), b)


def z_rows(size=48):
    a = at(op_eq("Z", "up", "+1", size), -3.2, 0.1)
    b = at(op_eq("Z", "down", "-1", size), -3.2, -1.3)
    return a, b


@slide("Now pack those numbers and states into one rule.", "One rule")
def op5(s):
    p = rule_pipe()
    yield [FadeIn(p[0]), FadeIn(at(mix(mt(r"\hat Z", size=44, color=PURPLE), ": our name for the rule; the hat marks a rule acting on states", size=22, color=PURPLE), 0, 1.05))]
    yield [FadeIn(p[1:]), FadeIn(at(lab("takes a state", 22), -3.4, 2.5)), FadeIn(at(lab("returns a state", 22), 3.4, 2.5))]
    a, b = z_rows()
    yield [FadeIn(a), FadeIn(left_at(lab("multiplies by +1: leaves the up state alone", 24, INK), 0.2, 0.1))]
    yield [FadeIn(b), FadeIn(left_at(lab("multiplies by −1: flips the sign", 24, INK), 0.2, -1.3))]


MIX_ROWS = [(r"\hat Z\big(c_0\," + KU + r" + c_1\," + KD + r"\big)", r"c_0\,\hat Z" + KU + r" + c_1\,\hat Z" + KD),
            (None, r"c_0\,(+1)\," + KU + r" + c_1\,(-1)\," + KD),
            (None, r"c_0\," + KU + r" - c_1\," + KD)]


def mix_line(k, size=40):
    lhs, rhs = MIX_ROWS[k]
    m = mt(lhs, "=", rhs, size=size) if lhs else mt("=", rhs, size=size)
    sign = m[1] if lhs else m[0]
    m.shift(P(-1.3, 1.6 - 1.15 * k) - sign.get_center())
    return m


@slide("On a mix of up and down, it treats each part separately.", "On a mix of up and down")
def op6(s):
    yield [FadeIn(mix_line(0)), FadeIn(at(lab("each part separately", 22, ORANGE), 2.0, 2.3))]
    yield [FadeIn(mix_line(1))]
    yield [FadeIn(mix_line(2)), FadeIn(left_at(words("the up part keeps its amplitude, and the down part gets a minus sign", 40, 24, INK), -1.0, -1.8)),
           FadeIn(left_at(mix(mt("c_0", size=40, color=BLUE), "and", mt("c_1", size=40, color=BLUE), ": the two amplitudes", size=22, color=BLUE), -1.0, -2.9))]


@slide("So this one rule holds everything about the vertical magnet.", "One rule holds the whole magnet")
def op7(s):
    a, b = z_rows(52)
    a.shift(UP * 1.1)
    b.shift(UP * 1.5)
    yield [FadeIn(a), FadeIn(b), FadeIn(at(vmag(4.4, 0.9, 2.2), 4.4, 0.9)), GrowArrow(arrow(P(0.2, 0.9), P(3.2, 0.9)))]
    yield [Create(underline(a[3])), Create(underline(b[3])), FadeIn(left_at(lab("the numbers its results give", 26, ORANGE, True), -6.0, -1.4)),
           Create(underline(a[4], BLUE)), Create(underline(b[4], BLUE)), FadeIn(left_at(lab("the state that gives each one", 26, BLUE, True), -6.0, -2.2))]


def eig_eq():
    return at(op_eq("Z", "up", "+1", 76), 0, 1.0)


def eig_tag(k):
    m = eig_eq()
    if k == 0:
        return VGroup(right_at(pill("an operator", PURPLE, 26), m[0].get_x() + 0.6, 2.3),
                      left_at(lab("every measurable quantity has one", 24, INK), m[0].get_x() + 0.9, 2.3))
    if k == 1:
        t = left_at(mix(T("eigenstate:", 26, BLUE, True), "a state it only multiplies"), m[4].get_x() - 1.0, -0.6)
        return VGroup(t, Arrow(P(m[4].get_x(), -0.3), m[4].get_bottom() + DOWN * 0.08, buff=0, color=BLUE, stroke_width=3, tip_length=0.13))
    t = right_at(mix(T("eigenvalue:", 26, ORANGE, True), "the number it multiplies by"), m[3].get_x() + 0.5, -1.6)
    return VGroup(t, Arrow(P(m[3].get_x(), -1.3), m[3].get_bottom() + DOWN * 0.08, buff=0, color=ORANGE, stroke_width=3, tip_length=0.13))


@slide("A rule like this is called an operator", "Operators, eigenstates, eigenvalues")
def op8(s):
    yield [FadeIn(eig_eq()), FadeIn(eig_tag(0))]
    yield [FadeIn(eig_tag(1))]
    yield [FadeIn(eig_tag(2))]


@slide("Eigen is German for own.", "Operators, eigenstates, eigenvalues")
def op9(s):
    s.add(eig_eq(), *[eig_tag(k) for k in range(3)])
    yield [FadeIn(at(lab("eigen: German for “own”", 26, INK, True), 0, -2.6))]
    yield [FadeIn(at(lab("the quantity's own states and its own numbers", 26, INK), 0, -3.3))]


@slide("An eigenvalue is a result you could read off a measuring device.", "Eigenvalues are real, amplitudes are complex")
def op10(s):
    ln = Arrow(P(-6.8, 0.3), P(-1.0, 0.3), buff=0, color=MUTED, stroke_width=3, tip_length=0.18)
    marks = VGroup(*[VGroup(Dot(P(x, 0.3), radius=0.13, color=INK), mt(t, size=44).move_to([x, -0.35, 0])) for x, t in ((-5.4, "-1"), (-2.6, "+1"))])
    yield [FadeIn(ln), FadeIn(marks), FadeIn(at(lab("an eigenvalue: a result read off a measuring device", 22, INK), -3.9, 1.6))]
    yield [FadeIn(at(T("always an ordinary real number", 26, INK, True), -3.9, -1.4))]
    c = P(4.0, 0.3)
    ring = VGroup(Circle(radius=1.4, color=LINE, stroke_width=2).move_to(c), DashedLine(c + LEFT * 1.7, c + RIGHT * 1.7, color=LINE, stroke_width=2),
                  DashedLine(c + DOWN * 1.7, c + UP * 1.7, color=LINE, stroke_width=2), varrow(c, c + 1.15 * uvec(np.radians(50))))
    yield [FadeIn(ring), FadeIn(at(T("only the amplitudes are complex", 26, BLUE, True), 4.0, -1.9))]
    yield [FadeIn(at(lab("here the maths has to touch what we actually observe", 24, MUTED), 0, -3.2))]


def spin_op(k, stage):
    x = (-3.8, 3.8)[k]
    op, names, color = (("Z", ("up", "down"), INK), ("S", ("right", "left"), ORANGE))[k]
    g = VGroup(magnet(("vertical", "sideways")[k], x - 1.4, 1.7, 2.0, color=color), at(mt(r"\hat %s" % op, size=60, color=PURPLE), x + 0.8, 1.7),
               at(lab(("the vertical operator", "its own operator")[k], 24, PURPLE, True), x, 0.75))
    if stage >= 1:
        g.add(at(op_eq(op, names[0], "+1", 42), x, -0.4), at(op_eq(op, names[1], "-1", 42), x, -1.4),
              at(lab(f"eigenstates: {names[0]} and {names[1]}", 22, BLUE), x, -2.4))
    return g


@slide("We'll call this first one the vertical operator.", "Two operators for the spin")
def op11(s):
    yield [FadeIn(spin_op(0, 1))]
    yield [FadeIn(spin_op(1, 0))]
    yield [FadeIn(spin_op(1, 1)[3:]), FadeIn(at(lab("eigenvalues: +1 and −1", 22, ORANGE), 3.8, -2.9))]


def nm_paper():
    a = place(alist([ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)], ["up", "down"], rowh=0.78), -5.9, 0.3)
    b = place(alist([ph(40, 0.6, 0.3), ph(300, 0.8, 0.3)], rowh=0.78), -2.0, 0.3)
    return VGroup(at(T("applying an operator: a calculation on paper", 24, PURPLE, True), -3.9, 1.9), a, slot_arrow(P(-5.25, 0.3), P(-4.75, 0.3)),
                  opbox(r"\hat Z", -4.0, 0.3), slot_arrow(P(-3.25, 0.3), P(-2.65, 0.3)), b)


def nm_notes():
    return VGroup(at(lab("doesn't pick a result", 24, INK), -3.9, -1.1), at(lab("doesn't collapse the state", 24, INK), -3.9, -1.65))


def nm_lab():
    a = place(alist([ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)], ["up", "down"], rowh=0.78), 2.0, 0.3)
    b = place(alist(["1", "0"], rowh=0.78), 6.6, 0.3)
    return VGroup(at(T("a measurement: as the last chapter said", 24, ORANGE, True), 4.1, 1.9), a, slot_arrow(P(2.65, 0.3), P(3.15, 0.3)), vmag(4.2, 0.3, 1.9),
                  Arrow(P(5.25, 0.3), P(6.1, 0.3), buff=0, color=ORANGE, stroke_width=5, tip_length=0.18), b,
                  at(lab("gives one result, with a chance", 24, INK), 4.1, -1.1), at(lab("collapses the state", 24, INK), 4.1, -1.65))


@slide("One warning before we go on.", "Applying an operator is not a measurement")
def op12(s):
    yield hold()
    yield [FadeIn(nm_paper())]
    yield [FadeIn(nm_notes())]
    yield [FadeIn(nm_lab()), Create(Line(P(0.2, -2.0), P(0.2, 2.2), color=LINE, stroke_width=2))]


@slide("Operators are for calculating.", "What operators are for")
def op13(s):
    yield [FadeIn(at(T("operators are for calculating", 30, PURPLE, True), 0, 2.0))]
    yield [FadeIn(at(card("the quantum version\nof the bracket", 5.6, 1.6, PURPLE, 28), -3.4, 0.0), shift=UP * 0.15),
           FadeIn(at(card("averages, straight\nfrom the amplitudes", 5.6, 1.6, PURPLE, 28), 3.4, 0.0), shift=UP * 0.15)]


# ================================================================== order matters
deck.part("Order matters")


@slide("Order matters.", "Ordinary numbers")
def ord1(s):
    yield hold()
    yield [FadeIn(at(lab("ordinary numbers: the order of multiplying doesn't matter", 26, INK), 0, 1.6))]
    yield [FadeIn(at(mt(r"2 \times 3 = 3 \times 2", size=84), 0, 0.0))]


def pipe(ops, y, x0=-6.2):
    st = left_at(chip("a state", BLUE, size=24), x0, y)
    b1, b2 = opbox(ops[0], x0 + 3.2, y), opbox(ops[1], x0 + 5.4, y)
    return VGroup(st, arrow(st, b1), b1, arrow(b1, b2), b2)


def pipe_out(y, text, color=BLUE):
    return VGroup(Arrow(P(-0.1, y), P(0.8, y), buff=0, color=MUTED, stroke_width=4, tip_length=0.18), left_at(chip(text, color, size=24), 1.0, y))


@slide("With operators, the order can matter.", "Operators: the order can matter")
def ord2(s):
    yield [FadeIn(at(T("with operators, the order can matter", 28, PURPLE, True), 0, 2.2))]
    yield [FadeIn(pipe([r"\hat Z", r"\hat S"], 0.9)), FadeIn(left_at(lab("vertical, then sideways", 22), -6.2, 1.65)), FadeIn(pipe_out(0.9, "one state"))]
    yield [FadeIn(pipe([r"\hat S", r"\hat Z"], -1.3)), FadeIn(left_at(lab("sideways first", 22), -6.2, -0.55)),
           FadeIn(pipe_out(-1.3, "can be a different state", ORANGE))]


def comm_def(size=84):
    m = mt(r"[\hat A, \hat B]", "=", r"\hat A\hat B", "-", r"\hat B\hat A", size=size, color=PURPLE)
    return at(m, 0, 0.9)


@slide("The commutator measures that difference.", "The commutator")
def ord3(s):
    m = comm_def()
    yield [FadeIn(m[0]), FadeIn(at(pill("the commutator", PURPLE, 26), -4.6, 2.3)), FadeIn(at(lab("of two operators: it measures that difference", 24, INK), 0.6, 2.3))]
    yield [FadeIn(m[1:]), FadeIn(note_to("one order", m[2], m[2].get_x() - 0.7, -0.4)), FadeIn(note_to("the other order", m[4], m[4].get_x() + 0.9, -0.4)),
           FadeIn(lab("subtract", 22, ORANGE).next_to(m[3], UP, buff=0.85)),
           FadeIn(at(mix(mt(r"\hat A\hat B", size=44, color=PURPLE), ": apply", mt(r"\hat B", size=44, color=PURPLE), "first, then", mt(r"\hat A", size=44, color=PURPLE), size=22, color=MUTED), 0, -1.3))]
    yield [FadeIn(at(card("when the commutator is zero: the two operators commute", 11.0, 1.0, PURPLE, 28), 0, -2.6))]


def mult_pipe(a, b, y):
    st = left_at(schip("a shared eigenstate", 22), -6.6, y)
    b1 = at(card(f"× {a}", 1.2, 0.8, PURPLE, 26), -1.6, y)
    b2 = at(card(f"× {b}", 1.2, 0.8, PURPLE, 26), 0.6, y)
    res = left_at(mix(mt(a + b, size=44), "times the state"), 2.4, y)
    return VGroup(st, arrow(st, b1), b1, arrow(b1, b2), b2, arrow(b2, res), res)


@slide("Here's when that happens.", "Shared eigenstates")
def ord4(s):
    yield [FadeIn(at(lab("when is it zero?", 26, INK, True), 0, 2.3))]
    yield [FadeIn(at(lab("suppose two operators share all their eigenstates", 24, BLUE), 0, 1.6))]
    yield [FadeIn(mult_pipe("a", "b", 0.5)), FadeIn(mult_pipe("b", "a", -0.8)),
           FadeIn(at(lab("on each shared state, both just multiply by numbers, a and b", 22, INK), 0, -1.7))]
    yield [FadeIn(at(VGroup(mt("ab = ba", size=52), T("so the commutator is zero", 28, PURPLE, True)).arrange(RIGHT, buff=0.5), 0, -2.8))]


@slide("The magnets in a row show the other case.", "The other case")
def ord5(s):
    m1, m2 = vmag(-5.4, 1.5), smag(-1.6, 1.5)
    a = slot_arrow(P(-4.35, 1.5), P(-2.65, 1.5))
    yield [FadeIn(m1), FadeIn(a), FadeIn(lab("keep up", 22, INK).next_to(a, UP, buff=0.08)), FadeIn(m2)]
    yield [GrowArrow(slot_arrow(P(-0.55, 1.5), P(0.25, 1.5))), FadeIn(left_at(T("half right, half left", 28, TEAL, True), 0.45, 1.5))]
    yield [FadeIn(at(mix(mt(KU, size=48, color=BLUE), "is not an eigenstate of", mt(r"\hat S", size=48, color=PURPLE), size=26), 0, -0.3))]
    yield [FadeIn(at(card("no shared eigenstates: the order does matter", 9.6, 1.0, ORANGE, 28), 0, -2.0))]


def s_on_up(k, size=46):
    rows = [(KU, r"\tfrac{1}{\sqrt2}\big(", KR, "+", KL, r"\big)"), (r"\hat S" + KU, r"\tfrac{1}{\sqrt2}\big(", KR, "-", KL, r"\big)")]
    if k < 2:
        lhs, *rest = rows[k]
        m = mt(lhs, "=", *rest, size=size)
        m[0].set_color(BLUE if k == 0 else INK)
        m[3].set_color(BLUE)
        m[5].set_color(BLUE)
        if k == 1:
            m[4].set_color(ORANGE)
    else:
        m = mt("=", KD, size=size)
        m[1].set_color(BLUE)
    sign = m[1] if k < 2 else m[0]
    m.shift(P(-3.4, 1.7 - 1.3 * k) - sign.get_center())
    return m


@slide("Let's check that on the up state.", "The sideways operator on up")
def ord6(s):
    yield hold()
    a = s_on_up(0)
    yield [FadeIn(a), FadeIn(left_at(lab("up: an equal mix of right and left", 22, BLUE), 2.2, 1.7))]
    b = s_on_up(1)
    yield [FadeIn(b[:4]), FadeIn(b[5:]), FadeIn(left_at(lab("flips the sign of the left part", 22, ORANGE), 2.2, 0.4))]
    yield [FadeIn(ring(b[4])), FadeIn(b[4])]


@slide("The last chapter showed that right minus left is the down state.", "The sideways operator on up")
def ord7(s):
    b = s_on_up(1)
    s.add(s_on_up(0), ring(b[4]), b, left_at(lab("up: an equal mix of right and left", 22, BLUE), 2.2, 1.7),
          left_at(lab("flips the sign of the left part", 22, ORANGE), 2.2, 0.4))
    yield [FadeIn(s_on_up(2)), FadeIn(left_at(lab("right minus left: the down state (last chapter)", 22, BLUE), -0.9, -0.9))]
    r = mt(r"\hat S", KU, "=", KD, size=56)
    r[0].set_color(PURPLE)
    r[1].set_color(BLUE)
    r[3].set_color(BLUE)
    box = at(card(None, 12.6, 1.2, PURPLE), 0, -2.6)
    yield [FadeIn(box), FadeIn(at(VGroup(r, T("the sideways operator turns up into down", 24, INK)).arrange(RIGHT, buff=0.5), 0, -2.6))]


CH_X = [-5.6, -1.6, 2.4]
CH_B = [-3.6, 0.4]


def chain(y, ops, names):
    chips = [at(schip(n, 26), x, y) for n, x in zip(names, CH_X)]
    boxes = [opbox(o, x, y) for o, x in zip(ops, CH_B)]
    arrows_ = [arrow(chips[0], boxes[0]), arrow(boxes[0], chips[1]), arrow(chips[1], boxes[1]), arrow(boxes[1], chips[2])]
    return chips, boxes, arrows_


def chain_all(k):
    y = (1.2, -1.0)[k]
    chips, boxes, arrows_ = chain(y, ([r"\hat Z", r"\hat S"], [r"\hat S", r"\hat Z"])[k], (["up", "up", "down"], ["up", "down", "−down"])[k])
    head = left_at(lab(("vertical first, then sideways", "sideways first, then vertical")[k], 24, INK, True), -6.6, y + 0.85)
    return VGroup(head, *chips, *boxes, *arrows_)


@slide("Now try both orders.", "Both orders on up")
def ord8(s):
    yield hold()
    g = chain_all(0)
    yield [FadeIn(g[0]), FadeIn(g[1]), FadeIn(g[4]), FadeIn(g[6])]
    yield [FadeIn(g[2]), FadeIn(g[7]), FadeIn(g[8]), FadeIn(g[5]), FadeIn(g[9]), FadeIn(g[3]),
           FadeIn(left_at(words("stays up, then becomes down", 16, 22, MUTED), 4.3, 1.2))]


@slide("Now take sideways first, then vertical.", "Both orders on up")
def ord9(s):
    s.add(chain_all(0), left_at(words("stays up, then becomes down", 16, 22, MUTED), 4.3, 1.2))
    g = chain_all(1)
    yield [FadeIn(g[0]), FadeIn(g[1]), FadeIn(g[4]), FadeIn(g[6])]
    yield [FadeIn(g[2]), FadeIn(g[7]), FadeIn(g[8]), FadeIn(g[5]), FadeIn(g[9]), FadeIn(g[3]),
           FadeIn(left_at(words("becomes down, then minus down", 16, 22, MUTED), 4.3, -1.0))]
    yield [Indicate(g[3], color=ORANGE), FadeIn(at(T("the same two steps, and the results differ by a sign", 26, ORANGE, True), 0, -2.7))]


def sign_pic(k):
    x = (-5.0, -1.2)[k]
    name = mt((KD, "-" + KD)[k], size=52, color=BLUE)
    return VGroup(at(name, x, 2.0), phasor([x, 0.3], (0, PI)[k], 1.0, r=1.0, width=6), at(lab("its down amplitude", 22, BLUE), x, -1.0))


def sign_chance():
    return VGroup(*[at(lab("chance of down: 1", 22, TEAL, True), x, -1.55) for x in (-5.0, -1.2)],
                  left_at(words("measured on its own: the same chances", 22, 26, TEAL), 1.6, 1.2))


def sign_phase():
    return VGroup(Arc(radius=0.55, start_angle=0, angle=PI, arc_center=P(-1.2, 0.3), color=ORANGE, stroke_width=5),
                  left_at(words("but its phase is different, half a turn away", 22, 26, ORANGE), 1.6, -0.4))


@slide("That sign needs a comment.", "Down and minus down")
def ord10(s):
    yield [FadeIn(sign_pic(0)), FadeIn(sign_pic(1))]
    yield [FadeIn(sign_chance())]
    yield [FadeIn(sign_phase())]


@slide("And a phase counts as soon as one state is added to another", "Down and minus down")
def ord11(s):
    s.add(sign_pic(0), sign_pic(1), sign_chance(), sign_phase())
    yield [FadeIn(at(card("a phase counts as soon as one state is added to another, or subtracted from it", 13.4, 0.9, ORANGE, 26), 0, -2.5))]
    yield [FadeIn(at(pill("this minus sign comes back much later, with spinors", MUTED, 24), 0, -3.5))]


def comm_up(size=50):
    m = mt(r"[\hat Z, \hat S]\," + KU, "=", "-" + KD, "-", KD, "=", r"-2\," + KD, r"\neq 0", size=size)
    if m.width > 13.4:
        m.scale_to_fit_width(13.4)
    return at(m, 0, 0.9)


def comm_up_notes():
    m = comm_up()
    return (lab("sideways first", 22, ORANGE).next_to(m[2], DOWN, buff=0.35), lab("vertical first", 22, ORANGE).next_to(m[4], DOWN, buff=0.35),
            lab("subtract", 22, INK).next_to(m[3], UP, buff=0.45))


@slide("Here it shows at once, because the commutator subtracts", "The commutator on up")
def ord12(s):
    m = comm_up()
    n = comm_up_notes()
    yield [FadeIn(m[0]), FadeIn(m[1]), FadeIn(at(lab("the commutator subtracts the two results", 24, INK), 0, 2.3))]
    yield [FadeIn(m[2]), FadeIn(n[0])]
    yield [FadeIn(m[4]), FadeIn(n[1])]
    yield [FadeIn(m[3]), FadeIn(n[2])]


@slide("That leaves minus two times down.", "The commutator on up")
def ord13(s):
    m = comm_up()
    s.add(m[:5], *comm_up_notes(), at(lab("the commutator subtracts the two results", 24, INK), 0, 2.3))
    yield [FadeIn(m[5]), FadeIn(m[6])]
    yield [FadeIn(m[7])]
    yield [FadeIn(at(card("the vertical and sideways operators don't commute", 10.4, 1.0, PURPLE, 28), 0, -2.2))]


# ================================================================== position and momentum operators
deck.part("Position and momentum operators")

PX_Y = -1.6


@slide("Position and momentum operators.", "From the spin to position and momentum")
def pm1(s):
    yield hold()
    sp = VGroup(mt(r"\hat Z", size=60, color=PURPLE), mt(r"\hat S", size=60, color=PURPLE)).arrange(RIGHT, buff=0.8)
    yield [FadeIn(at(sp, -3.8, 0.6)), FadeIn(at(lab("so far: the spin's operators", 24, INK), -3.8, -0.4))]
    yield [GrowArrow(arrow(P(-1.4, 0.6), P(0.6, 0.6))), FadeIn(at(pill("position", BLUE, 28), 2.6, 1.0)), FadeIn(at(pill("momentum", BLUE, 28), 5.0, 1.0)),
           FadeIn(at(lab("now: operators for chapter 1's two quantities", 24, INK), 3.8, -0.4))]


def pos_dots():
    return VGroup(*[Dot(P(x, PX_Y), radius=0.09, color=INK) for x in np.arange(-5.6, 5.7, 0.8)])


@slide("Position comes first.", "The position operator")
def pm2(s):
    yield [FadeIn(x_axis(PX_Y)), FadeIn(at(pill("position first", BLUE, 26), -5.4, 2.2))]
    yield [FadeIn(pos_dots()), FadeIn(at(lab("a position measurement can give any position along the line", 24, INK), 0, 1.2))]
    yield [FadeIn(at(lab("an eigenvalue: what a measurement can show", 24, ORANGE), 0, 0.4))]
    yield [FadeIn(at(mix("so the eigenvalues of", mt(r"\hat x", size=52, color=PURPLE), "are the positions themselves", size=26, bold=True), 0, -0.5))]


def sq_state():
    return VGroup(spike(-2.0, PX_Y), Dot(P(-2.0, PX_Y), radius=0.1, color=ORANGE), lab("one point", 22, ORANGE).next_to(P(-2.0, PX_Y), DOWN, buff=0.2))


@slide("Its eigenstates are the states certain to be at one point.", "The position operator")
def pm3(s):
    s.add(x_axis(PX_Y))
    yield [FadeIn(at(lab("its eigenstates: certain to be at one point", 24, BLUE, True), 2.6, 2.0))]
    yield [FadeIn(sq_state()), FadeIn(at(lab("a wave function squeezed onto that point", 24, BLUE), 2.6, 1.2))]
    yield [FadeIn(at(mix(mt(r"\hat x", size=52, color=PURPLE), "has to multiply it by that point's position", size=24), 2.6, 0.2))]


def bump_row(y, r=0.42):
    return amp_row_line(y, 0.9 * XS, np.exp(-XS ** 2 / 12), r=r)


@slide("Here's an operator that does it.", "The position operator")
def pm4(s):
    yield [FadeIn(x_axis(PX_Y)), FadeIn(bump_row(PX_Y + 0.75)), FadeIn(at(lab("a wave function: an arrow at each point", 22, BLUE), -3.6, 0.2))]
    m = mt(r"\hat x", r"\,\psi(x)", "=", "x", r"\,\psi(x)", size=64)
    m[0].set_color(PURPLE)
    m[3].set_color(ORANGE)
    yield [FadeIn(at(m, 0, 1.8)), FadeIn(at(lab("at each point: multiply the wave function by that point's own position x", 24, INK), 0, -3.0))]


@slide("Now momentum.", "The momentum operator")
def pm5(s):
    yield [FadeIn(at(pill("now momentum", BLUE, 26), -5.3, 2.2))]
    q = mix(mt(r"\hat p", size=72, color=PURPLE), "just multiplies by the momentum?", size=30)
    yield [FadeIn(at(q, 0, 0.4)), FadeIn(at(lab("the way position does", 24, MUTED), 0, -0.6))]


def mom_row(y):
    xs = np.linspace(-5.8, 5.8, 15)
    return amp_row_line(y, -1.3 * xs + 0.5, np.exp(-(xs - 1.6) ** 2 / 5), r=0.42, xs=xs)


def two_lists(stage):
    g = VGroup(VGroup(), x_axis(0.0, name="position"), bump_row(0.75),
               left_at(lab("one state's amplitudes, listed by position: the wave function", 24, BLUE), -6.6, 2.0),
               x_axis(-2.8, name="momentum"), mom_row(-2.05), left_at(lab("the same state's amplitudes, listed by momentum", 24, BLUE), -6.6, -1.2))
    return g


@slide("That would be true if we listed the state's amplitudes by momentum.", "The same state, two lists")
def pm6(s):
    g = two_lists(0)
    yield [FadeIn(g), FadeIn(right_at(lab("here, momentum would just multiply", 22, PURPLE, True), 6.9, -1.2))]
    yield [Create(SurroundingRectangle(VGroup(g[1], g[2]), color=ORANGE, stroke_width=3, buff=0.12, corner_radius=0.1)),
           FadeIn(right_at(lab("but this is the list we have", 22, ORANGE, True), 6.9, 2.0))]
    yield [FadeIn(right_at(lab("our choice: the list the last chapter built", 22, ORANGE), 6.9, 1.5))]


@slide("An operator acts by plain multiplying on one kind of list only.", "Multiplying needs the operator's own list")
def pm7(s):
    yield [FadeIn(at(T("an operator acts by plain multiplying on one kind of list only", 28, INK, True), 0, 2.0))]
    yield [FadeIn(at(card("a list of its own eigenstates:\nit just multiplies", 6.4, 1.6, PURPLE, 28), -3.6, 0.0), shift=UP * 0.15)]
    yield [FadeIn(at(card("any other list:\nit has to do something else", 6.4, 1.6, ORANGE, 28), 3.6, 0.0), shift=UP * 0.15)]


def ud_list():
    return VGroup(place(alist([mt("c_0", size=44, color=BLUE), mt("c_1", size=44, color=BLUE)], ["up", "down"], rowh=0.75), -5.2, 0.0), at(lab("the up and down list", 24, BLUE), -5.4, 1.3))


def ud_branch(k):
    y = (1.2, -1.4)[k]
    box = opbox((r"\hat Z", r"\hat S")[k], -2.2, y)
    out = place(alist([mt(t, size=44, color=BLUE) for t in (["c_0", "-c_1"], ["c_1", "c_0"])[k]], ["up", "down"], rowh=0.75), 1.0, y)
    a = Arrow(P(-4.5, 0.0), box.get_left() + LEFT * 0.1, buff=0, color=MUTED, stroke_width=4, tip_length=0.18)
    return VGroup(a, box, slot_arrow(P(-1.5, y), P(-0.6, y), MUTED), out)


@slide("The spin showed this.", "The spin showed this")
def pm8(s):
    yield [FadeIn(ud_list())]
    yield [FadeIn(ud_branch(0)), FadeIn(left_at(words("the vertical operator multiplies", 20, 24, PURPLE), 2.3, 1.2))]
    yield [FadeIn(ud_branch(1)), FadeIn(left_at(words("the sideways operator turned up into down", 22, 24, INK), 2.3, -1.0))]
    yield [FadeIn(left_at(words("on this list, it swaps the two amplitudes", 22, 24, ORANGE), 2.3, -2.2))]


WH_X = [-0.4, 4.4]
WH_Y = [0.3, -1.6]


def wh_head():
    return VGroup(at(mt(r"\hat x", size=56, color=PURPLE), WH_X[0], 2.1), at(mt(r"\hat p", size=56, color=PURPLE), WH_X[1], 2.1),
                  at(lab("position operator", 22), WH_X[0], 1.45), at(lab("momentum operator", 22), WH_X[1], 1.45))


def wh_row(k):
    y = WH_Y[k]
    name = left_at(words(("the position list (the wave function)", "the momentum list")[k], 20, 24, BLUE), -7.0, y)
    mult = card("multiplies", 4.0, 1.2, PURPLE, 26)
    other = card("something else", 4.0, 1.2, ORANGE, 26)
    return VGroup(name, at(mult, WH_X[k], y), at(other, WH_X[1 - k], y))


@slide("Had we chosen the momentum list, the roles would swap.", "Which operator multiplies on which list")
def pm9(s):
    yield [FadeIn(wh_head()), FadeIn(wh_row(0))]
    yield [FadeIn(wh_row(1), shift=UP * 0.15), FadeIn(at(lab("had we chosen the momentum list, the roles would swap", 24, INK), 0, -3.0))]


def def_wave(y=0.3):
    return turn_row(y, 4.0, -6.0, 6.4, 0.5, 0.3)


@slide("So the question is what the momentum operator does to the position list.", "A wave of definite momentum")
def pm10(s):
    yield [FadeIn(at(mix("what does", mt(r"\hat p", size=52, color=PURPLE), "do to the position list?", size=26, bold=True), 0, 2.2))]
    yield [LaggedStart(*[FadeIn(a) for a in def_wave()], lag_ratio=0.03),
           FadeIn(at(lab("a state of definite momentum: a wave (last chapter)", 24, BLUE), 0, 1.25))]
    yield [GrowArrow(Arrow([-6.0, -0.45, 0], [6.4, -0.45, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.2)),
           FadeIn(at(lab("the arrow keeps its length and turns steadily along the line", 24, INK), 0, -1.0))]
    br = BraceBetweenPoints([-6.0, -1.5, 0], [-2.0, -1.5, 0], direction=DOWN, color=ORANGE)
    yield [FadeIn(br), FadeIn(left_at(mix("one full turn every wavelength:", mt(r"\frac{h}{p}", size=52, color=PURPLE), size=24, color=ORANGE), -6.2, -2.6)),
           FadeIn(left_at(lab("Planck's constant divided by the momentum", 22), 0.0, -2.6))]


def wave_f(size=72):
    """psi_p(x) = e^{ipx/hbar}; its glyphs run psi, p, (, x, ), =, e, i, p, x, /, hbar.

    The h-bar is MUTED until the narration names it.
    """
    m = at(mt(r"\psi_p(x) = e^{ipx/\hbar}", size=size, color=BLUE), -3.8, 1.5)
    m[0][11].set_color(MUTED)
    return m


def wf_arrow():
    c = P(3.6, 1.3)
    t = np.radians(50)
    return VGroup(Circle(radius=1.0, color=LINE, stroke_width=2).move_to(c), DashedLine(c, c + RIGHT * 1.0, color=MUTED, stroke_width=2),
                  varrow(c, c + uvec(t)), Arc(radius=0.45, start_angle=0, angle=t, arc_center=c, color=ORANGE, stroke_width=4),
                  mt(r"\theta", size=40, color=ORANGE).move_to(c + 0.72 * uvec(t / 2)),
                  at(mt(r"e^{i\theta}", size=60, color=BLUE), 5.7, 1.5),
                  at(lab("an arrow of length one, at angle θ", 22, INK), 4.2, -0.1))


def wf_row():
    return VGroup(turn_row(-1.5, 4.0, -6.0, 6.4, 0.5, 0.27), Arrow([-6.0, -2.15, 0], [6.4, -2.15, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.2),
                  lab("position x", 22).move_to([5.6, -2.5, 0]))


@slide("As a formula, such a wave is an exponential", "The wave as a formula")
def pm11(s):
    yield [FadeIn(wave_f()), FadeIn(at(lab("the wave of momentum p: an exponential", 24, INK), -3.8, 0.35))]
    yield [FadeIn(wf_arrow())]
    yield [FadeIn(wf_row()), FadeIn(left_at(lab("for the wave, the angle grows with the position", 24, INK), -6.2, -2.9))]
    f = wave_f()
    yield [FadeIn(f[0][8:10].copy().set_color(ORANGE)), FadeIn(left_at(lab("so the exponent holds the momentum times the position", 24, ORANGE), -6.2, -3.5))]


@slide("It also holds a constant called h-bar.", "h-bar")
def pm12(s):
    f = wave_f()
    s.add(f, at(lab("the wave of momentum p: an exponential", 24, INK), -3.8, 0.35))
    yield [FadeIn(f[0][11].copy().set_color(PURPLE)), Create(underline(f[0][11], PURPLE)),
           FadeIn(at(mix(mt(r"\hbar", size=64, color=PURPLE), "“h-bar”: a constant", size=26, color=PURPLE), 3.4, 2.1))]
    c = P(5.5, 0.55)
    turn = VGroup(Circle(radius=0.38, color=ORANGE, stroke_width=4).move_to(c), left_at(lab("a full turn", 22, ORANGE), 6.05, 0.55),
                  left_at(lab("a full turn is an angle of 2π", 22, ORANGE), 1.3, -0.95))
    yield [FadeIn(at(mt(r"\hbar = \frac{h}{2\pi}", size=64, color=PURPLE), 3.0, 0.55)), FadeIn(turn),
           FadeIn(left_at(lab("Planck's constant divided by 2π", 22), 1.3, -0.5))]
    yield [FadeIn(left_at(mt(r"\hbar \approx 10^{-34}\ \text{joule-seconds}", size=48, color=PURPLE), 1.3, -2.1)), FadeIn(left_at(lab("tiny", 26, PURPLE, True), 1.3, -2.85))]


def goal_f(size=72):
    """p-hat psi_p = p e^{ipx/hbar}."""
    m = mt(r"\hat p", r"\,\psi_p", "=", "p", r"\,e^{ipx/\hbar}", size=size)
    m[0].set_color(PURPLE)
    m[1].set_color(BLUE)
    m[4].set_color(BLUE)
    return at(m, 0, 0.6)


@slide("Here's what we're looking for.", "What we're looking for")
def pm13(s):
    yield hold()
    yield [FadeIn(at(mix("this wave: an eigenstate of", mt(r"\hat p", size=48, color=PURPLE), ", with eigenvalue its momentum", mt("p", size=48), size=24), 0, 2.2))]
    g = goal_f()
    yield [FadeIn(g), FadeIn(right_at(lab("the momentum operator, applied to the wave", 22, BLUE), g[2].get_x() - 0.3, -0.4)), FadeIn(left_at(lab("the momentum times the wave", 22, BLUE), g[2].get_x() + 0.3, -0.4))]
    src, dst = g[4][2], g[3]
    yield [FadeIn(src.copy().set_color(ORANGE)), FadeIn(dst.copy().set_color(ORANGE)),
           Create(CurvedArrow(src.get_top() + UP * 0.12, dst.get_top() + UP * 0.25, angle=PI / 2.2, color=ORANGE, stroke_width=4, tip_length=0.18)),
           FadeIn(at(T("we need to pull the momentum down out of the exponent", 26, ORANGE, True), 0, -1.9))]


def slope_pic():
    ax = Axes(x_range=[0, 6, 1], y_range=[-1.3, 1.5, 1], x_length=5.6, y_length=2.6, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([-3.8, -0.9, 0])
    f = lambda x: np.sin(0.9 * x)
    x0, sl = 1.0, 0.9 * np.cos(0.9)
    tan = Line(ax.c2p(x0 - 0.9, f(x0) - 0.9 * sl), ax.c2p(x0 + 0.9, f(x0) + 0.9 * sl), color=ORANGE, stroke_width=5)
    return VGroup(ax, ax.plot(f, x_range=[0, 6], color=BLUE, stroke_width=4), tan, Dot(ax.c2p(x0, f(x0)), radius=0.08, color=ORANGE),
                  lab("along the line", 22).move_to([-1.8, -1.25, 0]), lab("slope", 22, ORANGE, True).move_to(ax.c2p(x0, f(x0)) + UP * 0.7 + LEFT * 0.5))


def slope_rule(size=60):
    return mt(r"\frac{d}{dx}\,e^{ax} = a\,e^{ax}", size=size)


@slide("Calculus has an operation that does that, and it's taking the slope.", "Taking the slope")
def pm14(s):
    yield [FadeIn(at(mix("taking the slope,", mt(r"\frac{d}{dx}", size=60, color=PURPLE), size=28, bold=True), -3.8, 1.9))]
    yield [FadeIn(slope_pic()), FadeIn(at(words("how fast the wave function changes as you move along the line", 30, 22, INK, ORIGIN), -3.8, -3.0))]
    yield [FadeIn(at(slope_rule(), 3.6, 0.6)),
           FadeIn(at(words("the slope of an exponential: the same exponential, times the number in front of x", 30, 24, INK, ORIGIN), 3.6, -1.2))]


def slope_f(size=64):
    """d psi_p / dx = (ip/hbar) e^{ipx/hbar}."""
    m = mt(r"\frac{d\psi_p}{dx}", "=", r"\frac{ip}{\hbar}", r"\,e^{ipx/\hbar}", size=size)
    m[3].set_color(BLUE)
    return m


@slide("Here that number is i, times the momentum, over h-bar.", "The slope of the wave")
def pm15(s):
    s.add(at(slope_rule(48), -3.6, 2.0), at(lab("the slope of an exponential", 22), 2.4, 2.0))
    yield [FadeIn(at(mix("here the number in front of x is", mt(r"a = \frac{ip}{\hbar}", size=56, color=ORANGE), size=26), 0, 0.6))]
    f = at(slope_f(72), 0, -1.4)
    f[2].set_color(ORANGE)
    yield [FadeIn(f), FadeIn(at(lab("the slope of the wave: that number, times the wave", 24, INK), 0, -2.9))]


def slope_top():
    f = at(slope_f(56), -3.4, 1.7)
    f[2].set_color(ORANGE)
    return f


@slide("That's almost what we want.", "Correcting the factor")
def pm16(s):
    yield [FadeIn(slope_top()), FadeIn(left_at(lab("almost what we want", 24, INK, True), 0.6, 2.0))]
    yield [FadeIn(left_at(mix("the p has come down, with an unwanted", mt(r"\frac{i}{\hbar}", size=48, color=ORANGE), size=24), 0.6, 1.2))]
    yield [FadeIn(at(mix("to correct for it, multiply by", mt(r"-i\hbar", size=60, color=PURPLE), size=26), 0, -0.4))]
    c = mt(r"-i\hbar \times \frac{i}{\hbar} = 1", size=60)
    yield [FadeIn(at(c, -1.0, -2.0)), FadeIn(tick(c)), FadeIn(left_at(words("minus i times i is one, and the h-bars cancel", 24, 22, MUTED), 2.6, -2.0))]


def p_result(size=60):
    m = mt(r"-i\hbar\,\frac{d\psi_p}{dx}", "=", "p", r"\,e^{ipx/\hbar}", size=size)
    m[3].set_color(BLUE)
    return m


@slide("What's left is the momentum times the wave.", "The momentum operator")
def pm17(s):
    r = at(p_result(), -1.0, 1.4)
    yield [FadeIn(r), FadeIn(tick(r)), FadeIn(at(lab("what's left: the momentum times the wave", 24, INK), 0, 0.3))]
    box = at(card(None, 9.0, 2.0, PURPLE), 0, -1.7)
    yield [FadeIn(box), FadeIn(at(mt(r"\hat p = -i\hbar\,\frac{d}{dx}", size=84, color=PURPLE), 0, -1.7)),
           FadeIn(at(lab("the momentum operator: minus i h-bar, times the slope", 24, PURPLE), 0, -3.2))]


def forever_row():
    return VGroup(turn_row(1.2, 4.0, -6.0, 6.0, 0.5, 0.3), at(T("…", 40, BLUE), -6.8, 1.2), at(T("…", 40, BLUE), 6.8, 1.2))


@slide("One caution about these waves.", "A caution about these waves")
def pm18(s):
    yield [FadeIn(forever_row())]
    yield [FadeIn(at(lab("they go on forever, so their total chance can't add up to one", 26, INK), 0, 0.1))]
    yield [FadeIn(at(T("no actual particle is in such a state", 28, ORANGE, True), 0, -0.8))]


@slide("It's a limit that actual states can come close to", "A caution about these waves")
def pm19(s):
    s.add(forever_row(), at(lab("they go on forever, so their total chance can't add up to one", 26, INK), 0, 0.1),
          at(T("no actual particle is in such a state", 28, ORANGE, True), 0, -0.8))
    sp = VGroup(Line(P(-6.6, -3.1), P(-3.4, -3.1), color=MUTED, stroke_width=3), spike(-5.0, -3.1, 1.3))
    yield [FadeIn(sp), FadeIn(left_at(words("a limit that actual states can come close to, like the state squeezed onto one point", 28, 22, INK), -3.0, -2.4))]
    xs = np.arange(1.9, 6.9, 0.45)
    bump = VGroup(*[phasor([x, -2.5], 2 * PI * x / 2.4, float(np.exp(-((x - 4.4) / 1.1) ** 2)), r=0.3, ring=False, width=4)
                    if np.exp(-((x - 4.4) / 1.1) ** 2) > 0.12 else Dot([x, -2.5, 0], radius=0.04, color=BLUE) for x in xs])
    yield [FadeIn(bump), FadeIn(at(lab("actual states: sums of such waves", 22, BLUE), 4.4, -3.4))]


# ================================================================== the bracket becomes a commutator
deck.part("The bracket becomes a commutator")


@slide("The bracket becomes a commutator.", "Does the order matter?")
def br1(s):
    yield hold()
    q = mix(mt(r"\hat x", size=72, color=PURPLE), "and", mt(r"\hat p", size=72, color=PURPLE), ": does the order matter?", size=30)
    yield [FadeIn(at(q, 0, 1.0))]
    yield [FadeIn(at(mix("apply both orders to any wave function", mt(r"\psi", size=56, color=BLUE), size=26), 0, -0.8))]


def ord_pipe(k):
    y = (1.0, -1.3)[k]
    names = (["take the slope", "multiply by x"], ["multiply by x", "take the slope"])[k]
    st = at(mt(r"\psi", size=56, color=BLUE), -6.2, y)
    b1 = at(card(names[0], 2.9, 0.9, PURPLE, 24), -3.7, y)
    b2 = at(card(names[1], 2.9, 0.9, PURPLE, 24), 0.0, y)
    res = left_at(mt((r"x\,\frac{d\psi}{dx}", r"\frac{d}{dx}\big(x\,\psi\big)")[k], size=52), 2.6, y)
    head = left_at(lab(("the first order: momentum first", "the second order: position first")[k], 24, INK, True), -6.5, y + 0.95)
    return VGroup(head, st, arrow(st, b1), b1, arrow(b1, b2), b2, arrow(b2, res), res)


@slide("In the first order, momentum goes first.", "Both orders on a wave function")
def br2(s):
    a = ord_pipe(0)
    yield [FadeIn(a[0]), FadeIn(a[1])]
    yield [FadeIn(a[2:])]
    b = ord_pipe(1)
    yield [FadeIn(b[0]), FadeIn(b[1])]
    yield [FadeIn(b[2:])]


def prod_rule(size=68):
    m = mt(r"\frac{d}{dx}\big(x\,\psi\big)", "=", r"x\,\frac{d\psi}{dx}", "+", r"\psi", size=size)
    m[4].set_color(ORANGE)
    return at(m, 0, 0.9)


@slide("The product rule from calculus handles the second order.", "The product rule")
def br3(s):
    m = prod_rule()
    yield [FadeIn(m[0]), FadeIn(at(pill("the product rule", MUTED, 26), -4.6, 2.3)), FadeIn(left_at(lab("for the second order", 24, INK), -2.9, 2.3))]
    yield [FadeIn(m[1]), FadeIn(left_at(lab("it has two pieces", 24, INK, True), 2.4, 2.3))]
    yield [FadeIn(m[2]), FadeIn(note_to("the position times the slope of the wave function", m[2], m[2].get_x() - 0.6, -1.0, INK, 22, 26))]
    yield [FadeIn(m[3]), FadeIn(m[4]), FadeIn(note_to("the wave function itself", m[4], m[4].get_x() + 0.8, -1.0, ORANGE, 22, 16))]


def two_orders(stage):
    """Both orders written out; stage 1 adds the slope's factor of minus i h-bar."""
    rows = VGroup()
    for k, y in enumerate((1.5, 0.1)):
        parts = [r"-i\hbar\,\Big(", r"x\,\frac{d\psi}{dx}"] + ([r"+", r"\psi"] if k else []) + [r"\Big)"]
        m = mt(*parts, size=52)
        m.shift(P(0.4, y) - m[1].get_left())
        if k:
            m[3].set_color(ORANGE)
        m[0].set_color(PURPLE)
        m[-1].set_color(PURPLE)
        if stage == 0:
            m[0].set_opacity(0)
            m[-1].set_opacity(0)
        rows.add(VGroup(right_at(lab(("the first order:", "the second order:")[k], 24, INK, True), -2.6, y), m))
    return rows


def extra_note():
    m = two_orders(1)[1][1]
    return VGroup(underline(m[3]), left_at(lab("one extra term", 22, ORANGE, True), m.get_right()[0] + 0.4, 0.1))


@slide("So the second order has one extra term, the wave function itself.", "One extra term")
def br4(s):
    yield [FadeIn(two_orders(0)), FadeIn(extra_note())]
    full = two_orders(1)
    yield [FadeIn(full[0][1][0]), FadeIn(full[0][1][-1]), FadeIn(full[1][1][0]), FadeIn(full[1][1][-1]),
           FadeIn(at(lab("each comes with the slope's factor of minus i h-bar", 24, PURPLE), 0, -1.7))]


def xp_comm(size=84):
    return mt(r"[\hat x, \hat p] = i\hbar", size=size, color=PURPLE)


@slide("The commutator is the first order minus the second.", "The commutator of position with momentum")
def br5(s):
    rows = two_orders(1)
    s.add(rows, extra_note())
    yield [Create(strike(rows[0][1][1], MUTED)), Create(strike(rows[1][1][1], MUTED)), FadeIn(left_at(words("first minus second: these cancel", 18, 22, MUTED), 3.4, 1.5))]
    r = mt(r"[\hat x, \hat p]\,\psi", "=", r"+\,i\hbar\,\psi", size=56)
    yield [FadeIn(at(r, 0, -1.5)), FadeIn(at(lab("the extra term gets subtracted, so the difference is plus i h-bar times the wave function", 22, ORANGE), 0, -2.3))]
    yield [FadeIn(at(xp_comm(64), 0, -3.3))]


@slide("Here a commutator equals a number.", "A commutator that equals a number")
def br6(s):
    yield [FadeIn(at(xp_comm(), 0, 1.6)), FadeIn(at(lab("here a commutator equals a number", 24, INK), 0, 0.5))]
    m = mt(r"\big(\hat x\hat p - \hat p\hat x\big)\,\psi = i\hbar\,\psi", size=56)
    yield [FadeIn(at(m, 0, -0.7)), FadeIn(at(lab("applied to any state, it just multiplies the state by i h-bar", 24, INK), 0, -1.6))]
    yield [FadeIn(at(card("never zero: position and momentum never commute", 10.4, 1.0, PURPLE, 28), 0, -2.9))]


CMP_X = [-1.1, 4.6]
CMP_Y = [0.6, -1.3]


def cmp_frame():
    return VGroup(at(card(None, 4.2, 4.6, MUTED), CMP_X[0], -0.1), at(card(None, 4.9, 4.6, PURPLE), CMP_X[1], -0.1),
                  at(lab("classical (chapter 1)", 24, MUTED, True), CMP_X[0], 1.8), at(lab("quantum (this chapter)", 24, PURPLE, True), CMP_X[1], 1.8))


def cmp_label(k):
    return left_at(lab(("the basic relation", "position squared")[k], 24, INK), -7.1, CMP_Y[k])


def cmp_cell(k, col):
    tex = [[r"\{x, p\} = 1", r"[\hat x, \hat p] = i\hbar"], [r"\{x^2, p\} = 2x", r"[\hat x^2, \hat p] = 2\,i\hbar\,\hat x"]][k][col]
    return at(mt(tex, size=48, color=(MUTED, PURPLE)[col]), CMP_X[col], CMP_Y[k])


@slide("Now compare chapter one.", "Bracket and commutator")
def br7(s):
    yield [FadeIn(cmp_frame())]
    yield [FadeIn(cmp_label(0)), FadeIn(left_at(lab("chapter 1 ended on one relation", 22), -7.1, 2.5))]
    yield [FadeIn(cmp_cell(0, 0))]
    yield [FadeIn(cmp_cell(0, 1))]


@slide("Take position squared.", "Bracket and commutator")
def br8(s):
    s.add(cmp_frame(), cmp_label(0), cmp_cell(0, 0), cmp_cell(0, 1))
    yield [FadeIn(cmp_label(1))]
    yield [FadeIn(cmp_cell(1, 0))]
    yield [FadeIn(cmp_cell(1, 1))]


@slide("The quantum answer is the classical one, times i h-bar.", "Bracket and commutator")
def br9(s):
    s.add(cmp_frame(), *[cmp_label(k) for k in (0, 1)], *[cmp_cell(k, c) for k in (0, 1) for c in (0, 1)])
    tags = VGroup()
    for y in CMP_Y:
        a = Arrow(P(1.1, y), P(2.05, y), buff=0, color=ORANGE, stroke_width=5, tip_length=0.18)
        tags.add(a, mt(r"\times\, i\hbar", size=36, color=ORANGE).next_to(a, UP, buff=0.12))
    yield [FadeIn(tags)]
    yield [FadeIn(right_at(lab("the pattern holds for the quantities this chapter needs", 22, INK), 7.2, -2.9))]


@slide("So here's the quantum version of the bracket that chapter one promised.", "The quantum version of the bracket")
def br10(s):
    m = mt(r"\{f, g\}", r"\ \longrightarrow\ ", r"\frac{[\hat f, \hat g]}{i\hbar}", size=84)
    m[0].set_color(MUTED)
    m[2].set_color(PURPLE)
    at(m, 0, 0.6)
    yield [FadeIn(m), FadeIn(lab("the Poisson bracket of two quantities f and g", 22).next_to(m[0], UP, buff=0.4).shift(LEFT * 0.8)),
           FadeIn(VGroup(lab("the quantum version that chapter 1 promised", 24, TEAL), check()).arrange(RIGHT, buff=0.25).move_to([0, 2.3, 0]))]
    yield [FadeIn(at(card("the commutator, divided by i h-bar, plays the role of the Poisson bracket", 13.4, 1.0, PURPLE, 28), 0, -2.0))]


@slide("Physicists often run this argument the other way.", "The other way round")
def br11(s):
    yield [FadeIn(at(lab("physicists often run this argument the other way", 26, INK), 0, 2.1))]
    a = at(card("start from\nthe bracket", 3.6, 1.4, MUTED, 26), -5.0, 0.3)
    b = at(card("replace it by\na commutator", 3.6, 1.4, PURPLE, 26), 0.0, 0.3)
    c = at(card("get the operators\nfrom that", 3.8, 1.4, PURPLE, 26), 5.0, 0.3)
    yield [FadeIn(a), GrowArrow(arrow(a, b)), FadeIn(b), GrowArrow(arrow(b, c)), FadeIn(c)]
    yield [FadeIn(at(pill("a later chapter on fields does exactly this", MUTED, 26), 0, -1.9))]


# ================================================================== averages and spreads
deck.part("Averages and spreads")

LEAN = [np.sin(np.radians(60)), np.cos(np.radians(60))]  # 60 degrees from vertical, to the right


@slide("Averages and spreads.", "One result says little")
def av1(s):
    yield hold()
    m = magnet("a measurement", -1.0, 0.6, 3.2)
    yield [FadeIn(atom([-4.6, 0.6], LEAN, 0.4)), GrowArrow(slot_arrow(P(-4.0, 0.6), P(-2.75, 0.6))), FadeIn(m), GrowArrow(slot_arrow(P(0.75, 0.6), P(1.8, 0.6))),
           FadeIn(left_at(T("one result", 28, BLUE, True), 2.0, 0.6)),
           FadeIn(at(lab("a single measurement gives a random result, so one result says little", 24, INK), 0, -1.2))]


def piles():
    g = VGroup(Line(P(2.5, 0.0), P(5.3, 0.0), color=LINE, stroke_width=2))
    for x, n in ((3.2, 12), (4.6, 4)):
        g.add(*[Dot(P(x - 0.13 + 0.26 * (i % 2), 0.18 + 0.26 * (i // 2)), radius=0.1, color=BLUE) for i in range(n)])
    return g


@slide("But repeat the measurement on many atoms in the same state.", "Many atoms, a pattern")
def av2(s):
    atoms = VGroup(*[atom([-6.6 + 0.75 * i, 0.9], LEAN, 0.28, width=4) for i in range(5)])
    yield [FadeIn(atoms), FadeIn(at(lab("many atoms in the same state", 22, BLUE), -5.1, 0.15)), GrowArrow(slot_arrow(P(-3.1, 0.9), P(-2.4, 0.9))),
           FadeIn(magnet("a measurement", -0.7, 0.9, 3.2))]
    yield [GrowArrow(slot_arrow(P(1.05, 0.9), P(2.1, 0.9))), FadeIn(piles()),
           FadeIn(at(words("the results form a pattern, and the theory predicts it exactly", 30, 22, TEAL, ORIGIN), 3.9, -0.8))]
    yield [FadeIn(at(pill("the average", ORANGE, 28), -4.6, -2.1)), FadeIn(at(pill("the spread", ORANGE, 28), -1.8, -2.1)),
           FadeIn(at(lab("two numbers describe it", 24, INK), -3.2, -1.3))]
    yield [FadeIn(at(lab("here quantum mechanics becomes predictable again", 24, INK), 0, -3.3))]


def ex_setup(stage):
    a = slot_arrow(P(-4.4, 0.8), P(-2.7, 0.8))
    g = VGroup(dial([-5.8, 0.8], 60, r=1.0), at(words("a first magnet, tilted 60° to the right", 20, 22, INK, ORIGIN), -5.6, -0.9),
               a, lab("keep up along it", 22, INK).next_to(a, UP, buff=0.08))
    if stage >= 1:
        g.add(VGroup(*[atom([-2.0 + 0.8 * i, 0.8], LEAN, 0.3, width=4) for i in range(3)]),
              at(words("leaning atoms, like the last chapter's", 20, 22, BLUE, ORIGIN), -1.2, -0.4))
    if stage >= 2:
        g.add(slot_arrow(P(0.4, 0.8), P(1.5, 0.8)), smag(2.7, 0.8, 2.2), two_out(3.8, 0.8, "right", "left"),
              at(lab("many of them, through a sideways magnet", 22, ORANGE), 3.4, -0.4))
    return g


@slide("Let's take an example.", "An example: the 60° atoms")
def av3(s):
    yield hold()
    yield [FadeIn(ex_setup(0))]
    yield [FadeIn(ex_setup(1)[4:])]
    yield [FadeIn(ex_setup(2)[6:])]


TB_X = [1.0, 3.3, 5.6]
TB_Y = [0.5, -0.5]
TB_ROWS = [("right", "+1", "93.3%"), ("left", "-1", "6.7%")]


def tb_head(stage):
    g = VGroup(at(lab("result", 22, MUTED, True), TB_X[0], 1.5), at(lab("chance", 22, TEAL, True), TB_X[2], 1.5),
               Line(P(0.0, 1.1), P(6.7, 1.1), color=LINE, stroke_width=2))
    if stage:
        g.add(at(lab("eigenvalue", 22, INK, True), TB_X[1], 1.5))
    return g


def tb_row(k, part):
    name, val, ch = TB_ROWS[k]
    return [VGroup(at(schip(name, 26), TB_X[0], TB_Y[k]), at(T(ch, 30, TEAL, True), TB_X[2], TB_Y[k])), at(mt(val, size=50), TB_X[1], TB_Y[k])][part]


def ex_left():
    return VGroup(smag(-4.6, 1.9, 2.2), at(lab("the 60° atoms", 22, BLUE), -4.6, 1.2))


def ex_bar(k):
    return bars(-5.4, -2.2, [0.933, 0.067], ["right", "left"], ["93.3%", "6.7%"], hmax=2.6, w=0.9, gap=1.6)[1 + 2 * k: 3 + 2 * k]


def ex_base():
    return bars(-5.4, -2.2, [0.933, 0.067], ["right", "left"], hmax=2.6, w=0.9, gap=1.6)[0]


@slide("They go right ninety-three point three percent of the time.", "The 60° atoms in a sideways magnet")
def av4(s):
    s.add(ex_left(), ex_base(), tb_head(0))
    yield [FadeIn(tb_row(0, 0)), FadeIn(ex_bar(0))]
    yield [FadeIn(tb_row(1, 0)), FadeIn(ex_bar(1))]


@slide("Right has eigenvalue plus one, and left has eigenvalue minus one.", "The average")
def av5(s):
    s.add(ex_left(), ex_base(), ex_bar(0), ex_bar(1), tb_head(0), tb_row(0, 0), tb_row(1, 0))
    yield [FadeIn(tb_head(1)[3]), FadeIn(tb_row(0, 1)), FadeIn(tb_row(1, 1))]
    yield [FadeIn(at(mt(r"(+1)(0.933) + (-1)(0.067)", size=44), 3.3, -1.7)), FadeIn(at(lab("each eigenvalue times its chance, added up", 22, INK), 3.3, -2.35))]
    yield [FadeIn(at(VGroup(mt(r"\approx 0.87", size=60, color=ORANGE), T("the average", 28, ORANGE, True)).arrange(RIGHT, buff=0.4), 3.3, -3.2))]


HIST_O = np.array([-3.75, -2.6, 0])  # value 0 on the axis
AV_X = 0.4


def hx(v):
    return HIST_O + RIGHT * 1.9 * v


def hist_base():
    axis = Line(hx(-1.6), hx(1.6), color=LINE, stroke_width=3)
    ticks = VGroup(*[lab(t, 24, INK).next_to(hx(v), DOWN, buff=0.15) for v, t in ((-1, "−1"), (0, "0"), (1, "+1"))])
    b1 = bar(hx(1)[0], HIST_O[1], 0.933, hmax=3.0, w=0.4)
    b1.add(T("93.3%", 22, TEAL, True).next_to(b1[0], RIGHT, buff=0.12).align_to(b1[0], UP))
    b2 = bar(hx(-1)[0], HIST_O[1], 0.067, hmax=3.0, w=0.4, label="6.7%", size=22)
    return VGroup(axis, ticks, lab("sideways result", 22).next_to(hx(0), DOWN, buff=0.6), b1, b2)


def avg_mark():
    x = hx(0.87)
    ln = DashedLine(x, x + UP * 3.9, color=ORANGE, stroke_width=4)
    return VGroup(ln, T("average 0.87", 24, ORANGE, True).next_to(ln.get_end(), LEFT, buff=0.15))


@slide("We call it the expectation value.", "The expectation value")
def av6(s):
    s.add(hist_base())
    yield [Create(avg_mark()[0]), FadeIn(avg_mark()[1]), FadeIn(left_at(pill("the expectation value", ORANGE, 28), AV_X, 1.7))]
    yield [FadeIn(left_at(lab("not a result any single atom gives:", 24, INK), AV_X, 0.6)),
           FadeIn(left_at(lab("each one gives +1 or −1", 24, INK), AV_X, 0.1))]
    yield [FadeIn(left_at(T("it's the average over many atoms", 26, INK, True), AV_X, -1.0))]


def dist_marks():
    y, y2 = 0.45, 0.95
    a = DoubleArrow(P(hx(-1)[0], y), P(hx(0.87)[0], y), buff=0, color=INK, stroke_width=3, tip_length=0.14)
    b = VGroup(Line(P(hx(0.87)[0], y2), P(hx(1)[0], y2), color=INK, stroke_width=5),
               Line(P(hx(1)[0], y2 - 0.12), P(hx(1)[0], y2 + 0.12), color=INK, stroke_width=3))
    return VGroup(a, lab("1.87", 22, INK).next_to(a, DOWN, buff=0.1), b, lab("0.13", 22, INK).next_to(b, RIGHT, buff=0.15))


def spread_mark():
    y = 2.0
    a = DoubleArrow(P(hx(0.37)[0], y), P(hx(1.37)[0], y), buff=0, color=ORANGE, stroke_width=4, tip_length=0.15)
    return VGroup(a, lab("0.5 each way, about the average", 22, ORANGE).next_to(a, UP, buff=0.08))


@slide("The spread measures how far the results land from the average.", "The spread")
def av7(s):
    s.add(hist_base(), avg_mark())
    yield [FadeIn(left_at(words("the spread: how far the results land from the average", 30, 26, ORANGE), AV_X + 1.9, 1.5))]
    yield [FadeIn(dist_marks()), FadeIn(left_at(lab("take each result's distance from the average", 24, INK), AV_X, 0.6))]
    yield [FadeIn(left_at(words("square the distances, average the squares, and take the square root", 40, 24, INK), AV_X, -0.4))]
    yield [FadeIn(left_at(VGroup(T("spread =", 32, ORANGE, True), mt("0.5", size=64, color=ORANGE)).arrange(RIGHT, buff=0.3), AV_X, -1.8)), FadeIn(spread_mark())]


def avg_formula(size=84):
    m = mt(r"\langle A\rangle", "=", r"\langle\psi\vert", r"\hat A", r"\vert\psi\rangle", size=size)
    m[3].set_color(PURPLE)
    m[2].set_color(BLUE)
    m[4].set_color(BLUE)
    return m


@slide("The operator gives both numbers directly.", "Straight from the operator")
def av8(s):
    yield [FadeIn(at(T("the operator gives the average and the spread directly", 28, PURPLE, True), 0, 2.1))]
    yield [FadeIn(at(lab("no need to find its eigenstates and eigenvalues first", 24, INK), 0, 1.3))]
    m = at(avg_formula(), 0, -0.4)
    yield [FadeIn(m), FadeIn(at(lab("the average of a quantity A", 22, ORANGE), m[0].get_x() - 0.6, -1.5)),
           FadeIn(at(lab("in the state ψ", 22, BLUE), m[4].get_x(), -1.5)), FadeIn(at(lab("the recipe for the average", 24, INK, True), 0, -2.4)),
           FadeIn(at(mix(mt(r"\langle\psi\vert", size=44, color=BLUE), "on the left: take the overlap with ψ", size=22, color=MUTED), 0, -3.2))]


RC_Y = 0.2
RC_STEPS = ["1. apply the operator to the state", "2. compare the result with the original state",
            "3. multiply their amplitudes pair by pair, and add"]


def rc_list(x, vals, names=None, rowh=0.8):
    return place(alist(vals, names, rowh=rowh), x, RC_Y)


def rc_pairs(x0, x1, rowh=0.8):
    g = VGroup()
    for dy in (rowh / 2, -rowh / 2):
        g.add(Line(P(x0, RC_Y + dy), P(x1, RC_Y + dy), color=ORANGE, stroke_width=3), at(T("×", 26, ORANGE, True), (x0 + x1) / 2, RC_Y + dy + 0.25))
    return g


def rc_generic(stage):
    v0 = lambda: [ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)]
    box = opbox(r"\hat A", -3.7, RC_Y)
    g = VGroup(rc_list(-5.8, v0()), slot_arrow(P(-5.15, RC_Y), P(-4.45, RC_Y)), box, slot_arrow(P(-2.95, RC_Y), P(-2.25, RC_Y)),
               rc_list(-1.6, [ph(100, 0.7, 0.3), ph(10, 0.7, 0.3)]), at(lab("the state", 22, BLUE), -5.8, RC_Y + 1.2),
               at(lab("the result", 22, BLUE), -1.6, RC_Y + 1.2))
    if stage >= 1:
        g.add(rc_list(0.8, v0()), at(lab("the original state", 22, BLUE), 1.0, RC_Y + 1.2))
    if stage >= 2:
        g.add(rc_pairs(-0.95, 0.15))
    if stage >= 3:
        c = at(card("the overlap", 3.0, 1.0, ORANGE, 28), 4.9, RC_Y)
        g.add(Arrow(P(1.5, RC_Y), c.get_left() + LEFT * 0.1, buff=0, color=MUTED, stroke_width=4, tip_length=0.18), c, at(lab("one number", 22), 4.9, RC_Y - 0.85))
    return g


def rc_step(k):
    return left_at(lab(RC_STEPS[k], 24, INK), -6.4, -1.7 - 0.6 * k)


@slide("Apply the operator to the state.", "The recipe for the average")
def av9(s):
    m = at(avg_formula(52), 0, 2.2)
    s.add(m)
    b1 = SurroundingRectangle(VGroup(m[3], m[4]), color=PURPLE, stroke_width=3, buff=0.04, corner_radius=0.06)
    b2 = SurroundingRectangle(m[2], color=ORANGE, stroke_width=3, buff=0.04, corner_radius=0.06)
    yield [FadeIn(rc_generic(0)), FadeIn(rc_step(0)), Create(b1), FadeIn(left_at(lab("1. apply the operator", 22, PURPLE), m.get_right()[0] + 0.4, 2.2))]
    yield [FadeIn(rc_generic(1)[7:]), FadeIn(rc_step(1)), Create(b2), FadeIn(right_at(lab("2. overlap with the original state", 22, ORANGE), m.get_left()[0] - 0.4, 2.2))]
    yield [FadeIn(rc_generic(2)[9:]), FadeIn(rc_step(2))]
    yield [FadeIn(rc_generic(3)[10:])]


def rc_tilted(stage):
    g = VGroup(rc_list(-5.4, ["√3/2", "1/2"], ["up", "down"]), slot_arrow(P(-4.6, RC_Y), P(-4.0, RC_Y)), opbox(r"\hat S", -3.3, RC_Y),
               slot_arrow(P(-2.6, RC_Y), P(-2.0, RC_Y)), rc_list(-1.2, ["1/2", "√3/2"]), rc_pairs(-0.5, 0.3), rc_list(1.0, ["√3/2", "1/2"]),
               at(lab("the sideways operator swaps them", 22, PURPLE), -3.3, RC_Y - 1.2))
    if stage >= 1:
        g.add(left_at(mt(r"=\ \frac{\sqrt3}{4} + \frac{\sqrt3}{4}", size=48), 2.0, RC_Y))
    return g


@slide("For our tilted atoms, that works straight from the up and down amplitudes.", "The tilted atoms, from the operator")
def av10(s):
    s.add(at(avg_formula(52), 0, 2.2))
    yield [FadeIn(rc_tilted(0)), FadeIn(left_at(lab("straight from the up and down amplitudes", 24, BLUE), -6.4, RC_Y + 1.15))]
    yield [FadeIn(at(lab("no need to rewrite the state as right and left", 24, INK), 0, -1.9))]
    r = VGroup(mt(r"\approx 0.87", size=60, color=ORANGE), T("the same average as before", 26, ORANGE, True), check()).arrange(RIGHT, buff=0.35)
    yield [FadeIn(rc_tilted(1)[8]), FadeIn(at(r, 0, -3.0))]


def results_line(y, seed, name, sym, w=0.8):
    rng = np.random.default_rng(seed)
    xs = np.clip(rng.normal(-2.4, w, 26), -5.4, 0.6)
    a = DoubleArrow(P(-2.4 - w, y - 0.45), P(-2.4 + w, y - 0.45), buff=0, color=ORANGE, stroke_width=4, tip_length=0.15)
    return VGroup(Line(P(-5.8, y), P(1.0, y), color=LINE, stroke_width=3), *[Dot(P(x, y), radius=0.07, color=BLUE) for x in xs],
                  left_at(lab(f"many {name} results", 22), -5.8, y + 0.5), a,
                  left_at(mix(mt(sym, size=60, color=ORANGE), f"the spread in {name}", size=26, color=ORANGE), 2.0, y - 0.2))


@slide("The spread comes the same way.", "Spread in position, spread in momentum")
def av11(s):
    yield [FadeIn(at(lab("the spread comes the same way, from the operator", 24, INK), 0, 2.3))]
    yield [FadeIn(results_line(1.0, 3, "position", r"\Delta x"))]
    yield [FadeIn(results_line(-1.6, 8, "momentum", r"\Delta p", 1.1))]


# ================================================================== uncertainty
deck.part("Position and momentum can't both be exact")

SL_Y0, SL_TOP, SL_BOT = 0.2, 2.3, -1.9


def slit_rig(bx, sx, gap, name):
    return VGroup(Line([bx, SL_BOT, 0], [bx, SL_Y0 - gap / 2, 0], color=INK, stroke_width=6), Line([bx, SL_Y0 + gap / 2, 0], [bx, SL_TOP, 0], color=INK, stroke_width=6),
                  Line([sx, SL_BOT, 0], [sx, SL_TOP, 0], color=MUTED, stroke_width=5), DashedLine([bx - 1.2, SL_Y0, 0], [bx - 0.1, SL_Y0, 0], color=MUTED, stroke_width=2),
                  Dot([bx - 1.3, SL_Y0, 0], radius=0.09, color=INK), lab(name, 22).move_to([bx, SL_BOT - 0.4, 0]), lab("screen", 22).move_to([sx, SL_BOT - 0.4, 0]))


def hump(sx, w, amp, color=TEAL, dashed=False):
    c = ParametricFunction(lambda t: np.array([sx + 0.1 + amp * np.exp(-(t - SL_Y0) ** 2 / (2 * w * w)), t, 0]), t_range=[SL_BOT, SL_TOP, 0.02],
                           color=color, stroke_width=5)
    return DashedVMobject(c, num_dashes=50) if dashed else c


@slide("Position and momentum can't both be exact.", "A narrower slit")
def un1(s):
    yield hold()
    yield [FadeIn(slit_rig(-5.4, -3.4, 0.9, "one slit")), Create(hump(-3.4, 0.45, 1.1)), FadeIn(left_at(words("the hump (last chapter)", 12, 22, TEAL), -2.1, 1.6))]
    exp = hump(3.0, 0.2, 1.4, RED, True)
    yield [FadeIn(slit_rig(1.0, 3.0, 0.3, "a narrower slit")), FadeIn(exp), FadeIn(left_at(words("you might expect a narrower hump", 16, 22, RED), 4.9, 1.6))]
    yield [Create(cross(Square(0.7).move_to([3.9, SL_Y0, 0]), RED, 5)), Create(hump(3.0, 1.0, 0.75)),
           FadeIn(left_at(words("instead the electrons spread out wider", 16, 22, TEAL), 4.9, -0.9))]


UB, US = -5.2, -1.6


def big_rig():
    return VGroup(slit_rig(UB, US, 0.4, "the narrow slit"), hump(US, 1.0, 1.1))


def dx_mark():
    t = left_at(mix("the slit's width: the spread in position,", mt(r"\Delta x", size=48, color=ORANGE), size=24, color=ORANGE), 0.9, 1.1)
    ticks = VGroup(Line(P(UB - 0.45, SL_Y0 + 0.2), P(UB - 0.15, SL_Y0 + 0.2), color=ORANGE, stroke_width=4),
                   Line(P(UB - 0.45, SL_Y0 - 0.2), P(UB - 0.15, SL_Y0 - 0.2), color=ORANGE, stroke_width=4),
                   mt(r"\Delta x", size=44, color=ORANGE).move_to([UB - 0.75, SL_Y0 + 0.75, 0]))
    return VGroup(t, ticks)


@slide("Read the slit and the hump as spreads.", "The slit and the hump as spreads")
def un2(s):
    yield [FadeIn(big_rig()), FadeIn(at(lab("read the slit and the hump as spreads", 24, INK, True), 3.8, 2.45))]
    yield [FadeIn(left_at(lab("the slit fixes where the electron is across it", 24, INK), 0.9, 1.8)), FadeIn(dx_mark()[1][:2])]
    yield [FadeIn(dx_mark()[0]), FadeIn(dx_mark()[1][2])]


def dp_mark():
    a = DoubleArrow(P(US + 1.5, SL_Y0 - 1.0), P(US + 1.5, SL_Y0 + 1.0), buff=0, color=ORANGE, stroke_width=4, tip_length=0.15)
    return VGroup(a, mt(r"\Delta p", size=44, color=ORANGE).next_to(a, RIGHT, buff=0.12),
                  left_at(lab("the hump's width: the spread in", 24, ORANGE), 0.9, -0.7), left_at(mix("sideways momentum,", mt(r"\Delta p", size=48, color=ORANGE), size=24, color=ORANGE), 0.9, -1.2))


def side_path():
    end = P(US, SL_Y0 + 1.5)
    mid = (P(UB, SL_Y0) + end) / 2
    return VGroup(Line(P(UB, SL_Y0), end, color=BLUE, stroke_width=3), Dot(end, radius=0.09, color=BLUE),
                  Arrow(mid, mid + UP * 0.75, buff=0, color=ORANGE, stroke_width=5, tip_length=0.16),
                  left_at(words("lands far from the centre: it was moving sideways", 30, 22, INK), 0.9, 0.2))


@slide("An electron that lands far from the centre was moving sideways.", "The slit and the hump as spreads")
def un3(s):
    s.add(big_rig(), dx_mark(), at(lab("read the slit and the hump as spreads", 24, INK, True), 3.8, 2.45),
          left_at(lab("the slit fixes where the electron is across it", 24, INK), 1.2, 1.8))
    yield [FadeIn(side_path())]
    yield [FadeIn(dp_mark())]
    yield [FadeIn(left_at(mix("a narrower slit: a smaller", mt(r"\Delta x", size=48, color=ORANGE), size=26, bold=True), 1.2, -2.3))]
    yield [FadeIn(left_at(mix("a wider hump: a larger", mt(r"\Delta p", size=48, color=ORANGE), size=26, bold=True), 1.2, -3.1))]


def sound_wave(y, click):
    if click:
        f = lambda t: 0.6 * np.sin(2 * PI * t / 0.22) * np.exp(-((t + 4.1) / 0.2) ** 2)
    else:
        f = lambda t: 0.4 * np.sin(2 * PI * t / 0.55)
    ax = Arrow(P(-6.9, y - 0.85), P(-1.2, y - 0.85), buff=0, color=MUTED, stroke_width=3, tip_length=0.16)
    return VGroup(ParametricFunction(lambda t: np.array([t, y + f(t), 0]), t_range=[-6.8, -1.5, 0.01], color=ORANGE, stroke_width=4),
                  ax, lab("time", 22).next_to(ax.get_end(), DOWN, buff=0.1).shift(LEFT * 0.3),
                  left_at(lab(("a long, steady note", "a short click")[click], 24, INK, True), -6.8, y + 0.9))


def pitch_chart(y, wide):
    f = (lambda u: 1.0 * np.exp(-((u - 2.2) / 1.0) ** 2)) if wide else (lambda u: 1.4 * np.exp(-((u - 2.2) / 0.05) ** 2))
    ax = Arrow(P(1.2, y - 0.85), P(6.4, y - 0.85), buff=0, color=MUTED, stroke_width=3, tip_length=0.16)
    return VGroup(ParametricFunction(lambda u: np.array([1.4 + u, y - 0.85 + f(u), 0]), t_range=[0, 4.4, 0.005], color=ORANGE, stroke_width=4),
                  ax, lab("pitch", 22).next_to(ax.get_end(), DOWN, buff=0.1).shift(LEFT * 0.3),
                  left_at(lab(("one pitch", "no single pitch: a mix of many")[wide], 24, ORANGE, True), 1.4, y + 0.9))


def sound_all():
    return VGroup(sound_wave(1.3, 0), pitch_chart(1.3, 0), sound_wave(-1.3, 1), pitch_chart(-1.3, 1),
                  Arrow(P(-0.8, 1.0), P(0.8, 1.0), buff=0, color=MUTED, stroke_width=4, tip_length=0.18),
                  Arrow(P(-0.8, -1.6), P(0.8, -1.6), buff=0, color=MUTED, stroke_width=4, tip_length=0.18))


@slide("Sound does the same.", "A note and a click")
def un4(s):
    g = sound_all()
    yield [FadeIn(g[0])]
    yield [FadeIn(g[4]), FadeIn(g[1])]
    yield [FadeIn(g[2])]
    yield [FadeIn(g[5]), FadeIn(g[3])]


@slide("A sound squeezed into a short time needs many pitches.", "A note and a click")
def un5(s):
    s.add(sound_all())
    yield [FadeIn(at(T("a sound squeezed into a short time needs many pitches", 24, ORANGE, True), 0, -3.0))]
    yield [FadeIn(at(T("a particle squeezed into a small region needs many wavelengths", 24, BLUE, True), 0, -3.65))]


# The three rows of docs/manim/page_diagrams.py, WaveSum.
WS_XS = np.linspace(-15, 15, 27)
WS_K0 = 2 * np.pi / 6
WS_KS = np.linspace(WS_K0 - 0.9, WS_K0 + 0.9, 61)
WS_W = np.exp(-(WS_KS - WS_K0) ** 2 / (2 * 0.25 ** 2))
WS_W = WS_W / WS_W.sum()
WS_F = [lambda x: np.exp(1j * WS_K0 * x), lambda x: 0.5 * (np.exp(1j * WS_K0 * x) + np.exp(1j * 2 * np.pi / 4.5 * x)),
        lambda x: np.sum(WS_W * np.exp(1j * WS_KS * x))]
WS_ROWS = [(1.6, "one wavelength", "arrow length the same everywhere: equally likely to be anywhere"),
           (-0.2, "two wavelengths", "the length rises and falls"),
           (-2.0, "many wavelengths", "they reinforce near the bump, and cancel everywhere else")]
WS_X0, WS_X1, WS_L = -4.4, 6.8, 0.32


def ws_row(k, part):
    y, name, note = WS_ROWS[k]
    if part == 1:
        return at(lab(note, 22, INK), (WS_X0 + WS_X1) / 2, y - 0.8)
    g = VGroup(Line([WS_X0 - 0.2, y, 0], [WS_X1 + 0.2, y, 0], color=MUTED, stroke_width=1.5).set_opacity(0.5), left_at(lab(name, 22, INK, True), -7.2, y))
    for x in WS_XS:
        z = WS_F[k](x)
        r = abs(z)
        px = WS_X0 + (x + 15) / 30 * (WS_X1 - WS_X0)
        if r * WS_L < 0.04:
            g.add(Dot([px, y, 0], radius=0.03, color=BLUE))
            continue
        d = np.array([np.cos(np.angle(z)), np.sin(np.angle(z)), 0]) * r * WS_L
        g.add(Arrow(P(px, y) - d / 2, P(px, y) + d / 2, buff=0, color=BLUE, stroke_width=3, max_tip_length_to_length_ratio=0.35, max_stroke_width_to_length_ratio=12))
    return g


@slide("Here's how that works for wave functions.", "Adding momentum waves")
def un6(s):
    yield hold()
    yield [FadeIn(ws_row(0, 0)), FadeIn(left_at(lab("a state of one momentum", 22, BLUE), WS_X0, 2.4))]
    yield [FadeIn(ws_row(0, 1))]


@slide("To make a narrow bump, you have to add many of those momentum waves", "Adding momentum waves")
def un7(s):
    s.add(ws_row(0, 0), ws_row(0, 1), left_at(lab("a state of one momentum", 22, BLUE), WS_X0, 2.4))
    yield [FadeIn(ws_row(1, 0)), FadeIn(ws_row(1, 1)), FadeIn(ws_row(2, 0))]
    yield [FadeIn(ws_row(2, 1))]
    yield [FadeIn(at(T("the narrower the bump, the wider the range of momenta it needs", 24, ORANGE, True), 0, -3.6))]


def bell(ax, w, color=TEAL):
    return ax.plot(lambda x: np.exp(-x * x / (2 * w * w)), x_range=[-4, 4], color=color, stroke_width=5)


def bell_axes(x, name):
    ax = Axes(x_range=[-4, 4, 1], y_range=[0, 1.15, 1], x_length=5.6, y_length=1.7, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([x, 1.3, 0])
    return ax, lab(name, 22).next_to(ax, DOWN, buff=0.08)


def spread_bar(ax, w, sym):
    a = DoubleArrow(ax.c2p(-w, 0.6), ax.c2p(w, 0.6), buff=0, color=ORANGE, stroke_width=4, tip_length=0.13)
    return VGroup(a, mt(sym, size=40, color=ORANGE).move_to(ax.c2p(0, 0.6) + RIGHT * 2.2 + UP * 0.5))


def bells(w):
    a1, n1 = bell_axes(-3.7, "position results")
    a2, n2 = bell_axes(3.7, "momentum results")
    return VGroup(a1, n1, a2, n2, bell(a1, w), spread_bar(a1, w, r"\Delta x"), bell(a2, 0.55 / w), spread_bar(a2, 0.55 / w, r"\Delta p"))


def unc_f(size=76):
    return at(mt(r"\Delta x\,\Delta p", r"\ \ge\ \frac{\hbar}{2}", size=size, color=PURPLE), 0, -1.9)


@slide("So the two spreads can't both be small.", "The uncertainty relation")
def un8(s):
    w = ValueTracker(0.9)
    pic = always_redraw(lambda: bells(w.get_value()))
    s.add(pic)
    yield [w.animate.set_value(0.45), FadeIn(at(lab("the two spreads can't both be small", 24, INK, True), 0, -0.55))]
    f = unc_f()
    yield [FadeIn(f[0]), FadeIn(right_at(lab("the two spreads, multiplied:", 22, INK), f[0].get_left()[0] - 0.3, -1.9))]
    yield [FadeIn(f[1]), FadeIn(left_at(lab("a lower limit: half of h-bar", 22, INK), f[1].get_right()[0] + 0.3, -1.9))]
    yield [FadeIn(at(pill("the Heisenberg uncertainty relation", PURPLE, 26), 0, -3.3))]


def sup_card():
    return at(card("suppose a state were exact in both\nposition and momentum: zero spread in each", 8.4, 1.5, ORANGE, 26), 0, 1.5)


def sup_rows():
    return [at(lab("on that state, both operators would only multiply by numbers", 24, INK), 0, 0.1),
            at(lab("then the two orders would agree, and the commutator would give zero", 24, INK), 0, -0.6)]


@slide("The commutator is the reason.", "The commutator is the reason")
def un9(s):
    yield hold()
    yield [FadeIn(sup_card(), shift=UP * 0.15)]
    r = sup_rows()
    yield [FadeIn(r[0])]
    yield [FadeIn(r[1])]


@slide("But we found that it multiplies every state by i h-bar.", "The commutator is the reason")
def un10(s):
    c = sup_card()
    s.add(c, *sup_rows())
    yield [FadeIn(at(VGroup(T("but", 26, INK), xp_comm(52), T("multiplies every state by i h-bar, not by zero", 24, INK)).arrange(RIGHT, buff=0.3), 0, -1.7))]
    yield [Create(cross(c, RED, 6).set_opacity(0.55)), FadeIn(at(T("so no such state exists", 28, RED, True), 0, -2.6))]
    yield [FadeIn(at(lab("the same commutator also sets the limit at half of h-bar (not shown here)", 22), 0, -3.5))]


def el_row(compact=False):
    if compact:
        return left_at(mix("an electron confined to an atom: speed uncertain by about", T("580 km/s", 26, ORANGE, True), size=22), -6.8, 2.3)
    c = np.array([-4.6, 0.0, 0])
    return VGroup(Circle(radius=1.5, color=LINE, stroke_width=3).move_to(c), Dot(c, radius=0.1, color=INK),
                  at(lab("an electron confined to the size of an atom", 22, BLUE), -4.4, -1.9))


@slide("That limit is tiny in everyday units.", "An electron and a ball")
def un11(s):
    yield [FadeIn(at(lab("the limit is tiny in everyday units", 24, INK), 0, 2.3))]
    yield [FadeIn(el_row())]
    yield [FadeIn(left_at(lab("its speed is then uncertain by about", 24, INK), -1.6, 0.9)), FadeIn(left_at(T("580 km/s", 48, ORANGE, True), -1.6, 0.1))]
    rng = np.random.default_rng(9)
    c = np.array([-4.6, 0.0, 0])
    cloud = VGroup(*[Dot(c + 0.6 * np.array([a, b, 0]), radius=0.045, color=BLUE).set_opacity(0.6) for a, b in rng.normal(size=(90, 2)).clip(-2.2, 2.2)])
    yield [FadeIn(cloud), FadeIn(left_at(lab("you can't picture it as a little ball on a path", 26, INK, True), -1.6, -1.1))]


@slide("Now confine a one kilogram ball to a micrometre.", "An electron and a ball")
def un12(s):
    s.add(el_row(True))
    yield [FadeIn(Dot([-5.0, 0.3, 0], radius=0.55, color=BLUE)), FadeIn(at(lab("a 1 kg ball, confined to a micrometre", 22, BLUE), -4.6, -0.8))]
    yield [FadeIn(left_at(lab("its speed is uncertain by only about", 24, INK), -1.6, 1.0)),
           FadeIn(left_at(mt(r"5\times10^{-29}\ \text{m/s}", size=72, color=ORANGE), -1.6, 0.1))]
    yield [FadeIn(left_at(lab("far below anything measurable", 26, INK, True), -1.6, -1.0)),
           FadeIn(at(card("so chapter 1 never noticed the limit", 8.0, 0.9, MUTED, 28), 0, -2.6))]


# ================================================================== the energy operator
deck.part("The energy operator")


@slide("The energy operator.", "Between measurements")
def en1(s):
    yield hold()
    st = place(alist([ph(40, 0.6, 0.3), ph(120, 0.8, 0.3)], rowh=0.72), -2.8, 0.8)
    st2 = place(alist([ph(-30, 0.6, 0.3), ph(200, 0.8, 0.3)], rowh=0.72), 2.8, 0.8)
    ar = Arrow([-2.1, 0.8, 0], [2.1, 0.8, 0], buff=0, color=MUTED, stroke_width=4, tip_length=0.18)
    yield [FadeIn(st), GrowArrow(ar), FadeIn(st2), FadeIn(at(words("between measurements: the state changes in a fully predictable way", 34, 22, INK, ORIGIN), 0, -0.75)),
           FadeIn(at(T("how?", 28, ORANGE, True), 0, 1.3))]
    yield [FadeIn(at(pill("to find how: start from the energy", PURPLE, 28), 0, -2.4))]


def ham(size=76):
    return at(mt("H", "=", r"\frac{p^2}{2m}", "+", "V(x)", size=size, color=MUTED), 0, 0.8)


@slide("In chapter one, the Hamiltonian was the energy.", "Chapter 1's Hamiltonian")
def en2(s):
    m = ham()
    yield [FadeIn(m[0]), FadeIn(left_at(lab("chapter 1: the Hamiltonian was the energy", 24, INK), -6.8, 2.3))]
    yl = m[2].get_bottom()[1] - 0.45
    yield [FadeIn(m[1:]), FadeIn(at(lab("kinetic energy", 22, ORANGE), m[2].get_x() - 0.4, yl)),
           FadeIn(at(lab("potential energy", 22, ORANGE), m[4].get_x() + 0.4, yl)), FadeIn(at(lab("it moved the state forward", 24, INK), 0, -1.6))]
    yield [Indicate(m[2], color=ORANGE), FadeIn(at(lab("kinetic energy: the momentum squared, divided by twice the mass", 22), 0, -2.6))]


@slide("To use the Hamiltonian now, we need its operator.", "From quantities to operators")
def en3(s):
    yield [FadeIn(at(lab("to use the Hamiltonian now, we need its operator", 24, INK), 0, 2.3))]
    yield [FadeIn(at(pill("the rule", PURPLE, 26), -6.2, 1.2))]
    a = at(mt(r"\frac{p^2}{2m} + V(x)", size=64, color=MUTED), -4.0, 0.0)
    yield [FadeIn(a), FadeIn(at(words("a quantity built from position and momentum", 24, 22, INK, ORIGIN), -4.0, -1.4))]
    b = at(mt(r"\frac{\hat p^2}{2m} + V(\hat x)", size=64, color=PURPLE), 4.0, 0.0)
    yield [GrowArrow(arrow(a, b, buff=0.35)), FadeIn(b),
           FadeIn(at(words("its operator: built the same way, from the position and momentum operators", 30, 22, PURPLE, ORIGIN), 4.0, -1.5))]


def sup_mom():
    return VGroup(turn_row(1.6, 3.2, -6.4, -0.6, 0.45, 0.27), at(lab("a state of definite momentum p", 22, BLUE), -3.5, 2.4))


@slide("Here's what supports the rule.", "What supports the rule")
def en4(s):
    yield hold()
    yield [FadeIn(sup_mom())]
    a = mt(r"\hat p", r"\,\psi_p = p\,\psi_p", size=56)
    a[0].set_color(PURPLE)
    yield [FadeIn(at(a, -3.5, 0.2)), FadeIn(at(lab("the momentum operator just multiplies by p", 22, INK), -3.5, -0.6))]
    b = mt(r"\hat p\,\hat p", r"\,\psi_p = p^2\,\psi_p", size=56)
    b[0].set_color(PURPLE)
    yield [FadeIn(at(b, -3.5, -1.8)), FadeIn(at(lab("applying it twice multiplies by p squared", 22, INK), -3.5, -2.6))]


@slide("The same goes for a state squeezed onto one point.", "What supports the rule")
def en5(s):
    a = mt(r"\hat p\,\hat p", r"\,\psi_p = p^2\,\psi_p", size=44)
    a[0].set_color(PURPLE)
    s.add(sup_mom(), at(a, -3.5, 0.4))
    sp = VGroup(Line(P(1.2, 1.2), P(6.4, 1.2), color=MUTED, stroke_width=3), spike(3.8, 1.2, 1.3), mt("x", size=40).move_to([3.8, 0.85, 0]),
                at(lab("a state squeezed onto one point x", 22, BLUE), 3.8, 0.25))
    yield [FadeIn(sp)]
    yield [FadeIn(at(mix(mt(r"V(\hat x)", size=52, color=PURPLE), "multiplies by", mt("V(x)", size=52), size=24), 3.8, -0.7)),
           FadeIn(at(lab("the potential energy at that point", 22), 3.8, -1.4))]
    c = card("a definite position or a definite momentum: the operator gives chapter 1's answer", 14.2, 0.9, TEAL, 26)
    yield [FadeIn(at(c, 0, -2.8))]


def part_cards(done=True):
    g = VGroup()
    for x, tex, name in ((-3.6, r"\frac{\hat p^2}{2m}", "the kinetic part"), (3.6, r"V(\hat x)", "the potential part")):
        c = at(card(None, 5.6, 3.2, PURPLE), x, -1.5)
        g.add(VGroup(c, at(mt(tex, size=60, color=PURPLE), x, -0.8), at(lab(name, 24, PURPLE, True), x, -1.95),
                     VGroup(lab("right for every state", 22, TEAL, True), check(TEAL, 0.3)).arrange(RIGHT, buff=0.2).move_to([x, -2.55, 0])))
    return g


@slide("Any state is a mix of such states, and an operator acts on each piece", "Each part is right for every state")
def en6(s):
    parts = VGroup(*[phasor([-2.6 + 2.6 * k, 1.6], a, f, r=0.55, width=5) for k, (a, f) in enumerate(((0.4, 0.8), (1.9, 0.6), (-0.8, 0.5)))],
                   *[at(T("+", 34, INK), -1.3 + 2.6 * k, 1.6) for k in range(2)])
    yield [FadeIn(parts), FadeIn(left_at(words("any state: a mix of such states", 16, 22, BLUE), -6.9, 1.6)),
           FadeIn(left_at(words("an operator acts on each piece", 16, 22, PURPLE), 3.9, 1.6))]
    g = part_cards()
    yield [FadeIn(g[0])]
    yield [FadeIn(g[1])]


def guess_f():
    m = mt(r"\frac{\hat p^2}{2m}", "+", r"V(\hat x)", size=84, color=PURPLE)
    m[1].set_color(ORANGE)
    return at(m, 0, 0.9)


@slide("What we haven't checked is adding them.", "Adding them is a guess")
def en7(s):
    m = guess_f()
    r = ring(m[1])
    note = at(lab("not checked: adding them", 24, ORANGE), m[1].get_x(), -0.85)
    yield [FadeIn(r), FadeIn(m), FadeIn(note),
           GrowArrow(Arrow(note.get_top() + UP * 0.05, r.get_bottom() + DOWN * 0.25, buff=0, color=ORANGE, stroke_width=3, tip_length=0.13))]
    yield [FadeIn(at(pill("that part is a guess", ORANGE, 28), 0, -1.7))]
    yield [FadeIn(at(lab("we assume the energy operator is just the two parts added together, as in chapter 1", 24, INK), 0, -2.8))]


@slide("No state has both a definite position and a definite momentum.", "How the guess is tested")
def en8(s):
    a = at(card("a definite position", 4.6, 1.0, BLUE, 26), -3.4, 1.5)
    b = at(card("a definite momentum", 4.6, 1.0, BLUE, 26), 3.4, 1.5)
    yield [FadeIn(a), FadeIn(b), FadeIn(at(T("no state has both", 26, RED, True), 0, 0.5)), Create(cross(Square(0.5).move_to([0, 1.5, 0]), RED, 5))]
    yield [FadeIn(at(lab("so we can't check the sum directly", 24, INK), 0, -0.6))]
    yield [FadeIn(at(card("we test it by what it predicts:\nlater in this chapter, and in the next", 8.4, 1.4, TEAL, 26), 0, -2.3))]


@slide("There's no deeper derivation.", "No deeper derivation")
def en9(s):
    yield [FadeIn(at(lab("there's no deeper derivation", 26, INK, True), 0, 2.0))]
    yield [FadeIn(at(card("the simplest operator that agrees with chapter 1\nwherever we can compare the two", 10.4, 1.5, PURPLE, 26), 0, 0.4))]
    yield [FadeIn(at(VGroup(T("and its predictions match experiment", 28, TEAL, True), check()).arrange(RIGHT, buff=0.3), 0, -1.6))]


def h_op(size=68):
    """H-hat psi = -(hbar^2/2m) d^2 psi/dx^2 + V(x) psi."""
    return mt(r"\hat H\,\psi", "=", r"-\frac{\hbar^2}{2m}\,\frac{d^2\psi}{dx^2}", "+", r"V(x)\,\psi", size=size, color=PURPLE)


def h_parts():
    m = at(h_op(), 0, 1.2)
    b1, b2 = Brace(m[2], DOWN, color=ORANGE), Brace(m[4], DOWN, color=ORANGE)
    return m, VGroup(b1, lab("the kinetic part", 24, ORANGE, True).next_to(b1, DOWN, buff=0.1), b2, lab("the potential part", 24, ORANGE, True).next_to(b2, DOWN, buff=0.1))


@slide("So here's the energy operator, written out on screen.", "The energy operator")
def en10(s):
    m, br = h_parts()
    yield [FadeIn(m), FadeIn(at(lab("what the energy operator does to a wave function ψ", 24, INK), 0, 2.4))]
    yield [FadeIn(br)]
    x1, x2 = br[1].get_x(), br[3].get_x()
    yield [FadeIn(at(words("the momentum operator applied twice", 22, 22, INK, ORIGIN), x1 - 0.6, -1.6)),
           FadeIn(at(mt(r"(-i\hbar)^2 = -\hbar^2", size=40), x1 - 0.6, -2.5))]
    yield [FadeIn(at(words("multiplies the wave function, at each point, by the potential energy there", 28, 22, INK, ORIGIN), x2 + 0.9, -1.8))]


@slide("We need it for two things.", "Two uses for the energy operator")
def en11(s):
    yield [FadeIn(at(h_op(48), 0, 2.0))]
    yield [FadeIn(at(card("1. its eigenstates are the\nstates of definite energy", 6.2, 1.6, BLUE, 26), -3.5, -0.2), shift=UP * 0.15),
           FadeIn(at(lab("next: what they do as time passes", 22), -3.5, -1.4))]
    yield [FadeIn(at(card("2. it drives the\nSchrödinger equation", 6.2, 1.6, PURPLE, 26), 3.5, -0.2), shift=UP * 0.15)]


# ================================================================== a definite energy turns the phase
deck.part("A definite energy turns the phase")


def time_row(y, n=8, x0=-1.0, x1=6.2, step=-0.7, r=0.36):
    xs = np.linspace(x0, x1, n)
    ax = Arrow([x0 - 0.6, y - 0.7, 0], [x1 + 0.6, y - 0.7, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.16)
    return VGroup(*[phasor([x, y], step * i, 1.0, r=r, ring=True) for i, x in enumerate(xs)], ax, lab("time", 22).next_to(ax.get_end(), DOWN, buff=0.1).shift(LEFT * 0.3))


@slide("A definite energy turns the phase.", "Turning in time")
def de1(s):
    yield hold()
    ang = ValueTracker(0.0)
    big = always_redraw(lambda: phasor([-4.6, 0.3], ang.get_value(), 1.0, r=1.1, width=6))
    yield [FadeIn(big), FadeIn(at(lab("a state of definite energy, as time passes", 24, BLUE), -4.2, 2.1))]
    yield [ang.animate(rate_func=linear).set_value(-1.5 * PI), FadeIn(time_row(0.3)), FadeIn(at(T("it turns its phase steadily", 26, INK, True), 2.6, -1.4))]


TT_X = [-5.4, -0.9, 4.2]
TT_Y = [0.9, -1.5]


def tt_head():
    return VGroup(*[at(lab(t, 22, MUTED, True), x, 2.3) for t, x in zip(("a state with a definite…", "its phase turns…", "how fast"), TT_X)],
                  Line(P(-7.1, 1.9), P(7.1, 1.9), color=LINE, stroke_width=2))


def tt_row(k, part):
    y = TT_Y[k]
    name, sym, where, tex, unit = (("momentum", "p", "along the line", r"\frac{p}{h}", "turns per metre"), ("energy", "E", "in time", r"\frac{E}{h}", "turns per second"))[k]
    if part == 0:
        return VGroup(at(mix(name, mt(sym, size=48), size=28, bold=True), TT_X[0], y), at(lab(where, 26, INK), TT_X[1], y))
    if part == 1:
        return at(mix(mt(tex, size=56, color=PURPLE), unit, size=26), TT_X[2], y)
    xs = np.linspace(-3.4, 1.6, 8)
    ax = Arrow([-3.9, y - 1.3, 0], [2.2, y - 1.3, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.15)
    return VGroup(*[phasor([x, y - 0.85], (0.9, -0.9)[k] * i, 1.0, r=0.27, ring=True) for i, x in enumerate(xs)], ax,
                  left_at(lab(("position", "time")[k], 22), 2.4, y - 1.3))


@slide("Momentum does the same thing along the line.", "Momentum and energy")
def de2(s):
    yield [FadeIn(tt_head())]
    yield [FadeIn(tt_row(0, 0)), FadeIn(tt_row(0, 2))]
    yield [FadeIn(tt_row(0, 1))]


@slide("A state of definite energy turns its phase a certain number of times per second.", "Momentum and energy")
def de3(s):
    s.add(tt_head(), *[tt_row(0, k) for k in range(3)])
    yield [FadeIn(tt_row(1, 0)), FadeIn(tt_row(1, 2))]
    yield [FadeIn(tt_row(1, 1))]


def packet(c, L=1.6, lam=0.35, color=ORANGE):
    c = P(c[0], c[1])
    f = lambda t: c + RIGHT * (t - L / 2) + UP * 0.25 * np.sin(2 * PI * t / lam) * np.exp(-((t - L / 2) / (L / 3.2)) ** 2)
    return ParametricFunction(f, t_range=[0, L], color=color, stroke_width=4)


def light_rule():
    return VGroup(packet([-5.6, 1.2]), packet([-3.6, 1.2]), packet([-1.6, 1.2]), at(lab("light arrives in packets", 24, ORANGE), -3.6, 0.4),
                  at(mt(r"E = h\,f", size=84, color=PURPLE), 3.4, 1.2),
                  at(words("each packet's energy: Planck's constant times the light's frequency f, the number of turns per second", 36, 22, INK, ORIGIN), 3.4, -0.3))


@slide("The rule for energy comes from light.", "Borrowed from light")
def de4(s):
    g = light_rule()
    yield [FadeIn(at(lab("the rule for energy comes from light", 24, INK, True), 0, 2.4))]
    yield [FadeIn(g[:4])]
    yield [FadeIn(g[4:])]


@slide("De Broglie applied the same rule to matter.", "Borrowed from light")
def de5(s):
    s.add(light_rule(), at(lab("the rule for energy comes from light", 24, INK, True), 0, 2.4))
    yield [FadeIn(at(T("de Broglie applied the same rule to matter", 28, BLUE, True), 0, -1.7))]
    yield [FadeIn(at(card("an assumption, which experiment has confirmed ever since", 10.6, 0.9, TEAL, 28), 0, -2.9))]


ST_XS = np.arange(-4.5, 4.6, 0.9)
ST_LEN = np.exp(-(ST_XS / 3.2) ** 2)


def st_row(turn, y, r=0.4):
    return VGroup(*[phasor([x, y], 0.8 * x + turn, l, r=r, ring=True, width=4) for x, l in zip(ST_XS, ST_LEN)])


def st_tags(y0, y1):
    return VGroup(right_at(lab("now", 22), -5.3, y0), right_at(lab("a moment later", 22), -5.3, y1))


@slide("Now look at what the turning does.", "Every arrow turns together")
def de6(s):
    yield [FadeIn(st_row(0, 1.4)), FadeIn(st_tags(1.4, 0.2)[0]), FadeIn(left_at(lab("a state of definite energy: its amplitudes", 24, BLUE), -4.9, 2.35))]
    t = ValueTracker(0.0)
    row = always_redraw(lambda: st_row(t.get_value(), 0.2))
    yield [FadeIn(row), FadeIn(st_tags(1.4, 0.2)[1]), t.animate.set_value(-1.2), FadeIn(at(T("every amplitude turns together", 26, INK, True), 0, -1.0))]
    yield [FadeIn(at(lab("every arrow turns by the same angle", 24, ORANGE), 0, -1.7))]


@slide("So no length changes, and no angle between arrows changes.", "A stationary state")
def de7(s):
    s.add(st_row(0, 1.9, 0.36), st_row(-1.2, 1.0, 0.36), st_tags(1.9, 1.0))
    yield [FadeIn(at(lab("no length changes, and no angle between arrows changes", 24, INK), 0, 0.2))]
    ax = Axes(x_range=[-5.6, 5.6, 1], y_range=[0, 1.1, 1], x_length=11.2, y_length=1.4, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([0, -1.3, 0])
    d = ax.plot(lambda x: np.exp(-2 * (x / 3.2) ** 2), x_range=[-5.6, 5.6], color=TEAL, stroke_width=5)
    ax.y_axis.set_opacity(0)
    yield [Create(ax), Create(d), FadeIn(at(lab("so no chance changes", 24, TEAL, True), 4.6, -0.6)),
           FadeIn(right_at(lab("position", 22), 5.6, -2.3)), FadeIn(left_at(lab("chance", 22, TEAL), -5.6, -0.75))]
    yield [FadeIn(at(pill("a stationary state", BLUE, 28), -3.4, -3.1)), FadeIn(left_at(lab("it looks the same at every moment", 24, INK), -1.4, -3.1))]


# ================================================================== a state that moves
deck.part("A state that moves")


@slide("A state that moves.", "One energy, or two")
def mv1(s):
    yield hold()
    yield [FadeIn(at(card("a state of one energy\nstands still", 6.0, 1.6, MUTED, 28), -3.6, 0.3))]
    yield [FadeIn(at(card("mix two energies,\nand the state does change", 6.0, 1.6, ORANGE, 28), 3.6, 0.3), shift=UP * 0.15)]


def even_field(cx=2.8, cy=0.3):
    g = VGroup(*[Line([cx + k * 0.6, cy - 1.6, 0], [cx + k * 0.6, cy + 1.6, 0], color=LINE, stroke_width=3) for k in (-2.5, -1.5, -0.5, 0.5, 1.5, 2.5)])
    c = P(cx, cy)
    d = np.array([LEAN[0], LEAN[1], 0])
    g.add(Arrow(c - d * 0.7, c + d * 0.7, buff=0, color=BLUE, stroke_width=7, tip_length=0.2),
          CurvedArrow(c + P(0.95, -0.2), c + P(0.35, 0.95), angle=PI / 2.2, color=ORANGE, stroke_width=4, tip_length=0.15),
          lab("an even vertical magnetic field", 24, INK).move_to([cx, cy + 2.0, 0]))
    return g


@slide("Take our tilted atoms again, leaning sixty degrees to the right.", "The tilted atoms in an even field")
def mv2(s):
    yield [FadeIn(dial([-4.8, 0.3], 60, r=1.2)), FadeIn(at(words("our tilted atoms: leaning 60° to the right", 22, 22, BLUE, ORIGIN), -4.8, -1.6))]
    yield [GrowArrow(arrow(P(-3.2, 0.3), P(0.6, 0.3))), FadeIn(even_field())]
    yield [FadeIn(at(lab("an even field only twists the atoms", 24, ORANGE), 2.8, -1.75))]
    yield [FadeIn(at(lab("it doesn't sort them or measure them", 24, INK), 2.8, -2.4))]


def ud_bars():
    return VGroup(bars(-5.6, -1.2, [0.75, 0.25], ["up", "down"], ["75%", "25%"], hmax=2.6, w=0.9, gap=1.6),
                  at(lab("the tilted atoms' chances", 22, TEAL), -4.8, 2.0))


def levels():
    g = VGroup(Arrow(P(1.0, -1.7), P(1.0, 2.0), buff=0, color=MUTED, stroke_width=3, tip_length=0.16), lab("energy", 22).move_to([1.0, 2.3, 0]))
    for y, name, d in ((0.5, "pointing down", DOWN), (-0.5, "pointing up", UP)):
        g.add(Line(P(1.6, y), P(4.2, y), color=INK, stroke_width=5), atom([4.8, y], d, 0.3, width=4), left_at(lab(name, 22, INK), 5.3, y))
    return g


@slide("Their chances are seventy-five percent for up and twenty-five percent for down.", "Two slightly different energies")
def mv3(s):
    yield [FadeIn(ud_bars())]
    yield [FadeIn(levels()), FadeIn(at(words("like a compass needle: slightly different energies pointing up and pointing down", 34, 22, INK, ORIGIN), 3.6, -2.6))]


@slide("The energy depends only on the up or down reading.", "Up and down have definite energies")
def mv4(s):
    yield [FadeIn(at(lab("the energy depends only on the up-or-down reading", 24, INK), 0, 2.2))]
    r = mix(mt(r"\hat H", size=64, color=PURPLE), "has the same eigenstates as", mt(r"\hat Z", size=64, color=PURPLE), size=28)
    yield [FadeIn(at(r, 0, 0.9)), FadeIn(at(lab("the energy operator", 22, PURPLE), r[0].get_x() - 0.9 - r.get_x(), 0.1)),
           FadeIn(at(lab("the vertical operator", 22, PURPLE), r[2].get_x() + 0.9 - r.get_x(), 0.1))]
    yield [FadeIn(at(VGroup(schip("up", 30), schip("down", 30)).arrange(RIGHT, buff=0.6), 0, -1.3)),
           FadeIn(at(T("the states of definite energy here", 26, BLUE, True), 0, -2.3))]


UP_C, DN_C, CB_C = np.array([-5.6, 0.7, 0]), np.array([-3.0, 0.7, 0]), np.array([3.4, 0.5, 0])
SR = 1.0


def spin_pair(au, ad):
    return VGroup(phasor(UP_C, au, 0.866, r=SR, width=6), phasor(DN_C, ad, 0.5, r=SR, width=6))


def pair_names():
    return VGroup(T("up", 24, INK, True).next_to(Circle(radius=SR).move_to(UP_C), DOWN, buff=0.15),
                  T("down", 24, INK, True).next_to(Circle(radius=SR).move_to(DN_C), DOWN, buff=0.15))


def both(au, ad, r=1.5):
    """The two arrows drawn from one centre, with the angle between them."""
    g = VGroup(Circle(radius=r, color=LINE, stroke_width=2).move_to(CB_C), varrow(CB_C, CB_C + 0.866 * r * uvec(au)), varrow(CB_C, CB_C + 0.5 * r * uvec(ad)))
    if abs(au - ad) > 0.05:
        g.add(Arc(radius=0.45, start_angle=au, angle=ad - au, arc_center=CB_C, color=ORANGE, stroke_width=5))
    return g


@slide("Here's what happens next.", "Two arrows, two rates")
def mv5(s):
    au, ad = ValueTracker(0.0), ValueTracker(0.0)
    pair = always_redraw(lambda: spin_pair(au.get_value(), ad.get_value()))
    yield [FadeIn(pair), FadeIn(pair_names()), FadeIn(at(lab("the state: a mix of up and down", 24, BLUE), -4.3, 2.3))]
    yield hold()
    yield [au.animate(rate_func=linear).set_value(-0.9), ad.animate(rate_func=linear).set_value(-2.3),
           FadeIn(at(words("each part turns its phase at its own energy's rate, and the two rates differ slightly", 34, 22, INK, ORIGIN), -4.3, -1.6))]
    yield [FadeIn(both(-0.9, -2.3)), FadeIn(at(T("so the angle between the two arrows grows steadily", 24, ORANGE, True), 3.4, -1.6))]


# The cone of docs/manim/page_diagrams.py, SpinPrecession: R / height = tan 60 degrees.
CN_O = np.array([-3.7, -1.9, 0])
CN_TOP = np.array([-3.7, -0.745, 0])
CN_R, CN_r = 2.0, 0.57
CN_STOPS = [("right", 0, RIGHT, "93%"), ("back", 90, UR, None), ("left", 180, LEFT, "7%"), ("front", 270, None, None)]


def cn_pt(deg):
    t = np.radians(deg)
    return CN_TOP + np.array([CN_R * np.cos(t), CN_r * np.sin(t), 0])


def cone():
    ftip = CN_TOP + np.array([0, CN_r + 1.3, 0])
    return VGroup(Arrow(CN_O, ftip, buff=0, color=MUTED, stroke_width=4, max_tip_length_to_length_ratio=0.05), lab("field", 22).move_to(ftip + LEFT * 0.6 + DOWN * 0.15),
                  Ellipse(width=2 * CN_R, height=2 * CN_r, color=MUTED, stroke_width=2).move_to(CN_TOP),
                  DashedVMobject(Line(CN_O, cn_pt(180), color=MUTED, stroke_width=2).set_opacity(0.5), num_dashes=14),
                  DashedVMobject(Line(CN_O, cn_pt(0), color=MUTED, stroke_width=2).set_opacity(0.5), num_dashes=14))


def cn_arrow(deg):
    return Arrow(CN_O, cn_pt(deg), buff=0, color=BLUE, stroke_width=6, max_tip_length_to_length_ratio=0.06)


def cn_stops():
    g = VGroup()
    for name, deg, d, ch in CN_STOPS:
        t = lab(name, 22, INK)
        if d is None:
            t.next_to(cn_pt(deg), LEFT, buff=0.25).shift(DOWN * 0.05)
            g.add(BackgroundRectangle(t, color=WHITE, fill_opacity=1, buff=0.06))
        else:
            t.next_to(cn_pt(deg), d, buff=0.22)
        g.add(Dot(cn_pt(deg), color=BLUE, radius=0.09), t)
    return g


def cn_chances():
    return VGroup(lab("93% right", 22, TEAL, True).next_to(cn_pt(0), RIGHT, buff=0.22).shift(DOWN * 0.42),
                  lab("7% right", 22, TEAL, True).next_to(cn_pt(180), LEFT, buff=0.22).shift(DOWN * 0.42))


@slide("In the last chapter, that angle set which way the atom leans.", "The lean swings round the field")
def mv6(s):
    yield [FadeIn(cone()), FadeIn(cn_arrow(0)), FadeIn(left_at(words("the angle between the two arrows sets which way the atom leans (last chapter)", 30, 24, ORANGE), 1.2, 1.6))]
    phi = ValueTracker(0.0)
    ar = always_redraw(lambda: cn_arrow(phi.get_value()))
    s.add(ar)
    yield [phi.animate(rate_func=linear).set_value(360), FadeIn(left_at(words("so the lean swings round the field, like a spinning top", 30, 24, BLUE), 1.2, 0.1))]
    yield [FadeIn(cn_stops()), FadeIn(left_at(lab("right, back, left and front in turn", 24, INK), 1.2, -1.2))]


def ch_axes():
    ax = Axes(x_range=[0, 1, 0.25], y_range=[0, 1, 0.5], x_length=5.4, y_length=3.2, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([4.2, -0.3, 0])
    g = VGroup(ax, lab("chance of “right”", 22, TEAL, True).move_to([4.2, 1.85, 0]), lab("one full turn of the lean", 22).move_to([4.2, -2.8, 0]))
    for u, name in ((0, "right"), (0.25, "back"), (0.5, "left"), (0.75, "front"), (1, "right")):
        g.add(lab(name, 22).move_to(ax.c2p(u, 0) + DOWN * 0.32))
    return ax, g


CH_F = lambda u: 0.5 + np.sqrt(3) / 4 * np.cos(2 * np.pi * u)


def ch_curve(ax):
    return VGroup(ax.plot(CH_F, x_range=[0, 1], color=TEAL, stroke_width=5), *[Dot(ax.c2p(u, CH_F(u)), color=BLUE, radius=0.07) for u in (0, 0.25, 0.5, 0.75, 1)])


def ch_ends(ax):
    return VGroup(T("93%", 24, TEAL, True).next_to(ax.c2p(0, CH_F(0)), UR, buff=0.08), T("7%", 24, TEAL, True).next_to(ax.c2p(0.5, CH_F(0.5)), UP, buff=0.15))


@slide("A sideways magnet's chance of right rises and falls with it.", "The chance of “right” rises and falls")
def mv7(s):
    s.add(cone(), cn_arrow(0), cn_stops())
    ax, frame = ch_axes()
    yield [FadeIn(frame), Create(ch_curve(ax)[0]), FadeIn(ch_curve(ax)[1:])]
    yield [FadeIn(cn_chances()), FadeIn(ch_ends(ax))]
    yield [FadeIn(at(words("up and down stay 75% and 25% throughout: they only see the lengths of the arrows", 44, 24, INK, ORIGIN), -3.6, -3.4))]


# ================================================================== the Schrodinger equation
deck.part("The Schrödinger equation")


def e_parts(turning=False):
    g = VGroup()
    for k, (a, f) in enumerate(((0.4, 0.8), (1.9, 0.6), (-0.8, 0.5))):
        x = -1.2 + 2.8 * k
        g.add(phasor([x, 0.5], a, f, r=0.75, width=6), T(f"energy {k + 1}", 22, INK).move_to([x, -0.55, 0]))
        if turning:
            g.add(Arc(radius=0.95, start_angle=1.1, angle=-(0.7, 1.15, 1.6)[k], arc_center=P(x, 0.5), color=ORANGE, stroke_width=4).add_tip(tip_length=0.16, tip_width=0.16))
    if not turning:
        g.add(*[at(T("+", 34, INK), 0.2 + 2.8 * k, 0.5) for k in range(2)])
    return g


@slide("The Schrodinger equation.", "A mix of definite energies")
def se1(s):
    yield hold()
    st = at(card("any state", 2.6, 0.9, BLUE, 28), -5.4, 0.5)
    yield [FadeIn(st), GrowArrow(arrow(P(-4.0, 0.5), P(-2.2, 0.5))), FadeIn(e_parts()), FadeIn(at(lab("a mix of states of definite energy", 24, INK), 1.6, 2.1))]
    yield [FadeIn(e_parts(True)[2::3]), FadeIn(at(lab("each part turns its phase at its own rate", 24, ORANGE), 1.6, -1.4))]
    yield [FadeIn(at(lab("as the spinning atom showed, that decides how the whole state moves", 24, INK), 0, -2.5))]


def se_f(size=96):
    """i hbar dPsi/dt = H-hat Psi."""
    return mt(r"i\hbar\,\frac{\partial\Psi}{\partial t}", "=", r"\hat H\,\Psi", size=size, color=PURPLE)


@slide("Written as one equation, it's the Schrodinger equation.", "The Schrödinger equation")
def se2(s):
    m = at(se_f(), 0, 0.9)
    yield [FadeIn(m), FadeIn(at(pill("the Schrödinger equation", PURPLE, 28), 0, 2.4)),
           FadeIn(at(mix(mt(r"\Psi", size=44, color=PURPLE), ": the wave function as it changes in time", size=22, color=MUTED), 0, -2.9))]
    yield hold()
    b1 = Brace(m[0], DOWN, color=ORANGE)
    yield [FadeIn(b1), FadeIn(at(words("the rate of change of the wave function in time, times i h-bar", 28, 22, INK, ORIGIN), b1.get_x() - 1.4, -1.4))]
    b2 = Brace(m[2], DOWN, color=ORANGE)
    yield [FadeIn(b2), FadeIn(at(words("the energy operator applied to the wave function", 26, 22, INK, ORIGIN), b2.get_x() + 1.6, -1.4))]


def se_top():
    return at(se_f(52), 0, 2.1)


def def_e():
    return at(mix("a state of definite energy", mt("E", size=48, color=BLUE), size=24, color=BLUE), 0, 1.1)


def chk_right():
    m = mt(r"\hat H\,\Psi", "=", r"E\,\Psi", size=52)
    return VGroup(right_at(lab("right side:", 24, INK, True), -3.6, 0.25), left_at(m, -3.2, 0.25), tick(left_at(m.copy(), -3.2, 0.25)),
                  left_at(lab("an eigenstate of the energy operator", 22), 1.2, 0.25))


@slide("Let's check it on a state of definite energy.", "Checking a state of definite energy")
def se3(s):
    s.add(se_top())
    yield [FadeIn(def_e())]
    yield [FadeIn(at(mix("both sides come out as", mt(r"E\,\Psi", size=52, color=ORANGE), ", the energy times the state", size=24), 0, -1.6))]
    yield [FadeIn(chk_right())]


CL_Y = [0.3, -1.05, -2.5]


def chk_left(stage):
    rows = [(r"\frac{\partial\Psi}{\partial t} = -\frac{iE}{\hbar}\,\Psi", "the state itself, times a multiple of i", INK, 48),
            (r"\frac{d\psi_p}{dx} = \frac{ip}{\hbar}\,\psi_p", "just like the slope of a momentum wave", MUTED, 38),
            (r"i\hbar\,\frac{\partial\Psi}{\partial t} = E\,\Psi", "times i h-bar: the energy times the state", PURPLE, 56)]
    tex, note, color, size = rows[stage]
    y = CL_Y[stage]
    m = left_at(mt(tex, size=size, color=color), -3.2, y)
    g = VGroup(m, left_at(lab(note, 22, MUTED if stage == 1 else INK), 1.6, y))
    if stage == 2:
        g.add(check().next_to(m, RIGHT, buff=0.25))
    return g


@slide("The left side does because of the steady turning.", "Checking a state of definite energy")
def se4(s):
    s.add(chk_right().shift(UP * 1.25), def_e().shift(UP * 1.2))
    yield [FadeIn(right_at(lab("left side:", 24, INK, True), -3.6, CL_Y[0])), FadeIn(right_at(lab("steady turning", 22, ORANGE), -3.6, CL_Y[0] - 0.45))]
    for k in range(3):
        yield [FadeIn(chk_left(k))]


THREE = ["the state fixes its future", "the total chance stays one", "energy and momentum look alike"]
PROP_X = [-4.85, 0.0, 4.85]
PROP_C = [BLUE, TEAL, PURPLE]


def prop_frame(k, titled=True):
    g = VGroup(at(card(None, 4.6, 4.3, PROP_C[k]), PROP_X[k], -1.45), at(num_pill(k + 1, PROP_C[k], 24), PROP_X[k] - 1.9, 0.3))
    if titled:
        g.add(at(words(THREE[k], 20, 24, PROP_C[k], ORIGIN), PROP_X[k] + 0.3, 0.1))
    return g


@slide("Every state is a mix of these states, so every state obeys the equation.", "Every state obeys it")
def se5(s):
    s.add(at(se_f(44), 0, 2.25))
    yield [FadeIn(at(lab("every state is a mix of these states, so every state obeys the equation", 24, INK, True), 0, 1.27))]
    yield [FadeIn(VGroup(*[prop_frame(k, False) for k in range(3)])), FadeIn(at(lab("the equation tells us three things", 22, INK), 0, 0.9))]


def prop_body(k, part):
    x = PROP_X[k]
    if k == 0:
        return [at(words("only the first rate of change in time, with no acceleration", 26, 22, INK, ORIGIN), x, -1.25),
                at(words("know the state now, and you know it at every later time", 26, 22, BLUE, ORIGIN), x, -2.8)][part]
    if k == 1:
        return [VGroup(phasor([x - 0.8, -0.95], 0.3, 0.9, r=0.42), phasor([x + 0.8, -0.95], -0.6, 0.6, r=0.42),
                       at(words("each energy part only turns its phase, and keeps its length", 24, 22, INK, ORIGIN), x, -2.0)),
                at(words("so the squares still add up to one", 24, 22, TEAL, ORIGIN), x, -3.05)][part]
    return [VGroup(at(mt(r"i\hbar\,\frac{\partial}{\partial t}", size=44, color=PURPLE), x, -0.95), at(lab("stands for the energy", 22, INK), x, -1.65)),
            VGroup(at(mt(r"-i\hbar\,\frac{d}{dx}", size=44, color=PURPLE), x, -2.45), at(lab("stands for the momentum", 22, INK), x, -3.15))][part]


@slide("First, the state fixes its future.", "Three things the equation tells us")
def se6(s):
    s.add(se_top(), *[prop_frame(k, False) for k in range(3)])
    yield [FadeIn(prop_frame(0)[2])]
    yield [FadeIn(prop_body(0, 0))]
    yield [FadeIn(prop_body(0, 1))]


@slide("Second, the total chance stays one.", "Three things the equation tells us")
def se7(s):
    s.add(se_top(), prop_frame(0), prop_frame(1, False), prop_frame(2, False), prop_body(0, 0), prop_body(0, 1))
    yield [FadeIn(prop_frame(1)[2])]
    yield [FadeIn(prop_body(1, 0))]
    yield [FadeIn(prop_body(1, 1))]


@slide("Third, energy and momentum look alike.", "Three things the equation tells us")
def se8(s):
    s.add(se_top(), prop_frame(0), prop_frame(1), prop_frame(2, False), *[prop_body(k, p) for k in (0, 1) for p in (0, 1)])
    yield [FadeIn(prop_frame(2)[2])]
    yield [FadeIn(prop_body(2, 0))]
    yield [FadeIn(prop_body(2, 1))]


# ================================================================== averages follow chapter one
deck.part("Averages follow chapter one")


def cl_rule(size=76):
    return mt(r"\frac{df}{dt} = \{f, H\}", size=size, color=MUTED)


def q_rule(size=76):
    return mt(r"\frac{d\langle A\rangle}{dt}", "=", r"\frac{\langle[\hat A, \hat H]\rangle}{i\hbar}", size=size, color=PURPLE)


@slide("Averages follow chapter one.", "The bracket's other job")
def avc1(s):
    yield hold()
    yield [FadeIn(at(lab("chapter 1's bracket had one more job", 24, INK), 0, 2.2))]
    yield [FadeIn(at(T("it told us how any quantity changes in time", 26, INK, True), 0, 1.4))]
    yield [FadeIn(at(cl_rule(84), 0, -0.4)), FadeIn(at(lab("its rate of change: the quantity's bracket with the Hamiltonian", 24, INK), 0, -1.9))]


@slide("The Schrodinger equation gives the quantum version, for averages.", "The quantum version, for averages")
def avc2(s):
    yield [FadeIn(at(lab("the Schrödinger equation gives the quantum version, for averages", 24, INK), 0, 2.2))]
    b = bars(-5.2, -1.6, [0.7, 0.3], ["one result", "another"], hmax=2.4, w=0.9, gap=2.0)
    yield [FadeIn(b), FadeIn(left_at(words("before a measurement: no single result, only chances", 30, 24, INK), -1.6, 0.6))]
    yield [FadeIn(left_at(mix("so what changes smoothly is its average,", mt(r"\langle A\rangle", size=56, color=ORANGE), size=26, bold=True), -1.6, -1.0))]


@slide("Here's the rule.", "How an average changes")
def avc3(s):
    yield hold()
    m = at(q_rule(84), 0, 0.4)
    c = mt(r"[\hat A, \hat H]", size=84, color=PURPLE).move_to(m[2])
    yield [FadeIn(c), FadeIn(at(lab("the commutator of the quantity with the energy operator", 24, INK), 0, 2.2))]
    yield [ReplacementTransform(c, m[2]), FadeIn(note_to("its average, divided by i h-bar", m[2], m[2].get_x() + 1.2, -1.3, ORANGE, 24))]
    yield [FadeIn(m[0]), FadeIn(m[1]), FadeIn(at(T("that's the rate of change of the quantity's average", 26, PURPLE, True), 0, -2.6))]


@slide("It's chapter one's rule again, with the same swap as before.", "Chapter 1's rule again")
def avc4(s):
    yield [FadeIn(at(card(None, 5.6, 3.0, MUTED), -3.9, 0.6)), FadeIn(at(card(None, 7.4, 3.0, PURPLE), 3.3, 0.6)),
           FadeIn(at(lab("chapter 1", 24, MUTED, True), -3.9, 1.75)), FadeIn(at(lab("quantum", 24, PURPLE, True), 3.3, 1.75)),
           FadeIn(at(cl_rule(60), -3.9, 0.3)), FadeIn(at(q_rule(60), 3.3, 0.3))]
    sw = VGroup(mt(r"\{\ \ ,\ \}", size=60, color=MUTED), mt(r"\longrightarrow", size=52), mt(r"\frac{[\ \ ,\ ]}{i\hbar}", size=60, color=PURPLE)).arrange(RIGHT, buff=0.4)
    yield [FadeIn(at(sw, -1.8, -2.4)), FadeIn(left_at(words("the same swap as before: the bracket becomes a commutator divided by i h-bar", 30, 22, INK), 1.6, -2.4))]


def ham_avg(k):
    y = (1.2, -1.2)[k]
    tex = (r"\frac{d\langle x\rangle}{dt} = \frac{\langle p\rangle}{m}", r"\frac{d\langle p\rangle}{dt} = \langle\text{force}\rangle")[k]
    note = ("the average position changes at the average momentum divided by the mass", "the average momentum changes at the average force")[k]
    return VGroup(at(mt(tex, size=64, color=PURPLE), -3.6, y), left_at(words(note, 30, 24, INK), 0.4, y))


@slide("For position and momentum, it gives Hamilton's equations for the averages.", "Hamilton's equations for the averages")
def avc5(s):
    yield [FadeIn(at(lab("for position and momentum: Hamilton's equations, for the averages", 24, INK, True), 0, 2.4))]
    yield [FadeIn(ham_avg(0))]
    yield [FadeIn(ham_avg(1))]


def force_pic(stage):
    ax = Axes(x_range=[-3, 3, 1], y_range=[0, 4.5, 1], x_length=7.0, y_length=3.6, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([-3.4, -0.4, 0])
    V = lambda x: 0.45 * x * x + 0.3
    g = VGroup(ax, ax.plot(V, x_range=[-3, 3], color=MUTED, stroke_width=4), lab("potential energy", 22).move_to(ax.c2p(0, 4.4)),
               lab("position", 22).move_to(ax.c2p(2.5, -0.4)))
    if stage == 0:
        w = ax.plot(lambda x: V(x) + 1.0 * np.exp(-(x + 1.2) ** 2 / 0.5), x_range=[-2.8, 0.4], color=BLUE, stroke_width=4)
        g.add(w, lab("where the particle might be", 22, BLUE).move_to(ax.c2p(-1.3, -0.4)),
              *[Line(ax.c2p(x - 0.3, V(x) - 0.3 * 0.9 * x), ax.c2p(x + 0.3, V(x) + 0.3 * 0.9 * x), color=ORANGE, stroke_width=5) for x in (-2.1, -1.2, -0.3)])
    else:
        x = 1.5
        w = ax.plot(lambda u: V(u) + 1.3 * np.exp(-(u - x) ** 2 / 0.004), x_range=[1.3, 1.7], color=BLUE, stroke_width=4)
        g.add(w, Line(ax.c2p(x - 0.5, V(x) - 0.5 * 0.9 * x), ax.c2p(x + 0.5, V(x) + 0.5 * 0.9 * x), color=ORANGE, stroke_width=5),
              lab("a narrow state", 22, BLUE).move_to(ax.c2p(1.5, 3.2)))
    return g


@slide("That's the force averaged over where the particle might be.", "The average force")
def avc6(s):
    yield [FadeIn(force_pic(0)), FadeIn(left_at(words("the average force: the force, set by the slope of the potential energy, averaged over where the particle might be", 34, 24, ORANGE), 0.9, 1.0))]
    yield [FadeIn(force_pic(1)[4:]), FadeIn(left_at(words("for a narrow state like a ball's: the force at the average position", 34, 24, INK), 0.9, -1.4))]


@slide("This is why chapter one works for a ball.", "Why chapter 1 works for a ball")
def avc7(s):
    path = VMobject(color=LINE, stroke_width=3).set_points_smoothly([[-6.5, -1.4, 0], [-4.0, 0.6, 0], [-1.0, 1.2, 0], [2.0, 0.5, 0], [4.5, -1.5, 0]])
    b = Dot([-6.5, -1.4, 0], radius=0.22, color=BLUE)
    yield [Create(path), FadeIn(b), MoveAlongPath(b, path), FadeIn(at(lab("a ball", 24, BLUE), 5.3, -1.5))]
    yield [FadeIn(at(lab("its spreads can be far too small to notice", 24, INK), 0, -2.3))]
    yield [FadeIn(at(card("the average is all we ever see, and the averages follow chapter 1's equations", 13.0, 0.9, PURPLE, 26), 0, -3.3))]


# ================================================================== where this goes next
deck.part("Where this goes next")


def sum_card(k):
    y = (1.7, -0.3, -2.4)[k]
    box = at(card(None, 13.0, 1.7, (BLUE, PURPLE, PURPLE)[k]), 0, y)
    if k == 0:
        body = at(words("a measurable quantity becomes an operator, with its own eigenstates and eigenvalues", 60, 26, INK, ORIGIN), 0, y)
    elif k == 1:
        body = at(VGroup(xp_comm(52), words("position and momentum don't commute, so they can't both be exact", 34, 24, INK), unc_f(48)).arrange(RIGHT, buff=0.45), 0, y)
    else:
        body = at(VGroup(words("the energy operator moves the state forward", 24, 26, INK), se_f(56)).arrange(RIGHT, buff=0.7), 0, y)
    return VGroup(box, body)


@slide("Where this goes next.", "Summing up")
def end1(s):
    yield hold()
    yield hold()
    yield [FadeIn(sum_card(0), shift=UP * 0.15)]


@slide("Position and momentum don't commute, and their commutator is i h-bar.", "Summing up")
def end2(s):
    s.add(sum_card(0))
    c = sum_card(1)
    yield [FadeIn(c[0]), FadeIn(c[1][:2])]
    yield [FadeIn(c[1][2])]
    yield [FadeIn(sum_card(2), shift=UP * 0.15)]


def spring_icon(x, y, n=7, L=2.6):
    pts_ = [[x, y, 0]] + [[x + 0.3 + (L - 0.6) * (i + 0.5) / n, y + (0.3 if i % 2 else -0.3), 0] for i in range(n)] + [[x + L, y, 0]]
    return VGroup(Line([x, y - 0.7, 0], [x, y + 0.7, 0], color=INK, stroke_width=6), VMobject(color=MUTED, stroke_width=4).set_points_as_corners(pts_),
                  Dot([x + L + 0.3, y, 0], radius=0.3, color=BLUE))


def ladder(x, y0, n=6, gap=0.62, w=3.0):
    return VGroup(*[Line([x - w / 2, y0 + gap * i, 0], [x + w / 2, y0 + gap * i, 0], color=INK, stroke_width=5) for i in range(n)])


@slide("The next chapter, the Harmonic Oscillator, applies these rules", "Next: The Harmonic Oscillator")
def end3(s):
    yield [FadeIn(at(card("next: The Harmonic Oscillator", 7.4, 1.0, INK, 30), 0, 2.0)), FadeIn(spring_icon(-6.2, -0.6)),
           FadeIn(at(lab("these rules, applied to chapter 1's spring", 24, INK), -4.4, -2.0))]
    yield [FadeIn(at(xp_comm(48), 0.0, -0.6)), GrowArrow(arrow(P(1.6, -0.6), P(2.8, -0.6))), FadeIn(ladder(4.8, -2.2)),
           FadeIn(at(words("the spring's energies, from the commutator alone: evenly spaced steps", 38, 22, INK, ORIGIN), 3.0, -3.2))]


@slide("Further on, a chapter on fields applies the same swap", "Further on")
def end4(s):
    sw = VGroup(mt(r"\{\ \ ,\ \}", size=60, color=MUTED), mt(r"\longrightarrow", size=52), mt(r"\frac{[\ \ ,\ ]}{i\hbar}", size=60, color=PURPLE),
                T("applied to a field", 28, INK, True)).arrange(RIGHT, buff=0.45)
    yield [FadeIn(at(sw, 0, 1.4)), FadeIn(at(lab("a later chapter on fields: the same swap, from bracket to commutator", 24, INK), 0, 2.4))]
    yield [FadeIn(at(lab("the change that carries a state forward in time keeps the total chance at one", 24, INK), 0, -0.6))]
    yield [FadeIn(at(pill("unitary", PURPLE, 30), -2.6, -1.8)), FadeIn(left_at(lab("it returns in later chapters too", 24, INK), -1.2, -1.8))]

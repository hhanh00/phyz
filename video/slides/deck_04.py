"""Slides for chapter four, Special Relativity.

Every value comes from video/scripts/04-special-relativity.txt or
docs/special-relativity.md. The drawings redraw the chapter's figures in
docs/manim/ (michelson-morley, light-clock, muon-counts, train-flash,
light-cone-intervals) as animations.

Colors: ORANGE for light itself (pulses, beams, the flash, light rays, the edge
of the light cone, the bands of light, packets of light and their E = hf, p =
h/λ, E = pc), BLUE for what the platform or the ground sees and measures (the
train's 30 m/s, the 31 m/s, the ground's 6.4 millionths of a second and 1,900 m,
the muon counts, the electric field of a charge for an observer beside it),
PURPLE for the moving observer's own view (the rider on the train, the muon and
its own clock, the shrunken mountain, a traveller slower than light, the
magnetic field a passing observer sees), TEAL for what every observer agrees on
(light's speed wherever it appears as a value or a limit, the laws of physics,
the spacetime interval, the rest energy, E² − (pc)² = (mc²)², an equation that
keeps its form) and for checks that pass, RED only for a rule or prediction that
fails (everyday rules near light's speed, the expected slide of the bands, the
30 muons expected, a lopsided rule, the Schrödinger equation), INK for gamma and
other equations, MUTED and LINE for apparatus, axes, the imagined medium and its
wind, context and connectors.
"""
from manim import *

from engine import *

STEM = "04-special-relativity"
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


def words(text, chars=40, size=26, color=INK, align=LEFT):
    return W(text, chars, size, color, align=align)


_code = code


def code(text, size=26, color=INK):
    """Monospace text with each ² pulled in against its neighbours.

    Menlo sets ² small in a full-width cell, so (c Δt)² would read as (c Δt) ² with the exponent floating off.
    """
    mob = _code(text, size, color)
    if "²" not in text:
        return mob
    glyphs = mob.submobjects
    idx = []              # (glyph index, whether the next character follows without a space)
    j = -1
    for k, ch in enumerate(text):
        if ch.isspace():
            continue
        j += 1
        if ch == "²":
            idx.append((j, k + 1 < len(text) and not text[k + 1].isspace()))
    if j + 1 != len(glyphs):
        return mob
    pad = 0.025 * size / 30
    for j, joined in idx:
        if j == 0:
            continue
        g, prev = glyphs[j], glyphs[j - 1]
        gap = g.get_left()[0] - prev.get_right()[0] - pad
        if gap > 0:
            VGroup(*glyphs[j:]).shift(LEFT * gap)
        if joined and j + 1 < len(glyphs):
            gap = glyphs[j + 1].get_left()[0] - g.get_right()[0] - 2 * pad
            if gap > 0:
                VGroup(*glyphs[j + 1:]).shift(LEFT * gap)
    return mob


def mchip(text, color=INK, w=None, h=0.56, size=22):
    """engine.chip, but set with this deck's code(), so a ² sits against its bracket."""
    label = code(text, size, color)
    box = RoundedRectangle(width=w or label.width + 0.34, height=h, corner_radius=0.09, stroke_color=color,
                           stroke_width=2, fill_color=WHITE, fill_opacity=1)
    label.move_to(box)
    return VGroup(box, label)


def hold():
    """A step that adds nothing, so the next reveal waits for its sentence."""
    return [Wait()]


def eq(text, size=34, color=INK):
    return code(text, size, color)


def sci(before, exponent, after="", size=40, color=INK, bold=False):
    """Text with a power of ten whose exponent is set small and raised, e.g. sci("about 9 × 10", "13", "joules").

    Unicode superscript digits sit at different heights in Helvetica Neue, so 10¹³ would read like 10 to the 1 to the 3.
    """
    base = T(before, size, color, bold)
    exp = T(exponent.replace("-", "−"), size * 0.6, color, bold)
    exp.next_to(base, RIGHT, buff=0.04).align_to(base, UP).shift(UP * 0.12 * size / 40)
    group = VGroup(base, exp)
    if after:
        group.add(T(after, size, color, bold).next_to(exp, RIGHT, buff=0.12 * size / 40).align_to(base[-1], DOWN))
    return group


def subbed(base, sub, size=30, color=INK):
    """Monospace text with a lowered, smaller subscript, such as p with x."""
    b = code(base, size, color)
    s_ = code(sub, size * 0.62, color)
    s_.next_to(b, RIGHT, buff=0.03).align_to(b, DOWN).shift(DOWN * 0.08 * size / 30)
    return VGroup(b, s_)


def clock(s, rate=1.0):
    """Time that keeps running during holds, so the things drawn from it keep moving."""
    t = ValueTracker(0.0)
    t.rate = rate
    t.add_updater(lambda m, dt: m.increment_value(m.rate * dt))
    s.add(t)
    return t


def tri(u):
    """A triangle wave between 0 and 1, for things bouncing between walls."""
    return abs((u % 2.0) - 1.0)


def bounce(u):
    """0 at u = 0, 1 at u = 1, back to 0 at u = 2."""
    return 1.0 - tri(u)


def hline(x0, x1, y, color=LINE, width=3):
    return Line(P(x0, y), P(x1, y), color=color, stroke_width=width)


def axis_arrow(a, b, color=MUTED, width=3):
    return Arrow(P(*a), P(*b), buff=0, color=color, stroke_width=width, tip_length=0.16, max_tip_length_to_length_ratio=0.2)


def tick(mob, color=TEAL, buff=0.2):
    return check(color).next_to(mob, RIGHT, buff=buff)


def xmark(mob, size=0.42, buff=0.2):
    return cross(Square(size).next_to(mob, RIGHT, buff=buff), RED, 6)


def hollow():
    """An invisible placeholder, so a redrawn group is never empty."""
    return Dot(ORIGIN, radius=0.001, fill_opacity=0, stroke_width=0)


# ------------------------------------------------------------------ people, trains, clocks, rulers

def person(x, y, color=INK, h=1.0, width=3):
    """A stick figure standing with its feet at (x, y)."""
    def p(a, b):
        return P(x + a * h, y + b * h)
    return VGroup(Circle(radius=0.11 * h, color=color, stroke_width=width).move_to(p(0, 0.87)),
                  Line(p(0, 0.76), p(0, 0.38), color=color, stroke_width=width),
                  Line(p(0, 0.38), p(-0.15, 0), color=color, stroke_width=width),
                  Line(p(0, 0.38), p(0.15, 0), color=color, stroke_width=width),
                  Line(p(-0.2, 0.42), p(0, 0.66), color=color, stroke_width=width),
                  Line(p(0.2, 0.42), p(0, 0.66), color=color, stroke_width=width))


def carriage(cx, cy, w=5.0, h=1.4, color=INK, fill=PALE, opacity=1.0):
    body = RoundedRectangle(width=w, height=h, corner_radius=0.12, stroke_color=color, stroke_width=3,
                            fill_color=fill, fill_opacity=opacity).move_to(P(cx, cy))
    wheels = VGroup(*[Circle(radius=0.15, color=color, stroke_width=3, fill_color=WHITE, fill_opacity=1)
                      .move_to(P(cx + f * w, cy - h / 2 - 0.12)) for f in (-0.32, 0.32)])
    return VGroup(body, wheels)


def poles(t, y0, y1, speed, gap=2.6, x0=-7.4, x1=7.4, color=LINE):
    """Scenery sliding backwards past a train that stays put on screen."""
    def draw():
        g = VGroup(hollow())
        span = x1 - x0
        k = 0
        while k * gap < span:
            x = x0 + ((k * gap - speed * t.get_value()) % span)
            g.add(Line(P(x, y0), P(x, y1), color=color, stroke_width=4))
            k += 1
        return g
    return always_redraw(draw)


def sleepers(t, y, speed, x0, x1, gap=0.5):
    """Short ties on a track sliding backwards, so a train drawn in place reads as moving."""
    def draw():
        g = VGroup(hollow())
        span = x1 - x0
        k = 0
        while k * gap < span:
            x = x0 + ((k * gap - speed * t.get_value()) % span)
            g.add(Line(P(x, y - 0.12), P(x, y + 0.02), color=MUTED, stroke_width=4))
            k += 1
        return g
    return always_redraw(draw)


def elbow(a, y, b, color=MUTED):
    """An arrow from a down to height y, across, then down into b."""
    a, b = np.array(a), np.array(b)
    return VGroup(Line(a, P(a[0], y), color=color, stroke_width=4), Line(P(a[0], y), P(b[0], y), color=color, stroke_width=4),
                  Arrow(P(b[0], y), b, buff=0, color=color, stroke_width=4, tip_length=0.2, max_tip_length_to_length_ratio=0.5))


def dial(c, r=0.45, ang=PI / 2, color=INK, hand=None):
    c = P(*c)
    hand = hand or color
    g = VGroup(Circle(radius=r, color=color, stroke_width=3, fill_color=WHITE, fill_opacity=1).move_to(c))
    for k in range(12):
        a = k * TAU / 12
        u = np.array([np.cos(a), np.sin(a), 0])
        g.add(Line(c + 0.78 * r * u, c + 0.93 * r * u, color=color, stroke_width=2))
    g.add(Line(c, c + 0.72 * r * np.array([np.cos(ang), np.sin(ang), 0]), color=hand, stroke_width=4),
          Dot(c, radius=0.05, color=hand))
    return g


def live_dial(c, t, rate=1.0, r=0.45, color=INK, hand=None):
    return always_redraw(lambda: dial(c, r, PI / 2 - rate * t.get_value(), color, hand))


def ruler(cx, cy, w=3.0, h=0.45, color=INK, n=10):
    g = VGroup(Rectangle(width=w, height=h, color=color, stroke_width=3, fill_color=PALE, fill_opacity=1).move_to(P(cx, cy)))
    for k in range(1, n):
        x = cx - w / 2 + k * w / n
        g.add(Line(P(x, cy + h / 2), P(x, cy + h / 2 - (0.2 if k % 5 == 0 else 0.12)), color=color, stroke_width=2))
    return g


def block(cx, cy, s=1.1, glow=0.0):
    """A lump of mass; glow > 0 shows the energy it holds."""
    sq = Square(s, stroke_color=INK, stroke_width=3, fill_color=TEAL if glow else PALE, fill_opacity=glow if glow else 1).move_to(P(cx, cy))
    return sq


def burst(c, r=0.28, color=ORANGE):
    return Star(7, outer_radius=r, inner_radius=r * 0.45, color=color, fill_opacity=1, stroke_width=0).move_to(P(*c))


def pend(pivot, L, ang, r=0.14, color=INK):
    p = P(*pivot)
    b = p + L * np.array([np.sin(ang), -np.cos(ang), 0])
    return VGroup(Line(p, b, color=color, stroke_width=3), Circle(radius=r, color=color, stroke_width=2.5, fill_color=WHITE, fill_opacity=1).move_to(b))


# ------------------------------------------------------------------ the light clock

LH, LW = 2.0, 1.3   # mirror gap and mirror width
RATE = 1.0          # one-way trips per second for a clock at rest (the pulse moves 2 units a second)
V = 1.2             # a moving clock's screen speed: 60% of the pulse's speed
VRATE = 0.8 * RATE  # its one-way trips per second, seen from the platform (gamma is 1.25 at 60%)


def mirrors(x, cy, h=LH, w=LW, color=INK):
    return VGroup(Line(P(x - w / 2, cy + h / 2), P(x + w / 2, cy + h / 2), color=color, stroke_width=7),
                  Line(P(x - w / 2, cy - h / 2), P(x + w / 2, cy - h / 2), color=color, stroke_width=7))


def pulse(x, y, r=0.11):
    return Dot(P(x, y), radius=r, color=ORANGE)


def pulse_y(cy, h, u):
    return cy - h / 2 + 0.12 + (h - 0.24) * bounce(u)


def rest_pulse(cx, cy, t, h=LH):
    return always_redraw(lambda: pulse(cx, pulse_y(cy, h, RATE * t.get_value())))


def zig_points(x0, cy, tau, h=LH):
    pts, k = [P(x0, pulse_y(cy, h, 0))], 1
    while k / VRATE < tau:
        tk = k / VRATE
        pts.append(P(x0 + V * tk, pulse_y(cy, h, VRATE * tk)))
        k += 1
    pts.append(P(x0 + V * tau, pulse_y(cy, h, VRATE * tau)))
    return pts


def moving_body(x0, cy, t, span, h=LH, extra=None):
    """The mirrors and the pulse of a light clock moving right, starting again after `span` units."""
    period = span / V

    def draw():
        tau = t.get_value() % period
        x = x0 + V * tau
        g = VGroup()
        if extra:
            g.add(extra(x))
        g.add(mirrors(x, cy, h), pulse(x, pulse_y(cy, h, VRATE * tau)))
        return g
    return always_redraw(draw)


def moving_trail(x0, cy, t, span, h=LH, color=ORANGE):
    period = span / V

    def draw():
        tau = t.get_value() % period
        if tau < 0.03:
            return hollow()
        return VMobject(color=color, stroke_width=3.5).set_points_as_corners(zig_points(x0, cy, tau, h))
    return always_redraw(draw)


def tick_dots(x, y, t, rate, n=6, color=ORANGE):
    """One dot per tick (a round trip), laid out left to right.

    All n dots always exist, with the ones not yet ticked fully transparent, so the
    group keeps the same parts while a FadeIn on it is running.
    """
    def draw():
        k = min(int(rate * t.get_value() / 2), n)
        g = VGroup(hollow())
        for i in range(n):
            g.add(Dot(P(x + 0.32 * i, y), radius=0.09, color=color).set_opacity(1 if i < k else 0))
        return g
    return always_redraw(draw)


# ================================================================== opening
deck.part("Chapter four")


@slide("Chapter four.", "Special Relativity")
def opening(s):
    t = clock(s)
    yield [FadeIn(mirrors(-4.6, 0.2)), FadeIn(rest_pulse(-4.6, 0.2, t)), FadeIn(at(lab("at rest", 26, INK), -4.6, -1.45))]
    yield [FadeIn(moving_trail(-1.9, 0.2, t, 8.2)), FadeIn(moving_body(-1.9, 0.2, t, 8.2)),
           FadeIn(at(lab("moving", 26, INK), 2.2, -1.45))]


# ================================================================== previously
deck.part("Previously")


@slide("The last chapter ended with a promise.", "Chapter 3's promise")
def prev1(s):
    a = at(card("chapter 3:\nthe quantum spring", 3.9, 1.5, INK, 28), -5.0, 0.4)
    b = at(card("quantum fields", 3.4, 1.5, INK, 30), 5.0, 0.4)
    link = DashedLine(a.get_right(), b.get_left(), color=LINE, stroke_width=3)
    yield [FadeIn(a), Create(link), FadeIn(b), FadeIn(at(lab("the promise: build these next", 24, MUTED), 5.0, -0.75))]
    gate = at(card("first, our equations\nmust agree with relativity", 4.5, 1.5, TEAL, 26), 0, 0.4)
    yield [FadeOut(link), FadeIn(gate, shift=DOWN * 0.2), GrowArrow(arrow(a, gate)), GrowArrow(arrow(gate, b))]


@slide("That matters because the particles", "Near the speed of light")
def prev2(s):
    t = clock(s)

    def streak():
        x = -5.6 + (5.0 * t.get_value()) % 11.5
        return VGroup(Line(P(max(x - 1.8, -5.6), 1.7), P(x, 1.7), color=LINE, stroke_width=7), Dot(P(x, 1.7), radius=0.16, color=INK))
    gauge = VGroup(hline(-5.6, 5.6, 0.35, LINE, 10),
                   Line(P(5.6, 0.05), P(5.6, 0.65), color=TEAL, stroke_width=5),
                   at(lab("light's speed", 22, TEAL), 5.6, 0.95))
    fill = Line(P(-5.6, 0.35), P(5.1, 0.35), color=INK, stroke_width=10)
    yield [FadeIn(always_redraw(streak)), FadeIn(at(lab("the particles of quantum field theory", 24, INK), -2.0, 2.4)),
           FadeIn(gauge), Create(fill), FadeIn(at(lab("often close to the speed of light", 24, INK), -0.6, -0.15))]
    names = ("time", "distance", "energy")
    chips = VGroup(*[at(chip(n, INK, size=28, h=0.75), x, -1.6) for n, x in zip(names, (-4.0, 0.0, 4.0))])
    yield [FadeIn(chips), LaggedStart(*[Create(xmark(c, 0.36, 0.15)) for c in chips], lag_ratio=0.25),
           FadeIn(at(lab("the everyday rules stop working", 26, RED, True), 0, -2.65))]


# ================================================================== the chapter at a glance
deck.part("Chapter four")

ROAD_Y = (1.8, 0.6, -0.6, -1.8)


def road_source():
    return at(card("one surprising\nfact about light", 3.8, 1.6, TEAL, 28), -4.9, 0.0)


def road_row(k):
    y = ROAD_Y[k]
    x = -0.4
    if k == 0:
        icon = dial((x, y), 0.36)
        text = "clocks that run slow"
    elif k == 1:
        icon = ruler(x, y, 1.0, 0.36, INK, 6)
        text = "lengths that shrink"
    elif k == 2:
        icon = block(x, y, 0.62, 0.55)
        text = "an energy hiding in every bit of mass"
    else:
        c = at(card("ψ", 0.72, 0.62, INK, 26), x, y)
        icon = VGroup(c, cross(c, RED, 4))
        text = "a test that the Schrödinger equation fails"
    return VGroup(icon, left_at(lab(text, 26, INK), x + 0.75, y))


def road_arrow(src, k):
    return Arrow(src.get_right(), P(-1.05, ROAD_Y[k]), buff=0.12, color=MUTED, stroke_width=3, tip_length=0.16)


@slide("This chapter starts from one surprising", "Where the chapter goes")
def road1(s):
    src = road_source()
    yield [FadeIn(src)]
    yield [*[GrowArrow(road_arrow(src, k)) for k in (0, 1)], *[FadeIn(road_row(k), shift=RIGHT * 0.15) for k in (0, 1)]]


@slide("We'll find an energy hiding", "Where the chapter goes")
def road2(s):
    src = road_source()
    s.add(src, *[road_arrow(src, k) for k in (0, 1)], *[road_row(k) for k in (0, 1)])
    yield [GrowArrow(road_arrow(src, 2)), FadeIn(road_row(2), shift=RIGHT * 0.15)]
    yield [GrowArrow(road_arrow(src, 3)), FadeIn(road_row(3), shift=RIGHT * 0.15)]


# ------------------------------------------------------------------ the contrast table

TAB_Y = (1.65, 0.7, -0.25, -1.2, -2.15)
TAB_X = (-5.05, -1.95, 4.2)       # right edge of the row names, centres of the two columns
TAB_W = (5.6, 6.0)
TAB_ROWS = (("speeds", "add up", "light's speed is the same for everyone"),
            ("time", "one clock for the whole universe", "moving clocks run slow"),
            ("lengths", "a ruler is just a ruler", "moving rulers shrink"),
            ("at the same time", "everyone agrees", "depends on who's watching"),
            ("energy", "kinetic energy, ½mv²", "even mass sitting still holds energy"))


def tab_heads():
    return VGroup(at(T("everyday speeds", 28, MUTED, True), TAB_X[1], 2.45),
                  at(T("near the speed of light", 28, INK, True), TAB_X[2], 2.45))


def tab_name(k):
    return right_at(lab(TAB_ROWS[k][0], 24, MUTED), TAB_X[0], TAB_Y[k])


def tab_cell(k, col):
    color = (MUTED, INK)[col] if not (k == 0 and col == 1) else TEAL
    box = at(card(None, TAB_W[col], 0.78, LINE), TAB_X[1 + col], TAB_Y[k])
    return VGroup(box, at(lab(TAB_ROWS[k][1 + col], 24, color), TAB_X[1 + col], TAB_Y[k]))


def tab_strike(k):
    c = tab_cell(k, 0)[1]
    return Line(c.get_left() + LEFT * 0.1, c.get_right() + RIGHT * 0.1, color=RED, stroke_width=4)


@slide("Here's the contrast.", "Everyday speeds")
def tab1(s):
    yield [FadeIn(tab_heads())]
    yield [*[FadeIn(VGroup(tab_name(k), tab_cell(k, 0)), shift=RIGHT * 0.15) for k in (0, 1)]]
    yield [*[FadeIn(VGroup(tab_name(k), tab_cell(k, 0)), shift=RIGHT * 0.15) for k in (2, 3)]]


@slide("Near the speed of light, every one", "Near the speed of light")
def tab2(s):
    s.add(tab_heads(), *[VGroup(tab_name(k), tab_cell(k, 0)) for k in range(4)])
    yield [LaggedStart(*[Create(tab_strike(k)) for k in range(4)], lag_ratio=0.2)]
    yield [FadeIn(tab_cell(0, 1), shift=LEFT * 0.15)]


@slide("Moving clocks run slow, and moving rulers", "Near the speed of light")
def tab3(s):
    s.add(tab_heads(), *[VGroup(tab_name(k), tab_cell(k, 0), tab_strike(k)) for k in range(4)], tab_cell(0, 1))
    yield [*[FadeIn(tab_cell(k, 1), shift=LEFT * 0.15) for k in (1, 2)]]
    yield [FadeIn(tab_cell(3, 1), shift=LEFT * 0.15)]
    yield [FadeIn(VGroup(tab_name(4), tab_cell(4, 0)), shift=RIGHT * 0.15), FadeIn(tab_cell(4, 1), shift=LEFT * 0.15),
           Create(tab_strike(4))]


# ================================================================== light's speed is the same for everyone
deck.part("Light's speed is the same for everyone")

TRY = 0.0      # the carriage's centre height
PLAT = -1.75   # the platform's surface


def walking_train(t, seen):
    """The carriage rolling right without ever jumping back, and a walker whose opacity is `seen`.

    One redrawn group carries both, so revealing the walker never stacks a second carriage on the first.
    """
    def draw():
        run = min(t.get_value(), 12.0)
        x = -4.4 + 0.45 * run
        wx = x - 2.3 + 0.2 * run
        o = seen.get_value()
        return VGroup(carriage(x, TRY, 6.0, 1.9),
                      person(wx, TRY - 0.85, PURPLE, 1.45).set_stroke(opacity=o),
                      Arrow(P(wx + 0.3, TRY + 0.3), P(wx + 0.9, TRY + 0.3), buff=0, color=PURPLE, stroke_width=4,
                            tip_length=0.14).set_opacity(o))
    return always_redraw(draw)


def train_ground():
    return VGroup(hline(-7.4, 7.4, TRY - 1.23, MUTED, 3), hline(-7.4, 7.4, PLAT, LINE, 6))


@slide("Light's speed is the same for everyone.", "Walking on a train")
def walk1(s):
    t = clock(s)
    seen = ValueTracker(0.0)
    s.add(train_ground(), seen, walking_train(t, seen))
    yield [
           GrowArrow(Arrow(P(-4.2, 1.75), P(-1.6, 1.75), buff=0, color=BLUE, stroke_width=5, tip_length=0.2)),
           FadeIn(left_at(lab("the train: 30 m/s", 26, BLUE, True), -1.3, 1.75))]
    yield [seen.animate.set_value(1.0), FadeIn(left_at(lab("you walk forward: 1 m/s", 26, PURPLE, True), -1.3, 2.4))]
    yield [FadeIn(person(5.9, PLAT, BLUE, 1.25)),
           FadeIn(at(words("someone on the platform sees you go by at 31 m/s", 30, 24, BLUE, align=ORIGIN), 3.2, -2.6))]


@slide("Speeds add.", "Speeds add")
def walk2(s):
    y = 0.9
    x0 = -5.4
    big = Arrow(P(x0, y), P(x0 + 6.0, y), buff=0, color=BLUE, stroke_width=7, tip_length=0.22)
    small = Arrow(P(x0 + 6.0, y), P(x0 + 6.6, y), buff=0, color=PURPLE, stroke_width=7, tip_length=0.18, max_tip_length_to_length_ratio=0.5)
    total = Arrow(P(x0, y - 1.0), P(x0 + 6.6, y - 1.0), buff=0, color=BLUE, stroke_width=7, tip_length=0.22)
    yield [GrowArrow(big), FadeIn(at(lab("train: 30", 24, BLUE), x0 + 3.0, y + 0.4)),
           GrowArrow(small), FadeIn(at(lab("you: 1", 24, PURPLE), x0 + 6.4, y + 0.4))]
    sum_ = at(VGroup(T("30 m/s", 34, BLUE, True), T("+", 34, INK), T("1 m/s", 34, PURPLE, True), T("=", 34, INK),
                     T("31 m/s", 34, BLUE, True)).arrange(RIGHT, buff=0.3), 4.3, 2.3)
    yield [GrowArrow(total), FadeIn(at(lab("seen from the platform: 31", 24, BLUE), x0 + 3.3, y - 1.45)), FadeIn(sum_)]
    yield [FadeIn(at(lab("so obvious that nobody questioned it for centuries", 26, MUTED), 0, -2.4))]


def light_wave(t, x0, x1, y, amp=0.35, k=2.4, speed=3.0, color=ORANGE):
    xs = np.linspace(x0, x1, 120)
    return always_redraw(lambda: VMobject(color=color, stroke_width=4).set_points_smoothly(
        [P(x, y + amp * np.sin(k * x - speed * t.get_value())) for x in xs]))


def maxwell_card():
    return at(card("Maxwell's equations\nelectricity and magnetism", 4.2, 1.5, INK, 26), -4.9, 1.0)


@slide("Light breaks it.", "Maxwell's waves")
def max1(s):
    t = clock(s)
    m = maxwell_card()
    yield [FadeIn(m), FadeIn(at(lab("the 1860s: James Clerk Maxwell", 24, MUTED), -4.9, 2.2))]
    yield [GrowArrow(Arrow(P(-2.7, 1.0), P(-1.9, 1.0), buff=0, color=MUTED, stroke_width=4, tip_length=0.18)),
           FadeIn(light_wave(t, -1.7, 6.9, 1.0)), FadeIn(at(lab("they predict waves", 24, INK), 2.6, 2.2))]
    yield [FadeIn(at(T("about 300,000 km/s", 34, TEAL, True), 2.6, -0.3))]


@slide("That's exactly the measured speed of light.", "A speed with no reference")
def max2(s):
    t = clock(s)
    s.add(maxwell_card(), at(lab("the 1860s: James Clerk Maxwell", 24, MUTED), -4.9, 2.2),
          Arrow(P(-2.7, 1.0), P(-1.9, 1.0), buff=0, color=MUTED, stroke_width=4, tip_length=0.18),
          light_wave(t, -1.7, 6.9, 1.0), at(lab("they predict waves", 24, INK), 2.6, 2.2), at(T("about 300,000 km/s", 34, TEAL, True), 2.6, -0.3))
    meas = at(VGroup(lab("= the measured speed of light", 26, INK), check()).arrange(RIGHT, buff=0.2), 2.6, -1.1)
    yield [FadeIn(meas)]
    people = VGroup(*[person(x, -2.95, MUTED, 0.95) for x in (-5.8, -4.3, -2.8)])
    qs = VGroup(*[at(T("?", 32, INK, True), x + 0.25, -1.7) for x in (-5.8, -4.3, -2.8)])
    yield [FadeIn(people), FadeIn(qs), FadeIn(left_at(lab("but relative to what?", 28, INK, True), -1.6, -2.5))]


def air_row(t, y, color, opacity=1.0, n=26, amp=0.13):
    base = np.linspace(-2.0, 6.9, n)

    def draw():
        g = VGroup()
        for row in (-0.32, 0.0, 0.32):
            for x in base:
                g.add(Dot(P(x + amp * np.sin(1.6 * x - 3.2 * t.get_value()), y + row), radius=0.05, color=color).set_opacity(opacity))
        return g
    return always_redraw(draw)


@slide("The natural guess was an invisible medium", "A medium for light")
def medium(s):
    t = clock(s)
    yield [FadeIn(air_row(t, 1.3, MUTED)), FadeIn(left_at(words("air carries sound", 14, 26, INK), -7.2, 1.3))]
    yield [FadeIn(air_row(t, -1.0, LINE, 0.8)), FadeIn(light_wave(t, -2.0, 6.9, -1.0, 0.3, 2.0, 3.2)),
           FadeIn(left_at(words("an invisible medium carries light", 16, 26, INK), -7.2, -1.0))]
    yield [FadeIn(at(lab("light's speed fixed relative to the medium", 26, INK, True), 2.4, -2.5))]


SUN = (-4.4, -0.4)


@slide("The Earth races around the Sun", "A wind of the medium")
def wind(s):
    t = clock(s)
    R = 2.2
    sun = VGroup(Circle(radius=0.55, color=MUTED, stroke_width=3, fill_color=LINE, fill_opacity=1).move_to(P(*SUN)),
                 at(lab("Sun", 22, INK), SUN[0], SUN[1]))
    orbit = DashedVMobject(Circle(radius=R, color=LINE, stroke_width=3).move_to(P(*SUN)), num_dashes=40)

    def earth():
        a = 0.5 * t.get_value() + 0.8
        c = P(SUN[0] + R * np.cos(a), SUN[1] + R * np.sin(a))
        u = np.array([-np.sin(a), np.cos(a), 0])
        return VGroup(Circle(radius=0.2, color=INK, stroke_width=3, fill_color=PALE, fill_opacity=1).move_to(c),
                      Arrow(c + 0.25 * u, c + 1.0 * u, buff=0, color=INK, stroke_width=4, tip_length=0.15))
    yield [FadeIn(sun), Create(orbit), FadeIn(always_redraw(earth)), FadeIn(at(lab("the Earth: 30 km/s", 26, INK, True), SUN[0], 2.3))]
    winds = VGroup(*[Arrow(P(4.2, y), P(0.8, y), buff=0, color=MUTED, stroke_width=3, tip_length=0.16) for y in (2.15, 1.55)])
    yield [LaggedStart(*[GrowArrow(w) for w in winds], lag_ratio=0.2), FadeIn(left_at(lab("a wind of the medium", 24, MUTED), 4.4, 1.85))]
    fast = Arrow(P(1.0, 0.3), P(6.2, 0.3), buff=0, color=ORANGE, stroke_width=6, tip_length=0.2)
    slow = Arrow(P(6.2, -1.3), P(1.6, -1.3), buff=0, color=ORANGE, stroke_width=6, tip_length=0.2)
    yield [GrowArrow(fast), GrowArrow(slow), FadeIn(at(lab("against the wind: a little slower", 24, INK), 3.6, -0.2)),
           FadeIn(at(lab("with the wind: a little faster", 24, INK), 3.9, -1.8))]


# ------------------------------------------------------------------ Michelson and Morley

MMC = (-3.7, -0.1)
FR = (4.6, -0.9)      # the bands' centre
FW, FH, FP = 4.0, 1.1, 0.8   # their width, height and the spacing of bright bands


def mm_draw(ang=0.0, t=None, stage=3, c=MMC):
    """The apparatus turned by `ang` about the beam splitter; stage 1 lamp only, 2 both arms, 3 recombined."""
    cx, cy = c
    ca, sa = np.cos(ang), np.sin(ang)

    def p(x, y):
        return P(cx + ca * x - sa * y, cy + sa * x + ca * y)
    g = VGroup(Polygon(p(-3.3, -1.75), p(2.55, -1.75), p(2.55, 2.55), p(-3.3, 2.55), stroke_color=LINE, stroke_width=3))
    d = 0.09
    segs = [((-2.65, 0), (0, 0))]
    if stage >= 2:
        segs += [((0, d), (2.22, d)), ((2.22, -d), (0, -d)), ((-d, 0), (-d, 2.22)), ((d, 2.22), (d, 0))]
    if stage >= 3:
        segs += [((0, 0), (0, -1.38))]
    for a, b in segs:
        g.add(Line(p(*a), p(*b), color=ORANGE, stroke_width=3, stroke_opacity=0.45))
    if t is not None:
        for a, b in segs:
            L = np.hypot(b[0] - a[0], b[1] - a[1])
            n = max(2, int(L / 0.75))
            for k in range(n):
                f = (k / n + 1.2 * t / L) % 1
                g.add(Dot(p(a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f), radius=0.07, color=ORANGE))
    g.add(Polygon(p(-3.25, -0.22), p(-2.65, -0.22), p(-2.65, 0.22), p(-3.25, 0.22), stroke_color=INK, fill_color=INK, fill_opacity=1),
          Line(p(-0.32, -0.32), p(0.32, 0.32), color=INK, stroke_width=6),
          Line(p(2.3, -0.5), p(2.3, 0.5), color=INK, stroke_width=8),
          Line(p(-0.5, 2.3), p(0.5, 2.3), color=INK, stroke_width=8))
    if stage >= 3:
        g.add(Line(p(-0.45, -1.47), p(0.45, -1.47), color=MUTED, stroke_width=10))
    return g


def mm_labels():
    cx, cy = MMC
    return VGroup(at(lab("lamp", 22), cx - 2.95, cy - 0.6),
                  at(lab("splits the beam", 22, INK), cx - 1.4, cy + 0.55),
                  at(lab("mirror", 22), cx + 2.3, cy - 0.85),
                  at(lab("mirror", 22), cx + 1.25, cy + 2.3),
                  at(lab("arm 1", 22), cx + 1.2, cy - 0.4),
                  at(lab("arm 2", 22), cx + 0.6, cy + 1.3))


def fringes(shift=0.0, c=FR, n=72):
    g = VGroup(Rectangle(width=FW, height=FH, stroke_width=0, fill_color=INK, fill_opacity=0.9).move_to(P(*c)))
    sw = FW / n
    for i in range(n):
        x = -FW / 2 + (i + 0.5) * sw
        b = np.cos(PI * (x / FP - shift)) ** 2
        g.add(Rectangle(width=sw * 1.04, height=FH, stroke_width=0, fill_color=ORANGE, fill_opacity=0.95 * b).move_to(P(c[0] + x, c[1])))
    g.add(Rectangle(width=FW, height=FH, color=INK, stroke_width=2).move_to(P(*c)),
          Triangle(color=INK, fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.11).rotate(PI).move_to(P(c[0], c[1] + FH / 2 + 0.14)))
    return g


def expected_ghost(shift=0.4, c=FR):
    g = VGroup()
    for m in range(-3, 3):
        x = FP * (m + shift)
        if abs(x) < FW / 2 - 0.1:
            g.add(DashedVMobject(Rectangle(width=0.3, height=FH + 0.3, color=RED, stroke_width=3), num_dashes=14).move_to(P(c[0] + x, c[1])))
    g.add(Triangle(color=RED, fill_color=RED, fill_opacity=1, stroke_width=0).scale(0.11).rotate(PI).move_to(P(c[0] + FP * shift, c[1] + FH / 2 + 0.14)))
    return g


def wind_arrows():
    return VGroup(*[Arrow(P(1.5, y), P(-0.6, y), buff=0, color=MUTED, stroke_width=3, tip_length=0.16) for y in (1.9, 1.2, 0.5)],
                  at(lab("expected wind", 22, MUTED), 0.45, 2.45))


@slide("In eighteen eighty-seven, Albert Michelson", "Michelson and Morley, 1887")
def mm1(s):
    t = clock(s)
    st = {"n": 1}
    app = always_redraw(lambda: mm_draw(0.0, t.get_value(), st["n"]))
    labels = mm_labels()
    yield [FadeIn(app), FadeIn(labels[0]), FadeIn(labels[1])]
    st["n"] = 2
    yield [FadeIn(labels[2:]), FadeIn(left_at(words("the halves go along arms at right angles", 22, 24, INK), 0.6, 1.6))]
    st["n"] = 3
    link = DashedLine(P(MMC[0] + 0.5, MMC[1] - 1.47), P(FR[0] - FW / 2 - 0.1, FR[1]), color=LINE, stroke_width=3)
    yield [Create(link), FadeIn(fringes()), FadeIn(at(lab("bands of light and dark", 24, INK), FR[0], FR[1] + 0.95))]


@slide("If one arm faced into the wind", "Turning the apparatus")
def mm2(s):
    t = clock(s)
    ang = ValueTracker(0.0)
    s.add(ang, always_redraw(lambda: mm_draw(ang.get_value(), t.get_value(), 3)), fringes(),
          at(lab("bands of light and dark", 24, INK), FR[0], FR[1] + 0.95))
    yield [FadeIn(wind_arrows()), FadeIn(left_at(words("into the wind, one half takes a different time to come back", 24, 24, INK), 2.2, 1.7))]
    yield [ang.animate.set_value(PI / 2), FadeIn(expected_ghost()),
           FadeIn(at(lab("expected: the bands slide", 24, RED, True), FR[0], FR[1] - 0.95))]


@slide("They barely moved.", "The bands stayed put")
def mm3(s):
    t = clock(s)
    ang = ValueTracker(PI / 2)
    sh = ValueTracker(0.0)
    s.add(ang, sh, always_redraw(lambda: mm_draw(ang.get_value(), t.get_value(), 3)),
          at(lab("bands of light and dark", 24, INK), FR[0], FR[1] + 0.95), expected_ghost(),
          at(lab("expected: the bands slide", 24, RED, True), FR[0], FR[1] - 0.95))
    s.add(always_redraw(lambda: fringes(sh.get_value())))
    yield [Succession(ang.animate.set_value(0.0), ang.animate.set_value(PI / 2)), sh.animate.set_value(0.02),
           FadeIn(at(lab("they barely moved", 28, INK, True), FR[0], 1.9))]
    y1, y2 = -2.4, -3.0
    exp = Rectangle(width=FP * 0.4 * 6, height=0.36, stroke_width=0, fill_color=RED, fill_opacity=0.7)
    left_at(exp, 2.6, y1)
    got = Rectangle(width=0.08, height=0.36, stroke_width=0, fill_color=INK, fill_opacity=0.9)
    left_at(got, 2.6, y2)
    yield [GrowFromEdge(exp, LEFT), FadeIn(right_at(lab("expected slide", 22, RED), 2.4, y1)),
           GrowFromEdge(got, LEFT), FadeIn(right_at(lab("measured", 22, INK), 2.4, y2)),
           FadeIn(left_at(lab("less than a twentieth of it", 22, INK), 2.9, y2))]


@slide("Experiments since then, far more precise", "The same speed for everyone")
def same_c(s):
    t = clock(s)
    lanes = (1.6, 0.1, -1.4)
    speeds = (0.0, 0.3, 0.55)
    tracks = VGroup(*[hline(-6.9, 3.0, y - 0.35, LINE, 3) for y in lanes])

    def riders():
        g = VGroup()
        for y, v in zip(lanes, speeds):
            x = -4.6 if v == 0 else -6.2 + min(v * t.get_value(), 5.6)
            if v == 0:
                g.add(person(x, y - 0.35, INK, 0.75))
            else:
                g.add(carriage(x, y + 0.05, 1.4, 0.55))
                g.add(person(x, y - 0.3, INK, 0.6))
        return g

    def front():
        x = -6.6 + min(2.6 * t.get_value(), 9.6)
        return Line(P(x, lanes[0] + 0.6), P(x, lanes[-1] - 0.5), color=ORANGE, stroke_width=6)
    yield [FadeIn(tracks), FadeIn(always_redraw(riders)), FadeIn(always_redraw(front)),
           FadeIn(at(lab("one flash of light, three observers moving differently", 24, INK), -1.9, 2.45))]
    reads = VGroup(*[left_at(VGroup(lab("measures", 22, INK), T("300,000 km/s", 24, TEAL, True), check(size=0.3)).arrange(RIGHT, buff=0.15), 3.4, y)
                     for y in lanes])
    yield [LaggedStart(*[FadeIn(r, shift=LEFT * 0.15) for r in reads], lag_ratio=0.3),
           FadeIn(at(pill("every observer measures the same speed of light", TEAL, 28), 0, -2.7), shift=UP * 0.15)]


@slide("In nineteen oh five, Albert Einstein", "Einstein's two rules, 1905")
def rules(s):
    a = at(card("light's speed is the same for everyone", 11.0, 1.2, TEAL, 30), 0, 1.3)
    yield [FadeIn(at(lab("1905: Albert Einstein takes it seriously", 26, MUTED), 0, 2.3)), FadeIn(a, shift=RIGHT * 0.2)]
    b = at(card("the laws of physics are the same for every\nobserver moving at a steady speed", 11.0, 1.6, TEAL, 30), 0, -1.05)
    yield [FadeIn(at(lab("one more rule", 26, INK, True), 0, 0.2)), FadeIn(b, shift=RIGHT * 0.2)]


@slide("No experiment inside a smoothly moving train", "No way to tell you're moving")
def rules2(s):
    t = clock(s)
    rows = ((1.2, "at rest", 0.0), (-1.3, "moving smoothly", 1.6))
    g = VGroup()
    for y, name, v in rows:
        if v:
            g.add(poles(t, y - 0.95, y + 0.75, v, gap=1.6, x0=-7.4, x1=-0.4),
                  hline(-7.3, -0.5, y - 1.08, MUTED, 3), sleepers(t, y - 1.08, v, -7.3, -0.5))
        g.add(carriage(-3.9, y, 4.4, 1.6), always_redraw(lambda y=y: pend((-3.9, y + 0.72), 1.05, 0.45 * np.cos(2.4 * t.get_value()))),
              left_at(lab(name, 22, INK), -7.3, y + 1.05))
    yield [FadeIn(g)]
    yield [FadeIn(left_at(VGroup(lab("the same swing in both", 26, INK), check()).arrange(RIGHT, buff=0.2), 0.3, 1.2)),
           FadeIn(left_at(words("no experiment inside can tell whether the train is moving", 26, 24, INK), 0.3, 0.2))]
    yield [FadeIn(left_at(pill("two rules: the whole of special relativity", TEAL, 24), 0.3, -1.3)),
           FadeIn(left_at(lab("everything else follows from them", 24, INK), 0.3, -2.0))]


@slide("Light's speed can't give", "Time and space give way")
def give(s):
    t = clock(s)
    c = at(card("light's speed:\nfixed for everyone", 4.2, 1.6, TEAL, 28), -4.6, 0.3)
    yield [FadeIn(c), FadeIn(at(lab("it can't give", 26, TEAL, True), -4.6, -1.05))]
    sq = always_redraw(lambda: ruler(3.6, -1.0, 3.6 * (0.82 + 0.18 * np.cos(1.8 * t.get_value())), 0.5))
    d = always_redraw(lambda: dial((3.6, 1.15), 0.75, PI / 2 - (1.0 + 0.6 * np.sin(1.3 * t.get_value())) * t.get_value()))
    yield [GrowArrow(Arrow(P(-2.3, 0.3), P(0.9, 0.3), buff=0, color=MUTED, stroke_width=4, tip_length=0.2)),
           FadeIn(sq), FadeIn(d), FadeIn(at(lab("time", 26, INK, True), 5.1, 1.15)), FadeIn(at(lab("space", 26, INK, True), 3.6, -1.75)),
           FadeIn(at(lab("something else has to give", 26, INK), 0.0, -2.7))]


# ================================================================== moving clocks run slow
deck.part("Moving clocks run slow")


@slide("Moving clocks run slow.", "A light clock")
def lc1(s):
    t = clock(s)
    cx, cy, h = -2.4, 0.0, 2.6
    yield [FadeIn(mirrors(cx, cy, h, 1.6)), FadeIn(left_at(lab("mirror", 24), cx + 1.0, cy + h / 2)),
           FadeIn(left_at(lab("mirror", 24), cx + 1.0, cy - h / 2))]
    yield [FadeIn(rest_pulse(cx, cy, t, h)), FadeIn(right_at(lab("a pulse of light", 26, ORANGE, True), cx - 1.1, cy))]
    yield [FadeIn(tick_dots(cx - 0.8, -2.3, t, RATE)), FadeIn(left_at(lab("each round trip is one tick", 26, INK), 1.6, -2.3))]


def rider_carriage(cx, cy):
    return carriage(cx, cy, 3.6, 2.9)


@slide("Now put that clock on a fast train.", "The clock on a train")
def lc2(s):
    t = clock(s)
    cx, cy = -3.2, 0.2
    yield [FadeIn(poles(t, -1.9, 2.0, 2.4, x1=-0.6)), FadeIn(hline(-7.4, 7.4, cy - 1.8, MUTED, 3)), FadeIn(rider_carriage(cx, cy)),
           FadeIn(mirrors(cx, cy)), FadeIn(rest_pulse(cx, cy, t)), FadeIn(at(lab("on a fast train", 26, INK, True), cx, 2.4))]
    yield [FadeIn(DashedLine(P(cx + 0.3, cy - 0.88), P(cx + 0.3, cy + 0.88), color=ORANGE, stroke_width=3)),
           FadeIn(left_at(words("to you, riding along: straight up and down", 20, 28, PURPLE), 0.4, 0.4)),
           FadeIn(person(cx + 1.15, cy - 1.4, PURPLE, 1.1))]


def lc_extra(cy):
    return lambda x: rider_carriage(x, cy)


@slide("But someone on the platform sees", "Seen from the platform")
def lc3(s):
    t = clock(s)
    x0, cy, span = -5.6, 0.25, 9.8
    yield [FadeIn(hline(-7.4, 7.4, cy - 1.8, MUTED, 3)), FadeIn(moving_body(x0, cy, t, span, extra=lc_extra(cy))),
           FadeIn(left_at(lab("from the platform: the mirrors move sideways", 26, BLUE, True), -7.2, 2.4))]
    yield hold()
    yield hold()
    yield [FadeIn(moving_trail(x0, cy, t, span)), FadeIn(at(lab("the light follows a slanted zigzag", 26, ORANGE, True), 0, -2.15))]
    yield hold()
    yield [FadeIn(at(lab("a longer path", 28, INK, True), 0, -2.8))]


CMP = (-5.0, 0.7)    # the clock at rest, for comparing
MOV0 = -2.6           # where the moving clock starts
MSPAN = 8.6


def compare_base(s, t):
    s.add(mirrors(*CMP), rest_pulse(CMP[0], CMP[1], t), at(lab("at rest", 26, INK, True), CMP[0], 2.3),
          moving_trail(MOV0, CMP[1], t, MSPAN), moving_body(MOV0, CMP[1], t, MSPAN),
          left_at(lab("moving", 26, INK, True), MOV0 - 0.4, 2.3))


@slide("And light's speed is the same for both", "Same speed, longer path")
def lc4(s):
    t = clock(s)
    compare_base(s, t)
    yield [FadeIn(at(lab("light's speed: the same for both", 26, TEAL, True), 0.5, -0.9))]
    y1, y2 = -1.75, -2.45
    a = Line(P(-4.0, y1), P(-4.0 + 1.76 * 1.4, y1), color=ORANGE, stroke_width=8)
    b = Line(P(-4.0, y2), P(-4.0 + 1.76 * 1.4 / 0.8, y2), color=ORANGE, stroke_width=8)
    yield [Create(a), Create(b), FadeIn(right_at(lab("straight trip", 22, INK), -4.2, y1)),
           FadeIn(right_at(lab("slanted trip", 22, INK), -4.2, y2)),
           FadeIn(left_at(words("a longer path at the same speed takes longer", 24, 24, INK), 0.6, -2.1))]


@slide("So from the platform, each tick takes longer.", "The moving clock runs slow")
def lc5(s):
    t = clock(s)
    compare_base(s, t)
    yield [FadeIn(tick_dots(-5.8, -1.2, t, RATE)), FadeIn(tick_dots(-1.6, -1.2, t, VRATE)),
           FadeIn(right_at(lab("ticks", 22, ORANGE), -6.1, -1.2)),
           FadeIn(at(lab("from the platform, each tick takes longer", 26, BLUE, True), 0, -2.05))]
    yield [FadeIn(at(pill("the moving clock runs slow", BLUE, 28), 0, -2.85), shift=UP * 0.15)]


def train_clocks(t, x0, cy, span):
    """A carriage carrying a light clock and two dial clocks, all ticking at the moving rate."""
    period = span / V

    def draw():
        tau = t.get_value() % period
        x = x0 + V * tau
        ang = PI / 2 - 0.8 * t.get_value()
        return VGroup(carriage(x, cy, 4.2, 2.6), mirrors(x - 1.2, cy, 1.8, 1.0),
                      pulse(x - 1.2, pulse_y(cy, 1.8, VRATE * t.get_value())),
                      dial((x + 0.3, cy + 0.4), 0.42, ang), dial((x + 1.4, cy - 0.5), 0.42, ang))
    return always_redraw(draw)


@slide("And it's not just this clock.", "Every clock on the train")
def lc6(s):
    t = clock(s)
    cy = 0.9
    yield [FadeIn(hline(-7.4, 7.4, cy - 1.6, MUTED, 3)), FadeIn(train_clocks(t, -5.0, cy, 7.4)),
           FadeIn(at(lab("every clock on the train", 26, INK, True), -2.6, 2.45))]
    yield [FadeIn(live_dial((-6.3, -1.95), t, 1.0, 0.5, BLUE)), FadeIn(at(lab("a clock on the platform", 22, BLUE), -6.3, -2.75)),
           FadeIn(left_at(words("from the platform, all of the train's clocks run slow by the same amount", 38, 26, BLUE), -4.2, -2.05))]


@slide("Otherwise you could compare them", "Time itself runs slow")
def lc7(s):
    t = clock(s)
    pair = VGroup(live_dial((-5.2, 0.9), t, 0.8, 0.7), live_dial((-3.2, 0.9), t, 1.3, 0.7))
    box = at(card(None, 5.0, 2.4, LINE), -4.2, 0.9)
    yield [FadeIn(box), FadeIn(pair), FadeIn(at(lab("two train clocks disagreeing", 24, INK), -4.2, 2.45))]
    yield [Create(cross(box, RED, 5)), FadeIn(left_at(words("you could tell that you were moving, which Einstein's added rule forbids", 26, 24, RED), 0.0, 1.3))]
    yield [FadeIn(at(pill("time itself runs slow on the train, seen from the platform", BLUE, 26), 0, -1.9), shift=UP * 0.15)]


# ------------------------------------------------------------------ gamma

GAMMA = "γ = 1 / √(1 − v²/c²)"


def g_card(text, cap, x, y, w=3.4, color=INK, below=False):
    c = at(card(text, w, 0.95, color, 30), x, y)
    return VGroup(c, at(lab(cap, 22, MUTED), x, y + (-0.78 if below else 0.78)))


def g_cards():
    return [g_card("v/c", "speed as a fraction of light's", -4.9, 0.7),
            g_card("v²/c²", "square it", -0.6, 0.7),
            g_card("1 − v²/c²", "subtract from one", 3.9, 0.7),
            g_card("√(1 − v²/c²)", "take the square root", -3.0, -1.55, 3.9, below=True),
            g_card(GAMMA, "gamma: one divided by the result", 3.2, -1.55, 5.6, below=True)]


def g_links(cards):
    return [arrow(cards[0][0], cards[1][0]), arrow(cards[1][0], cards[2][0]),
            elbow(cards[2][0].get_bottom() + DOWN * 0.08, -0.45, cards[3][0].get_top() + UP * 0.08),
            arrow(cards[3][0], cards[4][0])]


@slide("We call the slowdown factor gamma.", "The slowdown factor gamma")
def gam1(s):
    cards = g_cards()
    links = g_links(cards)
    yield [FadeIn(at(T("slowdown factor:  γ  (gamma)", 32, INK, True), 0, 2.3))]
    yield [FadeIn(cards[0])]
    yield [GrowArrow(links[0]), FadeIn(cards[1])]


@slide("Subtract that from one", "The slowdown factor gamma")
def gam2(s):
    cards = g_cards()
    links = g_links(cards)
    s.add(at(T("slowdown factor:  γ  (gamma)", 32, INK, True), 0, 2.3), cards[0], cards[1], links[0])
    yield [GrowArrow(links[1]), FadeIn(cards[2])]
    yield [Create(links[2]), FadeIn(cards[3])]
    yield [GrowArrow(links[3]), FadeIn(cards[4]), Create(SurroundingRectangle(cards[4][0], color=INK, buff=0.12, corner_radius=0.18))]


GO = (-6.4, -2.9)    # origin of the gamma plot
GX, GYS = 7.0, 0.5   # screen units per unit of v/c and per unit of gamma


def gx(v):
    return GO[0] + GX * v


def gy(g):
    return GO[1] + GYS * g


def gamma_of(v):
    return 1 / np.sqrt(1 - v * v)


def gamma_axes(ylabel="γ", xlabel="speed, as a fraction of light's", one=True):
    ax = VGroup(axis_arrow(GO, (gx(1.12), GO[1])), axis_arrow(GO, (GO[0], 2.55)),
                left_at(lab(ylabel, 26, INK, True), GO[0] + 0.2, 2.45), at(lab(xlabel, 22), gx(0.5), GO[1] - 0.35),
                at(lab("0", 22), GO[0], GO[1] - 0.35), at(lab("1", 22), gx(1.0), GO[1] - 0.35))
    base = VGroup(DashedLine(P(GO[0], gy(1)), P(gx(1.0), gy(1)), color=LINE, stroke_width=2))
    if one:
        base.add(right_at(lab("1", 22), GO[0] - 0.12, gy(1)))
    wall = VGroup(DashedLine(P(gx(1.0), GO[1]), P(gx(1.0), 2.4), color=TEAL, stroke_width=3))
    return VGroup(ax, base, wall)


def gamma_curve(vmax=0.9949, color=INK, sc=1.0):
    vs = np.concatenate([np.linspace(0, 0.9, 60), np.linspace(0.9, vmax, 60)])
    return VMobject(color=color, stroke_width=5).set_points_as_corners([P(gx(v), gy(sc * gamma_of(v))) for v in vs])


def g_point(v, g, color=INK):
    return Dot(P(gx(v), gy(g)), radius=0.1, color=color)


@slide("As the speed gets close to light's", "Gamma grows without limit")
def gam3(s):
    v = ValueTracker(0.0)
    s.add(v)
    yield [FadeIn(gamma_axes()), Create(gamma_curve()), FadeIn(at(lab("light's speed", 22, TEAL), gx(1.0) + 1.0, 2.2)),
           FadeIn(always_redraw(lambda: g_point(v.get_value(), gamma_of(v.get_value())))), v.animate.set_value(0.985)]
    yield [GrowArrow(Arrow(P(2.2, -0.4), P(2.2, 2.0), buff=0, color=INK, stroke_width=5, tip_length=0.22)),
           FadeIn(left_at(words("near light's speed the root shrinks toward zero, so gamma grows without limit", 20, 26, INK), 2.6, 0.8))]


def gam_base(s):
    s.add(gamma_axes(), gamma_curve(), at(lab("light's speed", 22, TEAL), gx(1.0) + 1.0, 2.2))


@slide("At everyday speeds, gamma is so close", "Everyday speeds")
def gam4(s):
    gam_base(s)
    zone = Rectangle(width=GX * 0.3, height=0.5, color=INK, stroke_width=3).move_to(P(gx(0.15), gy(1)))
    yield [Create(zone), FadeIn(left_at(words("everyday speeds: gamma is so close to 1 that nobody notices", 26, 26, INK), 2.0, 1.4))]
    yield [FadeIn(left_at(VGroup(lab("a jet plane, 250 m/s:", 24, INK), code("γ = 1.0000000000003", 26, INK)).arrange(DOWN, buff=0.15, aligned_edge=LEFT), 2.0, -0.2)),
           FadeIn(left_at(words("it differs from 1 only in the 13th decimal place", 30, 22, MUTED), 2.0, -1.2))]


GAM_PTS = ((0.6, 1.25, "60% of light speed", "1.25"), (0.87, 2.0, "87%", "2"), (0.99, 7.1, "99%", "7.1"))


def gam_row(k):
    v, g, name, val = GAM_PTS[k]
    y = 1.4 - 0.8 * k
    return VGroup(left_at(lab(name, 26, INK), 2.0, y), left_at(code(f"γ = {val}", 28, INK), 5.5, y))


def gam_mark(k):
    v, g, name, val = GAM_PTS[k]
    d = g_point(v, g)
    return VGroup(d, lab(val, 22, INK).next_to(d, UP, buff=0.12).shift(LEFT * 0.35))


@slide("At sixty percent of light speed", "Gamma near light's speed")
def gam5(s):
    gam_base(s)
    for k in range(3):
        yield [FadeIn(gam_mark(k), scale=1.4), FadeIn(gam_row(k), shift=LEFT * 0.15)]


# ------------------------------------------------------------------ muons

SEA = -2.6
SKY = 2.2


def falling(t, xs, top, bottom, rate=0.55, n=None, life=None, color=PURPLE, slant=0.0, seed=1):
    """Muons falling from `top` to `bottom`. `life` is the fraction surviving to the bottom."""
    rng = np.random.default_rng(seed)
    n = n or len(xs)
    phase = rng.uniform(0, 1, n)
    if life is None:
        ends = np.full(n, 2.0)
    else:
        k = -1 / np.log(life)
        ends = -np.log(rng.uniform(0.001, 1, n)) * k

    def draw():
        g = VGroup(hollow())
        for i in range(n):
            f = (rate * t.get_value() + phase[i]) % 1
            if f > ends[i]:
                continue
            x = xs[i % len(xs)] + slant * f
            g.add(Dot(P(x, top + (bottom - top) * f), radius=0.08, color=color))
        return g
    return always_redraw(draw)


@slide("Here's the evidence.", "Muons from cosmic rays")
def mu1(s):
    t = clock(s)
    hit = (-2.4, SKY)
    sky = VGroup(DashedLine(P(-7.3, SKY), P(7.3, SKY), color=LINE, stroke_width=3), left_at(lab("top of the atmosphere", 22), 2.4, SKY + 0.3),
                 hline(-7.3, 7.3, SEA, MUTED, 4), left_at(lab("the ground", 22), 2.4, SEA - 0.3))
    yield [FadeIn(sky), GrowArrow(Arrow(P(-6.6, 2.7), P(-2.6, SKY + 0.05), buff=0, color=INK, stroke_width=4, tip_length=0.18)),
           FadeIn(at(lab("cosmic ray", 22, INK), -5.4, 1.85)), FadeIn(burst(hit))]
    xs = np.linspace(-4.2, -0.6, 9)
    yield [FadeIn(falling(t, xs, SKY - 0.1, SEA + 0.1, rate=0.5, n=18)), FadeIn(left_at(lab("muons", 28, PURPLE, True), 0.2, 0.4))]
    yield [FadeIn(left_at(lab("about 99.4% of light's speed", 26, BLUE, True), 0.2, -0.4))]


def decay_grid(x, y, alive, cols=5, rows=4, gap=0.42, color=PURPLE):
    """A grid of muons; the first `alive` are drawn, the rest are faint outlines."""
    g = VGroup()
    for i in range(rows * cols):
        c = P(x + (i % cols - (cols - 1) / 2) * gap, y - (i // cols - (rows - 1) / 2) * gap)
        if i < alive:
            g.add(Dot(c, radius=0.11, color=color))
        else:
            g.add(Circle(radius=0.11, color=LINE, stroke_width=2).move_to(c))
    return g


@slide("At that speed, gamma is nine point one.", "Muons decay")
def mu2(s):
    gam_base(s)
    yield [FadeIn(g_point(0.994, 9.1, PURPLE), scale=1.4), FadeIn(right_at(code("γ = 9.1", 28, INK), gx(0.994) - 0.2, gy(9.1)))]
    full = decay_grid(5.1, 0.4, 16, 4, 4, 0.5)
    yield [FadeIn(full), FadeIn(at(words("muons at rest decay at random", 18, 24, INK, align=ORIGIN), 5.1, 1.9))]
    half = decay_grid(5.1, 0.4, 8, 4, 4, 0.5)
    yield [Transform(full, half), FadeIn(at(words("half are gone after about 1.5 millionths of a second (μs)", 22, 24, INK, align=ORIGIN), 5.1, -1.6))]


PEAK = (-3.4, 1.5)
DET = (-0.6, SEA + 0.18)


def mountain(sy=1.0, dy=0.0):
    """Mount Washington, squashed toward its summit by sy and moved up by dy."""
    top = PEAK[1] + dy

    def Y(y):
        return top - (PEAK[1] - y) * sy
    xs = ((-6.4, SEA), (-5.2, -0.9), (-4.4, 0.4), (-3.8, 1.1), (PEAK[0], PEAK[1]), (-2.8, 0.7), (-2.2, -0.6), (-1.5, SEA))
    return Polygon(*[P(x, Y(y)) for x, y in xs], stroke_color=MUTED, stroke_width=3, fill_color=LINE, fill_opacity=0.6)


def detector(c, color=INK):
    return Rectangle(width=0.5, height=0.3, stroke_color=color, stroke_width=3, fill_color=WHITE, fill_opacity=1).move_to(P(*c))


def mountain_scene():
    m = mountain()
    sea = VGroup(hline(-7.3, 0.4, SEA, MUTED, 4), at(lab("sea level", 22), -5.2, SEA - 0.32))
    alt = VGroup(DoubleArrow(P(-6.9, SEA), P(-6.9, PEAK[1]), buff=0, color=BLUE, stroke_width=3, tip_length=0.16),
                 DashedLine(P(-6.9, PEAK[1]), P(PEAK[0], PEAK[1]), color=LINE, stroke_width=2),
                 left_at(lab("about 1,900 m", 22, BLUE, True), -7.3, PEAK[1] + 0.35))
    dets = VGroup(detector((PEAK[0], PEAK[1] + 0.17)), detector(DET))
    return m, sea, alt, dets


def muon_path(t, rate=0.4, life=None, n=10):
    top = (PEAK[0] + 0.1, PEAK[1] + 0.45)
    xs = [top[0]] * n
    return falling(t, xs, top[1], DET[1] + 0.1, rate, n, life, slant=DET[0] - top[0], seed=4)


@slide("In nineteen sixty-three, David Frisch", "Mount Washington, 1963")
def mu3(s):
    t = clock(s)
    m, sea, alt, dets = mountain_scene()
    yield [FadeIn(m), FadeIn(sea), FadeIn(left_at(lab("1963: David Frisch and James Smith", 24, MUTED), 1.0, 2.4))]
    yield [FadeIn(dets[0]), FadeIn(left_at(words("they count muons on top of Mount Washington", 26, 26, INK), 1.0, 1.4))]
    yield [FadeIn(alt)]
    yield [FadeIn(dets[1]), FadeIn(muon_path(t)), FadeIn(left_at(lab("then count again at sea level", 26, INK), 1.0, 0.2))]


def mu_base(s, t, life=None):
    m, sea, alt, dets = mountain_scene()
    s.add(m, sea, alt, dets, muon_path(t, life=life))


def trip_bar(x0, y, frac=1.0):
    L = 6.4 * 0.62 * frac
    return Rectangle(width=max(L, 0.01), height=0.36, stroke_width=0, fill_color=BLUE, fill_opacity=0.75).move_to(P(x0 + L / 2, y))


@slide("The trip down takes six point four", "The trip down")
def mu4(s):
    t = clock(s)
    mu_base(s, t, life=0.055)
    x0, y = 1.4, 1.9
    bar = trip_bar(x0, y)
    yield [GrowFromEdge(bar, LEFT), FadeIn(left_at(lab("the trip down, on the ground's clock", 24, BLUE), x0, y + 0.5)),
           FadeIn(left_at(lab("6.4 μs", 28, BLUE, True), x0 + bar.width + 0.2, y))]
    grid = decay_grid(4.0, -0.4, 20, 5, 4, 0.48)
    yield [FadeIn(grid)]
    yield [Transform(grid, decay_grid(4.0, -0.4, 1, 5, 4, 0.48)),
           FadeIn(at(lab("all but about 1 in 20 decay", 26, INK, True), 4.0, -1.9))]


BAR_B = -1.9
BAR_S = 4.0 / 560


def count_bar(k):
    vals = ((560, "about 560", "at the top", BLUE), (30, "about 30", "expected at\nsea level", RED), (410, "about 410", "measured at\nsea level", BLUE))
    v, top, name, color = vals[k]
    x = (1.9, 4.2, 6.5)[k]
    h = v * BAR_S
    bar = Rectangle(width=1.5, height=h, stroke_width=0, fill_color=color, fill_opacity=0.8).move_to(P(x, BAR_B + h / 2))
    names = VGroup(*[lab(n, 22, INK) for n in name.split("\n")]).arrange(DOWN, buff=0.08)
    return bar, at(lab(top, 24, color, True), x, BAR_B + h + 0.3), at(names, x, BAR_B - 0.25 - names.height / 2)


@slide("About five hundred and sixty per hour", "The counts")
def mu5(s):
    t = clock(s)
    mu_base(s, t, life=0.73)
    s.add(hline(0.8, 7.3, BAR_B, MUTED, 3), at(lab("muons per hour", 22, MUTED), 4.2, 2.45))
    for k in range(3):
        bar, top, name = count_bar(k)
        yield [GrowFromEdge(bar, DOWN), FadeIn(top), FadeIn(name)]


MU_X0 = -2.6       # left end of the clock bars
MU_SC = 1.05       # screen units per millionth of a second


def mu_clock_bar(y, us, color):
    L = us * MU_SC
    return Rectangle(width=L, height=0.5, stroke_width=0, fill_color=color, fill_opacity=0.75).move_to(P(MU_X0 + L / 2, y))


def half_life_line():
    x = MU_X0 + 1.5 * MU_SC
    return VGroup(DashedLine(P(x, -2.0), P(x, 2.2), color=MUTED, stroke_width=3),
                  at(words("half gone, at rest: 1.5 μs", 14, 22, MUTED, align=ORIGIN), x, -2.6))


@slide("The muons' clocks were running slow.", "The muons' own clocks")
def mu6(s):
    yg, ym = 1.2, -0.6
    gb = mu_clock_bar(yg, 6.4, BLUE)
    yield [GrowFromEdge(gb, LEFT), FadeIn(right_at(lab("the ground's clock", 26, BLUE, True), MU_X0 - 0.25, yg)),
           FadeIn(left_at(lab("6.4 μs", 28, BLUE, True), MU_X0 + gb.width + 0.2, yg)), FadeIn(half_life_line())]
    yield [FadeIn(at(code("÷ 9.1", 32, INK), MU_X0 + 3.4, 0.3)), FadeIn(at(lab("gamma", 22, INK), MU_X0 + 4.9, 0.3))]
    mb = mu_clock_bar(ym, 0.7, PURPLE)
    yield [GrowFromEdge(mb, LEFT), FadeIn(right_at(lab("the muons' own clocks", 26, PURPLE, True), MU_X0 - 0.25, ym)),
           FadeIn(at(lab("0.7 μs", 28, PURPLE, True), MU_X0 + mb.width / 2, ym - 0.6))]


@slide("That's too short for most of them to decay.", "Most of them survive")
def mu7(s):
    a = decay_grid(-3.6, 0.6, 1, 5, 4, 0.5, PURPLE)
    b = decay_grid(3.6, 0.6, 15, 5, 4, 0.5, PURPLE)
    yield [FadeIn(a), FadeIn(at(lab("if clocks ran normally: 6.4 μs", 24, RED, True), -3.6, 2.2)),
           FadeIn(at(lab("almost all decay", 24, INK), -3.6, -1.1))]
    yield [FadeIn(b), FadeIn(at(lab("on the muons' clocks: 0.7 μs", 24, PURPLE, True), 3.6, 2.2)),
           FadeIn(at(lab("most survive", 24, INK), 3.6, -1.1))]
    yield [FadeIn(at(pill("moving clocks really do run slow, by the factor gamma", BLUE, 28), 0, -2.4), shift=UP * 0.15)]


# ================================================================== moving lengths shrink
deck.part("Moving lengths shrink")

MUON = (-1.6, PEAK[1] + 0.35)


def muon_dot(r=0.2):
    return Dot(P(*MUON), radius=r, color=PURPLE)


@slide("Moving lengths shrink.", "The muon's side")
def len1(s):
    t = clock(s)
    m, sea, alt, dets = mountain_scene()
    s.add(m, sea, alt)
    yield [FadeIn(muon_dot()), FadeIn(left_at(lab("from the muon's side", 28, PURPLE, True), 1.2, 2.35))]
    yield [FadeIn(live_dial((MUON[0] + 0.85, MUON[1]), t, 1.0, 0.42, PURPLE)),
           FadeIn(left_at(words("to the muon, its own clock is perfectly normal", 22, 26, PURPLE), 1.2, 1.1))]
    q = VGroup(DashedLine(P(MUON[0], MUON[1] - 0.3), P(MUON[0], SEA + 0.1), color=PURPLE, stroke_width=3),
               at(T("?", 40, PURPLE, True), MUON[0] + 0.45, -0.6))
    yield [Create(q[0]), FadeIn(q[1]), FadeIn(left_at(lab("so how does it reach the ground?", 26, INK, True), 1.2, -0.6))]


def squash_scene(sq, dy=0.0):
    top = PEAK[1]
    sea_y = top - (top - SEA) * sq
    return VGroup(mountain(sq), hline(-7.3, 0.4, sea_y, MUTED, 4))


@slide("To the muon, the mountain is what's moving.", "The mountain shrinks")
def len2(s):
    t = clock(s)
    sq = ValueTracker(1.0)
    s.add(sq, always_redraw(lambda: squash_scene(sq.get_value())), muon_dot(), live_dial((MUON[0] + 0.85, MUON[1]), t, 1.0, 0.42, PURPLE))
    ups = VGroup(*[Arrow(P(x, -2.2), P(x, -1.1), buff=0, color=PURPLE, stroke_width=5, tip_length=0.18) for x in (0.6, 1.2)])
    yield [GrowArrow(ups[0]), GrowArrow(ups[1]), FadeIn(left_at(words("to the muon, the mountain is what's moving", 22, 26, PURPLE), 1.8, -1.0))]
    yield [sq.animate.set_value(1 / 9.1), ups.animate.shift(UP * 2.0),
           FadeIn(left_at(words("moving lengths shrink, by the same factor gamma", 22, 26, INK), 1.8, 1.3))]


@slide("The nineteen hundred metres of air shrinks", "About 210 metres")
def len3(s):
    t = clock(s)
    sq = 1 / 9.1
    sea_y = PEAK[1] - (PEAK[1] - SEA) * sq
    dy = ValueTracker(0.0)
    s.add(dy)
    ghost = VGroup(DashedLine(P(-6.9, SEA), P(-6.9, PEAK[1]), color=BLUE, stroke_width=3),
                   left_at(lab("1,900 m, for the ground", 22, BLUE), -7.3, SEA - 0.35))
    s.add(always_redraw(lambda: squash_scene(sq).shift(UP * dy.get_value())), muon_dot())
    br = Brace(Line(P(-1.0, sea_y), P(-1.0, PEAK[1])), RIGHT, color=PURPLE)
    short = VGroup(br, lab("about 210 m, for the muon", 24, PURPLE, True).next_to(br, RIGHT, buff=0.12))
    yield [FadeIn(ghost), FadeIn(short)]
    d = MUON[1] - 0.25 - sea_y
    yield [dy.animate.set_value(d), short.animate.shift(UP * d),
           FadeIn(left_at(words("short enough to cross in 0.7 μs", 20, 28, PURPLE), 1.2, -0.4)),
           FadeIn(live_dial((5.6, -0.6), t, 1.0, 0.5, PURPLE)), FadeIn(at(lab("the muon's own clock", 22, PURPLE), 5.6, -1.4))]


def view_card(x, title, color):
    return VGroup(at(card(None, 6.6, 4.1, color), x, 0.15), at(lab(title, 26, color, True), x, 1.85))


@slide("So the two views tell the story", "Two views, one story")
def len4(s):
    t = clock(s)
    L, R = -3.65, 3.65
    yield [FadeIn(view_card(L, "the ground says", BLUE)), FadeIn(view_card(R, "the muon says", PURPLE))]
    tall = VGroup(Rectangle(width=0.9, height=2.6, stroke_width=0, fill_color=LINE, fill_opacity=0.8).move_to(P(L - 2.2, -0.2)),
                  live_dial((L - 0.6, 0.5), t, 0.11, 0.55, PURPLE))
    yield [FadeIn(tall), FadeIn(at(words("the muon's clock runs slow", 14, 24, INK, align=ORIGIN), L + 1.5, -0.4))]
    short = VGroup(Rectangle(width=0.9, height=0.3, stroke_width=0, fill_color=PURPLE, fill_opacity=0.45).move_to(P(R - 2.2, -1.35)),
                   live_dial((R - 0.6, 0.5), t, 1.0, 0.55, PURPLE))
    yield [FadeIn(short), FadeIn(at(words("the mountain is short", 12, 24, INK, align=ORIGIN), R + 1.5, -0.4))]


@slide("But they agree on what actually happens.", "Two views, one story")
def len5(s):
    L, R = -3.65, 3.65
    a = at(card("the muon's clock\nruns slow", 4.0, 1.3, BLUE, 26), L, 1.2)
    b = at(card("the mountain\nis short", 4.0, 1.3, PURPLE, 26), R, 1.2)
    s.add(a, b, at(lab("the ground says", 24, BLUE), L, 2.3), at(lab("the muon says", 24, PURPLE), R, 2.3))
    out = at(card("most muons reach the ground", 6.0, 1.1, TEAL, 30), 0, -1.4)
    yield [GrowArrow(arrow(a.get_bottom(), out.get_top() + LEFT * 1.0)), GrowArrow(arrow(b.get_bottom(), out.get_top() + RIGHT * 1.0)),
           FadeIn(at(lab("they agree on what actually happens", 26, INK), 0, -2.55))]
    yield [FadeIn(out), FadeIn(tick(out))]


@slide("Lengths shrink only along the direction", "Shorter, not thinner")
def len6(s):
    cy = 0.4
    rest = carriage(-0.8, cy, 6.0, 1.9, LINE, WHITE, 0)
    k = ValueTracker(1.0)
    moving = always_redraw(lambda: carriage(-0.8 - 3.0 * (1 - k.get_value()), cy, 6.0 * k.get_value(), 1.9, INK))
    yield [FadeIn(rest), FadeIn(moving), FadeIn(hline(-7.3, 7.3, cy - 1.23, MUTED, 3))]
    yield [k.animate.set_value(0.6), GrowArrow(Arrow(P(-3.8, 2.2), P(-1.6, 2.2), buff=0, color=BLUE, stroke_width=5, tip_length=0.2)),
           FadeIn(left_at(lab("going by", 24, BLUE), -1.4, 2.2)),
           FadeIn(at(lab("shorter along the motion", 26, BLUE, True), -2.6, -1.6))]
    hgt = VGroup(DoubleArrow(P(0.15, cy - 0.95), P(0.15, cy + 0.95), buff=0, color=BLUE, stroke_width=4, tip_length=0.14),
                 left_at(lab("same height: not thinner", 26, BLUE, True), 2.6, cy))
    yield [FadeIn(hgt)]


# ================================================================== same moment depends on who's watching
deck.part("Same moment depends on who's watching")

CW, CH = 5.0, 1.3
FX = -0.8               # where the lamp flashes
ROW_T, ROW_P = 1.25, -1.45
FV = 0.4                # the carriage's speed, as a fraction of light's
T_BACK, T_FRONT = (CW / 2) / (1 + FV), (CW / 2) / (1 - FV)


def flash_row(cy, tau, v=0.0):
    xc = FX + v * tau
    L = CW / 2
    back, front = xc - L, xc + L
    g = VGroup(carriage(xc, cy, CW, CH))
    if tau > 0:
        lb, rf = max(FX - tau, back), min(FX + tau, front)
        g.add(Rectangle(width=max(rf - lb, 0.01), height=CH - 0.12, stroke_width=0, fill_color=ORANGE, fill_opacity=0.18).move_to(P((lb + rf) / 2, cy)))
        for x, hit in ((lb, FX - tau <= back), (rf, FX + tau >= front)):
            if hit:
                g.add(burst((x, cy), 0.3))
            else:
                g.add(Line(P(x, cy - CH / 2 + 0.08), P(x, cy + CH / 2 - 0.08), color=ORANGE, stroke_width=6))
    g.add(Dot(P(xc, cy), radius=0.13, color=ORANGE if tau == 0 else INK))
    return g


def rail(cy):
    return hline(-7.3, 7.3, cy - CH / 2 - 0.3, MUTED, 3)


@slide("Same moment depends on who's watching.", "A flash in a carriage")
def fl1(s):
    tau = ValueTracker(0.0)
    s.add(tau)
    row = always_redraw(lambda: flash_row(ROW_T, tau.get_value()))
    yield [FadeIn(rail(ROW_T)), FadeIn(row), FadeIn(left_at(lab("on the train", 26, PURPLE, True), -7.3, ROW_T + 1.05)),
           FadeIn(at(lab("a lamp in the middle", 22, INK), FX, ROW_T - 1.3))]
    yield [tau.animate.set_value(0.35)]


@slide("On the train, the light reaches the front", "Seen on the train")
def fl2(s):
    tau = ValueTracker(0.35)
    s.add(tau, rail(ROW_T), always_redraw(lambda: flash_row(ROW_T, tau.get_value())),
          left_at(lab("on the train", 26, PURPLE, True), -7.3, ROW_T + 1.05))
    yield [tau.animate.set_value(CW / 2 + 0.01), FadeIn(left_at(lab("both walls at the same moment", 24, PURPLE, True), 2.4, ROW_T + 1.05))]
    br = VGroup(BraceBetweenPoints(P(FX - CW / 2, ROW_T - 1.0), P(FX, ROW_T - 1.0), direction=DOWN, color=PURPLE),
                BraceBetweenPoints(P(FX, ROW_T - 1.0), P(FX + CW / 2, ROW_T - 1.0), direction=DOWN, color=PURPLE))
    yield [FadeIn(br), FadeIn(at(lab("the same distance each way", 24, PURPLE), FX, ROW_T - 1.8))]


def train_done(s):
    s.add(rail(ROW_T), flash_row(ROW_T, CW / 2 + 0.01), left_at(lab("on the train", 26, PURPLE, True), -7.3, ROW_T + 1.05),
          left_at(lab("both walls at the same moment", 24, PURPLE, True), 2.4, ROW_T + 1.05))


@slide("Now watch from the platform.", "Seen from the platform")
def fl3(s):
    train_done(s)
    yield [FadeIn(rail(ROW_P)), FadeIn(flash_row(ROW_P, 0.0, FV)), FadeIn(left_at(lab("from the platform", 26, BLUE, True), -7.3, ROW_P + 1.05)),
           GrowArrow(Arrow(P(3.0, ROW_P + 1.05), P(4.6, ROW_P + 1.05), buff=0, color=BLUE, stroke_width=5, tip_length=0.2))]
    back = FX - CW / 2
    front = FX + CW / 2
    yield [GrowArrow(Arrow(P(back - 0.9, ROW_P), P(back - 0.15, ROW_P), buff=0, color=BLUE, stroke_width=5, tip_length=0.18)),
           GrowArrow(Arrow(P(front + 0.15, ROW_P), P(front + 0.9, ROW_P), buff=0, color=BLUE, stroke_width=5, tip_length=0.18)),
           FadeIn(at(words("back wall: moving toward the flash", 20, 22, BLUE, align=ORIGIN), back - 0.6, ROW_P - 1.45)),
           FadeIn(at(words("front wall: moving away", 24, 22, BLUE, align=ORIGIN), front + 1.0, ROW_P - 1.3))]


@slide("And light's speed is the same either way.", "The back wall first")
def fl4(s):
    train_done(s)
    tau = ValueTracker(0.0)
    s.add(tau, rail(ROW_P), always_redraw(lambda: flash_row(ROW_P, tau.get_value(), FV)),
          left_at(lab("from the platform", 26, BLUE, True), -7.3, ROW_P + 1.05),
          Arrow(P(3.0, ROW_P + 1.05), P(4.6, ROW_P + 1.05), buff=0, color=BLUE, stroke_width=5, tip_length=0.2))
    yield [tau.animate.set_value(T_BACK + 0.01), FadeIn(at(lab("light's speed: the same either way", 24, TEAL, True), 0, -0.1))]
    yield [FadeIn(at(lab("the back wall first", 26, BLUE, True), FX - CW / 2 + 0.3, ROW_P - 1.3))]
    yield [tau.animate.set_value(T_FRONT + 0.01), FadeIn(at(lab("then the front wall", 26, BLUE, True), FX + CW / 2 + 1.4, ROW_P - 1.3))]


def timeline(y, name, color, xs):
    g = VGroup(axis_arrow((-2.4, y), (5.6, y)), right_at(lab(name, 26, color, True), -2.7, y),
               at(lab("time", 22), 5.3, y - 0.35))
    for x, tag in xs:
        d = burst((x, y), 0.24)
        g.add(d, at(lab(tag, 22, INK), x, y + 0.5))
    return g


@slide("So two events that happen at the same time", "Same time depends on who's watching")
def fl5(s):
    a = timeline(1.0, "on the train", PURPLE, ((1.5, "back and front"),))
    b = timeline(-1.0, "from the platform", BLUE, ((0.4, "back"), (3.4, "front")))
    yield [FadeIn(a)]
    yield [FadeIn(b), FadeIn(at(words("the same two events: at the same time for one observer, at different times for another", 60, 24, INK, align=ORIGIN), 0, -2.6))]


@slide("Slow clocks, short lengths", "One rule behind all three")
def lor1(s):
    icons = VGroup(VGroup(dial((-4.8, 1.4), 0.5), at(lab("slow clocks", 24, INK), -4.8, 0.55)),
                   VGroup(ruler(0, 1.4, 2.0, 0.42), at(lab("short lengths", 24, INK), 0, 0.55)),
                   VGroup(burst((4.4, 1.4), 0.25), burst((5.2, 1.4), 0.25), at(lab("same time, or not", 24, INK), 4.8, 0.55)))
    yield [FadeIn(icons[0]), FadeIn(icons[1])]
    yield [FadeIn(icons[2])]
    box = at(card("the Lorentz transformation", 6.0, 1.2, INK, 32, bold=True), 0, -1.6)
    yield [*[GrowArrow(Arrow(P(x, 0.25), P(x * 0.35, -0.95), buff=0, color=MUTED, stroke_width=4, tip_length=0.18)) for x in (-4.8, 0.0, 4.8)],
           FadeIn(box)]


@slide("It converts one observer's times", "The Lorentz transformation")
def lor2(s):
    box = at(card("the Lorentz\ntransformation", 3.6, 1.4, INK, 28), 0, 1.2)
    a = at(card("one observer's\ntimes and positions", 3.8, 1.4, BLUE, 26), -5.2, 1.2)
    b = at(card("another's times\nand positions", 3.8, 1.4, PURPLE, 26), 5.2, 1.2)
    yield [FadeIn(a), GrowArrow(arrow(a, box)), FadeIn(box), GrowArrow(arrow(box, b)), FadeIn(b)]
    low = at(VGroup(lab("at everyday speeds:", 26, INK), T("speeds add, 30 + 1 = 31 m/s", 28, BLUE, True), check()).arrange(RIGHT, buff=0.25), 0, -1.3)
    yield [GrowArrow(Arrow(P(0, 0.4), P(0, -0.8), buff=0, color=MUTED, stroke_width=4, tip_length=0.18)), FadeIn(low)]


# ================================================================== what everyone agrees on
deck.part("What everyone agrees on")


def readout_rows():
    rows = VGroup()
    data = (("the ground", BLUE, 4.3, 0.994 * 4.3), ("the muon", PURPLE, 0.48, 0.0))
    for k, (name, color, tl, dl) in enumerate(data):
        y = 1.6 - 1.7 * k
        rows.add(VGroup(right_at(lab(name, 26, color, True), -4.9, y),
                        left_at(lab("time apart", 22), -4.6, y + 0.3), Rectangle(width=max(tl, 0.04), height=0.3, stroke_width=0, fill_color=color, fill_opacity=0.75).move_to(P(-2.2 + tl / 2, y + 0.3)),
                        left_at(lab("distance apart", 22), -4.6, y - 0.3), Rectangle(width=max(dl, 0.04), height=0.3, stroke_width=0, fill_color=color, fill_opacity=0.75).move_to(P(-2.2 + dl / 2, y - 0.3))))
    return rows


@slide("What everyone agrees on.", "Disagreeing observers")
def agr1(s):
    rows = readout_rows()
    yield [FadeIn(rows), FadeIn(at(lab("the muon's birth and arrival", 24, INK), -0.4, 2.45))]
    comb = VGroup(*[Rectangle(width=1.6, height=0.4, stroke_width=0, fill_color=TEAL, fill_opacity=0.8).move_to(P(5.4, 1.6 - 1.7 * k)) for k in range(2)])
    yield [LaggedStart(*[GrowFromEdge(c, LEFT) for c in comb], lag_ratio=0.3), FadeIn(at(lab("one combination", 24, TEAL, True), 5.4, 2.45)),
           FadeIn(at(lab("everyone agrees on it", 26, TEAL, True), 0, -2.3))]


EO = (-5.0, -1.3)     # first event
EDX, EDT = 1.6, 3.6   # screen sizes of the distance and of c times the time


def events_base(long=True):
    e1, q, e2 = P(*EO), P(EO[0] + EDX, EO[1]), P(EO[0] + EDX, EO[1] + EDT)
    g = VGroup(DashedLine(e1, q, color=MUTED, stroke_width=3), DashedLine(q, e2, color=MUTED, stroke_width=3),
               Dot(e1, radius=0.12, color=INK), Dot(e2, radius=0.12, color=INK),
               right_at(lab("event 1", 22, INK), e1[0] - 0.2, e1[1]), right_at(lab("event 2", 22, INK), e2[0] - 0.2, e2[1]))
    if long:
        g.add(lab("distance apart: Δx", 22, INK).next_to(Line(e1, q), DOWN, buff=0.2))
    else:
        g.add(lab("Δx", 24, INK).next_to(Line(e1, q), UP, buff=0.15))
    return g


def time_label(text, bold=False):
    return right_at(lab(text, 24 if not bold else 26, INK, bold), EO[0] + EDX - 0.2, EO[1] + EDT / 2)


@slide("Here's how to build it.", "Time as a distance")
def agr2(s):
    base = events_base()
    tl = time_label("time apart: Δt")
    yield [FadeIn(base), FadeIn(tl)]
    steps = VGroup(lab("the time between the events", 26, INK), lab("× the speed of light", 26, TEAL, True),
                   lab("= a distance:  c Δt", 26, INK, True)).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
    left_at(steps, 1.2, 0.6)
    yield [FadeIn(steps[0]), FadeIn(steps[1])]
    yield [FadeIn(steps[2]), Transform(tl, time_label("c Δt", True))]


def squares():
    big = Square(EDT, stroke_color=INK, stroke_width=3, fill_color=TEAL, fill_opacity=0.25)
    big.move_to(P(EO[0] + EDX + EDT / 2, EO[1] + EDT / 2))
    small = Square(EDX, stroke_color=INK, stroke_width=3, fill_color=MUTED, fill_opacity=0.25)
    small.move_to(P(EO[0] + EDX / 2, EO[1] - EDX / 2))
    return big, small


INTERVAL = "s² = (c Δt)² − Δx²"


@slide("Square it.", "The spacetime interval")
def agr3(s):
    s.add(events_base(False), time_label("c Δt", True))
    big, small = squares()
    yield [DrawBorderThenFill(big), FadeIn(at(code("(c Δt)²", 28, INK), big.get_center()[0], big.get_center()[1] + 0.9))]
    hole = small.copy()
    yield [DrawBorderThenFill(small), FadeIn(at(code("Δx²", 24, INK), small.get_center()[0], small.get_center()[1])),
           hole.animate.move_to(P(EO[0] + EDX + EDX / 2, EO[1] + EDX / 2)).set_fill(WHITE, 1)]
    yield [FadeIn(at(T("the spacetime interval", 30, TEAL, True), 4.6, 1.6)),
           FadeIn(at(code(INTERVAL, 34, TEAL), 4.6, 0.6)),
           FadeIn(at(lab("what's left after taking the small square away", 22, INK), 4.6, -0.3))]


@slide("It's a bit like the length of a ruler.", "Like a ruler's length")
def agr4(s):
    t = clock(s)
    c = (-3.6, -0.5)
    L = 3.2

    def draw():
        a = 0.35 + 0.55 * np.sin(0.8 * t.get_value())
        tip = P(c[0] + L * np.cos(a), c[1] + L * np.sin(a))
        o = P(*c)
        r = Line(o, tip, color=INK, stroke_width=12)
        return VGroup(DashedVMobject(Line(o, P(tip[0], c[1]), color=MUTED, stroke_width=3), num_dashes=14), DashedVMobject(Line(P(tip[0], c[1]), tip, color=MUTED, stroke_width=3), num_dashes=10), r)
    yield [FadeIn(always_redraw(draw)), FadeIn(at(lab("turn a ruler: its parts across and up change", 24, INK), -3.4, 2.45))]
    yield [FadeIn(at(code("across² + up² = length²", 30, INK), -3.4, -2.4)), FadeIn(at(lab("the length stays the same", 24, INK, True), -3.4, -3.0))]
    yield [FadeIn(at(lab("the interval: the same idea", 26, TEAL, True), 4.0, 1.0)), FadeIn(at(code(INTERVAL, 30, TEAL), 4.0, 0.1)),
           FadeIn(at(lab("but with a minus sign", 26, INK, True), 4.0, -0.8))]


MSC = 3.0 / 1900   # screen units per metre in the muon diagrams
MO_Y = -1.0        # height of the diagrams' origins


def st_axes(o, w, h):
    return VGroup(axis_arrow(o, (o[0] + w, o[1])), axis_arrow(o, (o[0], o[1] + h)),
                  left_at(lab("distance", 22), o[0] + w - 1.0, o[1] - 0.32), left_at(lab("time × c", 22), o[0] + 0.15, o[1] + h + 0.0))


def ground_diagram():
    o = (-6.4, MO_Y)
    e2 = P(o[0] + 1907 * MSC, o[1] + 1918.5 * MSC)
    g = VGroup(st_axes(o, 4.0, 3.5), Line(P(*o), e2, color=PURPLE, stroke_width=5), Dot(P(*o), radius=0.11, color=PURPLE), Dot(e2, radius=0.11, color=PURPLE),
               left_at(lab("birth, at the top", 22, PURPLE), o[0], o[1] - 0.33),
               right_at(lab("arrival, at sea level", 22, PURPLE), e2[0] - 0.2, e2[1] + 0.05))
    return g, o, e2


def ground_legs(o, e2):
    q = P(e2[0], o[1])
    return VGroup(DashedLine(P(*o), q, color=BLUE, stroke_width=3), DashedLine(q, e2, color=BLUE, stroke_width=3),
                  at(lab("1,900 m", 24, BLUE, True), (o[0] + e2[0]) / 2 + 0.6, o[1] - 0.7),
                  left_at(lab("c × 6.4 μs", 24, BLUE, True), e2[0] + 0.2, (o[1] + e2[1]) / 2))


@slide("The muon shows it.", "The muon's trip, for the ground")
def agr5(s):
    g, o, e2 = ground_diagram()
    yield [FadeIn(g[0]), FadeIn(g[2:]), FadeIn(at(lab("two events", 26, INK, True), 3.4, 2.2))]
    yield [Create(g[1])]
    legs = ground_legs(o, e2)
    yield [Create(legs[0]), Create(legs[1]), FadeIn(legs[2:]), FadeIn(at(lab("the ground: 6.4 μs and 1,900 m apart", 26, BLUE, True), 3.4, 1.2))]


@slide("The muon's own clock says", "The muon's trip, for the muon")
def agr6(s):
    g, o, e2 = ground_diagram()
    s.add(g, ground_legs(o, e2))
    o2 = (2.4, MO_Y)
    top = P(o2[0], o2[1] + 210 * MSC)
    yield [FadeIn(st_axes(o2, 4.0, 3.5)), Create(Line(P(*o2), top, color=PURPLE, stroke_width=6)), FadeIn(Dot(P(*o2), radius=0.11, color=PURPLE)),
           FadeIn(Dot(top, radius=0.11, color=PURPLE)), FadeIn(left_at(lab("c × 0.7 μs", 24, PURPLE, True), o2[0] + 0.25, top[1] + 0.2))]
    yield [FadeIn(left_at(words("no distance apart: the mountain moves, the muon stays put", 22, 24, PURPLE), o2[0] + 0.25, 1.0))]
    r1 = at(VGroup(code("(1,918.5 m)² − (1,907 m)²", 24, BLUE), code("≈ (210 m)²", 26, TEAL)).arrange(DOWN, buff=0.14), -4.2, -2.6)
    r2 = at(VGroup(code("(c × 0.7 μs)² − 0²", 24, PURPLE), code("≈ (210 m)²", 26, TEAL)).arrange(DOWN, buff=0.14), 4.4, -2.6)
    yield [FadeIn(r1), FadeIn(r2), FadeIn(at(T("=", 40, TEAL, True), 0.2, -2.6))]


@slide("Here's a handy fact.", "The interval on the traveller's clock")
def agr7(s):
    t = clock(s)
    o = (-4.4, -2.6)
    yield [FadeIn(st_axes(o, 3.6, 4.8)), FadeIn(Line(P(*o), P(o[0], 1.8), color=PURPLE, stroke_width=6)),
           FadeIn(live_dial((o[0] + 1.2, 0.3), t, 1.0, 0.55, PURPLE)), FadeIn(left_at(lab("the muon's own clock", 22, PURPLE), o[0] + 0.3, -0.55))]
    yield [FadeIn(at(T("interval = time on its own clock × c", 28, TEAL, True), 2.6, 1.0)),
           FadeIn(at(code("0.7 μs × c ≈ 210 m", 30, TEAL), 2.6, -0.2))]


SX0, SXS = 0.0, 1.0   # the interval's number line: centre and units


@slide("Because of the minus sign", "Positive, zero or negative")
def sign1(s):
    y = 0.9
    ln = VGroup(Line(P(-6.5, y), P(6.5, y), color=MUTED, stroke_width=3), Line(P(0, y - 0.15), P(0, y + 0.15), color=MUTED, stroke_width=3))
    signs = VGroup(at(lab("negative", 26, TEAL, True), -3.5, y + 0.55), at(lab("zero", 26, TEAL, True), 0, y + 0.55),
                   at(lab("positive", 26, TEAL, True), 3.5, y + 0.55))
    yield [FadeIn(ln), FadeIn(at(lab("the interval", 24, TEAL, True), 0, 2.2))]
    yield [LaggedStart(*[FadeIn(g) for g in signs], lag_ratio=0.3)]
    yield [Indicate(signs[0], color=TEAL)]
    neg = Rectangle(width=6.4, height=0.5, stroke_width=0, fill_color=MUTED, fill_opacity=0.15).move_to(P(-3.3, y - 1.2))
    pos = Rectangle(width=6.4, height=0.5, stroke_width=0, fill_color=INK, fill_opacity=0.3).move_to(P(3.3, y - 1.2))
    yield [FadeIn(pos), FadeIn(neg), FadeIn(at(lab("a length", 24, INK, True), 3.3, y - 1.85)),
           Create(cross(neg, RED, 4)), FadeIn(at(lab("a length can't be negative", 24, RED), -3.3, y - 1.85))]
    yield [FadeIn(at(lab("the sign tells you how the two events can be connected", 26, INK, True), 0, -2.4))]
    yield hold()


# ------------------------------------------------------------------ the light cone

LC = (-3.7, -0.5)
LR = 2.5
EV_A, EV_B, EV_C = (0.5, 1.8), (1.4, 1.4), (2.3, 0.8)


def lcp(p):
    return P(LC[0] + p[0], LC[1] + p[1])


def cone_base(cone=False):
    c = P(*LC)
    g = VGroup(axis_arrow((LC[0] - 3.2, LC[1]), (LC[0] + 3.3, LC[1])), axis_arrow((LC[0], LC[1] - 2.8), (LC[0], LC[1] + 3.1)),
               left_at(lab("time", 22), LC[0] + 0.2, LC[1] + 3.0), at(lab("space", 22), LC[0] + 3.0, LC[1] - 0.35))
    for sgn in (-1, 1):
        g.add(DashedLine(c + P(-LR, -LR * sgn), c + P(LR, LR * sgn), color=ORANGE, stroke_width=3))
    g.add(Dot(c, radius=0.11, color=INK), right_at(lab("an event", 22, INK), LC[0] - 0.2, LC[1] - 0.3))
    return g


def ray_to(p, color=ORANGE):
    """Light leaving the central event toward the side of point p, as far as p's place."""
    return Arrow(P(*LC), lcp((p[0], abs(p[0]))), buff=0, color=color, stroke_width=5, tip_length=0.18)


def cone_text(y, title, body, color=TEAL):
    return VGroup(left_at(lab(title, 26, color, True), 0.4, y), left_at(words(body, 60, 22, INK), 0.4, y - 0.45))


def place_line(p):
    return DashedLine(lcp((p[0], 0)), lcp((p[0], max(p[1], abs(p[0])) + 0.3)), color=LINE, stroke_width=2)


@slide("If it's positive", "Positive interval")
def cone1(s):
    s.add(cone_base())
    a = Dot(lcp(EV_A), radius=0.12, color=PURPLE)
    yield [FadeIn(a), FadeIn(lab("A", 24, PURPLE, True).next_to(a, LEFT, buff=0.12)), FadeIn(place_line(EV_A)), GrowArrow(ray_to(EV_A)),
           FadeIn(cone_text(2.2, "positive: more than enough time", "light reaches A's place before A happens"))]
    yield [Create(Line(P(*LC), lcp(EV_A), color=PURPLE, stroke_width=5)),
           FadeIn(left_at(words("so something slower than light can make the trip too", 60, 22, PURPLE), 0.4, 1.3))]
    yield [FadeIn(left_at(words("every observer agrees which came first", 60, 22, INK), 0.4, 0.85))]


def cone_a(s, brief=False):
    a = Dot(lcp(EV_A), radius=0.12, color=PURPLE)
    s.add(cone_base(), a, lab("A", 24, PURPLE, True).next_to(a, LEFT, buff=0.12), Line(P(*LC), lcp(EV_A), color=PURPLE, stroke_width=5))
    if brief:
        s.add(left_at(lab("positive: more than enough time", 24, MUTED, True), 0.4, 2.2))
        return
    s.add(cone_text(2.2, "positive: more than enough time", "light reaches A's place before A happens"),
          left_at(words("so something slower than light can make the trip too", 60, 22, PURPLE), 0.4, 1.3),
          left_at(words("every observer agrees which came first", 60, 22, INK), 0.4, 0.85))


@slide("If it's zero", "Zero interval")
def cone2(s):
    cone_a(s)
    b = Dot(lcp(EV_B), radius=0.12, color=ORANGE)
    yield [FadeIn(b), FadeIn(lab("B", 24, ORANGE, True).next_to(b, RIGHT, buff=0.12)), GrowArrow(Arrow(P(*LC), lcp(EV_B), buff=0.1, color=ORANGE, stroke_width=5, tip_length=0.18)),
           FadeIn(cone_text(0.2, "zero: exactly enough time for light", "only light can connect them"))]


def cone_b(s, brief=False):
    cone_a(s, brief)
    b = Dot(lcp(EV_B), radius=0.12, color=ORANGE)
    s.add(b, lab("B", 24, ORANGE, True).next_to(b, RIGHT, buff=0.12), Arrow(P(*LC), lcp(EV_B), buff=0.1, color=ORANGE, stroke_width=5, tip_length=0.18))
    if brief:
        s.add(left_at(lab("zero: exactly enough time for light", 24, MUTED, True), 0.4, 1.6))
    else:
        s.add(cone_text(0.2, "zero: exactly enough time for light", "only light can connect them"))


@slide("If it's negative", "Negative interval")
def cone3(s):
    cone_b(s, brief=True)
    c = Dot(lcp(EV_C), radius=0.12, color=INK)
    yield [FadeIn(c), FadeIn(lab("C", 24, INK, True).next_to(c, RIGHT, buff=0.12)), FadeIn(place_line(EV_C)),
           FadeIn(cone_text(0.6, "negative: not even light has time", "so nothing can get from one to the other"))]
    yield [FadeIn(left_at(words("the order can depend on who's watching, like the train flash", 42, 22, INK), 0.4, -0.55))]


@slide("But since nothing can travel between them", "Cause and effect stay safe")
def cone4(s):
    cone_b(s, brief=True)
    c = Dot(lcp(EV_C), radius=0.12, color=INK)
    s.add(c, lab("C", 24, INK, True).next_to(c, RIGHT, buff=0.12), place_line(EV_C),
          cone_text(0.6, "negative: not even light has time", "so nothing can get from one to the other"))
    sig = DashedLine(P(*LC), lcp(EV_C), color=RED, stroke_width=4)
    yield [Create(sig), FadeIn(cross(Square(0.4).move_to(lcp((EV_C[0] / 2, EV_C[1] / 2))), RED, 5)),
           FadeIn(left_at(lab("neither can cause the other", 24, INK, True), 0.4, -0.5))]
    yield [FadeIn(left_at(VGroup(lab("cause and effect stay safe", 28, TEAL, True), check()).arrange(RIGHT, buff=0.2), 0.4, -1.4))]


def cone_shape():
    c = P(*LC)
    g = VGroup(Polygon(c, c + P(LR, LR), c + P(-LR, LR), stroke_width=0, fill_color=PURPLE, fill_opacity=0.1),
               Polygon(c, c + P(LR, -LR), c + P(-LR, -LR), stroke_width=0, fill_color=PURPLE, fill_opacity=0.06),
               Ellipse(width=2 * LR, height=0.55, color=ORANGE, stroke_width=3).move_to(c + P(0, LR)),
               DashedVMobject(Ellipse(width=2 * LR, height=0.55, color=ORANGE, stroke_width=3).move_to(c + P(0, -LR)), num_dashes=30))
    return g


@slide("Picture it as a cone around an event", "The light cone")
def cone5(s):
    s.add(cone_base())
    yield [FadeIn(cone_shape()), FadeIn(right_at(lab("future", 22, INK), LC[0] - 0.8, LC[1] + 1.9)),
           FadeIn(right_at(lab("past", 22, INK), LC[0] - 0.8, LC[1] - 1.9))]
    yield [FadeIn(left_at(T("the light cone", 34, ORANGE, True), 0.6, 1.4))]
    yield [FadeIn(left_at(words("its edge: where light from the event can reach", 30, 26, ORANGE), 0.6, 0.3))]


def cone_dots(kind):
    rng = np.random.default_rng(7 + kind)
    pts = []
    if kind == 0:
        for _ in range(7):
            y = rng.uniform(0.6, 2.4) * rng.choice([-1, 1])
            pts.append((rng.uniform(-0.75, 0.75) * abs(y), y))
        color = PURPLE
    elif kind == 1:
        for _ in range(6):
            y = rng.uniform(0.6, 2.4) * rng.choice([-1, 1])
            pts.append((abs(y) * rng.choice([-1, 1]), y))
        color = ORANGE
    else:
        for _ in range(7):
            x = rng.uniform(1.0, 2.8) * rng.choice([-1, 1])
            pts.append((x, rng.uniform(-0.6, 0.6) * abs(x)))
        color = INK
    return VGroup(*[Dot(lcp(p), radius=0.1, color=color) for p in pts])


@slide("Events inside the cone have a positive", "Inside, on and outside")
def cone6(s):
    s.add(cone_base(), cone_shape(), left_at(T("the light cone", 34, ORANGE, True), 0.6, 2.2))
    rows = (("inside: a positive interval", PURPLE), ("on the edge: zero", ORANGE), ("outside: a negative interval", INK))
    for k, (text, color) in enumerate(rows):
        y = 1.0 - 1.1 * k
        yield [LaggedStart(*[FadeIn(d, scale=1.6) for d in cone_dots(k)], lag_ratio=0.1),
               FadeIn(left_at(VGroup(Dot(radius=0.1, color=color), lab(text, 26, color, True)).arrange(RIGHT, buff=0.25), 0.6, y))]


# ================================================================== energy and mass
deck.part("Energy and mass")


@slide("Energy and mass.", "Mass holds energy")
def em1(s):
    t = clock(s)
    floor = hline(-6.0, -1.0, -1.2, MUTED, 4)
    yield [FadeIn(floor), FadeIn(block(-3.5, -0.4, 1.6)), FadeIn(at(lab("sitting still", 24, INK), -3.5, -1.65)),
           FadeIn(left_at(words("mass is a form of energy", 22, 30, INK), 0.6, 1.4))]
    glow = always_redraw(lambda: block(-3.5, -0.4, 1.6, 0.35 + 0.25 * np.sin(2.5 * t.get_value())))
    yield [FadeIn(glow), FadeIn(left_at(words("anything with mass holds an energy, even when it sits still", 26, 26, TEAL), 0.6, 0.0))]


EMC = "E = mc²"


@slide("We call it the rest energy.", "E = mc²")
def em2(s):
    t = clock(s)
    s.add(always_redraw(lambda: block(-5.2, 0.4, 1.4, 0.35 + 0.25 * np.sin(2.5 * t.get_value()))))
    yield [FadeIn(at(T("the rest energy", 32, TEAL, True), -5.2, 1.75))]
    parts = VGroup(chip("mass", INK, size=28, h=0.8), T("×", 34, INK), mchip("(speed of light)²", TEAL, size=28, h=0.8)).arrange(RIGHT, buff=0.3)
    at(parts, 2.3, 0.4)
    yield [FadeIn(parts, shift=LEFT * 0.2)]
    big = at(code(EMC, 64, TEAL), 2.3, -1.4)
    yield [GrowArrow(Arrow(P(2.3, -0.2), P(2.3, -0.85), buff=0, color=MUTED, stroke_width=4, tip_length=0.16)), FadeIn(big, scale=1.2)]


def plant(c):
    x, y = c
    return VGroup(Rectangle(width=2.0, height=1.0, stroke_color=MUTED, stroke_width=3, fill_color=PALE, fill_opacity=1).move_to(P(x, y)),
                  Rectangle(width=0.32, height=1.0, stroke_color=MUTED, stroke_width=3, fill_color=PALE, fill_opacity=1).move_to(P(x + 0.55, y + 0.95)),
                  Rectangle(width=0.32, height=0.7, stroke_color=MUTED, stroke_width=3, fill_color=PALE, fill_opacity=1).move_to(P(x - 0.1, y + 0.8)))


@slide("The speed of light squared is huge", "One gram")
def em3(s):
    yield [FadeIn(at(words("the speed of light squared is huge, so a little mass is a lot of energy", 46, 26, INK, align=ORIGIN), 0, 2.2))]
    g = VGroup(block(-5.4, 0.3, 0.6, 0.5), at(lab("1 gram", 26, INK, True), -5.4, -0.4))
    num = at(sci("about 9 × 10", "13", "joules", 36, TEAL, True), -0.6, 0.3)
    yield [FadeIn(g), GrowArrow(Arrow(P(-4.7, 0.3), P(-3.5, 0.3), buff=0, color=MUTED, stroke_width=4, tip_length=0.18)), FadeIn(num)]
    day = ValueTracker(0.01)
    s.add(day)
    arc = always_redraw(lambda: Arc(radius=0.55, start_angle=PI / 2, angle=-TAU * day.get_value(), color=INK, stroke_width=8).move_arc_center_to(P(5.8, 1.1)))
    yield [FadeIn(plant((4.4, -0.4))), FadeIn(Circle(radius=0.55, color=LINE, stroke_width=3).move_to(P(5.8, 1.1))), FadeIn(arc),
           day.animate.set_value(0.999), FadeIn(at(words("roughly a large power station's output in a whole day", 26, 24, INK, align=ORIGIN), 4.6, -1.7))]


@slide("Energy and momentum behave like time", "Energy and momentum")
def em4(s):
    pairs = VGroup(*[VGroup(chip(a, INK, size=26, h=0.7), T("is like", 24, MUTED), chip(b, INK, size=26, h=0.7)).arrange(RIGHT, buff=0.3)
                     for a, b in (("energy", "time"), ("momentum", "distance"))]).arrange(DOWN, buff=0.4)
    at(pairs, -3.5, 1.5)
    yield [FadeIn(pairs)]
    rows = VGroup()
    for k, (name, color, e, p) in enumerate((("one observer", BLUE, 3.0, 2.0), ("another", PURPLE, 3.6, 2.82))):
        y = -0.6 - 1.2 * k
        rows.add(VGroup(right_at(lab(name, 24, color, True), -5.0, y),
                        right_at(code("E", 22, color), -4.45, y + 0.2), right_at(code("pc", 22, color), -4.45, y - 0.2),
                        Rectangle(width=e, height=0.28, stroke_width=0, fill_color=color, fill_opacity=0.75).move_to(P(-4.3 + e / 2, y + 0.2)),
                        Rectangle(width=p, height=0.28, stroke_width=0, fill_color=color, fill_opacity=0.4).move_to(P(-4.3 + p / 2, y - 0.2))))
    yield [FadeIn(rows), FadeIn(at(lab("energy and momentum: they disagree", 22, INK), -2.3, -2.75))]
    comb = VGroup(*[Rectangle(width=1.8, height=0.42, stroke_width=0, fill_color=TEAL, fill_opacity=0.8).move_to(P(4.4, -0.6 - 1.2 * k)) for k in range(2)])
    yield [LaggedStart(*[GrowFromEdge(c, LEFT) for c in comb], lag_ratio=0.3), FadeIn(at(code("E² − (pc)²", 26, TEAL), 4.4, 0.1)),
           FadeIn(at(words("but they agree on one combination, built just like the interval", 22, 24, TEAL, align=ORIGIN), 4.4, 1.4))]


EP = "E² − (pc)² = (mc²)²"


@slide("Take the energy squared", "Built like the interval")
def em5(s):
    cols = (-2.6, -0.8, 1.0, 2.8, 4.8)
    top = VGroup(*[at(code(t, 36, MUTED), x, 1.6) for t, x in zip(("(c Δt)²", "−", "Δx²", "=", "s²"), cols)])
    bot = VGroup(*[at(code(t, 40, TEAL), x, -0.1) for t, x in zip(("E²", "−", "(pc)²", "=", "(mc²)²"), cols)])
    yield [FadeIn(top), FadeIn(right_at(lab("the interval", 22, MUTED), -3.9, 1.6))]
    yield [FadeIn(bot, shift=UP * 0.15), FadeIn(right_at(lab("energy and momentum", 22, TEAL), -3.9, -0.1)),
           *[GrowArrow(Arrow(P(x, 1.15), P(x, 0.4), buff=0, color=LINE, stroke_width=3, tip_length=0.14)) for x in (cols[0], cols[2], cols[4])]]
    br = Brace(bot[4], DOWN, color=TEAL)
    yield [FadeIn(br), FadeIn(lab("always the rest energy, squared", 26, TEAL, True).next_to(br, DOWN, buff=0.15))]


@slide("At rest, the momentum is zero", "At rest and moving")
def em6(s):
    rows = (("at rest:", "p = 0,  so  E = mc²", TEAL), ("moving:", "E = γ mc²", INK), ("everyday speeds:", "E ≈ mc² + ½mv²", INK))
    for k, (name, e, color) in enumerate(rows):
        y = 1.6 - 1.4 * k
        g = VGroup(right_at(lab(name, 26, INK, True), -1.6, y), left_at(code(e, 32, color), -1.2, y))
        if k == 2:
            g.add(left_at(lab("the rest energy plus the familiar kinetic energy", 22, INK), -1.2, y - 0.6))
        yield [FadeIn(g, shift=RIGHT * 0.15)]


@slide("Near the speed of light, gamma shoots up.", "Why nothing with mass reaches light's speed")
def em7(s):
    v = ValueTracker(0.0)
    s.add(v)
    yield [FadeIn(gamma_axes("energy", "speed, as a fraction of light's", one=False)), Create(gamma_curve()), FadeIn(at(lab("light's speed", 22, TEAL), gx(1.0) + 1.0, 2.2)),
           FadeIn(always_redraw(lambda: g_point(v.get_value(), gamma_of(v.get_value())))), v.animate.set_value(0.99),
           FadeIn(right_at(lab("mc²", 22, INK), GO[0] - 0.12, gy(1) + 0.32))]
    yield [FadeIn(left_at(words("the energy grows without limit", 20, 28, INK), 2.2, 1.0))]
    yield [FadeIn(left_at(words("so nothing with mass can ever reach the speed of light", 22, 26, INK, ), 2.2, -0.6))]


@slide("Light has no mass.", "Light")
def em8(s):
    t = clock(s)
    s.add(light_wave(t, -6.8, -1.0, 1.5, 0.35, 2.6, 3.0))
    yield [FadeIn(at(code("m = 0", 34, INK), -3.9, 0.2)), FadeIn(at(lab("light has no mass", 24, INK), -3.9, -0.5))]
    yield [FadeIn(at(code("E = pc", 60, ORANGE), 3.4, 1.0)), FadeIn(at(lab("energy = momentum × light's speed", 24, INK), 3.4, 0.0))]
    yield [FadeIn(at(lab("that fits chapter 2", 26, INK, True), 3.4, -1.4))]


def packet(c, t=None):
    us = np.linspace(-2.2, 2.2, 160)
    return VMobject(color=ORANGE, stroke_width=4).set_points_smoothly([P(c[0] + u, c[1] + 0.7 * np.exp(-0.6 * u * u) * np.sin(2 * PI * u / 0.9)) for u in us])


@slide("A packet of light has an energy", "Chapter 2's packets of light")
def em9(s):
    c = (-3.6, 0.8)
    pk = packet(c)
    lam = BraceBetweenPoints(P(c[0] - 0.225, c[1] + 0.85), P(c[0] + 0.675, c[1] + 0.85), direction=UP, color=INK)
    yield [Create(pk), FadeIn(lam), FadeIn(lab("wavelength λ", 22, INK).next_to(lam, UP, buff=0.08)),
           FadeIn(at(code("E = hf", 40, ORANGE), 3.2, 1.3)), FadeIn(at(lab("Planck's constant × frequency", 22, INK), 3.2, 0.6))]
    yield [FadeIn(at(code("p = h/λ", 40, ORANGE), 3.2, -0.6)), FadeIn(at(lab("Planck's constant ÷ wavelength", 22, INK), 3.2, -1.3))]


@slide("And frequency times wavelength", "E = pc")
def em10(s):
    s.add(at(code("E = hf", 34, ORANGE), -4.4, 1.6), at(code("p = h/λ", 34, ORANGE), -4.4, 0.7))
    yield [FadeIn(at(code("f λ = c", 40, INK), 2.6, 1.6)), FadeIn(at(lab("frequency × wavelength = light's speed", 22, INK), 2.6, 0.9))]
    chain = at(code("E = hf = (h/λ) × c = pc", 40, ORANGE), 0, -1.0)
    yield [FadeIn(chain, shift=UP * 0.15), FadeIn(tick(chain))]


# ================================================================== the Schrödinger equation fails the test
deck.part("The Schrödinger equation fails the test")

TEST_Y = 0.5


def test_machine():
    box = at(card("switch to a moving\nobserver", 3.8, 1.5, INK, 26), 0, TEST_Y)
    return box


def rule_card(y=1.6):
    return at(card("the laws of physics look the same to every\nobserver moving at a steady speed", 11.0, 1.4, TEAL, 28), 0, y)


@slide("The Schrodinger equation fails the test.", "Einstein's rule as a test")
def tst1(s):
    t = clock(s)
    yield [FadeIn(rule_card()), FadeIn(at(lab("the rule Einstein added", 24, MUTED), 0, 2.55))]
    yield [FadeIn(person(-3.0, -2.6, BLUE, 1.2)),
           FadeIn(always_redraw(lambda: person(0.5 + min(0.8 * t.get_value(), 4.0), -2.6, PURPLE, 1.2))),
           FadeIn(at(lab("the same laws for both", 26, INK), -3.0, -0.6))]


@slide("That's a test you can put any equation through.", "The test")
def tst2(s):
    a = at(card("any equation", 3.4, 1.3, INK, 28), -5.3, TEST_Y)
    m = test_machine()
    out = at(card("does it keep\nits form?", 3.0, 1.3, MUTED, 26), 5.3, TEST_Y)
    yield [FadeIn(a), FadeIn(at(lab("a test for any equation", 26, INK, True), 0, 2.3))]
    yield [GrowArrow(arrow(a, m)), FadeIn(m), GrowArrow(arrow(m, out)), FadeIn(out)]


@slide("Maxwell's equations pass.", "Maxwell's equations pass")
def tst3(s):
    t = clock(s)
    a = at(card("Maxwell's\nequations", 3.4, 1.3, INK, 28), -5.3, TEST_Y)
    m = test_machine()
    out = at(card("same form", 3.0, 1.1, TEAL, 28), 5.3, TEST_Y)
    yield [FadeIn(a), GrowArrow(arrow(a, m)), FadeIn(m), GrowArrow(arrow(m, out)), FadeIn(out), FadeIn(check().next_to(out, DOWN, buff=0.25))]
    yield [FadeIn(at(lab("they were the starting point, after all", 24, INK), 0, -1.0))]
    yield [FadeIn(light_wave(t, -6.0, 6.0, -2.2, 0.3, 2.6, 3.0)), FadeIn(at(lab("light waves at light's speed, for everyone", 24, TEAL, True), 0, -3.0))]


SCHR = "iħ ∂ψ/∂t = −(ħ²/2m) ∇²ψ"


@slide("The Schrodinger equation from chapter two fails.", "The Schrödinger equation fails")
def tst4(s):
    a = at(card("Schrödinger\nequation", 3.4, 1.3, INK, 28), -5.3, TEST_Y)
    m = test_machine()
    out = at(card("changes form", 3.0, 1.1, RED, 28), 5.3, TEST_Y)
    yield [FadeIn(a), GrowArrow(arrow(a, m)), FadeIn(m), GrowArrow(arrow(m, out)), FadeIn(out), Create(cross(Square(0.5).next_to(out, DOWN, buff=0.25), RED, 6))]
    yield [FadeIn(at(code(SCHR, 40, INK), 0, -1.6)), FadeIn(at(lab("its shape, for a free particle", 24, MUTED), 0, -2.45))]


def schr_parts(y=0.9, size=46):
    parts = VGroup(code("iħ", size), code("∂ψ/∂t", size), code("=", size), code("−(ħ²/2m)", size), code("∇²ψ", size)).arrange(RIGHT, buff=0.4)
    return at(parts, 0, y)


@slide("In time, it takes one derivative.", "Lopsided")
def tst5(s):
    eqn = schr_parts()
    s.add(eqn)
    b1 = SurroundingRectangle(eqn[1], color=INK, buff=0.12)
    b2 = SurroundingRectangle(eqn[4], color=INK, buff=0.12)
    yield [Create(b1), FadeIn(lab("one derivative in time", 24, INK, True).next_to(b1, UP, buff=0.2))]
    yield [Create(b2), FadeIn(lab("two in space, in a row", 24, INK, True).next_to(b2, UP, buff=0.2))]
    ang = ValueTracker(0.0)
    s.add(ang)

    def beam():
        a = ang.get_value()
        c = P(0, -1.7)
        u = np.array([np.cos(a), np.sin(a), 0])
        g = VGroup(Line(c - 2.6 * u, c + 2.6 * u, color=INK, stroke_width=6),
                   at(card("time: 1", 1.6, 0.6, INK, 24), *(c - 2.3 * u + P(0, 0.42))[:2]),
                   at(card("space: 2", 1.6, 0.6, INK, 24), *(c + 2.3 * u + P(0, 0.42))[:2]))
        return g
    pivot = Triangle(color=MUTED, fill_color=MUTED, fill_opacity=1).scale(0.25).move_to(P(0, -1.95))
    yield [FadeIn(pivot), FadeIn(always_redraw(beam)), ang.animate.set_value(-0.22), FadeIn(left_at(lab("lopsided", 28, RED, True), 3.4, -2.2))]


MAPC = (-3.4, -0.3)


def map_frame(a, c=MAPC, r=2.0):
    """A map turned by angle a: its border and its north-south and east-west lines."""
    g = VGroup()
    sq = Square(2 * r, color=LINE, stroke_width=3).rotate(a).move_to(P(*c))
    u = np.array([np.cos(a), np.sin(a), 0])
    n = np.array([-np.sin(a), np.cos(a), 0])
    o = P(*c)
    g.add(sq, Arrow(o - u * r, o + u * r, buff=0, color=INK, stroke_width=4, tip_length=0.18),
          Arrow(o - n * r, o + n * r, buff=0, color=INK, stroke_width=4, tip_length=0.18),
          at(T("E", 24, INK, True), *(o + u * (r + 0.3))[:2]), at(T("N", 24, INK, True), *(o + n * (r + 0.3))[:2]))
    return g


@slide("Changing observer mixes time and space.", "Like turning a map")
def map1(s):
    a = ValueTracker(0.0)
    s.add(a)
    pt = P(MAPC[0] + 1.3, MAPC[1] + 0.9)

    def proj():
        an = a.get_value()
        o = P(*MAPC)
        u = np.array([np.cos(an), np.sin(an), 0])
        n = np.array([-np.sin(an), np.cos(an), 0])
        d = pt - o
        fe, fn = np.dot(d, u), np.dot(d, n)
        g = VGroup(DashedLine(pt, o + u * fe, color=MUTED, stroke_width=3), DashedLine(pt, o + n * fn, color=MUTED, stroke_width=3))
        bars = VGroup(Rectangle(width=max(abs(fe) * 1.6, 0.02), height=0.35, stroke_width=0, fill_color=INK, fill_opacity=0.6),
                      Rectangle(width=max(abs(fn) * 1.6, 0.02), height=0.35, stroke_width=0, fill_color=INK, fill_opacity=0.6))
        left_at(bars[0], 3.0, 0.4)
        left_at(bars[1], 3.0, -0.6)
        return VGroup(g, bars)
    yield [FadeIn(always_redraw(lambda: map_frame(a.get_value()))), FadeIn(Dot(pt, radius=0.12, color=INK)), FadeIn(always_redraw(proj)),
           FadeIn(right_at(lab("east–west", 24, INK), 2.8, 0.4)), FadeIn(right_at(lab("north–south", 24, INK), 2.8, -0.6)),
           FadeIn(at(lab("one place, read off the map", 24, INK), 3.9, 1.3))]
    yield [a.animate.set_value(0.6), FadeIn(at(words("turning the map mixes north–south with east–west", 26, 26, INK, align=ORIGIN), 3.9, -1.9))]


@slide("Picture a rule that treats north-south", "A lopsided rule")
def map2(s):
    a = ValueTracker(0.0)
    s.add(a)

    def shapes():
        an = a.get_value()
        el = Ellipse(width=1.6, height=3.2, color=RED, stroke_width=5).rotate(an).move_to(P(*MAPC))
        ci = Circle(radius=1.2, color=TEAL, stroke_width=5).move_to(P(*MAPC))
        return VGroup(el, ci)
    s.add(always_redraw(lambda: map_frame(a.get_value())))
    yield [FadeIn(always_redraw(shapes)), FadeIn(left_at(words("a rule that treats north–south differently from east–west", 28, 24, RED), 1.2, 1.7)),
           FadeIn(left_at(words("a rule that treats both alike", 28, 24, TEAL), 1.2, 0.5))]
    yield [a.animate.set_value(0.7), FadeIn(left_at(words("turn the map: the lopsided rule changes, the even one doesn't", 28, 24, INK), 1.2, -0.8))]
    yield [FadeIn(left_at(words("an equation that treats time differently from space changes when you change observer", 30, 24, INK), 1.2, -2.3))]


@slide("The lopsidedness comes from where", "Chapter 2's trick")
def trick1(s):
    yield [FadeIn(at(card("chapter 2: an energy rule  →  an equation", 9.0, 1.1, INK, 28), 0, 1.6))]
    r1 = VGroup(right_at(lab("energy", 28, INK, True), -1.4, 0.0), at(T("→", 32, MUTED), -0.8, 0.0), left_at(code("iħ ∂/∂t", 34, INK), -0.3, 0.0),
                left_at(lab("a time derivative", 24, MUTED), 2.6, 0.0))
    r2 = VGroup(right_at(lab("momentum", 28, INK, True), -1.4, -1.3), at(T("→", 32, MUTED), -0.8, -1.3), left_at(code("−iħ∇", 34, INK), -0.3, -1.3),
                left_at(lab("a space derivative", 24, MUTED), 2.6, -1.3))
    yield [FadeIn(r1, shift=RIGHT * 0.15)]
    yield [FadeIn(r2, shift=RIGHT * 0.15)]


@slide("Chapter two used it on the low-speed energy", "From the low-speed energy")
def trick2(s):
    e = VGroup(at(code("E", 54), -1.6, 1.4), at(code("=", 54), -0.6, 1.4), left_at(code("p²/2m", 54), 0.1, 1.4))
    yield [FadeIn(e), FadeIn(at(lab("the low-speed energy: momentum squared over twice the mass", 24, MUTED), 0, 2.45))]
    b1 = Brace(e[0], DOWN, color=INK)
    b2 = Brace(e[2][:2], DOWN, color=INK)
    yield [FadeIn(b1), FadeIn(right_at(lab("one power of energy", 24, INK, True), b1.get_center()[0] + 0.4, b1.get_bottom()[1] - 0.25)),
           FadeIn(b2), FadeIn(left_at(lab("two of momentum", 24, INK, True), b2.get_center()[0] - 0.4, b2.get_bottom()[1] - 0.25))]
    yield [GrowArrow(Arrow(P(0, -0.15), P(0, -1.0), buff=0, color=MUTED, stroke_width=4, tip_length=0.18)),
           FadeIn(at(code(SCHR, 36, INK), 0, -1.55)), FadeIn(at(lab("one derivative in time, two in space", 24, INK), 0, -2.35))]


@slide("That's fine at low speeds", "Fast particles")
def kg1(s):
    a = at(VGroup(lab("at low speeds, as in chapters 2 and 3", 26, INK), check()).arrange(RIGHT, buff=0.25), 0, 1.6)
    yield [FadeIn(a)]
    yield [FadeIn(at(lab("fast particles need an equation built from", 26, INK), 0, 0.2)),
           FadeIn(at(code(EP, 44, TEAL), 0, -0.9))]


@slide("Energy squared, minus momentum", "Two powers of each")
def kg2(s):
    e = VGroup(*[at(code(t, 48, TEAL), x, 1.4) for t, x in zip(("E²", "−", "(pc)²", "=", "(mc²)²"), (-4.3, -2.6, -0.6, 1.3, 3.2))])
    s.add(e)
    b1 = Brace(e[0], DOWN, color=INK)
    b2 = Brace(e[2], DOWN, color=INK)
    yield [FadeIn(b1), FadeIn(at(lab("two powers of energy", 24, INK, True), b1.get_center()[0], b1.get_bottom()[1] - 0.25))]
    yield [FadeIn(b2), FadeIn(at(lab("two of momentum", 24, INK, True), b2.get_center()[0], b2.get_bottom()[1] - 0.25))]
    beam = VGroup(Line(P(-2.6, -1.6), P(2.6, -1.6), color=TEAL, stroke_width=6),
                  at(card("time: 2", 1.6, 0.6, TEAL, 24), -2.3, -1.18), at(card("space: 2", 1.6, 0.6, TEAL, 24), 2.3, -1.18),
                  Triangle(color=MUTED, fill_color=MUTED, fill_opacity=1).scale(0.25).move_to(P(0, -1.85)))
    yield [FadeIn(beam), FadeIn(at(lab("balanced, just like the interval", 26, TEAL, True), 0, -2.6))]


@slide("Run the same trick on that rule", "The Klein–Gordon equation")
def kg3(s):
    a = at(code(EP, 34, TEAL), -3.6, 1.0)
    b = at(card("the Klein–Gordon\nequation", 4.2, 1.6, TEAL, 30), 4.0, 1.0)
    yield [FadeIn(a), GrowArrow(Arrow(P(-0.3, 1.0), P(1.7, 1.0), buff=0, color=MUTED, stroke_width=4, tip_length=0.2)),
           FadeIn(at(lab("chapter 2's trick", 22, MUTED), 0.7, 1.45)), FadeIn(b)]
    yield [FadeIn(at(card("next chapter", 3.4, 1.0, INK, 28), 4.0, -1.4)),
           GrowArrow(Arrow(P(4.0, 0.15), P(4.0, -0.85), buff=0, color=MUTED, stroke_width=4, tip_length=0.18))]


# ================================================================== notation for later chapters
deck.part("Notation for later chapters")

NX = (-3.6, -1.8, 0.0, 1.8)


def four_row(y, items, color=INK):
    g = VGroup()
    for x, it in zip(NX, items):
        box = Square(1.3, color=color, stroke_width=3, fill_color=color, fill_opacity=0.06).move_to(P(x, y))
        g.add(VGroup(box, it.move_to(P(x, y))))
    return g


def x_row():
    return four_row(1.3, [code("ct", 34), code("x", 34), code("y", 34), code("z", 34)])


def p_row():
    return four_row(-0.6, [code("E/c", 30), subbed("p", "x", 34), subbed("p", "y", 34), subbed("p", "z", 34)])


@slide("Notation for later chapters.", "Four-vectors")
def nt1(s):
    yield [FadeIn(at(lab("a compact notation for later chapters", 26, MUTED), 0, 2.45))]
    row = x_row()
    yield [LaggedStart(*[FadeIn(b, shift=DOWN * 0.15) for b in row], lag_ratio=0.15),
           FadeIn(left_at(words("time and space in one object with four parts: a four-vector", 20, 24, INK), 3.0, 1.3))]


@slide("Energy and momentum make a four-vector too.", "Four-vectors")
def nt2(s):
    s.add(at(lab("a compact notation for later chapters", 26, MUTED), 0, 2.45), x_row(),
          left_at(words("time and space in one object with four parts: a four-vector", 20, 24, INK), 3.0, 1.3))
    row = p_row()
    yield [LaggedStart(*[FadeIn(b, shift=DOWN * 0.15) for b in row], lag_ratio=0.15),
           FadeIn(left_at(words("energy and momentum: a four-vector too", 20, 24, INK), 3.0, -0.6))]
    yield [FadeIn(left_at(code("(ct)² − x² − y² − z²", 28, TEAL), -4.3, -2.0)), FadeIn(left_at(code("(E/c)² − p²", 28, TEAL), 2.0, -2.0)),
           FadeIn(at(lab("both built the same way", 24, TEAL, True), 0, -2.75))]


@slide("The time part comes with a plus", "Plus and minus")
def nt3(s):
    s.add(x_row(), p_row())
    signs = VGroup(*[at(T(sg, 48, INK if sg == "+" else MUTED, True), x, 2.3) for sg, x in zip(("+", "−", "−", "−"), NX)])
    yield [LaggedStart(*[FadeIn(sg, shift=DOWN * 0.15) for sg in signs], lag_ratio=0.15),
           FadeIn(left_at(words("time part: plus; space parts: minus", 20, 24, INK), 3.0, 2.0))]
    yield [FadeIn(at(pill("the notation does that bookkeeping for you", TEAL, 28), 0, -2.3), shift=UP * 0.15)]


QC = (-3.4, 0.2)


def e_field(c=QC, color=BLUE, r0=0.35, r1=2.0):
    o = P(*c)
    g = VGroup()
    for k in range(10):
        a = k * TAU / 10 + 0.15
        u = np.array([np.cos(a), np.sin(a), 0])
        g.add(Arrow(o + r0 * u, o + r1 * u, buff=0, color=color, stroke_width=3, tip_length=0.14))
    return g


def charge(c=QC):
    return VGroup(Circle(radius=0.28, color=INK, stroke_width=3, fill_color=PALE, fill_opacity=1).move_to(P(*c)), at(T("+", 30, INK, True), *c))


@slide("Changing observer also ties electricity", "A charge, seen moving")
def fld1(s):
    t = clock(s)
    yield [FadeIn(charge(), scale=1.4), FadeIn(right_at(lab("a charge", 24, INK), QC[0] - 2.2, QC[1]))]
    yield [LaggedStart(*[GrowArrow(a) for a in e_field()], lag_ratio=0.05),
           FadeIn(at(lab("a charge sitting still: only an electric field", 24, BLUE, True), QC[0], 2.55))]
    yield [FadeIn(always_redraw(lambda: person(1.6 + min(0.5 * t.get_value(), 3.0), -2.6, PURPLE, 1.1))),
           FadeIn(left_at(lab("someone moving past", 24, PURPLE, True), 1.4, 0.6)),
           GrowArrow(Arrow(P(QC[0] + 0.3, -2.3), P(QC[0] - 1.5, -2.3), buff=0, color=PURPLE, stroke_width=5, tip_length=0.2)),
           FadeIn(left_at(words("to them, the charge is moving", 30, 24, PURPLE), 1.4, -0.1))]


def b_loops(c=QC):
    o = P(*c)
    return VGroup(*[Ellipse(width=w, height=h, color=PURPLE, stroke_width=4).move_to(o) for w, h in ((0.7, 1.6), (1.1, 2.8), (1.5, 4.0))])


@slide("A moving charge is a current", "A magnetic field appears")
def fld2(s):
    s.add(e_field(), charge())
    yield [GrowArrow(Arrow(P(QC[0] + 0.3, -2.3), P(QC[0] - 1.5, -2.3), buff=0, color=PURPLE, stroke_width=5, tip_length=0.2)),
           FadeIn(left_at(lab("a moving charge is a current", 26, INK), 1.0, 1.3))]
    yield [LaggedStart(*[Create(e) for e in b_loops()], lag_ratio=0.25),
           FadeIn(left_at(words("currents make magnetic fields, so that observer sees one too", 26, 24, PURPLE), 1.0, 0.0))]


@slide("Electric and magnetic fields are two parts", "One object")
def fld3(s):
    rows = (("one observer", 1.0, BLUE), ("another", 0.55, PURPLE))
    g = VGroup()
    for k, (name, f, color) in enumerate(rows):
        y = 1.2 - 1.1 * k
        e = Rectangle(width=5.0 * f, height=0.5, stroke_width=0, fill_color=BLUE, fill_opacity=0.7).move_to(P(-2.2 + 2.5 * f, y))
        b = Rectangle(width=max(5.0 * (1 - f), 0.01), height=0.5, stroke_width=0, fill_color=PURPLE, fill_opacity=0.7).move_to(P(-2.2 + 5.0 * f + 2.5 * (1 - f), y))
        g.add(VGroup(right_at(lab(name, 24, color, True), -2.5, y), e, b, Rectangle(width=5.0, height=0.5, color=INK, stroke_width=2).move_to(P(0.3, y))))
    legend = VGroup(Square(0.3, stroke_width=0, fill_color=BLUE, fill_opacity=0.7), lab("electric", 22, BLUE, True),
                    Square(0.3, stroke_width=0, fill_color=PURPLE, fill_opacity=0.7), lab("magnetic", 22, PURPLE, True)).arrange(RIGHT, buff=0.15)
    legend[2].shift(RIGHT * 0.35)
    legend[3].shift(RIGHT * 0.35)
    at(legend, 0.3, 2.0)
    yield [FadeIn(legend), FadeIn(g[0]), FadeIn(at(lab("one object, split differently by different observers", 24, INK), 0, 2.5))]
    yield [FadeIn(g[1])]
    four = VGroup(*[card("", 1.0, 0.7, INK) for _ in range(4)]).arrange(RIGHT, buff=0.2)
    at(four, -3.6, -1.7)
    two = VGroup(*[card("", 1.4, 0.7, TEAL) for _ in range(2)]).arrange(RIGHT, buff=0.25)
    at(two, 3.2, -1.7)
    yield [FadeIn(four), FadeIn(at(lab("Maxwell's 4 equations", 22, INK), -3.6, -2.4)),
           GrowArrow(Arrow(P(-0.9, -1.7), P(1.1, -1.7), buff=0, color=MUTED, stroke_width=4, tip_length=0.18)),
           FadeIn(two), FadeIn(at(lab("2 short ones", 22, TEAL, True), 3.2, -2.4))]


# ================================================================== where this leads
deck.part("Where this leads")

RX = (-4.8, 0.0, 4.8)
RY = (1.0, -1.6)


def recap_card(k):
    x, y = RX[k % 3], RY[k // 3]
    texts = (("light's speed is the\nsame for everyone", TEAL), ("moving clocks\nrun slow", BLUE), ("moving lengths\nshrink", BLUE),
             ("everyone agrees\non the interval", TEAL), ("mass is energy:\nE = mc²", TEAL), ("the Schrödinger equation:\nlow speeds only", RED))
    text, color = texts[k]
    c = at(card(None, 4.4, 2.2, color), x, y)
    words_ = VGroup(*[lab(t, 24, INK, False) for t in text.split("\n")]).arrange(DOWN, buff=0.08)
    at(words_, x, y - 0.55)
    if k == 0:
        icon = VGroup(Arrow(P(x - 0.9, y + 0.45), P(x + 0.9, y + 0.45), buff=0, color=ORANGE, stroke_width=5, tip_length=0.18))
    elif k == 1:
        icon = dial((x, y + 0.45), 0.36)
    elif k == 2:
        icon = ruler(x, y + 0.45, 1.3, 0.36, INK, 6)
    elif k == 3:
        icon = code("s²", 32, TEAL).move_to(P(x, y + 0.45))
    elif k == 4:
        icon = block(x, y + 0.45, 0.5, 0.5)
    else:
        icon = code("ψ", 32, RED).move_to(P(x, y + 0.45))
    return VGroup(c, icon, words_)


@slide("Where this leads.", "Where we've got to")
def rec1(s):
    yield [FadeIn(recap_card(0), shift=UP * 0.15)]


@slide("So moving clocks run slow, and moving lengths", "Where we've got to")
def rec2(s):
    s.add(recap_card(0))
    yield [FadeIn(recap_card(1), shift=UP * 0.15), FadeIn(recap_card(2), shift=UP * 0.15)]
    yield [FadeIn(recap_card(3), shift=UP * 0.15)]


@slide("Mass is energy.", "Where we've got to")
def rec3(s):
    s.add(*[recap_card(k) for k in range(4)])
    yield [FadeIn(recap_card(4), shift=UP * 0.15)]
    yield [FadeIn(recap_card(5), shift=UP * 0.15)]


@slide("The next chapter is relativistic", "Next: relativistic quantum mechanics")
def rec4(s):
    a = at(card("the Klein–Gordon\nequation", 4.4, 1.6, TEAL, 30), -3.4, 0.4)
    yield [FadeIn(at(T("next chapter: Relativistic Quantum Mechanics", 32, INK, True), 0, 2.2)), FadeIn(a)]
    b = at(card("what goes\nwrong with it", 4.4, 1.6, RED, 30), 3.4, 0.4)
    yield [GrowArrow(arrow(a, b)), FadeIn(b)]

"""Slides for chapter three, The Harmonic Oscillator.

Every value comes from video/scripts/03-harmonic-oscillator.txt or
docs/harmonic-oscillator.md. The drawings redraw the chapter's figures in
docs/manim/ (oscillator-approximation, hcl-experiments,
classical-oscillator-energy, oscillator-ladder, steps-vs-thermal,
oscillator-ground-state, coherent-state) as animations.

Colors: BLUE for states and amplitudes (the spring's arrow in the
position-momentum plane, a ball or dot standing for where the spring is, the
amplitude arrows on the rungs, the swinging average), TEAL for chances and
probability densities (bell curves, chance bars) and for checks that pass,
ORANGE for the part under discussion and for the HCl bond's vibration (its
spring, its share of heat, its ladder), PURPLE for operators (a, a-dagger, the
number operator), h-bar, and the tumbling motion with its share and its ladder,
RED only for a prediction that fails (the classical share of heat, a spring
sitting perfectly still, stepping down past zero), INK, MUTED and LINE for
springs, apparatus, energy axes, context and connectors.
"""
import re

from manim import *

from engine import *

STEM = "03-harmonic-oscillator"
deck = Deck(f"scripts/{STEM}.txt")
slide = deck.slide

SPIN = 1.4  # how fast springs and arrows turn on screen, in radians per second


# ------------------------------------------------------------------ small helpers

def at(mob, x, y):
    return mob.move_to([x, y, 0])


def left_at(mob, x, y):
    """Place a mobject with its left edge at x."""
    return mob.move_to([x + mob.width / 2, y, 0])


def lab(text, size=24, color=MUTED, bold=False):
    return T(text, size, color, bold)


def words(text, chars=40, size=26, color=INK, align=LEFT):
    return W(text, chars, size, color, align=align)


def daggers(mob, text):
    """Raise and shrink every dagger glyph, so a† reads as a superscript rather than 'at'."""
    i = -1
    for j, ch in enumerate(text):
        if ch == " ":
            continue
        i += 1
        if ch == "†" and i > 0:
            g, prev = mob[i], mob[i - 1]
            g.scale(0.65)
            g.move_to([prev.get_right()[0] + g.width / 2 + 0.03, prev.get_bottom()[1] + 0.55 * prev.height + g.height / 2, 0])
            if j + 1 < len(text) and text[j + 1] != " " and i + 1 < len(mob):
                gap = mob[i + 1].get_left()[0] - g.get_right()[0] - 0.05 * prev.height / 0.25
                if gap > 0:
                    VGroup(*mob[i + 1:]).shift(LEFT * gap)
    return mob


def heq(text, size=34, color=INK, font=MONO):
    """Monospace math in which h-bar (with a following omega) is PURPLE and daggers are raised."""
    t2c = {f"[{m.start()}:{m.end()}]": PURPLE for m in re.finditer(r"ħω|ħ", text)}
    return daggers(Text(text, font=font, color=color, font_size=size, t2c=t2c), text)


def dT(text, size=30, color=INK, bold=False):
    """Body text with raised daggers."""
    return daggers(T(text, size, color, bold), text)


def dcard(text, w, h, color, size):
    """A one-line card whose text has raised daggers."""
    c = card(text, w, h, color, size)
    daggers(c[1][0], text)
    return c


def omega_subs(mob, text, subs, color=PURPLE):
    """Hand-placed subscripts after each omega in a monospace Text (Menlo has no subscript digits)."""
    chars = text.replace(" ", "")
    idx = [i for i, ch in enumerate(chars) if ch == "ω"]
    g = VGroup(mob)
    for i, k in zip(idx, subs):
        w = mob[i]
        sb = heq(str(k), 20, color)
        sb.scale_to_fit_height(w.height * 0.85)
        sb.move_to([w.get_right()[0] + sb.width / 2 + 0.03, w.get_bottom()[1] - sb.height * 0.25, 0])
        g.add(sb)
    return g


def glyphs(mob, full, sub, nth=0):
    """The glyphs of a Text that spell `sub` (Text drops spaces from its glyphs)."""
    idx = -1
    for _ in range(nth + 1):
        idx = full.index(sub, idx + 1)
    start = len(full[:idx].replace(" ", ""))
    return VGroup(*mob[start:start + len(sub.replace(" ", ""))])


def num_pill(n, color=INK, size=22):
    return pill(str(n), color, size)


def tick(mob, color=TEAL, buff=0.2):
    return check(color).next_to(mob, RIGHT, buff=buff)


def xmark(mob, size=0.42, buff=0.2):
    return cross(Square(size).next_to(mob, RIGHT, buff=buff), RED, 6)


def clock(s, rate=1.0):
    """Time that keeps running during holds, so the things drawn from it keep moving.

    Setting `.rate` on the result changes the speed from the next step on.
    """
    t = ValueTracker(0.0)
    t.rate = rate
    t.add_updater(lambda m, dt: m.increment_value(m.rate * dt))
    s.add(t)
    return t


def tri(u):
    """A triangle wave between 0 and 1, for things bouncing between walls."""
    return abs((u % 2.0) - 1.0)


def hline(x0, x1, y, color=LINE, width=3):
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=width)


def axis_arrow(a, b, color=MUTED, width=3):
    return Arrow(np.array([a[0], a[1], 0.0]), np.array([b[0], b[1], 0.0]), buff=0, color=color,
                 stroke_width=width, tip_length=0.16, max_tip_length_to_length_ratio=0.2)


def area(f, u0, u1, X, Y, sx, sy, color=TEAL, opacity=0.22, width=4, n=140):
    """A filled curve y = Y + sy f(u) over x = X + sx u, such as a probability density."""
    us = np.linspace(u0, u1, n)
    pts = [np.array([X + sx * u, Y + sy * f(u), 0.0]) for u in us]
    fill = Polygon(np.array([X + sx * u0, Y, 0.0]), *pts, np.array([X + sx * u1, Y, 0.0]),
                   stroke_width=0, fill_color=color, fill_opacity=opacity)
    line = VMobject(color=color, stroke_width=width).set_points_as_corners(pts)
    return VGroup(fill, line)


def curve(f, u0, u1, X, Y, sx, sy, color=INK, width=4, n=120):
    us = np.linspace(u0, u1, n)
    return VMobject(color=color, stroke_width=width).set_points_as_corners(
        [np.array([X + sx * u, Y + sy * f(u), 0.0]) for u in us])


def bell(c=0.0, w=1.0):
    return lambda u: np.exp(-((u - c) / w) ** 2)


def phasor(c, ang, r=0.8, color=BLUE, ring=True, width=5, frac=1.0):
    """A complex amplitude drawn as an arrow in a circle; frac is its size, 1 at the rim."""
    c = np.array([c[0], c[1], 0.0])
    g = VGroup()
    if ring:
        g.add(Circle(radius=r, color=LINE, stroke_width=2).move_to(c))
    g.add(Arrow(c, c + frac * r * np.array([np.cos(ang), np.sin(ang), 0]), buff=0, color=color, stroke_width=width,
                tip_length=0.16, max_tip_length_to_length_ratio=0.35, max_stroke_width_to_length_ratio=30))
    return g


def legend_item(text, color, x, y, dashed=False, width=4):
    ln = (DashedLine if dashed else Line)([x, y, 0], [x + 0.55, y, 0], color=color, stroke_width=width)
    return VGroup(ln, T(text, 22, color).next_to(ln, RIGHT, buff=0.15))


# ------------------------------------------------------------------ springs, molecules, pendulums

def coil(p, q, n=10, amp=0.16, color=INK, width=3):
    """A zigzag spring between two points."""
    p = np.array([p[0], p[1], 0.0])
    q = np.array([q[0], q[1], 0.0])
    d = q - p
    L = max(np.linalg.norm(d), 1e-3)
    u = d / L
    nrm = np.array([-u[1], u[0], 0.0])
    lead = min(0.2, L * 0.15)
    pts = [p, p + u * lead]
    for i in range(1, n):
        pts.append(p + u * (lead + (L - 2 * lead) * i / n) + nrm * (amp if i % 2 else -amp))
    pts += [q - u * lead, q]
    return VMobject(color=color, stroke_width=width).set_points_as_corners(pts)


def wall(x, y, h=1.3):
    g = VGroup(Line([x, y - h / 2, 0], [x, y + h / 2, 0], color=MUTED, stroke_width=5))
    for k in range(6):
        yy = y - h / 2 + 0.12 + k * (h - 0.24) / 5
        g.add(Line([x, yy, 0], [x - 0.2, yy - 0.2, 0], color=MUTED, stroke_width=2))
    return g


def rig_static(xw, y, length, size=0.8):
    """The wall and the floor of a mass-on-a-spring."""
    return VGroup(wall(xw, y, size + 0.5), hline(xw, xw + length, y - size / 2, LINE, 3))


def rig_moving(xw, y, rest, disp, size=0.8, spring=INK, width=3):
    """The spring and the block, with the block's centre at rest + disp from the wall."""
    bx = xw + rest + disp
    blk = Square(size, stroke_color=INK, stroke_width=2.5, fill_color=PALE, fill_opacity=1).move_to([bx, y, 0])
    return VGroup(coil([xw, y], [bx - size / 2, y], n=12, amp=0.16 * size / 0.8 + 0.03, color=spring, width=width), blk)


def hcl(c, d=1.6, k=1.0, spring=ORANGE, width=3, angle=0.0, n=8):
    """A chlorine atom (large) and a hydrogen atom (small) joined by a spring."""
    c = np.array([c[0], c[1], 0.0])
    u = np.array([np.cos(angle), np.sin(angle), 0.0])
    rc, rh = 0.5 * k, 0.28 * k
    a, b = c - u * d / 2, c + u * d / 2
    sp = coil(a + u * rc, b - u * rh, n=n, amp=0.1 * k + 0.03, color=spring, width=width)
    cl = Circle(radius=rc, color=INK, stroke_width=2, fill_color=PALE, fill_opacity=1).move_to(a)
    h = Circle(radius=rh, color=INK, stroke_width=2, fill_color=PALE, fill_opacity=1).move_to(b)
    return VGroup(sp, cl, h)


def gas(c, w, h, t, n=8, seed=3, k=0.3, spring=INK):
    """Small molecules flying around a box and tumbling as they go."""
    rng = np.random.default_rng(seed)
    out = VGroup()
    m = 0.35
    for _ in range(n):
        px, py = rng.uniform(0, 2), rng.uniform(0, 2)
        vx, vy = rng.uniform(0.12, 0.25) * rng.choice([-1, 1]), rng.uniform(0.12, 0.25) * rng.choice([-1, 1])
        a0, om = rng.uniform(0, TAU), rng.uniform(0.8, 1.6) * rng.choice([-1, 1])
        x = c[0] - w / 2 + m + (w - 2 * m) * tri(px + vx * t)
        y = c[1] - h / 2 + m + (h - 2 * m) * tri(py + vy * t)
        out.add(hcl([x, y], 0.55, k, spring=spring, width=2, angle=a0 + om * t, n=4))
    return out


def gas_box(c, w, h):
    return at(RoundedRectangle(width=w, height=h, corner_radius=0.12, color=MUTED, stroke_width=3), c[0], c[1])


def pendulum(pivot, L, ang, r=0.22):
    p = np.array([pivot[0], pivot[1], 0.0])
    b = p + L * np.array([np.sin(ang), -np.cos(ang), 0])
    return VGroup(Line(p, b, color=INK, stroke_width=3),
                  Circle(radius=r, color=INK, stroke_width=2.5, fill_color=PALE, fill_opacity=1).move_to(b))


def ceiling(pivot, w=1.0):
    p = np.array([pivot[0], pivot[1], 0.0])
    return VGroup(Line(p + LEFT * w / 2, p + RIGHT * w / 2, color=MUTED, stroke_width=5), Dot(p, radius=0.06, color=INK))


def bowl(cx, cy, w=1.2, h=0.8, color=MUTED):
    us = np.linspace(-1, 1, 40)
    return VMobject(color=color, stroke_width=3).set_points_smoothly([[cx + w * u, cy + h * u * u, 0] for u in us])


def ball_in_bowl(cx, cy, u, w=1.2, h=0.8, r=0.13, color=BLUE):
    return Dot([cx + w * u, cy + h * u * u + r, 0], radius=r, color=color)


# ------------------------------------------------------------------ the position-momentum plane

def plane(c, r=2.0, size=22, names=True):
    c = np.array([c[0], c[1], 0.0])
    g = VGroup(axis_arrow(c + LEFT * (r + 0.3), c + RIGHT * (r + 0.45)),
               axis_arrow(c + DOWN * (r + 0.3), c + UP * (r + 0.45)))
    if names:
        g.add(T("position", size, MUTED).next_to(g[0].get_end(), DOWN, buff=0.15).align_to(g[0].get_end(), RIGHT))
        g.add(T("momentum", size, MUTED).next_to(g[1].get_end(), RIGHT, buff=0.15))
    return g


def plane_arrow(c, r, ang, color=BLUE, width=6, opacity=1.0):
    c = np.array([c[0], c[1], 0.0])
    a = Arrow(c, c + r * np.array([np.cos(ang), np.sin(ang), 0]), buff=0, color=color, stroke_width=width,
              tip_length=0.24, max_tip_length_to_length_ratio=0.3)
    return a.set_opacity(opacity)


def orbit(c, r, color=LINE, width=3):
    return DashedVMobject(Circle(radius=r, color=color, stroke_width=width).move_to([c[0], c[1], 0]), num_dashes=40)


# ------------------------------------------------------------------ ladders

def rungs(x, base, gap, n, w=2.2, color=INK, width=4, start=0.5):
    return VGroup(*[Line([x - w / 2, base + (k + start) * gap, 0], [x + w / 2, base + (k + start) * gap, 0],
                         color=color, stroke_width=width) for k in range(n)])


def zero_line(x, base, w=2.8):
    g = DashedLine([x - w / 2, base, 0], [x + w / 2, base, 0], color=MUTED, stroke_width=2.5, dash_length=0.12)
    return VGroup(g, T("zero energy", 22, MUTED).next_to(g, LEFT, buff=0.2))


# ================================================================== opening
deck.part("Chapter three")


@slide("Chapter three.", "The Harmonic Oscillator")
def opening(s):
    t = clock(s)
    base = rig_static(-3.6, 0.4, 7.4, 1.0)
    mv = always_redraw(lambda: rig_moving(-3.6, 0.4, 3.6, 1.4 * np.cos(SPIN * t.get_value()), 1.0))
    yield [FadeIn(base), FadeIn(mv)]
    yield [FadeIn(at(T("a mass on a spring", 30, MUTED), 0, -1.4))]


# ================================================================== previously
deck.part("Previously")


def rules_card(x=-3.75, y=0.1):
    box = at(card(None, 6.7, 3.9, LINE), x, y)
    head = at(T("chapter 2: the rules", 28, INK, True), x, y + 1.45)
    rows = VGroup(T("a state: a list of amplitudes", 24, BLUE), T("a measurable quantity: an operator", 24, PURPLE),
                  T("a chance: an amplitude's size, squared", 24, TEAL),
                  T("the energy moves the state in time", 24, PURPLE)).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
    rows.move_to([x, y - 0.35, 0])
    return VGroup(box, head, rows)


@slide("The last chapter gave us the rules", "The rules from chapter 2")
def prev1(s):
    rc = rules_card()
    yield [FadeIn(rc[0]), FadeIn(rc[1]), LaggedStart(*[FadeIn(r, shift=RIGHT * 0.15) for r in rc[2]], lag_ratio=0.25)]
    one = at(card("one system,\nfrom start to finish", 4.2, 1.5, ORANGE, 28), 4.85, 0.1)
    yield [GrowArrow(arrow(rc[0], one)), FadeIn(one)]


@slide("That system is the spring from chapter one.", "The spring from chapter 1")
def prev2(s):
    t = clock(s)
    rc = rules_card()
    s.add(rc)
    frame = at(card(None, 6.3, 3.9, ORANGE), 3.95, 0.1)
    base = rig_static(1.3, 0.3, 5.6, 0.7)
    mv = always_redraw(lambda: rig_moving(1.3, 0.3, 2.8, 0.9 * np.cos(SPIN * t.get_value()), 0.7))
    yield [GrowArrow(arrow(rc[0], frame)), FadeIn(frame), FadeIn(base), FadeIn(mv)]
    yield [FadeIn(at(T("chapter 1's spring", 28, INK, True), 3.95, 1.55))]


# ================================================================== why the spring
deck.part("Chapter three")


def wobblers(t):
    xs = (-4.6, 0.0, 4.6)
    pv = (xs[0], 0.7)
    pend = VGroup(ceiling(pv), always_redraw(lambda: pendulum(pv, 1.7, 0.35 * np.cos(2.2 * t.get_value()))))
    mol = always_redraw(lambda: hcl([xs[1], -0.3], 1.6 + 0.2 * np.cos(5 * t.get_value()), 0.9, spring=INK))

    def string():
        a = 0.35 * np.cos(4 * t.get_value())
        us = np.linspace(0, 1, 40)
        return VMobject(color=INK, stroke_width=4).set_points_smoothly(
            [[xs[2] - 1.5 + 3 * u, -0.3 + a * np.sin(PI * u), 0] for u in us])
    strg = VGroup(Dot([xs[2] - 1.5, -0.3, 0], radius=0.08, color=MUTED), Dot([xs[2] + 1.5, -0.3, 0], radius=0.08, color=MUTED),
                  always_redraw(string))
    names = VGroup(*[at(lab(n, 26, INK), x, -1.75) for n, x in zip(("a pendulum", "a molecule", "a guitar string"), xs)])
    return VGroup(pend, mol, strg), names


@slide("The spring is worth the effort", "Why the spring")
def why1(s):
    t = clock(s)
    yield [FadeIn(at(T("two reasons", 30, INK, True), 0, 2.3))]
    first = left_at(VGroup(num_pill(1), T("anything that wobbles a little around a resting spot", 28, INK)).arrange(RIGHT, buff=0.25), -6.6, 1.45)
    yield [FadeIn(first, shift=RIGHT * 0.15)]
    icons, names = wobblers(t)
    yield [FadeIn(icons), FadeIn(names), FadeIn(at(lab("each behaves like a spring", 26, ORANGE, True), 0, -2.6))]


def standing(x0, x1, y, k, a, color=INK):
    us = np.linspace(0, 1, 60)
    return VMobject(color=color, stroke_width=4).set_points_smoothly(
        [[x0 + (x1 - x0) * u, y + a * np.sin(k * PI * u), 0] for u in us])


@slide("And later, every wave of a quantum field", "Later: the waves of a field")
def why2(s):
    t = clock(s)
    rows = VGroup()
    for i, (k, rate) in enumerate(((1, 1.3), (2, 2.2), (3, 3.1))):
        y = 1.55 - 1.3 * i
        wave = always_redraw(lambda y=y, k=k, rate=rate: standing(-6.6, -2.6, y, k, 0.42 * np.cos(rate * t.get_value())))
        st = rig_static(-0.3, y, 3.7, 0.5)
        mv = always_redraw(lambda y=y, rate=rate: rig_moving(-0.3, y, 2.0, 0.55 * np.cos(rate * t.get_value()), 0.5))
        rows.add(VGroup(wave, at(T("=", 34, MUTED), -1.45, y), st, mv))
    heads = VGroup(at(lab("each wave of a field", 24, INK), -4.6, 2.45), at(lab("a spring", 24, INK), 1.6, 2.45))
    yield [FadeIn(heads), LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.3)]
    yield [FadeIn(at(T("understand the quantum spring, and you understand a lot", 28, ORANGE, True), 0, -2.75))]


# ------------------------------------------------------------------ where we end up

EX = (-5.7, -1.25, 4.15)   # label, classical and quantum column centres
EW, EH = 5.2, 1.55
EY = (1.4, -0.35, -2.1)
END_LABELS = ("energy", "lowest energy", "motion")
END_TEXT = (("any amount", "only certain amounts, evenly spaced, like rungs"),
            ("sits still, with zero energy", "never still: it always jiggles a little"),
            ("swings back and forth", "swings like it, on average"))


def end_frame():
    heads = VGroup(at(T("classical spring", 28, MUTED, True), EX[1], 2.45), at(T("quantum spring", 28, INK, True), EX[2], 2.45))
    boxes = VGroup(*[at(card(None, EW, EH, LINE), x, y) for y in EY for x in EX[1:]])
    return heads, boxes


def end_label(k):
    return at(words(END_LABELS[k], 8, 26, MUTED, align=RIGHT), EX[0], EY[k]).align_to([-4.2, 0, 0], RIGHT)


def end_draw(k, q, t):
    """The moving picture in row k, column q (0 classical, 1 quantum)."""
    x, y = EX[1 + q] - 1.35, EY[k]
    if k == 0:
        def draw():
            v = t.get_value()
            bottom = y - 0.6
            frame = Rectangle(width=1.3, height=1.2, color=LINE, stroke_width=2).move_to([x, y, 0])
            if q == 0:
                hgt = 0.6 + 0.45 * np.sin(0.9 * v)
                lines = VGroup()
            else:
                lev = (0, 1, 2, 3, 4, 3, 2, 1)[int(v * 1.2) % 8]
                hgt = 0.12 + 0.24 * lev
                lines = VGroup(*[Line([x - 0.65, bottom + 0.12 + 0.24 * j, 0], [x + 0.65, bottom + 0.12 + 0.24 * j, 0],
                                      color=INK, stroke_width=2.5) for j in range(5)])
            fill = Rectangle(width=1.3, height=hgt, stroke_width=0, fill_color=BLUE, fill_opacity=0.35).move_to([x, bottom + hgt / 2, 0])
            return VGroup(fill, frame, lines)
        return always_redraw(draw)
    if k == 1:
        if q == 0:
            return VGroup(bowl(x, y - 0.5, 0.85), ball_in_bowl(x, y - 0.5, 0.0, 0.85))
        return VGroup(bowl(x, y - 0.5, 0.85), always_redraw(lambda: ball_in_bowl(
            x, y - 0.5, 0.14 * np.sin(7 * t.get_value()) + 0.08 * np.sin(11.3 * t.get_value()), 0.85)))
    track = hline(x - 0.95, x + 0.95, y - 0.45, MUTED, 3)
    if q == 0:
        return VGroup(track, always_redraw(lambda: Dot([x + 0.6 * np.cos(SPIN * t.get_value()), y - 0.3, 0], radius=0.13, color=BLUE)))
    return VGroup(track, always_redraw(lambda: area(bell(0.6 * np.cos(SPIN * t.get_value()), 0.17), -0.95, 0.95, x, y - 0.45, 1.0, 0.9, n=60)))


def end_text(k, q):
    return left_at(words(END_TEXT[k][q], 20, 24, INK), EX[1 + q] - 0.25, EY[k])


def end_base(s, t, full_rows, classical_extra=False):
    heads, boxes = end_frame()
    s.add(heads, boxes)
    for k in range(full_rows):
        s.add(end_label(k), end_draw(k, 0, t), end_text(k, 0), end_draw(k, 1, t), end_text(k, 1))
    if classical_extra:
        k = full_rows
        s.add(end_label(k), end_draw(k, 0, t), end_text(k, 0))


@slide("Here's where we end up.", "Where we end up")
def end1(s):
    t = clock(s)
    heads, boxes = end_frame()
    yield [FadeIn(heads), LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.05)]
    yield [FadeIn(end_label(0)), FadeIn(end_draw(0, 0, t)), FadeIn(end_text(0, 0))]


@slide("A quantum spring can only hold certain amounts", "Where we end up")
def end2(s):
    t = clock(s)
    end_base(s, t, 0, classical_extra=True)
    yield [FadeIn(end_draw(0, 1, t))]
    yield [FadeIn(end_text(0, 1), shift=LEFT * 0.15)]


@slide("A classical spring can sit still with zero energy.", "Where we end up")
def end3(s):
    t = clock(s)
    end_base(s, t, 1)
    yield [FadeIn(end_label(1)), FadeIn(end_draw(1, 0, t)), FadeIn(end_text(1, 0))]
    yield [FadeIn(end_draw(1, 1, t)), FadeIn(end_text(1, 1), shift=LEFT * 0.15)]


@slide("And yet, on average, it swings exactly", "Where we end up")
def end4(s):
    t = clock(s)
    end_base(s, t, 2)
    yield [FadeIn(end_label(2)), FadeIn(end_draw(2, 0, t)), FadeIn(end_text(2, 0))]
    yield [FadeIn(end_draw(2, 1, t)), FadeIn(end_text(2, 1), shift=LEFT * 0.15)]


# ================================================================== why springs are everywhere
deck.part("Why springs are everywhere")


def V(u):
    """A smooth, lopsided valley with its lowest point at u = 0."""
    return 0.5 * u * u - 0.14 * u ** 3 + 0.012 * u ** 4


def valley(X, Y, sc, u0=-1.6, u1=4.5, color=INK, width=5):
    return curve(V, u0, u1, X, Y, sc, sc, color, width)


def wobble_ball(X, Y, sc, t, a=0.25, rate=2.4, r=0.16):
    def draw():
        u = a * np.cos(rate * t.get_value())
        return Dot([X + sc * u, Y + sc * V(u) + r, 0], radius=r, color=BLUE)
    return always_redraw(draw)


@slide("Why springs are everywhere.", "Zooming in on a valley")
def zoom1(s):
    t = clock(s)
    X, Y, sc = -4.4, -3.0, 1.05
    yield [Create(valley(X, Y, sc)), FadeIn(wobble_ball(X, Y, sc, t)), FadeIn(at(lab("any smooth valley", 26, INK), -3.4, 0.7))]
    box = at(Rectangle(width=1.5, height=0.7, color=ORANGE, stroke_width=3), X, Y + 0.22)
    IX, IY = 3.9, -0.45
    inset = at(Rectangle(width=6.0, height=4.4, color=ORANGE, stroke_width=3), IX, IY)
    links = VGroup(DashedLine(box.get_corner(UR), inset.get_corner(UL), color=LINE, stroke_width=2),
                   DashedLine(box.get_corner(DR), inset.get_corner(DL), color=LINE, stroke_width=2))
    zoomed = curve(V, -0.6, 0.6, IX, IY - 1.9, 4.5, 14, INK, 5)

    def zball():
        u = 0.25 * np.cos(2.4 * t.get_value())
        return Dot([IX + 4.5 * u, IY - 1.9 + 14 * V(u) + 0.16, 0], radius=0.16, color=BLUE)
    yield [Create(box), Create(links), FadeIn(inset), Create(zoomed), FadeIn(always_redraw(zball)),
           FadeIn(at(lab("zoomed in: it looks like a parabola", 26, ORANGE, True), IX, IY + 1.75))]


@slide("A parabola is exactly the shape", "A spring's energy")
def zoom2(s):
    t = clock(s)
    xw, ry = -6.8, 1.95
    s.add(rig_static(xw, ry, 4.4, 0.6))
    rig = always_redraw(lambda: rig_moving(xw, ry, 2.5, 0.75 * np.cos(SPIN * t.get_value()), 0.6))
    O = (-4.3, -3.0)
    axes = VGroup(axis_arrow((-6.6, O[1]), (-2.0, O[1])), axis_arrow(O, (O[0], -0.15)),
                  lab("stretch", 22).move_to([-2.4, O[1] - 0.3, 0]), lab("energy", 22).move_to([O[0] + 0.55, -0.15, 0]))
    para = curve(lambda u: u * u, -1.3, 1.3, O[0], O[1], 1.6, 1.55, ORANGE, 5)
    dot = always_redraw(lambda: Dot([O[0] + 1.6 * np.cos(SPIN * t.get_value()), O[1] + 1.55 * np.cos(SPIN * t.get_value()) ** 2, 0],
                                    radius=0.12, color=BLUE))
    yield [FadeIn(rig), FadeIn(axes), Create(para), FadeIn(dot),
           FadeIn(at(lab("energy grows with the stretch squared", 24, ORANGE), -4.3, 0.75))]
    X, Y, sc = 3.5, -3.0, 0.85
    yield [Create(valley(X, Y, sc)), Create(curve(lambda u: 0.5 * u * u, -1.9, 1.9, X, Y, sc, sc, ORANGE, 4)),
           FadeIn(wobble_ball(X, Y, sc, t, 0.3)),
           FadeIn(at(words("a small wobble at the bottom is a spring wobble", 24, 26, INK, align=ORIGIN), 4.3, 0.9))]


PO = (-1.7, -3.0)      # origin of the pendulum's energy plot
PSX, PSY = 6.6, 4.0    # screen units per radian, per unit of energy
PIV = (-5.3, 2.1)


def pend_plot():
    axes = VGroup(axis_arrow(PO, (7.0, PO[1])), axis_arrow(PO, (PO[0], 0.9)),
                  lab("swing angle", 22).move_to([6.2, PO[1] - 0.32, 0]), lab("energy", 22).move_to([PO[0] + 0.6, 0.9, 0]))
    pcurve = curve(lambda u: 1 - np.cos(u), 0, 1.25, PO[0], PO[1], PSX, PSY, INK, 5)
    return axes, pcurve


def pend_rig(t, amp=0.19):
    return VGroup(ceiling(PIV), always_redraw(lambda: pendulum(PIV, 3.3, amp * np.cos(1.8 * t.get_value()))))


@slide("The pendulum is a good check.", "Checking with a pendulum")
def pend1(s):
    t = clock(s)
    axes, pcurve = pend_plot()
    yield [FadeIn(pend_rig(t)), FadeIn(at(lab("a pendulum", 24, INK), PIV[0], -1.85)), FadeIn(axes), Create(pcurve),
           FadeIn(legend_item("the pendulum's energy", INK, -0.9, 2.2))]
    para = curve(lambda u: u * u / 2, 0, 1.25, PO[0], PO[1], PSX, PSY, ORANGE, 4)
    yield [Create(DashedVMobject(para, num_dashes=50)), FadeIn(legend_item("the spring's parabola", ORANGE, -0.9, 1.7, dashed=True))]
    th = np.radians(11)
    band = Rectangle(width=PSX * th, height=1.2, stroke_width=0, fill_color=TEAL, fill_opacity=0.18).move_to([PO[0] + PSX * th / 2, PO[1] + 0.6, 0])
    edge = DashedLine([PO[0] + PSX * th, PO[1], 0], [PO[0] + PSX * th, PO[1] + 1.2, 0], color=TEAL, stroke_width=3)
    p = np.array([PIV[0], PIV[1], 0.0])
    rays = VGroup(*[DashedLine(p, p + 3.3 * np.array([np.sin(a), -np.cos(a), 0]), color=TEAL, stroke_width=2.5) for a in (-th, th)])
    yield [FadeIn(band), Create(edge), FadeIn(at(lab("11°", 24, TEAL, True), PO[0] + PSX * th, PO[1] + 1.45)),
           FadeIn(left_at(words("they agree to within 0.3% for swings up to about 11°", 26, 26, TEAL), PO[0] + 0.25, -0.65)),
           Create(rays), FadeIn(at(lab("11° each way", 22, TEAL), PIV[0] + 2.1, 0.9))]


def morse(r):
    return (1 - np.exp(-1.5 * (r - 1.4))) ** 2


@slide("The atoms in a molecule also sit", "A molecule's bond")
def mol1(s):
    t = clock(s)
    X0, Y0, SX, SY = -6.6, -3.0, 1.85, 2.4

    def X(r):
        return X0 + SX * (r - 0.9)
    axes = VGroup(axis_arrow((X0 - 0.1, Y0), (1.4, Y0)), axis_arrow((X0 - 0.1, Y0), (X0 - 0.1, 0.4)),
                  lab("distance between the atoms", 22).move_to([-1.3, Y0 - 0.32, 0]), lab("energy", 22).move_to([X0 + 0.55, 0.4, 0]))
    vc = curve(lambda r: morse(r), 0.9, 5.0, X0 - SX * 0.9, Y0, SX, SY, INK, 5)
    ball = always_redraw(lambda: Dot([X(1.4 + 0.12 * np.cos(3 * t.get_value())), Y0 + SY * morse(1.4 + 0.12 * np.cos(3 * t.get_value())) + 0.15, 0],
                                     radius=0.15, color=BLUE))
    yield [FadeIn(axes), Create(vc), FadeIn(ball), FadeIn(at(lab("the bottom of an energy valley", 24, INK), -2.6, 1.3))]
    para = curve(lambda r: 2.25 * (r - 1.4) ** 2, 0.98, 1.95, X0 - SX * 0.9, Y0, SX, SY, ORANGE, 4)
    mol = always_redraw(lambda: hcl([4.6, 0.0], 2.4 + 0.25 * np.cos(5 * t.get_value()), 1.3, spring=ORANGE, width=5))
    yield [Create(para), FadeIn(mol), FadeIn(at(lab("a tiny, very stiff spring", 28, ORANGE, True), 4.6, -1.4))]


# ================================================================== a puzzle about heat
deck.part("A puzzle about heat")


@slide("A puzzle about heat.", "Hydrogen chloride")
def hcl1(s):
    t = clock(s)
    box = gas_box((-4.3, -0.1), 4.6, 3.8)
    yield [FadeIn(box), FadeIn(always_redraw(lambda: gas((-4.3, -0.1), 4.6, 3.8, t.get_value(), n=9))),
           FadeIn(at(lab("a gas", 24, INK), -4.3, -2.35))]
    big = always_redraw(lambda: hcl([3.4, 0.2], 2.9 + 0.2 * np.cos(5 * t.get_value()), 1.6, spring=ORANGE, width=5))
    yield [FadeIn(big), FadeIn(at(T("hydrogen chloride, HCl", 30, INK, True), 3.4, 2.0))]
    yield [FadeIn(at(lab("chlorine", 24, INK), 1.95, -1.05)), FadeIn(at(lab("hydrogen", 24, INK), 4.85, -1.05)),
           FadeIn(at(lab("a tiny spring", 26, ORANGE, True), 3.4, -1.9))]


def absorb(f):
    return 1 / (1 + ((f - 0.55) / 0.05) ** 2)


def ir_parts(t):
    box = gas_box((-5.0, 0.9), 3.2, 2.1)
    mols = always_redraw(lambda: gas((-5.0, 0.9), 3.2, 2.1, t.get_value(), n=5, seed=8))
    us = np.linspace(-7.3, -2.75, 120)
    wave = VMobject(color=MUTED, stroke_width=3).set_points_smoothly([[x, 0.9 + 0.16 * np.sin(6 * x), 0] for x in us])
    ax = VGroup(axis_arrow((-1.6, -2.8), (6.9, -2.8)), axis_arrow((-1.6, -2.8), (-1.6, 1.4)),
                lab("frequency of the light", 22).move_to([5.3, -3.12, 0]), lab("light soaked up", 22).move_to([-0.55, 1.45, 0]))
    peak = curve(absorb, 0.0, 1.0, -1.6, -2.8, 8.2, 3.6, INK, 4, n=300)
    return VGroup(box, mols, wave, at(lab("infrared light", 22, MUTED), -5.0, 2.25)), ax, peak


@slide("Shine infrared light through the gas", "The light it soaks up")
def hcl2(s):
    t = clock(s)
    rig, ax, peak = ir_parts(t)
    yield [FadeIn(rig), FadeIn(ax), Create(peak)]
    px = -1.6 + 8.2 * 0.55
    yield [Create(DashedLine([px, -2.8, 0], [px, 0.8, 0], color=ORANGE, stroke_width=3)), FadeIn(Dot([px, 0.8, 0], radius=0.1, color=ORANGE)),
           FadeIn(at(words("about 86.5 trillion vibrations per second", 22, 24, ORANGE, align=ORIGIN), px + 2.4, 0.35))]
    mol = always_redraw(lambda: hcl([-5.0, -1.4], 1.9 + 0.2 * np.cos(9 * t.get_value()), 1.0, spring=ORANGE, width=4))
    yield [FadeIn(mol), FadeIn(at(lab("how fast the bond vibrates", 24, ORANGE, True), -4.8, -2.5))]


@slide("Now heat the gas.", "Heating the gas")
def heat1(s):
    t = clock(s, 1.0)
    c = (-3.6, 0.35)
    box = gas_box(c, 5.6, 3.6)
    s.add(box, always_redraw(lambda: gas(c, 5.6, 3.6, t.get_value(), n=10, seed=5)))
    waves = VGroup(*[VMobject(color=ORANGE, stroke_width=4).set_points_smoothly(
        [[x + 0.12 * np.sin(5 * y), y, 0] for y in np.linspace(-3.3, -1.75, 30)]) for x in (-5.4, -3.6, -1.8)])
    t.rate = 2.6
    yield [Create(waves), FadeIn(at(lab("heat", 26, ORANGE, True), -0.4, -2.6)),
           FadeIn(at(lab("molecules move faster", 24, INK), -3.6, 2.45))]
    yield [FadeIn(at(card("classical physics\nhas a simple rule", 4.6, 1.6, INK, 30), 4.6, 0.35), shift=LEFT * 0.2)]


def motion_icon(kind, c, t=None, k=0.6):
    """Flying, tumbling or vibrating: a molecule with a sign of how it moves."""
    x, y = c
    if kind == 0:
        if t is None:
            mol = hcl([x - 0.25, y], 0.95, k, spring=INK, width=2)
        else:
            mol = always_redraw(lambda: hcl([x - 0.25 + 0.3 * np.sin(1.5 * t.get_value()), y], 0.95, k, spring=INK, width=2))
        return VGroup(mol, Arrow([x + 0.55, y, 0], [x + 1.15, y, 0], buff=0, color=MUTED, stroke_width=4, tip_length=0.16))
    if kind == 1:
        if t is None:
            mol = hcl([x, y], 0.95, k, spring=INK, width=2, angle=0.5)
        else:
            mol = always_redraw(lambda: hcl([x, y], 0.95, k, spring=INK, width=2, angle=0.8 * t.get_value()))
        return VGroup(mol, CurvedArrow(np.array([x + 0.8, y - 0.3, 0]), np.array([x + 0.3, y + 0.75, 0]), angle=PI / 2.4,
                                       color=PURPLE, stroke_width=4, tip_length=0.16))
    if t is None:
        return hcl([x, y], 1.2, k, spring=ORANGE, width=3)
    return always_redraw(lambda: hcl([x, y], 1.2 + 0.18 * np.cos(6 * t.get_value()), k, spring=ORANGE, width=3))


MOTIONS = (("flying around", MUTED), ("tumbling", PURPLE), ("vibrating", ORANGE))


@slide("Every way a molecule can hold energy", "Equal shares")
def heat2(s):
    t = clock(s)
    yield [FadeIn(at(words("every way a molecule can hold energy takes an equal share of the heat", 40, 30, INK, align=ORIGIN), 0, 1.75))]
    xs = (-4.6, 0.0, 4.6)
    icons = VGroup(*[motion_icon(k, (xs[k], -0.3), t, 0.8) for k in range(3)])
    names = VGroup(*[at(lab(MOTIONS[k][0], 28, MOTIONS[k][1], True), xs[k], -1.7) for k in range(3)])
    yield [LaggedStart(*[FadeIn(VGroup(i, n)) for i, n in zip(icons, names)], lag_ratio=0.35)]


HB = 0.55            # height of one unit of heat in the bar chart
HBASE = -2.8
SX_, MX_ = -0.4, 3.2  # x of the predicted stack and of the measured bar


def heat_stack(vib_opacity=0.75):
    segs, y = VGroup(), HBASE
    for n, (name, color) in zip((3, 2, 2), MOTIONS):
        h = n * HB
        op = vib_opacity if color == ORANGE else 0.75
        segs.add(Rectangle(width=1.9, height=h, stroke_color=WHITE, stroke_width=2, fill_color=color, fill_opacity=op).move_to([SX_, y + h / 2, 0]))
        y += h
    return segs


def heat_legend():
    g = VGroup()
    ys = (HBASE + 1.5 * HB, HBASE + 4 * HB, HBASE + 6 * HB)
    for k, y in enumerate(ys):
        g.add(VGroup(motion_icon(k, (-6.5, y), None, 0.45), left_at(lab(MOTIONS[k][0], 24, MOTIONS[k][1], True), -5.15, y)))
    return g


def heat_axis():
    return VGroup(hline(-2.0, 4.8, HBASE, MUTED, 4), at(lab("classical prediction", 24, INK), SX_, HBASE - 0.38))


def measured_bar():
    h = 5 * HB
    return VGroup(Rectangle(width=1.9, height=h, stroke_width=0, fill_color=INK, fill_opacity=0.6).move_to([MX_, HBASE + h / 2, 0]),
                  at(lab("measured", 24, INK), MX_, HBASE - 0.38))


def share_brace():
    b = BraceBetweenPoints([SX_ + 1.05, HBASE + 7 * HB, 0], [SX_ + 1.05, HBASE + 5 * HB, 0], direction=RIGHT, color=ORANGE)
    return b


@slide("So the rule predicts how much heat it takes", "The classical prediction")
def heat3(s):
    s.add(heat_legend(), heat_axis())
    stack = heat_stack()
    yield [LaggedStart(*[GrowFromEdge(r, DOWN) for r in stack], lag_ratio=0.5)]
    yield [FadeIn(at(lab("heat needed to warm the gas", 24, INK), SX_, HBASE + 7 * HB + 0.35))]


@slide("The measurement comes out lower", "The measurement")
def heat4(s):
    s.add(heat_legend(), heat_axis(), at(lab("heat needed to warm the gas", 24, INK), SX_, HBASE + 7 * HB + 0.35))
    stack = heat_stack()
    s.add(stack)
    bar = measured_bar()
    top = HBASE + 5 * HB
    yield [GrowFromEdge(bar[0], DOWN), FadeIn(bar[1]), Create(DashedLine([SX_ - 0.95, top, 0], [MX_ + 0.95, top, 0], color=MUTED, stroke_width=2)),
           FadeIn(share_brace()), FadeIn(left_at(words("short by exactly the vibration's share", 22, 24, ORANGE), SX_ + 1.7, top + 0.55))]
    yield [stack[2].animate.set_fill(opacity=0.12), FadeIn(at(words("the bond takes no heat, as if it were frozen", 22, 26, INK, align=ORIGIN), 5.6, 1.75))]


@slide("Classical physics can't explain that.", "An open puzzle")
def heat5(s):
    stack = heat_stack(0.12)
    s.add(heat_legend(), heat_axis(), stack, measured_bar(), share_brace())
    yield [Create(cross(stack[2], RED, 5)), FadeIn(at(lab("the classical rule can't explain it", 26, RED, True), 3.4, 1.9))]
    yield [FadeIn(at(card("the quantum spring can,\nonce we've solved it", 4.8, 1.3, ORANGE, 28), 4.5, 0.95), shift=UP * 0.15)]


# ================================================================== the spinning arrow
deck.part("The spring as a spinning arrow")


@slide("The spring as a spinning arrow.", "Chapter 1's spring")
def arr1(s):
    t = clock(s)
    a = ValueTracker(0.0)
    s.add(a)
    xw, y, rest = -5.0, 0.4, 4.6
    base = rig_static(xw, y, 8.2, 1.0)

    name = T("mass", 22, INK)

    def draw():
        d = a.get_value() * np.cos(SPIN * t.get_value())
        g = rig_moving(xw, y, rest, d, 1.0)
        g.add(name.copy().move_to(g[1]))
        return g
    mv = always_redraw(draw)
    yield [FadeIn(base), FadeIn(mv), FadeIn(at(lab("stiffness", 24, INK), -3.2, 1.25))]
    yield [a.animate.set_value(1.6), FadeIn(at(lab("it swings back and forth", 26, INK), -0.4, -1.4))]


def energy_parts(t, x0=-2.4, L=6.0, rows=(True, True)):
    """A total-energy bar split into its position and momentum parts, and the two parts on their own."""
    def tot():
        c2 = np.cos(SPIN * t.get_value()) ** 2
        a = Rectangle(width=max(L * c2, 0.01), height=0.5, stroke_width=0, fill_color=INK, fill_opacity=0.65)
        b = Rectangle(width=max(L * (1 - c2), 0.01), height=0.5, stroke_width=0, fill_color=MUTED, fill_opacity=0.35)
        a.move_to([x0 + a.width / 2, -0.1, 0])
        b.move_to([x0 + L * c2 + b.width / 2, -0.1, 0])
        return VGroup(a, b)

    def part(k):
        def draw():
            c2 = np.cos(SPIN * t.get_value()) ** 2
            v = c2 if k == 0 else 1 - c2
            r = Rectangle(width=max(L * v, 0.01), height=0.42, stroke_width=0, fill_color=INK if k == 0 else MUTED,
                          fill_opacity=0.65 if k == 0 else 0.35)
            return r.move_to([x0 + r.width / 2, (-1.3, -2.45)[k], 0])
        return always_redraw(draw)
    total = VGroup(always_redraw(tot), Rectangle(width=L, height=0.5, color=INK, stroke_width=2).move_to([x0 + L / 2, -0.1, 0]),
                   left_at(lab("energy", 24, INK, True), -6.9, -0.1))
    rowp = VGroup(part(0), left_at(VGroup(lab("position part", 24, INK, True), lab("grows with position squared", 22)).arrange(DOWN, buff=0.08, aligned_edge=LEFT), -6.9, -1.3))
    rowm = VGroup(part(1), left_at(VGroup(lab("momentum part", 24, INK, True), lab("grows with momentum squared", 22)).arrange(DOWN, buff=0.08, aligned_edge=LEFT), -6.9, -2.45))
    return total, rowp, rowm


@slide("Its energy has two parts.", "Two parts of the energy")
def arr2(s):
    t = clock(s)
    s.add(rig_static(-3.6, 1.75, 6.0, 0.7), always_redraw(lambda: rig_moving(-3.6, 1.75, 3.6, 1.2 * np.cos(SPIN * t.get_value()), 0.7)))
    total, rowp, rowm = energy_parts(t)
    yield [FadeIn(total), FadeIn(left_at(lab("total stays the same", 22, INK), 3.85, -0.1))]
    yield [FadeIn(rowp)]
    yield [FadeIn(rowm)]


@slide("Here's a neat trick.", "A neat trick")
def arr3(s):
    e1 = at(heq("across² + up²", 40, INK), -3.6, 1.2)
    yield [FadeIn(e1), FadeIn(at(lab("two squares, added together", 24, INK), -3.6, 2.0))]
    o, tip = np.array([0.9, -2.5, 0]), np.array([5.3, 0.8, 0])
    legs = VGroup(DashedLine(o, [tip[0], o[1], 0], color=MUTED, stroke_width=3), DashedLine([tip[0], o[1], 0], tip, color=MUTED, stroke_width=3))
    arr = Arrow(o, tip, buff=0, color=BLUE, stroke_width=7, tip_length=0.26)
    names = VGroup(lab("across", 24, INK).next_to(legs[0], DOWN, buff=0.15), lab("up", 24, INK).next_to(legs[1], RIGHT, buff=0.15))
    yield [Create(legs), FadeIn(names), GrowArrow(arr),
           FadeIn(at(heq("= (length of one arrow)²", 34, BLUE), -3.6, 0.3)),
           FadeIn(at(lab("an arrow in the complex plane", 24, INK), -3.6, -0.5))]


PC = (-3.0, -0.4)


@slide("Position runs across, and momentum runs up.", "Position across, momentum up")
def arr4(s):
    pl = plane(PC, 2.1)
    xw, y = 1.6, 1.3
    rig = VGroup(rig_static(xw, y, 5.4, 0.7), rig_moving(xw, y, 2.6, 1.0, 0.7))
    rest = DashedLine([xw + 2.6, y - 0.6, 0], [xw + 2.6, y + 0.6, 0], color=MUTED, stroke_width=2)
    pos = Arrow([xw + 2.6, y - 0.6, 0], [xw + 3.6, y - 0.6, 0], buff=0, color=INK, stroke_width=4, tip_length=0.14)
    mom = Arrow([xw + 3.6, y + 0.55, 0], [xw + 4.4, y + 0.55, 0], buff=0, color=INK, stroke_width=4, tip_length=0.14)
    yield [FadeIn(pl), FadeIn(rig), FadeIn(rest), GrowArrow(pos), GrowArrow(mom),
           FadeIn(lab("position", 22, INK).next_to(pos, DOWN, buff=0.1)), FadeIn(lab("momentum", 22, INK).next_to(mom, UP, buff=0.08))]
    r, ang = 2.1, 0.62
    tip = np.array([PC[0] + r * np.cos(ang), PC[1] + r * np.sin(ang), 0])
    proj = VGroup(DashedLine(tip, [tip[0], PC[1], 0], color=MUTED, stroke_width=2), DashedLine(tip, [PC[0], tip[1], 0], color=MUTED, stroke_width=2))
    yield [Create(proj), GrowArrow(plane_arrow(PC, r, ang)), FadeIn(at(words("one arrow holds both the position and the momentum", 24, 26, BLUE, align=ORIGIN), 4.3, -1.4))]


@slide("Then the motion becomes very simple.", "A simple motion")
def arr5(s):
    s.add(plane(PC, 2.1))
    ang = ValueTracker(0.62)
    arr = always_redraw(lambda: plane_arrow(PC, 2.1, ang.get_value()))
    s.add(arr)
    yield [ang.animate.set_value(0.62 - 2 * PI), Create(orbit(PC, 2.1)), FadeIn(at(lab("the arrow goes round a circle", 26, INK), 3.6, 1.0))]
    yield [FadeIn(at(words("its length never changes, and the length sets the energy", 24, 26, BLUE, align=ORIGIN), 3.6, -0.6))]


@slide("And the arrow spins round at a steady rate", "The spinning arrow")
def arr6(s):
    t = clock(s)
    c = (-3.4, -0.4)
    xw, y = 0.9, -0.4
    spin = always_redraw(lambda: plane_arrow(c, 2.0, -SPIN * t.get_value()))

    def proj():
        a = -SPIN * t.get_value()
        tip = np.array([c[0] + 2.0 * np.cos(a), c[1] + 2.0 * np.sin(a), 0])
        return VGroup(Line(tip, [tip[0], c[1], 0], color=LINE, stroke_width=2), Dot([tip[0], c[1], 0], radius=0.08, color=INK))
    yield [FadeIn(plane(c, 2.0)), FadeIn(orbit(c, 2.0)), FadeIn(spin), FadeIn(always_redraw(proj)),
           FadeIn(rig_static(xw, y, 6.2, 0.7)), FadeIn(always_redraw(lambda: rig_moving(xw, y, 3.3, 1.4 * np.cos(SPIN * t.get_value()), 0.7))),
           FadeIn(at(words("a steady rate: the spring's frequency ω", 24, 26, INK, align=ORIGIN), 4.1, 1.6))]
    yield [FadeIn(at(pill("the whole spring: one spinning arrow", BLUE, 26), 4.1, -2.4), shift=UP * 0.15)]


@slide("This matters for one reason.", "Length squared as a product")
def arr7(s):
    c, r, ang = (-3.2, -0.3), 2.1, 0.6
    yield [FadeIn(plane(c, r)), GrowArrow(plane_arrow(c, r, ang)),
           FadeIn(lab("the arrow", 24, BLUE).move_to([c[0] + r * np.cos(ang) + 0.2, c[1] + r * np.sin(ang) + 0.35, 0]))]
    mirror = DashedVMobject(plane_arrow(c, r, -ang, width=5), num_dashes=14)
    yield [FadeIn(mirror), FadeIn(lab("its mirror image", 24, BLUE).move_to([c[0] + r * np.cos(ang) + 0.6, c[1] - r * np.sin(ang) - 0.4, 0])),
           FadeIn(at(heq("length² = arrow × mirror image", 28, BLUE), 3.7, 1.9))]
    ops = at(card("turn the product into\nquantum operators", 5.0, 1.3, PURPLE, 28), 3.5, -1.4)
    yield [GrowArrow(Arrow([3.5, 1.5, 0], [3.5, -0.65, 0], buff=0, color=PURPLE, stroke_width=4, tip_length=0.18)), FadeIn(ops)]


# ================================================================== turning the arrow into a tool
deck.part("Turning the arrow into a tool")


def op_pipe(first, second, x, y):
    a = at(card(first, 2.3, 0.7, PURPLE, 24), x, y)
    b = at(card(second, 2.3, 0.7, PURPLE, 24), x + 2.9, y)
    return VGroup(a, b, arrow(a, b))


@slide("Turning the arrow into a tool.", "Operators, where order matters")
def tool1(s):
    chips = VGroup(at(chip("position", BLUE, size=26, h=0.7), -5.0, 1.75), at(chip("momentum", BLUE, size=26, h=0.7), -5.0, 0.65))
    ops = VGroup(at(card("position operator", 3.6, 0.7, PURPLE, 24), 1.0, 1.75), at(card("momentum operator", 3.6, 0.7, PURPLE, 24), 1.0, 0.65))
    yield [FadeIn(chips), *[GrowArrow(arrow(c, o, PURPLE)) for c, o in zip(chips, ops)], FadeIn(ops)]
    p1 = op_pipe("position", "momentum", -5.6, -1.4)
    p2 = op_pipe("momentum", "position", 1.5, -1.4)
    yield [FadeIn(p1), FadeIn(p2), FadeIn(at(T("≠", 40, ORANGE, True), -0.6, -1.4)),
           FadeIn(at(lab("apply them in a different order, get a different result", 24, INK), 0, -2.4))]


@slide("The spring's energy keeps the same form.", "Which energies it allows")
def tool2(s):
    e = at(VGroup(T("energy  =", 30, INK), T("position part", 30, PURPLE), T("+", 30, INK), T("momentum part", 30, PURPLE)).arrange(RIGHT, buff=0.25), 0, 1.9)
    yield [FadeIn(e), FadeIn(at(lab("the same form, now built from operators", 24, INK), 0, 1.2))]
    ax = axis_arrow((-1.0, -3.0), (-1.0, 0.25))
    qs = VGroup(*[at(T("?", 30, MUTED, True), -0.4 + 0.5 * (k % 2), -2.5 + 0.58 * k) for k in range(5)])
    yield [FadeIn(ax), FadeIn(lab("energy", 22).next_to(ax.get_end(), UP, buff=0.08)), LaggedStart(*[FadeIn(q) for q in qs], lag_ratio=0.2),
           FadeIn(left_at(lab("which energies are allowed?", 28, ORANGE, True), 1.3, -1.1))]


@slide("You could solve a differential equation", "A shortcut")
def tool3(s):
    a = at(card("the spring's\nenergy", 3.0, 1.3, PURPLE, 26), -5.4, -0.4)
    b = at(card("the allowed\nenergies", 3.0, 1.3, INK, 26), 5.4, -0.4)
    xs = np.linspace(-3.9, 3.9, 120)
    long = VMobject(color=MUTED, stroke_width=4).set_points_smoothly([[x, 0.9 + 0.6 * np.sin(2.3 * x) + 0.3 * np.sin(5.1 * x), 0] for x in xs])
    yield [FadeIn(a), FadeIn(b), Create(long), FadeIn(at(lab("solve a differential equation", 24, MUTED), 0, 2.2))]
    short = Arrow([-3.85, -0.9, 0], [3.85, -0.9, 0], buff=0, color=ORANGE, stroke_width=6, tip_length=0.22)
    yield [GrowArrow(short), FadeIn(at(lab("a shortcut: copy the arrow trick", 26, ORANGE, True), 0, -1.45))]


def build_row(y, color, items, target, size=24):
    chips = VGroup(*[chip(t, color, size=size, h=0.66) for t in items]).arrange(RIGHT, buff=0.3)
    left_at(chips, -6.9, y)
    tg = at(target, 4.4, y)
    return VGroup(chips, arrow(chips, tg, color), tg)


@slide("The arrow is built from position and momentum, so build", "Building the arrow from operators")
def tool4(s):
    r1 = build_row(1.4, BLUE, ("position", "momentum"), card("the arrow", 2.6, 0.8, BLUE, 26))
    yield [FadeIn(r1), FadeIn(left_at(lab("numbers", 22), -6.9, 2.05))]
    r2 = build_row(-0.6, PURPLE, ("position operator", "momentum operator"), card("a new operator", 3.0, 0.8, PURPLE, 26))
    yield [FadeIn(r2), FadeIn(left_at(lab("operators", 22), -6.9, 0.05))]
    yield [FadeIn(at(T("call it  a", 34, PURPLE, True), 4.4, -1.75))]


@slide("Turn its mirror image into a partner operator", "a and a-dagger")
def tool5(s):
    r1 = build_row(1.6, BLUE, ("the arrow", "its mirror image"), heq("a, a†", 40, PURPLE))
    yield [FadeIn(r1), FadeIn(at(lab("a-dagger: the partner of a", 24, PURPLE), 4.4, 0.95))]
    row_c = left_at(VGroup(lab("classical:", 26, MUTED), heq("mirror image × arrow = energy", 30, BLUE)).arrange(RIGHT, buff=0.3), -6.4, -0.6)
    row_q = left_at(VGroup(lab("quantum:", 26, MUTED), heq("a† × a", 34, PURPLE)).arrange(RIGHT, buff=0.3), -6.4, -1.7)
    yield [FadeIn(row_c), FadeIn(row_q, shift=UP * 0.1)]


def len_bar(x0, y, L, color, opacity=0.55, h=0.45):
    return Rectangle(width=L, height=h, stroke_width=0, fill_color=color, fill_opacity=opacity).move_to([x0 + L / 2, y, 0])


@slide("With ordinary numbers, that product gives back", "Multiplying the pair")
def tool6(s):
    x0 = -1.6
    head1 = left_at(lab("with numbers", 26, INK, True), -6.9, 2.3)
    a = VGroup(left_at(lab("mirror × arrow", 24, BLUE), -6.9, 1.55), len_bar(x0, 1.55, 5.6, BLUE))
    b = VGroup(left_at(lab("the energy", 24, INK), -6.9, 0.95), len_bar(x0, 0.95, 5.6, INK, 0.4))
    yield [FadeIn(head1), FadeIn(a), FadeIn(b), FadeIn(check().move_to([x0 + 6.1, 1.25, 0]))]
    head2 = left_at(lab("with operators", 26, INK, True), -6.9, -0.4)
    c = VGroup(left_at(heq("a† a", 28, PURPLE), -6.9, -1.15), len_bar(x0, -1.15, 4.9, PURPLE))
    d = VGroup(left_at(lab("the energy", 24, INK), -6.9, -1.75), len_bar(x0, -1.75, 5.6, INK, 0.4))
    gap = Rectangle(width=0.7, height=0.45, color=ORANGE, stroke_width=3).move_to([x0 + 4.9 + 0.35, -1.15, 0])
    yield [FadeIn(head2), FadeIn(c), FadeIn(d), Create(gap), FadeIn(lab("a little short", 24, ORANGE, True).next_to(gap, RIGHT, buff=0.2)),
           FadeIn(at(lab("because position and momentum don't commute", 24, INK), 0, -2.75))]


MAIN = "energy = ħω(a†a + ½)"


def main_eq(size=52):
    return at(heq(MAIN, size, PURPLE), 0, 0.7)


@slide("The result is short.", "The energy in operators")
def tool7(s):
    e = main_eq()
    yield [FadeIn(glyphs(e, MAIN, "energy ="))]
    yield [FadeIn(glyphs(e, MAIN, "a†a"), shift=DOWN * 0.15)]
    yield [FadeIn(glyphs(e, MAIN, "+ ½")), FadeIn(glyphs(e, MAIN, "ħω(")), FadeIn(glyphs(e, MAIN, ")"))]
    yield [Create(SurroundingRectangle(e, color=PURPLE, buff=0.3, corner_radius=0.12)),
           FadeIn(at(lab("the spring's energy, in operators", 26, INK), 0, -0.6))]


@slide("So it's the classical answer with an extra", "An extra half")
def tool8(s):
    e = main_eq()
    s.add(e)
    half = glyphs(e, MAIN, "+ ½")
    box = SurroundingRectangle(half, color=ORANGE, buff=0.12, stroke_width=4)
    classic = glyphs(e, MAIN, "ħω(a†a")
    yield [Create(Underline(classic, color=MUTED, buff=0.1)), FadeIn(lab("the classical answer", 24, MUTED).next_to(classic, DOWN, buff=0.4).shift(LEFT * 0.45)),
           Create(box), FadeIn(words("an extra ½ ħω: pure quantum mechanics", 22, 26, ORANGE).next_to(box, DOWN, buff=0.4).shift(RIGHT * 1.15))]
    yield [FadeIn(at(pill("it will matter", ORANGE, 28), 0, -2.6), shift=UP * 0.15)]


SWAP = "[a, a†] = 1"


@slide("One more rule drops out.", "The swapping rule")
def tool9(s):
    p1 = at(dcard("a, then a†", 3.0, 0.8, PURPLE, 26), -3.2, 1.6)
    p2 = at(dcard("a†, then a", 3.0, 0.8, PURPLE, 26), 3.2, 1.6)
    yield [FadeIn(p1), FadeIn(p2), FadeIn(at(lab("swap the order", 24, INK), 0, 1.6))]
    e = at(heq(SWAP, 56, PURPLE), 0, -0.5)
    yield [FadeIn(e), FadeIn(at(lab("the two products differ by exactly one", 26, INK), 0, -1.6)),
           FadeIn(at(dT("[a, a†] is shorthand for a a† − a† a", 22, MUTED), 0, -2.3))]


@slide("That single rule is all we need next.", "The swapping rule")
def tool10(s):
    e = at(heq(SWAP, 56, PURPLE), 0, -0.5)
    s.add(at(dcard("a, then a†", 3.0, 0.8, PURPLE, 26), -3.2, 1.6), at(dcard("a†, then a", 3.0, 0.8, PURPLE, 26), 3.2, 1.6),
          at(lab("swap the order", 24, INK), 0, 1.6), e)
    yield [Create(SurroundingRectangle(e, color=ORANGE, buff=0.3, corner_radius=0.12, stroke_width=4))]
    yield [FadeIn(at(lab("all we need for what comes next", 26, ORANGE, True), 0, -2.0))]


# ================================================================== climbing the ladder
deck.part("Climbing the ladder")

NUM = "N = a†a"


@slide("Climbing the ladder.", "The number operator")
def lad1(s):
    e = at(heq(NUM, 60, PURPLE), 0, 0.5)
    yield [FadeIn(glyphs(e, NUM, "a†a"))]
    yield [FadeIn(glyphs(e, NUM, "N =")), FadeIn(at(T("the number operator", 32, PURPLE, True), 0, -0.8))]


@slide("To get the energy, take its value", "From number to energy")
def lad2(s):
    cards = [card("value of N", 2.6, 0.9, PURPLE, 26), card("+ ½", 1.6, 0.9, INK, 28), card("× ħω", 1.8, 0.9, PURPLE, 28),
             card("energy", 2.2, 0.9, INK, 26)]
    xs = (-5.3, -1.9, 0.9, 4.1)
    row = VGroup(*[at(c, x, 1.4) for c, x in zip(cards, xs)])
    links = VGroup(*[arrow(row[i], row[i + 1]) for i in range(3)])
    yield [LaggedStart(*[FadeIn(r) for r in row], lag_ratio=0.25), LaggedStart(*[GrowArrow(l) for l in links], lag_ratio=0.25)]
    line = axis_arrow((-5.5, -1.4), (5.8, -1.4))
    qs = VGroup(*[at(T("?", 32, ORANGE, True), -4.6 + 1.9 * k, -0.8) for k in range(6)])
    yield [FadeIn(line), FadeIn(lab("values of N", 22).next_to(line.get_end(), DOWN, buff=0.12)),
           LaggedStart(*[FadeIn(q) for q in qs], lag_ratio=0.15), FadeIn(at(lab("which values can N have?", 28, ORANGE, True), 0, -2.5))]


THREE = ("a steps down, a† steps up", "the ladder has a bottom", "the ladder has no top")


def three_rows(upto):
    g = VGroup()
    for k in range(3):
        y = 1.6 - 1.25 * k
        p = at(num_pill(k + 1, INK, 24), -1.4, y)
        body = left_at(dT(THREE[k], 28, INK), -0.9, y) if k < upto else left_at(hline(0, 4.5, 0, LINE, 4), -0.9, y)
        g.add(VGroup(p, body))
    return g


@slide("Using only the swapping rule, three things follow.", "What the swapping rule gives")
def lad3(s):
    rule = at(card(None, 3.6, 1.4, PURPLE), -5.0, 0.35)
    rule.add(at(heq(SWAP, 36, PURPLE), -5.0, 0.35))
    rows = three_rows(0)
    yield [FadeIn(rule), FadeIn(rows), GrowArrow(Arrow([-3.1, 0.35, 0], [-1.95, 0.35, 0], buff=0, color=PURPLE, stroke_width=4, tip_length=0.16))]
    yield [FadeIn(left_at(dT(THREE[0], 28, INK), -0.9, 1.6)), FadeOut(rows[0][1])]


LX, LB, LG = -3.6, -2.2, 1.6   # small ladder: x, lowest rung, gap


def small_ladder(names=("1", "2", "3")):
    r = rungs(LX, LB, LG, 3, 2.6, INK, 5, start=0)
    labels = VGroup(*[lab(n, 26, INK).next_to(r[k], LEFT, buff=0.3) for k, n in enumerate(names)])
    rails = VGroup(Line([LX - 1.3, LB - 0.4, 0], [LX - 1.3, LB + 2 * LG + 0.4, 0], color=LINE, stroke_width=3),
                   Line([LX + 1.3, LB - 0.4, 0], [LX + 1.3, LB + 2 * LG + 0.4, 0], color=LINE, stroke_width=3))
    return VGroup(rails, r, labels)


def step_arrows():
    up = CurvedArrow(np.array([LX + 1.6, LB + LG + 0.1, 0]), np.array([LX + 1.6, LB + 2 * LG - 0.1, 0]), angle=-PI / 2, color=PURPLE, stroke_width=5, tip_length=0.2)
    dn = CurvedArrow(np.array([LX + 2.9, LB + LG - 0.1, 0]), np.array([LX + 2.9, LB + 0.1, 0]), angle=-PI / 2, color=PURPLE, stroke_width=5, tip_length=0.2)
    return VGroup(up, heq("a†", 30, PURPLE).next_to(up, RIGHT, buff=0.15), dn, heq("a", 30, PURPLE).next_to(dn, RIGHT, buff=0.15))


@slide("Applied to a state, a lowers the number", "Stepping up and down")
def lad4(s):
    lad = small_ladder()
    dot = Dot([LX, LB + LG + 0.18, 0], radius=0.18, color=BLUE)
    s.add(lad, dot)
    arrs = step_arrows()
    yield [FadeIn(arrs), Succession(dot.animate.shift(UP * LG), dot.animate.shift(DOWN * 2 * LG), dot.animate.shift(UP * LG)),
           FadeIn(left_at(VGroup(heq("a† raises the number by 1", 28, PURPLE), heq("a lowers it by 1", 28, PURPLE)).arrange(DOWN, buff=0.25, aligned_edge=LEFT), 1.4, 1.4))]
    br = VGroup(BraceBetweenPoints([LX - 2.75, LB + LG, 0], [LX - 2.75, LB + 2 * LG, 0], direction=LEFT, color=PURPLE),
                BraceBetweenPoints([LX - 2.75, LB, 0], [LX - 2.75, LB + LG, 0], direction=LEFT, color=PURPLE))
    yield [FadeIn(br), *[FadeIn(heq("ħω", 24, PURPLE).next_to(b, LEFT, buff=0.08)) for b in br],
           FadeIn(left_at(VGroup(lab("each step: the energy changes by", 26, INK), heq("ħω", 30, PURPLE)).arrange(RIGHT, buff=0.2), 1.4, -0.8))]


@slide("That's why they're called ladder operators.", "Ladder operators")
def lad5(s):
    t = clock(s)
    s.add(small_ladder(), step_arrows())
    seq = (1, 2, 1, 0)
    dot = always_redraw(lambda: Dot([LX, LB + LG * seq[int(t.get_value() * 1.1) % 4] + 0.18, 0], radius=0.18, color=BLUE))
    yield [FadeIn(dot)]
    yield [FadeIn(at(pill("ladder operators", PURPLE, 32), 3.4, 0.0), shift=UP * 0.15)]


NX0, NS, NY = -2.2, 2.0, 0.2   # number line: x of 0, units per step, height


def nx(v):
    return NX0 + NS * v


def number_line(lo=-1.6, hi=4.4):
    g = VGroup(Line([nx(lo), NY, 0], [nx(hi), NY, 0], color=MUTED, stroke_width=3))
    for v in range(0, 5):
        g.add(Line([nx(v), NY - 0.12, 0], [nx(v), NY + 0.12, 0], color=MUTED, stroke_width=3), lab(str(v), 24, INK).move_to([nx(v), NY - 0.45, 0]))
    neg = Rectangle(width=nx(0) - nx(lo), height=2.4, stroke_width=0, fill_color=MUTED, fill_opacity=0.15).move_to([(nx(lo) + nx(0)) / 2, NY + 0.4, 0])
    return g, VGroup(neg, at(words("negative: not allowed", 12, 22, RED, align=ORIGIN), (nx(lo) + nx(0)) / 2, NY + 1.1))


def hop(a, b, y=NY, color=PURPLE):
    return CurvedArrow(np.array([nx(a), y + 0.15, 0]), np.array([nx(b), y + 0.15, 0]), angle=PI / 2.2, color=color, stroke_width=4, tip_length=0.16)


@slide("Second, the ladder has a bottom.", "The ladder has a bottom")
def lad6(s):
    line, neg = number_line()
    yield [FadeIn(line), FadeIn(neg), FadeIn(at(lab("values of the number", 22), nx(2), NY - 1.0))]
    dot = Dot([nx(3), NY, 0], radius=0.16, color=BLUE)
    s.add(dot)
    hops = VGroup(*[hop(v, v - 1) for v in (3, 2, 1)])
    yield [Create(hops), Succession(*[dot.animate.move_to([nx(v), NY, 0]) for v in (2, 1, 0)]),
           FadeIn(at(lab("stepping down with a, the number can't go below 0", 26, INK), 0.4, -2.0))]


def down_row(y, vals, ok):
    chips = VGroup(*[at(chip(v, BLUE if (ok or i < 3) else RED, size=26, h=0.7, w=1.3), -3.6 + 2.2 * i, y) for i, v in enumerate(vals)])
    links = VGroup(*[VGroup(arrow(chips[i], chips[i + 1], PURPLE), heq("a", 24, PURPLE).move_to([-2.5 + 2.2 * i, y + 0.38, 0])) for i in range(3)])
    return chips, links


@slide("So stepping down has to stop exactly at zero.", "Where stepping down stops")
def lad7(s):
    c1, l1 = down_row(1.3, ("3", "2", "1", "0"), True)
    yield [FadeIn(left_at(lab("start at 3", 26, INK, True), -7.0, 1.3)), LaggedStart(*[FadeIn(c) for c in c1], lag_ratio=0.25), FadeIn(l1),
           FadeIn(left_at(VGroup(lab("a gives nothing: stop", 24, TEAL, True), check()).arrange(RIGHT, buff=0.2), 3.95, 1.3))]
    c2, l2 = down_row(-0.9, ("2.5", "1.5", "0.5", "−0.5"), False)
    yield [FadeIn(left_at(lab("start at 2.5", 26, INK, True), -7.0, -0.9)), LaggedStart(*[FadeIn(c) for c in c2], lag_ratio=0.25), FadeIn(l2),
           Create(cross(c2[3], RED, 5)), FadeIn(left_at(lab("negative: not allowed", 24, RED, True), 3.95, -0.9))]


@slide("That means the numbers are whole numbers", "Whole numbers")
def lad8(s):
    c1, l1 = down_row(1.3, ("3", "2", "1", "0"), True)
    c2, l2 = down_row(-0.9, ("2.5", "1.5", "0.5", "−0.5"), False)
    s.add(VGroup(left_at(lab("start at 3", 26, INK, True), -7.0, 1.3), c1, l1,
                 left_at(lab("start at 2.5", 26, INK, True), -7.0, -0.9), c2, l2, cross(c2[3], RED, 5)).set_opacity(0.35))
    nums = VGroup(*[num_pill(n, BLUE, 30) for n in ("0", "1", "2", "3")], T("…", 36, BLUE, True)).arrange(RIGHT, buff=0.4)
    yield [FadeIn(at(lab("so the values are whole numbers", 28, INK, True), 0, -2.0))]
    yield [LaggedStart(*[FadeIn(n, scale=1.3) for n in at(nums, 0, -2.9)], lag_ratio=0.2)]


TX = 0.0


def tall_ladder(n=9, gap=0.62, base=-2.9):
    g = VGroup()
    for k in range(n):
        y = base + k * gap
        g.add(Line([TX - 1.1, y, 0], [TX + 1.1, y, 0], color=INK, stroke_width=4).set_opacity(max(0.08, 1 - k / (n - 0.5))))
    g.add(Line([TX - 1.1, base - 0.3, 0], [TX - 1.1, base + (n - 1) * gap + 0.3, 0], color=LINE, stroke_width=3),
          Line([TX + 1.1, base - 0.3, 0], [TX + 1.1, base + (n - 1) * gap + 0.3, 0], color=LINE, stroke_width=3))
    return g


@slide("Third, the ladder has no top.", "No top")
def lad9(s):
    t = clock(s)
    yield [FadeIn(tall_ladder()), FadeIn(left_at(lab("the rungs go on forever", 26, INK), 2.7, 1.0))]
    dot = always_redraw(lambda: Dot([TX, -2.9 + 0.62 * (int(t.get_value() * 1.6) % 7) + 0.16, 0], radius=0.16, color=BLUE))
    ups = VGroup(*[heq("a†", 26, PURPLE).move_to([TX + 1.5, -2.6 + 0.62 * k, 0]) for k in range(6)])
    yield [FadeIn(dot), LaggedStart(*[FadeIn(u) for u in ups], lag_ratio=0.15), FadeIn(left_at(lab("you can always step up", 26, PURPLE, True), 2.7, 0.2))]


RX, RB, RG = 3.4, -3.1, 1.12   # energy ladder: x, zero energy, rung gap
EN = "E  = ħω(n + ½)"   # the gap after E takes a hand-placed subscript n
RUNG_LABELS = ("½ ħω", "3/2 ħω", "5/2 ħω", "7/2 ħω", "9/2 ħω")


def energy_ladder(n=5, with_names=True):
    r = rungs(RX, RB, RG, n, 2.6, INK, 5)
    g = VGroup(r)
    if with_names:
        g.add(VGroup(*[lab(f"n = {k}", 24, INK).next_to(r[k], LEFT, buff=0.3) for k in range(n)]))
        g.add(VGroup(*[heq(RUNG_LABELS[k], 26, INK).next_to(r[k], RIGHT, buff=0.3) for k in range(n)]))
    return g


def en_text(size=44, color=INK):
    t = heq(EN, size, color)
    sub = heq("n", int(size * 0.62), color)
    e = t[0]
    sub.move_to([e.get_right()[0] + sub.width / 2 + 0.04, e.get_bottom()[1] - 0.06 * size / 44, 0])
    return VGroup(t, sub)


def en_eq():
    return VGroup(at(en_text(), -3.6, 1.6), at(lab("n = 0, 1, 2, and so on", 24, INK), -3.6, 0.8))


@slide("So each allowed energy is a whole number", "The allowed energies")
def lad10(s):
    yield [FadeIn(en_eq()), FadeIn(energy_ladder())]
    br = VGroup(*[BraceBetweenPoints([RX + 2.75, RB + (k + 0.5) * RG, 0], [RX + 2.75, RB + (k + 1.5) * RG, 0], direction=RIGHT, color=PURPLE) for k in range(4)])
    yield [FadeIn(br), FadeIn(at(VGroup(lab("evenly spaced, each step", 26, PURPLE, True), heq("ħω", 30, PURPLE)).arrange(RIGHT, buff=0.2), -3.6, -0.6))]


@slide("And the lowest rung isn't at zero.", "The bottom rung")
def lad11(s):
    lad = energy_ladder()
    s.add(en_eq(), lad)
    z = zero_line(RX, RB)
    yield [Create(z[0]), FadeIn(z[1]), lad[0][0].animate.set_color(ORANGE)]
    br = BraceBetweenPoints([RX + 1.45, RB + 0.5 * RG, 0], [RX + 1.45, RB, 0], direction=RIGHT, color=ORANGE)
    yield [FadeOut(lad[2][0]), FadeIn(br), FadeIn(heq("½ ħω", 28, ORANGE).next_to(br, RIGHT, buff=0.12)),
           FadeIn(at(lab("the lowest rung sits at ½ ħω", 26, ORANGE, True), -3.6, -0.6))]


@slide("One step of h-bar omega is called a quantum", "Quanta")
def lad12(s):
    lad = energy_ladder()
    s.add(en_eq(), lad, zero_line(RX, RB))
    dot = Dot([RX, RB + 3.5 * RG + 0.18, 0], radius=0.18, color=BLUE)
    steps = VGroup(*[Line([RX + 1.55, RB + (k + 0.5) * RG + 0.06, 0], [RX + 1.55, RB + (k + 1.5) * RG - 0.06, 0], color=ORANGE, stroke_width=8) for k in range(3)])
    yield [FadeOut(lad[2]), FadeIn(dot), LaggedStart(*[Create(x) for x in steps], lag_ratio=0.3),
           FadeIn(at(heq("one step of ħω: one quantum", 30, ORANGE), -3.6, -0.6))]
    yield [FadeIn(lab("3 quanta", 26, ORANGE, True).next_to(steps, RIGHT, buff=0.25)),
           FadeIn(at(lab("n counts the quanta the spring holds", 26, INK), -3.6, -1.5))]


# ================================================================== how big the steps are
deck.part("How big the steps are")

EB = -2.8          # the bottom rung of each ladder
U = 0.36           # a typical bump at room temperature, in screen units
VX, BX, QX = -4.6, -0.7, 3.8


def vib_ladder():
    return VGroup(Line([VX - 1.2, EB, 0], [VX + 1.2, EB, 0], color=ORANGE, stroke_width=7),
                  Line([VX - 1.2, EB + 13.8 * U, 0], [VX + 1.2, EB + 13.8 * U, 0], color=ORANGE, stroke_width=7),
                  at(lab("vibration", 26, ORANGE, True), VX, EB - 0.4))


def bump_bar():
    r = Rectangle(width=1.1, height=U, stroke_width=0, fill_color=MUTED, fill_opacity=0.6).move_to([BX, EB + U / 2, 0])
    return VGroup(r, at(lab("a typical bump", 24, INK), BX, EB - 0.4))


def tumble_ladder():
    g = VGroup(*[Line([QX - 1.2, EB + 0.05 * J * (J + 1) * U, 0], [QX + 1.2, EB + 0.05 * J * (J + 1) * U, 0], color=PURPLE, stroke_width=3)
                 for J in range(14)])
    return VGroup(g, at(lab("tumbling", 26, PURPLE, True), QX, EB - 0.4))


def base_line():
    return hline(-6.9, 6.9, EB, LINE, 3)


def vib_brace():
    b = BraceBetweenPoints([VX + 1.35, EB + 13.8 * U, 0], [VX + 1.35, EB, 0], direction=RIGHT, color=ORANGE)
    return VGroup(b, left_at(words("one step: about 14 times a typical bump", 16, 24, ORANGE), VX + 2.1, EB + 6.9 * U))


@slide("How big the steps are.", "Back to the heat puzzle")
def st1(s):
    stack = heat_stack(0.12)
    yield [FadeIn(heat_legend()), FadeIn(heat_axis()), FadeIn(stack), FadeIn(measured_bar())]
    q = at(T("?", 44, ORANGE, True), SX_, HBASE + 6 * HB)
    yield [FadeIn(q, scale=1.4), FadeIn(at(lab("now we can solve it", 28, ORANGE, True), 4.2, 1.6))]


@slide("For hydrogen chloride, one step on the ladder is big.", "One vibration step")
def st2(s):
    s.add(base_line())
    yield [FadeIn(vib_ladder()), FadeIn(at(lab("the HCl bond's ladder: one step", 24, ORANGE), VX, EB + 13.8 * U + 0.4))]
    yield [GrowFromEdge(bump_bar()[0], DOWN), FadeIn(bump_bar()[1]), FadeIn(vib_brace())]


@slide("The bond can only take a whole step", "Whole steps only")
def st3(s):
    t = clock(s)
    s.add(base_line(), vib_ladder(), bump_bar(), vib_brace(), at(lab("the HCl bond's ladder: one step", 24, ORANGE), VX, EB + 13.8 * U + 0.4))
    dot = always_redraw(lambda: Dot([VX, EB + 0.16 + U * abs(np.sin(2.6 * t.get_value())), 0], radius=0.16, color=BLUE))
    yield [FadeIn(dot), FadeIn(at(words("a whole step or nothing, never part of one", 20, 26, INK, align=ORIGIN), 4.2, 1.4))]
    yield [FadeIn(at(words("bumps that big: about 1 in a million", 20, 26, ORANGE, align=ORIGIN), 4.2, -0.2))]


@slide("So the bond almost never gets kicked up a rung.", "Stuck on the bottom rung")
def st4(s):
    s.add(base_line(), vib_ladder(), bump_bar(), vib_brace(), at(lab("the HCl bond's ladder: one step", 24, ORANGE), VX, EB + 13.8 * U + 0.4))
    dot = Dot([VX, EB + 0.16, 0], radius=0.16, color=BLUE)
    yield [FadeIn(dot), Flash(dot, color=ORANGE), FadeIn(at(lab("it stays on the bottom rung", 26, INK), 4.0, 1.9))]
    yield [FadeIn(at(lab("so it takes no heat", 26, ORANGE, True), 4.0, 1.2))]
    mini = VGroup(*[Rectangle(width=1.2, height=n * 0.3, stroke_color=WHITE, stroke_width=2, fill_color=c, fill_opacity=o)
                    for n, c, o in ((3, MUTED, 0.75), (2, PURPLE, 0.75), (2, ORANGE, 0.12))]).arrange(UP, buff=0)
    mini.move_to([3.4, -1.25, 0])
    yield [FadeIn(mini), FadeIn(VGroup(lab("the missing share", 24, ORANGE, True), check()).arrange(RIGHT, buff=0.2).next_to(mini[2], RIGHT, buff=0.25))]


def steps_base(s):
    s.add(base_line(), vib_ladder(), bump_bar(), vib_brace())


@slide("Tumbling comes in steps too.", "The tumbling ladder")
def st5(s):
    steps_base(s)
    yield [FadeIn(tumble_ladder())]
    a = Arrow([QX + 2.6, EB + 1.55, 0], [QX + 1.3, EB + 0.08, 0], buff=0, color=PURPLE, stroke_width=4, tip_length=0.16)
    yield [GrowArrow(a), FadeIn(at(words("first step: about a tenth of a bump", 13, 22, PURPLE, align=ORIGIN), QX + 2.6, EB + 2.25))]


@slide("So bumps move molecules up and down the tumbling", "Tumbling takes its share")
def st6(s):
    t = clock(s)
    steps_base(s)
    s.add(tumble_ladder())
    walk = (0, 1, 2, 3, 2, 3, 4, 3, 2, 1, 2, 1)
    dot = always_redraw(lambda: Dot([QX, EB + 0.05 * (J := walk[int(t.get_value() * 2.2) % len(walk)]) * (J + 1) * U + 0.14, 0], radius=0.14, color=BLUE))
    yield [FadeIn(dot), FadeIn(at(lab("bumps move it up and down", 24, PURPLE), QX, 2.3))]
    yield [FadeIn(at(VGroup(words("tumbling takes its full share of heat", 18, 24, TEAL), check()).arrange(RIGHT, buff=0.2), QX, 1.35))]


def mini_ladder(x, gap, color, n=None, top=1.6, bottom=-2.4, w=2.2, width=4):
    n = n or int((top - bottom) / gap) + 1
    return VGroup(*[Line([x - w / 2, bottom + k * gap, 0], [x + w / 2, bottom + k * gap, 0], color=color, stroke_width=width) for k in range(n)])


LADX = (-4.6, 0.0, 4.6)


@slide("Here's why the steps are so different.", "A ladder for every motion")
def st7(s):
    v = mini_ladder(LADX[0], 4.0, ORANGE, 2, width=6)
    r = mini_ladder(LADX[1], 0.3, PURPLE, width=3)
    yield [FadeIn(v), FadeIn(r), FadeIn(at(lab("vibrating", 26, ORANGE, True), LADX[0], -2.9)), FadeIn(at(lab("tumbling", 26, PURPLE, True), LADX[1], -2.9))]
    f = mini_ladder(LADX[2], 0.05, MUTED, width=1.5)
    yield [FadeIn(f), FadeIn(at(lab("flying around", 26, MUTED, True), LADX[2], -2.9)),
           FadeIn(at(lab("every motion has its own ladder", 28, INK, True), 0, 2.3))]


@slide("Its rungs are spaced by about h-bar times", "What sets the step size")
def st8(s):
    yield [FadeIn(at(heq("step ≈ ħ × how fast the motion repeats", 36, INK), 0, 1.8))]
    a = mini_ladder(-3.6, 2.2, ORANGE, 2, top=0.3, bottom=-1.9, width=6)
    b = mini_ladder(3.6, 0.27, PURPLE, top=0.3, bottom=-1.9, width=3)
    yield [FadeIn(a), FadeIn(at(lab("fast motion: big steps", 28, ORANGE, True), -3.6, -2.6)),
           FadeIn(b), FadeIn(at(lab("slow motion: small steps", 28, PURPLE, True), 3.6, -2.6))]


@slide("Vibrating is fast.", "Vibrating")
def st9(s):
    t = clock(s)
    mol = always_redraw(lambda: hcl([-2.6, 0.4], 3.2 + 0.25 * np.cos(14 * t.get_value()), 1.7, spring=ORANGE, width=5))
    yield [FadeIn(mol), FadeIn(at(lab("fast", 30, ORANGE, True), -2.6, 2.1))]
    yield [FadeIn(at(lab("stiffness", 24, INK), -2.6, -0.45)), FadeIn(at(lab("mass", 24, INK), -0.9, 1.3)),
           FadeIn(at(words("a spring rings at a rate set by its stiffness and its mass", 22, 26, INK, align=ORIGIN), 4.4, 0.4))]


@slide("The bond is very stiff, and the hydrogen atom", "Vibrating")
def st10(s):
    t = clock(s)
    mol = always_redraw(lambda: hcl([-3.4, 0.6], 3.0 + 0.12 * np.cos(14 * t.get_value()), 1.7, spring=ORANGE, width=9))
    yield [FadeIn(mol), FadeIn(at(lab("very stiff bond", 24, ORANGE, True), -3.4, -0.4)), FadeIn(at(lab("very light hydrogen", 24, INK), -1.9, 1.7))]
    lad = mini_ladder(4.4, 3.0, ORANGE, 2, top=0.8, bottom=-2.2, width=6)
    yield [FadeIn(at(words("almost 90 trillion times a second", 18, 26, ORANGE, align=ORIGIN), -3.4, -2.0)),
           FadeIn(lad), FadeIn(at(lab("big steps", 26, ORANGE, True), 4.4, -2.75))]


@slide("Tumbling is slow.", "Tumbling")
def st11(s):
    t = clock(s, 0.5)
    mol = always_redraw(lambda: hcl([-3.0, 0.2], 2.0, 1.2, spring=INK, width=3, angle=t.get_value()))
    yield [FadeIn(mol), FadeIn(at(lab("slow", 30, PURPLE, True), -3.0, 2.2))]
    ring = DashedVMobject(Circle(radius=1.35, color=PURPLE, stroke_width=2).move_to([-3.0, 0.2, 0]), num_dashes=36)
    yield [Create(ring), FadeIn(at(words("nothing pulls it back to a preferred angle, so it has no ringing rate of its own", 26, 26, INK, align=ORIGIN), 3.8, 0.2))]


@slide("Its slowest spin is set by how hard", "Tumbling")
def st12(s):
    t = clock(s, 0.5)
    s.add(always_redraw(lambda: hcl([-3.6, 0.6], 2.0, 1.2, spring=INK, width=3, angle=t.get_value())))
    turn = CurvedArrow(np.array([-2.2, -0.5, 0]), np.array([-2.0, 1.7, 0]), angle=PI / 2, color=PURPLE, stroke_width=5, tip_length=0.2)
    yield [Create(turn), FadeIn(at(lab("how hard the whole molecule is to turn", 24, PURPLE), -3.6, -1.4))]
    lad = mini_ladder(4.0, 0.3, PURPLE, top=1.0, bottom=-2.2, width=3)
    yield [FadeIn(at(words("about 100 times slower than the vibration", 20, 26, PURPLE, align=ORIGIN), -3.6, -2.4)),
           FadeIn(lad), FadeIn(at(lab("small steps", 26, PURPLE, True), 4.0, -2.75))]


BOXC, BOXW, BOXH = (-2.2, 0.0), 8.6, 3.6


def flying(t):
    def draw():
        u = tri(0.12 * t.get_value())
        x = BOXC[0] - BOXW / 2 + 0.8 + (BOXW - 1.6) * u
        return hcl([x, BOXC[1]], 0.8, 0.6, spring=INK, width=2, angle=0.6 * t.get_value())
    return always_redraw(draw)


@slide("Flying around is slower still.", "Flying around")
def st13(s):
    t = clock(s)
    yield [FadeIn(gas_box(BOXC, BOXW, BOXH)), FadeIn(flying(t)), FadeIn(at(lab("a container", 24, MUTED), BOXC[0], -2.15))]
    da = DoubleArrow([BOXC[0] - BOXW / 2 + 0.2, 2.15, 0], [BOXC[0] + BOXW / 2 - 0.2, 2.15, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.16)
    yield [GrowFromCenter(da), FadeIn(at(words("the only repeat: wall to wall, which takes ages", 16, 26, INK, align=ORIGIN), 5.3, 0.0))]


@slide("Its steps are far too small to matter.", "Flying around")
def st14(s):
    t = clock(s)
    s.add(gas_box(BOXC, BOXW, BOXH), flying(t), at(lab("a container", 24, MUTED), BOXC[0], -2.15))
    lad = mini_ladder(5.4, 0.05, MUTED, top=1.6, bottom=-1.6, w=1.8, width=1.5)
    yield [FadeIn(lad)]
    yield [FadeIn(at(words("steps far too small to matter", 14, 26, INK, align=ORIGIN), 5.4, -2.4))]


TEMP_X0, TEMP_X1 = -2.0, 6.6


def temp_scale():
    g = VGroup(axis_arrow((-2.4, -3.0), (-2.4, 2.5)), lab("energy", 22).move_to([-1.75, 2.45, 0]))
    rows = ((1.6, ORANGE, "vibration step"), (-1.6, PURPLE, "tumbling step"), (-2.75, MUTED, "flying step"))
    for y, c, name in rows:
        g.add(Line([TEMP_X0, y, 0], [TEMP_X0 + 3.0, y, 0], color=c, stroke_width=6), left_at(lab(name, 24, c, True), TEMP_X0 + 3.3, y))
    g.add(at(lab("not to scale", 22), 5.6, -3.3))
    return g


def temp_line(y=-0.2):
    return VGroup(DashedLine([-2.3, y, 0], [TEMP_X1, y, 0], color=INK, stroke_width=3), left_at(lab("room temperature", 24, INK), 4.3, y + 0.32))


@slide("Room temperature happens to sit between", "Where room temperature sits")
def st15(s):
    yield [FadeIn(temp_scale()), Create(temp_line()[0]), FadeIn(temp_line()[1])]
    yield [FadeIn(left_at(lab("frozen: only the vibration", 24, ORANGE, True), -6.9, 1.6)),
           FadeIn(left_at(lab("takes heat", 24, PURPLE), -6.9, -1.6))]


@slide("Cool the gas far enough", "Colder and hotter")
def st16(s):
    s.add(temp_scale())
    line, room = temp_line()
    s.add(line, room)
    cold_tag = left_at(lab("cold gas", 24, INK), 4.3, -2.2 + 0.32)
    hot_tag = left_at(lab("thousands of degrees", 24, INK), 4.3, 2.15 + 0.32)
    cold = left_at(lab("cold: tumbling freezes too", 24, PURPLE, True), -6.9, -1.6)
    yield [line.animate.shift(DOWN * 2.0), FadeOut(room), FadeIn(cold_tag), FadeIn(cold)]
    yield [line.animate.shift(UP * 4.35), FadeOut(cold_tag), FadeIn(hot_tag), cold.animate.set_opacity(0.35),
           FadeIn(left_at(lab("hot: the vibration thaws", 24, ORANGE, True), -6.9, 1.6))]


@slide("Chapter one's spring is the opposite case.", "Chapter 1's spring")
def st17(s):
    t = clock(s)
    yield [FadeIn(rig_static(-6.8, 0.3, 5.8, 0.8)), FadeIn(always_redraw(lambda: rig_moving(-6.8, 0.3, 3.0, 1.2 * np.cos(SPIN * t.get_value()), 0.8)))]
    bar = Rectangle(width=1.4, height=4.6, stroke_width=0, fill_color=BLUE, fill_opacity=0.3).move_to([2.2, -0.6, 0])
    sliver = Line([1.5, 1.72, 0], [2.9, 1.72, 0], color=ORANGE, stroke_width=2)
    yield [GrowFromEdge(bar, DOWN), FadeIn(at(lab("its energy", 24, BLUE, True), 2.2, -3.2)), Create(sliver),
           FadeIn(left_at(words("one step: far too thin to draw", 14, 24, ORANGE), 3.3, 1.72))]


@slide("Adding or removing one quantum changes", "Adding one quantum")
def st18(s):
    yield [FadeIn(at(lab("one quantum changes its energy by", 28, INK), 0, 1.4)), FadeIn(at(T("one part in 10³⁴", 52, ORANGE, True), 0, 0.3))]
    yield [FadeIn(at(lab("nobody could ever measure that", 28, INK), 0, -1.4))]


@slide("So its energy looks perfectly smooth", "Why chapter 1 missed the ladder")
def st19(s):
    lines = VGroup(*[Line([-1.6, -2.6 + 0.045 * k, 0], [1.6, -2.6 + 0.045 * k, 0], color=BLUE, stroke_width=1.2) for k in range(110)])
    smooth = Rectangle(width=3.2, height=0.045 * 109, stroke_width=0, fill_color=BLUE, fill_opacity=0.35).move_to(lines)
    yield [FadeIn(lines, lag_ratio=0.01), FadeIn(at(lab("rungs packed this close...", 26, INK), -4.6, 0.6))]
    yield [ReplacementTransform(lines, smooth), FadeIn(at(lab("...look perfectly smooth", 26, INK), 4.6, 0.6))]


# ================================================================== the lowest rung
deck.part("The lowest rung")

PX = (-3.6, 3.6)


@slide("The lowest rung.", "Sitting still")
def low1(s):
    heads = VGroup(at(T("classical spring", 28, MUTED, True), PX[0], 2.2), at(T("quantum spring", 28, INK, True), PX[1], 2.2))
    bowls = VGroup(*[bowl(x, -1.6, 2.2, 2.6, MUTED) for x in PX])
    yield [FadeIn(heads), Create(bowls)]
    b0 = ball_in_bowl(PX[0], -1.6, 0.0, 2.2, 2.6, 0.2)
    yield [FadeIn(b0), FadeIn(at(lab("perfectly still: zero energy", 26, INK), PX[0], -2.5))]
    b1 = ball_in_bowl(PX[1], -1.6, 0.0, 2.2, 2.6, 0.2)
    yield [FadeIn(b1), Create(cross(Square(0.9).move_to(b1), RED, 6)), FadeIn(at(lab("it can't", 26, RED, True), PX[1], -2.5))]


@slide("Sitting still at the bottom would mean", "Both sharp at once")
def low2(s):
    c = (-3.0, -0.4)
    d = Dot([c[0], c[1], 0], radius=0.14, color=BLUE)
    yield [FadeIn(plane(c, 2.1)), FadeIn(d), FadeIn(at(words("sitting still: position exactly 0 and momentum exactly 0", 26, 26, INK, align=ORIGIN), 3.6, 1.2))]
    blob = VGroup(*[Circle(radius=r, stroke_width=0, fill_color=TEAL, fill_opacity=0.13).move_to([c[0], c[1], 0]) for r in (0.35, 0.6, 0.85)])
    yield [Create(cross(Square(0.5).move_to(d), RED, 5)), FadeIn(blob),
           FadeIn(at(words("chapter 2: never both sharp at once", 20, 26, TEAL, align=ORIGIN), 3.6, -1.0))]


@slide("So even on its lowest rung, the spring keeps", "Energy on the lowest rung")
def low3(s):
    lad = energy_ladder(4, with_names=False)
    lad.shift(LEFT * 5.6)
    z = zero_line(RX - 5.6, RB)
    lad[0][0].set_color(ORANGE)
    br = BraceBetweenPoints([RX - 5.6 + 1.45, RB + 0.5 * RG, 0], [RX - 5.6 + 1.45, RB, 0], direction=RIGHT, color=ORANGE)
    yield [FadeIn(lad), FadeIn(z), FadeIn(br), FadeIn(heq("½ ħω", 30, ORANGE).next_to(br, RIGHT, buff=0.12)),
           FadeIn(at(words("even on the lowest rung, a little energy remains", 22, 28, INK, align=ORIGIN), 3.6, 0.8))]
    yield [FadeIn(at(pill("the zero-point energy", ORANGE, 30), 3.6, -0.8), shift=UP * 0.15)]


GY = -2.3   # baseline of the bell curves


def bell_panel(x, name, w=1.0, sx=1.15):
    ax = axis_arrow((x - 3.0, GY), (x + 3.1, GY))
    return VGroup(ax, lab(name, 24, INK).move_to([x, GY - 0.35, 0])), area(bell(0, w), -2.5, 2.5, x, GY, sx, 2.9)


@slide("Plot where the spring on its lowest rung", "Where the spring is likely to be")
def low4(s):
    ax0, b0 = bell_panel(PX[0], "position")
    yield [FadeIn(ax0), Create(b0), FadeIn(at(lab("chance of each position", 24, TEAL, True), PX[0], 1.3))]
    ax1, b1 = bell_panel(PX[1], "momentum")
    yield [FadeIn(ax1), Create(b1), FadeIn(at(lab("chance of each momentum", 24, TEAL, True), PX[1], 1.3))]


def spread_marks():
    g = VGroup()
    for x in PX:
        y = GY + 2.9 * np.exp(-0.5)
        g.add(DoubleArrow([x - 1.15 * 0.7071, y, 0], [x + 1.15 * 0.7071, y, 0], buff=0, color=ORANGE, stroke_width=4, tip_length=0.14),
              lab("spread", 22, ORANGE).move_to([x + 1.6, y + 0.3, 0]))
    return g


@slide("The two spreads are as small together", "The two spreads")
def low5(s):
    for x, n in zip(PX, ("position", "momentum")):
        ax, b = bell_panel(x, n)
        s.add(ax, b, at(lab(f"chance of each {n}", 24, TEAL, True), x, 1.3))
    yield [FadeIn(spread_marks()), FadeIn(at(lab("as small together as the uncertainty rule allows", 26, INK), 0, 2.2))]
    a = Rectangle(width=2.6, height=0.4, stroke_width=0, fill_color=MUTED, fill_opacity=0.45).move_to([-1.3, -3.55, 0])
    b = Rectangle(width=2.6, height=0.4, stroke_width=0, fill_color=INK, fill_opacity=0.6).move_to([1.3, -3.55, 0])
    yield [FadeIn(a), FadeIn(b), FadeIn(lab("from moving", 22, INK).next_to(a, LEFT, buff=0.2)), FadeIn(lab("from stretching", 22, INK).next_to(b, RIGHT, buff=0.2)),
           FadeIn(at(heq("½ ħω, split evenly", 24, INK), 0, -3.1))]


@slide("For chapter one's spring, the spread is about five", "How big the spread is")
def low6(s):
    yield [FadeIn(at(lab("chapter 1's spring", 28, INK, True), 0, 2.0)), FadeIn(at(T("spread ≈ 5 × 10⁻¹⁸ m", 44, ORANGE, True), 0, 1.1))]
    nuc = Circle(radius=1.5, stroke_color=MUTED, stroke_width=3, fill_color=MUTED, fill_opacity=0.12).move_to([-2.0, -1.4, 0])
    tiny = Dot([-2.0, -1.4, 0], radius=0.02, color=ORANGE)
    yield [FadeIn(nuc), FadeIn(tiny), FadeIn(at(lab("an atomic nucleus", 24, MUTED), -2.0, -3.2)),
           FadeIn(left_at(words("the spread: a few hundred times smaller than this", 20, 26, ORANGE), 0.6, -1.4))]


@slide("For a molecule's bond, it's a few percent", "A bond's blurred length")
def low7(s):
    c, d = (-0.6, 0.3), 5.0
    mol = hcl(c, d, 1.6, spring=ORANGE, width=4)
    hx = c[0] + d / 2
    blur = area(bell(0, 1.0), -2.5, 2.5, hx, -1.1, 0.22, 1.1, n=80)
    bl = BraceBetweenPoints([c[0] - d / 2, 1.5, 0], [hx, 1.5, 0], direction=UP, color=INK)
    yield [FadeIn(mol), FadeIn(bl), FadeIn(lab("the bond's length", 24, INK).next_to(bl, UP, buff=0.1)), FadeIn(blur),
           FadeIn(at(words("the hydrogen's position is spread by a few percent of the bond's length", 34, 24, TEAL, align=ORIGIN), -0.6, -2.0))]
    yield [FadeIn(at(lab("even near absolute zero, never perfectly sharp", 26, INK, True), -0.3, -3.1))]


# ================================================================== how the quantum spring moves
deck.part("How the quantum spring moves")


def mix_density(c0, c1, phase):
    """Chance of each position for c0 on rung 0 and c1 on rung 1, with their phase gap."""
    k = 2 * np.sqrt(2) * c0 * c1 * np.cos(phase)
    return lambda u: np.exp(-u * u) * (c0 * c0 + 2 * c1 * c1 * u * u + k * u)


@slide("How the quantum spring moves.", "One rung on its own")
def mv1(s):
    t = clock(s)
    ax = axis_arrow((-6.8, -2.2), (-0.2, -2.2))
    b = area(bell(0, 1.0), -2.6, 2.6, -3.5, -2.2, 1.15, 3.0)
    yield [FadeIn(ax), FadeIn(lab("position", 22).move_to([-3.5, -2.55, 0])), Create(b), FadeIn(at(lab("one rung: chance of each position", 24, TEAL, True), -3.5, 1.4))]
    yield [FadeIn(always_redraw(lambda: phasor([3.6, 0.0], -SPIN * t.get_value(), 1.3, BLUE, width=6))),
           FadeIn(at(lab("its phase turns", 26, BLUE, True), 3.6, 1.8))]
    yield [FadeIn(at(VGroup(lab("nothing you could measure changes", 24, TEAL), check()).arrange(RIGHT, buff=0.2), 3.6, -2.2))]


@slide("But the spring doesn't have to sit on a single rung.", "Not just one rung")
def mv2(s):
    r = rungs(-3.6, -2.6, 1.8, 3, 3.0, INK, 5, start=0)
    names = VGroup(*[lab(f"rung {k}", 24, INK).next_to(r[k], LEFT, buff=0.3) for k in range(3)])
    dots = VGroup(Dot([-3.6, -2.6 + 0.18, 0], radius=0.18, color=BLUE).set_opacity(0.6), Dot([-3.6, -0.8 + 0.18, 0], radius=0.18, color=BLUE).set_opacity(0.6))
    yield [FadeIn(r), FadeIn(names), FadeIn(dots), FadeIn(at(lab("partly on one rung, partly on another?", 26, INK), -3.4, 1.85))]
    c = np.array([3.6, -0.6, 0])
    dial = VGroup(Circle(radius=1.3, color=LINE, stroke_width=2).move_to(c), DashedLine(c, c + UP * 1.3, color=MUTED, stroke_width=2),
                  Arrow(c, c + 1.3 * np.array([np.sin(np.radians(60)), np.cos(np.radians(60)), 0]), buff=0, color=BLUE, stroke_width=6, tip_length=0.2))
    yield [FadeIn(dial), FadeIn(at(lab("chapter 2's tilted spin:", 24, INK), 3.6, 1.55)), FadeIn(at(lab("partly up, partly down", 24, BLUE, True), 3.6, -2.4))]


def two_rungs(x=-3.8):
    r = rungs(x, -1.8, 2.2, 2, 2.6, INK, 5, start=0)
    names = VGroup(*[lab(f"rung {k}", 24, INK).next_to(r[k], LEFT, buff=0.3) for k in range(2)])
    return VGroup(r, names)


@slide("In the same way, the spring's state can be partly", "Partly on two rungs")
def mv3(s):
    lad = two_rungs()
    amps = VGroup(phasor([-1.6, -1.7], 0.6, 0.7, frac=np.sqrt(0.5)), phasor([-1.6, 0.5], 1.9, 0.7, frac=np.sqrt(0.5)))
    yield [FadeIn(lad), LaggedStart(*[FadeIn(a) for a in amps], lag_ratio=0.3), FadeIn(at(lab("an amplitude on each rung", 24, BLUE, True), -2.8, 1.7))]
    yield [FadeIn(at(words("still one spring, in one state", 16, 28, INK, align=ORIGIN), 3.8, -0.6))]


def chance_bars(p, x0=1.8, x1=4.8, base=-2.3, hmax=3.4):
    """Chance bars for rung 0 and rung 1, with p the chance of rung 0."""
    g = VGroup()
    for x, v, name in ((x0, p, "rung 0 energy"), (x1, 1 - p, "rung 1 energy")):
        h = max(hmax * v, 0.02)
        g.add(Rectangle(width=1.3, height=h, stroke_width=0, fill_color=TEAL, fill_opacity=0.75).move_to([x, base + h / 2, 0]))
    return g


def chance_axis(x0=1.8, x1=4.8, base=-2.3):
    return VGroup(hline(x0 - 1.1, x1 + 1.1, base, MUTED, 3), lab("rung 0 energy", 22, INK).move_to([x0, base - 0.35, 0]),
                  lab("rung 1 energy", 22, INK).move_to([x1, base - 0.35, 0]))


@slide("Measure its energy, and you get one rung's", "Measuring the energy")
def mv4(s):
    p = ValueTracker(0.5)
    s.add(p, two_rungs(), always_redraw(lambda: VGroup(phasor([-1.6, -1.7], 0.6, 0.7, frac=np.sqrt(p.get_value())),
                                                       phasor([-1.6, 0.5], 1.9, 0.7, frac=np.sqrt(1 - p.get_value())))))
    bars = always_redraw(lambda: chance_bars(p.get_value()))
    def pcts(v):
        return VGroup(T(f"{round(100 * v)}%", 26, TEAL, True).move_to([1.8, -2.3 + 3.4 * v + 0.3, 0]),
                      T(f"{round(100 * (1 - v))}%", 26, TEAL, True).move_to([4.8, -2.3 + 3.4 * (1 - v) + 0.3, 0]))
    pct = pcts(0.5)
    yield [FadeIn(chance_axis()), FadeIn(bars), FadeIn(pct), FadeIn(at(lab("measure the energy: one rung or the other", 24, INK), 3.3, 2.2))]
    yield [FadeIn(at(lab("the mix needn't be equal", 24, INK), 3.3, 1.55))]
    yield [p.animate.set_value(0.75), Transform(pct, pcts(0.75)), FadeIn(at(lab("any split that adds up to 100%", 24, TEAL), 3.3, -3.25)),
           FadeIn(at(lab("bigger amplitude, bigger chance", 22, BLUE), -2.8, -2.6))]


@slide("A mix of two rungs swings.", "A two-rung mix swings")
def mv5(s):
    t = clock(s)
    X, Y = -3.4, -2.2
    ax = axis_arrow((-6.9, Y), (0.1, Y))
    dens = always_redraw(lambda: area(mix_density(0.7071, 0.7071, SPIN * t.get_value()), -3.0, 3.0, X, Y, 1.1, 2.2, n=90))
    mean = always_redraw(lambda: Dot([X + 1.1 * 0.7071 * np.cos(SPIN * t.get_value()), Y, 0], radius=0.13, color=BLUE))
    yield [FadeIn(ax), FadeIn(lab("position", 22).move_to([X, Y - 0.35, 0])), FadeIn(dens), FadeIn(mean),
           FadeIn(at(lab("50/50 mix of rungs 0 and 1", 24, TEAL, True), X, 1.4)), FadeIn(at(lab("average position", 22, BLUE), X, Y - 0.75))]
    ph0 = always_redraw(lambda: phasor([2.0, 0.0], -0.5 * SPIN * t.get_value(), 1.0))
    ph1 = always_redraw(lambda: phasor([5.0, 0.0], -1.5 * SPIN * t.get_value(), 1.0))
    yield [FadeIn(ph0), FadeIn(ph1), FadeIn(at(lab("rung 0", 24, INK), 2.0, -1.4)), FadeIn(at(lab("rung 1", 24, INK), 5.0, -1.4)),
           FadeIn(at(lab("phases turn at different rates", 24, BLUE, True), 3.5, 1.5))]


@slide("The gap between them grows steadily", "The average goes round")
def mv6(s):
    t = clock(s)
    s.add(always_redraw(lambda: phasor([-5.4, 0.9], -0.5 * SPIN * t.get_value(), 0.85)),
          always_redraw(lambda: phasor([-2.6, 0.9], -1.5 * SPIN * t.get_value(), 0.85)),
          at(lab("rung 0", 22, INK), -5.4, -0.2), at(lab("rung 1", 22, INK), -2.6, -0.2))
    gap = always_redraw(lambda: phasor([-4.0, -1.9], -SPIN * t.get_value(), 0.85, ORANGE))
    c, r = (3.4, -0.4), 1.9
    dot = always_redraw(lambda: Dot([c[0] + r * np.cos(-SPIN * t.get_value()), c[1] + r * np.sin(-SPIN * t.get_value()), 0], radius=0.16, color=BLUE))
    yield [FadeIn(gap), FadeIn(at(lab("the gap grows steadily", 22, ORANGE, True), -4.0, -3.15)),
           FadeIn(plane(c, r)), FadeIn(orbit(c, r)), FadeIn(dot), FadeIn(at(lab("the average goes round", 24, BLUE, True), 3.4, 2.35))]
    yield [FadeIn(at(lab("at exactly the classical spring's rate", 24, INK), 3.4, -3.3))]


MIX3 = ((0.5, "50/50"), (0.75, "75/25"), (0.99, "almost all rung 0"))


def swing_panel(k, t, x):
    p, name = MIX3[k]
    R = 1.45 * 2 * np.sqrt(p * (1 - p))
    c = (x, -1.3)
    bars = VGroup(*[Rectangle(width=0.5, height=max(1.1 * v, 0.02), stroke_width=0, fill_color=TEAL, fill_opacity=0.75)
                    .move_to([x - 0.35 + 0.7 * j, 1.0 + 1.1 * v / 2, 0]) for j, v in enumerate((p, 1 - p))])
    dot = always_redraw(lambda: Dot([c[0] + R * np.cos(-SPIN * t.get_value()), c[1] + R * np.sin(-SPIN * t.get_value()), 0], radius=0.14, color=BLUE))
    return VGroup(bars, hline(x - 0.8, x + 0.8, 1.0, MUTED, 2), at(lab(name, 24, TEAL, True), x, 2.45),
                  Circle(radius=max(R, 0.05), color=LINE, stroke_width=3).move_to([c[0], c[1], 0]), dot)


@slide("The more even the mix, the bigger the swing.", "How big the swing is")
def mv7(s):
    t = clock(s)
    xs = (-4.6, 0.0, 4.6)
    yield [FadeIn(swing_panel(0, t, xs[0])), FadeIn(swing_panel(1, t, xs[1])), FadeIn(at(lab("more even mix, bigger swing", 26, INK, True), 0, -3.4))]
    yield [FadeIn(swing_panel(2, t, xs[2]))]


@slide("Any mixture of rungs does this.", "Any mix of rungs")
def mv8(s):
    t = clock(s)
    x, base, gap = -4.2, -2.6, 1.0
    r = rungs(x, base, gap, 5, 2.2, INK, 5, start=0)
    names = VGroup(*[lab(f"rung {k}", 22, INK).next_to(r[k], LEFT, buff=0.25) for k in range(5)])
    phs = VGroup(*[always_redraw(lambda k=k: phasor([x + 2.0, base + k * gap + 0.05], -(k + 0.5) * 0.7 * t.get_value(), 0.4, width=4)) for k in range(5)])
    yield [FadeIn(r), FadeIn(names), FadeIn(phs), FadeIn(at(lab("any mix of rungs swings", 26, INK, True), 3.6, 2.2))]
    br = VGroup(*[BraceBetweenPoints([x + 2.65, base + (k + 1) * gap, 0], [x + 2.65, base + k * gap, 0], direction=RIGHT, color=PURPLE) for k in range(4)])
    yield [FadeIn(br), *[FadeIn(heq("ħω", 22, PURPLE).next_to(b, RIGHT, buff=0.08)) for b in br],
           FadeIn(at(words("evenly spaced rungs: every neighbouring phase gap grows at the same rate", 24, 26, INK, align=ORIGIN), 3.8, 0.0))]


@slide("That means the averages always follow", "Following chapter 1")
def mv9(s):
    t = clock(s)
    c, r = (-3.4, -0.4), 1.9
    dot = always_redraw(lambda: Dot([c[0] + r * np.cos(-SPIN * t.get_value()), c[1] + r * np.sin(-SPIN * t.get_value()), 0], radius=0.16, color=BLUE))
    yield [FadeIn(plane(c, r)), FadeIn(orbit(c, r)), FadeIn(dot), FadeIn(at(lab("the averages", 24, BLUE, True), c[0], 2.35)),
           FadeIn(rig_static(1.0, -0.4, 6.0, 0.7)), FadeIn(always_redraw(lambda: rig_moving(1.0, -0.4, 3.2, 1.3 * np.cos(SPIN * t.get_value()), 0.7)))]
    yield [FadeIn(at(VGroup(words("they follow chapter 1's equations exactly", 22, 26, TEAL), check()).arrange(RIGHT, buff=0.2), 4.0, 1.6))]


# ================================================================== what we see is a coherent state
deck.part("What we see is a coherent state")


@slide("What we see is a coherent state.", "Pull and let go")
def co1(s):
    t = clock(s, 0.0)
    a = ValueTracker(0.0)
    s.add(a)
    xw, y, rest = -5.4, 0.6, 4.4
    base = rig_static(xw, y, 9.4, 1.0)
    mv = always_redraw(lambda: rig_moving(xw, y, rest, a.get_value() * np.cos(SPIN * t.get_value()), 1.0))
    rl = DashedLine([xw + rest, y - 0.9, 0], [xw + rest, y + 0.9, 0], color=MUTED, stroke_width=2)
    yield [FadeIn(base), FadeIn(mv), FadeIn(rl), FadeIn(at(lab("at rest", 22, MUTED), xw + rest, y + 1.15))]
    br = BraceBetweenPoints([xw + rest, y - 0.75, 0], [xw + rest + 2.0, y - 0.75, 0], direction=DOWN, color=ORANGE)
    one = at(lab("1 m", 28, ORANGE, True), xw + rest + 1.0, y - 1.5)
    yield [a.animate.set_value(2.0), FadeIn(br), FadeIn(one)]
    t.rate = 1.0
    yield [FadeOut(br), FadeOut(one), FadeIn(at(lab("let go", 28, INK, True), xw + rest, -1.6))]


BAXY = -2.3


def pos_axis(x0=-6.6, x1=6.6, y=BAXY, name=True):
    g = VGroup(axis_arrow((x0, y), (x1, y)))
    if name:
        g.add(lab("position", 22).move_to([x1 - 0.6, y - 0.35, 0]))
    return g


@slide("Quantum mechanics describes it as the bell curve", "The shifted bell")
def co2(s):
    c = ValueTracker(-2.0)
    s.add(c)
    ground = DashedVMobject(curve(bell(0, 0.55), -1.6, 1.6, -2.0, BAXY, 1.0, 2.8, TEAL, 3), num_dashes=30)
    moving = always_redraw(lambda: area(bell(0, 0.55), -1.6, 1.6, c.get_value(), BAXY, 1.0, 2.8, n=80))
    marks = VGroup(Line([-2.0, BAXY - 0.1, 0], [-2.0, BAXY + 0.1, 0], color=MUTED, stroke_width=3), lab("at rest", 22).move_to([-2.0, BAXY - 0.38, 0]),
                   Line([2.6, BAXY - 0.1, 0], [2.6, BAXY + 0.1, 0], color=MUTED, stroke_width=3), lab("where you let go", 22).move_to([2.6, BAXY - 0.38, 0]))
    yield [FadeIn(pos_axis(name=False)), FadeIn(marks), FadeIn(ground), FadeIn(moving),
           FadeIn(at(lab("the lowest rung's bell", 24, TEAL), -2.0, 1.1)), c.animate.set_value(2.6)]
    yield [FadeIn(at(pill("a coherent state", BLUE, 30), 2.6, 1.6), shift=UP * 0.15)]


def swinging_bell(t, X, amp, w=0.5, Y=BAXY, sy=2.4, span=1.6, phase=0.0):
    return always_redraw(lambda: area(bell(0, w), -span, span, X + amp * np.cos(SPIN * t.get_value() + phase), Y, 1.0, sy, n=70))


def centre_dot(t, X, amp, Y=BAXY, phase=0.0):
    return always_redraw(lambda: Dot([X + amp * np.cos(SPIN * t.get_value() + phase), Y, 0], radius=0.12, color=BLUE))


@slide("In rung terms, it's a mix of a huge number", "It swings")
def co3(s):
    t = clock(s)
    from math import factorial
    m = 9.0
    probs = [np.exp(-m) * m ** n / factorial(n) for n in range(25)]
    top = max(probs)
    bars = VGroup(*[Rectangle(width=0.18, height=max(3.0 * p / top, 0.02), stroke_width=0, fill_color=TEAL, fill_opacity=0.8)
                    .move_to([-6.6 + 0.22 * n, BAXY + 1.5 * p / top, 0]) for n, p in enumerate(probs)])
    yield [FadeIn(hline(-6.8, -1.0, BAXY, MUTED, 3)), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.03),
           FadeIn(at(lab("rungs", 22), -3.9, BAXY - 0.35)), FadeIn(at(lab("chance on each rung: many rungs", 24, TEAL, True), -3.9, 1.6))]
    X, amp = 3.9, 2.0
    path = DashedLine([X - amp, BAXY - 0.6, 0], [X + amp, BAXY - 0.6, 0], color=BLUE, stroke_width=2)
    yield [FadeIn(pos_axis(0.6, 7.2, name=False)), FadeIn(swinging_bell(t, X, amp)), FadeIn(centre_dot(t, X, amp)), FadeIn(path),
           FadeIn(at(lab("the centre follows chapter 1's path", 24, BLUE, True), X, 1.6))]


@slide("And its width stays at the bell's width forever.", "The width stays")
def co4(s):
    t = clock(s)
    X, amp = -2.3, 2.6
    width = always_redraw(lambda: DoubleArrow([X + amp * np.cos(SPIN * t.get_value()) - 0.42, BAXY + 1.2, 0],
                                              [X + amp * np.cos(SPIN * t.get_value()) + 0.42, BAXY + 1.2, 0], buff=0, color=ORANGE, stroke_width=4, tip_length=0.12))
    c, r = (4.9, 0.0), 1.5
    blob = always_redraw(lambda: Circle(radius=0.35, stroke_width=0, fill_color=TEAL, fill_opacity=0.35).move_to(
        [c[0] + r * np.cos(-SPIN * t.get_value()), c[1] + r * np.sin(-SPIN * t.get_value()), 0]))
    yield [FadeIn(pos_axis(-6.8, 1.6, name=False)), FadeIn(swinging_bell(t, X, amp)), FadeIn(width),
           FadeIn(at(lab("the width never changes", 24, ORANGE, True), X, 1.6)),
           FadeIn(plane(c, r)), FadeIn(orbit(c, r)), FadeIn(blob)]
    yield [FadeIn(at(words("a swinging spring, a pendulum: anything oscillating at everyday scale is very close to this", 70, 24, INK, align=ORIGIN), 0, -3.3))]


@slide("Here's why it looks classical.", "Width against swing")
def co5(s):
    t = clock(s)
    rows = ((1.0, 0.7), (-1.9, 2.6))
    g = VGroup()
    for y, amp in rows:
        g.add(pos_axis(-6.4, 3.6, y, name=False), swinging_bell(t, -1.4, amp, 0.5, y, 1.8), centre_dot(t, -1.4, amp, y))
    yield [FadeIn(g), FadeIn(left_at(lab("pull a little", 24, INK), 4.0, 1.4)), FadeIn(left_at(lab("pull hard", 24, INK), 4.0, -1.5))]
    yield [FadeIn(left_at(words("the width: fixed by the mass and the frequency", 16, 24, ORANGE), 4.0, 0.4))]
    yield [FadeIn(left_at(words("the swing: whatever you give it", 16, 24, BLUE), 4.0, -2.55))]


@slide("So what you see depends on how the two compare.", "Chapter 1's spring")
def co6(s):
    yield [FadeIn(at(lab("what you see: the width compared with the swing", 28, INK), 0, 2.0))]
    yield [FadeIn(left_at(lab("width", 30, ORANGE, True), -5.0, 0.6)), FadeIn(left_at(T("≈ 5 × 10⁻¹⁸ m", 36, ORANGE, True), -1.8, 0.6))]


def co_rows(s):
    s.add(at(lab("what you see: the width compared with the swing", 28, INK), 0, 2.0),
          left_at(lab("width", 30, ORANGE, True), -5.0, 0.6), left_at(T("≈ 5 × 10⁻¹⁸ m", 36, ORANGE, True), -1.8, 0.6))


@slide("The swing is one metre.", "Chapter 1's spring")
def co7(s):
    co_rows(s)
    yield [FadeIn(left_at(lab("swing", 30, BLUE, True), -5.0, -0.5)), FadeIn(left_at(T("1 m", 36, BLUE, True), -1.8, -0.5))]
    yield [FadeIn(at(T("the swing is 2 × 10¹⁷ widths", 40, INK, True), 0, -2.0), shift=UP * 0.15)]


@slide("No instrument could ever see the width.", "Too small to see")
def co8(s):
    w = ValueTracker(0.6)
    s.add(w)
    b = always_redraw(lambda: area(bell(0, w.get_value()), -4.0 * w.get_value(), 4.0 * w.get_value(), 0, -2.0, 1.0, 3.0, n=80))
    yield [FadeIn(hline(-5.5, 5.5, -2.0, MUTED, 3)), FadeIn(b), FadeIn(at(lab("the bell, drawn far too wide", 24, TEAL), 0, 1.6))]
    yield [w.animate.set_value(0.01), FadeIn(at(lab("at true scale: no instrument could see the width", 26, INK, True), 0, -3.0))]


@slide("All you see is the centre", "The classical spring")
def co9(s):
    t = clock(s)
    X, amp = 0.0, 3.6
    rig = VGroup(rig_static(-6.0, 1.3, 12.0, 0.8), always_redraw(lambda: rig_moving(-6.0, 1.3, 6.0, amp * np.cos(SPIN * t.get_value()), 0.8)))
    yield [FadeIn(rig), FadeIn(hline(-4.2, 4.2, -1.2, MUTED, 3)), FadeIn(centre_dot(t, X, amp, -1.2)),
           FadeIn(at(lab("all you see: a point following chapter 1's path", 26, BLUE, True), 0, -2.0))]
    yield [FadeIn(at(VGroup(lab("the classical spring", 28, TEAL, True), check()).arrange(RIGHT, buff=0.2), 0, -3.0))]


@slide("For a molecule's bond, the width is about six", "A molecule's bond")
def co10(s):
    t = clock(s)
    a = ValueTracker(0.0)
    s.add(a)
    c, d = (-1.8, 0.9), 4.4
    w = 0.06 * d                      # the bell's width: about 6% of the bond's length
    hx = c[0] + d / 2

    def shift():
        return a.get_value() * np.cos(SPIN * t.get_value())
    mol = always_redraw(lambda: hcl([c[0] + shift() / 2, c[1]], d + shift(), 1.5, spring=ORANGE, width=4))
    blur = always_redraw(lambda: area(bell(0, w), -3 * w, 3 * w, hx + shift(), -1.3, 1.0, 1.6, n=60))
    yield [FadeIn(mol), FadeIn(hline(hx - 2.2, hx + 2.2, -1.3, MUTED, 3)), FadeIn(blur),
           FadeIn(at(words("the width: about 6% of the bond's length", 16, 24, TEAL, align=ORIGIN), 5.0, 0.9))]
    yield [a.animate.set_value(2.5 * w), FadeIn(at(words("a vibration spans only a few widths", 16, 24, INK, align=ORIGIN), 5.0, -1.3))]


@slide("So the blur can't be ignored", "Rungs and jumps")
def co11(s):
    t = clock(s)
    hx, w = -3.4, 0.37
    yield [FadeIn(hline(hx - 2.6, hx + 2.6, -1.3, MUTED, 3)), FadeIn(swinging_bell(t, hx, 2 * w, w / 1.4 * 1.4, -1.3, 2.2, 4.0 * w)),
           FadeIn(at(lab("the blur can't be ignored", 26, TEAL, True), hx, 1.4))]
    lad = mini_ladder(3.4, 1.3, ORANGE, 4, top=1.6, bottom=-2.3, width=5)
    seq = (0, 1, 0, 2, 1, 0)
    dot = always_redraw(lambda: Dot([3.4, -2.3 + 1.3 * seq[int(t.get_value() * 0.9) % len(seq)] + 0.16, 0], radius=0.16, color=BLUE))
    yield [FadeIn(lad), FadeIn(dot), FadeIn(at(lab("you see rungs and jumps", 26, ORANGE, True), 3.4, 2.35))]


@slide("Same rules, same kind of state.", "Same rules at every scale")
def co12(s):
    t = clock(s)
    xs = (-3.6, 3.6)
    left = VGroup(hline(xs[0] - 2.6, xs[0] + 2.6, -1.0, MUTED, 3), swinging_bell(t, xs[0], 0.7, 0.5, -1.0, 2.2),
                  at(lab("a molecule's bond: the blur shows", 24, INK, True), xs[0], 1.6))
    right = VGroup(hline(xs[1] - 2.6, xs[1] + 2.6, -1.0, MUTED, 3), centre_dot(t, xs[1], 2.2, -1.0),
                   at(lab("chapter 1's spring: just a point", 24, INK, True), xs[1], 1.6))
    yield [FadeIn(left), FadeIn(right), FadeIn(at(lab("same rules, same kind of state", 26, TEAL, True), 0, 2.4))]
    yield [FadeIn(at(lab("at our scale, the quantum blur is far too small to notice", 26, INK), 0, -2.6))]


# ================================================================== where this comes back
deck.part("Where this comes back")


@slide("Where this comes back.", "Where this comes back")
def cb1(s):
    t = clock(s)
    yield [FadeIn(rig_static(-6.6, 0.4, 5.4, 0.8)), FadeIn(always_redraw(lambda: rig_moving(-6.6, 0.4, 2.8, 1.0 * np.cos(SPIN * t.get_value()), 0.8))),
           FadeIn(mini_ladder(0.4, 0.8, INK, 5, top=1.6, bottom=-1.6, w=2.0)), FadeIn(at(lab("the quantum spring", 26, INK, True), -2.6, 2.3))]
    yield [GrowArrow(Arrow([1.9, 0.0, 0], [3.4, 0.0, 0], buff=0, color=ORANGE, stroke_width=5, tip_length=0.2)),
           FadeIn(at(words("it keeps coming back in later chapters", 16, 28, ORANGE, align=ORIGIN), 5.4, 0.0))]


def field_rows(t, ladders=True):
    g = VGroup()
    for i, (k, rate) in enumerate(((1, 1.3), (2, 2.2), (3, 3.1))):
        y = 1.55 - 1.4 * i
        g.add(always_redraw(lambda y=y, k=k, rate=rate: standing(-6.6, -3.0, y, k, 0.42 * np.cos(rate * t.get_value()))))
        if ladders:
            gap = 0.2 + 0.1 * i
            g.add(at(T("=", 30, MUTED), -2.3, y), mini_ladder(-0.9, gap, INK, 3, bottom=y - gap, w=1.6, width=3))
    return g


@slide("In the chapter on field quantization", "Field quantization")
def cb2(s):
    t = clock(s)
    yield [FadeIn(field_rows(t)), FadeIn(at(lab("each wave of a field: a spring with its own ladder", 24, INK), -2.6, 2.45))]
    dot = Dot([4.0, 0.15, 0], radius=0.2, color=BLUE)
    mom = Arrow([4.3, 0.15, 0], [5.8, 0.15, 0], buff=0, color=BLUE, stroke_width=5, tip_length=0.2)
    yield [GrowArrow(Arrow([0.4, 0.15, 0], [3.5, 0.15, 0], buff=0, color=ORANGE, stroke_width=4, tip_length=0.18)), FadeIn(dot), GrowArrow(mom),
           FadeIn(at(words("one quantum: one particle, moving with the wave's momentum", 22, 24, INK, align=ORIGIN), 4.6, -1.2))]


@slide("Every wave also has its own zero-point energy.", "Zero-point energy of every wave")
def cb3(s):
    t = clock(s)
    rows = field_rows(t, ladders=False)
    halves = VGroup(*[at(omega_subs(heq("½ ħω ", 28, ORANGE), "½ ħω ", [i + 1]), -1.5, 1.55 - 1.4 * i) for i in range(3)])
    yield [FadeIn(rows), FadeIn(halves), FadeIn(at(lab("each wave has its own ω; and so on, for every wave", 22, MUTED), -3.6, -2.9))]
    text = "½ ħω  + ½ ħω  + ½ ħω  + … = infinite"
    total = at(omega_subs(heq(text, 24, INK), text, [1, 2, 3]), 3.55, 0.6)
    yield [FadeIn(total), FadeIn(at(lab("infinitely many waves: it gets subtracted off", 24, INK), 3.6, -0.4))]


@slide("And the quanta of the light field are photons", "Photons")
def cb4(s):
    t = clock(s)
    xs = np.linspace(-6.6, -1.0, 100)
    light = always_redraw(lambda: VMobject(color=MUTED, stroke_width=4).set_points_smoothly(
        [[x, 0.2 + 0.5 * np.sin(2.2 * x - 3 * t.get_value()), 0] for x in xs]))
    yield [FadeIn(light), FadeIn(at(lab("the light field", 26, INK, True), -3.8, 1.6))]

    def packet(x0):
        us = np.linspace(-0.8, 0.8, 50)
        return VMobject(color=ORANGE, stroke_width=4).set_points_smoothly([[x0 + u, 0.2 + 0.4 * np.exp(-4 * u * u) * np.sin(12 * u), 0] for u in us])
    packets = VGroup(*[packet(x) for x in (1.4, 3.6, 5.8)])
    yield [LaggedStart(*[FadeIn(p, shift=RIGHT * 0.3) for p in packets], lag_ratio=0.3),
           FadeIn(at(words("its quanta are photons, the packets of light from chapter 2", 26, 26, ORANGE, align=ORIGIN), 3.6, -1.4))]


@slide("But first, fields have to agree with relativity.", "Next: special relativity")
def cb5(s):
    a = at(card("fields must agree\nwith relativity", 4.6, 1.5, INK, 28), -3.4, 0.2)
    yield [FadeIn(a)]
    b = at(card("next chapter:\nSpecial Relativity", 4.6, 1.5, ORANGE, 30), 3.4, 0.2)
    yield [GrowArrow(arrow(a, b, ORANGE)), FadeIn(b)]

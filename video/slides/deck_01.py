"""Slides for chapter one, Classical Mechanics.

Every value comes from video/scripts/01-classical-mechanics.txt or
docs/classical-mechanics.md. The drawings redraw the chapter's figures in
docs/manim/ (newton-motion, pendulum-forces, stationary-action-paths,
phase-space-states, classical-oscillator-energy) as animations.

Colors: BLUE for the motion itself (bodies, the bob, the block, positions and
velocities, the real path, momentum, states and the point in phase space),
ORANGE for forces (gravity, the string's tension, the spring's pull, the track's
push, the force side of the Euler-Lagrange equation and of Hamilton's second
equation), TEAL for energy (kinetic and potential energy, their bars, the 2 J
total) and for checks that pass, PURPLE for the functions that run the motion
(the Lagrangian, the action and its valley, the Euler-Lagrange equation, the
Hamiltonian, the Poisson bracket), RED only for something that fails (F = ma
with no paths, the dodge on a double pendulum, conservation of energy alone,
the name least action, comparing paths one by one, the bracket with velocity),
INK for other equations, MUTED for bent and imagined paths, and MUTED and LINE
for axes, apparatus, context and connectors.
"""
import json
from pathlib import Path

from manim import *

from engine import *

STEM = "01-classical-mechanics"
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


def eq(text, size=36, color=INK, bold=False):
    """An equation, set in the deck's type (Helvetica keeps ², ½ and ℓ tight)."""
    return T(text, size, color, bold)


def hold():
    """A step that adds nothing, so the next reveal waits for its sentence."""
    return [Wait()]


def clock(s, rate=1.0):
    """Time that keeps running during holds, so the things drawn from it keep moving."""
    t = ValueTracker(0.0)
    t.rate = rate
    t.add_updater(lambda m, dt: m.increment_value(m.rate * dt))
    s.add(t)
    return t


def tracker(s, v=0.0):
    k = ValueTracker(v)
    s.add(k)
    return k


def dim(mob, o):
    """Scale every part's stroke and fill opacity by o, keeping hollow shapes hollow."""
    if o >= 0.999:
        return mob
    for m in mob.family_members_with_points():
        m.set_stroke(opacity=m.get_stroke_opacity() * o)
        m.set_fill(opacity=m.get_fill_opacity() * o)
    return mob


def live(s, fn, seen=None):
    """A drawing redrawn every frame and added now; with `seen`, its opacity follows that tracker.

    Revealing a moving drawing through its own opacity, rather than with FadeIn, keeps it moving
    while it appears and never stacks a second copy on the first.
    """
    m = always_redraw(fn if seen is None else (lambda: dim(fn(), seen.get_value())))
    s.add(m)
    return m


def show(*trackers):
    return [k.animate.set_value(1.0) for k in trackers]


def hchip(text, color=INK, size=26, h=0.7, w=None):
    """A chip set in the deck's type, for words rather than values."""
    label = T(text, size, color)
    box = RoundedRectangle(width=w or label.width + 0.4, height=h, corner_radius=0.09, stroke_color=color,
                           stroke_width=2, fill_color=WHITE, fill_opacity=1)
    label.move_to(box)
    return VGroup(box, label)


def narration_start(at):
    """When the narration reaches the sentence starting with `at`, from video/timings (0 if not rendered yet)."""
    try:
        data = json.loads((Path(__file__).resolve().parent.parent / "timings" / f"{STEM}.json").read_text())
    except (OSError, ValueError):
        return 0.0
    for row in data:
        if row["text"].startswith(at):
            return row["start"]
    return 0.0


def tick(mob, color=TEAL, buff=0.2):
    return check(color).next_to(mob, RIGHT, buff=buff)


def xmark(mob, size=0.42, buff=0.2):
    return cross(Square(size).next_to(mob, RIGHT, buff=buff), RED, 6)


def varrow(a, vec, color, width=5, tip=0.2, minlen=0.16):
    """An arrow from a along vec that fades out, rather than collapsing, as vec shrinks."""
    a = np.array(a, dtype=float)
    v = np.array(vec, dtype=float)
    n = np.linalg.norm(v)
    o = 1.0
    if n < minlen:
        o = (n / minlen) ** 2
        v = (v / n if n > 1e-9 else RIGHT) * minlen
    ar = Arrow(a, a + v, buff=0, color=color, stroke_width=width, tip_length=tip,
               max_tip_length_to_length_ratio=0.45, max_stroke_width_to_length_ratio=40)
    return ar.set_opacity(o) if o < 1 else ar


def corners(pts, color=BLUE, width=4):
    return VMobject(color=color, stroke_width=width).set_points_as_corners(pts)


def smooth(pts, color=BLUE, width=4):
    return VMobject(color=color, stroke_width=width).set_points_smoothly(pts)


def hline(x0, x1, y, color=LINE, width=3):
    return Line(P(x0, y), P(x1, y), color=color, stroke_width=width)


def axis(a, b, color=MUTED, width=3):
    return Arrow(P(*a), P(*b), buff=0, color=color, stroke_width=width, tip_length=0.16,
                 max_tip_length_to_length_ratio=0.2)


def dashed(a, b, color=LINE, width=3, n=14):
    """A dashed line with a fixed number of dashes, safe to redraw every frame."""
    return DashedVMobject(Line(P(a[0], a[1]), P(b[0], b[1]), color=color, stroke_width=width), num_dashes=n)


# ------------------------------------------------------------------ the pendulum

PIV = P(-3.6, 2.45)   # the pivot
PL = 3.4              # the string's length on screen
TH0 = 0.6             # the swing's amplitude, in radians
WP = 1.8              # the swing's rate on screen, radians per second


def swing(t):
    return TH0 * np.cos(WP * t)


def swing_rate(t):
    return -TH0 * WP * np.sin(WP * t)


def bob_at(piv, l, th):
    return np.array(piv, dtype=float) + l * np.array([np.sin(th), -np.cos(th), 0])


def along(th):
    """The direction of increasing angle, along the circle."""
    return np.array([np.cos(th), np.sin(th), 0])


def pendulum(th, piv=PIV, l=PL, r=0.2, bar=True):
    piv = np.array(piv, dtype=float)
    b = bob_at(piv, l, th)
    g = VGroup(Line(piv + LEFT * 0.6, piv + RIGHT * 0.6, color=INK, stroke_width=6 if bar else 0),
               Line(piv, b, color=INK, stroke_width=3), Dot(b, radius=r, color=BLUE))
    return g


def circle_arc(piv=PIV, l=PL, half=0.78):
    return DashedVMobject(Arc(radius=l, start_angle=-PI / 2 - half, angle=2 * half, arc_center=np.array(piv, dtype=float),
                              color=LINE, stroke_width=3), num_dashes=30)


def gravity_arrow(th, piv=PIV, l=PL, n=1.0):
    return varrow(bob_at(piv, l, th) + DOWN * 0.22, DOWN * n, ORANGE)


def tension_arrow(th, piv=PIV, l=PL):
    """The string's pull on the bob, along the string; it grows as the bob passes the bottom."""
    b = bob_at(piv, l, th)
    u = (np.array(piv, dtype=float) - b) / l
    return varrow(b + u * 0.22, u * (0.55 * (3 * np.cos(th) - 2 * np.cos(TH0)) + 0.4), ORANGE, 6)


def motion_arrow(th, om, piv=PIV, l=PL, top=1.3):
    b = bob_at(piv, l, th)
    k = top / (TH0 * WP)
    return varrow(b + along(th) * np.sign(om) * 0.22, along(th) * om * k, BLUE)


def right_angle(th, om, piv=PIV, l=PL, s=0.42):
    b = bob_at(piv, l, th)
    u = (np.array(piv, dtype=float) - b) / l
    tv = along(th) * (1 if om >= 0 else -1)
    return corners([b + u * s, b + u * s + tv * s, b + tv * s], MUTED, 2.5)


def angle_mark(origin, th, name, r=0.8, length=1.6, color=BLUE, size=28):
    """A dashed line straight down from origin, an arc out to angle th, and its name."""
    origin = np.array(origin, dtype=float)
    vert = dashed(origin, origin + DOWN * length, LINE, 2.5, 10)
    arc = Arc(radius=r, start_angle=-PI / 2, angle=th if abs(th) > 1e-3 else 1e-3, arc_center=origin, color=color, stroke_width=4)
    mid = -PI / 2 + th / 2
    if not name:   # before the narration names the angle, draw the arc alone
        return VGroup(vert, arc)
    label = T(name, size, color, True).move_to(origin + (r + 0.3) * np.array([np.cos(mid), np.sin(mid), 0]))
    return VGroup(vert, arc, label)


# the double pendulum
D1, D2 = 2.1, 1.8
POSE = (0.42, 1.05)   # the pose it settles into to show the lower string's pull


def dp_angles(t):
    a = 0.30 * np.cos(1.5 * t) + 0.12 * np.cos(3.4 * t + 0.6)
    b = 0.45 * np.cos(1.5 * t) - 0.32 * np.cos(3.4 * t + 0.6)
    return a, b


def dp_pose(t, w=0.0):
    a, b = dp_angles(t)
    return (1 - w) * a + w * POSE[0], (1 - w) * b + w * POSE[1]


def double(th1, th2, piv=PIV, r=0.19):
    piv = np.array(piv, dtype=float)
    b1 = bob_at(piv, D1, th1)
    b2 = bob_at(b1, D2, th2)
    return VGroup(Line(piv + LEFT * 0.6, piv + RIGHT * 0.6, color=INK, stroke_width=6),
                  Line(piv, b1, color=INK, stroke_width=3), Line(b1, b2, color=INK, stroke_width=3),
                  Dot(b1, radius=r, color=BLUE), Dot(b2, radius=r, color=BLUE))


def pose_parts():
    """The double pendulum at POSE: the drawing, the upper bob, its motion and the lower string's pull on it."""
    th1, th2 = POSE
    b1 = bob_at(PIV, D1, th1)
    tv = along(th1)
    u = np.array([np.sin(th2), -np.cos(th2), 0])
    mot = Arrow(b1 + tv * 0.2, b1 + tv * 1.5, buff=0, color=BLUE, stroke_width=5, tip_length=0.2)
    pull = Arrow(b1 + u * 0.2, b1 + u * 1.25, buff=0, color=ORANGE, stroke_width=6, tip_length=0.22)
    a0, a1 = np.arctan2(u[1], u[0]), np.arctan2(tv[1], tv[0])
    arc = Arc(radius=0.62, start_angle=a0, angle=a1 - a0, arc_center=b1, color=INK, stroke_width=3)
    return double(*POSE), b1, mot, pull, arc


# ------------------------------------------------------------------ the spring

def zigzag(a, b, n=10, amp=0.18, color=MUTED):
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    d = b - a
    length = max(np.linalg.norm(d), 1e-3)
    u = d / length
    nrm = np.array([-u[1], u[0], 0])
    end = min(0.15, length / 4)
    pts = [a, a + u * end]
    for i in range(n):
        f = end + (length - 2 * end) * (i + 0.5) / n
        pts.append(a + u * f + nrm * amp * (1 if i % 2 == 0 else -1))
    pts += [b - u * end, b]
    return corners(pts, color, 3)


SPR = dict(y=1.3, wall=-7.2, rest=-4.4, sc=1.3, size=0.8, floor=-1.6)


def spring(x, y=1.3, wall=-7.2, rest=-4.4, sc=1.3, size=0.8, floor=-1.6):
    """A wall, a spring and a block stretched x metres from rest (sc screen units per metre)."""
    bx = rest + sc * x
    return VGroup(Line(P(wall, y - 0.7), P(wall, y + 0.7), color=INK, stroke_width=6),
                  hline(wall, floor, y - size / 2 - 0.04, LINE, 3),
                  zigzag(P(wall, y), P(bx - size / 2, y)),
                  Square(size, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to(P(bx, y)))


def rest_mark(y=1.3, rest=-4.4):
    return VGroup(dashed((rest, y - 0.75), (rest, y + 0.75), LINE, 2.5, 8), at(lab("rest", 22), rest, y + 0.95))


def osc_x(t):
    """The book's spring: 1 kg, k = 4 N/m, pulled out 1 m, so x = cos 2t and p = −2 sin 2t."""
    return np.cos(2 * t)


def osc_p(t):
    return -2 * np.sin(2 * t)


# ------------------------------------------------------------------ phase space

PX, PY = 3.6, -0.4    # the origin of the phase-space map
PXS = 1.25            # screen units per metre of position
PPS = 1.15            # screen units per unit of momentum, before rescaling


def pp(x, p, ps=PPS):
    return P(PX + PXS * x, PY + ps * p)


def phase_frame(xname="position x"):
    return VGroup(axis((PX - 2.3, PY), (PX + 2.1, PY)), axis((PX, PY - 2.7), (PX, 2.45)),
                  left_at(lab(xname, 22), PX + 2.2, PY), left_at(lab("momentum p", 22), PX + 0.2, 2.42))


def orbit(t0=0.0, t1=PI, ps=PPS, color=BLUE, width=4, n=90):
    ts = np.linspace(t0, t1, n)
    return smooth([pp(osc_x(t), osc_p(t), ps) for t in ts], color, width)


def phase_dot(t, ps=PPS, color=BLUE):
    return Dot(pp(osc_x(t), osc_p(t), ps), radius=0.13, color=color)


def trace(t, ps=PPS, n=70, start=0.0):
    """The part of the loop travelled from `start` to time t, drawn once round and then left whole."""
    end = start + max(min(t - start, PI), 1e-3)
    return corners([pp(osc_x(u), osc_p(u), ps) for u in np.linspace(start, end, n)], BLUE, 4)


# ------------------------------------------------------------------ the thrown ball and the action valley

def hgt(t, e=0.0):
    """Height of the thrown ball, plus a bulge e that leaves both ends fixed."""
    return 9.8 * t - 4.9 * t * t + 3.0 * e * np.sin(np.pi * t / 2)


def throw_frame(cx, cy, w, h, hmax=7.8, ticks=True):
    def c(t, y):
        return P(cx - w / 2 + t / 2.0 * w, cy - h / 2 + y / hmax * h)
    g = VGroup(axis((cx - w / 2, cy - h / 2), (cx + w / 2 + 0.35, cy - h / 2)), axis((cx - w / 2, cy - h / 2), (cx - w / 2, cy + h / 2 + 0.2)),
               right_at(lab("time", 22), cx + w / 2 + 0.35, cy - h / 2 - 0.62),
               at(lab("height", 22), cx - w / 2, cy + h / 2 + 0.45))
    if ticks:
        g.add(at(lab("0", 22), cx - w / 2, cy - h / 2 - 0.3), at(lab("2 s", 22), cx + w / 2, cy - h / 2 - 0.3),
              Line(c(2, 0), c(2, 0) + UP * 0.12, color=MUTED, stroke_width=3))
    return c, g


def throw_path(c, e=0.0, color=BLUE, width=5, t1=2.0, n=48):
    return smooth([c(t, hgt(t, e)) for t in np.linspace(0, t1, n)], color, width)


def ends(c):
    return VGroup(Dot(c(0, 0), radius=0.1, color=INK), Dot(c(2, 0), radius=0.1, color=INK))


def valley(cx, cy, w, h, emax=0.8, xname="bulge"):
    """The action of each path against its bend: a parabola whose flat bottom is the real path."""
    def vp(e):
        return P(cx + e / emax * w / 2, cy + h * (e / emax) ** 2)
    curve = smooth([vp(e) for e in np.linspace(-emax, emax, 33)], PURPLE, 5)
    base = cy - 0.3
    frame = VGroup(Line(P(cx - w / 2 - 0.3, base), P(cx + w / 2 + 0.3, base), color=LINE, stroke_width=3),
                   Line(P(cx, base), P(cx, cy + h + 0.35), color=LINE, stroke_width=3),
                   right_at(lab("action", 24, PURPLE), cx - 0.15, cy + h + 0.25))
    if xname:
        frame.add(right_at(lab(xname, 22), cx + w / 2 + 0.3, base - 0.32))
    return vp, curve, frame


def flat_line(vp, half=0.4, color=PURPLE):
    y = vp(0)[1]
    return DashedLine(P(vp(-half)[0], y), P(vp(half)[0], y), color=color, stroke_width=4)


def rise(vp, e, color=INK):
    """How far the action sits above the valley floor at bend e."""
    return Line(P(vp(e)[0], vp(0)[1]), vp(e), color=color, stroke_width=4)


# ------------------------------------------------------------------ icons

def icon_pend(x, y, th=0.45, l=1.25):
    return pendulum(th, P(x, y + 0.65), l, 0.15)


def icon_spring(x, y, stretch=0.0):
    return spring(stretch, y=y, wall=x - 1.0, rest=x + 0.45, sc=0.6, size=0.5, floor=x + 1.1)


def icon_ball(x, y):
    ground = hline(x - 0.95, x + 0.95, y - 0.6, LINE, 3)
    arc = DashedVMobject(ArcBetweenPoints(P(x - 0.75, y - 0.5), P(x + 0.75, y - 0.5), angle=-PI * 0.7, color=LINE), num_dashes=12)
    return VGroup(ground, arc, Dot(P(x - 0.15, y + 0.45), radius=0.16, color=BLUE))


def flat_icon(x, y, up=True, w=1.2):
    sgn = 1 if up else -1
    curve = smooth([P(x + u, y + sgn * 0.6 * u * u) for u in np.linspace(-w, w, 15)], PURPLE, 4)
    tan = DashedLine(P(x - 0.8, y), P(x + 0.8, y), color=PURPLE, stroke_width=3)
    return VGroup(curve, tan, Dot(P(x, y), radius=0.1, color=BLUE))


def saddle_icon(x, y, s=1.0):
    """A wireframe saddle, z = u² − v², seen at an angle, flat at its centre."""
    def pr(u, v):
        return P(x + s * (1.0 * u + 0.5 * v), y + s * (0.55 * (u * u - v * v) + 0.32 * v))
    g = VGroup()
    for v in np.linspace(-1, 1, 5):
        g.add(smooth([pr(u, v) for u in np.linspace(-1, 1, 13)], PURPLE, 2.5 if abs(v) > 0.01 else 4))
    for u in np.linspace(-1, 1, 5):
        g.add(smooth([pr(u, v) for v in np.linspace(-1, 1, 13)], PURPLE, 2.5 if abs(u) > 0.01 else 4))
    g.add(Dot(pr(0, 0), radius=0.1, color=BLUE))
    return g


def knob(c, ang, label, color=INK):
    """A dial whose pointer turns by ang from straight up."""
    c = np.array(c, dtype=float)
    g = VGroup(Circle(radius=0.6, color=color, stroke_width=3, fill_color=WHITE, fill_opacity=1).move_to(c))
    for k in range(9):
        a = PI / 2 + (k - 4) * 0.35
        u = np.array([np.cos(a), np.sin(a), 0])
        g.add(Line(c + 0.68 * u, c + 0.8 * u, color=MUTED, stroke_width=2))
    a = PI / 2 - ang
    g.add(Line(c, c + 0.48 * np.array([np.cos(a), np.sin(a), 0]), color=color, stroke_width=5), Dot(c, radius=0.07, color=color))
    g.add(at(lab(label, 24, INK), c[0], c[1] - 0.9))
    return g


def meter(x, y, amount, w=1.6):
    """A bar showing how much the Lagrangian changed, for a knob turned by `amount` (0 to 1)."""
    frame = Rectangle(width=w, height=0.32, stroke_color=LINE, stroke_width=2).move_to(P(x + w / 2, y))
    fill = Rectangle(width=max(w * amount, 0.002), height=0.32, stroke_width=0, fill_color=PURPLE, fill_opacity=0.85)
    left_at(fill, x, y)
    return VGroup(frame, fill)


# ================================================================== opening
deck.part("Chapter one")


@slide("Chapter one.", "Classical Mechanics")
def opening(s):
    t = clock(s)
    a, b = tracker(s), tracker(s)
    live(s, lambda: pendulum(swing(t.get_value()), P(-4.8, 2.2), 2.9), a)
    live(s, lambda: VGroup(spring(0.8 * np.cos(2 * t.get_value()), y=-0.9, wall=-1.4, rest=1.0, sc=1.0, size=0.7, floor=2.6),
                           hline(4.4, 6.6, -1.6, LINE, 3),
                           Dot(P(5.5, -1.42 + 3.2 * 4 * ((t.get_value() / 1.6) % 1) * (1 - (t.get_value() / 1.6) % 1)), radius=0.18, color=BLUE)), b)
    yield show(a)
    yield show(b)


@slide("Quantum theory has no forces", "No forces, no paths")
def nopaths(s):
    t = clock(s)
    q = tracker(s)
    rng = np.random.default_rng(3)
    offs = rng.normal(size=(40, 2)) * 0.5
    phases = rng.uniform(0, TAU, 40)

    def pt(u):
        return P(-6.3 + 5.6 * u, -1.9 + 2.9 * 4 * u * (1 - u))

    path_pts = [pt(u) for u in np.linspace(0, 1, 30)]

    def draw():
        qq = q.get_value()
        u = min(t.get_value() / 6.0, 1.0)
        c = pt(u)
        tt = t.get_value()
        g = VGroup(smooth(path_pts, BLUE, 4).set_stroke(opacity=1 - 0.8 * qq), Dot(c, radius=0.17, color=BLUE).set_opacity(1 - qq))
        for (dx, dy), ph in zip(offs, phases):
            k = qq * (1 + 0.18 * np.sin(2.5 * tt + ph))
            d = c + P(dx * k * 1.6, dy * k * 1.6)
            d[1] = min(d[1], 2.5)   # keep the cloud below the title
            g.add(Dot(d, radius=0.055, color=BLUE).set_opacity(0.75 * qq))
        return g
    live(s, draw)
    r1 = left_at(words("ordinary mechanics: a definite path", 22, 26, INK), 1.0, 1.6)
    yield [FadeIn(r1)]
    r2 = left_at(words("a quantum particle: no definite track", 22, 26, INK), 1.0, 0.1)
    yield [q.animate.set_value(1.0), FadeIn(r2)]
    f = left_at(chip("F = m a", INK, size=32, h=0.85), 1.0, -1.6)
    yield [FadeIn(f), Create(strike(f)), FadeIn(left_at(words("nothing to put into it", 30, 26, RED), 3.3, -1.6))]


@slide("But one thing from ordinary mechanics", "One thing survives")
def survives(s):
    t = clock(s)
    a = at(card("ordinary mechanics", 4.4, 1.1, INK, 28), -4.8, 1.8)
    b = at(card("quantum theory", 4.4, 1.1, INK, 28), 4.8, 1.8)
    one = at(chip("one thing", PURPLE, size=28, h=0.75), 0, 0.75)
    yield [FadeIn(a), FadeIn(b), GrowArrow(arrow(a, b)), FadeIn(one, shift=RIGHT * 2.2),
           FadeIn(at(lab("survives the trip", 24, INK), 0, 2.35))]
    fn = at(card("a single function,\nbuilt from the energy", 5.4, 1.4, PURPLE, 28), 0, 0.5)
    seen = tracker(s)
    live(s, lambda: spring(0.8 * np.cos(2 * t.get_value()), y=-2.0, wall=-3.0, rest=0.2, sc=1.0, size=0.7, floor=2.0), seen)
    yield [ReplacementTransform(one, fn), GrowArrow(Arrow(P(-3.6, -0.3), P(-3.6, -1.3), buff=0, color=MUTED, stroke_width=4, tip_length=0.18)),
           FadeIn(right_at(words("it tells the system how to move", 18, 26, INK), -4.0, -0.8)), *show(seen)]


@slide("This chapter rewrites ordinary mechanics", "A ball, a pendulum and a spring")
def systems(s):
    t = clock(s)
    fn = at(card("the function from the energy", 6.2, 0.95, PURPLE, 28), 0, 2.0)
    yield [FadeIn(fn), FadeIn(at(lab("ordinary mechanics, rewritten around it", 24, INK), 0, 1.15))]
    seen = tracker(s)
    live(s, lambda: VGroup(
        hline(-5.7, -3.5, -1.65, LINE, 3),
        Dot(P(-4.6, -1.47 + 2.4 * 4 * ((t.get_value() / 1.5) % 1) * (1 - (t.get_value() / 1.5) % 1)), radius=0.18, color=BLUE),
        pendulum(0.5 * np.cos(2.0 * t.get_value()), P(0, 0.55), 1.9, 0.18),
        spring(0.6 * np.cos(2 * t.get_value()), y=-0.7, wall=2.9, rest=4.8, sc=0.8, size=0.6, floor=6.4)), seen)
    names = VGroup(at(lab("a ball", 26, INK), -4.6, -2.25), at(lab("a pendulum", 26, INK), 0, -2.25), at(lab("a spring", 26, INK), 4.8, -2.25))
    yield [*show(seen), FadeIn(names)]
    yield [FadeIn(at(pill("next chapter: that function becomes quantum mechanics", INK, 26), 0, -3.3), shift=UP * 0.15)]


COLS = (-4.85, 0.0, 4.85)


def col_heads():
    return VGroup(*[at(pill(n, INK, 28), x, 2.2) for n, x in zip(("Newton", "Lagrange", "Hamilton"), COLS)])


def col_text(k):
    texts = ("starts from forces", "scores whole paths with one number built from energy",
             "describes one instant; the energy carries it forward")
    return at(words(texts[k], 22, 25, INK, ORIGIN), COLS[k], -1.05)


def icon_newton(x, y, t=None):
    run = 0.0 if t is None else min(t.get_value(), 3.0)
    bx = x - 1.0 + 0.2 * run * run
    return VGroup(hline(x - 1.6, x + 1.7, y - 0.45, LINE, 3),
                  Square(0.7, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to(P(bx, y - 0.08)),
                  Arrow(P(bx - 1.15, y - 0.08), P(bx - 0.37, y - 0.08), buff=0, color=ORANGE, stroke_width=5, tip_length=0.18))


def icon_paths(x, y):
    a, b = P(x - 1.5, y - 0.5), P(x + 1.5, y - 0.5)
    g = VGroup(*[ArcBetweenPoints(a, b, angle=-ang, color=MUTED, stroke_width=3) for ang in (0.5, 1.9, 2.5)])
    g.add(ArcBetweenPoints(a, b, angle=-1.3, color=BLUE, stroke_width=5), Dot(a, radius=0.08, color=INK), Dot(b, radius=0.08, color=INK),
          chip("S", PURPLE, size=24, h=0.5).move_to(P(x + 1.55, y + 0.65)))
    return g


def icon_phase(x, y, t=None):
    tt = 0.0 if t is None else t.get_value()
    g = VGroup(axis((x - 1.2, y), (x + 1.3, y)), axis((x, y - 0.85), (x, y + 0.95)),
               smooth([P(x + 0.75 * np.cos(u), y + 0.65 * np.sin(u)) for u in np.linspace(0, TAU, 40)], BLUE, 3),
               Dot(P(x + 0.75 * np.cos(-2 * tt), y + 0.65 * np.sin(-2 * tt)), radius=0.1, color=BLUE))
    return g


@slide("We'll describe the same motion three ways", "One motion, three descriptions")
def three1(s):
    t = clock(s)
    yield [FadeIn(col_heads()), FadeIn(at(lab("the same motion, exactly the same answers", 26, INK), 0, -3.4))]
    seen = tracker(s)
    start = {"at": None}
    live(s, lambda: icon_newton(COLS[0], 0.6, ValueTracker(0.0 if start["at"] is None else t.get_value() - start["at"])), seen)
    start["at"] = t.get_value()
    yield [*show(seen), FadeIn(col_text(0))]
    yield [FadeIn(icon_paths(COLS[1], 0.6)), FadeIn(col_text(1))]


@slide("Hamilton describes the system at one instant", "One motion, three descriptions")
def three2(s):
    t = clock(s)
    s.add(col_heads(), icon_newton(COLS[0], 0.6, ValueTracker(3.0)), col_text(0), icon_paths(COLS[1], 0.6), col_text(1))
    seen = tracker(s)
    live(s, lambda: icon_phase(COLS[2], 0.6, t), seen)
    yield [*show(seen), FadeIn(col_text(2))]
    pb = at(card("the Poisson bracket", 4.2, 0.85, PURPLE, 28), COLS[2], -2.55)
    yield [GrowArrow(Arrow(P(COLS[2], -1.65), P(COLS[2], -2.1), buff=0, color=MUTED, stroke_width=4, tip_length=0.16)), FadeIn(pb),
           FadeIn(right_at(lab("the last step", 24, INK), COLS[2] - 2.35, -2.55))]
    yield [FadeIn(at(lab("the piece quantum mechanics replaces", 26, INK, True), -1.5, -3.45)), Indicate(pb, color=PURPLE)]


# ================================================================== forces in, motion out
deck.part("Forces in, motion out")


def push_block(t, start):
    """A block pushed by a steady force, speeding up from rest and stopping at the frame's edge."""
    run = 0.0 if start["at"] is None else min(t.get_value() - start["at"], 5.2)
    bx = -5.4 + 0.35 * run * run
    y = -1.15
    v = 0.45 * run
    g = VGroup(Square(0.9, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to(P(bx, y)),
               Arrow(P(bx - 1.6, y), P(bx - 0.47, y), buff=0, color=ORANGE, stroke_width=6, tip_length=0.22),
               varrow(P(bx, y + 0.75), RIGHT * v, BLUE, 5, 0.2))
    return g


@slide("Forces in, motion out.", "A force makes a body accelerate")
def newton1(s):
    t = clock(s)
    start = {"at": None}
    yield [FadeIn(hline(-7.3, 7.3, -1.62, LINE, 4)), FadeIn(always_redraw(lambda: push_block(t, start)))]
    start["at"] = t.get_value()
    yield [FadeIn(at(lab("a steady force", 24, ORANGE), -4.8, -2.15)), FadeIn(at(lab("its speed keeps growing", 24, BLUE), 0.6, -2.15)),
           FadeIn(at(lab("a force makes a body accelerate", 28, INK), 0, 0.8))]
    e = at(VGroup(eq("F", 60, ORANGE), eq("=", 60), eq("m", 60), eq("a", 60, BLUE)).arrange(RIGHT, buff=0.3), 0, 2.0)
    yield [FadeIn(e)]


@slide("Acceleration is how fast the velocity changes", "Start, speed and forces fix the rest")
def newton2(s):
    t = clock(s, 0.0)
    names = ("position", "velocity", "acceleration")
    chips = [at(card(n, 2.7, 0.85, BLUE, 28), x, 1.6) for n, x in zip(names, (-5.3, 0, 5.3))]
    links = [arrow(a, b) for a, b in zip(chips, chips[1:])]
    rates = [at(lab("how fast it changes", 22), l.get_center()[0], 2.4) for l in links]
    yield [*[FadeIn(c) for c in chips], *[GrowArrow(l) for l in links], *[FadeIn(r) for r in rates]]
    given = VGroup(lab("where it starts", 26, INK), lab("how fast it's moving", 26, INK), lab("what forces act on it", 26, ORANGE))
    given.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
    left_at(given, -7.0, -1.3)
    yield [LaggedStart(*[FadeIn(g, shift=RIGHT * 0.15) for g in given], lag_ratio=0.3)]

    def pt(u):
        return P(-1.0 + 7.6 * u, -2.6 + 2.2 * np.sin(PI * u) * (1.0 - 0.25 * u))
    path = smooth([pt(u) for u in np.linspace(0, 1, 30)], LINE, 3)

    def ball():
        u = min(t.get_value() / 4.0, 1.0)
        return VGroup(smooth([pt(v) for v in np.linspace(0, u if u > 0.002 else 0.002, 30)], BLUE, 4), Dot(pt(u), radius=0.17, color=BLUE))
    t.rate = 1.0
    yield [GrowArrow(Arrow(P(-2.3, -1.3), P(-1.3, -1.3), buff=0, color=MUTED, stroke_width=4, tip_length=0.18)), FadeIn(path),
           FadeIn(always_redraw(ball)), FadeIn(at(lab("the law fixes everything next", 26, INK), 2.8, -3.3))]


# ------------------------------------------------------------------ the dropped ball

DROP_X, DROP_TOP, DROP_K = -5.6, 2.2, 0.1134   # the ball's column, its start and screen units per metre
SP = dict(x0=-2.4, y0=-2.4, w=3.4, h=3.6)       # speed against time, 0 to 3 s and 0 to 29.4 m/s
DS = dict(x0=2.9, y0=-2.4, w=3.4, h=3.6)        # distance fallen against time, 0 to 3 s and 0 to 44.1 m


def sp(t, v):
    return P(SP["x0"] + t / 3 * SP["w"], SP["y0"] + v / 29.4 * SP["h"])


def ds(t, d):
    return P(DS["x0"] + t / 3 * DS["w"], DS["y0"] + d / 44.1 * DS["h"])


def graph_frame(f, title, x0, y0, w):
    g = VGroup(axis((x0, y0), (x0 + w + 0.3, y0)), axis((x0, y0), (x0, y0 + 3.75)),
               at(lab(title, 24, INK), x0 + w / 2, 2.4), right_at(lab("time", 22), x0 + w + 0.3, y0 - 0.62))
    for k in (1, 2, 3):
        g.add(at(lab(f"{k} s", 22), f(k, 0)[0], y0 - 0.3))
    return g


def drop_static():
    ground = hline(DROP_X - 0.9, DROP_X + 0.9, -3.05, INK, 4)
    ruler = Line(P(DROP_X - 0.55, DROP_TOP), P(DROP_X - 0.55, -3.0), color=LINE, stroke_width=3)
    return VGroup(ground, ruler)


def drop_ball(tau):
    y = DROP_TOP - DROP_K * 4.9 * tau * tau
    return Dot(P(DROP_X, y), radius=0.2, color=BLUE)


@slide("Take a dropped ball.", "A dropped ball")
def drop1(s):
    yield [FadeIn(drop_static()), FadeIn(drop_ball(0)), FadeIn(at(lab("dropped from rest", 24, INK), DROP_X + 0.2, 2.55))]
    g = Arrow(P(DROP_X + 0.45, DROP_TOP), P(DROP_X + 0.45, DROP_TOP - 1.0), buff=0, color=ORANGE, stroke_width=6, tip_length=0.22)
    yield [GrowArrow(g), FadeIn(left_at(words("gravity: the same downward force at every moment", 26, 28, ORANGE), -3.6, 1.2))]
    yield [FadeIn(left_at(words("so the acceleration is constant too", 26, 28, BLUE), -3.6, -0.4))]


@slide("Its speed grows by nine point eight", "Speed and distance")
def drop2(s):
    t = clock(s, 0.5)   # half speed: three seconds of falling take six on screen
    s.add(drop_static())
    seen = tracker(s)

    def tau():
        return min(t.get_value(), 3.0)

    def ball():
        b = drop_ball(tau())
        return VGroup(b, varrow(b.get_center() + RIGHT * 0.45, DOWN * 0.42 * tau(), BLUE, 5, 0.18))
    live(s, ball)
    live(s, lambda: corners([sp(u, 9.8 * u) for u in np.linspace(0, max(tau(), 1e-3), 40)], BLUE, 4))
    live(s, lambda: corners([ds(u, 4.9 * u * u) for u in np.linspace(0, max(tau(), 1e-3), 40)], BLUE, 4), seen)
    steps = VGroup()
    for k in (0, 1, 2):
        steps.add(DashedLine(sp(k, 9.8 * k), sp(k + 1, 9.8 * k), color=LINE, stroke_width=2.5),
                  Line(sp(k + 1, 9.8 * k), sp(k + 1, 9.8 * (k + 1)), color=MUTED, stroke_width=3))
    yield [FadeIn(graph_frame(sp, "speed", SP["x0"], SP["y0"], SP["w"])), FadeIn(steps),
           FadeIn(at(lab("+9.8 m/s each second", 24, BLUE, True), sp(1.5, 0)[0], 1.9))]
    yield [FadeIn(graph_frame(ds, "distance fallen", DS["x0"], DS["y0"], DS["w"])), *show(seen),
           FadeIn(at(lab("grows with the square of the time", 24, INK), ds(1.5, 0)[0], 1.9))]
    b1 = Line(ds(1, 0), ds(1, 4.9), color=BLUE, stroke_width=7)
    b2 = Line(ds(2, 0), ds(2, 19.6), color=BLUE, stroke_width=7)
    yield [Create(b1), Create(b2), FadeIn(lab("×4", 28, BLUE, True).next_to(b2, LEFT, buff=0.12)),
           FadeIn(at(lab("twice as long, four times as far", 26, INK, True), ds(1.5, 0)[0], -3.4))]


# ------------------------------------------------------------------ two kinds of energy

KX = (-7.3, -2.7)    # the kinetic panel's left and right edges
VXR = (-2.4, 7.3)    # the potential panel's


def panels():
    return VGroup(at(card(None, KX[1] - KX[0], 4.9, TEAL), sum(KX) / 2, -0.35), at(card(None, VXR[1] - VXR[0], 4.9, TEAL), sum(VXR) / 2, -0.35))


def vbar_labels():
    return VGroup(at(lab("V", 24, TEAL, True), 0.9, 0.78), at(lab("V", 24, TEAL, True), 6.75, 0.78))


def roll_ball(t, start):
    run = 0.0 if start["at"] is None else min(t.get_value() - start["at"], 2.6)
    x = -6.7 + 1.0 * run
    return VGroup(Dot(P(x, -0.92), radius=0.2, color=BLUE), Arrow(P(x + 0.22, -0.3), P(x + 1.1, -0.3), buff=0, color=BLUE, stroke_width=5, tip_length=0.2))


def kinetic_done():
    return VGroup(at(T("kinetic energy T", 28, TEAL, True), sum(KX) / 2, 1.65), at(lab("the energy of motion", 24, INK), sum(KX) / 2, 1.1),
                  hline(KX[0] + 0.3, KX[1] - 0.3, -1.14, LINE, 3), roll_ball(ValueTracker(9.0), {"at": 0.0}),
                  at(eq("T = ½ m v²", 40, TEAL), sum(KX) / 2, -2.0), at(lab("mass m, speed v", 22), sum(KX) / 2, -2.6))


@slide("The rest of the chapter works with energies", "Two kinds of energy")
def kinetic(s):
    t = clock(s)
    start = {"at": None}
    yield [FadeIn(panels()[0]), FadeIn(at(lab("from here on: energies rather than forces", 26, INK), 0, 2.35))]
    start["at"] = t.get_value()
    yield [FadeIn(at(T("kinetic energy T", 28, TEAL, True), sum(KX) / 2, 1.65)), FadeIn(at(lab("the energy of motion", 24, INK), sum(KX) / 2, 1.1)),
           FadeIn(hline(KX[0] + 0.3, KX[1] - 0.3, -1.14, LINE, 3)), FadeIn(always_redraw(lambda: roll_ball(t, start)))]
    yield [FadeIn(at(eq("T = ½ m v²", 40, TEAL), sum(KX) / 2, -2.0)), FadeIn(at(lab("mass m, speed v", 22), sum(KX) / 2, -2.6))]


def vbar(x, y, amount, h=2.4, w=0.4):
    """A potential-energy bar of full height h, filled to `amount`."""
    frame = Rectangle(width=w, height=h, stroke_color=LINE, stroke_width=2).move_to(P(x, y + h / 2))
    fill = Rectangle(width=w, height=max(h * amount, 0.002), stroke_width=0, fill_color=TEAL, fill_opacity=0.85)
    fill.move_to(P(x, y + fill.height / 2))
    return VGroup(frame, fill)


@slide("A body can also store energy", "Two kinds of energy")
def potential(s):
    s.add(panels()[0], at(lab("from here on: energies rather than forces", 26, INK), 0, 2.35), kinetic_done())
    hb = tracker(s, 0.0)
    gy = -1.9
    s.add(hline(-1.9, 1.6, gy, INK, 3))
    live(s, lambda: VGroup(Dot(P(-0.3, gy + 0.2 + 2.2 * hb.get_value()), radius=0.2, color=BLUE),
                           DoubleArrow(P(-1.0, gy), P(-1.0, gy + max(2.2 * hb.get_value(), 0.25)), buff=0, color=BLUE, stroke_width=3,
                                       tip_length=0.14, max_tip_length_to_length_ratio=0.5)))
    yield [FadeIn(panels()[1]), hb.animate.set_value(0.5), FadeIn(at(lab("energy stored by where it is", 24, INK), sum(VXR) / 2, 1.1))]
    yield [FadeIn(at(T("potential energy V", 28, TEAL, True), sum(VXR) / 2, 1.65))]
    live(s, lambda: vbar(0.9, gy, hb.get_value()))
    yield [hb.animate.set_value(1.0), FadeIn(at(eq("V = m g x", 30, TEAL), -0.3, -2.55)), FadeIn(vbar_labels()[0]),
           FadeIn(right_at(lab("height x", 22, BLUE), -1.15, gy + 1.1))]
    st = tracker(s, 0.0)
    live(s, lambda: VGroup(spring(st.get_value(), y=-0.6, wall=2.3, rest=4.2, sc=1.2, size=0.6, floor=6.2),
                           vbar(6.75, gy, st.get_value() ** 2)))
    yield [st.animate.set_value(1.0), FadeIn(at(eq("V = ½ k x²", 30, TEAL), 4.5, -2.55)), FadeIn(vbar_labels()[1]),
           FadeIn(at(lab("stiffness k, stretched by x", 22), 4.5, 0.45))]


# ------------------------------------------------------------------ force is minus the slope

VC = (-3.4, -2.4)   # the bottom of the potential-energy curve


def vcurve_pt(x):
    return P(VC[0] + 2.3 * x, VC[1] + 1.25 * x * x)


def vcurve_frame():
    return VGroup(smooth([vcurve_pt(x) for x in np.linspace(-1.6, 1.6, 33)], TEAL, 5),
                  axis((VC[0] - 4.0, VC[1] - 0.35), (VC[0] + 4.1, VC[1] - 0.35)),
                  right_at(lab("position x", 22), VC[0] + 4.1, VC[1] - 0.7),
                  at(lab("potential energy V", 24, TEAL), VC[0], 1.35))


def downhill(x, slope_line=True, push=True):
    p = vcurve_pt(x)
    nrm = np.array([-2.5 * x / 2.3, 1, 0])
    nrm = nrm / np.linalg.norm(nrm)
    d = vcurve_pt(x + 0.3) - vcurve_pt(x - 0.3)
    g = VGroup(Dot(p + nrm * 0.2, radius=0.2, color=BLUE))
    g.add(Line(p - d * 0.9, p + d * 0.9, color=MUTED, stroke_width=3).set_opacity(1 if slope_line else 0))
    g.add(varrow(p + nrm * 0.2 + UP * 0.55, LEFT * 1.3 * x, ORANGE, 6, 0.22).set_opacity(1 if push else 0))
    return g


@slide("The force always pushes a body", "Downhill in potential energy")
def slope1(s):
    t = clock(s)
    s.add(vcurve_frame())
    sl = tracker(s)

    def draw():
        x = 1.35 * np.cos(1.5 * t.get_value())
        g = downhill(x)
        g[1].set_opacity(sl.get_value())
        return g
    live(s, draw)
    yield [FadeIn(left_at(words("the push is always toward lower V: downhill", 30, 26, ORANGE), 1.4, 1.5))]
    yield [sl.animate.set_value(1.0), FadeIn(left_at(words("steeper slope, harder push", 30, 26, INK), 1.4, 0.1))]
    f = left_at(eq("F = −dV/dx", 40, ORANGE), 1.4, -1.3)
    yield [FadeIn(f), FadeIn(left_at(lab("the force: minus the slope of V", 24, INK), 1.4, -2.1))]


@slide("For the ball, that's the steady pull", "Gravity and the spring")
def slope2(s):
    t = clock(s)
    # left: the ball, whose V grows in a straight line with height
    o = P(-6.6, -2.2)
    line = Line(o, o + P(4.4, 3.0), color=TEAL, stroke_width=5)
    fr = VGroup(axis((-6.6, -2.2), (-1.8, -2.2)), axis((-6.6, -2.2), (-6.6, 1.3)), right_at(lab("height x", 22), -1.8, -2.55),
                left_at(lab("V = m g x", 26, TEAL), -6.4, 1.3))

    def ball_pt():
        x = 0.5 + 0.35 * (1 + np.cos(1.2 * t.get_value()))
        p = o + P(4.4, 3.0) * x
        top = p + P(-0.12, 0.17) + UP * 0.55
        return VGroup(Dot(p + P(-0.12, 0.17), radius=0.17, color=BLUE),
                      Arrow(top, top + LEFT * 1.0, buff=0, color=ORANGE, stroke_width=5, tip_length=0.2))
    seen = tracker(s)
    live(s, ball_pt, seen)
    yield [FadeIn(fr), Create(line), *show(seen), FadeIn(at(lab("a straight slope: the same push toward lower height", 22, INK), -3.9, -3.1))]
    # right: the spring, whose V is a bowl around rest
    c = P(4.0, -2.2)

    def bowl(x):
        return c + P(1.6 * x, 1.35 * x * x)
    fr2 = VGroup(smooth([bowl(x) for x in np.linspace(-1.5, 1.5, 31)], TEAL, 5), axis((1.2, -2.5), (6.9, -2.5)),
                 right_at(lab("stretch x", 22), 6.9, -2.85), at(lab("V = ½ k x²", 26, TEAL), 4.0, 1.3), at(lab("rest", 22), 4.0, -2.85))

    def bowl_ball():
        x = 1.3 * np.cos(1.6 * t.get_value())
        p = bowl(x)
        return VGroup(Dot(p + UP * 0.2, radius=0.17, color=BLUE), varrow(p + UP * 0.75, LEFT * 1.1 * x, ORANGE, 5, 0.2))
    seen2 = tracker(s)
    live(s, bowl_ball, seen2)
    yield [FadeIn(fr2), *show(seen2), FadeIn(at(lab("a pull back toward rest", 24, INK), 4.0, -3.3))]
    yield [FadeIn(at(pill("forces in, motion out; the force is the downhill slope of V", INK, 25), 0, 2.2), shift=DOWN * 0.15)]


# ================================================================== where forces get awkward
deck.part("Where forces get awkward")

TRK = P(-3.2, 2.9)
TRR = 4.0


@slide("Where forces get awkward.", "Every force on the body")
def track(s):
    t = clock(s)
    rail = Arc(radius=TRR, start_angle=-PI / 2 - 0.85, angle=1.7, arc_center=TRK, color=LINE, stroke_width=9)
    seen, s1, s2 = tracker(s), tracker(s), tracker(s)

    def bead():
        a = -PI / 2 + 0.6 * np.cos(1.6 * t.get_value())
        p = TRK + TRR * np.array([np.cos(a), np.sin(a), 0])
        n = (TRK - p) / TRR
        g = VGroup(Dot(p, radius=0.2, color=BLUE),
                   Arrow(p + DOWN * 0.2, p + DOWN * 1.2, buff=0, color=ORANGE, stroke_width=5, tip_length=0.2).set_opacity(s1.get_value()),
                   Arrow(p + n * 0.2, p + n * (1.1 + 0.3 * np.cos(a + PI / 2)), buff=0, color=ORANGE, stroke_width=6,
                         tip_length=0.22).set_opacity(s2.get_value()))
        return dim(g, seen.get_value())
    live(s, bead)
    yield [Create(rail), *show(seen), FadeIn(at(lab("a body held on a track", 24, INK), -3.2, -2.75))]
    yield [s1.animate.set_value(1.0), FadeIn(left_at(T("Newton's law needs every force:", 28, INK), 1.2, 1.7)),
           FadeIn(left_at(lab("gravity", 26, ORANGE), 1.6, 0.8))]
    yield [s2.animate.set_value(1.0), FadeIn(left_at(words("the track's push, whose only job is to keep it on track", 26, 26, ORANGE), 1.6, -0.4))]


def pend_live(s, t, seen=None):
    return live(s, lambda: pendulum(swing(t.get_value())), seen)


@slide("Take a pendulum, a weight on a string.", "A pendulum")
def pend1(s):
    t = clock(s)
    s.add(circle_arc())
    seen, nm, fs = tracker(s), tracker(s), tracker(s)
    pend_live(s, t, seen)
    live(s, lambda: dim(VGroup(lab("the bob", 24, BLUE, True).next_to(bob_at(PIV, PL, swing(t.get_value())), LEFT, buff=0.3)), nm.get_value()))
    live(s, lambda: dim(VGroup(gravity_arrow(swing(t.get_value())), tension_arrow(swing(t.get_value()))), fs.get_value()))
    yield [*show(seen), FadeIn(left_at(lab("a weight on a string", 26, INK), 0.9, 1.9))]
    yield [*show(nm)]
    yield [*show(fs), FadeIn(left_at(lab("gravity pulls down", 26, ORANGE), 0.9, 0.7)),
           FadeIn(left_at(lab("the string pulls along itself", 26, ORANGE), 0.9, 0.0))]


def pend_forces(s, t):
    s.add(circle_arc())
    pend_live(s, t)
    live(s, lambda: VGroup(gravity_arrow(swing(t.get_value())), tension_arrow(swing(t.get_value()))))


@slide("Gravity is easy.", "Gravity is known, the tension is not")
def pend2(s):
    t = clock(s)
    pend_forces(s, t)
    g = left_at(lab("gravity", 28, ORANGE, True), 0.9, 1.7)
    yield [FadeIn(g), FadeIn(tick(g)), FadeIn(left_at(lab("the same pull at every moment", 24, INK), 0.9, 1.1))]
    ten = left_at(lab("the string's pull, its tension", 28, ORANGE, True), 0.9, -0.1)
    yield [FadeIn(ten), FadeIn(T("?", 34, ORANGE, True).next_to(ten, RIGHT, buff=0.2)),
           FadeIn(left_at(lab("not known in advance", 24, INK), 0.9, -0.7))]
    yield [FadeIn(left_at(words("it adjusts at every moment to keep the bob on its circle", 26, 24, INK), 0.9, -1.8)),
           Create(Arc(radius=PL, start_angle=-PI / 2 - 0.78, angle=1.56, arc_center=PIV, color=BLUE, stroke_width=3).set_stroke(opacity=0.5))]


@slide("For one pendulum, you can dodge", "The dodge for one pendulum")
def dodge1(s):
    t = clock(s)
    s.add(circle_arc())
    pend_live(s, t)
    tn, mv = tracker(s), tracker(s)
    live(s, lambda: dim(VGroup(tension_arrow(swing(t.get_value()))), tn.get_value()))
    live(s, lambda: dim(VGroup(motion_arrow(swing(t.get_value()), swing_rate(t.get_value())),
                               right_angle(swing(t.get_value()), swing_rate(t.get_value()))), mv.get_value()))
    yield [FadeIn(left_at(words("one pendulum: you can dodge the tension", 24, 28, INK), 0.9, 1.8))]
    yield [*show(tn), FadeIn(left_at(lab("the string pulls straight along itself", 26, ORANGE), 0.9, 0.5))]
    yield [*show(mv), FadeIn(left_at(lab("at right angles to the bob's motion", 26, BLUE), 0.9, -0.2))]


@slide("So it never speeds the bob up", "The dodge for one pendulum")
def dodge2(s):
    t = clock(s)
    s.add(circle_arc(), left_at(words("one pendulum: you can dodge the tension", 24, 28, INK), 0.9, 1.8),
          left_at(lab("the string pulls straight along itself", 26, ORANGE), 0.9, 0.5),
          left_at(lab("at right angles to the bob's motion", 26, BLUE), 0.9, -0.2))
    pend_live(s, t)
    fade, gs = tracker(s, 1.0), tracker(s)
    live(s, lambda: dim(VGroup(tension_arrow(swing(t.get_value()))), fade.get_value()))
    live(s, lambda: VGroup(motion_arrow(swing(t.get_value()), swing_rate(t.get_value())), right_angle(swing(t.get_value()), swing_rate(t.get_value()))))

    def along_circle():
        th = swing(t.get_value())
        b = bob_at(PIV, PL, th)
        return dim(VGroup(gravity_arrow(th), varrow(b - along(th) * np.sign(th) * 0.22, -along(th) * 1.4 * np.sin(th), ORANGE, 7, 0.22)),
                   gs.get_value())
    live(s, along_circle)
    yield [fade.animate.set_value(0.3), FadeIn(left_at(words("so it never speeds the bob up or slows it down", 26, 26, INK), 0.9, -1.2))]
    yield [*show(gs), FadeIn(left_at(words("look only at the forces along the circle", 26, 26, ORANGE), 0.9, -2.4))]


def dodge_card():
    return left_at(card("the dodge: look only along the circle", 6.0, 0.85, INK, 26), 0.9, 1.8)


@slide("But hang a second pendulum", "A second pendulum breaks the dodge")
def double1(s):
    t = clock(s)
    w = tracker(s, 0.0)
    seen = tracker(s)
    live(s, lambda: double(*dp_pose(t.get_value(), w.get_value())), seen)
    dc = dodge_card()
    yield [*show(seen), FadeIn(dc), Create(xmark(dc)), FadeIn(left_at(lab("a second pendulum, hung from the first", 24, INK), 0.9, 1.0))]
    yield [w.animate.set_value(1.0)]
    g, b1, mot, pull, arc = pose_parts()
    yield [GrowArrow(mot), GrowArrow(pull), Create(arc),
           FadeIn(left_at(words("the lower string tugs the upper bob at an angle to its motion", 34, 26, ORANGE), 0.9, -0.2))]
    q = T("?", 40, ORANGE, True).next_to(pull.get_end(), DOWN, buff=0.12)
    yield [FadeIn(q), FadeIn(left_at(words("work out that tension first, before anything else", 34, 26, INK), 0.9, -1.6))]


@slide("We'd like a method that works directly", "What we want instead")
def wanted(s):
    g, b1, mot, pull, arc = pose_parts()
    pull2 = Arrow(b1 + (PIV - b1) / D1 * 0.2, b1 + (PIV - b1) / D1 * 0.9, buff=0, color=ORANGE, stroke_width=6, tip_length=0.2)
    s.add(g, mot, pull)
    a1 = angle_mark(PIV, POSE[0], None, r=0.8, length=2.1)
    a2 = angle_mark(b1, POSE[1], None, r=0.75, length=1.5)
    yield [FadeIn(a1), FadeIn(a2), FadeIn(left_at(words("work directly with the angle of each string", 24, 28, BLUE), 0.9, 1.6))]
    pull2.set_opacity(0.6)
    marks = VGroup(*[cross(Square(0.3).move_to(a.get_end()), RED, 5) for a in (pull, pull2)])
    yield [FadeIn(pull2), pull.animate.set_opacity(0.6), Create(marks),
           FadeIn(left_at(words("never mention the strings' pulls", 24, 28, INK), 0.9, 0.2))]
    tv = left_at(VGroup(chip("T", TEAL, size=32, h=0.8), chip("V", TEAL, size=32, h=0.8)).arrange(RIGHT, buff=0.25), 0.9, -1.4)
    yield [FadeIn(tv), FadeIn(lab("built from energies alone", 26, TEAL, True).next_to(tv, RIGHT, buff=0.35))]


# ================================================================== one number for a whole path
deck.part("One number for a whole path")


@slide("One number for a whole path.", "Energies alone")
def alone(s):
    tv = at(VGroup(chip("T", TEAL, size=34, h=0.9), chip("V", TEAL, size=34, h=0.9)).arrange(RIGHT, buff=0.3), -4.6, 1.3)
    goal = at(T("the motion", 32, BLUE, True), 3.6, 1.3)
    yield [FadeIn(tv), FadeIn(lab("energies alone", 24).next_to(tv, UP, buff=0.2))]
    yield [GrowArrow(arrow(tv, goal)), FadeIn(goal), FadeIn(at(lab("have to pick out", 24, INK), -0.4, 1.75))]
    cons = at(card("conservation of energy:\nT + V stays the same", 6.2, 1.5, TEAL, 28), -2.0, -1.4)
    yield [FadeIn(cons, shift=UP * 0.2), Create(xmark(cons, 0.5, 0.3)), FadeIn(at(lab("not enough", 30, RED, True), 3.5, -1.4))]


@slide("It's one equation, and the double pendulum", "One equation, two angles")
def unknowns(s):
    g, b1, mot, pull, arc = pose_parts()
    a1 = angle_mark(PIV, POSE[0], None, r=1.0, length=2.1)
    a2 = angle_mark(b1, POSE[1], None, r=0.75, length=1.5)
    one = left_at(card("one equation", 3.0, 0.85, TEAL, 28), 0.2, 1.4)
    two = left_at(card("two angles to find", 3.4, 0.85, BLUE, 28), 4.0, 1.4)
    yield [FadeIn(g), FadeIn(a1), FadeIn(a2), FadeIn(one), FadeIn(two), FadeIn(at(T("<", 40, INK, True), 3.6, 1.4))]
    yield [FadeIn(left_at(pill("change the question", INK, 30), 1.8, -0.6), shift=UP * 0.15)]


GF = dict(x0=-5.8, x1=5.9, y0=-2.7, y1=1.1)   # a position-against-time frame


def gp(u, e=0.0, k=1):
    """A path from the fixed start to the fixed end; e and k bend it."""
    x = -4.4 + 9.0 * u
    y = -1.7 + 0.7 * u + 1.9 * np.sin(PI * u) + e * np.sin(k * PI * u)
    return P(x, y)


def gpath(e=0.0, k=1, color=BLUE, width=5):
    return smooth([gp(u, e, k) for u in np.linspace(0, 1, 40)], color, width)


def gframe():
    return VGroup(axis((GF["x0"], GF["y0"]), (GF["x1"], GF["y0"])), axis((GF["x0"], GF["y0"]), (GF["x0"], GF["y1"] + 0.3)),
                  right_at(lab("time", 22), GF["x1"], GF["y0"] - 0.35), left_at(lab("position", 22), GF["x0"] + 0.15, GF["y1"] + 0.3))


@slide("Don't ask how the body accelerates", "Change the question")
def question(s):
    old = at(card("how does it accelerate at each moment?", 8.0, 0.85, MUTED, 28), 0, 2.15)
    yield [FadeIn(old), Create(strike(old, RED))]
    a, b = Dot(gp(0), radius=0.13, color=INK), Dot(gp(1), radius=0.13, color=INK)
    yield [FadeIn(gframe()), FadeIn(a), FadeIn(b), Flash(a, color=INK), Flash(b, color=INK),
           FadeIn(lab("where it is at the start time", 24, INK).next_to(a, DR, buff=0.12)),
           FadeIn(lab("where it is at the end time", 24, INK).next_to(b, DOWN, buff=0.25))]
    cands = VGroup(gpath(-1.4, 1, MUTED, 3), gpath(0.7, 1, MUTED, 3), gpath(0.8, 2, MUTED, 3), gpath(-0.7, 3, MUTED, 3), gpath(0, 1, MUTED, 3))
    yield [LaggedStart(*[Create(c) for c in cands], lag_ratio=0.2), FadeIn(at(T("which path between them?", 30, INK, True), 0, -3.35))]


@slide("Fixing both ends usually pins down", "Both ends fix the motion")
def ends1(s):
    t = clock(s, 0.0)
    pa = VGroup(Dot(P(-6.4, -0.2), radius=0.12, color=INK), Arrow(P(-6.4, -0.2), P(-5.6, 0.7), buff=0, color=BLUE, stroke_width=5, tip_length=0.2),
                smooth([P(-6.4 + 5.0 * u, -0.2 + 2.0 * np.sin(PI * u)) for u in np.linspace(0, 1, 20)], BLUE, 3).set_stroke(opacity=0.5))
    pb = VGroup(Dot(P(0.6, -0.2), radius=0.12, color=INK), Dot(P(5.6, -0.2), radius=0.12, color=INK),
                smooth([P(0.6 + 5.0 * u, -0.2 + 2.0 * np.sin(PI * u)) for u in np.linspace(0, 1, 20)], BLUE, 3).set_stroke(opacity=0.5))
    first = VGroup(pa, pb, at(lab("fix the start and the speed", 24, INK), -3.9, -0.8), at(lab("fix both ends", 24, INK), 3.1, -0.8),
                   at(T("just as well", 30, INK, True), 0, -2.0))
    yield [FadeIn(first)]
    c, fr = throw_frame(-3.3, -0.3, 6.0, 3.6, hmax=8.5)
    hand = VGroup(Dot(c(0, 0), radius=0.12, color=INK), Dot(c(2, 0), radius=0.12, color=INK))

    def ball():
        tau = min(t.get_value(), 2.0)
        return VGroup(corners([c(u, hgt(u)) for u in np.linspace(0, max(tau, 1e-3), 40)], BLUE, 5), Dot(c(tau, hgt(tau)), radius=0.15, color=BLUE))
    t.rate = 1.0
    yield [FadeOut(first), FadeIn(fr), FadeIn(hand), FadeIn(always_redraw(ball)),
           FadeIn(left_at(words("leaves your hand and comes back two seconds later", 22, 26, INK), 1.6, 1.5))]
    slow = smooth([c(u, 6.0 * u - 4.9 * u * u) for u in np.linspace(0, 6.0 / 4.9, 20)], MUTED, 3)
    fast = smooth([c(u, 12.0 * u - 4.9 * u * u) for u in np.linspace(0, 2.25, 30)], MUTED, 3)
    yield [Create(slow), Create(fast), FadeIn(lab("too slow", 22).next_to(c(0.62, 1.9), UP, buff=0.05)),
           FadeIn(lab("too fast", 22).next_to(c(2.25, 0), UR, buff=0.08)),
           FadeIn(left_at(words("only one launch speed lands back on time", 22, 26, BLUE), 1.6, -0.6))]


# ------------------------------------------------------------------ the Lagrangian and the action

TF = dict(cx=-3.3, cy=0.6, w=6.0, h=3.0)


def lag(t):
    """The thrown ball's T − V for a 1 kg ball: ½ v² − 9.8 h."""
    return 48.02 * (1 - t) ** 2 - 9.8 * hgt(t)


def lbars(c, upto=2.0, base=-2.35):
    g = VGroup()
    for k, tm in enumerate(np.arange(0.05, 2.0, 0.1)):
        v = lag(tm) * 0.012
        x = c(tm, 0)[0]
        g.add(Rectangle(width=0.24, height=max(abs(v), 0.01), stroke_width=0, fill_color=PURPLE, fill_opacity=0.8 if tm <= upto else 0)
              .move_to(P(x, base + v / 2)))
    return g


def lbase(c, base=-2.35):
    return Line(P(c(0, 0)[0], base), P(c(2, 0)[0], base), color=LINE, stroke_width=2)


def energy_panel(tm, x0=1.4):
    """Live bars: the kinetic and potential energy at this moment, and their difference."""
    kin = 48.02 * (1 - tm) ** 2 / 48.02
    pot = 9.8 * hgt(tm) / 48.02
    g = VGroup()
    for k, (name, val, col) in enumerate((("kinetic T", kin, TEAL), ("potential V", pot, TEAL))):
        y = 1.6 - 0.75 * k
        g.add(right_at(lab(name, 24, col), x0 + 2.0, y), Rectangle(width=2.6, height=0.36, stroke_color=LINE, stroke_width=2).move_to(P(x0 + 2.3 + 1.3, y)))
        g.add(left_at(Rectangle(width=max(2.6 * val, 0.002), height=0.36, stroke_width=0, fill_color=col, fill_opacity=0.85), x0 + 2.3, y))
    d = kin - pot
    y = 0.1
    g.add(right_at(lab("T − V", 24, PURPLE), x0 + 2.0, y), Rectangle(width=2.6, height=0.36, stroke_color=LINE, stroke_width=2).move_to(P(x0 + 3.6, y)),
          Line(P(x0 + 3.6, y - 0.32), P(x0 + 3.6, y + 0.32), color=INK, stroke_width=3), at(lab("0", 22), x0 + 3.6, y - 0.5))
    bar = Rectangle(width=max(1.3 * abs(d), 0.002), height=0.36, stroke_width=0, fill_color=PURPLE, fill_opacity=0.85)
    (left_at if d >= 0 else right_at)(bar, x0 + 3.6, y)
    g.add(bar)
    return g


@slide("To compare paths, give each one a score.", "A score for each moment")
def score(s):
    t = clock(s, 0.0)
    c, fr = throw_frame(**TF)
    real = throw_path(c)
    yield [FadeIn(fr), Create(real), FadeIn(ends(c)), FadeIn(left_at(words("give each path a score", 22, 26, INK), 1.6, 2.3))]

    def tau():
        return min(t.get_value() / 2.0, 1.999)
    t.rate = 1.0
    yield [FadeIn(always_redraw(lambda: Dot(c(tau(), hgt(tau())), radius=0.15, color=BLUE))), FadeIn(always_redraw(lambda: energy_panel(tau()))),
           FadeIn(lbase(c)), FadeIn(always_redraw(lambda: lbars(c, tau()))), FadeIn(right_at(lab("L", 26, PURPLE, True), c(0, 0)[0] - 0.2, -2.35)),
           FadeIn(at(lab("at each moment: kinetic minus potential", 24, INK), c(1, 0)[0], -3.4))]
    yield [FadeIn(left_at(eq("L = T − V", 40, PURPLE), 1.6, -1.3)), FadeIn(left_at(lab("the Lagrangian", 26, PURPLE, True), 1.6, -2.0))]


@slide("Add it up over the whole trip", "The action of a path")
def action(s):
    c, fr = throw_frame(**TF)
    s.add(fr, throw_path(c), ends(c), left_at(eq("L = T − V", 40, PURPLE), 1.6, -1.3), left_at(lab("the Lagrangian", 26, PURPLE, True), 1.6, -2.0))
    bars = lbars(c)
    base = lbase(c)
    s.add(base, bars)
    S = left_at(VGroup(eq("S = ∫ L dt", 40, PURPLE)), 1.6, 1.5)
    yield [ReplacementTransform(bars, S), FadeOut(base), FadeIn(left_at(lab("add it up over the whole trip", 24, INK), 1.6, 2.3))]
    yield [FadeIn(left_at(lab("the action: one number per path", 28, PURPLE, True), 1.6, 0.6))]
    others = VGroup(throw_path(c, 0.7, MUTED, 3), throw_path(c, -0.6, MUTED, 3))
    tags = VGroup(chip("S", PURPLE, size=22, h=0.48).move_to(c(1.0, hgt(1.0, 0.7)) + UP * 0.45),
                  chip("S", PURPLE, size=22, h=0.48).move_to(c(1.0, hgt(1.0, -0.6)) + DOWN * 0.45))
    yield [LaggedStart(*[Create(o) for o in others], lag_ratio=0.2), FadeIn(tags),
           FadeIn(left_at(words("every imaginable path gets one, even paths the body never takes", 30, 24, INK), 1.6, -3.0))]


# ------------------------------------------------------------------ bending a path

VLY = dict(cx=3.9, cy=-1.7, w=5.2, h=3.0, xname="bend")


def bend_left(e):
    """The bent path in the left panel, drawn from the real path plus a bulge e."""
    return smooth([gp_left(u, e) for u in np.linspace(0, 1, 40)], MUTED, 5)


def gp_left(u, e=0.0):
    return P(-6.6 + 5.4 * u, -1.9 + 0.5 * u + 2.0 * np.sin(PI * u) + 1.4 * e * np.sin(PI * u))


def left_frame():
    a, b = Dot(gp_left(0), radius=0.12, color=INK), Dot(gp_left(1), radius=0.12, color=INK)
    return VGroup(axis((-7.0, -2.5), (-0.7, -2.5)), axis((-7.0, -2.5), (-7.0, 1.9)), right_at(lab("time", 22), -0.7, -2.85),
                  left_at(lab("position", 22), -6.85, 2.1)), VGroup(a, b)


@slide("Here's the rule that picks the real path out.", "Bend a path a little")
def bend1(s):
    e = tracker(s, 0.6)
    fr, ab = left_frame()
    vp, curve, vfr = valley(**VLY)
    live(s, lambda: bend_left(e.get_value()))
    live(s, lambda: Dot(vp(e.get_value()), radius=0.13, color=INK))
    yield [FadeIn(fr), FadeIn(ab), FadeIn(vfr), Create(curve), FadeIn(lab("a path", 24, INK).next_to(gp_left(0.2, 0.8), LEFT, buff=0.15)),
           FadeIn(left_at(lab("its action", 24, INK), vp(0.6)[0] + 0.25, vp(0.6)[1] - 0.35))]
    level = DashedLine(P(vp(0.6)[0] - 0.5, vp(0.6)[1]), P(vp(0.8)[0] + 0.2, vp(0.6)[1]), color=LINE, stroke_width=2.5)
    yield [e.animate.set_value(0.8), Flash(ab[0], color=INK), Flash(ab[1], color=INK), FadeIn(level),
           FadeIn(at(lab("both ends stay fixed", 24, INK), -3.9, -3.3))]
    d = vp(0.68) - vp(0.52)
    d = d / np.linalg.norm(d) * 1.2
    tan = Line(vp(0.6) - d, vp(0.6) + d, color=MUTED, stroke_width=3)
    yield [Create(tan), FadeIn(at(words("on most paths the change is proportional to the bend, like a step on a slope", 40, 24, INK, ORIGIN), 3.9, -3.05))]


@slide("On the real path, that proportional change", "The real path is a flat spot")
def bend2(s):
    e = tracker(s, 0.8)
    fr, ab = left_frame()
    vp, curve, vfr = valley(**VLY)
    s.add(fr, ab, vfr, curve)
    live(s, lambda: bend_left(e.get_value()))
    real = smooth([gp_left(u) for u in np.linspace(0, 1, 40)], BLUE, 5)
    live(s, lambda: Dot(vp(e.get_value()), radius=0.13, color=INK))
    flat = flat_line(vp, 0.45)
    yield [e.animate.set_value(0.0), FadeIn(real), Create(flat), FadeIn(at(lab("the real path", 24, BLUE, True), -3.9, -1.3)),
           FadeIn(at(lab("on the real path, no proportional change", 24, INK), 3.6, 2.2))]
    r1 = rise(vp, 0.5)
    yield [e.animate.set_value(0.5), Create(r1), FadeIn(at(lab("what's left grows like the bend squared", 24, INK), 3.9, -2.75))]
    r2 = rise(vp, 0.25)
    yield [e.animate.set_value(0.25), Create(r2), FadeIn(at(T("bend × ½  →  change × ¼", 28, INK, True), 3.9, -3.4))]


@slide("So for small bends, the action is flat", "The principle of stationary action")
def bend3(s):
    e = tracker(s, 0.25)
    fr, ab = left_frame()
    vp, curve, vfr = valley(**VLY)
    s.add(fr, ab, vfr, curve)
    live(s, lambda: bend_left(e.get_value()))
    s.add(smooth([gp_left(u) for u in np.linspace(0, 1, 40)], BLUE, 5), at(lab("the real path", 24, BLUE, True), -3.9, -1.3))
    live(s, lambda: Dot(vp(e.get_value()), radius=0.13, color=INK))
    bottom = smooth([vp(x) for x in np.linspace(-0.3, 0.3, 9)], PURPLE, 12).set_stroke(opacity=0.5)
    yield [e.animate.set_value(0.0), Create(bottom), FadeIn(at(lab("flat for small bends, like the bottom of a valley", 24, INK), 3.4, 2.2))]
    yield [FadeIn(at(card("the principle of stationary action", 7.0, 0.8, PURPLE, 30), 0, -3.6), shift=UP * 0.15)]


@slide("People often call it least action.", "Stationary, not least")
def stationary(s):
    least = at(hchip("least action", INK, size=32, h=0.9), 0, 1.9)
    yield [FadeIn(least), FadeIn(lab("its other name", 24).next_to(least, LEFT, buff=0.35))]
    v = flat_icon(-4.6, -0.4)
    yield [Create(strike(least)), FadeIn(v), FadeIn(at(lab("a valley floor", 24, INK), -4.6, -1.5)),
           FadeIn(at(lab("the flat spot need not be a minimum", 26, INK, True), 0, -2.8))]
    h = flat_icon(0, 0.3, up=False)
    sd = saddle_icon(4.6, -0.3)
    yield [FadeIn(h), FadeIn(sd), FadeIn(at(lab("a hilltop", 24, INK), 0, -1.5)), FadeIn(at(lab("a saddle", 24, INK), 4.6, -1.5))]


# ------------------------------------------------------------------ the thrown ball

TB = dict(cx=-3.0, cy=-0.4, w=5.4, h=3.8)
VB = dict(cx=4.3, cy=-1.5, w=4.8, h=2.8, xname="")
TB_COL = -6.6   # the ball's own column, left of the time axis


@slide("Let's try it.", "A ball thrown up and caught")
def throw1(s):
    t = clock(s, 0.0)
    c, fr = throw_frame(**TB)
    yield [FadeIn(fr), FadeIn(ends(c)), FadeIn(at(lab("hand", 22), TB_COL, c(0, 0)[1] - 0.35))]

    def tau():
        return min(t.get_value() / 2.0, 2.0)

    def ball():
        tm = tau()
        return VGroup(corners([c(u, hgt(u)) for u in np.linspace(0, max(tm, 1e-3), 40)], BLUE, 5),
                      Dot(c(tm, hgt(tm)), radius=0.11, color=BLUE), Dot(P(TB_COL, c(tm, hgt(tm))[1]), radius=0.18, color=BLUE),
                      DashedVMobject(Line(P(TB_COL + 0.2, c(tm, hgt(tm))[1]), c(tm, hgt(tm)), color=LINE, stroke_width=2), num_dashes=12))
    t.rate = 1.0
    yield [FadeIn(always_redraw(ball)), FadeIn(left_at(words("thrown straight up, caught a couple of seconds later", 30, 24, INK), 1.6, 1.9))]
    seen = tracker(s)
    live(s, lambda: throw_path(c, 0.6, MUTED, 4), seen)
    yield [*show(seen), Flash(ends(c)[0], color=INK), Flash(ends(c)[1], color=INK),
           FadeIn(left_at(words("other paths that leave and come back at the same moments", 30, 24, INK), 1.6, 0.5))]


def throw_base(s, e):
    c, fr = throw_frame(**TB)
    s.add(fr, ends(c), at(lab("hand", 22), TB_COL, c(0, 0)[1] - 0.35))
    live(s, lambda: throw_path(c, e.get_value(), MUTED, 4))
    s.add(throw_path(c))
    return c


@slide("But they bulge higher or lower", "Bulging the path")
def throw2(s):
    e = tracker(s, 0.6)
    c = throw_base(s, e)
    yield [e.animate.set_value(-0.6), FadeIn(left_at(lab("bulge higher or lower", 24, INK), 1.4, 2.35))]
    vp, curve, vfr = valley(**VB)
    seen = tracker(s)
    live(s, lambda: Dot(vp(e.get_value()), radius=0.13, color=INK), seen)
    yield [FadeIn(vfr), Create(curve), *show(seen), e.animate.set_value(0.6),
           FadeIn(at(lab("bent down", 22), vp(-0.8)[0], VB["cy"] - 0.62)), FadeIn(at(lab("bent up", 22), vp(0.8)[0] - 0.3, VB["cy"] - 0.62))]
    yield [Create(rise(vp, -0.6)), Create(rise(vp, 0.6)), FadeIn(at(lab("up or down: the same small rise", 24, INK), VB["cx"], -2.75))]


@slide("And doubling the bulge", "The flat spot")
def throw3(s):
    e = tracker(s, 0.6)
    c = throw_base(s, e)
    vp, curve, vfr = valley(**VB)
    s.add(vfr, curve, rise(vp, -0.6), rise(vp, 0.6), at(lab("bent down", 22), vp(-0.8)[0], VB["cy"] - 0.62),
          at(lab("bent up", 22), vp(0.8)[0] - 0.3, VB["cy"] - 0.62))
    live(s, lambda: Dot(vp(e.get_value()), radius=0.13, color=INK))
    r = rise(vp, 0.3)
    yield [e.animate.set_value(0.3), Create(r), FadeIn(at(T("bulge × 2  →  rise × 4", 28, INK, True), VB["cx"], 2.3))]
    flat = flat_line(vp, 0.35)
    yield [e.animate.set_value(0.0), Create(flat), FadeIn(at(lab("the flat spot", 26, PURPLE, True), VB["cx"], -2.75))]
    yield [Indicate(throw_path(c), color=BLUE), FadeIn(at(lab("the real path: the bottom of the valley", 24, BLUE, True), VB["cx"], -3.4))]


# ================================================================== the Euler-Lagrange equation
deck.part("Turning the rule into an equation")

EL = "d/dt (∂L/∂q̇) = ∂L/∂q"


@slide("Turning the rule into an equation.", "Checking is not finding")
def el1(s):
    c, fr = throw_frame(-3.6, -0.2, 5.4, 3.4, ticks=False)
    guess = throw_path(c, 0.0, BLUE, 5)
    yield [FadeIn(fr), Create(guess), FadeIn(at(lab("a guess", 24, BLUE), -3.6, 2.3))]
    near = VGroup(throw_path(c, 0.25, MUTED, 3), throw_path(c, -0.25, MUTED, 3))
    yield [Create(near), FadeIn(at(VGroup(lab("compare with its neighbours", 24, INK), check()).arrange(RIGHT, buff=0.2), -3.6, -3.25))]
    c2, fr2 = throw_frame(3.6, -0.2, 5.4, 3.4, ticks=False)
    many = VGroup(*[throw_path(c2, e, MUTED, 2.5) for e in np.linspace(-0.8, 0.8, 9)],
                  *[smooth([c2(u, hgt(u) * k + 1.5 * np.sin(PI * u * m) * k) for u in np.linspace(0, 2, 30)], MUTED, 2.5) for k, m in ((0.6, 2), (0.9, 3))])
    note = at(lab("endless paths: it can't find the real one", 24, INK), 3.4, -3.25)
    yield [FadeIn(fr2), LaggedStart(*[Create(m) for m in many], lag_ratio=0.08), FadeIn(note), FadeIn(xmark(note, 0.36, 0.15))]


@slide("For that, we need an equation", "The Euler-Lagrange equation")
def el2(s):
    c, fr = throw_frame(-3.6, 0.75, 5.4, 3.0, ticks=False)
    real = throw_path(c)
    ticks_ = VGroup(*[Line(c(tm, hgt(tm)) + DOWN * 0.14, c(tm, hgt(tm)) + UP * 0.14, color=BLUE, stroke_width=4) for tm in np.linspace(0.15, 1.85, 11)])
    yield [FadeIn(fr), Create(real), LaggedStart(*[FadeIn(k, scale=1.6) for k in ticks_], lag_ratio=0.1),
           FadeIn(left_at(words("an equation the real path obeys at every moment", 24, 26, INK), 1.4, 1.6))]
    v = flat_icon(3.8, -0.2)
    yield [FadeIn(v), FadeIn(left_at(lab("every small bend leaves the action flat", 24, INK), 1.0, -1.05))]
    e = at(eq(EL, 46, PURPLE), 0, -2.0)
    yield [FadeIn(e, shift=UP * 0.15), FadeIn(at(lab("the Euler-Lagrange equation", 26, PURPLE, True), 0, -2.8)),
           FadeIn(at(lab("q: the position (a height, an angle, ...);  q̇: how fast it changes", 22, INK), 0, -3.45))]


APEX = P(0, 0.45)


def balance():
    fulcrum = Polygon(APEX, APEX + P(-0.5, -0.75), APEX + P(0.5, -0.75), color=MUTED, fill_color=MUTED, fill_opacity=0.5, stroke_width=2)
    beam = Line(APEX + LEFT * 5.6, APEX + RIGHT * 5.6, color=INK, stroke_width=7)
    left = at(card("d/dt (∂L/∂q̇)", 3.6, 1.0, BLUE, 32), -3.6, 1.35)
    right = at(card("∂L/∂q", 3.6, 1.0, ORANGE, 32), 3.6, 1.35)
    return VGroup(fulcrum, beam), left, right, at(eq("=", 44), 0, 1.35)


KS, KP = P(-3.6, -1.2), P(3.6, -1.2)   # the speed knob and the position knob


def knobs(s, ks, kp):
    live(s, lambda: knob(KS, ks.get_value(), "speed"))
    live(s, lambda: knob(KP, kp.get_value(), "position"))
    live(s, lambda: VGroup(meter(-2.6, -0.85, min(ks.get_value() / 0.8, 1.0)), meter(4.6, -0.85, min(kp.get_value() / 0.8, 1.0))))


@slide("It reads as a balance", "Two sides of a balance")
def bal1(s):
    beam, left, right, equals = balance()
    yield [FadeIn(beam), FadeIn(left), FadeIn(right), FadeIn(equals), FadeIn(at(lab("the Euler-Lagrange equation", 24, PURPLE), 0, 2.3))]
    ks, kp = tracker(s), tracker(s)
    seen = tracker(s)
    live(s, lambda: dim(VGroup(knob(KS, ks.get_value(), "speed"), knob(KP, kp.get_value(), "position")), seen.get_value()))
    live(s, lambda: dim(VGroup(meter(-2.6, -0.85, min(ks.get_value() / 0.8, 1.0)), meter(4.6, -0.85, min(kp.get_value() / 0.8, 1.0)),
                               left_at(lab("change in L", 22, PURPLE), -2.6, -0.45), left_at(lab("change in L", 22, PURPLE), 4.6, -0.45)),
                        seen.get_value()))
    yield [*show(seen), FadeIn(at(lab("speed and position: two separate knobs", 24, INK), 0, -3.35))]
    yield [ks.animate.set_value(0.8)]


def bal_state(s, kp0=0.0):
    beam, left, right, equals = balance()
    s.add(beam, left, right, equals, at(lab("the Euler-Lagrange equation", 24, PURPLE), 0, 2.3))
    ks, kp = tracker(s, 0.8), tracker(s, kp0)
    knobs(s, ks, kp)
    s.add(left_at(lab("change in L", 22, PURPLE), -2.6, -0.45), left_at(lab("change in L", 22, PURPLE), 4.6, -0.45))
    return ks, kp, left, right


@slide("For an ordinary body, that's the mass", "Speed knob: momentum; position knob: force")
def bal2(s):
    ks, kp, left, right = bal_state(s)
    mom = at(lab("m v: the momentum p", 26, BLUE, True), -3.6, -2.95)
    yield [FadeIn(mom), Indicate(left, color=BLUE)]
    yield [kp.animate.set_value(0.8)]
    yield [FadeIn(at(lab("plays the role of the force", 26, ORANGE, True), 3.6, -2.95)), Indicate(right, color=ORANGE)]


@slide("The equation says the momentum changes", "Momentum changes at the rate the force sets")
def bal3(s):
    beam, left, right, equals = balance()
    s.add(beam, left, right, equals, at(lab("the Euler-Lagrange equation", 24, PURPLE), 0, 2.3))
    l2 = at(card("how fast the\nmomentum changes", 3.6, 1.0, BLUE, 26), -3.6, 1.35)
    r2 = at(card("the force", 3.6, 1.0, ORANGE, 28), 3.6, 1.35)
    yield [Transform(left, l2), Transform(right, r2)]
    nw = at(VGroup(lab("what Newton said:", 26, INK), eq("F = m a", 34), check()).arrange(RIGHT, buff=0.3), 0, -0.9)
    yield [FadeIn(nw)]
    chips = VGroup(hchip("a height", BLUE), hchip("an angle", BLUE), hchip("anything", BLUE)).arrange(RIGHT, buff=0.3)
    at(chips, 1.6, -2.3)
    yield [FadeIn(chips), FadeIn(right_at(lab("in whatever coordinate you choose:", 24, INK), chips.get_left()[0] - 0.3, -2.3))]


@slide("Only the potential energy depends on position.", "Nudging the position")
def nudge(s):
    t = clock(s)
    l = VGroup(eq("L =", 44, PURPLE), eq("½ m v²", 44, TEAL), eq("−", 44), eq("V(x)", 44, TEAL)).arrange(RIGHT, buff=0.25)
    at(l, 0, 2.0)
    br = Brace(l[3], DOWN, color=TEAL)
    yield [FadeIn(l), FadeIn(br), FadeIn(lab("the only part that depends on position", 24, INK).next_to(br, DOWN, buff=0.1).shift(RIGHT * 1.2))]
    def bp(u):
        return P(-3.4 + 1.5 * u, -2.6 + 0.8 * u * u)
    small = VGroup(smooth([bp(u) for u in np.linspace(-1.6, 1.6, 31)], TEAL, 5), axis((-6.2, -2.85), (-0.6, -2.85)),
                   right_at(lab("position x", 22), -0.6, -3.2), axis((-6.2, -2.85), (-6.2, -0.4)), at(lab("V", 26, TEAL, True), -6.2, -0.1))

    def mini():
        x = 1.35 * np.cos(1.5 * t.get_value())
        p = bp(x)
        return VGroup(Dot(p + UP * 0.2, radius=0.18, color=BLUE), varrow(p + UP * 0.7, LEFT * 0.9 * x, ORANGE, 5, 0.2))
    seen = tracker(s)
    live(s, mini, seen)
    yield [FadeIn(small), *show(seen), FadeIn(left_at(eq("−dV/dx", 40, ORANGE), 1.4, -0.8)),
           FadeIn(left_at(lab("minus its slope: the force from earlier", 26, ORANGE), 1.4, -1.6))]


@slide("For a body moving along a line, the equation", "Newton's law comes back")
def newton_back(s):
    t = clock(s, 0.0)
    r = at(VGroup(eq("m a = −dV/dx", 40), eq("=", 40), eq("F", 40, ORANGE)).arrange(RIGHT, buff=0.3), -1.2, 1.9)
    yield [FadeIn(r), FadeIn(tick(r, buff=0.35)), FadeIn(at(lab("exactly Newton's law, F = m a", 26, INK), -1.2, 1.1))]
    c, fr = throw_frame(-3.0, -1.4, 5.0, 2.4)
    t.rate = 1.0

    def ball():
        tm = min(t.get_value() / 2.0, 2.0)
        p = c(tm, hgt(tm))
        return VGroup(Dot(p, radius=0.15, color=BLUE), Arrow(p + DOWN * 0.18, p + DOWN * 0.9, buff=0, color=BLUE, stroke_width=5, tip_length=0.18))
    yield [FadeIn(fr), FadeIn(throw_path(c, 0.0, BLUE, 3).set_stroke(opacity=0.5)), FadeIn(always_redraw(ball)),
           FadeIn(left_at(words("the thrown ball: accelerates downward at 9.8 m/s every second", 24, 26, BLUE), 1.4, -1.4))]


# ------------------------------------------------------------------ the pendulum by its angle

@slide("Now describe the pendulum by its angle.", "The pendulum by its angle")
def ang1(s):
    t = clock(s)
    s.add(circle_arc())
    pend_live(s, t)
    am, hb = tracker(s), tracker(s)
    live(s, lambda: dim(angle_mark(PIV, swing(t.get_value()), "θ", r=1.1, length=PL + 0.3), am.get_value()))

    def height():
        th = swing(t.get_value())
        b = bob_at(PIV, PL, th)
        low = PIV[1] - PL
        return dim(VGroup(dashed((-6.6, low), (-0.6, low), LINE, 2, 24),
                          Line(P(b[0] + 0.45, low), P(b[0] + 0.45, max(b[1], low + 0.01)), color=BLUE, stroke_width=10),
                          lab("height", 22, BLUE).next_to(P(b[0] + 0.55, low), DR, buff=0.1)), hb.get_value())
    live(s, height)
    live(s, lambda: T("ℓ", 30, INK, True).move_to((PIV + bob_at(PIV, PL, swing(t.get_value()))) / 2
                                                     + along(swing(t.get_value())) * 0.32))
    yield [FadeIn(left_at(words("describe it by one angle", 24, 28, INK), 0.9, 1.9))]
    yield [*show(am), FadeIn(left_at(lab("θ: measured from straight down", 26, BLUE, True), 0.9, 1.0))]
    yield [*show(hb), FadeIn(left_at(lab("its height depends only on θ", 26, INK), 0.9, -0.1)),
           FadeIn(left_at(eq("height = ℓ (1 − cos θ)", 30, BLUE), 0.9, -0.8))]


@slide("Its speed depends only on how fast", "The Lagrangian in the angle")
def ang2(s):
    t = clock(s)
    s.add(circle_arc(), left_at(lab("θ: measured from straight down", 26, BLUE, True), 0.9, 1.9))
    pend_live(s, t)
    live(s, lambda: angle_mark(PIV, swing(t.get_value()), "θ", r=1.1, length=PL + 0.3))
    sp_ = tracker(s)
    live(s, lambda: dim(VGroup(motion_arrow(swing(t.get_value()), swing_rate(t.get_value()))), sp_.get_value()))
    yield [*show(sp_), FadeIn(left_at(eq("speed = ℓ θ̇", 30, BLUE), 0.9, 1.1)), FadeIn(left_at(lab("θ̇: how fast θ changes", 22), 0.9, 0.5))]
    L = left_at(eq("L = ½ m ℓ² θ̇² − m g ℓ (1 − cos θ)", 30, PURPLE), 0.2, -0.6)
    yield [FadeIn(L), FadeIn(left_at(lab("only θ and θ̇", 24, PURPLE), 0.2, -1.25))]
    ten = left_at(hchip("the string's pull", ORANGE), 0.9, -2.4)
    xm = xmark(ten, 0.36, 0.2)
    yield [FadeIn(ten), Create(xm), FadeIn(lab("never appears in L", 26, INK).next_to(xm, RIGHT, buff=0.3))]


@slide("The Euler-Lagrange equation then gives", "No tension anywhere")
def ang3(s):
    t = clock(s)
    one = VGroup(circle_arc())
    s.add(one)
    seen1 = tracker(s, 1.0)
    live(s, lambda: dim(VGroup(pendulum(swing(t.get_value())), angle_mark(PIV, swing(t.get_value()), "θ", r=1.1, length=PL + 0.3)), seen1.get_value()))
    res = left_at(eq("m ℓ² θ̈ + m g ℓ sin θ = 0", 32, INK), 0.6, 1.6)
    nt = left_at(lab("its motion, with no tension anywhere", 24, TEAL), 0.6, 0.9)
    yield [FadeIn(res), FadeIn(nt), FadeIn(tick(nt, buff=0.15))]
    seen2 = tracker(s)

    def two():
        a, b = dp_angles(t.get_value())
        b1 = bob_at(PIV, D1, a)
        return VGroup(double(a, b), angle_mark(PIV, a, "θ₁", r=0.95, length=2.1), angle_mark(b1, b, "θ₂", r=0.7, length=1.5))
    live(s, lambda: dim(two(), seen2.get_value()))
    yield [seen1.animate.set_value(0.0), FadeOut(one), *show(seen2), FadeIn(left_at(words("the double pendulum: write L in the two angles", 26, 26, INK), 0.6, -0.5))]


@slide("You get one equation for each angle", "The method we asked for")
def ang4(s):
    t = clock(s)

    def two():
        a, b = dp_angles(t.get_value())
        b1 = bob_at(PIV, D1, a)
        return VGroup(double(a, b), angle_mark(PIV, a, "θ₁", r=0.95, length=2.1), angle_mark(b1, b, "θ₂", r=0.7, length=1.5))
    live(s, two)
    s.add(left_at(words("the double pendulum: write L in the two angles", 26, 26, INK), 0.6, 2.0))
    e1 = left_at(card("Euler-Lagrange for θ₁", 4.2, 0.8, PURPLE, 26), 0.6, 0.6)
    e2 = left_at(card("Euler-Lagrange for θ₂", 4.2, 0.8, PURPLE, 26), 0.6, -0.4)
    nt = left_at(lab("again no tension", 26, TEAL), 0.6, -1.15)
    yield [FadeIn(e1), FadeIn(e2), FadeIn(nt), FadeIn(tick(nt, buff=0.15))]
    goal = left_at(card("works with the angles,\nnever mentions the strings' pulls", 6.0, 1.4, TEAL, 26), 0.6, -2.55)
    yield [FadeIn(goal, shift=UP * 0.15), FadeIn(tick(goal, buff=0.25))]


# ------------------------------------------------------------------ a missing coordinate

FLOAT_Y = -1.6


def float_block(x, p=True):
    g = VGroup(Square(0.9, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to(P(x, FLOAT_Y)))
    if p:
        g.add(Arrow(P(x + 0.5, FLOAT_Y + 0.85), P(x + 1.6, FLOAT_Y + 0.85), buff=0, color=BLUE, stroke_width=5, tip_length=0.2),
              T("p", 26, BLUE, True).move_to(P(x + 1.05, FLOAT_Y + 1.2)))
    return g


@slide("One more thing drops out.", "A missing coordinate")
def missing1(s):
    e = at(VGroup(eq("d/dt (∂L/∂q̇)", 40, BLUE), eq("=", 40), eq("∂L/∂q", 40, ORANGE)).arrange(RIGHT, buff=0.3), 0, 1.9)
    yield [FadeIn(e), FadeIn(at(lab("one more thing drops out", 26, INK), 0, 2.45))]
    z = eq("= 0", 40, ORANGE).next_to(e, RIGHT, buff=0.25)
    yield [FadeIn(z), FadeIn(at(lab("if L doesn't depend on that coordinate at all", 26, INK), 0, 1.05))]
    dots = VGroup(*[Dot(P(x, y), radius=0.03, color=LINE) for x, y in np.random.default_rng(5).uniform([-7, -2.3], [7, 0.3], size=(34, 2))])
    yield [FadeIn(dots), FadeIn(float_block(-3.0, False)), FadeIn(at(lab("a body floating freely", 26, INK), -3.0, -2.75))]


@slide("Its Lagrangian cares only how fast", "Its momentum never changes")
def missing2(s):
    t = clock(s)
    dots = VGroup(*[Dot(P(x, y), radius=0.03, color=LINE) for x, y in np.random.default_rng(5).uniform([-7, -2.3], [7, 0.3], size=(34, 2))])
    s.add(dots)
    pseen = tracker(s)

    def body():
        x = -3.0 + 0.3 * min(t.get_value(), 18.0)
        g = float_block(x)
        g[1:].set_opacity(pseen.get_value())
        return g
    live(s, body)
    l = at(eq("L = ½ m v²", 40, PURPLE), -3.0, 1.9)
    yield [FadeIn(l), FadeIn(at(lab("only how fast it moves, not where it is", 24, INK), -3.0, 1.15))]
    yield [*show(pseen), FadeIn(at(eq("∂L/∂x = 0", 36, ORANGE), 3.6, 1.9)),
           FadeIn(at(lab("so the momentum never changes", 26, BLUE, True), 3.6, 1.15))]


@slide("Shifting the system along that coordinate", "A symmetry")
def sym(s):
    dots = VGroup(*[Dot(P(x, y), radius=0.03, color=LINE) for x, y in np.random.default_rng(5).uniform([-7, -2.3], [7, 0.3], size=(34, 2))])
    s.add(dots)
    blk = float_block(-5.0)
    s.add(blk)
    ghost = float_block(-5.0, False).set_opacity(0.15)
    yield [FadeIn(ghost), blk.animate.shift(RIGHT * 3.0), FadeIn(at(lab("shift it along: nothing changes", 26, INK), 0, 2.3))]
    yield [FadeIn(at(pill("a symmetry", BLUE, 30), 0, 1.3))]
    q = at(card("a quantity that stays fixed:\nhere, the momentum", 6.4, 1.3, BLUE, 26), 3.6, -3.0)
    yield [FadeIn(q, shift=UP * 0.15), GrowArrow(Arrow(P(0, 0.85), P(2.4, -2.3), buff=0.1, color=MUTED, stroke_width=4, tip_length=0.2))]


@slide("A later chapter states this link", "Noether's theorem")
def noether(s):
    a = at(card("symmetry", 3.2, 1.0, BLUE, 30), -4.6, 1.3)
    b = at(card("a fixed quantity", 3.6, 1.0, BLUE, 30), 0.4, 1.3)
    s.add(a, b, arrow(a, b))
    n = at(card("Noether's theorem", 4.6, 1.0, PURPLE, 30), -2.1, -0.6)
    yield [FadeIn(n, shift=UP * 0.15), FadeIn(at(lab("a later chapter states the link in general", 24, INK), -2.1, -1.4))]
    c = at(card("conservation of\nelectric charge", 4.2, 1.3, INK, 28), 4.4, -0.6)
    yield [GrowArrow(arrow(n, c)), FadeIn(c), FadeIn(at(lab("another chapter uses it", 24, INK), 4.4, -1.6))]


# ================================================================== a state
deck.part("A state is position plus momentum")


@slide("A state is position plus momentum.", "Whole paths, or one instant")
def state1(s):
    c, fr = throw_frame(-3.6, -0.4, 5.6, 3.4, ticks=False)
    yield [FadeIn(fr), Create(throw_path(c)), FadeIn(ends(c)), FadeIn(at(lab("so far: whole paths between two fixed ends", 24, INK), -3.4, 2.3))]
    qm = at(card("quantum mechanics\nworks differently", 5.0, 1.6, INK, 30), 4.2, -0.2)
    yield [FadeIn(qm, shift=LEFT * 0.2)]


@slide("It describes a system at one instant", "One instant, carried forward")
def state2(s):
    tl = Arrow(P(-6.8, -1.6), P(6.8, -1.6), buff=0, color=MUTED, stroke_width=4, tip_length=0.25)
    now = Line(P(-3.6, -1.85), P(-3.6, -1.35), color=INK, stroke_width=4)
    snap = icon_spring(-3.6, 0.3, 0.5)
    later = icon_spring(3.6, 0.3, -0.7)
    yield [GrowArrow(tl), FadeIn(now), FadeIn(snap), FadeIn(at(lab("one instant", 24, INK), -3.6, -2.2)), FadeIn(right_at(lab("time", 22), 6.8, -2.0)),
           GrowArrow(Arrow(P(-1.8, 0.3), P(1.8, 0.3), buff=0, color=MUTED, stroke_width=4, tip_length=0.2)), FadeIn(later),
           FadeIn(at(lab("a rule carries it forward", 24, INK), 0, 0.85))]
    yield [FadeIn(at(lab("we need the classical version of the system at one instant", 26, INK), 0, 2.2))]
    yield [FadeIn(at(pill("the state", BLUE, 32), -3.6, 1.5))]


ROWS = (1.2, -1.5)   # the two springs' heights


def two_rows(t, xs):
    """Two springs passing the middle at the same moment, one moving each way."""
    g = VGroup()
    for k, y in enumerate(ROWS):
        x = xs(k)
        g.add(spring(x, y=y, wall=-6.8, rest=-3.2, sc=1.3, size=0.7, floor=-0.6))
    return g


@slide("Position alone isn't enough.", "The same position, twice")
def passes(s):
    t = clock(s, 0.0)
    for y in ROWS:
        s.add(rest_mark(y, -3.2))

    def xs(k):
        return (-1 if k == 0 else 1) * 0.9 * np.sin(2 * t.get_value())

    def arrows():
        g = VGroup()
        for k, y in enumerate(ROWS):
            x = xs(k)
            v = (-1 if k == 0 else 1) * 1.8 * np.cos(2 * t.get_value())
            g.add(varrow(P(-3.2 + 1.3 * x, y + 0.65), RIGHT * 0.7 * v, BLUE, 5, 0.2))
        return g
    live(s, lambda: two_rows(t, xs))
    av = tracker(s)
    live(s, lambda: dim(arrows(), av.get_value()))
    yield [FadeIn(left_at(lab("both at the middle", 26, INK), 0.6, 1.2)), FadeIn(left_at(lab("position alone: the same", 26, INK), 0.6, 0.6))]
    t.rate = 1.0
    yield [*show(av), FadeIn(left_at(lab("once going each way", 26, BLUE, True), 0.6, -0.4))]
    yield [FadeIn(left_at(words("what happens next is different", 34, 26, INK), 0.6, -1.4))]


@slide("So the state also has to say", "The conjugate momentum")
def conj(s):
    for k, y in enumerate(ROWS):
        s.add(rest_mark(y, -3.2), spring(0, y=y, wall=-6.8, rest=-3.2, sc=1.3, size=0.7, floor=-0.6))
    ps = VGroup(*[Arrow(P(-3.2, y + 0.65), P(-3.2 + (-1.3 if k == 0 else 1.3), y + 0.65), buff=0, color=BLUE, stroke_width=6, tip_length=0.22)
                  for k, y in enumerate(ROWS)])
    yield [GrowArrow(ps[0]), GrowArrow(ps[1]), FadeIn(left_at(lab("also say how it is moving", 26, INK), 0.6, 1.6))]
    yield [FadeIn(left_at(eq("p = ∂L/∂q̇", 34, BLUE), 0.6, 0.6)), FadeIn(left_at(lab("the momentum from the Euler-Lagrange equation", 22), 0.6, 0.0))]
    yield [FadeIn(left_at(pill("the conjugate momentum", BLUE, 28), 0.6, -1.1))]


@slide("For a body moving along a line, it's the ordinary", "Momentum for a line and for a pendulum")
def conj2(s):
    blk = Square(0.8, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to(P(-4.6, 1.0))
    yield [FadeIn(hline(-6.6, -2.6, 0.58, LINE, 3)), FadeIn(blk), GrowArrow(Arrow(P(-4.1, 1.0), P(-3.0, 1.0), buff=0, color=BLUE, stroke_width=5, tip_length=0.2)),
           FadeIn(left_at(eq("on a line:  p = m v", 32, BLUE), -0.8, 1.0)), FadeIn(left_at(lab("mass times velocity", 24), -0.8, 0.4))]
    pv = P(-4.6, -0.6)
    th = 0.4
    pd = pendulum(th, pv, 1.6, 0.17)
    b = bob_at(pv, 1.6, th)
    turn = Arc(radius=0.9, start_angle=-PI / 2 - 0.1, angle=0.9, arc_center=pv, color=BLUE, stroke_width=4).add_tip(tip_length=0.18)
    yield [FadeIn(pd), Create(turn), FadeIn(left_at(eq("the pendulum:  an angular momentum", 32, BLUE), -0.8, -1.3))]
    yield [FadeIn(at(pill("why momentum, not plain velocity: at the end of the chapter", INK, 25), 0, -3.2), shift=UP * 0.15)]


@slide("So the state is a pair", "A point on a map")
def pmap(s):
    pair = left_at(hchip("state = (position, momentum)", BLUE, size=28, h=0.85), -7.0, 1.6)
    yield [FadeIn(pair)]
    yield [FadeIn(phase_frame()), FadeIn(left_at(words("position across, momentum up", 30, 26, INK), -7.0, 0.7))]
    b, d = Dot(pp(0, -2), radius=0.14, color=BLUE), Dot(pp(0, 2), radius=0.14, color=BLUE)
    tags = VGroup(left_at(lab("(0, −2): moving left", 24, BLUE), PX + 0.3, PY - 2.3),
                  left_at(lab("(0, 2): moving right", 24, BLUE), PX + 0.3, PY + 2.3))
    icons = VGroup(spring(0, y=-0.7, wall=-6.8, rest=-4.6, sc=1.0, size=0.6, floor=-3.4),
                   Arrow(P(-4.6, -0.15), P(-3.7, -0.15), buff=0, color=BLUE, stroke_width=5, tip_length=0.18),
                   spring(0, y=-2.4, wall=-6.8, rest=-4.6, sc=1.0, size=0.6, floor=-3.4),
                   Arrow(P(-4.6, -1.85), P(-5.5, -1.85), buff=0, color=BLUE, stroke_width=5, tip_length=0.18))
    yield [FadeIn(icons), FadeIn(b), FadeIn(d), FadeIn(tags), Flash(b, color=BLUE), Flash(d, color=BLUE),
           FadeIn(left_at(lab("the two passes: two different points", 24, INK), -3.0, -1.5))]


@slide("We call that map of all possible states", "Phase space")
def pspace(s):
    t = clock(s)
    s.add(phase_frame(), left_at(hchip("state = (position, momentum)", BLUE, size=28, h=0.85), -7.0, 2.25))
    yield [FadeIn(left_at(T("phase space", 34, BLUE, True), -7.0, 1.3)), FadeIn(left_at(lab("the map of all possible states", 24, INK), -7.0, 0.7))]
    seen = tracker(s)
    live(s, lambda: dim(VGroup(spring(osc_x(t.get_value()), y=-1.4, wall=-7.2, rest=-4.6, sc=1.1, size=0.7, floor=-2.4),
                               trace(t.get_value()), phase_dot(t.get_value())), seen.get_value()))
    yield [*show(seen), FadeIn(at(lab("as it moves, its point traces a curve", 24, INK), -4.4, -2.6))]


# ================================================================== the Hamiltonian
deck.part("The energy moves the state")

ST = -3 * PI / 16   # the state used for Hamilton's equations, chosen with a large momentum so both arrows show


def st_xp():
    return osc_x(ST), osc_p(ST)


def st_dot():
    return Dot(pp(*st_xp()), radius=0.14, color=BLUE)


@slide("The energy moves the state.", "A rule to move the state")
def ham1(s):
    d = st_dot()
    q = T("?", 36, INK, True).next_to(d, RIGHT, buff=0.25)
    yield [FadeIn(phase_frame()), FadeIn(orbit(color=LINE, width=3)), FadeIn(d)]
    yield [FadeIn(q), FadeIn(left_at(words("a rule that moves the state forward, written in position and momentum", 26, 26, INK), -7.0, 1.5))]
    h = left_at(card("one function:\nthe Hamiltonian H", 4.6, 1.4, PURPLE, 28), -7.0, -0.6)
    yield [FadeIn(h, shift=UP * 0.15)]


def ham_base(s):
    s.add(phase_frame(), orbit(color=LINE, width=3), st_dot())


@slide("For everything in this chapter, it's the total", "The energy, written with momentum")
def ham2(s):
    ham_base(s)
    h = left_at(eq("H = T + V", 44, PURPLE), -7.0, 1.6)
    yield [FadeIn(h), FadeIn(left_at(lab("the total energy, kinetic plus potential", 24, INK), -7.0, 0.85))]
    t_ = left_at(eq("T = ½ m v²", 36, TEAL), -7.0, -0.4)
    yield [FadeIn(t_), FadeIn(left_at(lab("write it with momentum, not speed", 24, INK), -7.0, -1.15))]


@slide("Speed is momentum over mass.", "The Hamiltonian")
def ham3(s):
    ham_base(s)
    a = left_at(eq("v = p / m", 36, BLUE), -7.0, 1.6)
    yield [FadeIn(a), FadeIn(left_at(lab("speed is momentum over mass", 24, INK), -7.0, 0.95))]
    b = left_at(eq("½ m v²  =  p² / 2m", 36, TEAL), -7.0, -0.1)
    h = left_at(eq("H = p²/2m + V", 44, PURPLE), -7.0, -1.5)
    yield [FadeIn(b), FadeIn(h, shift=UP * 0.15), FadeIn(left_at(lab("the Hamiltonian", 26, PURPLE, True), -7.0, -2.3))]


def ham_arrows(k=0.45):
    x, p = st_xp()
    o = pp(x, p)
    hx = Arrow(o, o + RIGHT * k * p * PXS, buff=0.12, color=BLUE, stroke_width=6, tip_length=0.22)
    hp = Arrow(o, o + UP * k * (-4 * x) * PPS, buff=0.12, color=ORANGE, stroke_width=6, tip_length=0.22)
    both = Arrow(o, o + RIGHT * k * p * PXS + UP * k * (-4 * x) * PPS, buff=0.12, color=INK, stroke_width=6, tip_length=0.22)
    return hx, hp, both


@slide("The Hamiltonian moves the state through two rules", "Hamilton's first equation")
def hamq(s):
    ham_base(s)
    hx, hp, both = ham_arrows()
    yield [FadeIn(left_at(T("Hamilton's equations", 32, PURPLE, True), -7.0, 2.2)), FadeIn(left_at(eq("H = p²/2m + V", 30, PURPLE), -7.0, 1.5))]
    yield [FadeIn(left_at(eq("ẋ = ∂H/∂p", 38, BLUE), -7.0, 0.4)), GrowArrow(hx),
           FadeIn(left_at(lab("position's rate: how H depends on momentum", 22), -7.0, -0.25))]
    yield [FadeIn(left_at(eq("= p / m, the velocity", 30, BLUE), -6.4, -0.85))]


@slide("The second says momentum changes", "Hamilton's second equation")
def hamp(s):
    ham_base(s)
    hx, hp, both = ham_arrows()
    s.add(left_at(T("Hamilton's equations", 32, PURPLE, True), -7.0, 2.2), left_at(eq("H = p²/2m + V", 30, PURPLE), -7.0, 1.5),
          left_at(eq("ẋ = ∂H/∂p", 38, BLUE), -7.0, 0.4), hx, left_at(eq("= p / m, the velocity", 30, BLUE), -6.4, -0.85))
    yield [FadeIn(left_at(eq("ṗ = −∂H/∂x", 38, ORANGE), -7.0, -1.75)), GrowArrow(hp),
           FadeIn(left_at(lab("momentum's rate: how H depends on position", 22), -7.0, -2.4))]
    yield [FadeIn(left_at(eq("= −dV/dx, the force", 30, ORANGE), -6.4, -3.0))]
    yield [GrowArrow(both), FadeIn(at(lab("together: Newton's law again", 26, INK, True), PX, -3.45))]


@slide("Each rule gives a rate of change", "Step by step")
def steps(s):
    t = clock(s, 0.0)
    s.add(phase_frame(), orbit(color=LINE, width=3))
    yield [FadeIn(left_at(words("each rate comes straight from the current position and momentum", 26, 26, INK), -7.0, 1.6))]
    ts = [ST + k * PI / 14 for k in range(5)]
    pts = [pp(osc_x(u), osc_p(u)) for u in ts]
    hops = [Arrow(a, b, buff=0.05, color=BLUE, stroke_width=4, tip_length=0.15) for a, b in zip(pts, pts[1:])]
    d = Dot(pts[0], radius=0.14, color=BLUE)
    s.add(d)
    yield [LaggedStart(*[GrowArrow(h) for h in hops], lag_ratio=0.6), d.animate.move_to(pts[-1]),
           FadeIn(left_at(lab("the state now fixes the next small step", 24, INK), -7.0, 0.1))]
    start = ts[-1]
    t.rate = 1.0
    live(s, lambda: VGroup(corners([pp(osc_x(u), osc_p(u)) for u in np.linspace(start, start + min(t.get_value(), PI), 60)], BLUE, 4),
                           phase_dot(start + t.get_value())))
    yield [FadeOut(d), FadeIn(left_at(lab("then the next, and the whole motion", 24, INK), -7.0, -0.7))]


# ------------------------------------------------------------------ the spring

def spring_chips():
    a = left_at(chip("1 kg", BLUE, size=26, h=0.65), -3.3, 2.35)
    return VGroup(a, left_at(chip("k = 4 N/m", INK, size=26, h=0.65), a.get_right()[0] + 0.25, 2.35))


@slide("Let's run it on a spring.", "A mass on a spring")
def spr1(s):
    x = tracker(s, 0.0)
    rm = rest_mark()
    live(s, lambda: spring(x.get_value()))
    yield [FadeIn(rm)]
    yield [FadeIn(spring_chips())]

    def dim_arrow():
        return DoubleArrow(P(-4.4, 0.25), P(-4.4 + 1.3 * max(x.get_value(), 0.2), 0.25), buff=0, color=BLUE, stroke_width=3, tip_length=0.14,
                           max_tip_length_to_length_ratio=0.5).set_opacity(min(x.get_value() * 2, 1.0))
    live(s, dim_arrow)
    yield [x.animate.set_value(1.0), FadeIn(at(lab("pulled out 1 m, then let go", 24, BLUE), -4.0, -0.25))]


GR = dict(x0=-6.9, w=6.2)   # the time graphs: 0 to 2π seconds
GX_Y, GP_Y, GAMP = -0.95, -2.6, 0.55


def gt(tm):
    return GR["x0"] + tm / TAU * GR["w"]


def graph_axes():
    g = VGroup()
    for y, name in ((GX_Y, "x"), (GP_Y, "p")):
        g.add(axis((GR["x0"], y), (GR["x0"] + GR["w"] + 0.3, y)), right_at(T(name, 26, BLUE, True), GR["x0"] - 0.15, y))
    g.add(right_at(lab("time", 22), GR["x0"] + GR["w"] + 0.3, GP_Y - 0.4))
    return g


def x_graph(t1):
    return corners([P(gt(u), GX_Y + GAMP * osc_x(u)) for u in np.linspace(0, max(min(t1, TAU), 1e-3), 80)], BLUE, 4)


def p_graph(t1):
    return corners([P(gt(u), GP_Y + GAMP / 2 * osc_p(u)) for u in np.linspace(0, max(min(t1, TAU), 1e-3), 80)], BLUE, 4)


SPRING_FROM = "Hamilton's equations say the position swings"   # the narration where the spring is let go


def spring_clock(s, at):
    """Spring time that carries on across slides: the slide starting at `at` begins where the last one ended.

    It reads the scene's own elapsed time rather than summing frame steps, which drift
    by a few tenths of a second over a long slide and made the spring skip at slide changes.
    """
    off = max(narration_start(at) - narration_start(SPRING_FROM), 0.0)
    t = ValueTracker(off)
    t.rate = 1.0
    t.add_updater(lambda m, dt: m.set_value(off + s.renderer.time))
    s.add(t)
    return t


def spring_live(s, t):
    s.add(rest_mark())
    live(s, lambda: spring(osc_x(t.get_value())))
    s.add(spring_chips())


@slide("Hamilton's equations say the position swings", "Back and forth like a cosine")
def spr2(s):
    t = spring_clock(s, "Hamilton's equations say the position swings")
    spring_live(s, t)
    s.add(graph_axes())
    pseen = tracker(s)
    live(s, lambda: x_graph(t.get_value()))
    live(s, lambda: dim(p_graph(t.get_value()), pseen.get_value()))
    yield [FadeIn(at(eq("x = cos 2t", 38, BLUE), 3.8, 1.6)), FadeIn(at(lab("the position swings like a cosine", 24, INK), 3.8, 0.95))]
    yield [*show(pseen), FadeIn(at(eq("p = −2 sin 2t", 38, BLUE), 3.8, -0.2))]
    mk = VGroup(Dot(P(gt(PI / 4), GP_Y - GAMP), radius=0.1, color=INK), Dot(P(gt(PI / 4), GX_Y), radius=0.1, color=INK),
                DashedLine(P(gt(PI / 4), GX_Y), P(gt(PI / 4), GP_Y - GAMP), color=LINE, stroke_width=2))
    yield [FadeIn(mk), FadeIn(at(words("momentum is biggest just as the mass passes the middle", 28, 24, INK, ORIGIN), 3.8, -1.5))]


def spr_graphs_done(s):
    s.add(graph_axes(), x_graph(TAU), p_graph(TAU))


@slide("The spring has a natural rate", "The angular frequency")
def spr3(s):
    t = spring_clock(s, 'The spring has a natural rate')
    spring_live(s, t)
    spr_graphs_done(s)
    yield [FadeIn(at(lab("its natural rate: the angular frequency", 26, INK), 3.8, 2.1))]
    yield [FadeIn(at(eq("ω = √(k / m)", 40, PURPLE), 3.8, 1.2))]
    yield [FadeIn(at(eq("= √(4 / 1) = 2", 40, PURPLE), 4.2, 0.3))]


@slide("A cosine repeats every two pi.", "One full swing")
def spr4(s):
    t = spring_clock(s, 'A cosine repeats every two pi.')
    spring_live(s, t)
    spr_graphs_done(s)
    s.add(at(eq("ω = √(k / m)", 40, PURPLE), 3.8, 1.2), at(eq("= √(4 / 1) = 2", 40, PURPLE), 4.2, 0.3))
    yield [FadeIn(at(lab("a cosine repeats every 2π", 26, INK), 3.8, -0.75))]
    yield [FadeIn(at(eq("one swing = 2π / ω", 36, INK), 3.8, -1.6))]
    span = DoubleArrow(P(gt(0), GX_Y + GAMP + 0.3), P(gt(PI), GX_Y + GAMP + 0.3), buff=0, color=INK, stroke_width=3, tip_length=0.16)
    yield [FadeIn(at(eq("= π s", 40, INK, True), 3.8, -2.5)), GrowFromCenter(span),
           FadeIn(lab("π s", 26, INK, True).next_to(span, UP, buff=0.08))]


def total_bar(y=-2.5, x0=-6.8, w=4.0):
    return VGroup(left_at(lab("total", 24, TEAL, True), x0, y + 0.45), left_at(Rectangle(width=w, height=0.4, stroke_width=0, fill_color=TEAL, fill_opacity=0.85), x0, y),
                  left_at(lab("2 J", 24, TEAL, True), x0 + w + 0.2, y))


@slide("At release, the momentum is zero", "The energy: 2 joules")
def energy(s):
    t = spring_clock(s, 'At release, the momentum is zero')
    spring_live(s, t)
    yield [FadeIn(at(eq("at release:  p = 0,  x = 1 m", 32, BLUE), 3.6, 1.8))]
    yield [FadeIn(at(eq("E = ½ k x²", 40, TEAL), 3.6, 0.8)), FadeIn(at(lab("all of it potential", 24, INK), 3.6, 0.1))]
    yield [FadeIn(at(eq("= ½ · 4 · 1² = 2 J", 40, TEAL), 3.6, -0.9)), FadeIn(total_bar()),
           FadeIn(at(lab("and it stays 2 J the whole time", 26, TEAL, True), 3.6, -1.8))]


def kv_bars(t, x0=-6.8, w=4.0):
    tau = t.get_value()
    g = VGroup()
    for k, (name, val) in enumerate((("kinetic", 2 * np.sin(2 * tau) ** 2), ("potential", 2 * np.cos(2 * tau) ** 2))):
        y = -0.5 - 0.85 * k
        g.add(Rectangle(width=w, height=0.4, stroke_color=LINE, stroke_width=2).move_to(P(x0 + w / 2, y)),
              left_at(Rectangle(width=max(w * val / 2, 0.002), height=0.4, stroke_width=0, fill_color=TEAL, fill_opacity=0.85 if k == 0 else 0.5), x0, y))
    return g


def kv_labels(x0=-6.8):
    return VGroup(left_at(lab("kinetic", 24, TEAL), x0 + 4.2, -0.5), left_at(lab("potential", 24, TEAL), x0 + 4.2, -1.35))


@slide("At the ends of the swing it's all potential.", "Kinetic and potential trade places")
def trade(s):
    t = spring_clock(s, "At the ends of the swing it's all potential.")
    spring_live(s, t)
    s.add(total_bar(), at(eq("E = 2 J", 40, TEAL), 3.6, 1.8))
    seen = tracker(s)
    live(s, lambda: dim(kv_bars(t), seen.get_value()))
    yield [*show(seen), FadeIn(kv_labels()), FadeIn(at(lab("at the ends of the swing: all potential", 26, INK), 3.6, 0.6))]
    yield [FadeIn(at(lab("in the middle: all kinetic", 26, INK), 3.6, -0.2))]


@slide("On the phase-space map, the point goes round", "A loop of equal energy")
def loop(s):
    t = spring_clock(s, 'On the phase-space map, the point goes round')
    spring_live(s, t)
    s.add(total_bar(), kv_labels())
    live(s, lambda: kv_bars(t))
    seen = tracker(s)
    t0 = t.get_value()
    live(s, lambda: dim(VGroup(trace(t.get_value(), start=t0), phase_dot(t.get_value())), seen.get_value()))
    yield [FadeIn(phase_frame()), *show(seen)]
    yield [FadeIn(at(lab("every state on the loop: 2 J", 26, TEAL, True), PX, -3.45))]
    yield [FadeIn(left_at(lab("energy passes between kinetic and potential", 22, INK), -6.9, -3.45))]


@slide("Rescale the two axes", "Rescaled, the loop is a circle")
def circle(s):
    t = spring_clock(s, 'Rescale the two axes')
    spring_live(s, t)
    s.add(total_bar(), kv_labels())
    live(s, lambda: kv_bars(t))
    sc = tracker(s, PPS)
    s.add(phase_frame())
    live(s, lambda: VGroup(orbit(0, PI, sc.get_value()), phase_dot(t.get_value(), sc.get_value())))
    yield [sc.animate.set_value(PXS / 2), FadeIn(at(lab("rescale the axes: a circle", 26, BLUE, True), PX, -3.45))]
    yield [FadeIn(at(pill("the harmonic oscillator chapter builds on this", INK, 24), -3.9, -3.4), shift=UP * 0.15)]


# ================================================================== the Poisson bracket
deck.part("How anything changes")


def moving_phase(s, t):
    s.add(phase_frame(), orbit(color=LINE, width=3))
    live(s, lambda: phase_dot(t.get_value()))


@slide("How anything changes.", "Other quantities")
def pb1(s):
    t = clock(s)
    moving_phase(s, t)
    yield [FadeIn(left_at(lab("from Hamilton's equations:", 24), -7.0, 2.2))]
    a = left_at(hchip("how x changes", BLUE, size=28, h=0.75), -7.0, 1.4)
    b = left_at(hchip("how p changes", BLUE, size=28, h=0.75), -7.0, 0.4)
    yield [FadeIn(a), FadeIn(b), FadeIn(tick(a)), FadeIn(tick(b))]
    c = left_at(hchip("how the energy changes?", INK, size=28, h=0.75), -7.0, -1.0)
    d = left_at(hchip("how anything else changes?", INK, size=28, h=0.75), -7.0, -2.0)
    yield [FadeIn(c), FadeIn(d)]


@slide("And we'd like to know it without solving", "A quantity on the map")
def pb2(s):
    t = clock(s)
    s.add(phase_frame())
    no = left_at(hchip("solve the whole motion first", MUTED, size=26, h=0.75), -7.0, 1.8)
    yield [FadeIn(no), Create(strike(no, RED)), FadeIn(left_at(lab("without that", 24, INK), -7.0, 1.0))]
    contours = VGroup(*[smooth([pp(r * np.cos(u), 2 * r * np.sin(u)) for u in np.linspace(0, TAU, 50)], LINE, 2) for r in (0.35, 0.65, 0.95, 1.2)])
    f = left_at(eq("f(x, p)", 40, INK), -7.0, -0.2)
    yield [FadeIn(contours), FadeIn(f), FadeIn(left_at(lab("any quantity depends on the state", 24, INK), -7.0, -0.9))]
    seen = tracker(s)
    live(s, lambda: dim(VGroup(phase_dot(t.get_value())), seen.get_value()))
    yield [*show(seen), FadeIn(left_at(lab("as the state moves, f changes", 24, INK), -7.0, -2.0))]


@slide("The position moves, and the momentum moves.", "Two reasons, one recipe")
def pb3(s):
    s.add(phase_frame(), orbit(color=LINE, width=3))
    x, p = st_xp()
    o = pp(x, p)
    d = Dot(o, radius=0.14, color=BLUE)
    s.add(d)
    dx = RIGHT * 0.45 * p * PXS
    dp = UP * 0.45 * (-4 * x) * PPS
    a1 = Arrow(o, o + dx, buff=0, color=BLUE, stroke_width=6, tip_length=0.2)
    a2 = Arrow(o + dx, o + dx + dp, buff=0, color=ORANGE, stroke_width=6, tip_length=0.2)
    yield [GrowArrow(a1), GrowArrow(a2), FadeIn(left_at(lab("the position moves", 24, BLUE), -7.0, 2.2)),
           FadeIn(left_at(lab("the momentum moves", 24, ORANGE), -7.0, 1.6))]
    r = left_at(eq("rate of f = (∂f/∂x) ẋ + (∂f/∂p) ṗ", 30, INK), -7.0, 0.4)
    yield [FadeIn(r), FadeIn(left_at(lab("add the two; Hamilton's equations give ẋ and ṗ", 22), -7.0, -0.25))]
    yield [FadeIn(left_at(eq("= ∂f/∂x · ∂H/∂p − ∂f/∂p · ∂H/∂x", 30, PURPLE), -6.2, -1.0))]
    yield [FadeIn(left_at(pill("one fixed recipe", PURPLE, 28), -7.0, -2.1))]


@slide("We call it the Poisson bracket of the quantity", "The Poisson bracket")
def pb4(s):
    b = at(eq("{f, H}", 60, PURPLE), -3.0, 1.6)
    yield [FadeIn(b), FadeIn(at(lab("the Poisson bracket of f with the energy", 26, PURPLE, True), 2.8, 1.6))]
    r = at(eq("rate of change of f  =  {f, H}", 42, INK), 0, 0.0)
    yield [FadeIn(r, shift=UP * 0.15)]
    g = at(eq("{f, g}", 44, PURPLE), -3.0, -1.8)
    yield [FadeIn(g), FadeIn(at(lab("the recipe works for any two quantities", 26, INK), 2.6, -1.8))]


FB = [("{f, g}  =", INK), ("∂f/∂x · ∂g/∂p", PURPLE), ("−", INK), ("∂f/∂p · ∂g/∂x", PURPLE)]


def fb_parts(size=40):
    g = VGroup(*[eq(t, size, c) for t, c in FB]).arrange(RIGHT, buff=0.3)
    return at(g, 0, 1.4)


@slide("Take how the first changes with position", "The recipe")
def pb5(s):
    f = fb_parts()
    yield [FadeIn(f[0]), FadeIn(f[1]), FadeIn(at(lab("how f changes with position, times how g changes with momentum", 24, INK), 0, 0.3))]
    yield [FadeIn(f[2]), FadeIn(f[3]), FadeIn(at(lab("minus how f changes with momentum, times how g changes with position", 24, INK), 0, -0.4))]
    yield [Indicate(f, color=PURPLE, scale_factor=1.05), FadeIn(at(lab("here's what it gives", 26, INK, True), 0, -2.0))]


MX = -0.4


def machine():
    box = at(card(None, 3.4, 1.4, PURPLE), MX, 1.2)
    return VGroup(box, at(eq("{ · , H}", 40, PURPLE), MX, 1.2))


def feed(inp, out, note, y, color=BLUE, note_color=INK, below=False):
    i = at(chip(inp, color, size=32, h=0.8), -5.4, y)
    o = at(eq(out, 34, note_color), 3.6, y)
    n = lab(note, 24, note_color)
    n = n.next_to(o, DOWN, buff=0.2) if below else left_at(n, 4.6, y)
    a1 = Arrow(i.get_right(), P(MX - 1.75, 1.2 + (y - 1.2) * 0.25), buff=0.1, color=MUTED, stroke_width=4, tip_length=0.18)
    a2 = Arrow(P(MX + 1.75, 1.2 + (y - 1.2) * 0.25), o.get_left(), buff=0.1, color=MUTED, stroke_width=4, tip_length=0.18)
    return [FadeIn(i), GrowArrow(a1), GrowArrow(a2), FadeIn(o), FadeIn(n)], VGroup(i, a1, a2, o, n)


@slide("The bracket of position with the energy", "Bracket with the energy")
def pb6(s):
    s.add(machine(), at(lab("feed a quantity in, get its rate of change out", 24, INK), MX, 2.3))
    a, _ = feed("x", "p / m", "the velocity", 0.0)
    yield a
    b, _ = feed("p", "−dV/dx", "the force", -1.3, BLUE, ORANGE)
    yield b
    yield [FadeIn(at(pill("Hamilton's equations again", INK, 28), 0, -2.8))]


@slide("The bracket of the energy with itself", "The energy never changes")
def pb7(s):
    s.add(machine(), at(lab("feed a quantity in, get its rate of change out", 24, INK), MX, 2.3))
    a, _ = feed("H", "0", "the energy never changes", -0.4, PURPLE, TEAL, below=True)
    yield a
    yield [FadeIn(at(eq("{f, H} = 0  →  f stays constant", 36, INK), 0, -2.3))]


QP = [("{x, p}  =", INK), ("∂x/∂x", PURPLE), ("·", INK), ("∂p/∂p", PURPLE), ("−", INK), ("∂x/∂p", PURPLE), ("·", INK), ("∂p/∂x", PURPLE)]


def qp_parts():
    g = VGroup(*[eq(t, 40, c) for t, c in QP]).arrange(RIGHT, buff=0.25)
    return at(g, 0, 1.5)


def slot(parts, k, val, color=TEAL):
    return eq(val, 40, color, True).next_to(parts[k], DOWN, buff=0.35)


@slide("Now one special bracket.", "Position with momentum")
def qp1(s):
    big = at(eq("{x, p}", 64, PURPLE), 0, 1.5)
    yield [FadeIn(big), FadeIn(at(lab("one special bracket", 26, INK), 0, 2.45))]
    parts = qp_parts()
    yield [ReplacementTransform(big, parts)]
    q0 = -2.0
    line = Line(P(-5.0, -1.6), P(1.0, -1.6), color=LINE, stroke_width=4)
    d0 = Dot(P(q0, -1.6), radius=0.13, color=BLUE)
    nudge = Arrow(P(q0, -2.1), P(q0 + 1.6, -2.1), buff=0, color=INK, stroke_width=4, tip_length=0.18)
    yield [FadeIn(line), FadeIn(d0), GrowArrow(nudge), d0.animate.shift(RIGHT * 1.6), FadeIn(at(lab("nudge x", 22, INK), q0 + 0.8, -2.45)),
           FadeIn(left_at(lab("x moves by exactly the nudge", 24, INK), 1.6, -1.6)), FadeIn(slot(parts, 1, "1"))]


@slide("The same goes for momentum with momentum.", "Filling in the four slopes")
def qp2(s):
    parts = qp_parts()
    s.add(parts, slot(parts, 1, "1"))
    yield [FadeIn(slot(parts, 3, "1"))]
    yield [FadeIn(slot(parts, 5, "0")), FadeIn(slot(parts, 7, "0")), FadeIn(at(lab("neither changes with the other", 24, INK), 2.6, -0.4))]
    r = at(eq("{x, p} = 1 · 1 − 0 · 0 = 1", 48, PURPLE, True), 0, -2.0)
    yield [FadeIn(r, shift=UP * 0.15)]


@slide("It doesn't involve the energy at all.", "The same for every system")
def qp3(s):
    e = at(eq("{x, p} = 1", 56, PURPLE), 0, 1.7)
    s.add(e)
    yield [FadeIn(at(lab("no energy H in it", 26, INK), 0, 0.85))]
    xs = (-4.6, 0, 4.6)
    icons = [icon_ball(xs[0], -1.3), icon_pend(xs[1], -1.6), icon_spring(xs[2], -1.3)]
    ones = [at(eq("= 1", 30, PURPLE, True), x, -2.75) for x in xs]
    yield [*[FadeIn(i) for i in icons], *[FadeIn(o) for o in ones]]


@slide("Velocity doesn't share this.", "Why momentum")
def qv(s):
    good = at(eq("{x, p} = 1", 44, PURPLE), -3.8, 1.6)
    s.add(good)
    bad = at(eq("{x, v}", 44, INK), 2.6, 1.6)
    yield [FadeIn(bad)]
    res = eq("= 1 / m", 44, INK).next_to(bad, RIGHT, buff=0.25)
    yield [FadeIn(res)]
    n = at(lab("depends on the mass: no single rule for every system", 26, INK), 2.0, 0.3)
    under = Line(res[0].get_corner(DL) + DOWN * 0.1 + RIGHT * 0.45, res.get_corner(DR) + DOWN * 0.1, color=RED, stroke_width=5)
    yield [FadeIn(n), Create(under), FadeIn(xmark(n, 0.36, 0.2))]
    yield [FadeIn(tick(good, buff=0.3)), FadeIn(at(pill("that's why we use momentum", BLUE, 30), 0, -1.6))]


@slide("Better still, every other bracket", "One relation underneath")
def tree(s):
    root = at(card("{x, p} = 1", 4.0, 1.1, PURPLE, 36), -4.4, 0.0)
    kids = [at(hchip(t, PURPLE, size=28, h=0.75), 2.6, y) for t, y in (("{x², p} = 2x", 1.7), ("{x, H}", 0.55), ("{p, H}", -0.6), ("…", -1.75))]
    yield [FadeIn(root), FadeIn(at(lab("every other bracket", 26, INK), 2.6, 2.5))]
    yield [*[FadeIn(k) for k in kids], FadeIn(at(lab("built by adding and multiplying x and p", 24, INK), 2.6, -2.6))]
    yield [*[GrowArrow(Arrow(k.get_left(), root.get_right(), buff=0.12, color=MUTED, stroke_width=4, tip_length=0.18)) for k in kids],
           FadeIn(at(lab("reduces, step by step, to this one", 24, INK), -4.4, -1.0))]


@slide("So when the next chapter builds quantum mechanics", "Only one relation to replace")
def tree2(s):
    root = at(card("{x, p} = 1", 4.0, 1.1, PURPLE, 36), -4.4, 0.0)
    kids = [at(hchip(t, PURPLE, size=28, h=0.75), 2.6, y) for t, y in (("{x², p} = 2x", 1.7), ("{x, H}", 0.55), ("{p, H}", -0.6), ("…", -1.75))]
    s.add(root, *kids, *[Arrow(k.get_left(), root.get_right(), buff=0.12, color=MUTED, stroke_width=4, tip_length=0.18) for k in kids])
    yield [Indicate(root, color=PURPLE), FadeIn(at(lab("the next chapter replaces only this", 26, INK, True), -4.4, 1.2))]
    yield [LaggedStart(*[Indicate(k, color=PURPLE) for k in kids], lag_ratio=0.2), FadeIn(at(lab("everything else follows", 26, INK, True), 2.6, -2.6))]


# ================================================================== where this comes back
deck.part("Where this comes back")


@slide("Where this comes back.", "Next: first quantization")
def back1(s):
    yield [FadeIn(at(pill("next chapter: first quantization", INK, 30), 0, 2.15))]
    h = at(eq("H = p²/2m + V", 40, PURPLE), -3.6, 0.7)
    yield [FadeIn(h), FadeIn(left_at(words("keeps its job: it moves the state forward", 40, 26, INK), -0.6, 0.7))]
    q = at(VGroup(chip("x", BLUE, size=32, h=0.8), chip("p", BLUE, size=32, h=0.8)).arrange(RIGHT, buff=0.25), -3.6, -1.2)
    ops = at(card("operators,\na new kind of object", 4.4, 1.3, INK, 28), 3.6, -1.2)
    yield [FadeIn(q), GrowArrow(arrow(q, ops)), FadeIn(ops)]


@slide("It replaces the bracket of position with momentum", "One change, then the rest")
def back2(s):
    t = clock(s)
    a = at(card("{x, p} = 1", 3.8, 1.0, PURPLE, 34), -4.4, 1.6)
    b = at(card("a quantum version", 4.2, 1.0, INK, 30), 3.6, 1.6)
    yield [FadeIn(a), GrowArrow(arrow(a, b)), FadeIn(b)]
    yield [FadeIn(at(lab("the rest of quantum mechanics follows from that one change", 26, INK), 0, 0.4))]
    seen = tracker(s)
    live(s, lambda: spring(0.7 * np.cos(2 * t.get_value()), y=-1.6, wall=-5.6, rest=-3.0, sc=1.0, size=0.7, floor=-1.2), seen)
    yield [*show(seen), FadeIn(left_at(words("later: the harmonic oscillator chapter quantizes this spring", 28, 26, INK), 0.0, -1.6))]


@slide("The action comes back too.", "The action comes back")
def back3(s):
    t = clock(s)
    s_ = at(eq("S = ∫ L dt", 44, PURPLE), -4.0, 1.8)
    yield [FadeIn(s_), FadeIn(at(lab("the action comes back too", 26, INK), 2.6, 1.8))]
    xs = np.linspace(-6.4, 6.4, 25)
    seen = tracker(s)

    def field():
        g = VGroup(hline(-6.8, 6.8, -1.3, LINE, 2))
        for x in xs:
            y = -1.3 + 0.7 * np.sin(0.9 * x - 2.2 * t.get_value())
            g.add(Line(P(x, -1.3), P(x, y), color=LINE, stroke_width=2), Dot(P(x, y), radius=0.09, color=BLUE))
        return g
    live(s, field, seen)
    yield [*show(seen), FadeIn(at(lab("fields: one coordinate at every point of space", 26, INK), 0, 0.4)),
           FadeIn(at(lab("the Euler-Lagrange equation, applied to each", 24, PURPLE), 0, -3.2))]


@slide("And much later, path integrals", "Every path, weighted by its action")
def back4(s):
    a, b = P(-5.8, -1.6), P(0.6, -1.6)
    angles = (0.45, 0.9, 1.9, 2.4, -0.45)
    paths = VGroup(*[ArcBetweenPoints(a, b, angle=-ang, color=MUTED, stroke_width=3) for ang in angles])
    real = ArcBetweenPoints(a, b, angle=-1.4, color=BLUE, stroke_width=4)
    tags = VGroup(*[chip("S", PURPLE, size=22, h=0.48).move_to(p.point_from_proportion(f)) for p, f in zip(paths, (0.3, 0.7, 0.25, 0.75, 0.5))])
    yield [FadeIn(VGroup(Dot(a, radius=0.1, color=INK), Dot(b, radius=0.1, color=INK))), LaggedStart(*[Create(p) for p in paths], lag_ratio=0.15),
           Create(real), FadeIn(tags), FadeIn(left_at(words("path integrals add up every path, each weighted by its action", 30, 26, INK), 1.6, 1.0))]
    yield [real.animate.set_stroke(width=9), FadeIn(left_at(words("and explain why the flat-spot path is the one we see", 30, 26, BLUE), 1.6, -0.8))]

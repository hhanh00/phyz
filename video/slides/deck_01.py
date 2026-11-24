"""Slides for chapter one, Classical Mechanics.

Every value comes from video/scripts/01-classical-mechanics.txt or
docs/classical-mechanics.md. The animated figures follow docs/manim/page_diagrams.py
(NewtonMotion, StationaryActionPaths, PhaseSpaceStates) and
docs/manim/concept_diagrams.py (ClassicalOscillatorEnergy).

Colors: BLUE for positions, paths, coordinates and states (points in phase
space), TEAL for energy (kinetic, potential, totals) and for checks that pass,
ORANGE for the step or quantity under discussion, which in this chapter is a
force (gravity, tension, the spring's pull) or a bend applied to a path, PURPLE
for the Lagrangian, the action, the Hamiltonian and the Poisson bracket, RED
only for a wrong answer or a method that fails (the T + V rule, the projection
trick on a double pendulum), MUTED and LINE for context and connectors.
"""
from manim import *

from engine import *

STEM = "01-classical-mechanics"
deck = Deck(f"scripts/{STEM}.txt")
slide = deck.slide


def at(mob, x, y):
    return mob.move_to([x, y, 0])


def pts(first, title, items, sub=None, chars=56, size=32, y=None, gap=0.42):
    """A slide whose points arrive one at a time."""
    @slide(first, title, sub)
    def build(s):
        rows = bullets(items, chars, size, gap=gap)
        rows.move_to([-7.0 + rows.width / 2, 0 if y is None else y, 0])
        for row in rows:
            yield [FadeIn(row, shift=RIGHT * 0.15)]
    return build


def cards(first, title, items, sub=None, w=None, h=2.3, size=27, y=-0.3, note=None):
    """A row of colored cards, given as (text, color) pairs, arriving one at a time."""
    @slide(first, title, sub)
    def build(s):
        width = w or min(4.6, (14.6 - 0.35 * (len(items) - 1)) / len(items))
        row = VGroup(*[card(t, width, h, c, size) for t, c in items]).arrange(RIGHT, buff=0.35)
        at(row, 0, y)
        for c in row:
            yield [FadeIn(c, shift=UP * 0.2)]
        if note:
            yield [FadeIn(caption(note, y=y - h / 2 - 0.85, color=INK, size=28, chars=78))]
    return build


def eq(text, size=32, color=INK):
    return code(text, size, color)


def lab(text, size=24, color=MUTED, bold=False):
    return T(text, size, color, bold)


def tick_mark(mob, color=TEAL):
    return check(color).next_to(mob, RIGHT, buff=0.2)


# ------------------------------------------------------------------ shared drawings

def zigzag(a, b, n=9, amp=0.17, color=MUTED):
    """A spring drawn as a zigzag from point a to point b."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    d = b - a
    length = max(np.linalg.norm(d), 1e-3)
    u = d / length
    nrm = np.array([-u[1], u[0], 0])
    end = min(0.15, length / 4)
    pts_ = [a, a + u * end]
    for i in range(n):
        f = end + (length - 2 * end) * (i + 0.5) / n
        pts_.append(a + u * f + nrm * amp * (1 if i % 2 == 0 else -1))
    pts_ += [b - u * end, b]
    return VMobject(color=color, stroke_width=3).set_points_as_corners(pts_)


def spring_rig(xt, wall=-6.6, rest=-3.4, y=0.6, sc=1.4, size=0.8, floor_to=None):
    """A wall, a spring and a block whose stretch follows the tracker xt (in metres)."""
    base = VGroup(Line([wall, y - 0.75, 0], [wall, y + 0.75, 0], color=INK, stroke_width=6),
                  Line([wall, y - size / 2 - 0.04, 0], [floor_to if floor_to is not None else rest + 2.6, y - size / 2 - 0.04, 0],
                       color=LINE, stroke_width=3))
    block = always_redraw(lambda: Square(size, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to([rest + sc * xt.get_value(), y, 0]))
    spr = always_redraw(lambda: zigzag([wall, y, 0], [rest + sc * xt.get_value() - size / 2, y, 0]))
    return base, spr, block


def pend_pos(pivot, length, th):
    return np.array(pivot, dtype=float) + length * np.array([np.sin(th), -np.cos(th), 0])


def pend_static(pivot, length, th, r=0.2, color=BLUE):
    pivot = np.array(pivot, dtype=float)
    bar = Line(pivot + LEFT * 0.55, pivot + RIGHT * 0.55, color=INK, stroke_width=6)
    b = pend_pos(pivot, length, th)
    return VGroup(bar, Line(pivot, b, color=INK, stroke_width=3), Dot(b, radius=r, color=color))


def pend_live(pivot, length, tr, r=0.2):
    pivot = np.array(pivot, dtype=float)
    bar = Line(pivot + LEFT * 0.55, pivot + RIGHT * 0.55, color=INK, stroke_width=6)
    string = always_redraw(lambda: Line(pivot, pend_pos(pivot, length, tr.get_value()), color=INK, stroke_width=3))
    bob = always_redraw(lambda: Dot(pend_pos(pivot, length, tr.get_value()), radius=r, color=BLUE))
    return bar, string, bob


def swing_arc(pivot, length, half=0.85):
    return DashedVMobject(Arc(radius=length, start_angle=-PI / 2 - half, angle=2 * half, arc_center=np.array(pivot, dtype=float),
                              color=LINE, stroke_width=3), num_dashes=24)


def double_pend(pivot, l1, l2, th1, th2, r=0.19):
    pivot = np.array(pivot, dtype=float)
    b1 = pend_pos(pivot, l1, th1)
    b2 = pend_pos(b1, l2, th2)
    g = VGroup(Line(pivot + LEFT * 0.55, pivot + RIGHT * 0.55, color=INK, stroke_width=6),
               Line(pivot, b1, color=INK, stroke_width=3), Line(b1, b2, color=INK, stroke_width=3),
               Dot(b1, radius=r, color=BLUE), Dot(b2, radius=r, color=BLUE))
    return g, b1, b2


def angle_mark(origin, length, th, name, r=0.75, color=BLUE, size=26):
    """A dashed vertical below origin, an arc to angle th, and its label."""
    origin = np.array(origin, dtype=float)
    vert = DashedLine(origin, origin + DOWN * length * 0.75, color=LINE, stroke_width=2)
    arc = Arc(radius=r, start_angle=-PI / 2, angle=th, arc_center=origin, color=color, stroke_width=4)
    mid = -PI / 2 + th / 2
    label = T(name, size, color, True).move_to(origin + (r + 0.32) * np.array([np.cos(mid), np.sin(mid), 0]))
    return VGroup(vert, arc, label)


def icon_ball(x, y):
    ground = Line([x - 0.9, y - 0.6, 0], [x + 0.9, y - 0.6, 0], color=LINE, stroke_width=3)
    arc = DashedVMobject(ArcBetweenPoints([x - 0.7, y - 0.5, 0], [x + 0.7, y - 0.5, 0], angle=-PI * 0.7, color=LINE), num_dashes=12)
    return VGroup(ground, arc, Dot([x - 0.15, y + 0.45, 0], radius=0.17, color=BLUE))


def icon_spring(x, y):
    wall = Line([x - 0.95, y - 0.45, 0], [x - 0.95, y + 0.45, 0], color=INK, stroke_width=5)
    block = Square(0.55, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to([x + 0.6, y, 0])
    return VGroup(wall, zigzag([x - 0.95, y, 0], [x + 0.32, y, 0], n=7, amp=0.13), block)


def icon_pend(x, y):
    return pend_static([x, y + 0.65, 0], 1.25, 0.45, r=0.16)


# ------------------------------------------------------------------ opening
deck.part("Chapter one")


@slide("Chapter one.", "Classical Mechanics")
def opening(s):
    pp = at(card("particle physics", 4.4, 1.2, MUTED, 30), -4.4, 1.3)
    qt = at(card("quantum theory", 4.4, 1.2, INK, 30), 2.6, 1.3)
    link = arrow(pp, qt)
    yield [FadeIn(pp), FadeIn(qt), GrowArrow(link), FadeIn(lab("built on", 24).next_to(link, UP, buff=0.1))]
    f = at(chip("force", ORANGE, size=30, h=0.8), 1.3, -0.5)
    p = at(chip("path", BLUE, size=30, h=0.8), 3.9, -0.5)
    yield [FadeIn(f, shift=DOWN * 0.2), FadeIn(p, shift=DOWN * 0.2), FadeIn(lab("its basic equations contain:", 24).move_to([2.6, 0.35, 0]))]
    yield [Create(strike(f, MUTED)), Create(strike(p, MUTED)), FadeIn(at(T("neither one", 28, INK), 2.6, -1.5))]


@slide("A quantum particle doesn't follow", "What carries over")
def carry(s):
    rng = np.random.default_rng(3)
    cloud = VGroup(*[Dot([-4.6 + 1.3 * a, 1.5 + 0.55 * b, 0], radius=0.05, color=BLUE).set_opacity(0.55)
                     for a, b in rng.normal(size=(70, 2)).clip(-1.6, 1.6)])
    yield [FadeIn(cloud), FadeIn(lab("no definite path", 26).move_to([-4.6, 0.2, 0]))]
    fma = at(eq("F = ma", 48, INK), 2.6, 1.5)
    yield [FadeIn(fma), Create(Line(fma.get_left() + LEFT * 0.15, fma.get_right() + RIGHT * 0.15, color=MUTED, stroke_width=6)), FadeIn(lab("nothing to put in", 26).move_to([2.6, 0.5, 0]))]
    fn = at(card("one function of the kinetic\nand potential energies", 6.2, 1.5, PURPLE, 28), -3.4, -1.6)
    yield [FadeIn(fn, shift=UP * 0.2)]
    path = VMobject(color=BLUE, stroke_width=5).set_points_smoothly([[1.8, -2.4, 0], [3.0, -1.0, 0], [4.3, -0.7, 0], [5.6, -1.2, 0], [6.6, -2.4, 0]])
    yield [GrowArrow(arrow(fn, [1.6, -1.6, 0])), Create(path), FadeIn(lab("the motion follows", 26, BLUE).move_to([4.3, -2.9, 0]))]


@slide("This chapter rewrites ordinary mechanics", "A ball, a spring and a pendulum")
def systems(s):
    fn = at(card("ordinary mechanics,\nrewritten around one function", 5.6, 1.3, PURPLE, 28), 0, -0.9)
    yield [FadeIn(fn)]
    icons = [icon_ball(-4.8, 1.55), icon_spring(0, 1.55), icon_pend(4.8, 1.3)]
    names = [at(lab(n, 26, INK), x, 0.35) for n, x in (("ball", -4.8), ("spring", 0), ("pendulum", 4.8))]
    for i in (0, 2):
        names[i].set_y(0.35)
    yield [LaggedStart(*[FadeIn(VGroup(i, n)) for i, n in zip(icons, names)], lag_ratio=0.3),
           GrowArrow(arrow([-3.9, 0.1, 0], [-2.9, -0.6, 0])), GrowArrow(arrow([3.9, 0.1, 0], [2.9, -0.6, 0]))]
    qm = at(card("quantum mechanics", 4.4, 1.0, INK, 30), 0, -2.95)
    link = arrow(fn, qm)
    yield [GrowArrow(link), FadeIn(qm), FadeIn(lab("the next chapters", 24).next_to(link, RIGHT, buff=0.2))]


# ------------------------------------------------------------------ at a glance
deck.part("The chapter at a glance")

COLS = [-4.85, 0.0, 4.85]
CW = 4.6
NAMES = ["Newton", "Lagrange", "Hamilton"]
ROWS = {"q": (1.0, 1.7), "sup": (-0.7, 1.45), "get": (-2.3, 1.45), "ret": (-3.65, 0.85)}
ROW_LABEL = {"sup": "you supply", "get": "you get"}
GLANCE = [  # from the table in docs/classical-mechanics.md
    {"q": "Given the forces, how does it accelerate?", "sup": ("the forces", ORANGE), "get": ("the acceleration", BLUE),
     "ret": "everyday mechanics"},
    {"q": "Which path between two moments does it take?", "sup": ("L = T − V\nkinetic minus potential", PURPLE),
     "get": ("the same equation,\nin any coordinates", BLUE), "ret": "fields, path integrals"},
    {"q": "Given the present state, where does it go next?", "sup": ("H(q, p)\nin position q and momentum p", PURPLE),
     "get": ("two equations that\nmove a point (q, p)", BLUE), "ret": "quantum mechanics"},
]


def glance_heads():
    return VGroup(*[at(pill(n, INK, 28), x, 2.3) for n, x in zip(NAMES, COLS)])


def glance_frames(keys=("q", "sup", "get", "ret")):
    out = VGroup()
    for key in keys:
        y, h = ROWS[key]
        for x in COLS:
            box = at(card(None, CW, h, LINE), x, y)
            if key in ROW_LABEL:
                tag = lab(ROW_LABEL[key], 22)
                tag.move_to(box.get_corner(UL) + np.array([0.15 + tag.width / 2, -0.12 - tag.height / 2, 0]))
                box.add(tag)
            out.add(box)
    return out


def glance_icon(i, x, y):
    if i == 0:
        b = Dot([x - 0.4, y, 0], radius=0.16, color=BLUE)
        f = Arrow([x - 0.22, y, 0], [x + 0.6, y, 0], buff=0, color=ORANGE, stroke_width=5, tip_length=0.2)
        return VGroup(b, f)
    if i == 1:
        a, b = [x - 0.55, y - 0.35, 0], [x + 0.45, y - 0.35, 0]
        arcs = VGroup(*[ArcBetweenPoints(a, b, angle=-ang, color=LINE, stroke_width=3) for ang in (0.6, 1.5, 2.4)])
        real = ArcBetweenPoints(a, b, angle=-1.5, color=BLUE, stroke_width=5)
        return VGroup(arcs, real, Dot(a, radius=0.07, color=INK), Dot(b, radius=0.07, color=INK))
    loop = Ellipse(width=1.2, height=0.9, color=LINE, stroke_width=3).move_to([x, y, 0])
    d = Dot([x, y + 0.45, 0], radius=0.09, color=BLUE)
    step = Arrow([x, y + 0.45, 0], [x + 0.55, y + 0.3, 0], buff=0, color=ORANGE, stroke_width=4, tip_length=0.16)
    return VGroup(loop, d, step)


def glance_cells(i):
    """The question, supply, get and return contents of column i."""
    x, g = COLS[i], GLANCE[i]
    y, _ = ROWS["q"]
    icon = glance_icon(i, x - 1.6, y)
    qtext = W(g["q"], 19, 24, INK).move_to([x + 0.6, y, 0])
    sup = VGroup(*[T(t, 26 if k == 0 else 22, g["sup"][1] if k == 0 else MUTED) for k, t in enumerate(g["sup"][0].split("\n"))]).arrange(DOWN, buff=0.1)
    at(sup, x, ROWS["sup"][0] - 0.2)
    get = VGroup(*[T(t, 24, g["get"][1]) for t in g["get"][0].split("\n")]).arrange(DOWN, buff=0.1)
    at(get, x, ROWS["get"][0] - 0.2)
    ret = at(VGroup(lab("later:", 22), T(g["ret"], 23, INK)).arrange(RIGHT, buff=0.15), x, ROWS["ret"][0])
    return {"icon": icon, "q": qtext, "sup": sup, "get": get, "ret": ret}


def glance_later():
    """The 'later:' tags of the bottom row, before the narration names where each form returns."""
    return VGroup(*[at(lab("later: ?", 22), x, ROWS["ret"][0]) for x in COLS])


def glance_base(s, upto):
    """Add the table with columns before `upto` filled in."""
    s.add(glance_heads(), glance_frames(), glance_later())
    for i in range(3):
        c = glance_cells(i)
        if i < upto:
            s.add(c["icon"], c["q"], c["sup"], c["get"])


def same_path(x, y, w=3.2, h=1.8):
    return VMobject(color=BLUE, stroke_width=5).set_points_smoothly(
        [[x - w / 2 + w * k / 8, y - h / 2 + h * (1 - ((k - 4) / 4) ** 2), 0] for k in range(9)])


@slide("The chapter at a glance.", "One motion, three descriptions")
def glance_intro(s):
    heads = VGroup(*[at(pill(n, INK, 30), x, -2.4) for n, x in zip(NAMES, COLS)])
    yield [LaggedStart(*[FadeIn(h, shift=UP * 0.2) for h in heads], lag_ratio=0.25)]
    paths = [same_path(x, 0.2) for x in COLS]
    links = [arrow(h, p) for h, p in zip(heads, paths)]
    yield [*[Create(p) for p in paths], *[GrowArrow(a) for a in links]]
    one = same_path(0, 0.6, 5.0, 2.6)
    yield [*[ReplacementTransform(p, one.copy()) for p in paths], *[FadeOut(a) for a in links],
           *[GrowArrow(arrow(h.get_top(), one.point_from_proportion(f))) for h, f in zip(heads, (0.12, 0.5, 0.88))],
           FadeIn(lab("exactly the same motion", 26, BLUE).move_to([0, 2.3, 0]))]


@slide("What changes is what you put", "What goes in, what comes out")
def glance_frame(s):
    yield [FadeIn(glance_heads()), FadeIn(glance_frames(("q", "sup", "get")))]
    yield [FadeIn(glance_frames(("ret",))), LaggedStart(*[FadeIn(r) for r in glance_later()], lag_ratio=0.3)]


@slide("The first description is Newton's.", "Newton: forces in, acceleration out")
def glance_newton(s):
    glance_base(s, 0)
    c = glance_cells(0)
    heads = glance_heads()
    yield [Indicate(heads[0], color=ORANGE), FadeIn(c["icon"][0]), GrowArrow(c["icon"][1]), FadeIn(c["q"])]
    yield [FadeIn(c["sup"], shift=UP * 0.15)]
    yield [FadeIn(c["get"], shift=UP * 0.15)]


@slide("The second is Lagrange's.", "Lagrange: which path?")
def glance_lagrange_q(s):
    glance_base(s, 1)
    c = glance_cells(1)
    arcs, real, d1, d2 = c["icon"]
    yield [Indicate(glance_heads()[1], color=ORANGE), FadeIn(d1), FadeIn(d2)]
    yield [Create(arcs), FadeIn(c["q"])]
    yield [Create(real)]


@slide("You supply one function, the kinetic", "Lagrange: one function in")
def glance_lagrange(s):
    glance_base(s, 1)
    c = glance_cells(1)
    s.add(c["icon"], c["q"])
    yield [FadeIn(c["sup"], shift=UP * 0.15)]
    yield [FadeIn(c["get"], shift=UP * 0.15)]


@slide("The third description is Hamilton's.", "Hamilton: where next?")
def glance_hamilton_q(s):
    glance_base(s, 2)
    c = glance_cells(2)
    loop, d, step = c["icon"]
    yield [Indicate(glance_heads()[2], color=ORANGE), Create(loop), FadeIn(d)]
    yield [GrowArrow(step), FadeIn(c["q"])]


@slide("You supply the energy, written in terms", "Hamilton: the energy in")
def glance_hamilton(s):
    glance_base(s, 2)
    c = glance_cells(2)
    s.add(c["icon"], c["q"])
    yield [FadeIn(c["sup"], shift=UP * 0.15)]
    yield [FadeIn(c["get"], shift=UP * 0.15)]


@slide("Newton's form serves everyday mechanics.", "Where each form returns")
def glance_returns(s):
    s.add(glance_heads(), glance_frames())
    later = glance_later()
    for i in range(3):
        c = glance_cells(i)
        s.add(c["icon"], c["q"], c["sup"], c["get"])
    s.add(later)
    for i in range(3):
        ret = glance_cells(i)["ret"]
        yield [FadeOut(later[i]), FadeIn(ret, shift=UP * 0.15), Indicate(glance_heads()[i], color=ORANGE)]


IDEA_X = [-4.85, 0.0, 4.85]


def ideas_parts():
    """The three idea cards, as the groups that arrive in each build step."""
    xs = IDEA_X
    frames = VGroup(*[at(card(None, 4.6, 4.3, c), x, -0.45) for x, c in zip(xs, (PURPLE, BLUE, PURPLE))])
    top = lab("three new ideas along the way", 26).move_to([0, 2.3, 0])
    heads = [at(T(t, 28, c, True), x, 1.3) for t, x, c in (("the action", xs[0], PURPLE), ("the state", xs[1], BLUE),
                                                          ("the Poisson bracket", xs[2], PURPLE))]
    texts = [at(W(t, 22, 24, INK, align=ORIGIN), x, -1.85) for t, x in (("one number that scores a whole path", xs[0]),
                                                                       ("a point made of a position and a momentum", xs[1]),
                                                                       ("gives the rate of change of any quantity", xs[2]))]
    a, b = [xs[0] - 1.5, -0.4, 0], [xs[0] + 1.5, -0.4, 0]
    path = ArcBetweenPoints(a, b, angle=-1.6, color=BLUE, stroke_width=5)
    score = at(chip("S", PURPLE, size=30, h=0.62), xs[0], -0.85)
    action = VGroup(heads[0], Dot(a, radius=0.07, color=INK), Dot(b, radius=0.07, color=INK), path, score, texts[0])
    ax = VGroup(Line([xs[1] - 1.1, -0.45, 0], [xs[1] + 1.1, -0.45, 0], color=LINE, stroke_width=3),
                Line([xs[1] - 1.1, -0.45, 0], [xs[1] - 1.1, 0.75, 0], color=LINE, stroke_width=3))
    dot = Dot([xs[1] + 0.1, 0.25, 0], radius=0.11, color=BLUE)
    state = VGroup(heads[1], ax, dot, T("(q, p)", 24, BLUE).next_to(dot, RIGHT, buff=0.1),
                   lab("position q", 22).next_to(ax[0], DOWN, buff=0.1),
                   lab("momentum p", 22).rotate(PI / 2).next_to(ax[1], LEFT, buff=0.1), texts[1])
    br = at(eq("{f, H}", 38, PURPLE), xs[2], 0.25)
    out = at(T("rate of change of f", 24, INK), xs[2], -0.85)
    bracket = VGroup(heads[2], br, arrow(br, out), out, texts[2])
    return VGroup(frames, top), action, state, bracket


@slide("There are three new ideas along the", "Three new ideas")
def ideas(s):
    for group in ideas_parts():
        yield [FadeIn(group)]


@slide("One consequence comes with the action.", "Three new ideas")
def ideas_bonus(s):
    base, action, state, bracket = ideas_parts()
    s.add(base, action, state, bracket)
    yield [base[0][0][0].animate.set_fill(PURPLE, opacity=0.18), Indicate(action[0], color=PURPLE)]
    note = at(T("If L ignores a coordinate, a matching quantity never changes.", 27, PURPLE), 0, -3.3)
    yield [FadeIn(note, shift=UP * 0.15)]


CHAIN = ["Newton", "Lagrange", "Hamilton", "Poisson bracket", "quantum mechanics"]
CHAIN_Y = [2.1, 0.45, -0.85, -2.0, -3.15]


def chain_nodes():
    nodes = VGroup(*[at(card(n, 3.6, 0.7, INK, 26), -5.2, y) for n, y in zip(CHAIN, CHAIN_Y)])
    links = VGroup(*[arrow(a, b) for a, b in zip(nodes, nodes[1:])])
    return nodes, links


def reason(text, y, color=INK, size=25):
    t = T(text, size, color)
    return t.move_to([-3.0 + t.width / 2, y, 0])


REASONS = [  # (text, y, color), grouped by the link they explain
    [("forces are awkward when a body is tied to a string", 2.2, INK),
     ("quantum theory isn't written in terms of forces", 1.72, INK)],
    [("a function of energies avoids both", 1.24, TEAL)],
    [("summed along a path: a small bend barely changes it", 0.76, PURPLE)],
    [("quantum mechanics carries one instant forward", -0.05, INK),
     ("so: a state (q, p), moved by the energy", -0.5, INK)],
    [("asking how any quantity changes gives the bracket", -1.42, INK)],
    [("the next chapter swaps the q–p bracket for a commutator,", -2.35, INK),
     ("which measures how much order matters", -2.8, INK),
     ("quantization starts there", -3.25, ORANGE)],
]


def reasons(k):
    group = VGroup(*[reason(t, y, c) for t, y, c in REASONS[k]])
    if k == 1:
        group.add(check().next_to(group[0], RIGHT, buff=0.2))
    return group


def chain_base(s, upto, orange):
    nodes, links = chain_nodes()
    for k in orange:
        links[k].set_color(ORANGE)
    s.add(nodes, links, *[reasons(k) for k in range(upto)])
    return nodes, links


@slide("Each step has a reason.", "Each step has a reason")
def chain1(s):
    nodes, links = chain_nodes()
    yield [LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.15), LaggedStart(*[GrowArrow(a) for a in links], lag_ratio=0.15)]
    yield [links[0].animate.set_color(ORANGE), Indicate(nodes[0], color=ORANGE)]
    yield [FadeIn(reasons(0)[0], shift=RIGHT * 0.15)]


@slide("And quantum theory isn't written in terms", "Each step has a reason")
def chain2(s):
    nodes, links = chain_base(s, 0, (0,))
    s.add(reasons(0)[0])
    yield [FadeIn(reasons(0)[1], shift=RIGHT * 0.15)]
    yield [FadeIn(reasons(1), shift=RIGHT * 0.15), Indicate(nodes[1], color=PURPLE)]
    yield [FadeIn(reasons(2), shift=RIGHT * 0.15)]


@slide("We move to Hamilton because quantum mechanics", "Each step has a reason")
def chain3(s):
    nodes, links = chain_base(s, 3, (0,))
    yield [links[1].animate.set_color(ORANGE), FadeIn(reasons(3)[0], shift=RIGHT * 0.15)]
    yield [FadeIn(reasons(3)[1], shift=RIGHT * 0.15), Indicate(nodes[2], color=PURPLE)]


@slide("Asking how any quantity changes then gives", "Each step has a reason")
def chain4(s):
    nodes, links = chain_base(s, 4, (0, 1))
    yield [links[2].animate.set_color(ORANGE), FadeIn(reasons(4), shift=RIGHT * 0.15)]
    yield [links[3].animate.set_color(ORANGE), FadeIn(reasons(5)[0], shift=RIGHT * 0.15), FadeIn(reasons(5)[1], shift=RIGHT * 0.15)]
    yield [FadeIn(reasons(5)[2], shift=RIGHT * 0.15), Indicate(nodes[4], color=ORANGE)]


@slide("We still go through Lagrange on the way,", "Why Lagrange stays on the route")
def chain5(s):
    nodes, links = chain_nodes()
    for l in links:
        l.set_color(ORANGE)
    s.add(nodes, links)
    yield [nodes[1][0].animate.set_fill(PURPLE, opacity=0.2), Indicate(nodes[1], color=PURPLE),
           FadeIn(at(T("still needed, for two reasons", 30, PURPLE, True), 2.2, 2.0))]
    one = at(card("Hamilton's momentum p and energy H\nare both built from L", 7.4, 1.5, BLUE, 28), 2.2, 0.3)
    yield [FadeIn(one, shift=RIGHT * 0.15), GrowArrow(arrow(nodes[1].get_right(), one.get_left()))]
    two = at(card("fields and path integrals\nreuse the action itself", 7.4, 1.5, PURPLE, 28), 2.2, -1.75)
    yield [FadeIn(two, shift=RIGHT * 0.15), GrowArrow(arrow(nodes[1].get_right(), two.get_left()))]


# ------------------------------------------------------------------ Newton
deck.part("Newton's law, forces in, motion out")


def newton_eq(y=1.9, size=60):
    return at(VGroup(code("F", size, ORANGE), code("=", size, INK), code("m", size, INK), code("a", size, BLUE)).arrange(RIGHT, buff=0.3), 0, y)


def rate_chain(y=0.2):
    names = ["position", "velocity", "acceleration"]
    chips = [at(card(n, 2.8, 0.8, BLUE, 28), x, y) for n, x in zip(names, (-5.2, 0, 5.2))]
    links = [arrow(a, b) for a, b in zip(chips, chips[1:])]
    labels = [lab("rate of change", 22).next_to(l, UP, buff=0.12) for l in links]
    return chips, links, labels


@slide("Newton's law, forces in, motion out.", "Force equals mass times acceleration")
def newton1(s):
    e = newton_eq()
    yield [FadeIn(e)]
    yield [Indicate(e[0], color=ORANGE), Indicate(e[3], color=BLUE),
           FadeIn(lab("force = mass × acceleration", 26).next_to(e, DOWN, buff=0.3))]
    chips, links, labels = rate_chain()
    yield [FadeIn(chips[1]), FadeIn(chips[2]), GrowArrow(links[1]), FadeIn(labels[1])]


@slide("Velocity is how fast the position changes.", "Start and speed fix the future")
def newton2(s):
    e = newton_eq()
    chips, links, labels = rate_chain()
    s.add(e, lab("force = mass × acceleration", 26).next_to(e, DOWN, buff=0.3), chips[1], chips[2], links[1], labels[1])
    yield [FadeIn(chips[0]), GrowArrow(links[0]), FadeIn(labels[0])]
    start = [-4.6, -2.9, 0]
    path = VMobject(color=BLUE, stroke_width=4).set_points_smoothly([start, [-2.4, -1.6, 0], [0.4, -1.25, 0], [3.0, -1.7, 0], [5.0, -2.9, 0]])
    ball = Dot(start, radius=0.17, color=BLUE)
    v = Arrow(start, [-3.5, -2.1, 0], buff=0, color=BLUE, stroke_width=5, tip_length=0.2)
    yield [FadeIn(ball), GrowArrow(v), FadeIn(lab("where it starts, how fast it moves", 24, INK).move_to([-3.2, -3.55, 0]))]
    yield [Create(DashedVMobject(path, num_dashes=40)), MoveAlongPath(ball.copy(), path),
           FadeIn(lab("the law fixes everything after", 24, INK).move_to([3.4, -3.55, 0]))]


DROP = [(0, 0.0, 0.0, "0", "0"), (1, 9.8, 4.9, "9.8", "4.9"), (2, 19.6, 19.6, "19.6", "19.6"), (3, 29.4, 44.1, "29.4", "44.1")]


def drop_y(d):
    return 2.1 - 0.12245 * d


def drop_scene():
    ruler = Line([-5.75, 2.1, 0], [-5.75, -3.3, 0], color=LINE, stroke_width=3)
    marks = VGroup()
    for t, _, d, _, _ in DROP:
        y = drop_y(d)
        marks.add(Line([-5.9, y, 0], [-5.6, y, 0], color=MUTED, stroke_width=3), lab(f"{t} s", 22).move_to([-6.55, y, 0]))
    axes = []
    for cx, ymax, title in ((-0.9, 32, "speed (m/s)"), (4.6, 48, "distance fallen (m)")):
        ax = Axes(x_range=[0, 3.3, 1], y_range=[0, ymax, 10], x_length=4.3, y_length=3.5, tips=False,
                  axis_config={"color": LINE, "include_ticks": False}).move_to([cx, -0.75, 0])
        extra = VGroup(T(title, 26, BLUE).next_to(ax, UP, buff=0.3),
                       lab("time (s)", 22).next_to(ax.x_axis, DOWN, buff=0.45).align_to(ax.x_axis, RIGHT))
        for t in (1, 2, 3):
            extra.add(lab(str(t), 22).next_to(ax.c2p(t, 0), DOWN, buff=0.12))
        axes.append((ax, extra))
    top = lab("gravity: a constant acceleration g = 9.8 m/s every second", 25, ORANGE).move_to([2.0, 2.4, 0])
    return ruler, marks, axes, top


def drop_ball(k=0):
    y = drop_y(DROP[k][2])
    b = Dot([-5.15, y, 0], radius=0.17, color=BLUE)
    g = Arrow([-4.75, y + 0.1, 0], [-4.75, y - 0.75, 0], buff=0, color=ORANGE, stroke_width=5, tip_length=0.2)
    return VGroup(b, g)


def drop_second(axes, k):
    """The graph pieces for second k: two segments, two dots and two value labels."""
    (sp, _), (ds, _) = axes
    _, v, d, vs, dstr = DROP[k]
    seg_v = sp.plot(lambda t: 9.8 * t, x_range=[k - 1, k], color=BLUE, stroke_width=4)
    seg_d = ds.plot(lambda t: 4.9 * t * t, x_range=[k - 1, k], color=BLUE, stroke_width=4)
    dv = Dot(sp.c2p(k, v), radius=0.08, color=ORANGE)
    dd = Dot(ds.c2p(k, d), radius=0.08, color=ORANGE)
    return VGroup(seg_v, seg_d), VGroup(dv, T(vs, 22, ORANGE).next_to(dv, UL, buff=0.06),
                                        dd, T(dstr, 22, ORANGE).next_to(dd, UL, buff=0.06))


def drop_base(s, upto):
    """Add the ruler, axes and graph pieces for seconds 1..upto, with the ball at second upto."""
    ruler, marks, axes, top = drop_scene()
    s.add(ruler, marks, top, *[ax for ax, _ in axes], *[e for _, e in axes])
    for k in range(1, upto + 1):
        s.add(*drop_second(axes, k))
    ball = drop_ball(upto)
    s.add(ball)
    return axes, ball


def drop_step(axes, ball, k):
    segs, dots = drop_second(axes, k)
    return [ball.animate.shift(DOWN * (drop_y(DROP[k - 1][2]) - drop_y(DROP[k][2]))), Create(segs), FadeIn(dots)]


@slide("Take a ball dropped from rest.", "A dropped ball")
def drop1(s):
    ruler, marks, axes, top = drop_scene()
    ball = drop_ball(0)
    yield [Create(ruler), FadeIn(marks), FadeIn(ball[0]), *[Create(ax) for ax, _ in axes], *[FadeIn(e) for _, e in axes]]
    yield [GrowArrow(ball[1]), FadeIn(top)]


@slide("After one second it's falling at nine", "A dropped ball")
def drop2(s):
    axes, ball = drop_base(s, 0)
    yield drop_step(axes, ball, 1)


@slide("After two seconds it's at nineteen point", "A dropped ball")
def drop3(s):
    axes, ball = drop_base(s, 1)
    yield drop_step(axes, ball, 2)


@slide("After three seconds, twenty-nine point four", "A dropped ball")
def drop4(s):
    axes, ball = drop_base(s, 2)
    yield drop_step(axes, ball, 3)
    yield [FadeIn(lab("a straight line: v = g t", 24, INK).move_to([-0.9, -3.75, 0])),
           FadeIn(lab("grows with the square: ½ g t²", 24, INK).move_to([4.6, -3.75, 0]))]


@slide("For a spring or a pendulum, the force", "When the force depends on position")
def spring_force(s):
    xt = ValueTracker(1.0)
    base, spr, block = spring_rig(xt, wall=-6.8, rest=-3.6, y=0.7, sc=1.3, floor_to=-0.9)
    rest = DashedLine([-3.6, 0.2, 0], [-3.6, 1.6, 0], color=LINE, stroke_width=2)
    force = always_redraw(lambda: VMobject() if abs(xt.get_value()) < 0.05 else
                          Arrow([-3.6 + 1.3 * xt.get_value(), 1.45, 0], [-3.6 + 0.3 * xt.get_value(), 1.45, 0], buff=0,
                                color=ORANGE, stroke_width=5, tip_length=0.2))

    def stretch():
        x = xt.get_value()
        if abs(x) < 0.1:
            return VMobject()
        end = [-3.6 + 1.3 * x, -0.45, 0]
        line = DoubleArrow([-3.6, -0.45, 0], end, buff=0, color=BLUE, stroke_width=4, tip_length=0.16)
        return VGroup(line, T("x", 26, BLUE, True).next_to(line, DOWN, buff=0.1))

    xs = always_redraw(stretch)
    fx = at(eq("F = −k x", 40, ORANGE), 3.6, 1.9)
    key = at(W("k: the spring's stiffness, x: the stretch from rest", 30, 24, MUTED, align=ORIGIN), 3.6, 0.95)
    yield [FadeIn(base), FadeIn(spr), FadeIn(block), FadeIn(rest), FadeIn(force), FadeIn(xs),
           FadeIn(lab("rest", 22).move_to([-3.6, 1.85, 0])), FadeIn(lab("stiffness k", 24).move_to([-5.7, 1.85, 0])),
           xt.animate.set_value(-1.0), FadeIn(fx), FadeIn(key)]
    ax = Axes(x_range=[0, 6.3, 1], y_range=[-1.2, 1.2, 1], x_length=5.0, y_length=1.9, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([3.8, -1.35, 0])
    curve = DashedVMobject(ax.plot(lambda t: np.cos(t), x_range=[0, 6.3], color=BLUE, stroke_width=4), num_dashes=30)
    names = VGroup(lab("stretch x", 22).next_to(ax.y_axis, UP, buff=0.1), lab("time", 22).next_to(ax.x_axis, RIGHT, buff=0.15))
    yield [Create(ax), FadeIn(names), Create(curve),
           FadeIn(lab("solve F = ma for the unknown path", 24, INK).move_to([3.6, -2.75, 0]))]
    yield [FadeIn(lab("the logic is the same", 24, INK).move_to([3.6, -3.35, 0]))]


def energy_cards():
    left = at(card(None, 6.9, 4.8, TEAL), -3.65, -0.3)
    right = at(card(None, 6.9, 4.8, TEAL), 3.65, -0.3)
    lt = at(T("kinetic energy T", 30, TEAL, True), -3.65, 1.65)
    rt = at(T("potential energy V", 30, TEAL, True), 3.65, 1.65)
    return left, right, lt, rt


@slide("We'll need two kinds of energy, so", "Two kinds of energy")
def kinetic(s):
    left, right, lt, rt = energy_cards()
    yield [FadeIn(left), FadeIn(right), FadeIn(lt), FadeIn(rt)]
    track = Line([-6.6, -0.6, 0], [-0.7, -0.6, 0], color=LINE, stroke_width=3)
    ball = VGroup(Dot([-5.9, -0.42, 0], radius=0.18, color=BLUE),
                  Arrow([-5.7, -0.42, 0], [-4.7, -0.42, 0], buff=0, color=BLUE, stroke_width=5, tip_length=0.2))
    yield [FadeIn(at(T("energy of motion", 26, INK), -3.65, 1.05)), Create(track), FadeIn(ball), ball.animate.shift(RIGHT * 3.6)]
    yield [FadeIn(at(eq("T = ½ m v²", 38, TEAL), -3.65, -1.65)), FadeIn(lab("mass m, speed v", 22).move_to([-3.65, -2.3, 0]))]


def kinetic_done():
    track = Line([-6.6, -0.6, 0], [-0.7, -0.6, 0], color=LINE, stroke_width=3)
    ball = VGroup(Dot([-2.3, -0.42, 0], radius=0.18, color=BLUE),
                  Arrow([-2.1, -0.42, 0], [-1.1, -0.42, 0], buff=0, color=BLUE, stroke_width=5, tip_length=0.2))
    return VGroup(at(T("energy of motion", 26, INK), -3.65, 1.05), track, ball, at(eq("T = ½ m v²", 38, TEAL), -3.65, -1.65),
                  lab("mass m, speed v", 22).move_to([-3.65, -2.3, 0]))


@slide("Potential energy is energy stored by position.", "Two kinds of energy")
def potential(s):
    left, right, lt, rt = energy_cards()
    s.add(left, right, lt, rt, kinetic_done())
    yield [FadeIn(at(T("energy stored by position", 26, INK), 3.65, 1.05))]
    ground = Line([0.6, -1.0, 0], [3.2, -1.0, 0], color=LINE, stroke_width=3)
    ball = Dot([1.9, -0.82, 0], radius=0.18, color=BLUE)
    hline = DashedLine([1.1, -1.0, 0], [1.1, 0.35, 0], color=BLUE, stroke_width=3)
    yield [Create(ground), FadeIn(ball), ball.animate.shift(UP * 1.2), Create(hline),
           FadeIn(T("x", 24, BLUE).next_to(hline, LEFT, buff=0.1)), FadeIn(at(eq("V = m g x", 30, TEAL), 1.9, -1.5)),
           FadeIn(lab("ball at height x", 22).move_to([1.9, -1.98, 0])), FadeIn(lab("g = 9.8", 22).move_to([1.9, -2.36, 0]))]
    xt = ValueTracker(0.0)
    base, spr, block = spring_rig(xt, wall=3.9, rest=5.3, y=-0.55, sc=0.9, size=0.55, floor_to=7.0)
    yield [FadeIn(base), FadeIn(spr), FadeIn(block), xt.animate.set_value(1.0), FadeIn(at(eq("V = ½ k x²", 30, TEAL), 5.5, -1.5)),
           FadeIn(lab("spring, stiffness k", 22).move_to([5.5, -1.98, 0])), FadeIn(lab("stretched by x", 22).move_to([5.5, -2.36, 0]))]


@slide("The slope of the potential energy is how", "Force is minus the slope")
def slope(s):
    ax = Axes(x_range=[-1.6, 1.6, 1], y_range=[0, 2.7, 1], x_length=6.6, y_length=4.0, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([-2.9, -0.6, 0])
    names = VGroup(lab("position x", 22).next_to(ax.x_axis, DOWN, buff=0.15).align_to(ax.x_axis, RIGHT),
                   lab("potential energy V", 22, TEAL).next_to(ax.y_axis, UP, buff=0.1))
    curve = ax.plot(lambda x: x * x, x_range=[-1.6, 1.6], color=TEAL, stroke_width=5)
    xt = ValueTracker(1.2)
    ball = always_redraw(lambda: Dot(ax.c2p(xt.get_value(), xt.get_value() ** 2), radius=0.16, color=BLUE))

    def tangent():
        x = xt.get_value()
        p = ax.c2p(x, x * x)
        d = ax.c2p(x + 0.35, x * x + 0.7 * x) - ax.c2p(x - 0.35, x * x - 0.7 * x)
        return Line(p - d / 2, p + d / 2, color=MUTED, stroke_width=3)

    tan = always_redraw(tangent)
    push = always_redraw(lambda: Arrow(ax.c2p(xt.get_value(), xt.get_value() ** 2) + DOWN * 0.45,
                                       ax.c2p(0.25 * xt.get_value(), xt.get_value() ** 2) + DOWN * 0.45, buff=0,
                                       color=ORANGE, stroke_width=5, tip_length=0.2))
    rule = at(eq("F = − slope of V", 34, ORANGE), 4.0, 0.9)
    yield [Create(ax), FadeIn(names), Create(curve), FadeIn(T("V = ½ k x²", 26, TEAL).next_to(ax.c2p(1.6, 2.56), LEFT, buff=0.25)),
           FadeIn(ball), Create(tan), FadeIn(at(W("slope: how steeply V changes with position", 24, 26, INK), 4.0, 2.0))]
    yield [GrowArrow(push), FadeIn(rule), FadeIn(lab("pushed toward lower potential energy", 24).next_to(rule, DOWN, buff=0.25))]
    restd = Dot(ax.c2p(0, 0), radius=0.1, color=INK)
    yield [xt.animate.set_value(-1.2), FadeIn(restd), FadeIn(lab("rest", 22).next_to(restd, DOWN, buff=0.12)),
           FadeIn(at(W("For the spring: a pull back toward the rest position", 26, 26, INK), 4.0, -1.5))]


# ------------------------------------------------------------------ awkward forces
deck.part("Where forces become awkward")


@slide("Where forces become awkward.", "Every force on the list")
def track(s):
    c = np.array([-3.0, 2.6, 0])
    r = 3.8
    rail = Arc(radius=r, start_angle=-PI / 2 - 0.9, angle=1.8, arc_center=c, color=LINE, stroke_width=8)
    th = -PI / 2 - 0.45
    p = c + r * np.array([np.cos(th), np.sin(th), 0])
    bead = Dot(p, radius=0.2, color=BLUE)
    yield [Create(rail), FadeIn(bead), FadeIn(lab("a body held to a track", 24).move_to([-2.4, -2.6, 0]))]
    grav = Arrow(p, p + DOWN * 1.2, buff=0, color=ORANGE, stroke_width=5, tip_length=0.2)
    head = at(T("To use F = ma, list every force:", 28, INK), 3.4, 1.6)
    l1 = T("gravity", 26, ORANGE).move_to([1.5, 0.7, 0], aligned_edge=LEFT)
    yield [FadeIn(head), GrowArrow(grav), FadeIn(l1)]
    n = (c - p) / np.linalg.norm(c - p)
    push = Arrow(p, p + n * 1.2, buff=0, color=ORANGE, stroke_width=5, tip_length=0.2)
    l2 = W("the track's push, whose only job is to keep it on its path", 30, 26, ORANGE).move_to([1.5, -0.4, 0], aligned_edge=UL)
    yield [GrowArrow(push), FadeIn(l2)]


PIV = np.array([-3.4, 2.3, 0])
PL = 3.6
TH0 = 35 * DEGREES


def tension_len(th):
    return 0.85 * (3 * np.cos(th) - 2 * np.cos(TH0))


@slide("Take a pendulum, a weight on a", "Gravity is known, the tension is not")
def tension(s):
    tr = ValueTracker(TH0)
    bar, string, bob = pend_live(PIV, PL, tr)
    yield [FadeIn(bar), Create(swing_arc(PIV, PL)), FadeIn(string), FadeIn(bob)]
    grav = always_redraw(lambda: Arrow(pend_pos(PIV, PL, tr.get_value()), pend_pos(PIV, PL, tr.get_value()) + DOWN * 1.1, buff=0,
                                       color=ORANGE, stroke_width=5, tip_length=0.2))

    def tens():
        b = pend_pos(PIV, PL, tr.get_value())
        u = (PIV - b) / PL
        return Arrow(b, b + u * tension_len(tr.get_value()), buff=0, color=ORANGE, stroke_width=6, tip_length=0.22)

    ten = always_redraw(tens)
    g_txt = T("gravity", 28, ORANGE).move_to([2.0, 1.2, 0], aligned_edge=LEFT)
    t_txt = T("tension in the string", 28, ORANGE).move_to([2.0, 0.1, 0], aligned_edge=LEFT)
    yield [GrowArrow(grav), GrowArrow(ten), FadeIn(g_txt), FadeIn(t_txt)]
    yield [FadeIn(check().next_to(g_txt, RIGHT, buff=0.25)), FadeIn(lab("known", 24, TEAL).next_to(g_txt, DOWN, aligned_edge=LEFT, buff=0.15))]
    yield [tr.animate.set_value(-TH0), FadeIn(W("unknown: it adjusts at every moment to keep the weight on its circle", 30, 24, ORANGE).next_to(t_txt, DOWN, aligned_edge=LEFT, buff=0.15))]


def single_trick(th=30 * DEGREES):
    g = pend_static(PIV, PL, th)
    b = pend_pos(PIV, PL, th)
    u = (PIV - b) / PL
    t = np.array([np.cos(th), np.sin(th), 0])
    ten = Arrow(b, b + u * 1.1, buff=0, color=ORANGE, stroke_width=6, tip_length=0.22)
    mot = Arrow(b, b + t * 1.3, buff=0, color=BLUE, stroke_width=5, tip_length=0.2)
    sq = VMobject(color=MUTED, stroke_width=2).set_points_as_corners([b + u * 0.28, b + u * 0.28 + t * 0.28, b + t * 0.28])
    return g, b, u, t, ten, mot, sq


@slide("For a single pendulum, there's a trick.", "The trick for one pendulum")
def trick(s):
    th = 30 * DEGREES
    g, b, u, t, ten, mot, sq = single_trick(th)
    yield [FadeIn(g), Create(swing_arc(PIV, PL)), FadeIn(at(card("a trick for one pendulum", 5.4, 0.9, INK, 28), 3.8, 1.9))]
    yield [GrowArrow(ten), GrowArrow(mot), Create(sq), FadeIn(lab("motion", 24, BLUE).next_to(mot.get_end(), UR, buff=0.08)),
           FadeIn(lab("tension", 24, ORANGE).next_to(ten.get_end(), LEFT, buff=0.15)),
           FadeIn(W("The string pulls at right angles to the motion.", 30, 26, INK).move_to([1.4, 0.6, 0], aligned_edge=UL))]
    grav = Arrow(b, b + DOWN * 1.2, buff=0, color=ORANGE, stroke_width=5, tip_length=0.2)
    along = Arrow(b, b - t * 1.2 * np.sin(th), buff=0, color=TEAL, stroke_width=5, tip_length=0.18)
    yield [GrowArrow(grav), GrowArrow(along), ten.animate.set_opacity(0.5),
           FadeIn(lab("gravity", 24, ORANGE).next_to(grav.get_end(), RIGHT, buff=0.12)),
           FadeIn(lab("along the circle", 24, TEAL).next_to(along.get_end(), LEFT, buff=0.12)),
           FadeIn(W("Along the circle only gravity counts, so the tension drops out.", 30, 26, TEAL).move_to([1.4, -0.8, 0], aligned_edge=UL))]


D1 = (np.array([-3.4, 2.4, 0]), 2.5, 2.0, 20 * DEGREES, 50 * DEGREES)


def double_parts():
    piv, l1, l2, t1, t2 = D1
    g, b1, b2 = double_pend(piv, l1, l2, t1, t2)
    t = np.array([np.cos(t1), np.sin(t1), 0])
    u = (b2 - b1) / l2
    mot = Arrow(b1, b1 + t * 1.2, buff=0, color=BLUE, stroke_width=5, tip_length=0.2)
    ten = Arrow(b1, b1 + u * 1.15, buff=0, color=ORANGE, stroke_width=6, tip_length=0.22)
    ang = Arc(radius=0.5, start_angle=np.arctan2(u[1], u[0]), angle=np.arctan2(t[1], t[0]) - np.arctan2(u[1], u[0]),
              arc_center=b1, color=ORANGE, stroke_width=3)
    return g, b1, b2, mot, ten, ang


def trick_card(crossed=False):
    c = at(card("the trick: look only\nalong the circle", 5.2, 1.4, INK, 27), 3.6, 1.6)
    return VGroup(c.fade(0.6), trick_x(c)) if crossed else c


def trick_x(c):
    mark = Square(0.45).next_to(c, RIGHT, buff=0.25)
    return cross(mark, RED, 7)


@slide("But hang a second pendulum from the", "A second pendulum breaks the trick")
def double1(s):
    g, b1, b2, mot, ten, ang = double_parts()
    s.add(g[0], g[1], g[3])
    tc = trick_card()
    yield [Create(g[2]), FadeIn(g[4]), FadeIn(tc)]
    yield [GrowArrow(mot), GrowArrow(ten), Create(ang),
           FadeIn(W("The lower string pulls on the upper weight at an angle to its motion.", 30, 26, ORANGE).move_to([1.3, 0.3, 0], aligned_edge=UL)),
           tc.animate.fade(0.6), Create(trick_x(tc))]


@slide("So now you have to solve for", "One recipe in the angles")
def double2(s):
    g, b1, b2, mot, ten, ang = double_parts()
    s.add(g, mot, ten, ang, trick_card(True))
    q = T("?", 40, ORANGE, True).next_to(ten.get_end(), RIGHT, buff=0.15)
    yield [FadeIn(q), FadeIn(W("Solve for this tension first.", 30, 26, ORANGE).move_to([1.3, 0.3, 0], aligned_edge=UL))]
    piv, l1, l2, t1, t2 = D1
    a1 = angle_mark(piv, l1, t1, "θ₁", r=0.9)
    a2 = angle_mark(b1, l2, t2, "θ₂", r=0.75)
    goal = at(card("Wanted: one recipe that works with\nthe angles directly and never\nmentions constraint forces", 6.4, 1.9, BLUE, 26), 3.9, -1.6)
    yield [FadeIn(a1), FadeIn(a2), FadeIn(goal), ten.animate.set_opacity(0.2), q.animate.set_opacity(0.2)]
    yield [FadeIn(at(T("built from the energies alone", 28, TEAL, True), 3.9, -3.1), shift=UP * 0.15)]


# ------------------------------------------------------------------ the action
deck.part("One number for a whole path")


@slide("One number for a whole path.", "Energies alone")
def energies_alone(s):
    tv = at(VGroup(chip("T", TEAL, size=34, h=0.9), chip("V", TEAL, size=34, h=0.9)).arrange(RIGHT, buff=0.3), -4.6, 1.4)
    goal = at(T("the motion?", 32, BLUE, True), 2.4, 1.4)
    yield [FadeIn(tv), FadeIn(lab("energies alone", 24).next_to(tv, UP, buff=0.2)), GrowArrow(arrow(tv, goal)), FadeIn(goal)]
    cons = at(card("conservation of energy\nT + V stays the same", 6.0, 1.6, TEAL, 28), -3.4, -1.3)
    yield [FadeIn(cons, shift=UP * 0.2)]
    yield [FadeIn(at(T("not enough on its own", 30, INK), 3.4, -1.3))]


@slide("It's one equation, and the double pendulum", "One equation, two unknowns")
def two_unknowns(s):
    g, b1, b2 = double_pend([-4.6, 2.3, 0], 1.9, 1.5, 20 * DEGREES, 50 * DEGREES, r=0.16)
    a1 = angle_mark([-4.6, 2.3, 0], 1.9, 20 * DEGREES, "θ₁", r=0.75, size=24)
    a2 = angle_mark(b1, 1.5, 50 * DEGREES, "θ₂", r=0.6, size=24)
    one = at(card("1 equation", 2.8, 0.85, TEAL, 30), 0.5, 1.6)
    two = at(card("2 angles to find", 3.6, 0.85, BLUE, 30), 5.0, 1.6)
    yield [FadeIn(g), FadeIn(a1), FadeIn(a2), FadeIn(one), FadeIn(two), FadeIn(at(T("<", 40, INK, True), 2.55, 1.6))]
    a, b = [0.2, -2.6, 0], [6.4, -2.6, 0]
    bundle = VGroup(*[ArcBetweenPoints(a, b, angle=-ang, color=LINE, stroke_width=3) for ang in (0.5, 1.0, 1.9, 2.4)])
    real = ArcBetweenPoints(a, b, angle=-1.45, color=BLUE, stroke_width=5)
    yield [Create(bundle), Create(real), FadeIn(Dot(a, radius=0.08, color=INK)), FadeIn(Dot(b, radius=0.08, color=INK)),
           FadeIn(at(T("the rule that works compares whole paths", 26, INK), 3.3, -3.4))]


def height(t, e=0.0):
    return 9.8 * t - 4.9 * t * t + e * np.sin(np.pi * t / 2)


def throw_axes(cx=-3.6, cy=-0.35, w=6.6, h=4.4, numbers=True):
    ax = Axes(x_range=[0, 2, 1], y_range=[0, 6, 1], x_length=w, y_length=h, tips=False,
              axis_config={"color": LINE, "include_ticks": False}).move_to([cx, cy, 0])
    extra = VGroup(lab("height (m)", 22).next_to(ax.y_axis, UP, buff=0.12),
                   lab("time (s)", 22).next_to(ax.x_axis, DOWN, buff=0.5).align_to(ax.x_axis, RIGHT))
    if numbers:
        for t in (0, 1, 2):
            extra.add(lab(str(t), 22).next_to(ax.c2p(t, 0), DOWN, buff=0.12))
    return ax, extra


def throw_path(ax, e=0.0, color=BLUE, width=5):
    return ax.plot(lambda t: height(t, e), x_range=[0, 2], color=color, stroke_width=width)


def candidates(ax):
    fns = [lambda t: 2.4 * np.sin(np.pi * t / 2), lambda t: 2.8 * t * (2 - t),
           lambda t: height(t) + 0.7 * np.sin(2 * np.pi * t), lambda t: 1.2 * t * (2 - t) * (1 + t)]
    return VGroup(*[ax.plot(f, x_range=[0, 2], color=LINE, stroke_width=4) for f in fns])


@slide("So we change the question.", "Change the question")
def new_question(s):
    old = at(card("How does it accelerate at each moment?", 8.4, 0.9, MUTED, 28), 0, 2.0)
    yield [FadeIn(old)]
    yield [Create(strike(old[0], MUTED))]
    ax, extra = throw_axes(0, -0.95, 7.4, 3.4)
    ends = VGroup(Dot(ax.c2p(0, 0), radius=0.12, color=BLUE), Dot(ax.c2p(2, 0), radius=0.12, color=BLUE))
    yield [Create(ax), FadeIn(extra), FadeIn(ends), Flash(ends[0], color=BLUE), Flash(ends[1], color=BLUE),
           FadeIn(lab("start: fixed", 24, BLUE).next_to(ends[0], UL, buff=0.1)),
           FadeIn(lab("end: fixed", 24, BLUE).next_to(ends[1], UR, buff=0.1))]


@slide("Then ask which path between those two", "Which path between them?")
def which_path(s):
    ax, extra = throw_axes(0, -0.95, 7.4, 3.4)
    ends = VGroup(Dot(ax.c2p(0, 0), radius=0.12, color=BLUE), Dot(ax.c2p(2, 0), radius=0.12, color=BLUE))
    s.add(ax, extra, ends)
    yield [LaggedStart(*[Create(c) for c in candidates(ax)], lag_ratio=0.2), FadeIn(at(T("which path?", 30, INK), 0, 1.9))]
    real = throw_path(ax)
    tag = at(T("the one it takes", 26, BLUE), 5.5, 0.4)
    yield [Create(real), FadeIn(tag), GrowArrow(Arrow(tag.get_bottom() + LEFT * 0.4, ax.c2p(1.72, height(1.72)), buff=0.15, color=BLUE,
                                                      stroke_width=4, tip_length=0.18)),
           FadeIn(caption("Fixing both ends usually pins down the motion, as a starting position and speed would.", y=-3.75, color=INK, size=25))]


def score_axes():
    return throw_axes(-2.4, 0.75, 7.4, 2.7)


def l_values():
    return [(t, 48.02 * (1 - t) ** 2 - 9.8 * height(t)) for t in np.arange(0.05, 2.0, 0.1)]


def l_bars(ax, base_y=-2.25, k=0.011):
    bars = VGroup()
    for t, v in l_values():
        x = ax.c2p(t, 0)[0]
        h = abs(v) * k
        bars.add(Rectangle(width=0.27, height=max(h, 0.01), stroke_width=0, fill_color=PURPLE, fill_opacity=0.75)
                 .move_to([x, base_y + np.sign(v) * h / 2, 0]))
    base = Line(ax.c2p(0, 0) * [1, 0, 0] + [0, base_y, 0], ax.c2p(2, 0) * [1, 0, 0] + [0, base_y, 0], color=LINE, stroke_width=2)
    return bars, base


def lagrangian_eq():
    e = at(eq("L = T − V", 42, PURPLE), 4.9, 1.6)
    return VGroup(e, lab("the Lagrangian", 24, PURPLE).next_to(e, DOWN, buff=0.2))


@slide("To compare paths, we give each one", "A score for each moment")
def score(s):
    ax, extra = score_axes()
    real = throw_path(ax)
    dot = Dot(ax.c2p(0, 0), radius=0.12, color=BLUE)
    yield [Create(ax), FadeIn(extra), Create(real), FadeIn(dot), MoveAlongPath(dot, real)]
    bars, base = l_bars(ax)
    yield [Create(base), LaggedStart(*[GrowFromEdge(b, DOWN if b.get_y() > -2.25 else UP) for b in bars], lag_ratio=0.05),
           FadeIn(at(T("T − V at each moment", 26, PURPLE), 4.9, -2.25))]
    yield [FadeIn(lagrangian_eq())]


@slide("Add it up over the whole trip,", "The action of a path")
def action(s):
    ax, extra = score_axes()
    real = throw_path(ax)
    bars, base = l_bars(ax)
    s.add(ax, extra, real, bars, base, lagrangian_eq())
    total = at(chip("S", PURPLE, size=34, h=0.8), 4.9, -0.2)
    yield [ReplacementTransform(bars, total), FadeOut(base), FadeIn(lab("the action: the total over the trip", 24, PURPLE).move_to([4.9, -0.95, 0]))]
    up, down = throw_path(ax, 0.5, ORANGE, 4), throw_path(ax, -0.5, ORANGE, 4)
    yield [Create(up), Create(down),
           FadeIn(at(VGroup(lab("paths it never takes:", 24, ORANGE), chip("S", PURPLE, size=28, h=0.7)).arrange(RIGHT, buff=0.2), 4.9, -2.0)),
           FadeIn(lab("every path gets a number", 24, INK).move_to([4.9, -2.8, 0]))]


def s_curve_plot(cx, cy, w, h, e_lo=-0.6, e_hi=0.6, s_lo=-32.06, s_hi=-31.6):
    """A plain plot of the action of T − V against the bend."""
    def p(e, v):
        return np.array([cx + (e - (e_lo + e_hi) / 2) / (e_hi - e_lo) * w, cy + (v - (s_lo + s_hi) / 2) / (s_hi - s_lo) * h, 0])
    frame = VGroup(Line(p(e_lo, s_lo), p(e_hi, s_lo), color=LINE, stroke_width=3), Line(p(0, s_lo), p(0, s_hi), color=LINE, stroke_width=3))
    curve = VMobject(color=PURPLE, stroke_width=5).set_points_smoothly([p(e, -32.01 + 1.23 * e * e) for e in np.linspace(-0.55, 0.55, 23)])
    return p, frame, curve


@slide("Now the rule.", "Bend the path a little")
def bend(s):
    ax, extra = throw_axes(-3.7, -0.35, 6.4, 4.2)
    real = throw_path(ax)
    et = ValueTracker(0.0)
    bent = always_redraw(lambda: ax.plot(lambda t: height(t, et.get_value()), x_range=[0, 2], color=ORANGE, stroke_width=4))
    ends = VGroup(Dot(ax.c2p(0, 0), radius=0.1, color=INK), Dot(ax.c2p(2, 0), radius=0.1, color=INK))
    s.add(ax, extra, real, ends)
    yield [FadeIn(bent), et.animate.set_value(0.5), Flash(ends[0], color=INK), Flash(ends[1], color=INK),
           FadeIn(lab("both ends stay fixed", 24, INK).move_to([-3.7, 2.35, 0]))]
    p, frame, curve = s_curve_plot(3.9, 0.1, 5.4, 3.6)
    dot = always_redraw(lambda: Dot(p(et.get_value(), -32.01 + 1.23 * et.get_value() ** 2), radius=0.11, color=ORANGE))
    rise = always_redraw(lambda: Line(p(et.get_value(), -32.01), p(et.get_value(), -32.01 + 1.23 * et.get_value() ** 2),
                                      color=ORANGE, stroke_width=4))
    yield [Create(frame), Create(curve), FadeIn(dot), FadeIn(rise), FadeIn(lab("action", 24, PURPLE).next_to(frame[1], UP, buff=0.1)),
           FadeIn(lab("bend", 24).move_to([6.3, -2.05, 0])),
           FadeIn(lab("change grows like the bend squared", 24, INK).move_to([3.9, -2.65, 0]))]
    yield [et.animate.set_value(0.25), FadeIn(at(T("bend × ½  →  change × ¼", 28, ORANGE, True), 3.9, -3.4))]


def flat_icon(x, y, up=True, color=PURPLE):
    sgn = 1 if up else -1
    curve = VMobject(color=color, stroke_width=4).set_points_smoothly([[x + u, y + sgn * 0.55 * u * u, 0] for u in np.linspace(-1.2, 1.2, 13)])
    tan = DashedLine([x - 0.8, y, 0], [x + 0.8, y, 0], color=color, stroke_width=3)
    return VGroup(curve, tan, Dot([x, y, 0], radius=0.09, color=BLUE))


@slide("So for small bends, the change shrinks", "A flat spot")
def flat(s):
    p, frame, curve = s_curve_plot(-3.2, -0.2, 6.6, 4.2)
    et = ValueTracker(0.45)
    dot = always_redraw(lambda: Dot(p(et.get_value(), -32.01 + 1.23 * et.get_value() ** 2), radius=0.12, color=ORANGE))
    yield [Create(frame), Create(curve), FadeIn(dot), et.animate.set_value(0.08),
           FadeIn(lab("action", 24, PURPLE).next_to(frame[1], UP, buff=0.1)),
           FadeIn(lab("bend", 24).next_to(frame[0], RIGHT, buff=0.15)),
           FadeIn(at(W("small bend: the change shrinks much faster than the bend", 30, 24, INK), 3.9, 2.0))]
    tan = DashedLine(p(-0.45, -32.01), p(0.45, -32.01), color=PURPLE, stroke_width=4)
    yield [et.animate.set_value(0.0), Create(tan), FadeIn(at(T("the real path: a flat spot", 26, BLUE), -3.2, -2.85))]
    v, h = flat_icon(3.2, 0.6), flat_icon(5.9, 1.2, up=False)
    yield [FadeIn(v), FadeIn(h), FadeIn(lab("bottom of a valley", 22).move_to([3.2, -0.3, 0])),
           FadeIn(lab("top of a hill", 22).move_to([5.9, -0.3, 0]))]


@slide("We call this rule the principle", "Stationary, not least")
def stationary(s):
    v, h = flat_icon(-3.4, 0.9), flat_icon(3.4, 1.5, up=False)
    s.add(v, h, lab("bottom of a valley", 22).move_to([-3.4, 0.0, 0]), lab("top of a hill", 22).move_to([3.4, 0.0, 0]))
    st = at(card("the principle of\nstationary action", 5.6, 1.5, PURPLE, 32), -2.6, -1.6)
    yield [FadeIn(st, shift=UP * 0.2), Indicate(v[1], color=PURPLE), Indicate(h[1], color=PURPLE)]
    least = at(chip("least action", MUTED, size=28, h=0.8), 3.4, -1.6)
    yield [FadeIn(least), Create(strike(least, MUTED)), Indicate(h, color=PURPLE),
           FadeIn(lab("a flat spot need not be a lowest point", 24, INK).move_to([3.4, -2.6, 0]))]


THROW = dict(cx=-3.7, cy=-0.35, w=6.4, h=4.4)


def fact(text, y, color=INK):
    return W(text, 28, 28, color).move_to([0.8, y, 0], aligned_edge=UL)


def throw_base():
    ax, extra = throw_axes(**THROW)
    return ax, extra, throw_path(ax)


@slide("Let's try it.", "A ball thrown up and caught")
def throw1(s):
    ax, extra, real = throw_base()
    ball = Dot(ax.c2p(0, 0), radius=0.14, color=BLUE)
    yield [Create(ax), FadeIn(extra), FadeIn(ball), FadeIn(lab("hand", 22).next_to(ax.c2p(0, 0), LEFT, buff=0.15)),
           FadeIn(fact("A 1 kg ball, back in the hand after 2 s", 1.6))]
    yield [Create(real), MoveAlongPath(ball, real)]
    mid = DashedLine(ax.c2p(1, 0), ax.c2p(1, 4.9), color=LINE, stroke_width=2)
    yield [Create(mid), FadeIn(lab("rises 1 s", 22, INK).move_to(ax.c2p(0.5, 1.2))), FadeIn(lab("falls 1 s", 22, INK).move_to(ax.c2p(1.5, 1.2))),
           FadeIn(fact("Rises for 1 s, falls for 1 s", 0.5))]


@slide("So it leaves your hand at nine", "A ball thrown up and caught")
def throw2(s):
    ax, extra, real = throw_base()
    mid = DashedLine(ax.c2p(1, 0), ax.c2p(1, 4.9), color=LINE, stroke_width=2)
    s.add(ax, extra, real, mid, lab("hand", 22).next_to(ax.c2p(0, 0), LEFT, buff=0.15),
          fact("A 1 kg ball, back in the hand after 2 s", 1.6), fact("Rises for 1 s, falls for 1 s", 0.5))
    o = ax.c2p(0, 0)
    d = ax.c2p(0.25, 2.45) - o
    v = Arrow(o, o + d / np.linalg.norm(d) * 1.4, buff=0, color=BLUE, stroke_width=5, tip_length=0.2)
    yield [GrowArrow(v), FadeIn(fact("Leaves the hand at 9.8 m/s", -0.4, BLUE))]
    top = DashedLine(ax.c2p(0, 4.9), ax.c2p(1, 4.9), color=BLUE, stroke_width=2)
    yield [Create(top), FadeIn(T("4.9 m", 24, BLUE).next_to(ax.c2p(0, 4.9), LEFT, buff=0.12)),
           FadeIn(fact("Climbs to 4.9 m, then comes back down", -1.5))]


def bent_paths(ax):
    return VGroup(throw_path(ax, 0.5, ORANGE, 4), throw_path(ax, -0.5, ORANGE, 4),
                  throw_path(ax, 0.2, ORANGE, 3).set_stroke(opacity=0.55), throw_path(ax, -0.2, ORANGE, 3).set_stroke(opacity=0.55))


@slide("Now compare it with bent paths.", "Bent paths, same ends")
def throw3(s):
    ax, extra, real = throw_base()
    s.add(ax, extra, real)
    bent = bent_paths(ax)
    ends = VGroup(Dot(ax.c2p(0, 0), radius=0.1, color=INK), Dot(ax.c2p(2, 0), radius=0.1, color=INK))
    yield [Create(bent[0]), Create(bent[1]), FadeIn(fact("Bent paths", 1.6, ORANGE))]
    yield [Create(bent[2]), Create(bent[3]), FadeIn(ends), Flash(ends[0], color=INK), Flash(ends[1], color=INK),
           FadeIn(fact("They leave and return at the same moments, but bulge up or down by up to 0.5 m.", 0.6))]


TMV = [(-0.5, -31.70, "−31.70"), (-0.2, -31.96, "−31.96"), (0.0, -32.01, "−32.01"), (0.2, -31.96, "−31.96"), (0.5, -31.70, "−31.70")]
TPV = [(-0.5, 83.87, "83.87"), (-0.2, 91.10, "91.10"), (0.0, 96.04, "96.04"), (0.2, 101.08, "101.08"), (0.5, 108.83, "108.83")]


def tmv_plot():
    """The action of T − V against the bend, as in the right half of StationaryActionPaths."""
    p, frame, curve = s_curve_plot(4.1, 0.85, 5.2, 2.2, s_lo=-32.14, s_hi=-31.62)
    title = at(T("action of T − V", 26, PURPLE), 4.1, 2.35)
    ticks = VGroup(*[lab(t, 22).move_to(p(e, -32.14) + DOWN * 0.3) for e, t in ((-0.5, "−0.5"), (0.0, "0"), (0.5, "0.5"))])
    name = lab("bulge (m)", 22).next_to(p(0.6, -32.14), UP, buff=0.1)
    ticks.add(name.align_to(p(0.6, -32.14), RIGHT))
    return p, frame, curve, title, ticks


def tmv_point(p, k):
    e, v, t = TMV[k]
    d = Dot(p(e, v), radius=0.09, color=PURPLE)
    label = T(t, 22, PURPLE)
    if k == 2:
        label.next_to(d, DR, buff=0.06)
    elif abs(e) < 0.3:
        label.move_to(d.get_center() + UP * 0.5)
    else:
        label.next_to(d, LEFT if e < 0 else RIGHT, buff=0.15)
    return VGroup(d, label)


def throw_left(s, bright=()):
    ax, extra, real = throw_base()
    bent = bent_paths(ax)
    s.add(ax, extra, real, bent)
    return ax, real, bent


@slide("The real path has an action of", "Scoring the paths")
def score1(s):
    ax, real, bent = throw_left(s)
    p, frame, curve, title, ticks = tmv_plot()
    yield [FadeIn(title), Create(frame), FadeIn(ticks), FadeIn(tmv_point(p, 2)), Indicate(real, color=BLUE, scale_factor=1.04)]
    yield [bent[2].animate.set_stroke(width=5, opacity=1), bent[3].animate.set_stroke(width=5, opacity=1)]
    yield [FadeIn(tmv_point(p, 1)), FadeIn(tmv_point(p, 3))]


@slide("Bulge it by half a metre either", "Scoring the paths")
def score2(s):
    ax, real, bent = throw_left(s)
    p, frame, curve, title, ticks = tmv_plot()
    s.add(title, frame, ticks, *[tmv_point(p, k) for k in (1, 2, 3)])
    yield [FadeIn(tmv_point(p, 0)), FadeIn(tmv_point(p, 4)), Indicate(bent[0], color=ORANGE), Indicate(bent[1], color=ORANGE)]
    yield [Create(curve), FadeIn(at(T("up or down: the same", 26, INK), 4.1, -1.1))]


@slide("Making the bulge two and a half", "The square growth of a flat spot")
def score3(s):
    ax, real, bent = throw_left(s)
    p, frame, curve, title, ticks = tmv_plot()
    s.add(title, frame, ticks, curve, *[tmv_point(p, k) for k in range(5)])
    rows = VGroup(eq("bulge   0.2 → 0.5    × 2.5", 26, ORANGE), eq("change  0.049 → 0.308  × 6.25", 26, PURPLE)).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
    at(rows, 4.1, -1.5)
    yield [FadeIn(rows[0]), FadeIn(rows[1])]
    tan = DashedLine(p(-0.35, -32.01), p(0.35, -32.01), color=PURPLE, stroke_width=4)
    yield [Create(tan), FadeIn(at(T("2.5² = 6.25: a flat spot", 26, INK), 4.1, -2.75))]


def tpv_plot():
    def p(e, v):
        return np.array([4.1 + e / 1.2 * 5.2, -2.6 + (v - 96.0) / 28.0 * 1.5, 0])
    frame = VGroup(Line(p(-0.6, 82), p(0.6, 82), color=LINE, stroke_width=3), Line(p(0, 82), p(0, 110), color=LINE, stroke_width=3))
    line = VMobject(color=RED, stroke_width=5).set_points_smoothly([p(e, 96.04 + 24.96 * e + 1.23 * e * e) for e in np.linspace(-0.55, 0.55, 12)])
    title = at(T("total of T + V instead", 26, RED), 4.1, -1.15)
    return p, frame, line, title


def tpv_point(p, k, label=True):
    e, v, t = TPV[k]
    d = Dot(p(e, v), radius=0.09, color=RED)
    if not label:
        return VGroup(d)
    return VGroup(d, T(t, 22, RED).next_to(d, DR if k == 2 else (RIGHT if e > 0 else LEFT), buff=0.12))


@slide("Now try the energy itself, kinetic plus", "Try T + V instead")
def tpv1(s):
    ax, real, bent = throw_left(s)
    p, frame, curve, title, ticks = tmv_plot()
    s.add(title, frame, ticks, curve, *[tmv_point(p, k) for k in range(5)])
    q, f2, line, t2 = tpv_plot()
    yield [FadeIn(t2), Create(f2)]
    yield [FadeIn(tpv_point(q, 2))]
    yield [FadeIn(tpv_point(q, 0)), FadeIn(tpv_point(q, 1, False)), FadeIn(tpv_point(q, 3, False)), FadeIn(tpv_point(q, 4)), Create(line)]


@slide("So the real path isn't a flat", "Why the sign is minus")
def tpv2(s):
    ax, real, bent = throw_left(s)
    p, frame, curve, title, ticks = tmv_plot()
    q, f2, line, t2 = tpv_plot()
    s.add(title, frame, ticks, curve, *[tmv_point(p, k) for k in range(5)], t2, f2, line,
          *[tpv_point(q, k, k in (0, 2, 4)) for k in range(5)])
    flat_t = DashedLine(p(-0.3, -32.01), p(0.3, -32.01), color=PURPLE, stroke_width=4)
    slope_t = DashedLine(q(-0.35, 96.04 - 24.96 * 0.35), q(0.35, 96.04 + 24.96 * 0.35), color=RED, stroke_width=4)
    yield [Create(flat_t), Create(slope_t), FadeIn(check().next_to(title, RIGHT, buff=0.25)),
           FadeIn(VGroup(Line(UL, DR), Line(DL, UR)).scale(0.17).set_stroke(RED, 6).next_to(t2, RIGHT, buff=0.25))]
    yield [Indicate(title, color=PURPLE, scale_factor=1.15),
           FadeIn(at(T("so L = T − V subtracts V", 28, PURPLE, True), -3.7, -3.6))]


@slide("For the systems in this chapter, stationary", "Newton's law in another form")
def same_law(s):
    icon = flat_icon(-4.2, 0.8)
    st = lab("stationary action", 26, PURPLE).next_to(icon, DOWN, buff=0.25)
    yield [FadeIn(icon), FadeIn(st), FadeIn(at(T("⇔", 54, INK), 0, 0.8)), FadeIn(newton_eq(0.8, 50).shift(RIGHT * 4.2))]
    a = at(card("uses only T and V", 4.6, 0.9, TEAL, 28), -4.4, -1.9)
    b = at(card("works the same in any coordinates", 7.2, 0.9, BLUE, 28), 2.9, -1.9)
    yield [FadeIn(a), FadeIn(b)]


# ------------------------------------------------------------------ Euler-Lagrange
deck.part("From stationary action to an equation")


@slide("From stationary action to an equation.", "From paths to an equation")
def to_equation(s):
    ax1, ex1 = throw_axes(-3.8, -0.5, 6.0, 3.6, numbers=False)
    cands = candidates(ax1)
    marks = VGroup(*[T("?", 26, MUTED, True).move_to(ax1.c2p(x, y)) for x, y in ((0.5, 5.6), (1.0, 3.3), (1.5, 5.5), (1.62, 1.0))])
    yield [Create(ax1), FadeIn(ex1)]
    yield [LaggedStart(*[Create(c) for c in cands], lag_ratio=0.15), FadeIn(marks),
           FadeIn(lab("endless paths to compare", 24, INK).move_to([-3.8, 1.85, 0]))]
    ax2, ex2 = throw_axes(3.8, -0.5, 6.0, 3.6, numbers=False)
    real = throw_path(ax2)
    ticks = VGroup(*[Dot(ax2.c2p(t, height(t)), radius=0.08, color=TEAL) for t in np.linspace(0.15, 1.85, 8)])
    yield [Create(ax2), FadeIn(ex2), Create(real), LaggedStart(*[FadeIn(d, scale=1.5) for d in ticks], lag_ratio=0.12),
           FadeIn(lab("one equation, true at every moment", 24, INK).move_to([3.8, 1.85, 0]))]


@slide("Asking that the real path sit", "The Euler–Lagrange equation")
def el_name(s):
    ax, extra = throw_axes(-3.4, -0.4, 6.4, 3.9, numbers=False)
    real = throw_path(ax)
    bends = VGroup(*[ax.plot(lambda t, f=f: height(t) + 0.35 * f(t), x_range=[0, 2], color=ORANGE, stroke_width=3)
                     for f in (lambda t: np.sin(np.pi * t / 2), lambda t: np.sin(np.pi * t), lambda t: -np.sin(np.pi * t / 2))])
    yield [Create(ax), FadeIn(extra), Create(real), LaggedStart(*[Create(b) for b in bends], lag_ratio=0.25),
           FadeIn(lab("the real path sits at a flat spot of the action", 24, INK).move_to([-2.2, 2.4, 0]))]
    el = at(card("the Euler–Lagrange\nequation", 5.0, 1.6, PURPLE, 30), 4.2, -0.4)
    yield [GrowArrow(arrow([0.3, -0.4, 0], el)), FadeIn(el)]


APEX = np.array([0, -0.45, 0])


def seesaw():
    fulcrum = Polygon(APEX, APEX + [-0.55, -0.9, 0], APEX + [0.55, -0.9, 0], color=MUTED, fill_color=MUTED, fill_opacity=0.5, stroke_width=2)
    beam = Line(APEX + [-5.0, 0, 0], APEX + [5.0, 0, 0], color=INK, stroke_width=7)
    left = at(card("how fast the\nmomentum changes", 4.4, 1.4, BLUE, 28), -3.2, APEX[1] + 0.75)
    right = at(card("L's slope with position,\nthe force", 4.4, 1.4, ORANGE, 28), 3.2, APEX[1] + 0.75)
    return fulcrum, beam, left, right


@slide("The equation reads like a balance.", "The momentum: L's slope with velocity")
def balance0(s):
    fulcrum, beam, _, _ = seesaw()
    yield [FadeIn(fulcrum), Create(beam), FadeIn(lab("a balance", 24).next_to(fulcrum, DOWN, buff=0.15))]
    sl = at(card("slope of L with velocity", 6.4, 0.9, PURPLE, 30), 0, 2.0)
    yield [FadeIn(sl, shift=DOWN * 0.15),
           FadeIn(at(lab("how fast L changes when only the velocity changes", 24), 0, 1.2))]
    p = at(VGroup(T("ordinary motion:", 28, INK), eq("m v", 32, BLUE), T("= the momentum p", 28, BLUE, True)).arrange(RIGHT, buff=0.25), 0, -2.6)
    yield [FadeIn(p, shift=UP * 0.15)]


@slide("One side of the balance is how", "A balance")
def balance1(s):
    fulcrum, beam, left, right = seesaw()
    s.add(fulcrum, beam)
    tilt = 6 * DEGREES
    left.rotate(tilt, about_point=APEX)
    yield [FadeIn(left, shift=DOWN * 0.3), Rotate(beam, tilt, about_point=APEX)]
    _, _, left2, _ = seesaw()
    yield [FadeIn(right, shift=DOWN * 0.3), Rotate(beam, -tilt, about_point=APEX), Transform(left, left2)]
    yield [FadeIn(at(W("For an angle, it is a torque, the turning effect of a force.", 40, 26, ORANGE, align=ORIGIN), 3.2, -2.4))]


@slide("So momentum changes at a rate set", "A balance in any coordinate")
def balance2(s):
    fulcrum, beam, left, right = seesaw()
    s.add(fulcrum, beam, left, right)
    words = at(T("rate of change of momentum  =  force", 30, INK), 0, 2.2)
    yield [FadeIn(words)]
    h = at(chip("a height x", BLUE, size=28, h=0.8), -5.0, -2.5)
    a = at(chip("an angle θ", BLUE, size=28, h=0.8), -1.8, -2.5)
    yield [FadeIn(lab("the coordinate can be", 24).move_to([-3.4, -1.75, 0])), FadeIn(h), FadeIn(a)]
    yield [FadeIn(at(T("a generalized coordinate", 28, BLUE, True), 3.6, -2.0)), Indicate(h, color=BLUE), Indicate(a, color=BLUE)]
    yield [FadeIn(at(lab("several coordinates: one equation for each", 24, INK), 3.6, -2.75))]


@slide("Two checks show that it works.", "Check 1: the ball")
def check_ball(s):
    c1 = at(pill("check 1: a ball", INK, 26), -4.3, 2.2)
    c2 = at(pill("check 2: the pendulum", MUTED, 26), 0.2, 2.2)
    ground = Line([-6.6, -2.8, 0], [-3.8, -2.8, 0], color=LINE, stroke_width=3)
    ball = Dot([-5.2, 0.3, 0], radius=0.2, color=BLUE)
    g = Arrow([-5.2, 0.05, 0], [-5.2, -1.0, 0], buff=0, color=ORANGE, stroke_width=5, tip_length=0.2)
    yield [FadeIn(c1), FadeIn(c2), Create(ground), FadeIn(ball)]
    rows = VGroup(eq("L = ½ m v² − m g x", 32, PURPLE), eq("m a = − m g", 32, INK), eq("F = ma", 32, TEAL)).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
    rows.move_to([-2.4, 0.2, 0], aligned_edge=LEFT)
    yield [FadeIn(rows[0]), FadeIn(rows[1]), GrowArrow(g), FadeIn(rows[2]), FadeIn(check().next_to(rows[2], RIGHT, buff=0.3))]


@slide("And if you used kinetic plus potential", "Check 1: the ball")
def check_ball2(s):
    s.add(at(pill("check 1: a ball", INK, 26), -4.3, 2.2), at(pill("check 2: the pendulum", MUTED, 26), 0.2, 2.2),
          Line([-6.6, -2.8, 0], [-3.8, -2.8, 0], color=LINE, stroke_width=3))
    rows = VGroup(eq("L = ½ m v² − m g x", 32, PURPLE), eq("m a = − m g", 32, INK), eq("F = ma", 32, TEAL)).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
    rows.move_to([-2.4, 0.2, 0], aligned_edge=LEFT)
    s.add(rows, check().next_to(rows[2], RIGHT, buff=0.3))
    ball = VGroup(Dot([-5.2, -1.6, 0], radius=0.2, color=RED),
                  Arrow([-5.2, -1.35, 0], [-5.2, -0.3, 0], buff=0, color=RED, stroke_width=5, tip_length=0.2))
    wrong = eq("with T + V:  m a = + m g", 30, RED).move_to([-2.4, -2.2, 0], aligned_edge=LEFT)
    yield [FadeIn(ball), ball.animate.shift(UP * 1.8), FadeIn(wrong), FadeIn(lab("a ball that falls upward", 24, RED).next_to(wrong, DOWN, aligned_edge=LEFT, buff=0.2))]
    yield [Indicate(rows[0], color=PURPLE, scale_factor=1.08), FadeIn(lab("the minus sign again", 26, PURPLE).next_to(rows[0], RIGHT, buff=0.4))]


PIV3 = np.array([-4.4, 2.3, 0])
PL3 = 3.3
TH3 = 30 * DEGREES


def pend3(th=TH3):
    return VGroup(pend_static(PIV3, PL3, th), angle_mark(PIV3, PL3, th, "θ", r=1.0, size=30))


def pend_rows():
    rows = VGroup(eq("T = ½ m ℓ² θ̇²", 30, TEAL), eq("V = m g ℓ (1 − cos θ)", 30, TEAL)).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
    return rows.move_to([-1.3, 0.3, 0], aligned_edge=LEFT)


def ell_label():
    mid = (PIV3 + pend_pos(PIV3, PL3, TH3)) / 2
    return T("ℓ", 30, INK, True).move_to(mid + np.array([np.cos(TH3), np.sin(TH3), 0]) * 0.3)


def pend_key():
    return lab("ℓ: string length    θ̇: how fast θ changes", 24, MUTED).move_to([-1.3, -0.55, 0], aligned_edge=LEFT)


@slide("Second, the pendulum.", "Check 2: the pendulum")
def check_pend(s):
    yield [FadeIn(pend_static(PIV3, PL3, TH3)), Create(swing_arc(PIV3, PL3, 0.7)), FadeIn(ell_label())]
    yield [FadeIn(angle_mark(PIV3, PL3, TH3, "θ", r=1.0, size=30)), FadeIn(at(T("coordinate: the angle θ", 28, BLUE), 2.4, 1.6))]
    yield [FadeIn(pend_rows()), FadeIn(pend_key()), FadeIn(lab("the energies, written with θ", 24, INK).move_to([1.6, -1.5, 0]))]


@slide("Out comes the pendulum's equation of motion,", "No tension anywhere")
def no_tension(s):
    tr = ValueTracker(TH3)
    bar, string, bob = pend_live(PIV3, PL3, tr)
    s.add(swing_arc(PIV3, PL3, 0.7), bar, string, bob, at(T("coordinate: the angle θ", 28, BLUE), 2.4, 1.6), pend_rows(), pend_key())
    res = eq("m ℓ² θ̈ + m g ℓ sin θ = 0", 32, INK).move_to([-1.3, -1.4, 0], aligned_edge=LEFT)
    key = lab("θ̈: how fast θ̇ changes", 24, MUTED).next_to(res, DOWN, aligned_edge=LEFT, buff=0.2)
    nt = lab("no tension in it", 26, TEAL).next_to(key, DOWN, aligned_edge=LEFT, buff=0.2)
    yield [FadeIn(res), FadeIn(key), FadeIn(nt), FadeIn(check().next_to(nt, RIGHT, buff=0.2))]
    yield [tr.animate.set_value(-TH3), FadeIn(lab("the angle already keeps the weight on its circle", 24, BLUE).move_to([-1.3, -3.05, 0], aligned_edge=LEFT))]
    yield [Indicate(res, color=TEAL)]


@slide("For two, the trick fails, but this", "Two pendulums, still no tension")
def two_no_tension(s):
    piv, l1, l2, t1, t2 = D1
    g, b1, b2 = double_pend(piv, l1, l2, t1, t2)
    a1 = angle_mark(piv, l1, t1, "θ₁", r=0.9)
    a2 = angle_mark(b1, l2, t2, "θ₂", r=0.75)
    yield [FadeIn(g), FadeIn(a1), FadeIn(a2), FadeIn(trick_card(True))]
    rec = at(card("write T and V in θ₁ and θ₂,\napply the equation to each", 6.0, 1.6, PURPLE, 27), 3.9, -0.6)
    out = at(VGroup(T("no tension anywhere", 28, TEAL), check()).arrange(RIGHT, buff=0.25), 3.9, -2.1)
    yield [FadeIn(rec), FadeIn(out)]


def free_track():
    return Line([-6.8, -0.9, 0], [6.8, -0.9, 0], color=LINE, stroke_width=4)


def free_block(x):
    return Square(0.9, color=BLUE, fill_opacity=0.3, stroke_width=3).move_to([x, -0.43, 0])


@slide("There's a bonus.", "A missing coordinate")
def bonus(s):
    blk = free_block(-4.6)
    yield [Create(free_track()), FadeIn(blk), FadeIn(at(T("a bonus", 28, MUTED, True), -5.6, 2.2))]
    l = at(eq("L = ½ m v²", 36, PURPLE), -0.5, 1.6)
    yield [FadeIn(l), FadeIn(lab("no position x anywhere in L", 24, INK).next_to(l, RIGHT, buff=0.4))]
    ghost = free_block(-4.6).set_opacity(0.15)
    yield [FadeIn(ghost), blk.animate.shift(RIGHT * 4.0), FadeIn(at(T("sliding it changes nothing: a symmetry", 28, BLUE), 0, -2.0))]


@slide("So the force side of the balance", "Symmetry gives a conserved momentum")
def conserved(s):
    s.add(free_track(), at(eq("L = ½ m v²", 36, PURPLE), -0.5, 1.6))
    yield [FadeIn(at(VGroup(T("force side = 0, since", 28, ORANGE), T("L", 28, PURPLE, True), T("has no x", 28, ORANGE)).arrange(RIGHT, buff=0.15), 0, 0.95))]
    blk = free_block(-5.6)
    pv = always_redraw(lambda: VGroup(Arrow(blk.get_right() + UP * 0.9, blk.get_right() + UP * 0.9 + RIGHT * 1.2, buff=0, color=BLUE,
                                            stroke_width=5, tip_length=0.2), T("p", 26, BLUE, True).next_to(blk.get_top(), UP, buff=0.35)))
    yield [FadeIn(blk), FadeIn(pv), FadeIn(at(T("the matching momentum never changes", 28, INK), 0, -2.0))]
    yield [blk.animate.shift(RIGHT * 9.4), FadeIn(at(T("free body: p = m v stays constant", 28, BLUE), 0, -2.75))]
    yield [FadeIn(caption("symmetry → conserved quantity: comes back as Noether's theorem", y=-3.65, color=PURPLE, size=26))]


# ------------------------------------------------------------------ state
deck.part("A state as a point")


@slide("A state as a point.", "Two ways to describe motion")
def two_ways(s):
    ax, extra = throw_axes(-3.7, -0.4, 6.2, 3.8, numbers=False)
    real = throw_path(ax)
    ends = VGroup(Dot(ax.c2p(0, 0), radius=0.11, color=INK), Dot(ax.c2p(2, 0), radius=0.11, color=INK))
    yield [Create(ax), FadeIn(extra), Create(real), FadeIn(ends), FadeIn(lab("so far: whole paths, two fixed ends", 24, INK).move_to([-3.7, 2.15, 0]))]
    qm = at(card("quantum mechanics:\none instant,\ncarried forward", 5.4, 2.2, INK, 28), 3.9, -0.2)
    yield [FadeIn(qm, shift=LEFT * 0.2)]


@slide("It takes the state at one instant", "One instant, carried forward")
def instant(s):
    line = Arrow([-6.6, -1.0, 0], [6.6, -1.0, 0], buff=0, color=MUTED, stroke_width=4, tip_length=0.25)
    t0 = Line([-3.0, -1.25, 0], [-3.0, -0.75, 0], color=INK, stroke_width=4)
    snap = at(card("the state now", 3.4, 1.0, BLUE, 28), -3.0, 0.6)
    yield [GrowArrow(line), Create(t0), FadeIn(lab("time", 24).move_to([6.2, -1.45, 0])), FadeIn(snap), FadeIn(lab("one instant", 22).move_to([-3.0, -1.55, 0]))]
    later = at(card("the state later", 3.4, 1.0, BLUE, 28), 3.4, 0.6)
    yield [GrowArrow(arrow(snap, later)), FadeIn(later), FadeIn(lab("carried forward", 24).move_to([0.2, 1.3, 0]))]
    yield [FadeIn(at(T("What must we know at one instant?", 30, ORANGE, True), 0, -2.6))]


PA = np.array([-5.2, 2.3, 0])
PB = np.array([-1.6, 2.3, 0])
PLS = 2.8
THS = 15 * DEGREES


def pass_arrow(pivot, sign):
    b = pend_pos(pivot, PLS, THS)
    t = np.array([np.cos(THS), np.sin(THS), 0]) * sign
    return Arrow(b, b + t * 1.1, buff=0, color=BLUE, stroke_width=5, tip_length=0.2)


@slide("Position alone isn't enough.", "Same angle, opposite motion")
def same_angle(s):
    ta, tb = ValueTracker(-30 * DEGREES), ValueTracker(32 * DEGREES)
    pa, pb = pend_live(PA, PLS, ta), pend_live(PB, PLS, tb)
    yield [FadeIn(VGroup(*pa)), FadeIn(VGroup(*pb)), Create(swing_arc(PA, PLS, 0.65)), Create(swing_arc(PB, PLS, 0.65)),
           FadeIn(lab("first pass", 24).move_to([-5.2, -1.25, 0])), FadeIn(lab("second pass", 24).move_to([-1.6, -1.25, 0]))]
    yield [ta.animate.set_value(THS), tb.animate.set_value(THS)]
    yield [GrowArrow(pass_arrow(PA, 1)), GrowArrow(pass_arrow(PB, -1)),
           FadeIn(at(W("Same angle, moving opposite ways, so what happens next differs.", 26, 27, INK), 4.6, 0.6))]


def passes():
    return VGroup(pend_static(PA, PLS, THS), pend_static(PB, PLS, THS), swing_arc(PA, PLS, 0.65), swing_arc(PB, PLS, 0.65),
                  pass_arrow(PA, 1), pass_arrow(PB, -1), lab("first pass", 24).move_to([-5.2, -1.25, 0]),
                  lab("second pass", 24).move_to([-1.6, -1.25, 0]))


@slide("So we also need to know how", "Momentum, not velocity")
def momentum(s):
    s.add(passes())
    yield [FadeIn(at(T("also needed: how it is moving", 28, INK), 4.3, 1.9))]
    yield [FadeIn(at(card("the momentum p,\nnot the velocity", 5.0, 1.5, BLUE, 30), 4.3, 0.6))]
    yield [FadeIn(at(VGroup(eq("p", 30, BLUE), T("= L's slope with velocity", 28, INK)).arrange(RIGHT, buff=0.2), 4.3, -0.8))]


@slide("We call it the conjugate momentum.", "Momentum, not velocity")
def conjugate(s):
    s.add(passes(), at(T("also needed: how it is moving", 28, INK), 4.3, 1.9),
          at(card("the momentum p,\nnot the velocity", 5.0, 1.5, BLUE, 30), 4.3, 0.6),
          at(VGroup(eq("p", 30, BLUE), T("= L's slope with velocity", 28, INK)).arrange(RIGHT, buff=0.2), 4.3, -0.8))
    yield [FadeIn(at(T("the conjugate momentum", 30, BLUE, True), 4.3, -1.75))]
    yield [FadeIn(at(eq("on a line: p = m v", 30, BLUE), 4.3, -2.7))]


@slide("For a pendulum, it's an angular momentum.", "Why momentum")
def momentum2(s):
    icon = icon_pend(-5.6, 1.55)
    yield [FadeIn(icon), FadeIn(at(T("pendulum: an angular momentum", 28, BLUE), -1.2, 1.9))]
    h = at(chip("one function: the energy", PURPLE, size=30, h=0.85), 0, 0.55)
    a = at(card("how the position changes", 5.2, 1.0, BLUE, 30), -3.0, -1.0)
    b = at(card("how the momentum changes", 5.2, 1.0, BLUE, 30), 3.0, -1.0)
    yield [FadeIn(h), GrowArrow(arrow(h.get_bottom(), a.get_top())), GrowArrow(arrow(h.get_bottom(), b.get_top())), FadeIn(a), FadeIn(b),
           FadeIn(lab("both equations of motion", 26).move_to([0, -1.95, 0]))]
    yield [FadeIn(at(T("Momentum is also what stays constant when L lacks a coordinate.", 28, INK), 0, -3.1))]


PHASE = dict(x_range=[-2.4, 2.4, 1], y_range=[-2.7, 2.7, 1])


def phase_axes(cx, cy, w, h, q="q"):
    ax = Axes(**PHASE, x_length=w, y_length=h, tips=False, axis_config={"color": LINE, "include_ticks": False}).move_to([cx, cy, 0])
    labels = VGroup(lab(f"position {q}", 22).next_to(ax.x_axis, DOWN, buff=0.15).align_to(ax.x_axis, RIGHT),
                    lab("momentum p", 22).next_to(ax.y_axis, UP, buff=0.1))
    return ax, labels


def orbit(ax, t0=0.0, t1=PI, color=BLUE, width=4):
    return ParametricFunction(lambda t: ax.c2p(np.cos(2 * t), -2 * np.sin(2 * t)), t_range=[t0, t1], color=color, stroke_width=width)


@slide("A position together with a momentum is", "Phase space")
def phase(s):
    st = at(card("state = (position, momentum)", 6.4, 1.0, BLUE, 30), 0, 2.0)
    yield [FadeIn(st)]
    ax, labels = phase_axes(-0.5, -1.0, 6.0, 3.6)
    d = Dot(ax.c2p(0.6, 1.2), radius=0.12, color=BLUE)
    yield [Create(ax), FadeIn(labels), FadeIn(d), FadeIn(at(T("phase space", 30, BLUE, True), 4.9, -0.2)),
           FadeIn(lab("the space of all states", 24).move_to([4.9, -0.8, 0]))]


@slide("Each state is a point in it,", "States as points")
def states(s):
    ax, labels = phase_axes(-2.3, -0.4, 6.4, 5.0)
    s.add(ax, labels)
    path = orbit(ax)
    dot = Dot(ax.c2p(1, 0), radius=0.12, color=BLUE)
    yield [Create(path), MoveAlongPath(dot, path), FadeIn(at(T("the motion traces a curve", 28, INK), 4.4, 1.6))]
    B, D = Dot(ax.c2p(0, -2), radius=0.13, color=ORANGE), Dot(ax.c2p(0, 2), radius=0.13, color=ORANGE)
    yield [FadeIn(B), FadeIn(D), FadeIn(T("(0, −2)", 24, ORANGE).next_to(B, DR, buff=0.08)), FadeIn(T("(0, +2)", 24, ORANGE).next_to(D, UR, buff=0.08)),
           FadeIn(at(W("Same position, opposite momentum: two different points.", 26, 27, INK), 4.4, -0.6))]


# ------------------------------------------------------------------ Hamiltonian
deck.part("Energy moves the point")


@slide("Energy moves the point.", "Swap velocity for momentum")
def swap(s):
    ax, labels = phase_axes(-3.9, -0.4, 5.6, 4.6)
    d = Dot(ax.c2p(0.7, 1.4), radius=0.12, color=BLUE)
    q = T("?", 34, ORANGE, True).next_to(d, UR, buff=0.2)
    yield [Create(ax), FadeIn(labels), FadeIn(d)]
    yield [FadeIn(q), FadeIn(at(T("a rule that moves the state", 28, INK), 3.6, 2.0))]
    old = at(chip("(position, velocity)", MUTED, size=26, h=0.75), 3.6, 1.0)
    new = at(chip("(position, momentum)", BLUE, size=26, h=0.75), 3.6, -0.2)
    yield [FadeIn(old), Create(strike(old, MUTED)), GrowArrow(arrow(old, new)), FadeIn(new)]
    want = at(card("wanted: a function of q and p\nwhose slope with p is the velocity", 7.0, 1.4, PURPLE, 28), 3.6, -1.65)
    yield [FadeIn(want, shift=UP * 0.15)]
    yield [FadeIn(at(lab("it says how fast q changes: an equation of motion", 24, INK), 3.6, -2.75)), Indicate(q, color=ORANGE)]


def pv_term(y=1.9):
    return at(eq("p v", 56, INK), -4.6, y)


@slide("Momentum times velocity already changes with", "Building the function from p v")
def legendre_motive(s):
    pv = pv_term(1.75)
    good = at(VGroup(T("nudge p:", 28, INK), eq("p v changes at rate v", 30, TEAL)).arrange(RIGHT, buff=0.3), 2.0, 2.3)
    bad = at(VGroup(T("nudge v:", 28, INK), eq("p v changes too", 30, ORANGE)).arrange(RIGHT, buff=0.3), 2.0, 1.2)
    yield [FadeIn(pv), GrowArrow(arrow(pv.get_right(), good.get_left())), FadeIn(good), FadeIn(check().next_to(good, RIGHT, buff=0.2))]
    yield [GrowArrow(arrow(pv.get_right(), bad.get_left())), FadeIn(bad), FadeIn(lab("remove this part", 24, ORANGE).next_to(bad, DOWN, buff=0.15))]
    h = at(eq("p v − L", 56, PURPLE), 0, -1.4)
    yield [FadeIn(h, shift=UP * 0.2), FadeIn(lab("take p v, and subtract the Lagrangian", 26, INK).next_to(h, DOWN, buff=0.3))]


def nudge_rows():
    rows = VGroup(
        VGroup(eq("p v", 32, INK), eq("grows by  p × nudge", 32, INK)),
        VGroup(eq("L", 32, PURPLE), eq("grows by  p × nudge", 32, INK)),
        VGroup(eq("p v − L", 32, PURPLE), eq("grows by  0", 32, TEAL)),
    )
    for k, r in enumerate(rows):
        y = (1.0, -0.05, -1.55)[k]
        r[0].move_to([-3.6, y, 0], aligned_edge=RIGHT)
        r[1].move_to([-3.0, y, 0], aligned_edge=LEFT)
    return rows


@slide("Nudge only the velocity.", "Nudge the velocity")
def nudge_v(s):
    yield [FadeIn(at(VGroup(T("nudge only v,", 30, ORANGE, True), T("keep q and p fixed", 28, MUTED)).arrange(RIGHT, buff=0.3), 0, 2.2))]
    rows = nudge_rows()
    yield [FadeIn(rows[0])]
    yield [FadeIn(rows[1]), FadeIn(lab("because p is L's slope with velocity", 24, MUTED).next_to(rows[1], DOWN, buff=0.1).align_to(rows[1][1], LEFT))]
    line = Line([-6.0, -0.95, 0], [4.6, -0.95, 0], color=LINE, stroke_width=3)
    yield [Create(line), FadeIn(rows[2]), FadeIn(at(T("no response to the velocity at all", 28, TEAL, True), 0, -2.6))]


@slide("Nudge the momentum, and the result changes", "The Legendre transform")
def legendre(s):
    e = at(eq("p v − L", 52, PURPLE), -3.0, 1.7)
    out = at(VGroup(T("nudge p:", 28, INK), eq("changes at rate v", 30, TEAL)).arrange(RIGHT, buff=0.3), 3.3, 1.7)
    yield [FadeIn(e), GrowArrow(arrow(e, out)), FadeIn(out), FadeIn(check().next_to(out, RIGHT, buff=0.2))]
    v = at(chip("velocity v", MUTED, size=30, h=0.9), -3.2, -0.4)
    gone = Line(v.get_left() + RIGHT * 0.1, v.get_right() + LEFT * 0.1, color=RED, stroke_width=5)
    qp = at(chip("a function of q and p", BLUE, size=30, h=0.9), 2.4, -0.4)
    yield [FadeIn(v), v.animate.set_opacity(0.45), Create(gone), FadeIn(lab("velocity swapped out", 24).next_to(v, DOWN, buff=0.2)),
           GrowArrow(arrow(v, qp)), FadeIn(qp),
           FadeIn(at(T("a Legendre transform", 34, PURPLE, True), 0, -2.6))]


@slide("Let's try it on a spring.", "For the spring: the total energy")
def spring_h(s):
    r0 = VGroup(eq("p v", 32), eq("=", 32), eq("m v²", 32), eq("=", 32), eq("2 × ½ m v²", 32, TEAL)).arrange(RIGHT, buff=0.25)
    r1 = VGroup(Text("p v − L", font=MONO, color=INK, font_size=32, t2c={"L": PURPLE}), eq("=", 32),
                eq("m v² − (½ m v² − ½ k x²)", 32)).arrange(RIGHT, buff=0.25)
    r2 = VGroup(eq("=", 32), eq("½ m v²", 32, TEAL), eq("+", 32), eq("½ k x²", 32, TEAL)).arrange(RIGHT, buff=0.25)
    at(r1, 0.9, 0.6)
    r0.shift(r1[1].get_center() - r0[1].get_center() + UP * 1.2)
    r2.next_to(r1, DOWN, buff=0.5)
    r2.shift(RIGHT * (r1[1].get_x() - r2[0].get_x()))
    xt = ValueTracker(0.5)
    base, spr, block = spring_rig(xt, wall=-7.0, rest=-5.9, y=-2.4, sc=0.6, size=0.5, floor_to=-4.6)
    yield [FadeIn(base), FadeIn(spr), FadeIn(block), FadeIn(r0), FadeIn(lab("twice the kinetic energy", 24, TEAL).next_to(r0[4], UP, buff=0.15))]
    br_k = Brace(r2[1], DOWN, color=TEAL)
    br_v = Brace(r2[3], DOWN, color=TEAL)
    yield [FadeIn(r1), FadeIn(r2), FadeIn(br_k), FadeIn(br_v), FadeIn(lab("kinetic", 24, TEAL).next_to(br_k, DOWN, buff=0.1)),
           FadeIn(lab("potential", 24, TEAL).next_to(br_v, DOWN, buff=0.1))]
    yield [FadeIn(at(T("T + V: the total energy", 32, TEAL, True), 1.6, -2.9))]


@slide("Written with momentum, it's the momentum squared", "For the spring: the total energy")
def hamiltonian(s):
    sub = at(VGroup(eq("v = p / m", 34, BLUE), T("turns ½ m v² into", 28, INK), eq("p² / 2m", 34, TEAL)).arrange(RIGHT, buff=0.3), 0, 1.6)
    yield [FadeIn(sub)]
    h = at(eq("p²/2m + V", 60, PURPLE), 0, -0.4)
    yield [FadeIn(h, shift=UP * 0.2), FadeIn(lab("the total energy, written with position and momentum", 26).next_to(h, DOWN, buff=0.35))]


@slide("In general, momentum times velocity minus", "The Hamiltonian")
def ham_general(s):
    h = at(eq("H = p v − L", 56, PURPLE), 0, 1.9)
    yield [FadeIn(h), FadeIn(lab("written with q and p: the Hamiltonian", 26, PURPLE).next_to(h, DOWN, buff=0.25))]
    box = at(card(None, 9.6, 2.1, TEAL), 0, -0.55)
    l1 = at(T("H is the total energy T + V when", 28, TEAL, True), 0, 0.1)
    l2 = at(T("T is a constant × (rate of change of q)²", 28, INK), 0, -0.55)
    l3 = at(T("and V does not involve velocity", 28, INK), 0, -1.2)
    yield [FadeIn(box), FadeIn(l1), FadeIn(l2)]
    yield [FadeIn(l3)]
    nx = at(chip("the next chapter starts here", INK, size=28, h=0.8), 0, -2.6)
    yield [FadeIn(nx), Indicate(h, color=PURPLE)]


def ham_state(ax):
    t = -PI / 8
    return ax.c2p(np.cos(2 * t), -2 * np.sin(2 * t)), np.cos(2 * t), -2 * np.sin(2 * t)


def ham_rows():
    r1 = VGroup(eq("rate of q", 28, BLUE), eq("=", 28), eq("slope of H with p", 28, PURPLE)).arrange(RIGHT, buff=0.2)
    r2 = VGroup(eq("rate of p", 28, ORANGE), eq("=", 28), eq("− slope of H with q", 28, PURPLE)).arrange(RIGHT, buff=0.2)
    return r1, r2


@slide("The Hamiltonian moves the state through two", "Hamilton's equations")
def hams(s):
    ax, labels = phase_axes(-3.9, -0.4, 5.6, 4.8)
    p0, x, p = ham_state(ax)
    d = Dot(p0, radius=0.12, color=BLUE)
    hc = at(T("Hamilton's equations", 30, PURPLE, True), 3.5, 1.9)
    yield [Create(ax), FadeIn(labels), FadeIn(d), FadeIn(hc)]
    k = 0.8
    hx = ax.c2p(x + k * p / 2.0, p) - p0
    hp = ax.c2p(x, p - k * 4 * x / 2.0) - p0
    r1, r2 = ham_rows()
    at(r1, 3.5, 0.7)
    at(r2, 3.5, -0.5)
    ar1 = Arrow(p0, p0 + hx, buff=0, color=BLUE, stroke_width=4, tip_length=0.18)
    yield [GrowArrow(ar1), FadeIn(r1)]
    ar2 = Arrow(p0, p0 + hp, buff=0, color=ORANGE, stroke_width=4, tip_length=0.18)
    res = Arrow(p0, p0 + hx + hp, buff=0, color=INK, stroke_width=6, tip_length=0.22)
    yield [GrowArrow(ar2), FadeIn(r2), GrowArrow(res), FadeIn(lab("the point's next step", 22, INK).next_to(d, UP, buff=0.2))]


@slide("The first holds because we built the", "Where the two equations come from")
def ham_origins(s):
    r1, r2 = ham_rows()
    at(r1, -1.8, 1.4)
    at(r2, -1.8, -0.6)
    s.add(r1, r2)
    w1 = at(card("built that way:\nthe Legendre transform", 4.4, 1.3, PURPLE, 26), 4.9, 1.4)
    yield [GrowArrow(arrow(r1, w1)), FadeIn(w1)]
    w2 = at(card("the Euler–Lagrange\nbalance", 4.4, 1.3, ORANGE, 26), 4.9, -0.6)
    yield [GrowArrow(arrow(r2, w2)), FadeIn(w2)]


@slide("Both say how fast things change,", "The point is the complete state")
def steps(s):
    ax, labels = phase_axes(-3.9, -0.4, 5.6, 4.8)
    s.add(ax, labels)
    t0 = -PI / 8
    ts = [t0 + k * PI / 12 for k in range(4)]
    pts_ = [ax.c2p(np.cos(2 * t), -2 * np.sin(2 * t)) for t in ts]
    d = Dot(pts_[0], radius=0.12, color=BLUE)
    s.add(d)
    hops = [Arrow(a, b, buff=0.05, color=BLUE, stroke_width=4, tip_length=0.16) for a, b in zip(pts_, pts_[1:])]
    yield [LaggedStart(*[GrowArrow(h) for h in hops], lag_ratio=0.6), d.animate.move_to(pts_[-1]),
           FadeIn(at(W("rates of change, not rates of rates: (q, p) now fixes the next small step", 28, 26, INK), 3.6, 1.6))]
    rest = orbit(ax, ts[-1], ts[0] + PI)
    yield [Create(rest), MoveAlongPath(d, rest), FadeIn(at(T("and with it the whole motion", 26, INK), 3.6, 0.2))]
    yield [FadeIn(at(T("the point is the complete state", 28, BLUE, True), 3.6, -0.8))]
    yield [FadeIn(at(W("Together: the same as the one Euler–Lagrange equation", 28, 26, PURPLE), 3.6, -2.3))]


SPR = dict(wall=-6.4, rest=-1.6, y=0.9, sc=1.6, size=0.8, floor_to=1.4)


def spring_fixed():
    return VGroup(DashedLine([-1.6, 0.3, 0], [-1.6, 1.8, 0], color=LINE, stroke_width=2), lab("rest", 22).move_to([-1.6, 0.0, 0]),
                  at(chip("mass 1 kg", BLUE, size=26, h=0.7), 4.6, 1.6), at(chip("stiffness k = 4", MUTED, size=26, h=0.7), 4.6, 0.7))


@slide("Let's follow a spring.", "A mass on a spring")
def spring_setup(s):
    xt = ValueTracker(0.0)
    base, spr, block = spring_rig(xt, **SPR)
    fixed = spring_fixed()
    yield [FadeIn(base), FadeIn(spr), FadeIn(block), FadeIn(fixed[0]), FadeIn(fixed[1])]
    yield [FadeIn(fixed[2]), FadeIn(fixed[3])]
    yield [xt.animate.set_value(1.0), FadeIn(at(T("pull out 1 m, let go", 28, ORANGE), -1.6, -1.2))]


def spring_eqs():
    rows = VGroup(eq("rate of x = p", 30, BLUE), eq("rate of p = − 4 x", 30, ORANGE)).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
    return at(rows, -3.2, -1.6)


@slide("Hamilton's equations say the position changes", "A mass on a spring")
def spring_move(s):
    tt = ValueTracker(0.0)
    xt = ValueTracker(1.0)
    xt.add_updater(lambda m: m.set_value(np.cos(2 * tt.get_value())))
    base, spr, block = spring_rig(xt, **SPR)
    s.add(xt, base, spr, block, spring_fixed())
    rows = spring_eqs()
    yield [FadeIn(rows[0])]
    yield [FadeIn(rows[1])]
    sol = at(eq("x = cos 2t", 34, BLUE), 3.6, -1.35)
    yield [tt.animate(rate_func=linear).set_value(PI), FadeIn(sol),
           FadeIn(at(T("it repeats every π seconds", 28, INK, True), 3.6, -2.1))]


@slide("That two is the angular frequency,", "The angular frequency")
def omega(s):
    s.add(*spring_rig(ValueTracker(1.0), **SPR), spring_fixed(), spring_eqs())
    sol = at(eq("x = cos 2t", 34, BLUE), 3.6, -1.35)
    s.add(sol)
    w = at(eq("2 = ω = √(k / m) = √(4 / 1)", 30, PURPLE), 3.6, -2.75)
    yield [Indicate(sol, color=PURPLE), FadeIn(w), FadeIn(at(lab("the angular frequency", 24, PURPLE), 3.6, -2.05))]
    yield [FadeIn(at(lab("used throughout the harmonic oscillator chapter", 24, INK), 3.6, -3.45))]


MOMENTS = [("A", 0.0, "(1, 0)", "stretched, at rest"), ("B", PI / 4, "(0, −2)", "middle, moving left"),
           ("C", PI / 2, "(−1, 0)", "squeezed, at rest"), ("D", 3 * PI / 4, "(0, 2)", "middle, moving right")]
SW = dict(wall=-7.0, rest=-3.7, y=1.7, sc=1.4, size=0.7, floor_to=-1.4)


def swing_parts(tt):
    xt = ValueTracker(np.cos(2 * tt.get_value()))
    xt.add_updater(lambda m: m.set_value(np.cos(2 * tt.get_value())))
    base, spr, block = spring_rig(xt, **SW)
    rest = DashedLine([-3.7, 1.15, 0], [-3.7, 2.4, 0], color=LINE, stroke_width=2)
    ax, labels = phase_axes(3.9, -0.4, 5.2, 4.8, q="x")
    ell = orbit(ax, 0, PI, LINE, 3)
    trace = always_redraw(lambda: orbit(ax, 0, max(tt.get_value(), 1e-3), BLUE, 5))
    dot = always_redraw(lambda: Dot(ax.c2p(np.cos(2 * tt.get_value()), -2 * np.sin(2 * tt.get_value())), radius=0.13, color=BLUE))
    tags = VGroup()
    for name, t, _, _ in MOMENTS:
        x, p = np.cos(2 * t), -2 * np.sin(2 * t)
        side = UR if x > 0.5 else UL if x < -0.5 else (DR if p < 0 else UR)
        tags.add(T(name, 24, BLUE, True).next_to(ax.c2p(x, p), side, buff=0.15))
    return xt, VGroup(base, rest), spr, block, ax, labels, ell, trace, dot, tags


def moment_row(k, energy=False):
    name, _, st, words = MOMENTS[k]
    y = 0.4 - 0.85 * k
    row = VGroup(pill(name, BLUE, 24).move_to([-6.7, y, 0]), chip(st, BLUE, size=24, h=0.6).move_to([-5.3, y, 0]),
                 T(words, 24, INK).move_to([-4.3, y, 0], aligned_edge=LEFT))
    if energy:
        row.add(T("2 J", 24, TEAL, True).move_to([-0.7, y, 0]))
    return row


def energy_a():
    return eq("A: all potential, ½ × 4 × 1² = 2 J", 26, TEAL).move_to([-6.9, -2.95, 0], aligned_edge=LEFT)


def motion_hint(ax, x, p, d, text, side, at_end=False):
    start = ax.c2p(x, p)
    arr = Arrow(start, start + d, buff=0.18, color=ORANGE, stroke_width=5, tip_length=0.18)
    label = lab(text, 22, ORANGE)
    label.next_to(arr.get_end() if at_end else arr, side, buff=0.1)
    return VGroup(arr, label)


@slide("Follow it through one swing.", "One swing, four moments")
def swing1(s):
    tt = ValueTracker(0.0)
    xt, fixed, spr, block, ax, labels, ell, trace, dot, tags = swing_parts(tt)
    s.add(xt)
    yield [FadeIn(fixed), FadeIn(spr), FadeIn(block), Create(ax), FadeIn(labels), Create(ell)]
    yield [FadeIn(dot), FadeIn(trace), FadeIn(tags[0]), FadeIn(moment_row(0))]
    yield [FadeIn(energy_a())]
    yield [FadeIn(motion_hint(ax, 1, 0, DOWN * 1.1, "p starts to fall", DR, at_end=True))]


@slide("A quarter swing later, it passes", "One swing, four moments")
def swing1b(s):
    tt = ValueTracker(0.0)
    xt, fixed, spr, block, ax, labels, ell, trace, dot, tags = swing_parts(tt)
    s.add(xt, fixed, spr, block, ax, labels, ell, trace, dot, tags[0], moment_row(0), energy_a())
    yield [tt.animate(rate_func=linear).set_value(PI / 4), FadeIn(tags[1]), FadeIn(moment_row(1))]
    yield [FadeIn(motion_hint(ax, 0, -2, LEFT * 1.0, "x changes fastest", LEFT))]


@slide("Half a swing in, it's squeezed and", "One swing, four moments")
def swing2(s):
    tt = ValueTracker(PI / 4)
    xt, fixed, spr, block, ax, labels, ell, trace, dot, tags = swing_parts(tt)
    s.add(xt, fixed, spr, block, ax, labels, ell, trace, dot, tags[0], tags[1], moment_row(0), moment_row(1), energy_a())
    yield [tt.animate(rate_func=linear).set_value(PI / 2), FadeIn(tags[2]), FadeIn(moment_row(2))]
    yield [tt.animate(rate_func=linear).set_value(3 * PI / 4), FadeIn(tags[3]), FadeIn(moment_row(3))]
    yield [FadeIn(VGroup(*[moment_row(k, True)[3] for k in range(4)])), FadeIn(T("energy", 22, TEAL).move_to([-0.7, 1.05, 0]))]


@slide("In phase space, the point goes round", "A closed loop of equal energy")
def loop(s):
    tt = ValueTracker(3 * PI / 4)
    xt, fixed, spr, block, ax, labels, ell, trace, dot, tags = swing_parts(tt)
    s.add(xt, fixed, spr, block, ax, labels, ell, trace, dot, tags, *[moment_row(k, True) for k in range(4)],
          T("energy", 22, TEAL).move_to([-0.7, 1.05, 0]))
    yield [tt.animate(rate_func=linear).set_value(PI), FadeIn(T("an ellipse", 26, BLUE).next_to(ax.c2p(1.1, 1.6), UR, buff=0.05))]
    full = orbit(ax, 0, PI, TEAL, 8).set_stroke(opacity=0.5)
    yield [Create(full), FadeIn(at(T("every point on it: 2 J", 26, TEAL, True), 3.9, -3.55))]


def energy_bars(tt):
    xs, w = -6.6, 4.4

    def bar(fn, y):
        return always_redraw(lambda: Rectangle(width=max(w * fn(tt.get_value()) / 2, 0.001), height=0.45, stroke_width=0,
                                               fill_color=TEAL, fill_opacity=1 if y > -1.4 else 0.5)
                             .move_to([xs + max(w * fn(tt.get_value()) / 2, 0.001) / 2, y, 0]))

    kin = bar(lambda t: 2 * np.sin(2 * t) ** 2, -0.8)
    pot = bar(lambda t: 2 * np.cos(2 * t) ** 2, -1.9)
    frames = VGroup(*[Rectangle(width=w, height=0.45, stroke_color=LINE, stroke_width=2).move_to([xs + w / 2, y, 0]) for y in (-0.8, -1.9)])
    names = VGroup(lab("kinetic", 24, TEAL).move_to([xs, -0.3, 0], aligned_edge=LEFT),
                   lab("potential", 24, TEAL).move_to([xs, -1.4, 0], aligned_edge=LEFT))
    total = T("total: always 2 J", 26, TEAL, True).move_to([xs, -2.6, 0], aligned_edge=LEFT)
    return kin, pot, frames, names, total


@slide("As it goes round, the energy passes", "Kinetic and potential trade places")
def trade(s):
    tt = ValueTracker(0.0)
    xt, fixed, spr, block, ax, labels, ell, trace, dot, tags = swing_parts(tt)
    full = orbit(ax, 0, PI, BLUE, 4)
    s.add(xt, fixed, spr, block, ax, labels, full, dot, tags)
    kin, pot, frames, names, total = energy_bars(tt)
    yield [FadeIn(frames), FadeIn(names), FadeIn(kin), FadeIn(pot), FadeIn(total)]
    yield [tt.animate(rate_func=linear).set_value(PI / 4)]
    yield [tt.animate(rate_func=linear).set_value(PI / 2), FadeIn(lab("at the turning points: all potential", 24, INK).move_to([-6.6, -3.25, 0], aligned_edge=LEFT))]
    yield [tt.animate(rate_func=linear).set_value(3 * PI / 4), FadeIn(lab("in the middle: all kinetic", 24, INK).move_to([-6.6, -3.8, 0], aligned_edge=LEFT))]


# ------------------------------------------------------------------ Poisson bracket
deck.part("How any quantity changes")


@slide("How any quantity changes.", "Rates of other quantities")
def other_rates(s):
    a = at(chip("rate of q", BLUE, size=28, h=0.8), -4.2, 1.2)
    b = at(chip("rate of p", BLUE, size=28, h=0.8), -4.2, -0.1)
    yield [FadeIn(a), FadeIn(b), FadeIn(check().next_to(a, RIGHT, buff=0.25)), FadeIn(check().next_to(b, RIGHT, buff=0.25)),
           FadeIn(lab("from Hamilton's equations", 24).move_to([-4.2, 2.1, 0]))]
    c = at(chip("rate of the energy?", ORANGE, size=28, h=0.8), 3.4, 1.2)
    d = at(chip("rate of anything else?", ORANGE, size=28, h=0.8), 3.4, -0.1)
    yield [FadeIn(c), FadeIn(d)]
    yield [FadeIn(at(T("without solving for the whole motion first", 28, INK, True), 0, -1.9))]


@slide("Take any quantity that depends on the", "Two ways a quantity changes")
def two_changes(s):
    ax, labels = phase_axes(-3.9, -0.4, 5.6, 4.6)
    p0 = ax.c2p(-0.6, 1.5)
    p1 = ax.c2p(0.6, 0.5)
    d = Dot(p0, radius=0.12, color=BLUE)
    f = at(eq("f(q, p)", 40, ORANGE), 3.6, 1.9)
    yield [Create(ax), FadeIn(labels), FadeIn(d), FadeIn(f), FadeIn(lab("any quantity that depends on the state", 24).move_to([3.6, 1.15, 0]))]
    hq = Arrow(p0, [p1[0], p0[1], 0], buff=0, color=BLUE, stroke_width=4, tip_length=0.18)
    hp = Arrow([p1[0], p0[1], 0], p1, buff=0, color=ORANGE, stroke_width=4, tip_length=0.18)
    yield [GrowArrow(hq), GrowArrow(hp), d.animate.move_to(p1),
           FadeIn(at(VGroup(eq("change through q", 28, BLUE), eq("+ change through p", 28, ORANGE)).arrange(DOWN, buff=0.2, aligned_edge=LEFT), 3.6, -0.1))]
    yield [FadeIn(at(W("a slope: how fast a quantity changes when only q, or only p, changes", 34, 26, INK), 3.6, -2.2))]


def chain_terms():
    head = eq("rate of f  =", 30, INK)
    t1 = VGroup(eq("(slope of f with q)", 28, INK), eq("×", 28), eq("(rate of q)", 28, BLUE)).arrange(RIGHT, buff=0.2)
    t2 = VGroup(eq("+ (slope of f with p)", 28, INK), eq("×", 28), eq("(rate of p)", 28, ORANGE)).arrange(RIGHT, buff=0.2)
    head.move_to([-6.9, 1.9, 0], aligned_edge=LEFT)
    t1.move_to([-5.6, 1.1, 0], aligned_edge=LEFT)
    t2.move_to([-6.0, 0.3, 0], aligned_edge=LEFT)
    t2.shift(RIGHT * (t1[1].get_x() - t2[1].get_x()))
    return head, t1, t2


@slide("Each change is a slope times how", "Building the combination")
def combination(s):
    head, t1, t2 = chain_terms()
    yield [FadeIn(head), FadeIn(t1), FadeIn(t2)]
    n1 = eq("(slope of H with p)", 28, PURPLE).move_to(t1[2], aligned_edge=LEFT)
    n2 = eq("(slope of H with q)", 28, PURPLE).move_to(t2[2], aligned_edge=LEFT)
    plus = t2[0]
    minus = eq("− (slope of f with p)", 28, INK).move_to(plus, aligned_edge=LEFT)
    note = at(lab("Hamilton's equations swap the rates for H's slopes", 24, PURPLE), 0, -0.6)
    yield [Transform(t1[2], n1), Transform(t2[2], n2), Transform(plus, minus), FadeIn(note)]
    line = Line([-6.9, -1.25, 0], [6.9, -1.25, 0], color=LINE, stroke_width=3)
    yield [Create(line), FadeIn(at(T("one fixed combination of slopes", 30, INK, True), 0, -1.85))]
    name = at(VGroup(eq("{f, H}", 44, PURPLE), T("its name: the Poisson bracket", 32, PURPLE, True)).arrange(RIGHT, buff=0.5), 0, -2.95)
    yield [FadeIn(name, shift=UP * 0.15)]


SLOPES = ["slope of f with q", "slope of f with p", "slope of g with q", "slope of g with p"]


@slide("Here is the combination.", "What the bracket is")
def bracket_formula(s):
    cells = VGroup(*[card(t, 3.4, 0.8, ORANGE if t[9] == "f" else PURPLE, 24) for t in SLOPES]).arrange(RIGHT, buff=0.2)
    at(cells, 0, 2.0)
    yield [FadeIn(lab("two quantities f and g, four slopes", 24).move_to([0, 1.3, 0])),
           LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in cells], lag_ratio=0.2)]
    one = at(VGroup(eq("(slope of f with q)", 30, ORANGE), eq("×", 30, INK), eq("(slope of g with p)", 30, PURPLE)).arrange(RIGHT, buff=0.25), 0.3, 0.4)
    yield [FadeIn(one), Indicate(cells[0], color=ORANGE), Indicate(cells[3], color=PURPLE)]
    minus = at(eq("−", 40, INK), -6.2, -0.6)
    two = at(VGroup(eq("(slope of f with p)", 30, ORANGE), eq("×", 30, INK), eq("(slope of g with q)", 30, PURPLE)).arrange(RIGHT, buff=0.25), 0.3, -0.6)
    yield [FadeIn(minus), FadeIn(two), Indicate(cells[1], color=ORANGE), Indicate(cells[2], color=PURPLE)]
    brace = Line([-6.4, -1.3, 0], [6.6, -1.3, 0], color=PURPLE, stroke_width=4)
    name = at(VGroup(eq("=  {f, g}", 44, PURPLE), T("the Poisson bracket", 30, PURPLE, True)).arrange(RIGHT, buff=0.4), 0, -2.2)
    yield [Create(brace), FadeIn(name)]


@slide("When the second quantity is the Hamiltonian", "What the bracket is")
def bracket_energy(s):
    e = at(eq("g = H", 44, PURPLE), 0, 1.4)
    yield [FadeIn(e)]
    r = at(eq("{f, H}  =  rate of change of f", 40, INK), 0, -0.2)
    yield [FadeIn(r, shift=UP * 0.2)]
    yield [Indicate(r, color=PURPLE), FadeIn(at(lab("true for any quantity that depends on the state", 26), 0, -1.5))]


MX = -1.4


def machine(y=0.4):
    box = at(card(None, 3.6, 1.6, PURPLE), MX, y)
    return VGroup(box, at(eq("{ · , H}", 40, PURPLE), MX, y))


@slide("A few examples show how it works.", "Bracket with the energy")
def examples(s):
    m = machine()
    yield [FadeIn(m), FadeIn(lab("feed a quantity in, get its rate of change out", 24).move_to([MX, 1.7, 0]))]
    for k, (inp, out, note, y) in enumerate((("q", "rate of q", ("Hamilton's first", "spring (q is x): p"), -1.2),
                                             ("p", "rate of p", ("Hamilton's second", "spring (q is x): − 4 x"), -2.6))):
        i = at(chip(inp, BLUE, size=32, h=0.8), -5.8, y)
        o = at(chip(out, BLUE, size=28, h=0.8), 2.4, y)
        ex = VGroup(*[lab(t, 24, INK) for t in note]).arrange(DOWN, buff=0.08, aligned_edge=LEFT).next_to(o, RIGHT, buff=0.3)
        yield [FadeIn(i), GrowArrow(Arrow(i.get_right(), m.get_left() + DOWN * 0.3 * (k + 1), buff=0.1, color=MUTED, stroke_width=4, tip_length=0.18)),
               GrowArrow(Arrow(m.get_right() + DOWN * 0.3 * (k + 1), o.get_left(), buff=0.1, color=MUTED, stroke_width=4, tip_length=0.18)),
               FadeIn(o), FadeIn(ex)]


@slide("And the bracket of the Hamiltonian with", "Bracket with the energy")
def hh(s):
    m = machine()
    s.add(m)
    i = at(chip("H", PURPLE, size=34, h=0.9), -5.8, -1.4)
    o = at(chip("0", TEAL, size=34, h=0.9), 2.4, -1.4)
    yield [FadeIn(i), GrowArrow(Arrow(i.get_right(), m.get_left() + DOWN * 0.4, buff=0.1, color=MUTED, stroke_width=4, tip_length=0.18)),
           GrowArrow(Arrow(m.get_right() + DOWN * 0.4, o.get_left(), buff=0.1, color=MUTED, stroke_width=4, tip_length=0.18)), FadeIn(o)]
    terms = VGroup(eq("{H, H} = A × B − B × A = 0", 30, PURPLE),
                   lab("A: slope of H with q,  B: slope of H with p", 22)).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
    terms.move_to([-6.9, 2.05, 0], aligned_edge=LEFT)
    yield [FadeIn(terms), FadeIn(lab("the same product, opposite signs", 26, INK).move_to([1.5, 2.25, 0], aligned_edge=LEFT))]
    yield [FadeIn(at(T("the energy never changes", 30, TEAL, True), 2.4, -2.3)), Indicate(o, color=TEAL)]
    yield [FadeIn(at(eq("in general: f stays constant exactly when {f, H} = 0", 28, INK), 0, -3.3))]


@slide("One bracket is special.", "{q, p} = 1")
def special(s):
    e = at(eq("{q, p} = 1", 64, PURPLE), 0, 1.7)
    yield [FadeIn(e)]
    work = at(VGroup(eq("= (slope of q with q)(slope of p with p) − (cross slopes)", 24, INK),
                     eq("= 1 × 1 − 0 × 0 = 1", 28, INK)).arrange(DOWN, buff=0.2), 0, 0.45)
    yield [FadeIn(work)]
    xs = (-4.6, 0, 4.6)
    icons = [icon_ball(xs[0], -1.9), icon_spring(xs[1], -1.9), icon_pend(xs[2], -2.1)]
    ones = [at(T("= 1", 30, TEAL, True), x + 1.5, -1.9) for x in xs]
    yield [*[FadeIn(i) for i in icons], *[FadeIn(o) for o in ones],
           FadeIn(at(T("no H in it, so the same for every system", 28, INK), 0, -3.45))]


@slide("That isn't true for velocity.", "Velocity does not do this")
def velocity(s):
    good = at(eq("{q, p} = 1", 44, PURPLE), -3.9, 1.6)
    bad = at(eq("{q, v} = 1 / m", 44, MUTED), 3.4, 1.6)
    s.add(good)
    yield [FadeIn(bad), FadeIn(at(eq("v = p / m", 28, MUTED), 3.4, 0.75))]
    rows = VGroup(eq("on a line: 1 / m", 28, MUTED), eq("pendulum:  1 / (m ℓ²)", 28, MUTED)).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
    at(rows, 3.4, -0.5)
    yield [FadeIn(rows), FadeIn(at(T("changes from system to system", 26, INK), 3.4, -1.8))]
    yield [FadeIn(check().next_to(good, RIGHT, buff=0.3)), FadeIn(at(T("another reason to use momentum", 28, TEAL, True), -3.9, -0.1))]


@slide("The bracket obeys a product rule,", "A product rule")
def product_rule(s):
    rule = at(eq("{f g, h} = f {g, h} + g {f, h}", 38, PURPLE), 0, 1.8)
    yield [FadeIn(rule), FadeIn(at(lab("like the product rule for ordinary slopes", 24), 0, 1.05))]
    ex = at(eq("{q², p} = {q q, p} = q {q, p} + q {q, p}", 34, INK), 0, -0.3)
    yield [FadeIn(ex)]
    res = at(eq("= q × 1 + q × 1 = 2q", 34, INK), 0, -1.3)
    used = at(lab("uses only {q, p} = 1", 26, PURPLE), 0, -2.3)
    yield [FadeIn(res), FadeIn(used)]


@slide("For quantities built by adding and multiplying", "One relation to change")
def one_relation(s):
    root = at(card("{q, p} = 1", 4.0, 1.0, PURPLE, 34), -4.4, 0.0)
    kids = [at(chip(t, PURPLE, size=26, h=0.7), 1.4, y) for t, y in (("{q², p} = 2q", 1.6), ("{q, H}", 0.5), ("{p, H}", -0.6), ("…", -1.7))]
    yield [FadeIn(root), *[FadeIn(k) for k in kids], *[GrowArrow(arrow(root.get_right(), k.get_left())) for k in kids],
           FadeIn(W("every bracket of sums and products of q and p comes down to it", 26, 24, INK, align=ORIGIN).move_to([-4.4, -1.3, 0]))]
    q = at(card("a quantum\nrelation", 3.4, 1.4, ORANGE, 30), 5.4, 0.0)
    yield [Indicate(root, color=ORANGE), FadeIn(at(T("change only this one", 26, ORANGE), -4.4, 1.0))]
    yield [FadeIn(q), FadeIn(lab("the next chapter", 24).move_to([5.4, -1.1, 0]))]


# ------------------------------------------------------------------ where they return
deck.part("Where these tools come back")

TOOLS = [("H = p²/2m + V", PURPLE, "the operator of the Schrödinger equation (next chapter)"),
         ("the spring", BLUE, "the harmonic oscillator, quantized exactly"),
         ("{q, p} = 1", PURPLE, "the commutator: how much order matters"),
         ("action, Euler–Lagrange", PURPLE, "fields: a coordinate at every point of space"),
         ("momentum, Hamiltonian", PURPLE, "built the same way for fields"),
         ("symmetry → conservation", BLUE, "Noether's theorem: electric charge")]
TOOL_Y = [1.55, 0.6, -0.35, -1.3, -2.25, -3.2]


def tool_row(k):
    name, color, dest = TOOLS[k]
    a = at(card(name, 4.6, 0.72, color, 26), -4.8, TOOL_Y[k])
    b = T(dest, 26, INK).move_to([-1.75, TOOL_Y[k], 0], aligned_edge=LEFT)
    return VGroup(a, Arrow(a.get_right(), b.get_left(), buff=0.12, color=MUTED, stroke_width=4, tip_length=0.18), b)


def tool_anim(k):
    a, ar, b = tool_row(k)
    return [FadeIn(a, shift=RIGHT * 0.2), GrowArrow(ar), FadeIn(b, shift=RIGHT * 0.2)]


def tool_heads():
    return VGroup(lab("this chapter", 24, MUTED, True).move_to([-4.8, 2.4, 0]), lab("comes back as", 24, MUTED, True).move_to([0.0, 2.4, 0]))


@slide("Where these tools come back.", "Where these tools come back")
def back1(s):
    yield [FadeIn(tool_heads())]
    yield tool_anim(0)


@slide("The harmonic oscillator chapter quantizes", "Where these tools come back")
def back2(s):
    s.add(tool_heads(), tool_row(0))
    yield tool_anim(1)
    yield tool_anim(2)


@slide("The action and the Euler-Lagrange equation come", "Where these tools come back")
def back3(s):
    s.add(tool_heads(), *[tool_row(k) for k in range(3)])
    yield tool_anim(3)
    yield tool_anim(4)
    yield tool_anim(5)


@slide("Every path has an action.", "Path integrals: every path counts")
def back4(s):
    a, b = np.array([-5.6, -1.4, 0]), np.array([0.6, -1.4, 0])
    angles = (0.4, 0.9, 1.9, 2.4, -0.4)
    paths = VGroup(*[ArcBetweenPoints(a, b, angle=-ang, color=LINE, stroke_width=4) for ang in angles])
    real = ArcBetweenPoints(a, b, angle=-1.4, color=BLUE, stroke_width=6)
    ends = VGroup(Dot(a, radius=0.1, color=INK), Dot(b, radius=0.1, color=INK))
    tags = VGroup(*[chip("S", PURPLE, size=22, h=0.5).move_to(p.point_from_proportion(f)) for p, f in zip(paths, (0.3, 0.7, 0.25, 0.75, 0.5))])
    yield [FadeIn(ends), LaggedStart(*[Create(p) for p in paths], lag_ratio=0.15), Create(real), FadeIn(tags),
           FadeIn(at(T("every path has an action", 28, INK), -2.5, 2.2))]
    w = at(card("add up all paths,\neach weighted by a\nfactor set by its action", 5.6, 2.0, PURPLE, 28), 4.3, 0.9)
    yield [FadeIn(w, shift=LEFT * 0.2)]
    yield [real.animate.set_stroke(width=9), Indicate(real, color=BLUE),
           FadeIn(at(W("explains why classical physics sees the stationary path", 26, 26, BLUE, align=ORIGIN), 4.3, -1.15))]
    yield [FadeIn(at(pill("an optional part, after the Standard Model", MUTED, 24), 0, -3.4))]


@slide("In the next chapter, position and momentum", "Next: first quantization")
def finale(s):
    q = at(chip("q", BLUE, size=36, h=0.9), -4.8, 1.4)
    p = at(chip("p", BLUE, size=36, h=0.9), -3.4, 1.4)
    ops = at(card("operators", 3.6, 1.0, ORANGE, 30), 2.6, 1.4)
    yield [FadeIn(q), FadeIn(p), GrowArrow(arrow(VGroup(q, p), ops)), FadeIn(ops), FadeIn(lab("next chapter", 24).move_to([-0.9, 2.1, 0]))]
    h = at(eq("H = p²/2m + V", 40, PURPLE), -3.6, -0.6)
    job = at(W("keeps its job: the function that moves the state forward in time", 30, 26, INK, align=LEFT), 3.9, -0.6)
    yield [FadeIn(h), GrowArrow(arrow(h, job)), FadeIn(job)]
    yield [FadeIn(at(pill("next: first quantization", INK, 30), 0, -2.6))]

"""Electroweak unification diagrams. Render through npm run docs:manim -- --page electroweak-unification."""
from manim import *
import numpy as np
from concept_diagrams import label, math, arrow, box, heading, INK, MUTED, BLUE, TEAL, ORANGE, PURPLE, PALE

config.background_color = WHITE
config.frame_width = 16
config.frame_height = 9

GREY = '#9aaabb'
RED = '#b3261e'


def circle_node(x, y, sym, color, radius=0.5):
    return VGroup(Circle(radius=radius, color=color, stroke_width=3,
                         fill_color=PALE, fill_opacity=0.7),
                  MathTex(sym, font_size=40, color=INK)).move_to([x, y, 0])


def edge_toward(center, target, radius=0.66):
    center = np.array([*center, 0.])
    d = np.array([*target, 0.]) - center
    return center + d / np.linalg.norm(d) * radius


def edge_pair(a, b, radius=0.66):
    a = np.array([*a, 0.])
    b = np.array([*b, 0.])
    d = (b - a) / np.linalg.norm(b - a)
    return a + d * radius, b - d * radius


class W3PhotonMismatch(Scene):
    def construct(self):
        heading(self, 'Why W³ cannot be the photon',
                'Solid line: that component couples to the field. Dashed line with ×: no coupling.')
        w3 = (-5.2, 0.0)
        ph = (5.2, 0.0)
        self.add(circle_node(*w3, r'W^3', TEAL, 0.58),
                 circle_node(*ph, r'\gamma', ORANGE, 0.58))
        self.add(math(r'SU(2)_L', -5.2, -0.98, 26, TEAL),
                 label('neutral field', -5.2, -1.46, 19, TEAL),
                 label('the photon', 5.2, -0.98, 21, ORANGE),
                 label('couples to electric charge', 5.2, -1.46, 19, ORANGE, 3.1))
        rows = [(1.35, r'\nu_{eL}', r'Q=0', True, False),
                (0.05, r'e_L', r'Q=-e', True, True),
                (-1.25, r'e_R', r'Q=-e', False, True)]
        for y, sym, q, couples_w3, couples_ph in rows:
            self.add(box(0, y, 2.3, 0.95),
                     math(sym, 0, y + 0.16, 32),
                     math(q, 0, y - 0.27, 24, MUTED))
            for center, x_edge, couples, color in [
                    (w3, -1.15, couples_w3, TEAL),
                    (ph, 1.15, couples_ph, ORANGE)]:
                start = edge_toward(center, [x_edge, y])
                end = np.array([x_edge, y, 0.])
                if couples:
                    self.add(Line(start, end, color=color, stroke_width=4))
                else:
                    dashed = DashedLine(start, end, color=GREY, stroke_width=3)
                    self.add(dashed, MathTex(r'\times', font_size=42, color=RED)
                             .move_to(dashed.get_center()))
        self.add(label('W³ couples to the left-chiral neutrino but not to the right-chiral electron;', 0, -2.6, 23, MUTED, 15),
                 label('the photon does the opposite. No coupling strength g repairs this mismatch.', 0, -3.15, 23, MUTED, 15))


class HyperchargeOffset(Scene):
    def construct(self):
        heading(self, 'Hypercharge shifts both doublet members together',
                'The lepton doublet moves from weak isospin to electric charge by one shared offset')
        axis_x = -4.3
        values = [0.5, 0.0, -0.5, -1.0]
        y_of = {v: 0.4 + 2.0 * v for v in values}
        self.add(Line([axis_x, 1.85, 0], [axis_x, -2.05, 0], color=GREY, stroke_width=3))
        for v, tag in [(0.5, r'+\tfrac12'), (0.0, r'0'),
                       (-0.5, r'-\tfrac12'), (-1.0, r'-1')]:
            y = y_of[v]
            self.add(Line([axis_x - 0.14, y, 0], [axis_x + 0.14, y, 0], color=GREY, stroke_width=3),
                     math(tag, axis_x - 0.45, y, 26, MUTED))
        cols = [(-3.5, 0.5, 0.0, r'\nu_{eL}', r'Q=0', BLUE),
                (-2.6, -0.5, -1.0, r'e_L', r'Q=-1', TEAL)]
        for x, t_start, t_end, name, q, color in cols:
            y0, y1 = y_of[t_start], y_of[t_end]
            self.add(DashedLine([axis_x + 0.14, y0, 0], [x - 0.13, y0, 0], color='#c6cfda', stroke_width=2),
                     DashedLine([axis_x + 0.14, y1, 0], [x - 0.13, y1, 0], color='#c6cfda', stroke_width=2),
                     Dot([x, y0, 0], color=color, radius=0.11),
                     Dot([x, y1, 0], color=color, radius=0.11),
                     arrow((x, y0 - 0.14), (x, y1 + 0.14), PURPLE, 4),
                     math(name, x + 0.55, y0, 30, color),
                     math(q, x + 0.55, y1, 28, color))
        self.add(label('same shift\nY/2 = −1/2', -3.05, -0.12, 20, MUTED))
        self.add(box(3.9, 1.3, 7.0, 2.2, PURPLE),
                 math(r'Q = T^3 + \frac{Y}{2}', 3.9, 1.55, 44),
                 label('weak isospin plus half the hypercharge', 3.9, 0.62, 21, MUTED, 6.2))
        self.add(box(3.9, -1.35, 7.0, 2.6, TEAL),
                 label('Lepton doublet:  Y = −1', 3.9, -0.32, 23, TEAL),
                 math(r'\nu_{eL}:\; +\tfrac12 - \tfrac12 = 0', 3.9, -1.0, 29, BLUE),
                 math(r'e_L:\; -\tfrac12 - \tfrac12 = -1', 3.9, -1.6, 29, TEAL),
                 label('Both entries move by the same −1/2; their difference stays 1.', 3.9, -2.3, 20, MUTED, 6.2))
        self.add(label('Start: weak-isospin values. End: electric charges. One hypercharge belongs to the whole multiplet,', 0, -3.5, 22, MUTED, 15.2),
                 label('so its members always shift together.', 0, -4.0, 22, MUTED, 15.2))


class NeutralFieldMixing(Scene):
    def construct(self):
        heading(self, 'From symmetry fields to photon and Z',
                'Hypercharge adds B; rotating the two neutral fields produces A and Z')
        left = {'W+': (-5.2, 1.6), 'W-': (-5.2, 0.7), 'W3': (-5.2, -0.95), 'B': (-5.2, -2.45)}
        right = {'W+': (5.2, 1.6), 'W-': (5.2, 0.7), 'A': (5.2, -0.95), 'Z': (5.2, -2.45)}
        for key, (x, y) in left.items():
            color = PURPLE if key == 'B' else BLUE
            self.add(circle_node(x, y, {'W+': r'W^+', 'W-': r'W^-', 'W3': r'W^3', 'B': r'B'}[key], color))
        for key, (x, y) in right.items():
            color = {'W+': BLUE, 'W-': BLUE, 'A': ORANGE, 'Z': TEAL}[key]
            self.add(circle_node(x, y, {'W+': r'W^+', 'W-': r'W^-', 'A': r'A', 'Z': r'Z'}[key], color))
        self.add(arrow((-4.55, 1.6), (4.55, 1.6), BLUE, 4),
                 arrow((-4.55, 0.7), (4.55, 0.7), BLUE, 4),
                 label('charged fields unchanged', 0, 1.15, 20, MUTED))
        for src, dst, color in [(left['W3'], right['A'], BLUE),
                                (left['W3'], right['Z'], BLUE),
                                (left['B'], right['A'], PURPLE),
                                (left['B'], right['Z'], PURPLE)]:
            p1, p2 = edge_pair(src, dst)
            self.add(Line(p1, p2, color=color, stroke_width=3.5))
        self.add(box(0, -0.1, 8.4, 1.25),
                 math(r'A_\mu = s_W\,W^3_\mu + c_W\,B_\mu', 0, 0.2, 30, ORANGE),
                 math(r'Z_\mu = c_W\,W^3_\mu - s_W\,B_\mu', 0, -0.42, 30, TEAL))
        self.add(label('hypercharge', -6.9, -2.2, 20, PURPLE),
                 math(r'U(1)_Y', -6.9, -2.75, 26, PURPLE),
                 arrow((-6.2, -2.45), (-5.82, -2.45), PURPLE, 2.5))
        self.add(label('charged weak', 6.7, 1.6, 21, BLUE, 2.3),
                 label('charged weak', 6.7, 0.7, 21, BLUE, 2.3),
                 label('electromagnetic', 6.7, -0.95, 21, ORANGE, 2.4),
                 label('neutral weak', 6.7, -2.45, 21, TEAL, 2.3))
        self.add(label('Each connecting line means "contributes to this field combination", not particle conversion.\n'
                       'The rotation is a change of basis: two neutral fields in, two out.', 0, -3.9, 21, MUTED, 15.5))

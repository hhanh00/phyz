"""Diagrams for the Math Refresher appendix; pnpm docs:manim --page appendix-math-*."""
from manim import *
import numpy as np
from concept_diagrams import label, math, heading, INK, MUTED, BLUE, TEAL, ORANGE, PURPLE

config.background_color = WHITE
config.frame_width = 16
config.frame_height = 9


def arrow3(a, b, color=MUTED, width=3):
    return Arrow(np.asarray(a, dtype=float), np.asarray(b, dtype=float), buff=0.08,
                 color=color, stroke_width=width, max_tip_length_to_length_ratio=0.12)


class EulerCircle(Scene):
    def construct(self):
        heading(self, "Euler's formula places the unit circle in the complex plane",
                'A point at angle θ has coordinates (cos θ, sin θ) and is written as a phase')
        center = np.array([-4, -0.2, 0])
        R = 2.2
        self.add(Circle(radius=R, color=BLUE, stroke_width=3).move_to(center))
        self.add(arrow3(center + [-R - 0.7, 0, 0], center + [R + 0.7, 0, 0]),
                 arrow3(center + [0, -R - 0.7, 0], center + [0, R + 0.7, 0]))
        theta = 0.9
        pt = center + R * np.array([np.cos(theta), np.sin(theta), 0])
        self.add(Line(center, pt, color=ORANGE, stroke_width=3), Dot(pt, color=ORANGE, radius=0.11))
        self.add(Arc(radius=0.75, angle=theta, arc_center=center, color=PURPLE, stroke_width=3))
        self.add(DashedLine(pt, center + [R * np.cos(theta), 0, 0], color=TEAL),
                 DashedLine(pt, center + [0, R * np.sin(theta), 0], color=TEAL))
        self.add(math('Re', center[0] + R + 0.9, center[1] + 0.2, 28),
                 math('Im', center[0] + 0.2, center[1] + R + 0.7, 28))
        self.add(math(r'\cos\theta', center[0] + R * np.cos(theta) / 2 - 0.15, center[1] - 0.55, 30, TEAL),
                 math(r'\sin\theta', center[0] + R * np.cos(theta) - 0.95, center[1] + R * np.sin(theta) / 2, 30, TEAL),
                 math(r'\theta', center[0] + 0.85, center[1] + 0.5, 26, PURPLE))
        self.add(math(r'e^{i\theta}=\cos\theta+i\sin\theta', 4.4, 1.5, 40),
                 math(r'|e^{i\theta}|=1', 4.4, 0.7, 32),
                 label('A number of magnitude one sits on the unit circle.', 4.4, -0.1, 22, MUTED, width=6.2),
                 label('Its angle θ is the phase.', 4.4, -0.8, 22, MUTED, width=6.2))
        self.add(label('The projections onto the axes are cosine and sine.', 0, -3.6, 26, MUTED))


class EigenvectorScaling(Scene):
    def construct(self):
        heading(self, 'An eigenvector keeps its direction when the matrix acts',
                'One vector is only stretched; another is turned')
        o1 = np.array([-5.4, -1.2, 0])
        v = np.array([1.9, 1.0, 0])
        self.add(arrow3(o1, o1 + v, BLUE), arrow3(o1, o1 + 2 * v, ORANGE))
        self.add(Dot(o1, color=INK, radius=0.07))
        self.add(label('v', o1[0] + v[0] / 2 - 0.35, o1[1] + v[1] / 2 + 0.35, 26, BLUE),
                 label('Av = 2v', o1[0] + 2 * v[0] + 0.55, o1[1] + 2 * v[1], 26, ORANGE))
        self.add(label('Eigenvector: same direction', -3.45, 1.5, 23, MUTED))
        o2 = np.array([0.7, -1.2, 0])
        w = np.array([2.3, 0.6, 0])
        aw = np.array([0.7, 2.2, 0])
        self.add(arrow3(o2, o2 + w, BLUE), arrow3(o2, o2 + aw, ORANGE))
        self.add(Dot(o2, color=INK, radius=0.07))
        self.add(label('w', o2[0] + w[0] / 2 + 0.15, o2[1] + w[1] / 2 - 0.5, 26, BLUE),
                 label('Aw', o2[0] + aw[0] / 2 - 0.35, o2[1] + aw[1] / 2 + 0.3, 26, ORANGE))
        self.add(label('Other vector: turned', 1.85, 1.5, 23, MUTED))
        self.add(math(r'A v=\lambda v', 5.4, 1.6, 40),
                 label('For an eigenvector, the matrix only rescales it.', 5.4, 0.5, 22, MUTED, width=5.6),
                 label('The rescaling factor λ is the eigenvalue.', 5.4, -0.2, 22, MUTED, width=5.6))
        self.add(label('Solving A v = λ v finds the special directions of a matrix.', 0, -3.6, 26, MUTED))


class RotationGenerator(Scene):
    def construct(self):
        heading(self, 'The generator is the tangent direction at the identity',
                'An infinitesimal rotation moves a point along the circle')
        center = np.array([-4, -0.2, 0])
        R = 2.2
        self.add(Circle(radius=R, color=BLUE, stroke_width=3).move_to(center))
        identity = center + [R, 0, 0]
        self.add(Dot(identity, color=INK, radius=0.11), math('1', identity[0], identity[1] - 0.55, 28))
        self.add(arrow3(identity, identity + [0, 1.35, 0], ORANGE, width=4))
        self.add(label('generator T', identity[0] + 0.4, identity[1] + 1.95, 26, ORANGE))
        a = 0.5
        pt = center + R * np.array([np.cos(a), np.sin(a), 0])
        self.add(Line(center, pt, color=TEAL, stroke_width=3), Dot(pt, color=TEAL, radius=0.11),
                 Arc(radius=0.8, angle=a, arc_center=center, color=TEAL, stroke_width=3))
        self.add(math(r'e^{i\alpha T}', center[0] + R * np.cos(a) + 0.15, center[1] + R * np.sin(a) + 0.55, 30, TEAL))
        self.add(math(r'U=e^{i\alpha T}=1+i\alpha T+\cdots', 4.4, 1.4, 36),
                 math(r'\text{For U(1), }T=1', 4.4, 0.55, 30),
                 label('The generator fixes the direction of the infinitesimal change.', 4.4, -0.25, 22, MUTED, width=6.4),
                 label('Repeating that change builds a finite rotation.', 4.4, -0.9, 22, MUTED, width=6.4))
        self.add(label('The tangent at the identity points along the infinitesimal rotation.', 0, -3.6, 26, MUTED))

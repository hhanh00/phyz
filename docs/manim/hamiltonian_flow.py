"""Hamiltonian flow in the (phi, pi) state plane, for the QFT page.

One oscillator mode of the free field, H = 1/2 pi^2 + 1/2 w^2 phi^2 (w = 1):
its level sets are circles, the flow (phi_dot = pi, pi_dot = -phi) runs
clockwise along them, and the vacuum at the origin is where the flow
vanishes. Sparse background arrows show the direction H plants everywhere.

Render a static image:
    manim render -s -r 2400,1350 -q m hamiltonian_flow.py HamiltonianFlow
"""

from manim import *
import numpy as np

config.background_color = "#ffffff"  # diagrams sit on white in the docs

GRAY = "#666666"
LIGHT = "#c9ced6"
BLUE = "#2563eb"
ORANGE = "#d97706"


class HamiltonianFlow(Scene):
    def construct(self):
        mobs = []

        # --- title and formula ---
        title = Text("Hamiltonian flow in state space", font="Helvetica",
                     color=GRAY, font_size=26).move_to([0, 3.35, 0])
        formula = MathTex(r"H = \tfrac{1}{2}\,\pi^2 + \tfrac{1}{2}\,\omega^2\phi^2",
                          color=GRAY).scale(0.9).next_to(title, DOWN, buff=0.22)
        mobs += [title, formula]

        # --- sparse vector-field arrows: direction (pi, -phi) everywhere ---
        for gx in (-2, -1, 0, 1, 2):
            for gy in (-2, -1, 0, 1, 2):
                if (gx, gy) == (0, 0):
                    continue
                p = np.array([gx, gy, 0.0])
                d = np.array([gy, -gx, 0.0])
                d = d / np.linalg.norm(d)
                mobs.append(Arrow(p - 0.13 * d, p + 0.13 * d, color=LIGHT,
                                  stroke_width=3, tip_length=0.13,
                                  max_tip_length_to_length_ratio=0.5))

        # --- axes ---
        x_axis = Line([-3.0, 0, 0], [3.0, 0, 0], color=GRAY, stroke_width=4).add_tip(tip_length=0.18)
        y_axis = Line([0, -3.0, 0], [0, 3.0, 0], color=GRAY, stroke_width=4).add_tip(tip_length=0.18)
        mobs += [x_axis, y_axis]
        mobs.append(MathTex(r"\phi", color=GRAY).scale(0.9).move_to([3.2, 0.22, 0]))
        mobs.append(MathTex(r"\pi", color=GRAY).scale(0.9).move_to([0.25, 3.15, 0]))

        # --- level sets of H: circles at r = sqrt(2H); flow is clockwise ---
        def tangent(theta):
            # velocity at angle theta for (phi_dot, pi_dot) = (pi, -phi)
            return np.array([np.sin(theta), -np.cos(theta), 0.0])

        def orbit(r, sw):
            c = Circle(radius=r, color=BLUE, stroke_width=sw)
            mobs.append(c)
            for theta in np.radians([30, 150, 270]):
                p = r * np.array([np.cos(theta), np.sin(theta), 0.0])
                t = tangent(theta)
                mobs.append(ArrowTriangleFilledTip(length=0.18, width=0.18,
                                                   color=BLUE)
                            .rotate(np.arctan2(t[1], t[0])).move_to(p))

        orbit(0.9, 3.5)
        orbit(1.7, 4.5)
        orbit(2.5, 6)

        # --- energy labels, stacked clear of the orbits, with leader lines
        # to each circle along the 45-degree direction ---
        targets = (0.9, 1.7, 2.5)
        for i, (r, lab) in enumerate(zip(targets, (r"H\ \text{small}",
                                                   r"H\ \text{mid}",
                                                   r"H\ \text{large}"))):
            lab_mob = MathTex(lab, color=BLUE).scale(0.55).move_to(
                [3.05, 1.55 + 0.55 * i, 0])
            tgt = (r / np.sqrt(2)) * np.array([1, 1, 0])
            start = lab_mob.get_left() + np.array([-0.06, 0, 0])
            mobs.append(Line(start, tgt, color=LIGHT, stroke_width=1.5))
            mobs.append(lab_mob)

        # --- vacuum at the origin: the one state where the flow vanishes ---
        mobs.append(Dot([0, 0, 0], radius=0.05, color="#333333"))
        mobs.append(Text("vacuum", font="Helvetica", color=GRAY,
                         font_size=18).move_to([0.22, 0.5, 0]))

        # --- one state on the outer orbit, with the arrow H gives it ---
        theta = np.radians(210)
        p = 2.5 * np.array([np.cos(theta), np.sin(theta), 0.0])
        t = tangent(theta)
        mobs.append(Dot(p, radius=0.08, color=ORANGE))
        mobs.append(Arrow(p + 0.15 * t, p + 0.62 * t, color=ORANGE,
                          stroke_width=4, tip_length=0.16))
        mobs.append(Text("one state", font="Helvetica", color=ORANGE,
                         font_size=18).move_to(p + np.array([-0.55, -0.45, 0])))

        # --- bottom note ---
        mobs.append(MathTex(
            r"\text{orbits close because } H \text{ is conserved; one such plane per momentum mode } \mathbf{k}",
            color=GRAY).scale(0.55).move_to([0, -3.6, 0]))

        self.add(VGroup(*mobs))

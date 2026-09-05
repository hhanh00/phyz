"""Fock-state occupation diagrams for the Field Quantization page.

Three panels, each a momentum axis with one filled dot per quantum, stacked
above the momentum the quanta occupy:

  1.  a^dag(p) |0>                   : one particle at p
  2.  (a^dag(p))^2 |0>               : two particles stacked at p
  3.  a^dag(q) (a^dag(p))^2 |0>      : two at p, one at q >> p

A dot is one quantum of a mode; the mode's momentum places the dot on the
axis, and a column of dots is one mode filled with several quanta.

Render a static image:
    manim render -s -r 2400,1350 -q m occupation_states.py OccupationStates
"""

from manim import *
import numpy as np

config.background_color = "#ffffff"  # diagrams sit on white in the docs

GRAY = "#666666"
LIGHT = "#c9ced6"
BLUE = "#2563eb"
ORANGE = "#d97706"


class OccupationStates(Scene):
    def construct(self):
        self.add(panel(-5.0, 1, 0, r"\text{one particle at } p",
                       r"\hat a^\dagger(p)\,\lvert 0\rangle"))
        self.add(panel(0.0, 2, 0, r"\text{two particles at } p",
                       r"\big(\hat a^\dagger(p)\big)^2\,\lvert 0\rangle"))
        self.add(panel(5.0, 2, 1, r"\text{two at } p,\ \text{one at } q",
                       r"\hat a^\dagger(q)\big(\hat a^\dagger(p)\big)^2\lvert 0\rangle"))

        self.add(MathTex(
            r"\text{each dot is one quantum; a mode's momentum places it on the axis}",
            color=GRAY).scale(0.6).move_to([0, -3.7, 0]))


def panel(cx, n_p, n_q, title, formula):
    """One occupation diagram centered at x = cx. Returns a VGroup."""
    mobs = []
    axis_y = -0.4          # height of the momentum axis
    p_x = -0.5             # momentum p (moderate)
    q_x = 1.75             # momentum q >> p (near the far right)

    # --- momentum axis ---
    axis = Line([cx - 2.2, axis_y, 0], [cx + 2.2, axis_y, 0],
                color=GRAY, stroke_width=4).add_tip(tip_length=0.16)
    mobs.append(axis)
    mobs.append(MathTex(r"\text{momentum}", color=GRAY).scale(0.55)
                .move_to([cx + 1.35, axis_y + 0.42, 0]))

    # --- origin and momentum ticks ---
    mobs.append(Dot([cx - 2.2, axis_y, 0], radius=0.04, color="#333333"))
    mobs.append(MathTex("0", color=GRAY).scale(0.7).move_to([cx - 2.2, axis_y - 0.38, 0]))

    for x, lab in ((p_x, "p"), (q_x, "q")):
        mobs.append(Line([cx + x, axis_y, 0], [cx + x, axis_y - 0.14, 0],
                         color=GRAY, stroke_width=3))
        mobs.append(DashedLine([cx + x, axis_y + 0.12, 0], [cx + x, axis_y + 2.0, 0],
                               color=LIGHT, stroke_width=1.5, dash_length=0.08))
        mobs.append(MathTex(lab, color=GRAY).scale(0.7).move_to([cx + x, axis_y - 0.42, 0]))

    # q >> p annotation between the two ticks
    mobs.append(MathTex(r"q \gg p", color=GRAY).scale(0.55)
                .move_to([cx + (p_x + q_x) / 2, axis_y - 0.85, 0]))

    # --- particles: one filled dot per quantum, stacked above its momentum ---
    def stack(x, count):
        for i in range(count):
            mobs.append(Dot([cx + x, axis_y + 0.45 + 0.34 * i, 0],
                            radius=0.12, color=BLUE))

    stack(p_x, n_p)
    stack(q_x, n_q)

    # --- caption ---
    title_mob = MathTex(title, color=GRAY).scale(0.65)
    formula_mob = MathTex(formula, color=ORANGE).scale(0.6)
    cap = VGroup(title_mob, formula_mob).arrange(DOWN, buff=0.14).move_to([cx, 2.95, 0])
    mobs.append(cap)

    return VGroup(*mobs)

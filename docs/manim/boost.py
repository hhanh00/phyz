"""Galilean vs Lorentz boost spacetime diagrams.

Convention: x on the VERTICAL axis, t on the HORIZONTAL axis (c = 1).
Galilean: the t'-axis coincides with t (t' = t), the x'-axis tilts up.
Lorentz:  both primed axes tilt symmetrically so light always bisects them.

Render a static image:
    manim render -s -r 2400,1350 -q m boost.py BoostDiagrams
"""

from manim import *
import numpy as np

config.background_color = "#ffffff"  # diagrams sit on white in the docs

GRAY = "#666666"
BLUE = "#2563eb"
ORANGE = "#d97706"
V = 0.5  # boost speed in units of c


class BoostDiagrams(Scene):
    def construct(self):
        self.add(panel(-3.5, -0.5, galilean=True))
        self.add(panel(3.5, -0.5, galilean=False))


def panel(cx, cy, galilean):
    """One spacetime diagram. Returns a VGroup."""
    O = np.array([cx, cy, 0.0])
    R = RIGHT
    U = UP
    mobs = []

    def P(t, x):
        return O + t * R + x * U

    # --- unprimed axes (gray) ---
    t_axis = Line(P(-2.7, 0), P(2.7, 0), color=GRAY, stroke_width=4).add_tip(tip_length=0.18)
    x_axis = Line(P(0, -2.7), P(0, 2.7), color=GRAY, stroke_width=4).add_tip(tip_length=0.18)
    mobs += [t_axis, x_axis]

    # --- light cone at 45° (dashed orange) ---
    light = DashedLine(P(-2.6, -2.6), P(2.6, 2.6), color=ORANGE, stroke_width=3, dash_length=0.12)
    mobs.append(light)

    # --- x'-axis: x = v t, tilts up toward the light ray ---
    xp = Line(P(-2.7, -V * 2.7), P(2.7, V * 2.7), color=BLUE, stroke_width=4).add_tip(tip_length=0.18)
    mobs.append(xp)

    if galilean:
        # t'-axis coincides with t axis (t' = t)
        mobs.append(MathTex(r"t = t'", color=GRAY).scale(0.8).move_to(P(1.25, -0.32)))
    else:
        # t'-axis: t = v x, tilts up symmetrically toward the x-axis
        tp = Line(P(-V * 2.7, -2.7), P(V * 2.7, 2.7), color=BLUE, stroke_width=4).add_tip(tip_length=0.18)
        mobs.append(tp)
        mobs.append(MathTex(r"t'", color=BLUE).scale(0.8).move_to(P(1.8, 2.35)))

    # --- light-speed annotation: angle the light ray makes with the
    # primed axes ---
    def polar(r, deg):
        a = np.radians(deg)
        return O + r * (np.cos(a) * R + np.sin(a) * U)

    if galilean:
        # 45° to the t-axis, but only ~18° to the x'-axis: not bisected,
        # so S' measures a different light speed
        a45 = Angle(t_axis, light, radius=0.85, color=ORANGE, stroke_width=3)
        a18 = Angle(xp, light, radius=1.4, color=ORANGE, stroke_width=3)
        mobs += [a45, a18]
        mobs.append(MathTex(r"45^\circ", color=ORANGE).scale(0.7).move_to(polar(1.02, 22.5)))
        mobs.append(MathTex(r"\approx 18^\circ", color=ORANGE).scale(0.7).move_to(polar(1.55, 35.8)))
    else:
        # equal ~18° angles on both sides of the light ray: bisected, so
        # light speed is the same in every frame
        a1 = Angle(xp, light, radius=1.15, color=ORANGE, stroke_width=3)
        a2 = Angle(light, tp, radius=1.15, color=ORANGE, stroke_width=3)
        mobs += [a1, a2]
        mobs.append(MathTex(r"\approx 18^\circ", color=ORANGE).scale(0.65).move_to(polar(1.42, 35.8)))
        mobs.append(MathTex(r"\approx 18^\circ", color=ORANGE).scale(0.65).move_to(polar(1.42, 54.2)))

    # --- origin and labels ---
    mobs.append(Dot(P(0, 0), radius=0.05, color="#333333"))
    mobs.append(MathTex("t", color=GRAY).scale(0.9).next_to(P(2.8, 0), UR, buff=0.12))
    mobs.append(MathTex("x", color=GRAY).scale(0.9).next_to(P(0, 2.8), UR, buff=0.12))
    mobs.append(MathTex(r"x'", color=BLUE).scale(0.8).move_to(P(2.35, 0.95)))
    mobs.append(Text("light", font="Helvetica", color=ORANGE, font_size=20).move_to(P(1.8, 1.95)))
    # Caption: title in Helvetica (ASCII only — ≠ and ′ are not in
    # Helvetica, so the note line is rendered in LaTeX instead), placed
    # clear of the x-axis arrowhead.
    caption_title = Text("Galilean boost" if galilean else "Lorentz boost",
                         font="Helvetica", color=GRAY, font_size=16)
    caption_note = MathTex(
        r"\text{light speed} \neq c \text{ in } S'" if galilean
        else r"\text{light speed} = c \text{ in every frame}",
        color=GRAY,
    ).scale(0.55)
    mobs.append(VGroup(caption_title, caption_note).arrange(DOWN, buff=0.1).move_to(P(0, -3.3)))
    return VGroup(*mobs)

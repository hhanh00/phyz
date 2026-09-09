"""Higgs-mechanism diagrams. Render through npm run docs:manim -- --page higgs-mechanism."""
from manim import *
import numpy as np
from concept_diagrams import label, math, arrow, box, INK, MUTED, BLUE, TEAL, ORANGE, PURPLE, PALE

config.background_color = WHITE
config.frame_width = 16
config.frame_height = 9

R0 = 1.5          # radius of the circle of minima, in scene units
HAT = '#a9c7f5'   # surface fill, two soft shades of the house blue
HAT2 = '#d3e2fb'
WALL = '#5f7fb8'  # surface mesh lines


def height(r):
    """Mexican-hat profile V(r): maximum at the centre, trough at r = R0."""
    return 1.15 * ((r * r) / (R0 * R0) - 1.0) ** 2


class MexicanHatPotential(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=62 * DEGREES, theta=-48 * DEGREES, zoom=0.95)

        surface = Surface(
            lambda u, v: np.array([u * np.cos(v), u * np.sin(v), height(u)]),
            u_range=[0.001, 2.25],
            v_range=[0, TAU],
            resolution=(22, 48),
            fill_opacity=0.9,
            stroke_width=0.6,
            stroke_color=WALL,
            checkerboard_colors=[HAT, HAT2],
        )
        self.add(surface)

        # Circle of degenerate minima at the bottom of the trough.
        minima = ParametricFunction(
            lambda t: np.array([R0 * np.cos(t), R0 * np.sin(t), 0.0]),
            t_range=[0, TAU], color=TEAL, stroke_width=7,
        )
        self.add(minima)

        # One chosen vacuum on that circle.
        vac = np.array([R0, 0.0, 0.0])
        self.add(Sphere(radius=0.13, color=ORANGE).move_to(vac).set_fill(ORANGE, 1.0))

        # Radial excitation h: up the wall, a curved (massive) direction.
        h_tip = np.array([2.15, 0.0, height(2.15)])
        self.add(Arrow3D(vac, h_tip, color=ORANGE, thickness=0.02, base_radius=0.07))

        # Angular excitation chi: around the trough at z = 0, a flat (massless) direction.
        chi = ParametricFunction(
            lambda t: np.array([R0 * np.cos(t), R0 * np.sin(t), 0.02]),
            t_range=[0, 0.9], color=PURPLE, stroke_width=6,
        )
        chi_end = np.array([R0 * np.cos(0.9), R0 * np.sin(0.9), 0.02])
        chi_dir = np.array([-np.sin(0.9), np.cos(0.9), 0.0])
        self.add(chi, Arrow3D(chi_end - 0.25 * chi_dir, chi_end + 0.05 * chi_dir,
                              color=PURPLE, thickness=0.02, base_radius=0.07))

        # Faint field-plane axes for Re(phi), Im(phi).
        self.add(
            Arrow3D([0, 0, 0], [2.7, 0, 0], color=MUTED, thickness=0.006, base_radius=0.04),
            Arrow3D([0, 0, 0], [0, 2.7, 0], color=MUTED, thickness=0.006, base_radius=0.04),
        )

        # Everything below is drawn in the flat 16x9 frame, not the 3D world.
        head = label('The Mexican-hat potential', 0, 3.8, 36)
        sub = label('Energy of the scalar field over the complex plane', 0, 3.2, 23, MUTED, 10)
        formula = math(r'V(\phi)=-\mu^2\,\phi^\ast\phi+\lambda(\phi^\ast\phi)^2', -4.9, 2.15, 30)

        legend = VGroup(
            box(4.6, 1.1, 5.9, 3.7, MUTED),
            math(r'|\phi|=v/\sqrt2', 4.6, 2.55, 28, TEAL),
            label('circle of degenerate minima', 4.6, 2.05, 20, TEAL, 5.2),
            label('chosen vacuum', 4.75, 1.45, 21, ORANGE, 4.6),
            label('h: radial, up the wall\ncurved direction, massive', 4.75, 0.7, 20, ORANGE, 5.2),
            label('chi: around the trough\nflat direction, massless (Goldstone)', 4.75, -0.25, 20, PURPLE, 5.4),
        )
        origin_lbl = label('Re phi', 2.9, -3.35, 21, MUTED)
        origin_lbl2 = label('Im phi', -3.0, -2.4, 21, MUTED)
        note = label('Moving around the trough costs no energy, so that excitation is massless; '
                     'climbing the wall costs energy, so the radial excitation has a mass.',
                     0, -4.05, 21, MUTED, 15.2)

        self.add_fixed_in_frame_mobjects(head, sub, formula, legend, origin_lbl, origin_lbl2, note)


class GoldstoneModes(Scene):
    def construct(self):
        self.add(label('The two excitations of the broken vacuum', 0, 3.85, 34))
        self.add(label('Radial motion costs energy; motion around the circle does not', 0, 3.22, 22, MUTED, 12))
        self.add(math(r'\phi=\tfrac{1}{\sqrt2}\,(v+h)\,e^{i\theta/v}', 0, 2.45, 32))
        self.add(Line([0, 1.9, 0], [0, -2.7, 0], color='#dfe4ea', stroke_width=2))

        # --- left panel: the complex phi plane ---
        self.add(label('Field space (the complex φ plane)', -4.2, 1.7, 22, INK, 6.4))
        ox, oy, R = -4.2, -0.55, 1.5
        self.add(Line([ox - 2.1, oy, 0], [ox + 2.0, oy, 0], color='#c6cfda', stroke_width=2),
                 Line([ox, oy - 1.75, 0], [ox, oy + 1.85, 0], color='#c6cfda', stroke_width=2),
                 label('Re φ', ox + 2.0, oy - 0.32, 19, MUTED),
                 label('Im φ', ox + 0.36, oy + 1.85, 19, MUTED))
        self.add(Circle(radius=R, color=TEAL, stroke_width=6).move_to([ox, oy, 0]))
        self.add(label('circle of minima', ox, oy - 2.15, 20, TEAL, 4.6))

        theta0 = 34 * DEGREES
        vac = np.array([ox + R * np.cos(theta0), oy + R * np.sin(theta0), 0])
        rad = np.array([np.cos(theta0), np.sin(theta0), 0])
        self.add(Dot(vac, color=ORANGE, radius=0.11))
        self.add(label('chosen\nvacuum', vac[0] + 0.02, vac[1] - 0.9, 19, ORANGE, 1.9))

        # radial excitation h: outward, up the wall
        self.add(arrow(vac[:2], (vac + 0.85 * rad)[:2], ORANGE, 5))
        self.add(math(r'h', vac[0] + 1.02 * rad[0] + 0.28, vac[1] + 1.02 * rad[1] + 0.12, 30, ORANGE))

        # angular excitation theta: along the circle, the Goldstone direction
        arc = Arc(radius=R, start_angle=theta0, angle=0.9, arc_center=[ox, oy, 0],
                  color=PURPLE, stroke_width=5)
        arc.add_tip(tip_length=0.24)
        self.add(arc)
        tl = 34 + 24
        self.add(math(r'\theta', ox + (R + 0.55) * np.cos(tl * DEGREES),
                      oy + (R + 0.55) * np.sin(tl * DEGREES), 30, PURPLE))

        # --- right panel: energy cost of each excitation ---
        self.add(label('Energy of each excitation', 4.1, 1.7, 22, INK, 6.4))
        vx, bx, by = 1.95, 3.5, -1.15
        self.add(arrow((vx, by - 0.35), (vx, 1.75), MUTED, 3), label('V', vx - 0.32, 1.72, 22, MUTED))
        parab = ParametricFunction(lambda t: np.array([bx + t, by + 0.8 * t * t, 0]),
                                   t_range=[-1.5, 1.55, 0.02], color=BLUE, stroke_width=6)
        flat = Line([bx - 1.5, by, 0], [bx + 1.7, by, 0], color=PURPLE, stroke_width=6)
        self.add(flat, parab, Dot([bx, by, 0], color=ORANGE, radius=0.1))
        self.add(label('vacuum', bx, by - 0.4, 18, ORANGE, 2.0))
        self.add(math(r'V(h)\sim h^2', bx, by + 2.05, 26, BLUE))
        self.add(label('radial h:', bx + 2.6, by + 1.7, 21, BLUE, 2.2),
                 label('curved, so massive', bx + 2.6, by + 1.3, 20, BLUE, 3.0),
                 math(r'm_h^2=2\lambda v^2', bx + 2.6, by + 0.8, 24, BLUE))
        self.add(label('angular θ:', bx + 2.6, by + 0.05, 21, PURPLE, 2.4),
                 label('flat, so massless (Goldstone)', bx + 2.6, by - 0.35, 20, PURPLE, 3.2))

        self.add(label('Radial motion (h) climbs the wall of the potential, so it costs energy and h is massive. '
                       'Motion around the circle (θ) stays at the minimum, so it costs no energy and θ is the massless Goldstone mode.',
                       0, -3.75, 21, MUTED, 15.4))

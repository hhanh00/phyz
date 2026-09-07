"""Static teaching diagrams. Render through npm run docs:manim.

All positions use a 16 x 9 frame. No animations or runtime dependencies
are required by the website; the generated PNGs are committed assets.
"""
from manim import *
import numpy as np

config.background_color = WHITE
config.frame_width = 16
config.frame_height = 9
INK = '#172b4d'
MUTED = '#526477'
BLUE = '#2563eb'
TEAL = '#008577'
ORANGE = '#c66a08'
PURPLE = '#8052bd'
PALE = '#eef3fa'


def label(s, x, y, size=26, color=INK, width=None):
    obj = Text(s, font_size=size, color=color)
    if width and obj.width > width:
        obj.scale_to_fit_width(width)
    return obj.move_to([x, y, 0])


def math(s, x, y, size=34, color=INK, width=None):
    obj = MathTex(s, font_size=size, color=color)
    if width and obj.width > width:
        obj.scale_to_fit_width(width)
    return obj.move_to([x, y, 0])


def arrow(a, b, color=MUTED, width=3):
    return Arrow([*a, 0], [*b, 0], buff=0.08, color=color,
                 stroke_width=width, max_tip_length_to_length_ratio=0.12)


def box(x, y, w, h, color=BLUE):
    return RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            stroke_color=color, stroke_width=2,
                            fill_color=PALE, fill_opacity=0.6).move_to([x, y, 0])


def heading(scene, title, subtitle):
    scene.add(label(title, 0, 3.7, 36), label(subtitle, 0, 3.03, 23, MUTED, 14.5))


class PhotonPolarizations(Scene):
    def construct(self):
        heading(self, 'Four potential components, two photon polarizations',
                'A free wave moving along z: k = (E, 0, 0, E)')
        specs = [(-5, r'(\varepsilon^0,\varepsilon^1,\varepsilon^2,\varepsilon^3)',
                  '4 amplitudes', 'Start with the potential'),
                 (0, r'(a,\varepsilon^1,\varepsilon^2,a)',
                  '3 amplitudes', 'Time and z components agree'),
                 (5, r'(0,\varepsilon^1,\varepsilon^2,0)',
                  '2 physical amplitudes', 'Remove the shared gauge part')]
        for x, formula, count, detail in specs:
            self.add(box(x, 1.05, 4.25, 1.65), math(formula, x, 1.35, width=3.9),
                     label(count, x, 0.65, 23, BLUE), label(detail, x, -0.2, 20, MUTED, 4.4))
        self.add(arrow((-2.85, 1), (-2.2, 1)), arrow((2.2, 1), (2.85, 1)))
        self.add(label('Maxwell constraint', -2.5, 2.55, 21),
                 math(r'k\cdot\varepsilon=0', -2.5, 2.12, 26),
                 label('Gauge transformation', 2.5, 2.55, 21),
                 math(r'\varepsilon\to\varepsilon-(a/E)k', 2.5, 2.12, 26))
        # A spatial sketch only: no Euclidean picture of Minkowski orthogonality.
        origin = (1.5, -2.45)
        self.add(arrow(origin, (5.3, -2.45), MUTED), label('z: propagation', 5.25, -2.95, 22),
                 arrow(origin, (1.5, -0.9), BLUE), label('x polarization', 0.0, -1.0, 22, BLUE),
                 arrow(origin, (0.15, -3.3), TEAL), label('y polarization', -1.2, -3.45, 22, TEAL),
                 label('Spatial view', -4.6, -1.65, 25),
                 label('Both physical directions\nare perpendicular to z.', -4.6, -2.55, 24, MUTED))


class GaugeDescriptions(Scene):
    def construct(self):
        heading(self, 'Different potentials can describe the same field',
                'Schematic space of field configurations; positions here are not spacetime coordinates')
        self.add(Ellipse(width=7.1, height=4.6, color=BLUE, fill_color=PALE,
                         fill_opacity=0.5).move_to([-3.55, -0.2, 0]))
        self.add(label('One gauge orbit', -3.55, 1.6, 27, BLUE),
                 label('Equivalent descriptions', -3.55, 1.1, 22, MUTED))
        pts = [(-5.8, 0.1), (-3.8, -0.2), (-2.2, -1.3)]
        for pos in pts:
            self.add(Dot([*pos, 0], color=BLUE, radius=0.09))
        self.add(math(r'A_\mu', -5.75, 0.55, 30),
                 math(r'A_\mu+\partial_\mu\chi', -3.6, 0.3, 30),
                 math(r'A_\mu+\partial_\mu\widetilde\chi', -2.8, -1.85, 30))
        self.add(Line([-5.8, -1.15, 0], [-1.0, -0.6, 0], color=TEAL, stroke_width=3))
        for x, y in [(-5.1, -1.07), (-4.0, -0.944)]:
            self.add(Dot([x, y, 0], color=TEAL, radius=0.1))
        self.add(label('Lorenz representatives', -4.7, -2.9, 23, TEAL),
                 math(r'\partial\cdot A=0', -4.7, -3.45, 30, TEAL))
        self.add(arrow((0.25, 0), (2.1, 0), BLUE), box(4.65, 0, 4.8, 2.6, TEAL),
                 label('The same electromagnetic field', 4.65, 0.85, 24, TEAL, 4.35),
                 math(r'F_{\mu\nu}', 4.65, 0.05, 48, TEAL),
                 math(r'\mathbf E,\quad\mathbf B', 4.65, -0.75, 36, TEAL),
                 label('Residual freedom remains', 3.6, -2.7, 26),
                 math(r'A\to A+\partial\chi,\qquad\Box\chi=0', 3.6, -3.4, 30))


class PhotonQuantizationRoute(Scene):
    def construct(self):
        heading(self, 'Quantize four modes, then select physical states',
                'Gauge fixing and the physical-state restriction work together')
        steps = [(-5, 1.1, '1. Maxwell field', r'\pi^0=0', 'A zero momentum blocks\nthe independent canonical pairing.'),
                 (0, 1.1, '2. Add gauge fixing', r'-\tfrac12(\partial\cdot A)^2', 'Every component now\nhas a conjugate momentum.'),
                 (5, 1.1, '3. Quantize the modes', r'c_0,\ c_1,\ c_2,\ c_3', 'Timelike, two transverse,\nand longitudinal modes.'),
                 (5, -2.05, '4. Select physical states', r'(c_0-c_3)|\mathrm{phys}\rangle=0', 'Gupta–Bleuler condition\n(shown for momentum along z).'),
                 (-1, -2.05, '5. Identify null gauge states', r'\varepsilon^{(1)},\quad\varepsilon^{(2)}', 'States differing by a null gauge state\nrepresent the same physical state.')]
        for x, y, title, formula, text in steps:
            w = 4.3 if x != -1 else 6.2
            self.add(box(x, y, w, 2.35, TEAL if y < 0 else BLUE),
                     label(title, x, y+0.72, 23, width=w-0.3),
                     math(formula, x, y+0.02, 31, width=w-0.4),
                     label(text, x, y-0.72, 20, MUTED, w-0.3))
        self.add(arrow((-2.8, 1.1), (-2.2, 1.1)), arrow((2.2, 1.1), (2.8, 1.1)),
                 arrow((5, -0.12), (5, -0.8)), arrow((2.8, -2.05), (2.2, -2.05)),
                 label('Two physical\npolarizations', -5.6, -2.1, 29, TEAL))


class FieldModes(Scene):
    def construct(self):
        heading(self, 'A spatial field profile is a sum of modes',
                'One snapshot of a real field; each mode evolves as a harmonic oscillator')
        xs = np.linspace(-np.pi, np.pi, 250)
        functions = [lambda x: 0.9*np.sin(x), lambda x: 0.48*np.sin(2*x),
                     lambda x: 0.28*np.cos(3*x)]
        colors = [BLUE, TEAL, ORANGE]
        def plot(fn, cx, cy, w, h, color):
            self.add(Line([cx-w/2, cy, 0], [cx+w/2, cy, 0], color='#bdc8d7'))
            points = [[cx+x/np.pi*w/2, cy+fn(x)*h, 0] for x in xs]
            self.add(VMobject(color=color, stroke_width=4).set_points_smoothly(points))
        plot(lambda x: sum(fn(x) for fn in functions), -4.45, 0.0, 5.5, 1.1, INK)
        self.add(label('Combined profile', -4.45, 1.9, 28), math(r'\phi(t_0,x)', -4.45, 1.28),
                 label('position x', -2.5, -0.4, 20, MUTED),
                 label('Illustrative Fourier amplitudes', -4.45, -2.4, 23, MUTED),
                 math(r'\phi(t_0,x)=\sum_n q_n(t_0)f_n(x)', -4.45, -3.0, 29),
                 math('=', -0.75, 0, 52))
        for i, (fn, color) in enumerate(zip(functions, colors)):
            y = 1.5-i*1.85
            plot(fn, 2.2, y, 4.4, 0.65, color)
            self.add(label('Mode '+str(i+1), 1, y+0.62, 21, color),
                     math(r'q_'+str(i+1)+r'(t)', 5.6, y+0.2, 32, color),
                     math(r'\omega_'+str(i+1)+r'=E_'+str(i+1)+r'/\hbar', 5.6, y-0.38, 28, color))
            if i < 2:
                self.add(math('+', 2.2, y-0.94, 30, MUTED))
        self.add(label('mode coordinate and frequency', 5.15, -3.7, 21, MUTED, 4.7))


class ContractionsToDiagram(Scene):
    def construct(self):
        heading(self, 'A field contraction becomes an internal line',
                'Second order in a cubic scalar interaction: six fields, four external attachments')
        self.add(label('Operator product', -4.2, 2.15, 27),
                 label('The same connections as a graph', 3.8, 2.15, 27))
        for x, tag, color in [(-5.9, 'x', BLUE), (-2.8, 'y', TEAL)]:
            for i in range(3):
                self.add(math(r'\phi('+tag+')', x, 0.9-i*1.0, 34, color))
        self.add(Line([-5.3, -1.1, 0], [-3.4, -1.1, 0], color=PURPLE, stroke_width=5),
                 math(r'\langle0|T\phi(x)\phi(y)|0\rangle', -4.3, -2.15, 28, PURPLE),
                 label('One contracted pair', -4.3, -2.8, 23, PURPLE))
        for y, tag in [(0.9, 'p_1'), (-0.1, 'p_2')]:
            self.add(arrow((-7.25,y),(-6.5,y),BLUE),math(tag,-7.2,y+0.34,24,BLUE))
        for y, tag in [(0.9, 'p_3'), (-0.1, 'p_4')]:
            self.add(arrow((-2.2,y),(-1.3,y),TEAL),math(tag,-1.5,y+0.34,24,TEAL))
        self.add(arrow((-0.7,-0.3),(0.4,-0.3)))
        a=np.array([2.2,-0.3,0]); b=np.array([5.0,-0.3,0])
        for end,tag in [(np.array([0.95,1.05,0]),'p_1'),(np.array([0.95,-1.6,0]),'p_2')]:
            self.add(Line(end,a,color=BLUE,stroke_width=4),math(tag,end[0]-0.25,end[1],26,BLUE))
        for end,tag in [(np.array([6.6,1.05,0]),'p_3'),(np.array([6.6,-1.6,0]),'p_4')]:
            self.add(Line(b,end,color=TEAL,stroke_width=4),math(tag,end[0]+0.3,end[1],26,TEAL))
        self.add(Line(a,b,color=PURPLE,stroke_width=5),Dot(a,color=INK),Dot(b,color=INK),
                 math('x',2.2,0.15,28),math('y',5,0.15,28),
                 math(r'\frac{i}{r^2-m^2+i\epsilon}',3.6,-2.35,35,PURPLE),
                 label('Propagator in momentum space',3.6,-3.05,23,PURPLE),
                 label('This shows one pairing. Add the other allowed pairings to obtain the amplitude.',0,-3.95,23,MUTED,14.5))


class StateAndField(Scene):
    def construct(self):
        heading(self, 'An operator changes a state',
                'Bosonic occupation numbers: each dot is one quantum of a momentum mode')
        def state(cx, npart):
            self.add(box(cx,1.05,3.5,2.45))
            for dx,name,n in [(-0.75,'p',npart),(0.75,'q',1)]:
                self.add(Line([cx+dx-0.4,0.55,0],[cx+dx+0.4,0.55,0],color=MUTED),
                         math(name,cx+dx,0.15,28))
                for i in range(n):
                    self.add(Dot([cx+dx,0.92+i*0.42,0],radius=0.12,color=BLUE if name=='p' else TEAL))
        state(-5,1);state(5,2)
        self.add(math(r'|1_p,1_q\rangle',-5,2.55),math(r'\sqrt{2}\,|2_p,1_q\rangle',5,2.55),
                 arrow((-3.1,1),(3.1,1)),math(r'\hat a_p^\dagger',0,1.7,46,ORANGE),
                 label('Add one quantum in mode p',0,0.4,24),
                 label('The square-root factor is the bosonic normalization.',0,-0.65,24,MUTED),
                 box(0,-2.4,12.5,2.0,TEAL),
                 math(r'\hat\phi(x)=\sum_p\left[f_p(x)\hat a_p+f_p^*(x)\hat a_p^\dagger\right]',0,-2.05,36,TEAL),
                 label('A field operator combines many modes, with coefficients depending on spacetime x.',0,-2.95,23,MUTED,11.9),
                 label('Discrete, normalized modes shown; a continuum uses a momentum integral.',0,-3.85,22,MUTED))


class AmplitudeInterference(Scene):
    def construct(self):
        heading(self, 'Add amplitudes before taking the squared magnitude',
                'Illustrative complex amplitudes for one fixed choice of external spins and polarizations')
        origin=np.array([-5.8,-1.4,0]); scale=1.25
        s=np.array([2,0.6,0])*scale; u=np.array([-0.5,1.1,0])*scale
        self.add(arrow((-6.4,-1.4),(-0.5,-1.4)),arrow((-5.8,-2.1),(-5.8,2.1)),
                 label('Re',-0.6,-1.85,23,MUTED),label('Im',-6.35,2.1,23,MUTED))
        for start,end,color in [(origin,origin+s,BLUE),(origin+s,origin+s+u,TEAL),(origin,origin+s+u,ORANGE)]:
            self.add(Arrow(start,end,buff=0,color=color,stroke_width=5))
        self.add(math(r'\mathcal M_s',-4.1,-1.9,31,BLUE),
                 math(r'\mathcal M_u',-2.6,0.3,31,TEAL),
                 math(r'\mathcal M_s+\mathcal M_u',-3.8,1.7,30,ORANGE),
                 label('Place the second arrow\nat the tip of the first.',-3.6,-2.8,24,MUTED),
                 math(r'|\mathcal M_s+\mathcal M_u|^2',3.5,1.6,39,ORANGE),
                 math(r'=|\mathcal M_s|^2+|\mathcal M_u|^2',3.5,0.65,34),
                 math(r'+\,2\operatorname{Re}(\mathcal M_s\mathcal M_u^*)',3.5,-0.25,34,PURPLE),
                 box(3.5,-2.1,6.1,1.8,PURPLE),
                 label('The extra term is interference.',3.5,-1.75,25,PURPLE,5.7),
                 label('Its sign depends on the relative phase.\nHere it is negative: partial cancellation.',3.5,-2.45,22,MUTED,5.7),
                 label('These arrows are amplitudes, not particle trajectories or spatial momenta.',0,-3.85,23,MUTED))


class OscillatorApproximation(Scene):
    def construct(self):
        heading(self, 'Near a stable minimum, the potential is almost quadratic',
                'The constant shifts the energy reference; the curvature sets the restoring force')
        ax = Axes(x_range=[-2.1,2.1,1], y_range=[0,5,1], x_length=6.8, y_length=4.7,
                  tips=False, axis_config={'color':MUTED,'include_ticks':False}).move_to([-3.85,-0.5,0])
        self.add(ax, ax.plot(lambda u:u*u+0.18*u**3+0.15*u**4,x_range=[-1.8,1.6],color=BLUE),
                 ax.plot(lambda u:u*u,x_range=[-2,2],color=ORANGE),
                 Dot(ax.c2p(0,0),color=INK,radius=0.08),
                 label('displacement from equilibrium',-3.85,-3.3,23,MUTED),
                 math(r'x-x_0',-3.85,-3.8,29),label('Potential',-6.55,2.15,24,MUTED))
        # Highlight the small-displacement region without claiming a global fit.
        self.add(DashedLine(ax.c2p(-0.65,0),ax.c2p(-0.65,1.25),color=TEAL),
                 DashedLine(ax.c2p(0.65,0),ax.c2p(0.65,1.25),color=TEAL),
                 label('Local agreement',-3.85,-1.2,22,TEAL).add_background_rectangle(color=WHITE,opacity=1,buff=0.06),
                 label('Example smooth potential',3.7,1.9,27,BLUE),
                 label('Quadratic approximation',3.7,1.25,27,ORANGE),
                 box(3.7,-0.35,6.4,1.7,ORANGE),
                 math(r'V(x)-V(x_0)\approx\tfrac12 k(x-x_0)^2',3.7,-0.1,31,ORANGE,width=6),
                 math(r'k=V^{\prime\prime}(x_0)>0',3.7,-0.8,31),
                 math(r'F\approx-k(x-x_0)',3.7,-2.05,35),
                 label('Displace to the right: force points left.\nDisplace to the left: force points right.',3.7,-3.05,24,MUTED,width=6.5))


class ClassicalOscillatorEnergy(Scene):
    def construct(self):
        heading(self, 'One classical orbit, with energy changing form',
                'Scaled coordinates X and P make the constant-energy ellipse a circle')
        ax=Axes(x_range=[-1.4,1.4,1],y_range=[-1.4,1.4,1],x_length=4.7,y_length=4.7,
                tips=True,axis_config={'color':MUTED,'include_ticks':False}).move_to([-4.3,-0.35,0])
        radius=4.7/2.8
        self.add(ax,Circle(radius=radius,color=BLUE,stroke_width=4).move_to(ax.c2p(0,0)),
                 math('X',-1.65,-0.75,30),math('P',-4.75,2.25,30))
        for x,y,tag in [(1,0,'A'),(0,-1,'B'),(-1,0,'C'),(0,1,'D')]:
            pos=ax.c2p(x,y)
            self.add(Dot(pos,color=BLUE,radius=0.09),label(tag,pos[0]+(0.35 if x==0 else 0.25*x),pos[1]+(0.3 if y==0 else 0.27*y),23,BLUE))
        for theta in [np.pi/4,5*np.pi/4]:
            p1=ax.c2p(np.cos(theta+0.17),np.sin(theta+0.17))
            p2=ax.c2p(np.cos(theta-0.17),np.sin(theta-0.17))
            self.add(Arrow(p1,p2,buff=0,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.45))
        self.add(math(r'X=\sqrt{m\omega}\,x,\quad P=p/\sqrt{m\omega}',-4.2,-3.2,28),
                 math(r'H=\tfrac{\omega}{2}(X^2+P^2)',-4.2,-3.8,30))
        self.add(label('Potential energy',2.15,2.2,24,ORANGE),label('Kinetic energy',5.35,2.2,24,TEAL))
        for y,tag,detail,pot,kin in [(1.35,'A, C','Turning points',1,0),(-0.1,'B, D','Passing equilibrium',0,1),(-1.55,'Example','Equal energy split',0.5,0.5)]:
            self.add(label(tag,0.15,y,24,BLUE),label(detail,3.65,y+0.4,22,MUTED))
            for x,value,color in [(2.15,pot,ORANGE),(5.35,kin,TEAL)]:
                self.add(Rectangle(width=2.6,height=0.32,stroke_color='#ccd5df',fill_color=PALE,fill_opacity=1).move_to([x,y-0.18,0]))
                if value:
                    self.add(Rectangle(width=2.6*value,height=0.32,stroke_width=0,fill_color=color,fill_opacity=1).move_to([x-1.3+1.3*value,y-0.18,0]))
        self.add(label('The two energies always add to the same H.',3.5,-3.1,25,width=7))


class OscillatorLadder(Scene):
    def construct(self):
        heading(self, 'Ladder operators connect equally spaced energy levels',
                'Energy is vertical; the arrows show changes of state, not motion through space')
        for n in range(5):
            y=-2.65+n*1.05
            self.add(Line([-6.1,y,0],[-1.7,y,0],color=BLUE,stroke_width=3),
                     math(r'|'+str(n)+r'\rangle',-6.75,y,30,BLUE),
                     math(r'\tfrac{'+str(2*n+1)+r'}{2}\hbar\omega',-0.8,y,29))
        self.add(DashedLine([-6.1,-3.18,0],[-1.7,-3.18,0],color=MUTED),
                 label('zero energy',-3.9,-3.65,22,MUTED),
                 arrow((-4.7,-0.49),(-4.7,0.45),TEAL),
                 arrow((-3.1,0.45),(-3.1,-0.49),ORANGE),
                 math(r'\hat a^\dagger',-5.2,0.0,36,TEAL),math(r'\hat a',-2.65,0.0,36,ORANGE),
                 math(r'\Delta E=\hbar\omega',-3.9,2.22,32))
        self.add(math(r'\hat a^\dagger|n\rangle=\sqrt{n+1}|n+1\rangle',3.8,1.6,34,TEAL,width=6.2),
                 label('Add one quantum of excitation',3.8,0.95,24,TEAL),
                 math(r'\hat a|n\rangle=\sqrt n\,|n-1\rangle',3.8,-0.15,34,ORANGE,width=6.2),
                 label('Remove one quantum of excitation',3.8,-0.8,24,ORANGE),
                 box(3.8,-2.4,6.2,1.7),math(r'\hat a|0\rangle=0,\qquad E_0=\tfrac12\hbar\omega',3.8,-2.1,32,width=5.8),
                 label('The zero vector is not a lower-energy state.',3.8,-2.92,22,MUTED,width=5.8))


class OscillatorGroundState(Scene):
    def construct(self):
        heading(self, 'The ground state has a finite spread in position and momentum',
                'These are probability densities for repeated measurements on identically prepared ground states')
        for cx,symbol,width_eq,color in [(-3.9,'x',r'\Delta x=\sqrt{\frac{\hbar}{2m\omega}}',BLUE),
                                          (3.9,'p',r'\Delta p=\sqrt{\frac{m\hbar\omega}{2}}',TEAL)]:
            ax=Axes(x_range=[-3.2,3.2,1],y_range=[0,0.5,0.1],x_length=6.2,y_length=2.8,
                    tips=False,axis_config={'color':MUTED,'include_ticks':False}).move_to([cx,0.6,0])
            curve=ax.plot(lambda u:np.exp(-u*u/2)/np.sqrt(2*np.pi),color=color)
            self.add(ax,ax.get_area(curve,x_range=[-1,1],color=color,opacity=0.14),curve,
                     label('Position' if symbol=='x' else 'Momentum',cx,2.32,27,color),
                     math('0',*ax.c2p(0,0)[:2]+np.array([0,-0.25]),size=25))
            for u in [-1,1]:
                pt=ax.c2p(u,np.exp(-0.5)/np.sqrt(2*np.pi))
                self.add(DashedLine(ax.c2p(u,0),pt,color=color),
                         math(('-' if u<0 else '+')+r'\Delta '+symbol,pt[0],ax.c2p(0,0)[1]-0.45,25,color))
            self.add(math(width_eq,cx,-1.95,35,color),
                     label('Dashed lines mark one standard deviation.',cx,-2.68,21,MUTED,width=6.8))
        self.add(math(r'\Delta x\,\Delta p=\tfrac{\hbar}{2},\qquad E_0=\tfrac12\hbar\omega',0,-3.55,35),
                 label('The distributions stay constant in time; they do not describe a classical trajectory.',0,-4.1,21,MUTED,width=14.5))

"""Page-by-page static diagrams; pnpm docs:manim --page <chapter-slug>."""
from manim import *
import numpy as np
from concept_diagrams import label, math, arrow, box, heading, INK, MUTED, BLUE, TEAL, ORANGE, PURPLE, PALE
config.background_color = WHITE
config.frame_width = 16
config.frame_height = 9


def axes_at(cx,cy,w=5.8,h=3.9,xr=(-3,3,1),yr=(-2,2,1)):
    return Axes(x_range=list(xr),y_range=list(yr),x_length=w,y_length=h,tips=False,
                axis_config={'color':'#9aaabb','include_ticks':False}).move_to([cx,cy,0])


def path_curve(ax, fn, interval, color=BLUE):
    return ax.plot(fn,x_range=interval,color=color,stroke_width=4)


class NewtonMotion(Scene):
    def construct(self):
        heading(self,'A constant force changes momentum and bends the trajectory','One-dimensional example: constant positive force, with the particle initially at rest')
        for cx,title,fn,formula in [(-5,'Acceleration',lambda t:1,r'a=F/m'),(0,'Velocity',lambda t:t,r'v(t)=at'),(5,'Position',lambda t:0.5*t*t,r'x(t)=x_0+\tfrac12at^2')]:
            ax=axes_at(cx,-0.1,4.1,3.5,(0,2,1),(0,2.3,1))
            self.add(ax,path_curve(ax,fn,[0,2]),label(title,cx,2.15,28),math(formula,cx,-2.6,31),label('time',cx+1.5,-2.08,22,MUTED))
        self.add(label('Integrate acceleration to get velocity; integrate velocity to get position.',0,-3.65,26,MUTED))


class StationaryActionPaths(Scene):
    def construct(self):
        heading(self,'Stationary action compares complete paths','Free particle with fixed endpoints; the straight path has constant velocity')
        ax=axes_at(-4,0,6.2,4.4,(0,1,1),(0,1.2,1))
        self.add(ax)
        for e,c in [(-0.25,ORANGE),(0.25,TEAL),(0,BLUE)]:
            self.add(path_curve(ax,lambda t,e=e:t+e*np.sin(np.pi*t),[0,1],c))
        for t in [0,1]:self.add(Dot(ax.c2p(t,t),color=INK,radius=0.09))
        self.add(label('time t',-1.25,-2.6,23),label('position x',-5.8,2.5,23),
                 math(r'x_\epsilon(t)=t+\epsilon\sin(\pi t)',-4,-3.25,31),
                 label('All paths share the endpoints.',-4,-3.9,23,MUTED))
        ax2=axes_at(4,0,5.7,3.3,(-1,1,1),(0,2,1));self.add(ax2,path_curve(ax2,lambda e:0.4+e*e,[-1,1],PURPLE),
                 label('Action S',2,2.15,25,PURPLE),label('path variation ε',4,-2.2,24),
                 math(r'\left.\frac{dS}{d\epsilon}\right|_{\epsilon=0}=0',4,-3,34,PURPLE),
                 label('Here the stationary action is a minimum.',4,-3.8,22,MUTED,width=6.8))


class PhaseSpaceStates(Scene):
    def construct(self):
        heading(self,'Position alone does not specify a classical state','Two oscillators can pass the same position while moving in opposite directions')
        ax=axes_at(-4,0,5.4,4.5,(-1.4,1.4,1),(-1.4,1.4,1));self.add(ax)
        self.add(Ellipse(width=5.4/1.4,height=4.5/1.4,color=BLUE).move_to(ax.c2p(0,0)))
        for y,c,tag in [(1,TEAL,'A: moving right'),(-1,ORANGE,'B: moving left')]:
            pt=ax.c2p(0,y);self.add(Dot(pt,color=c,radius=.11),label(tag,pt[0]+1.9,pt[1],23,c,width=3.1))
        self.add(label('momentum p',-5.5,2.65,24),label('position x',-1.8,-.4,23),
                 box(4,0,6,3.5),math(r'A=(0,+p_0)',4,.9,38,TEAL),math(r'B=(0,-p_0)',4,-.1,38,ORANGE),
                 label('Same position. Different states.',4,-1.1,25),
                 label('A point in phase space specifies both position and momentum.',0,-3.5,28,MUTED))


class BornDensity(Scene):
    def construct(self):
        heading(self,'A wave amplitude becomes a probability density','Illustrative real wave function: negative amplitudes still give positive probabilities')
        ax=axes_at(-4,0,6,3.8,(-3,3,1),(-1.1,1.1,1));self.add(ax)
        fn=lambda x:np.exp(-x*x/3)*np.cos(2*x)
        self.add(path_curve(ax,fn,[-3,3],BLUE),label('Amplitude ψ(x)',-4,2.3,29,BLUE),label('position x',-1.8,-.4,22))
        ax2=axes_at(4,0,6,3.8,(-3,3,1),(0,1.1,.5));curve=path_curve(ax2,lambda x:fn(x)**2,[-3,3],TEAL)
        self.add(ax2,ax2.get_area(curve,x_range=[.2,1.0],color=TEAL,opacity=.23),curve,
                 label('Density |ψ(x)|²',4,2.3,29,TEAL),label('position x',6,-2.2,22),
                 math(r'P(a<x<b)=\int_a^b|\psi(x)|^2\,dx',4,-3.05,31,TEAL),
                 label('Shade an interval to calculate its probability.',4,-3.8,23,MUTED,width=7))
        self.add(label('Square the magnitude, then normalize\nso the total area under the density is one.',-4,-3.05,24,MUTED,width=6.8))


class EigenbasisProbabilities(Scene):
    def construct(self):
        heading(self,'The chosen eigenbasis determines the measurement amplitudes','A two-level example with real coefficients; general coefficients can be complex')
        origin=(-6,-1.5)
        self.add(arrow(origin,(-1,-1.5)),arrow(origin,(-6,2)),
                 arrow(origin,(-2.54,.5),BLUE),
                 DashedLine([-2.54,.5,0],[-2.54,-1.5,0],color=TEAL),
                 DashedLine([-6,.5,0],[-2.54,.5,0],color=ORANGE),
                 math(r'|0\rangle',-1,-2,30),math(r'|1\rangle',-6.5,2.1,30),math(r'|\psi\rangle',-2.2,1,34,BLUE),
                 math(r'\sqrt3/2',-4.2,-2.05,30,TEAL),math(r'1/2',-6.7,-.4,30,ORANGE))
        for x,prob,name,c in [(2.5,.75,'0',TEAL),(5.5,.25,'1',ORANGE)]:
            self.add(Rectangle(width=1.5,height=3.2*prob,fill_color=c,fill_opacity=.8,stroke_width=0).move_to([x,-1.5+1.6*prob,0]),
                     math(name,x,-1.9,28),label(str(int(100*prob))+'%',x,-1.5+3.2*prob+.3,25,c))
        self.add(label('Measurement probabilities',4,2.3,28),
                 math(r'|\psi\rangle=\tfrac{\sqrt3}{2}|0\rangle+\tfrac12|1\rangle',0,-3,35),
                 label('Project onto each eigenstate, then square the amplitude’s magnitude.',0,-3.85,25,MUTED))


class FourierUncertainty(Scene):
    def construct(self):
        heading(self,'Localizing a wave packet broadens its momentum distribution','Gaussian packets: narrowing the position spread increases the momentum spread')
        for y,sigma,c,tag in [(1,.48,BLUE,'Narrow in position'),(-1.25,1.2,TEAL,'Broad in position')]:
            for x,width in [(-4,sigma),(4,1/sigma)]:
                ax=axes_at(x,y,5.8,1.5,(-4,4,1),(0,1.2,1))
                self.add(ax,path_curve(ax,lambda u,w=width:np.exp(-u*u/(2*w*w)),[-4,4],c))
            self.add(label(tag,0,y+.25,21,c,width=2.1))
        self.add(label('Position density',-4,2.55,28),label('Momentum density',4,2.55,28),
                 math(r'\Delta x\,\Delta p\geq\hbar/2',0,-3.2,38),
                 label('Horizontal scales are fixed within each column; peak heights are rescaled for comparison.',0,-4,22,MUTED,width=14.5))


class LightConeIntervals(Scene):
    def construct(self):
        heading(self,'The interval classifies which events can be causally connected','Events are measured relative to the origin; c = 1, with x vertical and t horizontal')
        center=np.array([-4,-.2,0])
        self.add(Polygon(center,center+[2.4,2.4,0],center+[2.4,-2.4,0],fill_color=BLUE,fill_opacity=.1,stroke_width=0))
        for sign in [-1,1]:self.add(DashedLine(center+[-2.4,-2.4*sign,0],center+[2.4,2.4*sign,0],color=ORANGE))
        self.add(arrow((-6.6,-.2),(-1.3,-.2)),arrow((-4,-2.8),(-4,2.4)),math('t',-1.25,-.6,28),math('x',-4.4,2.45,28))
        for pt,c,tag in [([1.8,.5,0],BLUE,'T'),([1.4,1.4,0],ORANGE,'L'),([.4,2,0],TEAL,'S')]:
            pos=center+pt;self.add(Dot(pos,color=c,radius=.1),label(tag,pos[0]+.25,pos[1]+.2,24,c))
        for y,title,formula,desc,c in [(1.7,'T: timelike',r'\Delta t^2-\Delta x^2>0','A slower-than-light signal can connect the events.',BLUE),
             (0,'L: lightlike',r'\Delta t^2-\Delta x^2=0','A light signal connects the events.',ORANGE),
             (-1.7,'S: spacelike',r'\Delta t^2-\Delta x^2<0','No signal at or below c can connect the events.',TEAL)]:
            self.add(label(title,3.6,y+.45,26,c),math(formula,3.6,y-.1,31),label(desc,3.6,y-.65,21,MUTED,width=7.5))
        self.add(label('Future timelike events lie inside the right-hand cone; the left-hand cone is the past.',0,-3.85,24,MUTED,width=14.5))


class RelativeSimultaneity(Scene):
    def construct(self):
        heading(self,'Simultaneous events in one frame need not be simultaneous in another','Two events at t = 1 have different positions; use v = 0.5 and c = 1')
        origin=np.array([-5.8,-.1,0]);scale=1.6
        def pt(t,x):return origin+scale*np.array([t,x,0])
        self.add(Line(pt(0,-1.5),pt(0,1.5),color=MUTED),Line(pt(0,0),pt(2.6,0),color=MUTED),
                 Line(pt(1,-1.4),pt(1,1.4),color=BLUE,stroke_width=4))
        for x,tag,c in [(1,'A',TEAL),(-1,'B',ORANGE)]:
            pos=pt(1,x);self.add(Dot(pos,color=c,radius=.11),label(tag,pos[0]-.3,pos[1]+.2,26,c),
                DashedLine(pt(1+.5*(-1.35-x),-1.35),pt(1+.5*(1.35-x),1.35),color=c))
        self.add(math('x',-6.2,2.45,28),math('t',-1.5,-.5,28),label('t = 1',-4.2,2.5,25,BLUE),
                 math(r"t'=\gamma(t-vx)",3.6,1.8,40),
                 math(r"t'_A=\gamma(1-0.5)=\gamma/2",3.6,.5,33,TEAL),
                 math(r"t'_B=\gamma(1+0.5)=3\gamma/2",3.6,-.7,33,ORANGE),
                 label('A occurs before B in the primed frame.',3.6,-1.9,25,width=7),
                 label('Dashed lines have constant t′. Their tilt changes which events share a time coordinate.',0,-3.65,24,MUTED,width=14.5))


class RelativisticEnergySolutions(Scene):
    def construct(self):
        heading(self,'The relativistic wave equation admits both energy signs','Illustrative units m = c = 1; momentum is horizontal and energy is vertical')
        ax=axes_at(-3.8,0,6.2,5,(-2.5,2.5,1),(-3,3,1))
        self.add(ax,path_curve(ax,lambda p:np.sqrt(1+p*p),[-2.5,2.5],BLUE),path_curve(ax,lambda p:-np.sqrt(1+p*p),[-2.5,2.5],ORANGE),
                 label('E',-4.2,2.7,26),label('p',-.4,-.35,26),
                 math(r'+mc^2',-5.15,.85,26,BLUE),math(r'-mc^2',-5.15,-.85,26,ORANGE),
                 math(r'E=+\sqrt{p^2c^2+m^2c^4}',3.65,1.6,34,BLUE,width=6.8),
                 math(r'E=-\sqrt{p^2c^2+m^2c^4}',3.65,-.05,34,ORANGE,width=6.8),
                 label('The negative-energy values\nhave no lower bound.',3.65,-1.55,27,ORANGE),
                 label('Field quantization reinterprets negative-frequency modes as positive-energy antiparticle creation.',0,-3.75,23,MUTED,width=14.6))


class KleinGordonDensity(Scene):
    def construct(self):
        heading(self,'A conserved density is not automatically a probability density','For a Klein–Gordon plane wave, the current density has the sign of its energy')
        for x,sign,c in [(-4,'+',BLUE),(4,'-',ORANGE)]:
            self.add(box(x,0,6.6,4,c),math(r'\psi\propto e^{'+('-' if sign=='+' else '+')+r'iE_pt/\hbar}',x,1.25,36,c),
                     math(r'E='+sign+r'E_p',x,.3,35),math(r'\rho='+sign+r'\frac{2E_p}{\hbar}|\psi|^2',x,-.85,38,c),
                     label('Positive conserved density' if sign=='+' else 'Negative conserved density',x,-2.6,25,c))
        self.add(label('Probability must be nonnegative. Charge density can have either sign.',0,-3.65,28,MUTED))


class DiracLinearization(Scene):
    def construct(self):
        heading(self,'Linearizing the energy relation requires matrices','Matching the squared Hamiltonian removes mixed terms and fixes the matrix algebra')
        self.add(box(-4.5,.75,5.5,2.4),math(r'H=\boldsymbol\alpha\cdot\mathbf p+\beta m',-4.5,1.05,34,width=5.1),
                 label('First order in momentum',-4.5,.05,25,BLUE),arrow((-1.65,.75),(.25,.75)),label('square',-.7,1.3,23),
                 box(3.8,.75,6.8,2.4,TEAL),math(r'H^2=\mathbf p^2+m^2',3.8,1.05,38,TEAL),label('Correct relativistic dispersion',3.8,.05,25,TEAL),
                 math(r'\{\alpha_i,\alpha_j\}=2\delta_{ij},\quad\{\alpha_i,\beta\}=0,\quad\beta^2=1',0,-1.6,33),
                 label('Ordinary numbers cannot satisfy all these conditions.',0,-2.65,27),
                 label('The smallest complex matrices are 4 × 4, so the wave function has four components.',0,-3.55,25,MUTED,width=14.3))


class SpinMeasurement(Scene):
    def construct(self):
        heading(self,'A spin-½ measurement along one axis has two outcomes','An ideal spin analyzer measures a component of angular momentum, not a tiny rotating ball')
        self.add(math(r'|\psi\rangle=\tfrac1{\sqrt2}(|+z\rangle+|-z\rangle)',-4.5,1.4,32,width=6),
                 arrow((-7,0),(-1.5,0),BLUE),box(0,0,2.6,2.6),label('Measure',0,.45,26),math(r'S_z',0,-.3,38),
                 arrow((1.4,0),(4.2,1.65),TEAL),arrow((1.4,0),(4.2,-1.65),ORANGE),
                 math(r'+\hbar/2',5.5,1.8,38,TEAL),label('50% of outcomes',5.5,1.05,24,TEAL),
                 math(r'-\hbar/2',5.5,-1.5,38,ORANGE),label('50% of outcomes',5.5,-2.25,24,ORANGE),
                 label('The chosen state fixes the probabilities; the operator fixes the possible values.',0,-3.65,26,MUTED,width=14.5))


class SpinorRotationSign(Scene):
    def construct(self):
        heading(self,'A 2π rotation changes a spinor’s sign; 4π restores it','Track the phase of a spin-up component under a rotation about z')
        for x,theta,phase,direction in [(-5,'0','1',1),(0,r'2\pi','-1',-1),(5,r'4\pi','1',1)]:
            self.add(Circle(radius=1.1,color='#b8c6d4').move_to([x,.2,0]),
                     arrow((x,.2),(x+direction*.95,.2),BLUE),math(r'\theta='+theta,x,2,32),
                     math(r'e^{-i\theta/2}='+phase,x,-1.7,33,BLUE),math(('' if direction==1 else '-')+r'|\uparrow\rangle',x,-2.5,33))
        self.add(label('A common sign does not change probabilities. Interference can compare it with a reference.',0,-3.85,24,MUTED,width=14.5))


class RestSpinorBasis(Scene):
    def construct(self):
        heading(self,'At rest, the Dirac basis separates into two pairs','Standard Dirac representation; overall spinor normalization is omitted')
        for x,vals,name,c in [(-5.4,[1,0,0,0],'u_1',BLUE),(-1.8,[0,1,0,0],'u_2',BLUE),(1.8,[0,0,1,0],'v_1',ORANGE),(5.4,[0,0,0,1],'v_2',ORANGE)]:
            self.add(math(name,x,1.9,34,c))
            for i,v in enumerate(vals):
                self.add(Square(side_length=.65,stroke_color=c,fill_color=c if v else PALE,fill_opacity=.85 if v else .4).move_to([x,.9-i*.7,0]),
                         label(str(v),x,.9-i*.7,25,WHITE if v else MUTED))
        self.add(math(r'E=+m',-3.6,-2.3,35,BLUE),math(r'E=-m',3.6,-2.3,35,ORANGE),
                 label('Two independent solutions per energy sign',0,-3.2,28),
                 label('Away from rest, upper and lower components mix; they are not separate particle labels.',0,-3.95,24,MUTED,width=14.5))


class FieldTransformationTypes(Scene):
    def construct(self):
        heading(self,'A field type specifies how its components transform','Compare descriptions of the same event in two Lorentz frames')
        for x,title,c in [(-5,'Scalar',BLUE),(0,'Vector',TEAL),(5,'Spinor',ORANGE)]:
            self.add(label(title,x,2,29,c),box(x,.05,4.45,2.75,c))
        self.add(Dot([-5,.5,0],color=BLUE,radius=.35),math(r'\phi',-5,-.65,38,BLUE),
                 math(r"\phi'(x')=\phi(x)",-5,-2,29,BLUE),label('One component; unchanged value',-5,-3,22,MUTED,width=4.7))
        for i,txt in enumerate(['A^0','A^1','A^2','A^3']):self.add(math(txt,-.9+(i%2)*1.8,.6-(i//2)*1.1,29,TEAL))
        self.add(math(r"A'^\mu=\Lambda^\mu{}_{\nu}A^\nu",0,-2,29,TEAL),label('Four components mix with Λ',0,-3,22,MUTED,width=4.7))
        for i in range(4):self.add(Square(side_length=.42,color=ORANGE,fill_color=ORANGE,fill_opacity=.2+.18*i).move_to([4.2+i*.55,.1,0]))
        self.add(math(r"\psi'(x')=S(\Lambda)\psi(x)",5,-2,29,ORANGE),label('Components mix with S(Λ)',5,-3,22,MUTED,width=4.7),
                 label('The vector matrix Λ and spinor matrix S represent the same transformation in different ways.',0,-3.95,22,MUTED,width=14.5))


class QuantumPictures(Scene):
    def construct(self):
        heading(self,'Two quantum pictures give the same expectation value','Move time dependence between the state and the operator using U(t) = exp(−iHt/ℏ)')
        for y,title,state,operator,c in [(1,'Schrödinger',r'|\psi(t)\rangle=U(t)|\psi(0)\rangle',r'O_S',BLUE),
                                       (-1.65,'Heisenberg',r'|\psi_H\rangle=|\psi(0)\rangle',r'O_H(t)=U^\dagger(t)O_SU(t)',TEAL)]:
            self.add(label(title,-5.5,y+.9,27,c),box(-3.5,y,7,1.25,c),math(state,-3.5,y,32,c,width=6.6),
                     box(4,y,6.5,1.25,c),math(operator,4,y,32,c,width=6),label('state',-3.5,y-.95,22,MUTED),label('operator',4,y-.95,22,MUTED))
        self.add(math(r'\langle\psi(t)|O_S|\psi(t)\rangle=\langle\psi(0)|O_H(t)|\psi(0)\rangle',0,-3.55,35,width=14.3))


class FieldHistorySlice(Scene):
    def construct(self):
        heading(self,'A field history contains a configuration at every time','Color indicates the scalar field value at a spacetime point; a highlighted column is one time slice')
        for i in range(9):
            for j in range(9):
                value=np.sin(j*.6-i*.45)
                self.add(Dot([-6.6+i*.56,-2+j*.48,0],radius=.13,color=BLUE if value>=0 else ORANGE,fill_opacity=.22+.78*abs(value)))
        self.add(RoundedRectangle(width=.49,height=4.3,corner_radius=.1,color=TEAL,stroke_width=3).move_to([-4.36,-.08,0]),
                 arrow((-7,-2.6),(-1.6,-2.6)),arrow((-7,-2.6),(-7,2.35)),math('t',-1.55,-3,29),math('x',-7.3,2.4,29),
                 math(r't=t_0',-4.36,2.45,29,TEAL),arrow((-1.4,-.1),(.3,-.1),TEAL))
        ax=axes_at(4,0,5.8,4,(-1.2,1.2,1),(-2.4,2.4,1));self.add(ax)
        pts=[ax.c2p(np.sin((x+2)*1.25-1.8),x) for x in np.linspace(-2,2,180)]
        self.add(VMobject(color=TEAL,stroke_width=4).set_points_smoothly(pts),
                 math(r'\phi(t_0,x)',5.8,-.4,29,TEAL),math('x',3.6,2.3,29),
                 label('One spatial configuration',4,-2.65,25,TEAL),
                 label('To specify a classical state, also give the conjugate momentum field π(t₀, x).',0,-3.75,25,MUTED,width=14.5))


class LocalFieldVariation(Scene):
    def construct(self):
        heading(self,'Vary the field locally to derive its equation of motion','The variation vanishes at the boundary but can have either sign inside a small region')
        ax=axes_at(-4,0,6,4.2,(-2.5,2.5,1),(-1,1,1));self.add(ax)
        base=lambda x:.35*np.sin(x)
        bump=lambda x:max(0,1-((x-.5)/.7)**2)**2
        self.add(path_curve(ax,base,[-2.5,2.5],BLUE),path_curve(ax,lambda x:base(x)+.55*bump(x),[-2.5,2.5],ORANGE),
                 label('Original field',-5.2,2.1,23,BLUE),label('Local variation',-2.5,2.1,23,ORANGE),
                 label('position x',-1.65,-.4,22),math(r'\phi\to\phi+\delta\phi',-4,-2.9,34))
        self.add(math(r'\delta S=\int d^4x\,C(x)\,\delta\phi(x)',3.7,1.35,34,width=6.6),
                 label('Stationary for every local variation',3.7,.35,25,width=6.8),
                 arrow((3.7,-.1),(3.7,-.85),TEAL),math(r'C(x)=0',3.7,-1.4,45,TEAL),
                 math(r'\frac{\partial\mathcal L}{\partial\phi}-\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}=0',3.7,-2.75,32,width=7),
                 label('The Euler–Lagrange equation holds at each spacetime point.',0,-3.85,27,MUTED))


class BosonFermionOccupancy(Scene):
    def construct(self):
        heading(self,'The operator algebra controls how many quanta fit in one mode','A fermion mode includes its momentum and spin label; all states below use discrete normalization')
        for x,title,c in [(-4,'Boson mode',BLUE),(4,'Fermion mode',ORANGE)]:
            self.add(label(title,x,2.2,29,c))
            for i,n in enumerate([0,1,2]):
                y=1.25-i*1.4
                self.add(box(x,y,4.8,.95,c))
                if x>0 and n==2:self.add(label('zero vector',x,y,28,ORANGE))
                else:
                    self.add(math(r'|'+str(n)+r'\rangle',x-1.7,y,28,c))
                    for j in range(n):self.add(Dot([x+.25+j*.5,y,0],radius=.14,color=c))
                if i<2:self.add(arrow((x,y-.5),(x,y-.9),c),math(r'a^\dagger',x+.65,y-.7,24,c))
        self.add(math(r'(a^\dagger)^2|0\rangle=\sqrt2\,|2\rangle',-4,-3.05,32,BLUE),
                 math(r'(a^\dagger)^2=0',4,-3.05,37,ORANGE),
                 label('Boson occupancies: 0, 1, 2, …',-4,-3.8,24,BLUE),label('Fermion occupancies: 0 or 1',4,-3.8,24,ORANGE))


class GlobalLocalPhase(Scene):
    def construct(self):
        heading(self,'Global and local phase changes differ in how they vary across spacetime','Each circle is a complex phase at one point; gray arrows show the original common phase')
        for row,y,title,angles,c in [(0,1.0,'Global: one angle everywhere',[60,60,60],BLUE),(1,-1.35,'Local: angle depends on x',[70,140,10],TEAL)]:
            self.add(label(title,-4.8,y,25,c,width=4.2))
            for i,deg in enumerate(angles):
                x=-.6+i*3.2
                self.add(Circle(radius=.68,color='#ccd5df').move_to([x,y,0]))
                for a,col in [(20,'#bcc6d2'),(deg,c)]:
                    r=np.radians(a);self.add(arrow((x,y),(x+.6*np.cos(r),y+.6*np.sin(r)),col))
                if row==0:self.add(math(r'x_'+str(i+1),x,y+1.15,28))
        self.add(math(r'\partial_\mu(e^{i\alpha(x)}\psi)=e^{i\alpha(x)}[\partial_\mu\psi+i(\partial_\mu\alpha)\psi]',0,-3,31,width=14.3),
                 label('For a local gauge change, transform Aμ as well so the covariant derivative compensates.',0,-3.85,24,MUTED,width=14.5))


class ScatteringEventRate(Scene):
    def construct(self):
        heading(self,'A cross section connects scattering strength to event counts','For a thin target with independent scattering and uniform incident flux')
        for y in [-1,0,1]:
            self.add(arrow((-6.8,y),(-2,y),BLUE))
        self.add(box(-.8,0,1.1,4.3,TEAL))
        for y in np.linspace(-1.7,1.7,7):self.add(Dot([-.8,y,0],color=TEAL,radius=.1))
        for y in [-1.8,0,1.8]:
            self.add(arrow((-.3,0),(4.3,y),ORANGE),box(4.8,y,.6,.85,ORANGE))
        self.add(label('Incident beam',-4.5,2.2,28,BLUE),label('Target',-.8,2.6,28,TEAL),label('Detectors',4.8,2.6,28,ORANGE),
                 math(r'\Phi',-4.5,-1.9,40,BLUE),math('N',-.8,-2.6,40,TEAL),
                 math(r'\mathrm{rate}=\Phi\,N\,\sigma',0,-3.5,44),label('Ideal total count; real detectors require acceptance and efficiency corrections.',0,-4.1,22,MUTED))


class TwoBodyPhaseSpace(Scene):
    def construct(self):
        heading(self,'Conservation restricts the allowed final momenta','Two-body final state in the center-of-momentum frame; the circle is a plane through a momentum sphere')
        cx=-3.7;cy=-.2;r=2
        self.add(Circle(radius=r,color=MUTED,stroke_opacity=.4).move_to([cx,cy,0]))
        for a in [.45,1.3,2.2]:
            d=np.array([np.cos(a),np.sin(a)])*r
            self.add(arrow((cx,cy),(cx+d[0],cy+d[1]),BLUE),arrow((cx,cy),(cx-d[0],cy-d[1]),ORANGE))
        self.add(label('Alternative directions',cx,-2.75,26),math(r'\mathbf p_1',-1.25,1.1,32,BLUE),math(r'\mathbf p_2',-6.2,-1.5,32,ORANGE),
                 math(r'\mathbf p_1+\mathbf p_2=0',3.5,1.6,37,width=6.3),
                 math(r'\sqrt{p^2+m_1^2}+\sqrt{p^2+m_2^2}=E_{\rm CM}',3.5,.2,33,width=6.7),
                 label('Energy fixes the magnitude p.',3.5,-1,27,width=6.5),label('Direction remains to be integrated.',3.5,-1.8,26,width=6.5),
                 label('Phase space counts allowed outcomes; |ℳ|² weights how strongly each outcome occurs.',0,-3.85,25,MUTED,width=14.5))


class PredictionWorkflow(Scene):
    def construct(self):
        heading(self,'From a field theory to a predicted count','Each step supplies a different part of the calculation')
        entries=[(-5.4,r'\mathcal L','Specify fields','and interactions',BLUE),(-1.8,r'\mathcal M','Add amplitude','contributions',TEAL),(1.8,r'\sigma','Square, sum and','integrate outcomes',PURPLE),(5.4,r'\mathrm{rate}','Include beam','and target',ORANGE)]
        for x,eq,a,b,c in entries:
            self.add(box(x,.4,3,3.5,c),math(eq,x,1.25,48,c,width=2.6),label(a,x,0,24,width=2.7),label(b,x,-.6,24,width=2.7))
            if x<5:self.add(arrow((x+1.52,.4),(x+2.05,.4)))
        self.add(math(r'\mathcal M=\sum_j\mathcal M_j',-3.7,-2.4,36,TEAL),math(r'\mathrm{rate}=\Phi N\sigma',3.7,-2.4,36,ORANGE),
                 label('Add contributions to the same transition before taking the squared magnitude.',0,-3.65,27,MUTED,width=14.5))


class OperatorOrdering(Scene):
    def construct(self):
        heading(self,'Time ordering and normal ordering sort by different rules','For bosonic operators; fermionic exchanges also introduce signs')
        self.add(label('Time ordering',-4,2.1,31,BLUE),arrow((-6.7,.9),(-1.3,.9)),Dot([-5.5,.9,0],color=BLUE),Dot([-2.5,.9,0],color=TEAL),
                 math(r't_1',-5.5,1.4,29,BLUE),math(r't_2>t_1',-2.5,1.4,29,TEAL),math('t',-1.1,.5,28),
                 math(r'T[H_I(t_1)H_I(t_2)]=H_I(t_2)H_I(t_1)',-4,-.55,32,width=7),
                 label('Earlier operation acts first, on the right.',-4,-1.55,25,width=7),
                 label('Normal ordering',4,2.1,31,ORANGE),math(r':aa^\dagger:\;=a^\dagger a',4,.7,43,ORANGE),
                 label('Creation operators go to the left.',4,-.55,26,width=6.6),math(r'aa^\dagger=a^\dagger a+1',4,-1.65,39),
                 label('Reordering the actual product adds a commutator term; Wick contractions account for these terms.',0,-3.4,25,MUTED,width=14.3))


class FeynmanPolePrescription(Scene):
    def construct(self):
        heading(self,'The Feynman prescription selects the two time orderings','Complex energy plane; infinitesimal pole displacements are exaggerated')
        self.add(arrow((-6.8,0),(6.8,0)),arrow((0,-2.7),(0,2.5)),math(r'\operatorname{Re}p^0',6.4,-.5,28),math(r'\operatorname{Im}p^0',1.2,2.45,28))
        for x,y,eq,c in [(-3,.45,r'-E_p+i0',ORANGE),(3,-.45,r'+E_p-i0',BLUE)]:
            self.add(Cross(stroke_color=c,stroke_width=4).scale(.12).move_to([x,y,0]),math(eq,x,y+(.5 if y>0 else -.5),33,c))
        self.add(Arc(radius=5,start_angle=0,angle=PI,color=ORANGE,stroke_width=3).stretch(.44,1,about_point=ORIGIN),
                 Arc(radius=5,start_angle=PI,angle=PI,color=BLUE,stroke_width=3).stretch(.44,1,about_point=ORIGIN),
                 label('Δt < 0: close above',-4.3,2.45,25,ORANGE),label('Δt > 0: close below',4.2,-2.55,25,BLUE),
                 math(r'e^{-ip^0\Delta t}',0,-3.35,37),label('The exponential decays in the chosen half-plane. This is the time-ordered propagator.',0,-4,24,MUTED,width=14.5))


class LoopMomentumFreedom(Scene):
    def construct(self):
        heading(self,'A loop leaves an internal momentum free','An electron–photon insertion illustrates the momentum routing inside a larger QED diagram')
        for y,title,c in [(1.35,'Electron segment',BLUE),(-1.25,'With a loop insertion',TEAL)]:
            self.add(label(title,-4.8,y+.65,26,c,width=4.5),arrow((-6.8,y),(-2,y),c),math('P',-4.4,y-.5,30,c))
        self.add(arrow((-1,1.35),(6.6,1.35),BLUE),math('P',5.8,.85,32,BLUE),label('No unfixed momentum',3,2.2,26,BLUE))
        y=-1.25
        self.add(arrow((-1,y),(1,y),TEAL),arrow((1,y),(4.5,y),TEAL),arrow((4.5,y),(6.6,y),TEAL))
        pts=[]
        for t in np.linspace(0,PI,220):
            r=1.75+.1*np.sin(18*t)
            pts.append([2.75-r*np.cos(t),y+r*np.sin(t),0])
        self.add(VMobject(color=ORANGE,stroke_width=3).set_points_smoothly(pts),Dot([1,y,0],color=INK),Dot([4.5,y,0],color=INK),
                 math(r'\ell',2.75,.8,32,ORANGE),math(r'P-\ell',2.75,-1.8,33,TEAL),math('P',-.4,-1.8,30),math('P',6,-1.8,30),
                 math(r'P=(P-\ell)+\ell',-3.6,-2.85,35),math(r'\int\frac{d^4\ell}{(2\pi)^4}',3.6,-2.95,39),
                 label('Conservation holds for every choice of ℓ. Integrate over that remaining four-momentum.',0,-4,25,MUTED,width=14.5))

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
        heading(self,'A constant force: a ball dropped from rest','Gravity gives a constant acceleration g = 9.8 m/s² downward; speed and distance fallen are measured downward')
        g=9.8
        panels=[(-5,'Acceleration',lambda t:g,(0,3.2,1),(0,12,4),r'g=9.8\ \mathrm{m/s^2}',[]),
                (0,'Speed (m/s)',lambda t:g*t,(0,3.2,1),(0,32,10),r'v=gt',[(t,g*t) for t in (1,2,3)]),
                (5,'Distance fallen (m)',lambda t:0.5*g*t*t,(0,3.2,1),(0,48,16),r'd=\tfrac12 g t^2',[(t,0.5*g*t*t) for t in (1,2,3)])]
        for cx,title,fn,xr,yr,formula,marks in panels:
            ax=axes_at(cx,-0.1,4.1,3.5,xr,yr)
            self.add(ax,path_curve(ax,fn,[0,3]),label(title,cx,2.15,28),math(formula,cx,-2.6,31),label('time (s)',cx+1.5,-2.08,22,MUTED))
            for t,v in marks:
                pt=ax.c2p(t,v)
                self.add(Dot(pt,color=ORANGE,radius=0.07),label(f'{v:.1f}',pt[0]-0.45,pt[1]+0.25,20,ORANGE))
        self.add(label('Integrate the acceleration to get the speed; integrate the speed to get the distance.',0,-3.65,26,MUTED))


class StationaryActionPaths(Scene):
    def construct(self):
        heading(self,'The real path sits at a flat spot','A ball thrown up and caught, and paths bent up or down that leave and return at the same moments')
        ax=axes_at(-4.6,0,5.6,4.2,(0,2,1),(0,6.5,2))
        self.add(ax)
        real=lambda t:9.8*t-4.9*t*t
        for e,c in [(-0.5,ORANGE),(0.5,TEAL),(0,BLUE)]:
            self.add(path_curve(ax,lambda t,e=e:real(t)+e*np.sin(np.pi*t/2),[0,2],c))
        for t in [0,2]:self.add(Dot(ax.c2p(t,0),color=INK,radius=0.09))
        self.add(label('time',-2.2,-2.5,23),label('height',-6.5,2.45,23),
                 label('bent up',-0.6,1.6,22,TEAL),label('real path',-0.6,1.15,22,BLUE),label('bent down',-0.6,0.7,22,ORANGE),
                 label('All paths leave the hand and return to it at the same moments.',-4.3,-3.3,22,MUTED,width=6.5))
        ax2=axes_at(4,-0.1,5.2,3.6,(-0.5,0.5,0.5),(0,0.4,0.2))
        sa=lambda e:1.2337*e*e+0.02  # the action, shifted so its axis sits below the curve
        self.add(ax2,path_curve(ax2,sa,[-0.5,0.5],PURPLE))
        for e,c in ((-0.5,ORANGE),(0,BLUE),(0.5,TEAL)):
            self.add(Dot(ax2.c2p(e,sa(e)),color=c,radius=0.09))
        self.add(label('action of each path',4,2.35,24,PURPLE),
                 label('bent down',2.0,-2.3,20,ORANGE),label('bent up',6.0,-2.3,20,TEAL),label('real path',4,-2.3,20,BLUE),
                 label('Bending either way raises the action by the same small amount.',4,-3.3,22,MUTED,width=6.5))


class PhaseSpaceStates(Scene):
    def construct(self):
        heading(self,'Position alone does not specify the state','The spring passes the middle twice in each swing, moving in opposite directions')
        ax=axes_at(-4,0,5.4,4.5,(-1.4,1.4,1),(-2.8,2.8,1));self.add(ax)
        self.add(Ellipse(width=5.4/1.4,height=4.5/1.4,color=BLUE).move_to(ax.c2p(0,0)))
        for y,c,tag in [(2,TEAL,'D: moving right'),(-2,ORANGE,'B: moving left')]:
            pt=ax.c2p(0,y);self.add(Dot(pt,color=c,radius=.11),label(tag,pt[0]+2.4,pt[1]+(0.45 if y>0 else -0.45),23,c,width=3.1))
        self.add(label('momentum p',-5.6,2.65,24),label('position x',-1.2,-0.7,23),
                 box(4,0,6,3.5),math(r'D=(0,\,+2)',4,.9,38,TEAL),math(r'B=(0,\,-2)',4,-.1,38,ORANGE),
                 label('Same position. Different states.',4,-1.1,25),
                 label('Points B and D of the spring in section 6: a point in phase space specifies both position and momentum.',0,-3.5,25,MUTED,width=15))


class TwoSlitCounts(Scene):
    def construct(self):
        heading(self,'Two slits open: some spots get fewer electrons','Counts on the screen with only slit A open, only slit B open, and both open')
        src=Dot([-6.6,0.2,0],color=INK,radius=0.1)
        bar=[Line([-4.8,y0,0],[-4.8,y1,0],color=INK,stroke_width=6) for y0,y1 in [(-1.9,-0.65),(-0.35,0.75),(1.05,2.3)]]
        scr=Line([-3.0,-1.9,0],[-3.0,2.3,0],color=MUTED,stroke_width=6)
        self.add(src,*bar,scr,label('source',-6.6,-0.35,21,MUTED),label('A',-5.15,0.9,22,TEAL),label('B',-5.15,-0.5,22,ORANGE),
                 label('two slits',-4.8,-2.3,21,MUTED),label('screen',-3.0,-2.3,21,MUTED))
        for y in (-0.5,0.9):
            self.add(DashedLine([-6.5,0.2,0],[-4.8,y,0],color=MUTED,stroke_width=2))
        ax=axes_at(2.6,-0.25,7.0,3.5,(-3,3,1),(0,4.2,1));self.add(ax)
        A=lambda y:np.exp(-(y+0.35)**2/2.6); B=lambda y:np.exp(-(y-0.35)**2/2.6)
        both=lambda y:A(y)+B(y)+2*np.sqrt(A(y)*B(y))*np.cos(4.2*y)
        self.add(DashedVMobject(ax.plot(lambda y:A(y)+B(y),x_range=[-3,3],color=MUTED,stroke_width=3),num_dashes=60),
                 path_curve(ax,A,[-3,3],TEAL).set_stroke(width=3),path_curve(ax,B,[-3,3],ORANGE).set_stroke(width=3),
                 path_curve(ax,both,[-3,3],BLUE))
        dark=-np.pi/4.2
        pt=ax.c2p(dark,both(dark))
        self.add(Dot(pt,color=INK,radius=0.07),arrow((pt[0]-1.4,pt[1]+2.6),(pt[0]-0.05,pt[1]+0.12),INK),
                 label('fewer than with\none slit open',pt[0]-1.9,pt[1]+3.05,21,INK,width=3.4))
        items=[('both open',BLUE),('only A open',TEAL),('only B open',ORANGE),('A + B, if chances added',MUTED)]
        for i,(s,c) in enumerate(items):
            x0=-0.6+4.0*(i%2); y0=2.4-0.5*(i//2)
            ln=Line([x0,y0,0],[x0+0.45,y0,0],color=c,stroke_width=5)
            lab=label(s,0,0,20,c); lab.next_to(ln,RIGHT,buff=0.15)
            self.add(ln,lab)
        self.add(label('position on the screen',2.6,-2.45,22,MUTED))
        self.add(label('If each electron went through one slit, the both-open count could never fall below either single-slit count.',0,-3.55,24,MUTED,width=15))


class SingleSlit(Scene):
    def construct(self):
        heading(self,'One slit: electrons pile up in a hump','Each electron lands as a single dot, anywhere on the screen')
        bx=-4.8; sx=-3.0
        self.add(Dot([-6.6,0.2,0],color=INK,radius=0.1),label('source',-6.6,-0.35,21,MUTED),
                 Line([bx,-1.9,0],[bx,0.0,0],color=INK,stroke_width=6),Line([bx,0.4,0],[bx,2.3,0],color=INK,stroke_width=6),
                 Line([sx,-1.9,0],[sx,2.3,0],color=MUTED,stroke_width=6),
                 label('one slit',bx,-2.3,21,MUTED),label('screen',sx,-2.3,21,MUTED),
                 DashedLine([-6.5,0.2,0],[bx,0.2,0],color=MUTED,stroke_width=2))
        rng=np.random.default_rng(3)
        for y in np.clip(rng.normal(0.2,0.75,45),-1.8,2.2):
            self.add(Dot([sx+0.18,y,0],radius=0.035,color=BLUE))
        ax=axes_at(2.6,-0.25,7.0,3.5,(-3,3,1),(0,1.2,1)); self.add(ax)
        self.add(path_curve(ax,lambda y:np.exp(-y**2/1.6),[-3,3],BLUE),
                 label('position on the screen',2.6,-2.45,22,MUTED),label('number of electrons',2.6,1.9,21,MUTED))
        self.add(label('Most electrons land behind the slit, fewer further out.',0,-3.55,22,MUTED,width=15))


class PhaseAlongScreen(Scene):
    def construct(self):
        heading(self,'The phase turns with distance','One slit open: an arrow for landing at each spot on the screen')
        bx=-5.4; sx=-1.6; lam=0.55
        self.add(Line([bx,2.3,0],[bx,0.15,0],color=INK,stroke_width=6),Line([bx,-0.15,0],[bx,-2.3,0],color=INK,stroke_width=6),
                 Line([sx,2.3,0],[sx,-2.3,0],color=MUTED,stroke_width=4),
                 label('slit',bx,-2.7,20,MUTED),label('screen',sx,-2.7,20,MUTED))
        hump=lambda y:np.exp(-y**2/3.0)
        for y in np.linspace(-2.0,2.0,9):
            d=np.hypot(sx-bx,y); ang=2*np.pi*d/lam; L=0.9*hump(y)
            u=np.array([sx-bx,y,0])/d
            self.add(DashedVMobject(Line(np.array([bx,0,0])+0.6*u,[sx,y,0],color=MUTED,stroke_width=1.5,stroke_opacity=0.5),num_dashes=12))
            o=np.array([sx+0.75,y,0]); v=np.array([np.cos(ang),np.sin(ang),0])*L
            self.add(Dot([sx,y,0],radius=0.04,color=INK),
                     Arrow(o-v/2,o+v/2,buff=0,color=BLUE,stroke_width=5,max_tip_length_to_length_ratio=0.3,max_stroke_width_to_length_ratio=10))
        self.add(label('arrow directions: set by the distance from the slit',sx+0.4,2.65,20,BLUE))
        ax=axes_at(4.6,0.0,3.4,4.0,(0,1.2,1),(-2.2,2.2,1)); self.add(ax)
        self.add(ax.plot_parametric_curve(lambda s:np.array([hump(s)**2,s,0]),t_range=[-2.2,2.2],color=TEAL,stroke_width=4),
                 label('chance per metre',4.6,2.45,21,TEAL),label('only the lengths count',4.6,-2.45,20,MUTED))
        self.add(label('Turn every arrow by any amount and the chances stay the same, so one slit alone can never show the phase.',0,-3.65,21,MUTED,width=15))


def wave_between(a, b, wavelength, amp=0.18, color=ORANGE, width=3):
    a=np.array([*a,0.]); b=np.array([*b,0.]); d=b-a; L=np.linalg.norm(d); u=d/L; n=np.array([-u[1],u[0],0.])
    return ParametricFunction(lambda s: a+u*s+n*amp*np.sin(2*np.pi*s/wavelength), t_range=[0,L], color=color, stroke_width=width)


class SternGerlachSetup(Scene):
    def construct(self):
        heading(self,'A magnet sorts silver atoms into two spots','Atoms leave a hot oven with their tilts pointing every which way, pass a shaped magnet, and hit a plate')
        oven=Rectangle(width=1.3,height=1.1,color=INK,fill_color=PALE,fill_opacity=1).move_to([-6.2,0.3,0])
        self.add(oven,label('oven',-6.2,-0.55,21,MUTED),Line([-5.55,0.3,0],[-1.4,0.3,0],color=BLUE,stroke_width=4))
        top=Polygon([-3.4,1.55,0],[-1.4,1.55,0],[-1.4,0.85,0],[-2.4,0.55,0],[-3.4,0.85,0],color=INK,fill_color=PALE,fill_opacity=1)
        bot=Polygon([-3.4,-0.25,0],[-1.4,-0.25,0],[-1.4,-0.95,0],[-3.4,-0.95,0],color=INK,fill_color=PALE,fill_opacity=1)
        self.add(top,bot,label('N',-2.4,1.2,24),label('S',-2.4,-0.6,24),label('magnet: field stronger near the top',-2.4,-1.4,20,MUTED,width=3.6))
        for y in (1.25,-0.65):
            self.add(Line([-1.4,0.3,0],[0.2,y,0],color=BLUE,stroke_width=3))
        self.add(Line([0.2,-1.6,0],[0.2,2.2,0],color=MUTED,stroke_width=6),label('plate',0.2,-2.0,21,MUTED))
        # expected vs seen
        for cx,title,c in [(3.3,'expected',MUTED),(6.0,'seen',BLUE)]:
            self.add(RoundedRectangle(width=1.6,height=3.4,corner_radius=0.1,color=MUTED,stroke_width=2).move_to([cx,0.3,0]),label(title,cx,2.35,24,c))
        self.add(Line([3.3,-1.0,0],[3.3,1.6,0],color=MUTED,stroke_width=10).set_opacity(0.6),
                 Dot([6.0,1.15,0],radius=0.17,color=BLUE),Dot([6.0,-0.55,0],radius=0.17,color=BLUE),
                 label('a continuous line',3.3,-1.75,20,MUTED),label('two spots, up and down',6.0,-1.75,20,BLUE,width=2.6))
        self.add(label('The tilt along the field takes only two values.',0,-3.3,25,INK))


class MagnetsInRow(Scene):
    def construct(self):
        heading(self,'Magnets in a row','Each magnet keeps one beam and passes it on; the last magnet shows how the atoms split')
        def mag(x,y,kind):
            c=BLUE if kind=='vertical' else ORANGE
            return VGroup(box(x,y,1.9,0.85,c),label(kind,x,y,22,c))
        rows=[(1.6,['vertical','vertical'],['up'],'all up'),
              (0.0,['vertical','sideways'],['up'],'50% right, 50% left'),
              (-1.6,['vertical','sideways','vertical'],['up','right'],'50% up, 50% down')]
        for y,mags,keeps,result in rows:
            x=-5.6
            for i,m in enumerate(mags):
                self.add(mag(x,y,m))
                if i<len(mags)-1:
                    self.add(arrow((x+1.0,y),(x+2.0,y),INK),label('keep '+keeps[i],x+1.5,y+0.35,19,MUTED))
                    x+=3.0
            self.add(arrow((x+1.0,y),(x+2.0,y),INK),label(result,x+3.6,y,23,INK,width=3.6))
        self.add(label('A measurement leaves a state that repeats (top), identical atoms give random results (middle),',0,-2.9,22,MUTED,width=15),
                 label('and measuring sideways erases the earlier up (bottom).',0,-3.4,22,MUTED,width=15))


class PhotoelectricEffect(Scene):
    def construct(self):
        heading(self,'Light knocks electrons out of a metal','Sodium: the fastest electrons gain energy in step with the frequency, above a threshold')
        self.add(Rectangle(width=0.5,height=3.2,color=INK,fill_color=PALE,fill_opacity=1).move_to([-3.6,0,0]),label('metal',-3.6,-1.95,21,MUTED))
        for y in (1.0,0.0,-1.0):
            self.add(wave_between((-7.0,y+0.9),(-3.9,y),0.35,0.12,ORANGE,3))
        # Electrons leave the lit face, back toward the light.
        for (x0,y0),(x1,y1) in (((-4.05,1.45),(-5.0,2.35)),((-4.05,-1.45),(-5.1,-2.3))):
            self.add(Dot([x0,y0,0],radius=0.09,color=BLUE),arrow((x0-0.05,y0),(x1,y1),BLUE))
        self.add(label('light',-6.6,2.3,21,ORANGE),label('electrons',-4.6,2.7,21,BLUE))
        ax=axes_at(3.4,-0.15,6.2,3.8,(0,12,2),(0,3,1)); self.add(ax)
        f0=5.56; h=4.1357e-15*1e14  # eV per 1e14 Hz
        self.add(DashedLine(ax.c2p(0,0),ax.c2p(f0,0),color=MUTED),ax.plot(lambda f:h*(f-f0),x_range=[f0,12],color=BLUE,stroke_width=4))
        self.add(Dot(ax.c2p(f0,0),color=INK,radius=0.08),label('threshold 5.6',ax.c2p(f0,0)[0]-0.9,ax.c2p(f0,0)[1]+0.4,20,INK),
                 label('slope h',ax.c2p(9.5,h*(9.5-f0))[0]-0.6,ax.c2p(9.5,h*(9.5-f0))[1]+0.35,22,BLUE))
        for v in (0,4,8,12): self.add(label(str(v),ax.c2p(v,0)[0],ax.c2p(v,0)[1]-0.32,18,MUTED))
        for v in (1,2,3): self.add(label(str(v),ax.c2p(0,v)[0]-0.25,ax.c2p(0,v)[1],18,MUTED))
        self.add(math(r'\text{frequency } (10^{14}\ \text{Hz})',3.4,-2.75,22,MUTED),label('energy of fastest electrons (eV)',2.4,2.1,21,MUTED))
        self.add(label('Brighter light ejects more electrons along the same line. Below the threshold, none come out.',0,-3.45,23,MUTED,width=15))


class ComptonScattering(Scene):
    def construct(self):
        heading(self,'X-rays bounce off electrons and come out longer','The shift matches a collision between an electron and a packet of momentum h/λ')
        e=np.array([0.0,0.0])
        self.add(wave_between((-6.0,0.0),(-0.15,0.0),0.42,0.18,ORANGE,3),label('incoming X-ray',-4.2,0.6,22,ORANGE))
        self.add(Dot([0,0,0],radius=0.14,color=BLUE),label('electron',0.0,-0.5,21,BLUE))
        ang=np.radians(40)
        self.add(wave_between((0.15*np.cos(ang),0.15*np.sin(ang)),(3.6*np.cos(ang),3.6*np.sin(ang)),0.75,0.2,ORANGE,3),
                 label('scattered X-ray:\nlonger wavelength',4.6,2.0,22,ORANGE))
        self.add(arrow((0.15,-0.15),(2.2,-1.6),BLUE),label('electron recoils',3.0,-1.95,21,BLUE))
        self.add(DashedLine([0,0,0],[3.0,0,0],color=MUTED),Arc(radius=1.1,start_angle=0,angle=ang,color=MUTED),label('θ',1.35,0.45,24,MUTED))
        self.add(label('A smooth wave would shake the electron at its own frequency and re-emit the same wavelength.',0,-2.9,22,MUTED,width=15),
                 label('Instead the wavelength grows, and grows more at larger angles.',0,-3.4,22,MUTED,width=15))


class LightConeIntervals(Scene):
    def construct(self):
        heading(self,'The light cone','Events compared with the one at the centre; time points up')
        c=np.array([-3.2,-0.3,0]); R=2.7
        self.add(Polygon(c,c+[R,R,0],c+[-R,R,0],fill_color=BLUE,fill_opacity=.12,stroke_width=0),
                 Polygon(c,c+[R,-R,0],c+[-R,-R,0],fill_color=BLUE,fill_opacity=.06,stroke_width=0))
        for s in (-1,1):self.add(DashedLine(c+[-R,-R*s,0],c+[R,R*s,0],color=ORANGE))
        self.add(arrow((c[0]-3.2,c[1]),(c[0]+3.2,c[1])),arrow((c[0],c[1]-2.9),(c[0],c[1]+3.0)),
                 label('time',c[0]+0.55,c[1]+2.95,22),label('space',c[0]+3.2,c[1]-0.35,22),
                 Dot(c,color=INK,radius=.08),
                 label('future',c[0]-0.85,c[1]+2.2,22,BLUE),label('past',c[0]-0.75,c[1]-2.2,22,BLUE))
        for pt,col,tag in [([0.5,1.6,0],BLUE,'A'),([1.4,1.4,0],ORANGE,'B'),([2.1,0.6,0],TEAL,'C')]:
            pos=c+pt;self.add(Dot(pos,color=col,radius=.1),label(tag,pos[0]+.28,pos[1]+.18,24,col))
        for y,title,desc,col in [(1.7,'A: positive interval','Inside the cone. Something slower than light can get there.',BLUE),
             (0,'B: zero interval','On the edge. Only light gets there.',ORANGE),
             (-1.7,'C: negative interval','Outside the cone. Nothing can get there, not even light.',TEAL)]:
            self.add(label(title,3.9,y+.3,26,col),label(desc,3.9,y-.3,21,MUTED,width=6.8))
        self.add(label('With two space directions drawn, the dashed X becomes a cone.',0,-3.75,22,MUTED,width=14.5))


class RelativisticEnergySolutions(Scene):
    def construct(self):
        heading(self,'The relativistic rule allows two energies for every momentum','Energy against momentum for one particle of mass m')
        ax=axes_at(-2.6,-0.35,7.4,5.6,(-2.5,2.5,1),(-3,3,1))
        gap=Polygon(ax.c2p(-2.5,1),ax.c2p(2.5,1),ax.c2p(2.5,-1),ax.c2p(-2.5,-1),stroke_width=0,fill_color=PALE,fill_opacity=0.9)
        self.add(gap,ax,
                 DashedLine(ax.c2p(-2.5,1),ax.c2p(2.5,1),color=MUTED,stroke_width=2),
                 DashedLine(ax.c2p(-2.5,-1),ax.c2p(2.5,-1),color=MUTED,stroke_width=2),
                 path_curve(ax,lambda p:np.sqrt(1+p*p),[-2.5,2.5],BLUE),path_curve(ax,lambda p:-np.sqrt(1+p*p),[-2.5,2.5],ORANGE),
                 label('energy',-3.25,2.2,22,MUTED),label('momentum',1.75,-0.62,22,MUTED),
                 math(r'+mc^2',-6.95,0.58,28,BLUE),math(r'-mc^2',-6.95,-1.28,28,ORANGE),
                 label('no energy allowed in between',-0.75,-0.05,20,MUTED),
                 label('positive energies',4.6,1.75,26,BLUE),label('start at +mc² and go up',4.6,1.25,22,BLUE),
                 label('negative energies',4.6,-1.7,26,ORANGE),label('start at −mc² and go down\nwithout end',4.6,-2.4,22,ORANGE),
                 Arrow(ax.c2p(2.15,-2.37),ax.c2p(2.45,-2.65),buff=0,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.5),
                 Arrow(ax.c2p(-2.15,-2.37),ax.c2p(-2.45,-2.65),buff=0,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.5))


class DiracSeaHole(Scene):
    def construct(self):
        heading(self,'Dirac’s sea, and a hole in it','Every negative-energy state is filled, so an ordinary electron has nowhere to fall')
        x0,x1=-5.2,0.6
        top=Rectangle(width=x1-x0,height=1.7,stroke_color=BLUE,stroke_width=2,fill_color=PALE,fill_opacity=0.5).move_to([(x0+x1)/2,1.55,0])
        sea=Rectangle(width=x1-x0,height=2.3,stroke_color=ORANGE,stroke_width=2,fill_color=ORANGE,fill_opacity=0.12).move_to([(x0+x1)/2,-1.95,0])
        self.add(top,sea,
                 Arrow([x0-0.7,-3.2,0],[x0-0.7,2.6,0],buff=0,color=MUTED,stroke_width=3,max_tip_length_to_length_ratio=0.04),
                 label('energy',x0-0.7,2.85,20,MUTED),
                 math(r'+mc^2',x0-1.55,0.7,26,BLUE),math(r'-mc^2',x0-1.55,-0.8,26,ORANGE),
                 Line([x0-0.85,0.7,0],[x0-0.55,0.7,0],color=MUTED),Line([x0-0.85,-0.8,0],[x0-0.55,-0.8,0],color=MUTED),
                 )
        hole=(-1.2,-1.1)
        for r,y in enumerate((-1.1,-1.45,-1.8,-2.15,-2.5,-2.85)):
            for c in range(12):
                x=x0+0.35+c*((x1-x0-0.7)/11)
                if abs(x-hole[0])<0.2 and abs(y-hole[1])<0.05:
                    self.add(Circle(radius=0.13,color=ORANGE,stroke_width=3).move_to([x,y,0])); hx=x
                else:
                    self.add(Dot([x,y,0],radius=0.09,color=ORANGE))
        e=(hx,1.5)
        self.add(Dot([*e,0],radius=0.13,color=BLUE),
                 Arrow([hx,hole[1]+0.2,0],[hx,e[1]-0.2,0],buff=0,color=INK,stroke_width=4,max_tip_length_to_length_ratio=0.07))
        wave=ParametricFunction(lambda t:np.array([-4.9+t*3.5,0.4+t*(-0.65)+0.13*np.sin(t*10*PI),0]),t_range=[0,1],color=PURPLE,stroke_width=3)
        self.add(wave,label('a packet of light, at least 2mc²',-3.4,-0.55,20,PURPLE))
        self.add(label('the electron, lifted out:',4.3,1.85,22,BLUE),label('negative charge,\npositive energy',4.3,1.15,22,BLUE),
                 label('the hole it leaves:',4.3,-1.05,22,ORANGE),label('looks like a positive charge\nwith positive energy',4.3,-1.75,22,ORANGE),
                 Line([hx+0.25,e[1],0],[2.2,1.6,0],color=BLUE,stroke_width=2),Line([hx+0.25,hole[1],0],[2.0,-1.3,0],color=ORANGE,stroke_width=2))
        self.add(label('The electron and the hole appear together: a pair.',0,-3.75,24,MUTED))


class PositronTrack(Scene):
    def construct(self):
        heading(self,'Anderson’s trail, 1932','A sketch of the cloud-chamber photograph: one trail crossing a lead plate')
        cx,cy,R=-2.6,-0.45,2.75
        self.add(Circle(radius=R,color=MUTED,stroke_width=3).move_to([cx,cy,0]),
                 Rectangle(width=2*R-0.5,height=0.22,stroke_width=0,fill_color=INK,fill_opacity=0.85).move_to([cx,cy,0]))
        # Below the plate: more energy, gently curved. Above: less energy, tightly curved. Both bend to the left.
        p0=np.array([cx+0.55,cy-0.11,0])
        r1=6.0; c1=p0+np.array([-r1,0,0])
        low=Arc(radius=r1,start_angle=-0.42,angle=0.42,arc_center=c1,color=ORANGE,stroke_width=5)
        p1=np.array([cx+0.55,cy+0.11,0])
        r2=2.1; c2=p1+np.array([-r2,0,0])
        up=Arc(radius=r2,start_angle=0,angle=1.02,arc_center=c2,color=ORANGE,stroke_width=5)
        tip=up.point_from_proportion(1.0); pre=up.point_from_proportion(0.93)
        self.add(low,up,Arrow(pre,tip,buff=0,color=ORANGE,stroke_width=5,max_tip_length_to_length_ratio=1.2))
        self.add(label('lead plate',cx-1.55,cy+0.42,20,INK),
                 label('enters with more energy:\ngentle curve',3.9,-1.75,23,INK),Line([cx+1.0,cy-1.4,0],[2.2,-1.7,0],color=MUTED,stroke_width=2),
                 label('loses energy in the lead',3.9,-0.45,23,INK),Line([cx+R-0.2,cy,0],[2.05,-0.45,0],color=MUTED,stroke_width=2),
                 label('leaves with less energy:\ntighter curve',3.9,1.2,23,INK),Line([cx+0.45,cy+1.25,0],[2.2,1.2,0],color=MUTED,stroke_width=2))
        self.add(label('The tighter half shows which way it went. Going that way, the bend is a positive charge’s.',0,-3.75,23,MUTED,width=14.5))


class MagnetTwiceTooStrong(Scene):
    def construct(self):
        heading(self,'The puzzle: a magnet twice too strong','Spots of silver atoms on the plate: the count gives the angular momentum, the gap gives the strength of the magnet')
        cases=[(-5.2,[0.45,-0.45],'angular momentum ℏ/2,\nby the rule',r'\mu=\frac{e\hbar}{4m}','right count, gap too small',INK,MUTED),
               (0.0,[0.9,0,-0.9],'angular momentum ℏ,\nby the rule',r'\mu=\frac{e\hbar}{2m}','right gap, one spot too many',INK,MUTED),
               (5.2,[0.9,-0.9],'measured',r'\mu=\frac{e\hbar}{2m}','two spots, wide apart',ORANGE,ORANGE)]
        for x,ys,title,form,note,tc,c in cases:
            self.add(label(title,x,2.2,24,tc),
                     Rectangle(width=2.4,height=3.2,stroke_color=INK,stroke_width=3,fill_color=PALE,fill_opacity=0.7).move_to([x-0.5,-0.2,0]))
            for y in ys:
                self.add(Ellipse(width=1.4,height=0.32,stroke_width=0,fill_color=c,fill_opacity=0.9).move_to([x-0.5,-0.2+y,0]))
            g=max(ys)
            self.add(DoubleArrow([x+1.0,-0.2-g,0],[x+1.0,-0.2+g,0],buff=0,color=c,stroke_width=4,tip_length=0.16))
            if form: self.add(math(form,x+1.95,-0.2,30,tc))
            self.add(label(note,x-0.1,-2.2,22,tc))
        self.add(label('Two spots mean an angular momentum of ℏ/2. Their gap is the one a whole ℏ would give.',0,-3.0,23,INK,width=14.5),
                 label('Where does the spin come from, and why is its magnet twice as strong?',0,-3.75,24,ORANGE,width=14.5))


class WaveOnCircle(Scene):
    def construct(self):
        heading(self,'A wave round a circle has to join up with itself','A whole number of wavelengths fits; half a wavelength left over does not')
        R,a=1.75,0.38
        for x,n,c,title,note in [(-5.0,3,TEAL,'3 wavelengths','joins up: allowed'),(2.6,2.5,ORANGE,'2½ wavelengths','does not join up: not allowed')]:
            ctr=np.array([x,-0.3,0])
            self.add(Circle(radius=R,color='#b8c6d4',stroke_width=2).move_to(ctr))
            f=lambda s,n=n,ctr=ctr: ctr+(R+a*np.cos(n*s))*np.array([np.cos(s),np.sin(s),0])
            self.add(ParametricFunction(f,t_range=[0,2*PI-0.001,0.01],color=c,stroke_width=5))
            self.add(label(title,x,2.15,26,c),label(note,x,-2.75,24,c))
            if n!=int(n):
                s0=f(0.0001); s1=f(2*PI-0.001)
                self.add(Dot(s0+np.array([0,0.0,0]),radius=0.08,color=INK),Dot(s1,radius=0.08,color=INK),
                         Line(s0,s1,color=INK,stroke_width=3),
                         label('start and end\nout of step',x+3.5,-0.3,21,INK))
            else:
                self.add(Dot(f(0),radius=0.08,color=INK),label('start and end\nmeet',x+3.4,-0.3,21,INK))
        self.add(label('Angular momentum = number of wavelengths round the circle, times ℏ.',0,-3.75,24,MUTED,width=14.5))


class AngularMomentumParts(Scene):
    def construct(self):
        heading(self,'Angular momentum about the vertical axis, in two parts','Seen from above: distance from the axis, times the momentum that carries the particle round')
        for cx,pos,mom,c,sense,form,word in [(-4.2,(1.9,0),(0,1.5),TEAL,1,r'+\,x\,p_y','goes round anticlockwise'),(4.2,(0,1.5),(1.5,0),ORANGE,-1,r'-\,y\,p_x','goes round clockwise')]:
            O=np.array([cx,-0.4,0]); P=O+np.array([*pos,0]); M=np.array([*mom,0])
            self.add(Arrow(O+[-2.7,0,0],O+[2.9,0,0],buff=0,color='#b8c6d4',stroke_width=2,max_tip_length_to_length_ratio=0.04),
                     Arrow(O+[0,-2.2,0],O+[0,2.2,0],buff=0,color='#b8c6d4',stroke_width=2,max_tip_length_to_length_ratio=0.05),
                     math('x',O[0]+3.1,O[1],26,MUTED),math('y',O[0]-0.3,O[1]+2.1,26,MUTED),
                     Dot(O,radius=0.1,color=INK),label('axis',O[0]-0.65,O[1]-0.4,27,MUTED),
                     Line(O,P,color=INK,stroke_width=4),Dot(P,radius=0.13,color=c),
                     Arrow(P,P+M,buff=0,color=c,stroke_width=6,max_tip_length_to_length_ratio=0.2))
            if pos[1]==0:
                self.add(math('x',O[0]+0.95,O[1]-0.3,28),math('p_y',P[0]+0.45,P[1]+0.85,30,c))
                arc=Arc(radius=1.0,start_angle=0.35,angle=1.5,arc_center=O,color=c,stroke_width=3)
            else:
                self.add(math('y',O[0]-0.3,O[1]+0.95,28),math('p_x',P[0]+0.85,P[1]+0.4,30,c))
                arc=Arc(radius=1.0,start_angle=PI/2-0.35,angle=-1.5,arc_center=O,color=c,stroke_width=3)
            arc.add_tip(tip_length=0.2,tip_width=0.2)
            self.add(arc,label(word,cx,-3.0,23,c),math(r'\text{contributes }'+form,cx+0.4,2.4,30,c))
        self.add(math(r'L_z = x\,p_y - y\,p_x',0,-3.75,36))


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
        heading(self,'One full turn flips the sign; two full turns restore it','The phase of the spin-up amplitude as the spin is turned about the vertical')
        for x,theta,phase,direction,word in [(-5,r'0^\circ','1',1,'as at the start'),(0,r'360^\circ','-1',-1,'minus the start'),(5,r'720^\circ','1',1,'as at the start')]:
            self.add(Circle(radius=1.1,color='#b8c6d4').move_to([x,.3,0]),
                     arrow((x,.3),(x+direction*.95,.3),BLUE),math(r'\text{turned by }'+theta,x,2.05,32),
                     math(r'\text{amplitude}\times('+phase+')' if direction==-1 else r'\text{amplitude}\times '+phase,x,-1.5,32,BLUE),
                     label(word,x,-2.25,26))
        self.add(label('A shared sign changes no chance on its own. It shows when the state is added to a copy that was not turned.',0,-3.75,23,MUTED,width=14.5))


class HalfAngleState(Scene):
    def construct(self):
        heading(self,'An angle in space is half that angle in the state','A spin tilted away from up, and the two amplitudes that describe it')
        self.add(label('in space',-6.3,0.75,24,ORANGE),label('in the state',-6.3,-1.2,24,BLUE))
        for x,theta,sp,st,tex,word in [(-3.9,r'0^\circ',1,0,r'(1,\ 0)','up'),(-1.1,r'180^\circ',-1,90,r'(0,\ 1)','down'),(1.7,r'360^\circ',1,180,r'(-1,\ 0)','minus up'),(4.5,r'720^\circ',1,0,r'(1,\ 0)','up')]:
            self.add(math(r'\text{tilted by }'+theta,x,2.0,30))
            self.add(DashedLine([x,0.15,0],[x,1.35,0],color='#b8c6d4',stroke_width=2),
                     arrow((x,0.75-sp*0.5),(x,0.75+sp*0.5),ORANGE))
            c=np.array([x,-1.2,0]); r=0.8
            self.add(Line(c+[-r,0,0],c+[r,0,0],color='#b8c6d4',stroke_width=2),Line(c+[0,-r,0],c+[0,r,0],color='#b8c6d4',stroke_width=2))
            a=np.radians(st)
            self.add(Arrow([x,-1.2,0],[x+0.8*np.cos(a),-1.2+0.8*np.sin(a),0],buff=0,color=BLUE,stroke_width=7,max_tip_length_to_length_ratio=0.25))
            self.add(math(tex,x,-2.45,30,BLUE),label(word,x,-3.0,24))
        self.add(label('Each state is drawn as an arrow: across for the up amplitude, upward for the down amplitude.',0,-3.75,22,MUTED,width=14.5))


class RestSpinorBasis(Scene):
    def construct(self):
        heading(self,'A particle at rest: four solutions','Each solution fills one entry of the column of four wave functions')
        for x,vals,spin,c in [(-5.4,[1,0,0,0],'spin up',BLUE),(-1.8,[0,1,0,0],'spin down',BLUE),(1.8,[0,0,1,0],'spin up',ORANGE),(5.4,[0,0,0,1],'spin down',ORANGE)]:
            self.add(label(spin,x,2.0,28,c))
            for i,v in enumerate(vals):
                self.add(Square(side_length=.65,stroke_color=c,fill_color=c if v else PALE,fill_opacity=.85 if v else .4).move_to([x,1.0-i*.7,0]),
                         label(str(v),x,1.0-i*.7,25,WHITE if v else MUTED))
        self.add(math(r'\text{energy }+mc^2',-3.6,-2.1,34,BLUE),math(r'\text{energy }-mc^2',3.6,-2.1,34,ORANGE),
                 Line([-6.2,-1.65,0],[-1.0,-1.65,0],color=BLUE,stroke_width=3),Line([1.0,-1.65,0],[6.2,-1.65,0],color=ORANGE,stroke_width=3),
                 label('upper pair of entries',-3.6,-2.75,22,MUTED),label('lower pair of entries',3.6,-2.75,22,MUTED),
                 label('The energy tells the pairs apart. The spin tells the two entries of a pair apart.',0,-3.75,24,MUTED,width=14.5))


class NeutronFullTurn(Scene):
    def construct(self):
        heading(self,'Seeing the sign: split, turn one path, recombine','A sketch of the 1975 neutron experiments')
        src=np.array([-7.0,-0.4,0]); S=np.array([-5.6,-0.4,0]); top=np.array([-3.6,1.2,0]); bot=np.array([-3.6,-2.0,0]); R=np.array([-1.6,-0.4,0]); det=np.array([-0.4,-0.4,0])
        beam=lambda a,b:Line(a,b,color=ORANGE,stroke_width=4)
        self.add(beam(src,S),beam(S,top),beam(top,R),beam(S,bot),beam(bot,R),Arrow(R,det,buff=0,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.25))
        for P in (S,R):
            self.add(Line(P+[0,-0.45,0],P+[0,0.45,0],color=TEAL,stroke_width=7))
        self.add(Line(top+[-0.5,0.02,0],top+[0.5,0.02,0],color=TEAL,stroke_width=7),Line(bot+[-0.5,-0.02,0],bot+[0.5,-0.02,0],color=TEAL,stroke_width=7))
        mag=(S+top)/2
        self.add(Rectangle(width=1.0,height=0.75,stroke_color=PURPLE,stroke_width=3,fill_color=PURPLE,fill_opacity=0.15).rotate(np.arctan2(1.6,2.0)).move_to(mag),
                 label('magnet: turns\nthe spin',mag[0]-0.9,mag[1]+0.95,21,PURPLE),
                 label('this path is\nleft alone',-4.9,-2.35,21,MUTED),
                 label('neutrons',src[0]+0.3,src[1]+0.4,21),
                 label('plates cut from one\nsilicon crystal split\nthe wave and bring\nit together',-3.25,-0.75,20,TEAL),
                 Rectangle(width=0.5,height=0.9,color=INK,fill_color=INK,fill_opacity=1).move_to(det+[0.25,0,0]),label('counter',det[0]+0.3,det[1]-0.8,21))
        ax=Axes(x_range=[0,720,180],y_range=[0,1.15,1],x_length=5.6,y_length=2.9,axis_config={'color':MUTED,'stroke_width':2,'include_tip':False}).move_to([4.2,-0.5,0])
        curve=ax.plot(lambda d:0.5*(1+np.cos(np.radians(d)/2)),x_range=[0,720],color=BLUE,stroke_width=5)
        self.add(ax,curve,label('count at the counter',4.2,1.45,22,BLUE))
        for d,s in [(0,r'0^\circ'),(360,r'360^\circ'),(720,r'720^\circ')]:
            q=ax.c2p(d,0); self.add(math(s,q[0],q[1]-0.35,26))
        self.add(label('angle the spin was turned through',4.2,-2.85,21,MUTED),
                 Dot(ax.c2p(360,0),radius=0.09,color=ORANGE),label('the two paths cancel',4.2,0.25,21,ORANGE),
                 Line([4.2,0.0,0],ax.c2p(360,0.06),color=ORANGE,stroke_width=2))
        self.add(label('After 360° of turn the paths cancel. The count comes back only at 720°.'.replace('°',' degrees'),0,-3.75,23,MUTED,width=14.5))



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


class HclExperiments(Scene):
    def construct(self):
        heading(self,'Heating hydrogen chloride gas','Heat needed per kelvin, in J/(mol K), at fixed volume, near room temperature')
        base=-2.4; scale=0.55; x1,x2=-1.6,2.2
        y=base
        for name,val,c in [('moving',1.5,TEAL),('rotating',1.0,PURPLE),('vibrating',1.0,ORANGE)]:
            h=val*scale*2
            self.add(Rectangle(width=1.8,height=h,stroke_width=0,fill_color=c,fill_opacity=0.85).move_to([x1,y+h/2,0]),
                     label(name,x1-2.0,y+h/2,22,c))
            y+=h
        hm=2.5*scale*2
        self.add(Rectangle(width=1.8,height=hm,stroke_width=0,fill_color=BLUE,fill_opacity=0.85).move_to([x2,base+hm/2,0]),
                 Line([x1-1.3,base,0],[x2+1.3,base,0],color=MUTED),
                 math(r'\tfrac72 R = 29.1',x1,y+0.35,26),math(r'\tfrac52 R = 20.8',x2,base+hm+0.35,26,BLUE),
                 label('classical prediction',x1,base-0.4,22,INK),label('measured',x2,base-0.4,22,BLUE),
                 label('The measured value matches the prediction with the vibration left out.',0,-3.55,22,MUTED,width=12))

class CoherentState(Scene):
    def construct(self):
        heading(self,'A coherent state swings without spreading','The lowest state shifted to one side keeps its width while its average goes round')
        # Left: position density at four times.
        swing=2.2; w=0.45
        for i,(lab,c) in enumerate([(r'\omega t=0',np.cos(0)),(r'\omega t=\pi/2',np.cos(np.pi/2)),(r'\omega t=\pi',np.cos(np.pi)),(r'\omega t=3\pi/2',np.cos(3*np.pi/2))]):
            yb=1.55-1.2*i
            ax=Axes(x_range=[-3.6,3.6,1],y_range=[0,1,1],x_length=6.0,y_length=0.95,tips=False,
                    axis_config={'color':MUTED,'include_ticks':False}).move_to([-3.6,yb+0.35,0])
            mu=swing*c
            self.add(ax,ax.plot(lambda u,mu=mu:np.exp(-(u-mu)**2/(2*w*w)),x_range=[-3.6,3.6],color=BLUE,stroke_width=3),
                     math(lab,-7.25,yb+0.25,21))
        self.add(label('position density',-3.6,-3.1,20,MUTED))
        # Right: the averages go round, each with the same small spread.
        cx,cy,R=3.9,-0.3,2.0
        self.add(Circle(radius=R,color=MUTED,stroke_width=2).move_to([cx,cy,0]),
                 math('X',cx+R+0.9,cy,26),math('P',cx,cy+R+0.75,26))
        for th in [0,np.pi/2,np.pi,3*np.pi/2]:
            p=[cx+R*np.cos(-th),cy+R*np.sin(-th),0]
            self.add(Circle(radius=0.41,color=BLUE,fill_color=BLUE,fill_opacity=0.25,stroke_width=2).move_to(p))
        self.add(Arrow([cx+R*np.cos(0.5),cy+R*np.sin(0.5),0],[cx+R*np.cos(0.15),cy+R*np.sin(0.15),0],buff=0,color=ORANGE,
                       stroke_width=4,max_tip_length_to_length_ratio=0.5),
                 label('averages in scaled coordinates; circles mark the spreads',cx,cy-R-0.6,19,MUTED,width=6.2))
        self.add(math(r'\text{Swing drawn about 5 times the spread. For chapter 1\textquoteright s spring it is }2\times10^{17}\text{ times.}',0,-3.65,22,MUTED,width=14.5))


class StepsVsThermal(Scene):
    def construct(self):
        heading(self,'One step of energy against the thermal energy','HCl at 300 K, energies above the bottom rung in units of the thermal energy')
        top=15.0; y0=-2.6; H=5.6
        Y=lambda e:y0+H*e/top
        self.add(Line([-6.2,y0,0],[6.2,y0,0],color=MUTED))
        # vibration ladder
        for e in (0.0,13.8):
            self.add(Line([-5.4,Y(e),0],[-2.6,Y(e),0],color=ORANGE,stroke_width=5))
        self.add(label('vibration',-4.0,y0-0.4,24,ORANGE),
                 math(r'13.8\,k_BT',-1.6,Y(13.8),24,ORANGE))
        # thermal bar
        self.add(Rectangle(width=0.9,height=Y(1)-y0,stroke_width=0,fill_color=BLUE,fill_opacity=0.8).move_to([0,(Y(1)+y0)/2,0]),
                 math(r'k_BT',0,Y(1)+0.35,24,BLUE),label('thermal\nenergy',0,y0-0.55,22,BLUE))
        # rotation ladder, E_J = 0.05 J(J+1) k_BT
        J=0
        while 0.05*J*(J+1)<=top:
            e=0.05*J*(J+1)
            self.add(Line([2.6,Y(e),0],[5.4,Y(e),0],color=PURPLE,stroke_width=3))
            J+=1
        self.add(label('rotation',4.0,y0-0.4,24,PURPLE),
                 math(r'\text{first step}',6.55,Y(0.1)+1.65,20,PURPLE),math(r'0.1\,k_BT',6.55,Y(0.1)+1.25,20,PURPLE),
                 Arrow([6.4,Y(0.1)+1.0,0],[5.5,Y(0.1),0],buff=0,color=PURPLE,stroke_width=3,max_tip_length_to_length_ratio=0.18))
        self.add(math(r'\text{A collision trades about one }k_BT\text{. It almost never reaches the first vibration rung, but often moves a molecule up the rotation rungs.}',0,-3.6,22,MUTED,width=14.5))


class LightClock(Scene):
    def construct(self):
        heading(self,'A moving light clock ticks slower','Light travels at the same speed in both pictures, but the moving clock gives it a longer path')
        top,bot=1.6,-1.6
        # Left: the clock at rest.
        cx=-4.6
        for y in (top,bot):
            self.add(Line([cx-0.9,y,0],[cx+0.9,y,0],color=INK,stroke_width=6))
        self.add(Arrow([cx-0.15,bot+0.08,0],[cx-0.15,top-0.08,0],buff=0,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.08),
                 Arrow([cx+0.15,top-0.08,0],[cx+0.15,bot+0.08,0],buff=0,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.08),
                 label('at rest',cx,top+0.6,26),
                 label('straight up and back',cx,bot-0.55,22,MUTED))
        # Right: the clock moving to the right, drawn at three moments.
        xs=[-0.2,2.4,5.0]
        for i,x in enumerate(xs):
            op=1.0 if i==1 else 0.35
            for y in (top,bot):
                self.add(Line([x-0.9,y,0],[x+0.9,y,0],color=INK,stroke_width=6,stroke_opacity=op))
        self.add(Arrow([xs[0],bot+0.08,0],[xs[1],top-0.08,0],buff=0,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.07),
                 Arrow([xs[1],top-0.08,0],[xs[2],bot+0.08,0],buff=0,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.07),
                 Arrow([1.4,top+0.55,0],[3.4,top+0.55,0],buff=0,color=BLUE,stroke_width=4,max_tip_length_to_length_ratio=0.15),
                 label('moving',2.4,top+1.05,26),
                 label('the same trip, slanted and longer',2.4,bot-0.55,22,MUTED))
        self.add(label('Same speed, longer path, so each tick takes longer: the moving clock runs slow.',0,-3.6,24,MUTED,width=14.5))


class MuonCounts(Scene):
    def construct(self):
        heading(self,'Muons reaching sea level','Frisch and Smith, 1963: muons per hour at the top of Mount Washington and at sea level')
        base=-2.2; scale=4.3/563
        for x,val,txt,c in [(-4,563,'at the top\n(1,907 m up)',BLUE),(0,31,'at sea level, if\nclocks ran normally',MUTED),(4,408,'at sea level,\nmeasured',ORANGE)]:
            h=val*scale
            self.add(Rectangle(width=2.0,height=h,stroke_width=0,fill_color=c,fill_opacity=0.85).move_to([x,base+h/2,0]),
                     label(f'about {round(val,-1):,}' if val>100 else 'about 30',x,base+h+0.35,24,c),
                     label(txt,x,base-0.6,21,INK))
        self.add(Line([-5.6,base,0],[5.6,base,0],color=MUTED),
                 label('The trip down takes about three lifetimes, but the moving muons’ clocks run about 9 times slow.',0,-3.75,22,MUTED,width=14.5))


class TrainFlash(Scene):
    def construct(self):
        heading(self,'“At the same time” depends on who’s watching','A lamp flashes in the middle of a carriage moving to the right')
        def carriage(cx,cy):
            return Rectangle(width=5.0,height=1.3,color=INK,stroke_width=4).move_to([cx,cy,0])
        # Top: on the train, both walls are hit together.
        cy=1.0; cx=0
        self.add(label('On the train',-5.4,cy+0.95,24),carriage(cx,cy),
                 Dot([cx,cy,0],color=ORANGE,radius=0.12),
                 Arrow([cx,cy,0],[cx-2.45,cy,0],buff=0.15,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.12),
                 Arrow([cx,cy,0],[cx+2.45,cy,0],buff=0.15,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.12),
                 Star(5,outer_radius=0.22,color=TEAL,fill_opacity=1).move_to([cx-2.5,cy,0]),
                 Star(5,outer_radius=0.22,color=TEAL,fill_opacity=1).move_to([cx+2.5,cy,0]),
                 label('light reaches both walls together',4.6,cy+0.95,21,TEAL))
        # Bottom: from the platform, the carriage has moved on; the back wall meets the light first.
        cy=-1.7; shift=0.9
        self.add(label('From the platform',-5.0,cy+0.95,24),
                 carriage(cx,cy).set_stroke(opacity=0.3),carriage(cx+shift,cy),
                 Dot([cx,cy,0],color=ORANGE,radius=0.12).set_opacity(0.5),
                 Arrow([cx,cy,0],[cx+shift-2.5,cy,0],buff=0.15,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.25),
                 Arrow([cx,cy,0],[cx+1.6,cy,0],buff=0.15,color=ORANGE,stroke_width=4,max_tip_length_to_length_ratio=0.12),
                 Star(5,outer_radius=0.22,color=TEAL,fill_opacity=1).move_to([cx+shift-2.5,cy,0]),
                 Arrow([3.8,cy+0.95,0],[5.4,cy+0.95,0],buff=0,color=BLUE,stroke_width=4,max_tip_length_to_length_ratio=0.2),
                 label('the back wall meets the light first;\nthe front wall is still running away',4.4,cy-1.15,21,TEAL))
        self.add(label('Light’s speed is the same for both observers, so they disagree about whether the walls are hit together.',0,-3.75,22,MUTED,width=14.5))


class MichelsonMorley(Scene):
    def construct(self):
        heading(self,'The Michelson–Morley experiment','One beam split in two, sent along arms at right angles, and recombined')
        S=np.array([-2.2,-0.7,0]); src=np.array([-6.0,-0.7,0])
        m1=np.array([2.0,-0.7,0]); m2=np.array([-2.2,2.0,0]); scr=np.array([-2.2,-2.9,0])
        beam=lambda a,b,**k:Line(a,b,color=ORANGE,stroke_width=4,**k)
        d=0.09
        self.add(beam(src,S),
                 beam(S+[0,d,0],m1+[-0.05,d,0]),beam(m1+[-0.05,-d,0],S+[0,-d,0]),
                 beam(S+[-d,0,0],m2+[-d,-0.05,0]),beam(m2+[d,-0.05,0],S+[d,0,0]),
                 beam(S,scr+[0,0.12,0]))
        self.add(Rectangle(width=0.7,height=0.5,color=INK,fill_color=INK,fill_opacity=1).move_to(src+[-0.35,0,0]),
                 label('lamp',src[0]-0.35,src[1]-0.55,21),
                 Line(S+[-0.4,-0.4,0],S+[0.4,0.4,0],color=TEAL,stroke_width=7),
                 label('half-silvered mirror:\nsplits the beam',S[0]-1.75,S[1]+0.85,20,TEAL),
                 Line(m1+[0,-0.6,0],m1+[0,0.6,0],color=INK,stroke_width=8),label('mirror',m1[0]+0.65,m1[1],21),
                 Line(m2+[-0.6,0,0],m2+[0.6,0,0],color=INK,stroke_width=8),label('mirror',m2[0]+1.05,m2[1],21),
                 label('arm 1',(S[0]+m1[0])/2,S[1]+0.4,21,MUTED),label('arm 2',S[0]+0.55,(S[1]+m2[1])/2,21,MUTED))
        # Screen with bands.
        for i in range(7):
            self.add(Rectangle(width=0.22,height=0.45,stroke_width=0,fill_color=ORANGE if i%2==0 else INK,
                               fill_opacity=0.85 if i%2==0 else 0.75).move_to(scr+[(i-3)*0.22,-0.15,0]))
        self.add(label('bands of light and dark',scr[0]+2.6,scr[1]-0.15,21))
        # Expected wind.
        for y in (1.6,0.6,-0.4):
            self.add(Arrow([3.6,y,0],[5.6,y,0],buff=0,color=BLUE,stroke_width=3,max_tip_length_to_length_ratio=0.12))
        self.add(label('expected “wind”\nas the Earth moves',4.6,-1.25,21,BLUE),
                 label('Turning the apparatus swaps which arm faces the wind, so the bands should slide. They barely moved.',0,-3.75,22,MUTED,width=14.5))


class PendulumForces(Scene):
    def construct(self):
        heading(self,'Why one pendulum is easy and two are not','Blue arrows show how each bob is moving; orange arrows show a string pulling on it')
        def unit(a,b):
            v=np.array(b,dtype=float)-np.array(a,dtype=float); return v/np.linalg.norm(v)
        def pend(piv,bob):
            return VGroup(Line(piv+[-0.4,0,0],piv+[0.4,0,0],color=INK,stroke_width=6),
                          Line(piv,bob,color=MUTED,stroke_width=3),Dot(bob,color=INK,radius=0.14))
        def arr(at,d,c,L=1.3):
            return Arrow(at,at+L*d,buff=0,color=c,stroke_width=5,max_tip_length_to_length_ratio=0.22)
        def vert(piv,L):
            return DashedVMobject(Line(piv,piv+[0,-L,0],color=MUTED,stroke_width=2),num_dashes=12)
        def ang(piv,th,r,tex,off=0.35):
            a=Arc(radius=r,start_angle=-PI/2,angle=th,arc_center=piv,color=INK,stroke_width=3)
            mid=-PI/2+th/2
            return VGroup(a,math(tex,piv[0]+(r+off)*np.cos(mid),piv[1]+(r+off)*np.sin(mid),30))
        # One pendulum: the string pulls at right angles to the motion.
        piv=np.array([-4.6,2.0,0]); th=np.radians(30); bob=piv+2.6*np.array([np.sin(th),-np.cos(th),0])
        mv=np.array([np.cos(th),np.sin(th),0]); pull=unit(bob,piv)
        mid=(piv+bob)/2
        self.add(vert(piv,2.9),ang(piv,th,0.8,r'\theta',0.3),math(r'\ell',mid[0]+0.3,mid[1]+0.1,30),
                 pend(piv,bob),arr(bob,mv,BLUE),arr(bob,pull,ORANGE,1.1),
                 label('one pendulum',-4.6,2.55,26),
                 label('the string pulls at right angles\nto the motion, so it never\nspeeds the bob up or slows it',-4.4,-2.3,22,MUTED))
        # Two pendulums: the lower string tugs the upper bob at an angle to its motion.
        piv2=np.array([2.6,2.1,0]); t1=np.radians(25); t2=np.radians(-22)
        b1=piv2+2.0*np.array([np.sin(t1),-np.cos(t1),0]); b2=b1+1.9*np.array([np.sin(t2),-np.cos(t2),0])
        self.add(vert(piv2,2.3),ang(piv2,t1,0.75,r'\theta_1',0.55),vert(b1,2.1),ang(b1,t2,0.7,r'\theta_2',0.55),
                 pend(piv2,b1),Line(b1,b2,color=MUTED,stroke_width=3),Dot(b2,color=INK,radius=0.14),
                 arr(b1,np.array([np.cos(t1),np.sin(t1),0]),BLUE),
                 arr(b1,unit(b1,b2),ORANGE,1.1),
                 label('two pendulums',2.6,2.65,26),
                 label('the lower string tugs the upper bob\nat an angle to its motion, so its pull\nmust be worked out first',4.2,-2.3,22,MUTED))


class TiltCircle(Scene):
    def construct(self):
        heading(self,'Same lean, different directions','Atoms leaning by the same amount from vertical, toward the right, the front and the left')
        o=np.array([-4.0,-2.5,0]); top=np.array([-4.0,0.9,0]); R=2.3; r=0.8
        ring=lambda deg:top+np.array([R*np.cos(np.radians(deg)),r*np.sin(np.radians(deg)),0])
        dirs=((-25,BLUE,'leans right'),(-115,ORANGE,'leans toward the front'),(155,TEAL,'leans left'))
        self.add(DashedVMobject(Line(o,top+[0,1.2,0],color=MUTED,stroke_width=3),num_dashes=18),
                 label('vertical',top[0],top[1]+1.45,22,MUTED),
                 Ellipse(width=2*R,height=2*r,color=MUTED,stroke_width=2,stroke_opacity=0.6).move_to(top))
        for deg,name in ((-25,'right'),(65,'back'),(155,'left'),(-115,'front')):
            q=ring(deg); d=(q-top)/np.linalg.norm(q-top)
            if name=='front':
                self.add(label(name,-4.45,0.0,20,MUTED)); continue
            self.add(label(name,q[0]+0.55*d[0],q[1]+0.4*d[1]+(0.12 if deg in (65,155) else -0.12),20,MUTED))
        for deg,c,_ in dirs:
            q=ring(deg)
            self.add(DashedVMobject(Line(top,q,color=c,stroke_width=2,stroke_opacity=0.6),num_dashes=7),
                     Arrow(o,q,buff=0,color=c,stroke_width=7,max_tip_length_to_length_ratio=0.07))
        self.add(label('all lean the same amount',o[0],o[1]-0.45,20,INK))
        def bars(x,y,vals,names,c):
            g=VGroup()
            for i,(v,n) in enumerate(zip(vals,names)):
                h=1.0*v/100; xx=x+i*0.95
                g.add(Rectangle(width=0.7,height=max(h,0.02),stroke_width=0,fill_color=c,fill_opacity=0.85).move_to([xx,y+h/2,0]),
                      label(n,xx,y-0.22,17,MUTED))
            return g
        self.add(label('vertical magnet',2.35,2.55,22,INK),label('sideways magnet',5.6,2.55,22,INK))
        rows=((0.95,[93,7]),(-0.75,[50,50]),(-2.45,[7,93]))
        for (deg,c,name),(y,side) in zip(dirs,rows):
            self.add(label(name,-0.05,y+0.45,19,c,width=2.2),
                     bars(1.9,y,[75,25],['up','down'],c),bars(5.15,y,side,['right','left'],c))
        self.add(label('the same',2.35,-3.25,20,INK),label('different',5.6,-3.25,20,INK))
        self.add(label('A vertical magnet only sees how far the atoms lean. A sideways magnet also sees which way.',0,-3.8,21,MUTED,width=14.5))


class SpinPrecession(Scene):
    def construct(self):
        heading(self,'The tilted spin swings round the field','In a vertical magnetic field, the tilt sweeps a cone; up and down stay 75% and 25% throughout')
        o=np.array([-3.2,-2.0,0]); top=np.array([-3.2,-0.672,0]); R=2.3; r=0.65  # R/height = tan 60 degrees
        ftip=top+np.array([0,r+1.3,0])
        self.add(Arrow(o,ftip,buff=0,color=MUTED,stroke_width=4,max_tip_length_to_length_ratio=0.05),
                 label('field',ftip[0]-0.6,ftip[1]-0.15,22,MUTED),
                 Ellipse(width=2*R,height=2*r,color=MUTED,stroke_width=2).move_to(top),
                 DashedVMobject(Line(o,top+[-R,0,0],color=MUTED,stroke_width=2,stroke_opacity=0.5),num_dashes=14),
                 DashedVMobject(Line(o,top+[R,0,0],color=MUTED,stroke_width=2,stroke_opacity=0.5),num_dashes=14))
        stops=[('right',top+[R,0,0],'93% right',RIGHT),('back',top+[0,r,0],'50% right',UR),
               ('left',top+[-R,0,0],'7% right',LEFT),('front',top+[0,-r,0],'50% right',DR)]
        for name,pt,chance,d in stops:
            g=VGroup(label(name,0,0,22,INK),label(chance,0,0,20,TEAL)).arrange(DOWN,buff=0.08)
            g.next_to(pt,d,buff=0.22)
            if name=='front':
                g.next_to(pt,LEFT,buff=0.25).shift(DOWN*0.05)
                self.add(BackgroundRectangle(g,color=WHITE,fill_opacity=1,buff=0.06))
            self.add(Dot(pt,color=BLUE,radius=0.09),g)
        self.add(Arrow(o,top+[R,0,0],buff=0,color=BLUE,stroke_width=6,max_tip_length_to_length_ratio=0.06),
                 CurvedArrow(top+[R*0.75,r*0.66,0],top+[R*0.2,r*0.98,0],color=ORANGE,stroke_width=3,tip_length=0.18))
        # Right: the chance of "right" over one turn.
        ax=axes_at(3.6,-0.3,5.6,3.4,(0,1,0.25),(0,1,0.5)); self.add(ax)
        f=lambda u:0.5+np.sqrt(3)/4*np.cos(2*np.pi*u)
        self.add(path_curve(ax,f,[0,1],TEAL))
        for u,name in ((0,'right'),(0.25,'back'),(0.5,'left'),(0.75,'front'),(1,'right')):
            self.add(Dot(ax.c2p(u,f(u)),color=BLUE,radius=0.07),label(name,ax.c2p(u,0)[0],ax.c2p(u,0)[1]-0.32,18,MUTED))
        self.add(label('chance of \u201cright\u201d',3.6,1.75,22,TEAL),label('one full turn of the tilt',3.6,-2.75,18,MUTED),
                 label('Up and down only see the lengths of the arrows; the sideways chances follow the angle between them.',0,-3.75,21,MUTED,width=14.5))


class WaveSum(Scene):
    def construct(self):
        heading(self,'Adding momentum waves of different wavelengths','At each point, the arrows of all the waves add; their total length sets where the particle is likely to be')
        xs=np.linspace(-15,15,27); k0=2*np.pi/6
        def one(x): return np.exp(1j*k0*x)
        def two(x): return 0.5*(np.exp(1j*k0*x)+np.exp(1j*2*np.pi/4.5*x))
        ks=np.linspace(k0-0.9,k0+0.9,61); w=np.exp(-(ks-k0)**2/(2*0.25**2)); w/=w.sum()
        def many(x): return np.sum(w*np.exp(1j*ks*x))
        rows=[(1.45,one,'one wavelength','arrow length the same everywhere'),
              (-0.35,two,'two wavelengths','length rises and falls'),
              (-2.15,many,'many wavelengths','one bump: the particle is near one place')]
        X0,X1=-4.6,6.6; L=0.4
        for y,f,name,note in rows:
            self.add(Line([X0-0.2,y,0],[X1+0.2,y,0],color=MUTED,stroke_width=1.5,stroke_opacity=0.5),
                     label(name,-6.0,y+0.05,22,INK),label(note,(X0+X1)/2,y-0.85,20,TEAL))
            for x in xs:
                z=f(x); r=abs(z); px=X0+(x+15)/30*(X1-X0)
                if r*L<0.04:
                    self.add(Dot([px,y,0],radius=0.03,color=BLUE)); continue
                d=np.array([np.cos(np.angle(z)),np.sin(np.angle(z)),0])*r*L
                self.add(Arrow([px,y,0]-d/2,[px,y,0]+d/2,buff=0,color=BLUE,stroke_width=3,max_tip_length_to_length_ratio=0.35,max_stroke_width_to_length_ratio=12))
        self.add(label('position along the line',(X0+X1)/2,-3.45,20,MUTED),
                 label('More wavelengths, so more momenta, gather the particle into one bump.',0,-3.85,21,MUTED,width=14.5))


class TwoRoutes(Scene):
    def construct(self):
        heading(self,'Why the stripes alternate','Each route’s arrow turns one full turn per wavelength; the routes to a spot differ in length')
        bx=-4.6; sx=-0.6; A=np.array([bx,0.75,0]); B=np.array([bx,-0.75,0])
        P=np.array([sx,0.0,0]); Q=np.array([sx,1.9,0])
        self.add(Line([bx,2.6,0],[bx,0.95,0],color=INK,stroke_width=6),Line([bx,0.55,0],[bx,-0.55,0],color=INK,stroke_width=6),
                 Line([bx,-0.95,0],[bx,-2.6,0],color=INK,stroke_width=6),Line([sx,2.6,0],[sx,-2.6,0],color=MUTED,stroke_width=4),
                 label('A',bx-0.35,0.75,22,TEAL),label('B',bx-0.35,-0.75,22,PURPLE),label('screen',sx,-2.95,20,MUTED))
        self.add(Line(A,P,color=TEAL,stroke_width=3),Line(B,P,color=PURPLE,stroke_width=3),
                 DashedVMobject(Line(A,Q,color=TEAL,stroke_width=3),num_dashes=20),DashedVMobject(Line(B,Q,color=PURPLE,stroke_width=3),num_dashes=22),
                 Dot(P,color=ORANGE,radius=0.1),Dot(Q,color=INK,radius=0.1),
                 label('bright spot',sx+0.95,P[1],20,ORANGE),label('dark spot',sx+0.85,Q[1],20,INK))
        def pair(cx,cy,ang_b,title,sub,total,c):
            o=np.array([cx,cy,0]); L=0.9
            a=Arrow(o,o+L*RIGHT,buff=0,color=TEAL,stroke_width=6,max_tip_length_to_length_ratio=0.25)
            d=np.array([np.cos(ang_b),np.sin(ang_b),0])
            b=Arrow(o+np.array([0,-0.35,0]),o+np.array([0,-0.35,0])+L*d,buff=0,color=PURPLE,stroke_width=6,max_tip_length_to_length_ratio=0.25)
            return VGroup(label(title,cx+0.2,cy+0.75,22,c),a,b,label(sub,cx+0.2,cy-0.95,19,MUTED),label(total,cx+0.2,cy-1.35,20,c))
        self.add(pair(3.6,1.25,0,'at the bright spot','routes equally long: arrows match','together: length 2, chance 4',ORANGE),
                 pair(3.6,-1.55,PI,'at the dark spot','B half a wavelength longer: arrows opposite','together: length 0, chance 0',INK))
        self.add(label('Each route alone would give length 1, chance 1. Adding chances would always give 2.',0,-3.75,21,MUTED,width=14.5))

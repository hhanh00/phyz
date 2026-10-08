"""Portrait physics roadmap; render with pnpm docs:manim --page mindmap."""
from manim import *
from concept_diagrams import BLUE, INK, MUTED, ORANGE, PALE, PURPLE, TEAL, label, math

config.background_color = WHITE
config.frame_width = 12
config.frame_height = 20
AMBER, GREEN, HIGGS = '#d97706', '#059669', '#db2777'
CONNECTOR_WIDTH = 2.2

def node(text, point, width=2.0, height=0.72, color=BLUE, size=22, fill=PALE):
    shape = RoundedRectangle(width=width, height=height, corner_radius=0.14,
        stroke_color=color, stroke_width=2.4, fill_color=fill, fill_opacity=1).move_to(point)
    return VGroup(shape, label(text, point[0], point[1], size, INK, width - 0.20))

def edge(start, end, color=MUTED, buff=0.38):
    return Arrow(start, end, buff=buff, color=color, stroke_width=CONNECTOR_WIDTH,
        max_stroke_width_to_length_ratio=100,
        tip_length=.10, max_tip_length_to_length_ratio=0.35)

def cell(text, x, y, color, width=1.65, height=0.56):
    shape = Rectangle(width=width, height=height, stroke_color=color, stroke_width=2,
        fill_color=WHITE, fill_opacity=1).move_to([x, y, 0])
    return VGroup(shape, math(text, x, y, 24, INK, width - 0.25))

class PhysicsRoadmap(Scene):
    def construct(self):
        self.add(label('From mechanics to the Standard Model', 0, 9.35, 37),
                 label('Foundations converge into fields, interactions, and the observed particles.', 0, 8.83, 21, MUTED, 11.2))
        p = {
            'newton':(-5,7.65,0),'lagrange':(-3,7.65,0),'hamilton':(-.9,7.65,0),'qm':(1.2,7.65,0),
            'sr':(-1.2,6.3,0),'kg':(1.2,6.3,0),'spin':(-.9,5.1,0),'dirac':(1.2,5.1,0),
            'maxwell':(1.2,3.9,0),'cf':(4.15,5.1,0),'qft':(4.15,3.6,0),
            'scalar':(-3.65,2.2,0),'spinor':(0,2.2,0),'vector':(3.65,2.2,0),
            'higgs':(-3.65,1.02,0),'fermions':(0,1.02,0),'bosons':(3.65,1.02,0),
            'quarks':(-2.15,-.18,0),'electron':(0,-.18,0),'neutrino':(2.15,-.18,0),'photon':(4.45,-.18,0),
            'qcd':(-3.3,-1.45,0),'weak':(0,-1.45,0),'qed':(3.65,-1.45,0),
            'wch':(-1.05,-3.75,0),'wneut':(1.15,-2.65,0),'z':(1.05,-3.75,0),'gamma':(3.15,-3.75,0),
            'breaking':(-4.5,-.25,0),'mass':(-4.65,-2.65,0),'gluon':(-3.3,-3.75,0),
        }
        links=[('newton','lagrange',PURPLE),('lagrange','hamilton',PURPLE),('hamilton','qm',BLUE),
          ('qm','kg',BLUE),('sr','kg',BLUE),('kg','dirac',ORANGE),('spin','dirac',ORANGE),
          ('kg','cf',BLUE),('dirac','cf',ORANGE),('maxwell','cf',TEAL),('cf','qft',PURPLE),
          ('qft','scalar',BLUE),('qft','spinor',ORANGE),('qft','vector',TEAL),('scalar','higgs',BLUE),
          ('spinor','fermions',ORANGE),('vector','bosons',TEAL),('fermions','quarks',ORANGE),
          ('fermions','electron',ORANGE),('fermions','neutrino',ORANGE),('bosons','photon',TEAL),
          ('quarks','qcd',PURPLE),('electron','qed',PURPLE),('photon','qed',PURPLE),
          ('quarks','weak',PURPLE),('electron','weak',PURPLE),('neutrino','weak',PURPLE),
          ('weak','wch',TEAL),('weak','wneut',TEAL),('wneut','z',TEAL),('wneut','gamma',TEAL),
          ('qed','wneut',TEAL),('higgs','breaking',HIGGS),('breaking','mass',HIGGS),
          ('qcd','gluon',GREEN),('mass','wneut',HIGGS)]
        node_start = len(self.mobjects)
        self.add(
          node('Newton',p['newton'],1.45,color=PURPLE),node('Lagrangian',p['lagrange'],1.55,color=PURPLE,size=20),
          node('Hamiltonian',p['hamilton'],1.6,color=PURPLE,size=20),node('Quantum\nmechanics',p['qm'],1.7,.9,BLUE,20),
          node('Special relativity',p['sr'],1.85,color=BLUE,size=20),node('Klein–Gordon\nspin 0',p['kg'],1.75,.9,BLUE,19),
          node('Spin',p['spin'],1.35,color=ORANGE),node('Dirac\nspin 1/2',p['dirac'],1.55,.9,ORANGE,19),
          node('Maxwell\nspin 1',p['maxwell'],1.6,.9,TEAL,19),node('Classical fields',p['cf'],2.05,.9,PURPLE,23,'#f3edff'),
          node('Quantum field theory',p['qft'],2.15,.9,PURPLE,22,'#f3edff'),node('Klein–Gordon\nspin 0',p['scalar'],1.75,.9,BLUE,19),
          node('Dirac\nspin 1/2',p['spinor'],1.75,.9,ORANGE,19),node('Maxwell & Yang–Mills\nspin 1',p['vector'],2.35,.9,TEAL,19),
          node('Higgs',p['higgs'],1.45,color=HIGGS,fill='#fce7f3'),node('Fermions',p['fermions'],1.55,color=AMBER,fill='#fef3c7'),
          node('Bosons',p['bosons'],1.45,color=TEAL),node('Quarks',p['quarks'],1.45,color=AMBER,fill='#fef3c7'),
          node('Electron',p['electron'],1.45,color=AMBER,fill='#fef3c7'),node('Neutrino',p['neutrino'],1.45,color=AMBER,fill='#fef3c7'),
          node('Photon',p['photon'],1.45,color=TEAL),node('QCD /\nStrong Force',p['qcd'],1.85,.9,PURPLE,20,'#f3edff'),
          node('Weak force',p['weak'],1.65,color=PURPLE,fill='#f3edff'),node('QED / EM',p['qed'],1.75,color=PURPLE,fill='#f3edff'),
          node('W+, W-',p['wch'],1.5,color=GREEN,fill='#dcfce7'),node('W0, B',p['wneut'],1.5,color=TEAL),
          node('Z',p['z'],1.15,color=GREEN,fill='#dcfce7'),node('γ',p['gamma'],1.15,color=GREEN,fill='#dcfce7'),
          node('Symmetry\nbreaking',p['breaking'],1.65,.9,HIGGS,20,'#fce7f3'),
          node('Mass',p['mass'],1.35,color=HIGGS,fill='#fce7f3'),
          node('g',p['gluon'],1.45,color=GREEN,fill='#dcfce7'))
        nodes = dict(zip(p, self.mobjects[node_start:]))
        def boundary(key, toward):
            obj = nodes[key][0]
            center = obj.get_center()
            delta = np.array(toward) - center
            factor = min((obj.width / 2) / max(abs(delta[0]), 1e-9),
                         (obj.height / 2) / max(abs(delta[1]), 1e-9))
            return center + delta * factor
        segments = []
        for a,b,c in links:
            start, end = boundary(a,p[b]), boundary(b,p[a])
            self.add(edge(start,end,c,buff=.035).set_z_index(-1))
            segments.append((a,b,start,end,c))

        # Mark interior crossings, excluding shared endpoints and node interiors.
        crossings = []
        def cross(u,v):
            return u[0]*v[1]-u[1]*v[0]
        for i,(a,b,start,end,color) in enumerate(segments):
            direction = end-start
            for c,d,other_start,other_end,other_color in segments[i+1:]:
                if {a,b} & {c,d}:
                    continue
                other_direction = other_end-other_start
                denominator = cross(direction,other_direction)
                if abs(denominator) < 1e-8:
                    continue
                offset = other_start-start
                t = cross(offset,other_direction)/denominator
                u = cross(offset,direction)/denominator
                if not (.015 < t < .985 and .015 < u < .985):
                    continue
                point = start+t*direction
                if any(abs(point[0]-obj[0].get_center()[0]) < obj[0].width/2+.05
                       and abs(point[1]-obj[0].get_center()[1]) < obj[0].height/2+.05
                       for obj in nodes.values()):
                    continue
                if all(np.linalg.norm(point-existing[0]) > .16 for existing in crossings):
                    crossings.append((point,direction/np.linalg.norm(direction),color,
                                      other_direction/np.linalg.norm(other_direction),other_color))
        for point,direction,color,under_direction,under_color in crossings:
            radius=.09
            angle=np.arctan2(direction[1],direction[0])
            self.add(Line(point-radius*direction,point+radius*direction,
                          color=WHITE,stroke_width=7).set_z_index(2))
            self.add(Line(point-2*radius*under_direction,point+2*radius*under_direction,
                          color=under_color,stroke_width=CONNECTOR_WIDTH).set_z_index(3))
            self.add(Arc(radius=radius,start_angle=angle,angle=PI,
                         arc_center=point,color=color,stroke_width=CONNECTOR_WIDTH).set_z_index(4))
        self.add(label('reformulate',-4,8.18,15,MUTED),label('reformulate',-1.95,8.18,15,MUTED),
                 label('quantize',.12,8.25,16,BLUE),label('quantize',4.78,4.35,16,PURPLE))

        top=-5.05; xs=[-2.7,-.9,.9,2.7]
        headers=['Generation I','Generation II','Generation III','Gauge bosons']
        rows=[([r'u',r'c',r't',r'g'],[AMBER,AMBER,AMBER,GREEN]),
              ([r'd',r's',r'b',r'\gamma'],[AMBER,AMBER,AMBER,GREEN]),
              ([r'e',r'\mu',r'\tau',r'Z'],[AMBER,AMBER,AMBER,GREEN]),
              ([r'\nu_e',r'\nu_\mu',r'\nu_\tau',r'W^\pm'],[AMBER,AMBER,AMBER,GREEN])]
        positions={(ri,ci):np.array([xs[ci],top-.70*(ri+1),0]) for ri in range(4) for ci in range(4)}
        higgs_cell=np.array([0,top-3.75,0])
        def row_bus(source, row_indices, color, gutter=-5.45):
            for ri in row_indices:
                y=positions[(ri,0)][1]
                bus_y=y+.35
                title={'quarks':'Quarks','electron':'Electron','neutrino':'Neutrino'}[source]
                self.add(label(title,-4.6,y,17,color,width=1.55))
                self.add(Line([-3.72,y,0],[-3.62,y,0],color=color,stroke_width=CONNECTOR_WIDTH),
                         Line([-3.62,y,0],[-3.62,bus_y,0],color=color,stroke_width=CONNECTOR_WIDTH),
                         Line([-3.62,bus_y,0],[xs[2],bus_y,0],color=color,stroke_width=CONNECTOR_WIDTH))
                for ci in range(3):
                    self.add(Arrow([xs[ci],bus_y,0],[xs[ci],y+.28,0],buff=0,color=color,
                                   stroke_width=CONNECTOR_WIDTH,max_stroke_width_to_length_ratio=100,
                                   max_tip_length_to_length_ratio=.8))

        def gauge_link(source, row_index):
            target=positions[(row_index,3)]
            title={'gluon':'g','gamma':'γ','z':'Z','wch':'W+, W-'}[source]
            self.add(label(title,4.65,target[1],18,GREEN,width=1.45),
                     edge([4.05,target[1],0],[3.54,target[1],0],GREEN,buff=.015))

        row_bus('quarks',[0,1],AMBER)
        row_bus('electron',[2],AMBER)
        row_bus('neutrino',[3],AMBER)
        gauge_link('gluon',0); gauge_link('gamma',1); gauge_link('z',2); gauge_link('wch',3)
        self.add(label('Higgs',-2.25,higgs_cell[1],18,HIGGS),
                 edge([-1.75,higgs_cell[1],0],[-1.10,higgs_cell[1],0],HIGGS,buff=.015))
        self.add(label('Standard Model particles',0,top+.58,26))
        for x,text in zip(xs,headers):self.add(node(text,(x,top,0),1.65,.54,MUTED,16,'#f8fafc'))
        for ri,(values,colors) in enumerate(rows):
            for ci,(value,color) in enumerate(zip(values,colors)):self.add(cell(value,xs[ci],top-.70*(ri+1),color))
        self.add(node('Higgs',higgs_cell,2.15,.68,HIGGS,21,'#fce7f3'))
        self.add(label('Side labels continue the matching branches above.',0,-9.55,18,MUTED))

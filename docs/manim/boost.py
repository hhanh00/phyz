"""Correct coordinate axes for Galilean and Lorentz boosts (x vertical, t horizontal)."""
from manim import *
from concept_diagrams import label, math, arrow, heading, INK, MUTED, BLUE, ORANGE, TEAL
config.background_color=WHITE
config.frame_width=16
config.frame_height=9

class BoostDiagrams(Scene):
    def construct(self):
        heading(self,'A coordinate axis is a line on which the other coordinate vanishes','For v = 0.5 and c = 1; x is vertical and t is horizontal')
        for cx,lorentz in [(-4,False),(4,True)]:
            def pt(t,x):return [cx+t,x-.2,0]
            self.add(Line(pt(-2.3,0),pt(2.3,0),color=MUTED),Line(pt(0,-2.3),pt(0,2.3),color=MUTED))
            self.add(DashedLine(pt(-2.2,-2.2),pt(2.2,2.2),color=ORANGE),
                     Line(pt(-2.2,-1.1),pt(2.2,1.1),color=BLUE,stroke_width=4))
            if lorentz:self.add(Line(pt(-1.1,-2.2),pt(1.1,2.2),color=TEAL,stroke_width=4))
            else:self.add(Line(pt(0,-2.2),pt(0,2.2),color=TEAL,stroke_width=4))
            self.add(label('Lorentz' if lorentz else 'Galilean',cx,2.5,28),
                     math(r"t'",cx+2.45,.85,31,BLUE),math(r"x'",cx+(1.25 if lorentz else .25),2.18,31,TEAL),
                     math('t',cx+2.45,-.5,28),label('light',cx+1.6,1.8,22,ORANGE),
                     math(r"t'\text{ axis: }x'=0\ \Rightarrow\ x=vt",cx,-3.0,29,BLUE),
                     math(r"x'\text{ axis: }t'=0\ \Rightarrow\ "+('t=vx' if lorentz else 't=0'),cx,-3.65,29,TEAL))

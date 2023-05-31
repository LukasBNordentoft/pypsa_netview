#%%

from schemdraw.segments import Segment, util, math, SegmentCircle
from schemdraw.elements import Element

# ----- Define custom elements -----
class PyPSA_Gen(Element):
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment(
            [(0, 0), (0.75, 0)]))
        sin_y = util.linspace(-.25, .25, num=25)
        sin_x = [.2 * math.sin((sy-.25)*math.pi*2/.5) + 1.25 for sy in sin_y]
        self.segments.append(Segment(list(zip(sin_x, sin_y))))
        self.segments.append(SegmentCircle((1.25, 0), 0.5,))
        
class PyPSA_Load(Element):
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        lead = 0.95
        h = 0.8
        w = 0.5
        self.segments.append(Segment(
            [(0, 0), (0, lead), (-w, lead+h), (w, lead+h), (0, lead)]))
        self.params['drop'] = (0, 0)
        self.params['theta'] = 0
        self.anchors['start'] = (0, 0)
        self.anchors['center'] = (0, 0)
        self.anchors['end'] = (0, 0)
        
class PyPSA_Store(Element):
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        lead = 0.75
        h = lead + 1
        w = 1
        self.segments.append(Segment(
            [(0, 0), (lead, 0), (lead, w/2), (h, w/2),
              (h, -w/2), (lead, -w/2), (lead, 0)
              ]))

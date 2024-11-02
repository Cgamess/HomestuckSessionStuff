class entity2d:
    def __init__(self, xy, state): 
        if not isinstance(xy, (list, tuple)): raise TypeError(f"XY pair needs to be a list or a tuple not a {type(xy)}")
        self.x=xy[0]
        self.y=xy[1]
        self.state=state

class entity3d:
    def __init__(self, xyz, state): 
        if not isinstance(xyz, (list, tuple)): raise TypeError(f"XYZ needs to be a list or a tuple not a {type(xyz)}")
        self.x=xyz[0]
        self.y=xyz[1]
        self.x=xyz[2]
        self.state=state
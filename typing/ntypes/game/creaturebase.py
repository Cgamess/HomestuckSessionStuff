global tmap,change
class BaseEntityModel():
    def __init__(self):
        self.hp = 100
        self.dead = False
        self.anibuffer=[]
        self.color = [0, 0, 0]
        self.x, self.y, self.z, self.world = 0, 0, 0, 0
        self.tx, self.ty, self.tz = 0, 0, 0
        self.mx, self.my, self.mz = 0, 0, 0
        self.lcolor = [0, 0, 0]
        self.lx, self.ly, self.lz, self.lworld = 0, 0, 0, 0
        self.ltx, self.lty, self.ltz = 0, 0, 0
        self.lmx, self.lmy, self.lmz = 0, 0, 0
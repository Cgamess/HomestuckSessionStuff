import pygame as pg
from collections import deque

class uiobjects:
    def __init__(self, pygame : pg, active = 0) -> None:
        self.uiobjectlist : deque = deque([])
        self.active = active
    def new(self, pygame : pg, xy : tuple, objtype : int = 0):
        self.uiobjectlist.append(uiobject(pg, xy, objtype))
    def render(self, pygame : pg):
        if self.active:
            for i in self.uiobjectlist:
                i.render(pygame)

class uiobject:
    def __init__(self, pygame : pg, xy : tuple, objtype : int = 0, data={}) -> None:
        self.objtype=objtype
        self.xy=xy
    def render(self, pygame : pg):
        match self.objtype:

            case 0: 
                pass


            case _:
                pass
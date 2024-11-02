import colorama
from collections import deque
from time import perf_counter_ns
import json
import tkinter as tk
from tkinter import filedialog
import numpy as np
import time
import json

class imdict(dict):
    def __hash__(self):
        return id(self)

    def _immutable(self, *args, **kws):
        raise TypeError('object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear       = _immutable
    update      = _immutable
    setdefault  = _immutable
    pop         = _immutable
    popitem     = _immutable



class tlist(list):
    def _undefined():
        raise Exception("Error: undefined")
    def __init__(*stuff):
        super().__init__(stuff)
    # not done yet

class queue(tlist):
    def __init__(*stuff):
        super().__init__(stuff)
    def _undefined():
        raise Exception("Error: undefined")
    def ret(self):
        pass
    def swap(self):
        pass
    def pop(self):
        pass
    def retpop(self):
        var=self.ret()
        self.pop()
        return var


class jsonsavehandler:
    def __init__(self, path):
        self.basefile=open(path,"r+")
        self.path=path
    def refresh(self):
        self.basefile.close()
        self.basefile=open(self.path,"r+")
    def jsonread(self):
        tdata=self.read()
        data = json.loads(tdata)
        return data
    def read(self):
        self.refresh()
        return self.basefile.read()
    def write(self, data):
        self.basefile.write(data)
        self.basefile.flush
    def replace(self, data):
        self.olddata=self.jsonread()
        self.basefile.seek(0)
        self.basefile.truncate()
        self.write(data)
        self.basefile.flush()
    def jsonreplace(self, data):
        self.olddata=self.jsonread()
        self.basefile.seek(0)
        self.basefile.truncate()
        self.write(json.dumps(data))
        self.basefile.flush()
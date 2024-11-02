import math, time
class bit:
    def __init__(self, start:bool=False):
        self.val=start
    def __int__(self):
        return int(self.val)
    def __str__(self):
        return f"{self.val}"
class byte:
    def __init__(self, size=8, start:list[bit]|None|int=None):
        if type(start)==int:
            if start>(2**size):
                raise ValueError("Byte too large")
            binary_start=bin(start)[2:]
            binary_start=(("0"*size)+(binary_start))[-max(len(binary_start),size):][:size]
            start=[]
            for i in binary_start:
                start.append(bit({"0":0,"1":1}[i]))
        if start==None: start=[bit()]*size
        else:
            if type(start)==list:
                if len(start)!=size: raise ValueError(f"Length of the values stored in the byte ({len(start)}) needs to be equal to the bytes size ({size}), Value: {binary_start}")
        self.val=start
        self.size=size
    def __add__(self,other):
        return byte(self.size, self.__int__()+other.__int__()%256)
    def __int__(self):
        out=0
        for i in self.val:
            out*=2
            out+=int(i.val)
        return int(out)
    def __str__(self):
        out=0
        for i in self.val:
            out*=2
            out+=i.__int__()
        out=(str(hex(out))[2:].zfill(math.ceil(self.size / 4))[:math.ceil(self.size / 4)])
        return out

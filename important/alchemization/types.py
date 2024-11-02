class captialogCode:
    def __init__(self,validSizes:list[int],code:str):
        self.size=64
        self.validSizes=[i for i in validSizes if i>=8]
        self.binValidSizes=[i*6 for i in self.validSizes]
        self.code=code
        if len(self.code) not in validSizes:
            raise ValueError("Error, Invalid code (Not in validsizes list)")
        self.binaryCode=[f"{bin(int(i,self.size))}"[2:] for i in self.code]
        self.intCode=0
        for i in self.binaryCode:
            self.intCode+=i
            self.intCode*=2
        self.intCode//=2
#cc=captialogCode([8],"00000000")
#print(cc.intCode)
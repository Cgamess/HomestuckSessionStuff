from Types import captialogCode
def orList(vals:list[int|bool]):
    v=0
    for i in vals:
        v|=i
    return v
def andList(vals:list[int|bool]):
    v=vals[0]
    for i in vals:
        v&=i
    return v
def xorList(vals:list[int|bool]):
    v=0
    for i in vals:
        v^=i
    return v
def norList(vals:list[int|bool]):
    return int(not orList(vals))
def xnorList(vals:list[int|bool]):
    return int(not norList(vals))
def nandList(vals:list[int|bool]):
    return int(not andList(vals))


def Or(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]) -> captialogCode:
    binaryCodes=[i.binCode for i in codes]
    outCode=[]
    validSizes=[]
    for i in [i.valid_sizes for i in codes]:
        extension = [j for j in i if j not in validSizes]
        validSizes.extend(extension)
    lengths=[len(i) for i in binaryCodes]
    last=lengths[0]
    for i in lengths:
        if last != i:
            raise ValueError("Length of codes are not equivlent")
        last=i
    for idx, val in enumerate(binaryCodes[0]):
        outCode.append(orList([i[idx] for i in binaryCodes]))
        val=val
    #print(validSizes)
    #print(outCode,len(outCode))
    return(captialogCode(validSizes,outCode))
def And(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]) -> captialogCode:
    binaryCodes=[i.binCode for i in codes]
    outCode=[]
    validSizes=[]
    for i in [i.valid_sizes for i in codes]:
        extension = [j for j in i if j not in validSizes]
        validSizes.extend(extension)
    lengths=[len(i) for i in binaryCodes]
    last=lengths[0]
    for i in lengths:
        if last != i:
            raise ValueError("Length of codes are not equivlent")
        last=i
    for idx, val in enumerate(binaryCodes[0]):
        outCode.append(andList([i[idx] for i in binaryCodes]))
        val=val
    #print(validSizes)
    #print(outCode,len(outCode))
    return(captialogCode(validSizes,outCode))
def Xor(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]) -> captialogCode:
    binaryCodes=[i.binCode for i in codes]
    outCode=[]
    validSizes=[]
    for i in [i.valid_sizes for i in codes]:
        extension = [j for j in i if j not in validSizes]
        validSizes.extend(extension)
    lengths=[len(i) for i in binaryCodes]
    last=lengths[0]
    for i in lengths:
        if last != i:
            raise ValueError("Length of codes are not equivlent")
        last=i
    for idx, val in enumerate(binaryCodes[0]):
        outCode.append(xorList([i[idx] for i in binaryCodes]))
        val=val
    #print(validSizes)
    #print(outCode,len(outCode))
    return(captialogCode(validSizes,outCode))
def Nor(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]) -> captialogCode:
    binaryCodes=[i.binCode for i in codes]
    outCode=[]
    validSizes=[]
    for i in [i.valid_sizes for i in codes]:
        extension = [j for j in i if j not in validSizes]
        validSizes.extend(extension)
    lengths=[len(i) for i in binaryCodes]
    last=lengths[0]
    for i in lengths:
        if last != i:
            raise ValueError("Length of codes are not equivlent")
        last=i
    for idx, val in enumerate(binaryCodes[0]):
        outCode.append(norList([i[idx] for i in binaryCodes]))
        val=val
    #print(validSizes)
    #print(outCode,len(outCode))
    return(captialogCode(validSizes,outCode))
def Nand(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]) -> captialogCode:
    binaryCodes=[i.binCode for i in codes]
    outCode=[]
    validSizes=[]
    for i in [i.valid_sizes for i in codes]:
        extension = [j for j in i if j not in validSizes]
        validSizes.extend(extension)
    lengths=[len(i) for i in binaryCodes]
    last=lengths[0]
    for i in lengths:
        if last != i:
            raise ValueError("Length of codes are not equivlent")
        last=i
    for idx, val in enumerate(binaryCodes[0]):
        outCode.append(nandList([i[idx] for i in binaryCodes]))
        val=val
    #print(validSizes)
    #print(outCode,len(outCode))
    return(captialogCode(validSizes,outCode))
def Xnor(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]) -> captialogCode:
    binaryCodes=[i.binCode for i in codes]
    outCode=[]
    validSizes=[]
    for i in [i.valid_sizes for i in codes]:
        extension = [j for j in i if j not in validSizes]
        validSizes.extend(extension)
    lengths=[len(i) for i in binaryCodes]
    last=lengths[0]
    for i in lengths:
        if last != i:
            raise ValueError("Length of codes are not equivlent")
        last=i
    for idx, val in enumerate(binaryCodes[0]):
        outCode.append(xnorList([i[idx] for i in binaryCodes]))
        val=val
    #print(validSizes)
    #print(outCode,len(outCode))
    return(captialogCode(validSizes,outCode))

def Add(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]) -> captialogCode:
    intCodes=[i.intCode for i in codes]
    outCode=0
    validSizes=[]
    for i in [i.valid_sizes for i in codes]:
        extension = [j for j in i if j not in validSizes]
        validSizes.extend(extension)
    for val in intCodes:
        outCode+=val
    outCode%=2**(max(validSizes)*6)
    #print(validSizes)
    #print(outCode,len(outCode))
    return(captialogCode(validSizes,outCode))
def Subtract(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]) -> captialogCode:
    intCodes=[i.intCode for i in codes]
    outCode=intCodes[0]
    validSizes:list[int]=[]
    for i in [i.valid_sizes for i in codes]:
        extension = [j for j in i if j not in validSizes]
        validSizes.extend(extension)
    #print(len(intCodes),len(intCodes[1:]))
    for val in intCodes[1:]:
        outCode-=val
    outCode%=2**(max(validSizes)*6)
    #print(validSizes)
    #print(outCode,len(outCode))
    return(captialogCode(validSizes,outCode))
def Mult(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]) -> captialogCode:
    intCodes=[i.intCode for i in codes]
    outCode=intCodes[0]
    validSizes:list[int]=[]
    for i in [i.valid_sizes for i in codes]:
        extension = [j for j in i if j not in validSizes]
        validSizes.extend(extension)
    #print(len(intCodes),len(intCodes[1:]))
    for val in intCodes[1:]:
        outCode*=val
    #print(outCode)
    outCode%=2**(max(validSizes)*6)
    #print(validSizes)
    #print(outCode,len(outCode))
    return(captialogCode(validSizes,outCode))

"""
codes = [
    captialogCode([8],90),
    captialogCode([8],125),
    captialogCode([8],"Pchooooo"),
    captialogCode([8],90000),
]

for i in enumerate(codes): print(i[1], i[0])
print(Or(codes),"Or")
print(And(codes),"And")
print(Xor(codes),"Xor")
print(Nor(codes),"Nor")
print(Nand(codes),"Nand")
print(Xnor(codes),"Xnor")
print(Add(codes),"Add")
print(Subtract(codes),"Subtract")
print(Mult(codes),"Mult")


"""
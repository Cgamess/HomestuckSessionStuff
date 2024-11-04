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

def Or(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]):
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
def And(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]):
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
def Xor(codes:list[captialogCode]|tuple[captialogCode]|set[captialogCode]):
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

"""
codes = [
    captialogCode([8,48],90),
    captialogCode([8,48],125),
]
print(Or(codes))
print(And(codes))
print(Xor(codes))
"""
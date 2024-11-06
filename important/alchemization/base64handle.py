import base64

def captialogCodeBase64(data:str, decode=False):
    alphabets = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/','0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY(:)']
    table = {alphabets[decode][i[0]]: i[1] for i in enumerate(alphabets[(decode+1)%2])}
    if decode == 1:
        data=list[data]
        for i in enumerate(data):
            if i[1] in alphabets[0]: data[i[0]]=table[i[1]]
            else: data[i[0]]=i[1]
        data="".join(data)
        return base64.b64decode(data)
    else:
        out=base64.b64encode(data).decode()
        out=list(out)
        for i in enumerate(out):
            if i[1] in alphabets[0]: out[i[0]]=table[i[1]]
            else: out[i[0]]=i[1]
        out="".join(out)
        return out
        
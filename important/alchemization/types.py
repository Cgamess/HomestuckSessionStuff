import base64
from important.alchemization.base64handle import captialogCodeBase64 as CCB64

class captialogCode:
    def __init__(self, valid_sizes: list[int], code: str | int | list[int]):
        self.size = 64
        self.valid_sizes = [i for i in valid_sizes if i >= 1]
        if isinstance(code,list):
            if len(code) not in [i*6 for i in self.valid_sizes]:
                raise ValueError("Error: Invalid code length (Not in valid sizes list)")
        elif isinstance(code,str):
            if len(code) not in self.valid_sizes:
                raise ValueError("Error: Invalid code length (Not in valid sizes list)")
        self.strCode = ""
        self.intCode = 0
        self.binCode = []

        if isinstance(code, int):
            if not (0 <= code < (1 << max(self.valid_sizes)*6)):
                raise ValueError("Error: Integer code must be a 48-bit integer.")
            self.intCode = code
            self.binCode = [int(bit) for bit in f"{code:048b}"]
            byte_array = code.to_bytes(6, byteorder='big')
            self.strCode = CCB64(byte_array)

        elif isinstance(code, str):
            if len(code) not in self.valid_sizes or not all(c.isascii() for c in code):
                raise ValueError("Error: String code must be a valid Base64 string with appropriate length.")
            decoded_bytes = CCB64(code,1)
            self.binCode = [int(bit) for byte in decoded_bytes for bit in f"{byte:08b}"]
            #print(self.binCode)
            self.binCode = self.binCode[:len(code)*6]
            self.intCode = int(''.join(map(str, self.binCode)), 2)
            self.strCode = code

        elif isinstance(code, list):
            if len(code) not in [i*6 for i in valid_sizes] or not all(bit in (0, 1) for bit in code):
                raise ValueError("Error: List code must be a 48-length list of binary values (0 or 1).")
            self.binCode = code
            self.intCode = int(''.join(map(str, code)), 2)
            byte_array = int(''.join(map(str, code)), 2).to_bytes(6, byteorder='big')
            self.strCode = CCB64(byte_array)

        else:
            raise TypeError("Error: Code must be int, str, or list of int.")

    def __repr__(self):
        return (f"CaptialogCode(valid_sizes={self.valid_sizes}, "
                f"strCode='{self.strCode}', intCode={self.intCode}, "
                f"binCode={self.binCode})")

#cc=captialogCode([8],1)
#print(cc)
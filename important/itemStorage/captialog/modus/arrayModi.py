from important.alchemization.Types import captialogCode
from important.alchemization import arithmatic
from important.itemStorage.captialog.card.captiaCard import captiaCard
from important.itemStorage.captialog.modus.baseModus import baseModus, emptyCard

class arrayModus(baseModus):
    __name__="arrayModus"
    def pop(self,idx:int) -> captiaCard:
        item:captiaCard=self.items[idx]
        self.items[idx]=emptyCard
        return item
    def add(self,idx:int,item:captiaCard) -> None:
        self.items[idx]=item

class fifoModus(baseModus):
    __name__="fifoModus"
    def pop(self) -> captiaCard:
        item:captiaCard=self.items[0]
        self.items:list[captiaCard] = self.items[1:] + [emptyCard]
        return item
    def add(self,item:captiaCard) -> captiaCard:
        index:int|None=None
        for idx, Item in enumerate(self.items):
            if Item == emptyCard:
                index:int|None=idx
                break
        if index == None:
            Item=self.items[-1]
            self.items:list[captiaCard] = self.items[:-1] + [item]
            return Item
        else:
            self.items[index] = item

class filoModus(baseModus):
    __name__="fifoModus"
    def pop(self) -> captiaCard:
        item:captiaCard=self.items[0]
        self.items:list[captiaCard] = self.items[1:] + [emptyCard]
        return item
    def add(self,item:captiaCard) -> captiaCard:
        index:int|None=None
        for idx, Item in enumerate(self.items):
            if Item == emptyCard:
                index:int|None=idx
                break
        if index == None:
            Item=self.items[0]
            self.items:list[captiaCard] = self.items[1:] + [item]
            return Item
        else:
            self.items[index] = item
















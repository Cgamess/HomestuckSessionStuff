from important.alchemization.Types import captialogCode
from important.itemStorage.captialog.card.captiaCard import captiaCard
from important.alchemization import arithmatic
emptyCard=captiaCard({})

class baseModus:
    __name__="baseModus"
    def __init__(self, size:int, items:list[captiaCard]|tuple[captiaCard]|set[captiaCard]|None=None, debug:bool=False) -> None:
        self.size=size
        self.debug=debug
        if items: self.items=items
        else: self.items=[emptyCard]*size
        while len(self.items) < size: self.items.append(captiaCard({}))
    def __repr__(self) -> str:
        return f"{self.__name__}(size={self.size}, items={self.items})"
    def addCaptiaCard(self) -> None:
        self.items.append(emptyCard)
        self.size+=1
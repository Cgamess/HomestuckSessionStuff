from important.alchemization.arithmatic import captialogCode

class captiaCard:
    def __init__(self, items:dict[captialogCode:int],punched:bool=False) -> None:
        self.items:dict[captialogCode:list[int]]={i: [items[i],0] for i in items if i != None and (items[i])}
        self.items:dict[captialogCode:list[int]]={i: [self.items[i[1]][0], i[0]] for i in enumerate(self.items)}
        self.punched:bool=punched
    def addItem(self, item:captialogCode|None, count:int) -> None:
        if (not count) or item == None or self.punched:
            return
        if item in self.items:
            self.items[item][0]+=count
        else:
            self.items[item]=[count,max([self.items[i][1] for i in self.items])+1]
    def takeItem(self, Id:int, count:int):
        if self.punched: return
        captiaCode:captialogCode=[self.items[i] for i in self.items if self.items[i][1]==Id][0]
        item:dict[captialogCode:int] = {captiaCode:min(self.items[captiaCode][0],count)}
        if self.items[captiaCode][0] <= count: 
            self.items.pop(captiaCode)
            self.items:dict[captialogCode:list[int]]={i: [self.items[i][0], max([0]+[self.items[i][1] for i in self.items])+1] for i in self.items}
        if count > 0: return item
    def takeItemByCaptialogCode(self, captiaCode:captialogCode, count:int):
        if self.punched: return
        item:dict[captialogCode:int] = {captiaCode:min(self.items[captiaCode][0],count)}
        if self.items[captiaCode][0] <= count: 
            self.items.pop(captiaCode)
            self.items:dict[captialogCode:list[int]]={i: [self.items[i[1]][0], i[0]] for i in enumerate(self.items)}
        if count > 0: return item
    def listItems(self):
        return self.items
    def getItemInfo(self, Id):
        captiaCode:captialogCode=[self.items[i] for i in self.items if self.items[i][1]==Id][0]
        item:dict[captialogCode:int] = {captiaCode:self.items[captiaCode][0]}
        return item
    def getItemInfoByCaptialogCode(self, captiaCode:captialogCode):
        item:dict[captialogCode:list[int]] = {captiaCode:self.items[captiaCode]}
        return item
    def removeItem(self):
        while not self.punched:
            Id, count = 0, 1
            captiaCode=[self.items[i] for i in self.items if self.items[i][1]==Id][0]
            item = {captiaCode:min(self.items[captiaCode][0],count)}
            if self.items[captiaCode][0] <= count: 
                self.items.pop(captiaCode)
                self.items={i: [self.items[i][0], max([0]+[self.items[i][1] for i in self.items])+1] for i in self.items}
            yield item
    def __repr__(self) -> str:
        return f"captiaCard(items={self.items}, punched={self.punched})"
    def __add__(self, other):
                if self.punched: return NotImplemented
                if isinstance(other, captiaCard):
                    outItems={i: self.items[i][0] for i in self.items}
                    outItems.update({i: other.items[i][0] for i in other.items})
                    return captiaCard(outItems)
                elif isinstance(other, captialogCode):
                    tempCard:captiaCard=self
                    tempCard.addItem(other,1)
                    return tempCard
                else:
                    return NotImplemented




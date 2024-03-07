class grandparent:
    def __init__(self) -> None:
        pass
    def property(self):
        print("I have 5 corer  taka")

class parent(grandparent):
    def property(self):
        print("IHAVE 3 CORE")
    def __init__(self) -> None:
        super().__init__()

class chid(parent):
    def property(self):
        print("i have 2 core")
    def __init__(self) -> None:
        super().__init__()

ami=chid()
ami.property()

baba=parent()
baba.property()

dada=grandparent()
dada.property()
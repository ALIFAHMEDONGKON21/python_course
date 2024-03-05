from math import pi

class shape:
    def __init__(self,name) -> None:
        self.name=name

class rectangle(shape):
    def __init__(self, name,length,width) -> None:
        self.legtht=length
        self.width=width
        super().__init__(name)
    
    def area(self):
        return self.width*self.legtht
    
class circle(shape):
    def __init__(self, name,radius) -> None:
        self.radius=radius
        super().__init__(name)
    
    def area(self):
        return pi*self.radius*self.radius

goal=rectangle('3',3,3)
print(goal.area())
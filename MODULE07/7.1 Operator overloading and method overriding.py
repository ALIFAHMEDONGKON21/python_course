class parson:
    def __init__(self,name, age, height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print('He eat rice')
        
    def exercise(self):
        raise NotADirectoryError
    
class cricket(parson):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team=team
        super().__init__(name, age, height, weight)
        
    def eat(self):
        print('cricket eat helthy food')
    
    def exercise(self):
        print('nedd it')
    

    def __add__(self,other):
        return self.age + other.age
    
      # + sign operator overload
    def __add__(self, other):
        return self.age + other.age
    
    # * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight
    
    # len overload
    def __len__(self):
        return self.height
    
    # > operator overload
    def __gt__(self, other):
        return self.age > other.age

shakib=cricket('skakib',45,76,80,'bd')
rakib=cricket('rakib', 34,67,80,'bogura')
shakib.eat()
shakib.exercise()

print(shakib + rakib)
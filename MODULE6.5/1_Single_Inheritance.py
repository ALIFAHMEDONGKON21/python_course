class animal:
    def __init__(self,name) -> None:
        self.name=name
    def eat(self):
        print(f'{self.name}' 'I can eat ')

class cat(animal):
    def __init__(self, name) :
        super().__init__(name)

class dog(animal):
    def __init__(self, name):
        super().__init__(name)

c=cat('Cat')
print(c.eat())

d=dog('Dog')
print(d.eat())
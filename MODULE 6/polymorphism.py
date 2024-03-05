# poly --> many (multiple)
# morph --> shape

class animal:
    def __init__(self,name) -> None:
        self.name=name
    
    def make_sound(self):
        print('animal making some sound')
        
class cat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('mow mow')
        
class dog(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('bok bok ')
class goat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def make_sound(self):
         print('beh beh')
    
don=cat('real don')
don.make_sound()

shefer=dog('real dog')
shefer.make_sound()

mess=goat('l m 10')
mess.make_sound()     

animals=[don,shefer,mess]

for animal in animals:
    animal.make_sound()
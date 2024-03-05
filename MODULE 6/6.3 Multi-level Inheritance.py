class vehcile:
    def __init__(self,name,brand,price) -> None:
        self.name=name
        self.price=price
    def __repr__(self) -> str:
        return f'{self.name} {self.price}'
    
    def move(self):
        pass

class bus(vehcile):
    def __init__(self, name, brand, price,seat) -> None:
        self.seat=seat
        super().__init__(name, brand, price)
        
    def __repr__(self) -> str:
        return super().__repr__()
    
class truck(vehcile):
    def __init__(self, name, brand, price,weight) -> None:
        self.weight=weight
        super().__init__(name, brand, price)

class pickuptruck(truck):
    def __init__(self, name, brand, price, weight) -> None:
        super().__init__(name, brand, price, weight)      

class AcBus(bus):
    def __init__(self, name, brand, price, seat,teperature) -> None:
        self.temperature=teperature
        super().__init__(name, brand, price, seat)         
        
    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()

green_line= AcBus('hanif','hino',1000000000000,42,10)
print(green_line)
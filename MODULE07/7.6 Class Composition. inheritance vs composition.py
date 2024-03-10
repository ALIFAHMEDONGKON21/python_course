class cpu:
    def __init__(self,core) -> None:
        self.core=core
class RAM:
    def __init__(self,size) -> None:
        self.size=size

class harddrive:
    def __init__(self,capacity) -> None:
        self.capacity=capacity

class computer:
    def __init__(self,core,ram_size,hd_capacity) -> None:
        self.cpu=cpu(core)
        self.ram=RAM(ram_size)
        self.hard_disa=harddrive(hd_capacity)
        
mac=computer(4,16,256)
rem=mac.ram()
print(rem)
        
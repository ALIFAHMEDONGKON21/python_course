class compony:
    def __init__(self,cnname,location) -> None:
        self.cname=cnname
        self.location=location
    def cpmpony_details(self):
        print("Compony Name :" ,self.cname, "Location :" , self.location)

class parson:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        
    def parson_details(self):
        print("Name",self.name ,"age:",self.age)
        
class emploee(parson,compony):
    def __init__(self,em_name, em_age, com_location, com_name) -> None:
        parson.__init__(self,em_name,em_age)
        compony.__init__(self,com_name,com_location)
    
    def details(self,salary, skill):
        print("salary:",salary,"skill:", skill)
        
ob_employe=emploee('alif',25,'usa','google')
ob_employe.cpmpony_details()
ob_employe.parson_details()
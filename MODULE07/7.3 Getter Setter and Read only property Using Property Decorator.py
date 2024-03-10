class user:
    def __init__(self,name,age,tk) -> None:
        self.name=name
        self.age=age
        self.__tk=tk
    
    @property
    def salary(self):
        return self.__tk
    @salary.setter
    def salary(self,value):
        if value<0:
            print('NOT MOER TK')
        self.__tk+=value
    
samsu=user('samsu',24,600)
print(samsu.salary)
samsu.__tk=4000
print(samsu.salary)
# encapsulation --> hide details
# access modifier: public, protected, private

class bank:
    def __init__(self,holder_name, initial_deposit) -> None:
        self.holder_name=holder_name
        self._branch='borogula bogura'
        self.__balance=initial_deposit
    
    def deposite(self,amount):
        self.__balance+=amount
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance=self.__balance-amount
            return amount
        else:
            return f'not wirthdraw'
 

alif=bank('alif',10000)
alif.get_balance()
print(alif.holder_name)
alif.deposite(5000)
print(alif.get_balance())



print(alif._branch)

print(dir(alif))

print(alif._bank__balance)
        
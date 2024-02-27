class bank:
    def __init__(self,balance) -> None:
        self.balance=balance
        self.min_balance=10
        self.max_balance=10000
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            
            
    def withdraw(self,amount):
        if amount > self.max_balance:
            print('Not Allow is this balance  .you withdraw less than this amount')
            print('your balance now {balance}')
        elif amount<self.min_balance:
            print('This amount not allow withdraw .this minimum amounnt ')
        else:
            self.balance-=amount

brack=bank(15000)
brack.deposit(10)
print(brack.balance)

brack.withdraw(1000)

print(brack.balance)
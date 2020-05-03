class Account():
    def __init__(self , title = None , balance = 0):
        self.balance = balance
        self.title = title
        pass
    
    def deposit(self , amount):
        self.balance += amount
    
    def withdrawal(self , amount):
        self.balance -= amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):

    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        interest_amount = self.balance * self.interestRate / 100
        return interest_amount


obj1 = SavingsAccount("Steve", 5000, 10)
print("Initial Balance:", obj1.getBalance())
obj1.withdrawal(1000)
print("Balance after withdrawal:", obj1.getBalance())
obj1.deposit(500)
print("Balance after deposit:", obj1.getBalance())
print("Interest on current balance:", obj1.interestAmount())
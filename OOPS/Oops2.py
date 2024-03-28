# Create Account class with 2 attributes - balance and account no.
# Create method for debit, credit and print the balance

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc

    def debit(self,amount):
        self.balance -= amount
        print("The Rs: ",amount,"was debitated")
        print("The Account balance is : ",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("The Amount : ",amount,"was credited")
        print("The Total balance is : ",self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000,101)
acc1.debit(1000)
acc1.credit(40000)
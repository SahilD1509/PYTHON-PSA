"""class account:
    def deposit_amount(self,amount):
        self.accbalance = self.accbalance + amount"""

class Account:
    def __init__(self):
        print("Constructor is a special method")

    def open_acc(self):
        print("Account Opened")
    
    def deposit_amount(self):
        print("Amount Deposited")

a1 = Account()
a2 = Account()
class Account:
    def open_account(self):
        print("Account Opened")
    def deposit_amount(self):
        print("Amount Deposited")
    def withdraw(self):
        print("Amount Withdrawn")
    def get_bal(self):
        return 100
    def close_acc(self):
        print("Account closed")


a1 = Account()
a1.open_account()
a1.deposit_amount()
a1.withdraw()
a1.get_bal()
a1.close_acc()

print("****************************")
a2 = Account()
a2.open_account()
a2.deposit_amount()
a2.withdraw()
a2.get_bal()
a2.close_acc()

#Self is a keyword or pointer to refer current object
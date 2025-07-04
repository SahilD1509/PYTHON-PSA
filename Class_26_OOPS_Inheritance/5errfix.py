class InsufficientBalError(Exception):
    def __init__(self, msg):
        super().__init__(msg)  
        self.msg = msg

def withdrawal_amount():
    amount = int(input("Enter amount to withdraw: "))
    acc_bal = 1500
    if acc_bal >= amount:
        print('Enjoy')
    else:
        raise InsufficientBalError('Low Balance')
    print('Please follow rules')

# Calling the function
try:
    withdrawal_amount()
except InsufficientBalError as e:
    print(f"Error: {e.msg}")

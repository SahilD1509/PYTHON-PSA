def InsufficientBalError(Exception):
    def __init__(self,msg):
        super()
        self.msg = msg

def withdrawl_amount():
    amount = int(input("Enter amount to withdraw: "))
    acc_bal = 1500
    if acc_bal > amount:
        print('Enjoy')
    else:
        raise InsufficientBalError('Low Bal')
    print('Please follow rules')

withdrawl_amount()
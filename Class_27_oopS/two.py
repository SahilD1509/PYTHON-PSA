from errors import InsufficientBalError
def withdrawl_amount():
    amount = int(input("Enter Amount: "))
    acc_bal = 5000
    try:
        if acc_bal < amount:
            raise InsufficientBalError("low Bal....")
        else:
            print("Enjoy")

    except InsufficientBalError as err:
        print(err.msg)
    print("Follow Rules") 
withdrawl_amount()
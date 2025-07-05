from errors import InsufficientBalError

def withdrawl_amount():
    amount = int(input("Enter Amount: "))
    acc_bal = 5000
    if acc_bal < amount:
        raise insufficientBalError("No Balance")
    else:
        print("Enjoy")

    print("Follow Rules")

withdrawl_amount()
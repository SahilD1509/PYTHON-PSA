fp = None
a = None
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print("Your number is:", a,":",b)
    print(a/b)

    fp = open("xyz.txt", "r")
except TypeError as error:
    pass
except ZeroDivisionError as error:
    print("Can't divide by zero")
except FileNotFoundError as error:
    pass
except:
    pass



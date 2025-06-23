fp = None
num = None
try:
    num = int(input("Enter a number: "))
    print("Your number is:", num)
    print(num/5)
    print(num/0)

    fp = open("xyz.txt", "r")
except TypeError as error:
    pass
except ZeroDivisionError as error:
    print(num/1)
except FileNotFoundError as error:
    pass
except:
    pass



try:
    n = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    res = b / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")
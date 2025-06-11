"""def factorial(n):
    if n < 0:
        print("Invalid Number")
    elif n == 0 and n == 1:
       return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
            return result
        
number = int(input("Enter number: "))
print(f"Factorial of given number is: {factorial(number)} ")"""

def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Get input from the user
number = int(input("Enter a number to compute its factorial: "))
print(f"The factorial of {number} is: {factorial(number)}")

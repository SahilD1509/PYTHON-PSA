#Program to print Fibonacci number series up to a given number
limit = int(input("Enter the upper limit for the Fibonacci series: "))

a, b = 0, 1

print("Fibonacci series up to", limit, ":")

while a <= limit:
    print(a, end=' ')
    a, b = b, a + b
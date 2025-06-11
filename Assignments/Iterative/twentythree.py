#Write a program to print the sum of first n numbers?
n = int(input("Enter a number (n): "))

sum_n = 0
for i in range(1, n + 1):
    sum_n += i

print(f"The sum of the first {n} natural numbers is: {sum_n}")

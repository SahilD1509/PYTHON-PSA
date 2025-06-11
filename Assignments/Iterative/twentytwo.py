#Write a program to check if a given number is an Armstrong number or not.
num = int(input("Enter a number: "))

# Convert the number to a string to find the number of digits
num_str = str(num)
num_digits = len(num_str)

# Calculate the sum of each digit raised to the power of num_digits
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

# Check if the sum is equal to the original number
if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
#Program to read 5 numbers from CLA and print only even numbers
import sys

# Skip the first argument (script name)
args = sys.argv[1:]

# Ensure exactly 5 numbers are provided
if len(args) != 5:
    print(1,2,5,6,9)
else:
    print("Even numbers are:")
    for num_str in args:
        num = int(num_str)
        if num % 2 == 0:
            print(num)
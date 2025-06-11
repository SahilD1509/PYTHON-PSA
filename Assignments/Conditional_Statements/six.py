num = input("Enter a single digit number (0-9): ")

digits_in_english = [
    "Zero", "One", "Two", "Three", "Four",
    "Five", "Six", "Seven", "Eight", "Nine"
]

if num.isdigit() and 0 <= int(num) <= 9:
    print(digits_in_english[int(num)])
else:
    print("Invalid input. Please enter a single digit number (0-9).")
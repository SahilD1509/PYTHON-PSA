x = float(input("Enter number A:"))
y = float(input("Enter number B:"))
z = float(input("Enter number C:"))
if x >= y and x >= z:
    print(f"{x} is the greatest number")
elif y >= x and y >= z:
    print(f"{y} is the greatest number")
else:
    print(f"{z} is the greatest number")
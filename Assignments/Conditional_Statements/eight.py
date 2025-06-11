x = int(input("Enter number A: "))
y = int(input("Enter number B: "))
z = int(input("Enter number C: "))
if x > y and x > z:
    print("Number A is the largest")
elif y > x and y > z:
    print("Number B is the largest")
else:
    print("Number C is the largest")
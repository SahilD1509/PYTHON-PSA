a = 10
b = 10
print(a is b)  # This will print True because both a and b point to the same integer object in memory.
print(id(a))  # This will print the memory address of the integer object that a points to.
print(id(b))  # This will print the memory address of the integer object that b points to, which should be the same as id(a).
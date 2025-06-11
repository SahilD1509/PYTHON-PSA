"""union = |
intersection = &
difference = -
symmetric difference = ^"""

s1 = {10,20,30,40}
s2 = {30,40,50,60}

print(s1.union(s2)) #for printing all elements
print(s1 | s2)

print(s1.intersection(s2)) #for printing common elements
print(s1 & s2)

print(s1.difference(s2)) # for printing different values from first set
print(s1 - s2)

print(s1.symmetric_difference(s2)) #Only Different elements from both sets no common elements going to represent
print(s1 ^ s2) 
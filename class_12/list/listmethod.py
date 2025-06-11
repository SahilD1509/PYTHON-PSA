enames = ["RG","SG","PG","RG"]
print(enames)
print(enames[1])
# print(enames[8]) gives index error because 8 index not defined

print(enames.index("RG"))
print(enames.count("RG"))

# Adding name in list at last position
enames.append("NM")
print(enames)

# Adding name in list at 3rd position
enames.insert(3,"VK")
print(enames)

# To display names in list in reverse order
enames.reverse()
print(enames)

# To print names in sorted format like alphabetically
enames.sort()
print(enames)
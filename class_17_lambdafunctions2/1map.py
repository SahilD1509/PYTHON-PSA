enames = ["rahul","sonia","priya"]
def changecase(name):
    return name.upper()
new_names = list(map(changecase,enames))
print(new_names)

print(enames)
print(list(map(lambda ename: ename.upper(),enames)))

new_names = []
for ename in enames:
      new_names.append(ename.upper())
print(new_names)
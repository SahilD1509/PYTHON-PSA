enames = ["rahul","sonia","priya"]
#method 1
def changecase(name):
    return name.upper()
new_names = list(map(changecase,enames))
print(new_names)

#method 2 using lambda map function
print(enames)
print(list(map(lambda ename: ename.upper(),enames)))

#method 3 using for loop
new_names = []
for ename in enames:
      new_names.append(ename.upper())
print(new_names)
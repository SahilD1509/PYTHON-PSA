a= 10
def add():
    print("Addition")

print(id(add))
print(type(a))     #<class 'int'>
print(type(add))   #<class 'function'>
print(type(add())) #<class 'nonetype'> invoking function
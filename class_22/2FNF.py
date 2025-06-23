fp = None
try:
    fp = open("xyz.txt","r")
except FileNotFoundError as error:
    fp = open("def.txt","r")
data = fp.read()
fp.close()
print(data)
print("Good Morning")
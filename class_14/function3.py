#POSITIONAL ARGUMENT
def cal(a,b):
    print(b-a)
cal(100,200)
cal(200,100)

#KEYWORD ARGUMENT
def calc(a,b):
    print(b-a)
calc(a=100,b=200)
calc(b=200,a=100)

#DEFAULT ARGUMENT
def calc(a,b,c=1):
    print(a+b+c)
calc(1,2,3)
calc(10,20,30)
calc(100,200)

#variable length Arguments
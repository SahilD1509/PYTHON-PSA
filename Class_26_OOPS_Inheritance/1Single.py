#Single Inheritance
class Parent:
    def m1(self):
        print("Parent class - M1,Method")
    def m2(self):
        print("Parent class - M2,Method")

class child(Parent):
    def m3(self):
        print("Child class - M3, Method")

c1 = child()
print(c1.__dict__)
c1.m1()
c1.m3()
c1.m2()
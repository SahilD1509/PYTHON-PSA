#Multilevel Inheritrnce
class GP:
    def m1(self):
        print("GP Class, M1")
    def m2(self):
        print("GP Class, M2")

class parent(GP):
    def m3(self):
        print("Parent Class, Method M3")

class child(parent):
    def m4(self):
        print("Child Class, Method M4")

c1 = child()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
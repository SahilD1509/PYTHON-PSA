class Parent1:
    def m1(self):
        print("Parent 1 - class M1 Method")
    def m2(self):
        print("Parent 2 - class M2 Method")

class Parent2:
    def m1(self):
        print("Parent 2 - class M1 Method")
    def m2(self):
        print("Parent 2 - class M2 Method")

class Child(Parent1,Parent2):
    def m3(self):
        print("Child - class M3 Method")
        
c1 = Child()
c1.m1()
c1.m2()
c1.m3()
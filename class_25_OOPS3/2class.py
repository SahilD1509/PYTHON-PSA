class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30
    
    @classmethod
    def m2(cls):
        cls.e = 50
        Test.h = 70
        Test.z = 80

t1 = Test()
t1.m1()
t1.m2()

t2 = Test()
t2.d = 40
Test.f = 60
t1.m2()

print(t1.__dict__)
print(t2.__dict__)
print(Test.__dict__)
class Test:
    def __init__(self):
        print("Constructor Called")

    def m1(self):
        pass
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass

Test()
class employee:
    company_name = 'TCS'

    def __init__(self, id, name, salary):
        self.eid = id
        self.ename = name
        self.esalary = salary


e1 = employee(101,'Rahul',45000)
e2 = employee(102,'Sonia',55000)
e3 = employee(103,'Priyanka',65000)

print(employee.__dict__)
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)
employees=[
    {'eid':101,'ename':'Rahul','gender':'Male'},
    {'eid':102,'ename':'Sonia','gender':'Female'},
    {'eid':103,'ename':'Priya','gender':'Female'},
    {'eid':104,'ename':'Modi','gender':'Male'},
    {'eid':105,'ename':'Amith','gender':'Male'}
]

"""for emp in employees:
    print(emp['eid'])"""

i = 0
while i <= 4:
    print(employees[i]['ename'])
    i = i + 1

for i in range(10):
    print("Good Morning")
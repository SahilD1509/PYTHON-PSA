employees = [
    {'eid': 101, 'ename': 'Rahul', 'esal': 45000},
    {'eid': 102, 'ename': 'Sonia', 'esal': 55000},
    {'eid': 103, 'ename': 'Priyanka', 'esal': 65000}
]

for emp in employees:
    print(emp['ename'],emp['esal'])

for emp in employees:
    print(emp['esal'])
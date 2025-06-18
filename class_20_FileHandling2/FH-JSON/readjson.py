"""import json
with open('emp.json', 'r') as file:
    data = json.load(file)
print(data)"""
import json
fp = open('emp.json', 'r')
employees=json.load(fp)
print(type(employees))
print(employees)
#for reading names of json file with for loop
for emp in employees:
    print(emp['ename'])

fp.close()
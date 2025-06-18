import json
emp = {
    'eid':101,
    'ename':'Rahul',
    'avail':True,
    'loc':None
}
print(type(emp))
print(emp)
emp_json = json.dumps(emp)
print(emp_json)
print(type(emp_json))

#dumps - converts python data to json data
#loads - converts json data to python data
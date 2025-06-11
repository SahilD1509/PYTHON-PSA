employees = [{"eid":1,"name":"Ray","gender":"Male"},
{"eid":2,"name":"Lorna","gender":"Female"},
{"eid":3,"name":"Tricia","gender":"Female"},
{"eid":4,"name":"Sallie","gender":"Female"},
{"eid":5,"name":"Allie","gender":"Male"},
{"eid":6,"name":"Aurthur","gender":"Male"},
{"eid":7,"name":"Koren","gender":"Female"},
{"eid":8,"name":"Udell","gender":"Male"},
{"eid":9,"name":"Yetta","gender":"Female"},
{"eid":10,"name":"Silva","gender":"Female"},
{"eid":11,"name":"Antonietta","gender":"Female"},
{"eid":12,"name":"Gabriel","gender":"Male"},
{"eid":13,"name":"Ilario","gender":"Male"},
{"eid":14,"name":"Gare","gender":"Male"},
{"eid":15,"name":"Alyson","gender":"Female"},
{"eid":16,"name":"Crin","gender":"Female"},
{"eid":17,"name":"Lev","gender":"Male"},
{"eid":18,"name":"Humberto","gender":"Male"},
{"eid":19,"name":"Nolan","gender":"Male"},
{"eid":20,"name":"Hilary","gender":"Male"},
{"eid":21,"name":"Jessie","gender":"Female"},
{"eid":22,"name":"Alexei","gender":"Male"},
{"eid":23,"name":"Leshia","gender":"Female"},
{"eid":24,"name":"Bennie","gender":"Male"},
{"eid":25,"name":"Arnold","gender":"Male"},
{"eid":26,"name":"Jeromy","gender":"Polygender"},
{"eid":27,"name":"Conrade","gender":"Male"},
{"eid":28,"name":"Taylor","gender":"Male"},
{"eid":29,"name":"Otto","gender":"Male"},
{"eid":30,"name":"Phillipp","gender":"Male"},
{"eid":31,"name":"Karlen","gender":"Female"},
{"eid":32,"name":"Brunhilda","gender":"Female"},
{"eid":33,"name":"Ferdinand","gender":"Male"},
{"eid":34,"name":"Bendicty","gender":"Male"},
{"eid":35,"name":"Ferdie","gender":"Male"},
{"eid":36,"name":"Antonin","gender":"Male"},
{"eid":37,"name":"Clerissa","gender":"Female"},
{"eid":38,"name":"Mason","gender":"Male"},
{"eid":39,"name":"Flss","gender":"Polygender"},
{"eid":40,"name":"Thornie","gender":"Male"},
{"eid":41,"name":"Roslyn","gender":"Female"},
{"eid":42,"name":"Adrianna","gender":"Female"},
{"eid":43,"name":"Arron","gender":"Male"},
{"eid":44,"name":"Vittoria","gender":"Female"},
{"eid":45,"name":"Ashlan","gender":"Female"},
{"eid":46,"name":"Michaeline","gender":"Female"},
{"eid":47,"name":"Manny","gender":"Male"},
{"eid":48,"name":"Garth","gender":"Male"},
{"eid":49,"name":"Elwood","gender":"Male"},
{"eid":50,"name":"Murdoch","gender":"Male"},
{"eid":51,"name":"Joanne","gender":"Female"},
{"eid":52,"name":"Archer","gender":"Bigender"},
{"eid":53,"name":"Orv","gender":"Male"},
{"eid":54,"name":"Garv","gender":"Male"},
{"eid":55,"name":"Kaine","gender":"Genderqueer"},
{"eid":56,"name":"Farr","gender":"Male"},
{"eid":57,"name":"Virge","gender":"Polygender"},
{"eid":58,"name":"Jo","gender":"Male"},
{"eid":59,"name":"Stoddard","gender":"Non-binary"},
{"eid":60,"name":"Hamlin","gender":"Male"},
{"eid":61,"name":"Tito","gender":"Male"},
{"eid":62,"name":"Geralda","gender":"Female"},
{"eid":63,"name":"Zsazsa","gender":"Female"},
{"eid":64,"name":"Harald","gender":"Male"},
{"eid":65,"name":"Lolly","gender":"Female"},
{"eid":66,"name":"Deloria","gender":"Female"},
{"eid":67,"name":"Louie","gender":"Polygender"},
{"eid":68,"name":"Laird","gender":"Male"},
{"eid":69,"name":"Ulises","gender":"Genderfluid"},
{"eid":70,"name":"Leontyne","gender":"Female"},
{"eid":71,"name":"Pattin","gender":"Male"},
{"eid":72,"name":"Ivar","gender":"Male"},
{"eid":73,"name":"Karlan","gender":"Male"},
{"eid":74,"name":"Gilbertina","gender":"Female"},
{"eid":75,"name":"Blanca","gender":"Female"},
{"eid":76,"name":"Emilio","gender":"Male"},
{"eid":77,"name":"Stillmann","gender":"Male"},
{"eid":78,"name":"Sapphire","gender":"Female"},
{"eid":79,"name":"Cicily","gender":"Female"},
{"eid":80,"name":"Adel","gender":"Female"},
{"eid":81,"name":"Yolanda","gender":"Female"},
{"eid":82,"name":"Lora","gender":"Female"},
{"eid":83,"name":"Nora","gender":"Female"},
{"eid":84,"name":"Hedvig","gender":"Bigender"},
{"eid":85,"name":"Galvin","gender":"Male"},
{"eid":86,"name":"Florie","gender":"Female"},
{"eid":87,"name":"Silvain","gender":"Male"},
{"eid":88,"name":"Tova","gender":"Female"},
{"eid":89,"name":"Evaleen","gender":"Female"},
{"eid":90,"name":"Delores","gender":"Genderfluid"},
{"eid":91,"name":"Kizzee","gender":"Female"},
{"eid":92,"name":"Bondy","gender":"Male"},
{"eid":93,"name":"Collette","gender":"Female"},
{"eid":94,"name":"Wylma","gender":"Female"},
{"eid":95,"name":"Rennie","gender":"Female"},
{"eid":96,"name":"Wolfgang","gender":"Male"},
{"eid":97,"name":"Ellyn","gender":"Female"},
{"eid":98,"name":"Stephine","gender":"Female"},
{"eid":99,"name":"Lenci","gender":"Male"},
{"eid":100,"name":"Corina","gender":"Female"}]

#Print all employee names using for loop
"""print("Using for loop:")
for employee in employees:
    print(employee['name'])"""

#Print all employee names using while loop
"""print("Using while loop:")
i = 0
while i <= len(employees)-1:
    print(employees[i]['name'])
    i = i + 1
"""

#Print only male employees using for loop
"""print("Using for loop:")
for employee in employees:
    if employee['gender'] == 'Male':
        print(employee['name'])"""

#Print only Female employees using while loop
"""print("Using while loop:")
i = 0
while i <= len(employees)-1:
    if employees[i]['gender'] == 'Female':
        print(employees[i]['name'])
    i = i + 1"""

#print number of male employees using for loop
"""print("Using for loop:")    
count = 0
for employee in employees:
    if employee['gender'] == 'Male':
      count = count + 1
print(len(employees))
print("Total number of male employees:", count)"""

#Print number of female emoyees using while loop
print("Using while loop:")  
count = 0
i = 0
while i <= len(employees)-1:
    if employees[i]['gender'] == 'Female':
        count = count + 1
    i = i + 1
print("Total number of female employees:", count)


#function: Group of statements for specific purpose
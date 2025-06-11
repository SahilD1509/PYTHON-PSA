enames = ["RG","SG","PG","NM","AS"]
#indexing   0    1   2     3    4
print(enames[0]) #RG
print(enames[1]) #SG
print(enames[2]) #PG
print(enames[3]) #NM
print(enames[4]) #AS
#print(enames[15]) #IndexError: list index out of range

#update
enames[0] = "Rahul Gandhi"
print(enames)

del enames[4]
print(enames)
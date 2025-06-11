eids = {101,102,103,101,102,101}
unames = {"AM","DK","NM"}
print(eids)

#to add element in set where order gurantee is not applicable
eids.add(104)
print(eids)

#only for loop can be used not while loop because indexing is not possible in set
for eid in eids:
    print(eid)

#to add multiple elements in set we use extend method 
eids.update({"RG","SG"})
print(eids)
eids.update(unames)
print(eids)

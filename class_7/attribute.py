l1 = [10,20,30,40,50]
l1.append(60)  # This will add 60 to the end of the list l1.
print(l1)  # This will print the updated list, which is now [10, 20, 30, 40, 50, 60].

l1.xyz(60)  # This will raise an AttributeError because the list object does not have a method named xyz.
print(l1)  # This line will not be executed because the previous line raises an error.
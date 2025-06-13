numbers = [37,18,31,14,8,12,7]
#collect all even/odd numbers into new list
#using loop
#Even Number
even_no = []
for num in numbers:
    if num % 2 == 0:
        even_no.append(num)
print(numbers)
print(even_no)
#Odd Number
odd_no = []
for num in numbers:
    if num % 2 != 0:
        odd_no.append(num)
print(numbers)
print(odd_no)

even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]
print("Even numbers: " , even)
print("ODD numbers: " , odd)

#using lambda function
even_num = list(filter(lambda num:num%2 == 0,numbers))
print(even_num)
odd_num = list(filter(lambda num:num%2 != 0,numbers))
print(odd_num)
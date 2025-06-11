"""list1 = [1, 2, 3,50,60]
bytes_obj = bytes(a)
print(bytes_obj)  # Output: b'\x01\x02\x03\x32\x3c'

bytes_obj[3] = 100  # This will raise an error because bytes objects are immutable
"""

list1 = [80,40,81,14,255,0]

ba =  bytearray(list1)
print(type(ba))

print(ba)  # Output: bytearray(b'P@Q\x0e\xff\x00')

print(81 in ba)  # Output: True

for value in ba:
    print(value)  # Output: 80, 40, 81, 14, 255, 0

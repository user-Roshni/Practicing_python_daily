#Input a tuple of numbers and print max & min.
a = input("Enter values with space: ")
a_tuple = tuple(a.split())
print(a_tuple)
''' Or you can use this
a_tuple = a.split()
print(a_tuple)
print(tuple(a_tuple))
'''
print(min(a_tuple))
print(max(a_tuple))

#Convert List of Tuples to Dictionary
b = int(input("How many tuples do you want to enter: "))
tuple_list = []
for i in range(b):
    b1 = input("Enter first element of a tuple: ")
    b2 = input("Enter second element of a tuple: ")
    tuple_list.append((b1, b2))
print(tuple_list)
print(dict(tuple_list))

#Pack multiple values into a tuple, then unpack them into variables.
c = input("Enter values with space: ")
c_tuple = tuple(c.split())
print(c_tuple)
print(type(c_tuple))

#unpacking
for element in c_tuple:
    print(element, end = " ")
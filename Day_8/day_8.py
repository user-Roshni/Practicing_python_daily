#Square Numbers Using map()
a = input("Enter values with space in-between: ")
a_list = a.split()
print(a_list)

square = map(lambda sq: int(sq)**2, a_list)
print("Square value of a: ", list(square))

#Filter Even Numbers Using filter()
b = input("Enter elements with space in-between: ")
b_list = b.split()
print(b_list)

even = filter(lambda o: int(o) % 2 == 0, b_list)
odd = filter(lambda o: int(o) % 2 != 0, b_list)

print("Even numbers: ", list(even))
print("Odd numbers: ", list(odd))

#Sum of List Using reduce()
from functools import reduce
c = input("Enter elements with space in-between: ")
c_list = c.split()
print("Given list: ", c_list)

add = reduce(lambda x, y: int(x) + int(y), c_list)
print("Sum of list: ", add)

#Sort List of Tuples by Second Element
d = int(input("How many tuple you want to enter: "))
d_list = []

for i in range(d):
    d1 = input("Enter values for tuple with space in-between: ")
    d1_tuple = tuple(d1.split())
    d_list.append(d1_tuple)
print("Given list of tuple: ", d_list)

d_sort = sorted(d_list, key= lambda s: s[1])
print(d_sort)

#Find Longest Word in a Sentence Using max() + key
e = input("Enter a sentence: ")
e_split = e.split()

sorted_e = max(e_split, key= lambda e1: len(e1))
print(sorted_e)
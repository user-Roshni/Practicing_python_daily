#Input two sets and print intersection.
a = input("Enter elements for set1 with space: ")
a1 = input("Enter elements for set2 with space: ")
a_set = set(a.split())
a1_set = set(a1.split())
print(a_set)
print(a1_set)
print(a_set.intersection(a1_set))

#Input two sets and check if one is a subset of the other.
b = input("Enter elements for set1 with space: ")
b1 = input("Enter elements for set2 with space: ")
b_set = set(b.split())
print(b_set)

b1_set = set(b1.split())
print(b1_set)
print(b_set.issubset(b1_set))

#Input a list with duplicates, convert to set, then back to list.
c = input("Enter elements for list with space inbetween: ")
c_list = c.split()
print(c_list)
print(type(c_list))

print(set(c_list))
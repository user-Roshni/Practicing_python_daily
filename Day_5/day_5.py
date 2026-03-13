#Input a list of numbers and print the second largest.
a = input("Enter numbers with space: ")
a_list = a.split()
print(a_list)
a_list.sort(reverse = True)
print(a_list)
print("Second largest number in the list is: ", a_list[1])

#Input a list and remove duplicates.
b = input("Enter elements for a list with space: ")
b_list = b.split()
print(b_list)
print(set(b_list))

#Input a list and count how many times each element appears.
c = input("Enter elements for a list with space: ")
c_list = c.split()
print(c_list)
count = {}

for i in c_list:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

#Reverse a List with & Without Using reverse()
d = input("Enter a number with spaces: ")
d_list = d.split() 
print("Your list: ", d_list)

# Reversing list without reverse()
print(d_list[: : -1])

# Reversing list using reverse() function
d_list.reverse()
print(d_list)

#Merge Two Lists Element-Wise
e = input("Enter elements for list1 with space inbetween: ")
e_list = e.split()
print(e_list)

e1 = input("Enter elements for list2 with space inbetween: ")
e1_list = e1.split()
print(e1_list)

merge = [(x, y) for x, y in zip(e_list, e1_list)]
print("Merged list: ", merge)

#Find Common Elements Between Two Lists
f = input("Enter elements for a list1 with spaces: ")
f1 = input("Enter elements for a list2 with spaces: ")
f_list = f.split()
print("list1: ", f_list)

f1_list = f1.split()
print("list2: ", f1_list)

common = []
for element in f_list:
    if element in f1_list:
        common.append(element)
print("Common elements: ", common)

f_list.extend(f1_list)
print("merged_list: ", f_list)

print("removing common elements in list:", set(f_list))

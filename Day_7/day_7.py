#Input a string and count frequency of each character using a dictionary.
a = input("Enter a string: ")
count = {}
for p in a:
    if p in count:
        count[p] += 1
    else:
        count[p] = 1
print("Word count: ", count)

#Input a dictionary and swap keys with values.
b = {}
b_entry = int(input("Enter the number of pairs you want to add:"))
for m in range(b_entry):
    key = input("enter key: ")
    value = input("enter value: ")
    b[key] = value
print("Dictionary: ", b) 

b_swap = {}
for key, value in b.items():
    if value not in b_swap:
        b_swap[value] = [key]
    else:
        b_swap[value].append(key)

print("Swapped Dictionary:", b_swap)

#Input two dictionaries and merge them.
c = {}
c_entry = int(input("Enter the number of pairs you want to add:"))
for i in range(c_entry):
    key = input("enter key: ")
    value = input("enter value: ")
    c[key] = value
print("dictionary1: ", c)
print(type(c))

c1 = {}
c1_entry = int(input("Enter the number of pairs you want to add:"))
for l in range(c1_entry):
    key = input("enter key: ")
    value = input("enter value: ")
    c1[key] = value
print("dictionary2: ", c1)
(c.update(c1))
print(c)

#Input a dictionary of student marks and print the student with the highest marks.
d1 = {}
d1_entry = int(input("Enter the number of key-value pairs you want to add: "))

for n in range(d1_entry):
    key = input("Enter student name: ")
    value = int(input("Enter marks: "))   
    d1[key] = value

print("Dictionary: ", d1)

highest_student = max(d1, key=d1.get)
print("Student with highest marks:", highest_student)
print("Marks:", d1[highest_student])

#Input a sentence and count how many times each word appears.
e = input("Enter a sentence: ")
e1 = e.split()
count1 = {}

for q in e1:
    if q in count1:
        count1[q] += 1
    else:
        count1[q] = 1
print("Word count: ", count1)

#Input a nested dictionary of students and print details of a given student ID.
'''f = {}
outer_dict = int(input("Enter the number of outer keys: "))

for s in range(outer_dict):
    outer_key = input("Enter student ID as a outer key: ")
    f[outer_key] = {}

    inner_dict = int(input("Enter number of pairs for inner dictionary: "))

    for t in range(inner_dict):
        inner_key = input("Enter key for inner dictionary: ")
        inner_value = input("Enter value for inner dictionary: ")
        f[outer_key][inner_key] = inner_value

print("Nested dictionary: ", f)
print(f[2])
'''
f = {}
outer_dict = int(input("Enter the number of students: "))

for s in range(outer_dict):
    student_id = input("Enter student ID: ")
    f[student_id] = {}   
    
    inner_dict = int(input(f"Enter number of details for student {student_id}: "))
    
    for t in range(inner_dict):
        key = input("Enter key for inner dictionary: ")
        value = input("Enter value for inner dictionary: ")
        f[student_id][key] = value

print("\nNested dictionary of students:")
print(f)

search_id = input("Enter a student ID to view details: ")

if search_id in f:
    print(f"Details of student {search_id}:")
    for k, v in f[search_id].items():
        print(k, ":", v)
else:
    print("Student ID not found.")


'''d_list = []
d_count = int(input("Enter the number of dictionaries you want to add: "))
for j in range(d_count):
    print("dictionary", j + 1)
    d = {}
    d_entry = int(input("Enter the number of pair you want to add: "))
    
    for k in range(d_entry):
        d_key = input("Enter key: ")
        d_value = input("Enter value: ")
        d[d_key] = d_value
    d_list.append(d)
    print("Dictionary",k ,":", d)
print("All dictionaaries: ", d_list)
'''
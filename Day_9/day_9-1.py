#Write a program that appends new content to an existing file without overwriting it.
with open('D:/python daily practice/Day_9/text.txt', 'a+') as file5:
    file5.write("\nHe was famously known as Captain cool.")
    file5.seek(0)
    print(file5.read())
 
#Read a file and write its content into another file, skipping blank lines.
with open('D:/python daily practice/Day_9/text.txt', 'r') as file6:
    lines_file6 = file6.readlines()

with open('D:/python daily practice/Day_9/text2.txt', 'w+') as file6_1:
    for i in lines_file6:
        if i.strip():
            file6_1.write(i)
            file6_1.seek(0)
            print(file6_1.read())

#Read a file and count how many times each word appears.
with open('D:/python daily practice/Day_9/text2.txt', 'r') as file7:
    text = file7.read()
    words = text.split()
    word_count = {}

for k in words:
    if k in word_count:
        word_count[k] +=1
    else:
        word_count[k] = 1

for k, count in word_count.items():
    print(k, ":", count)

#Write student names and marks into a file.
students = int(input("Enter the number of students: "))
with open('D:/python daily practice/Day_9/student.txt', 'w+') as file8:
    for j in range(students):
        name = input(f"Enter the name of a student {j+1}: ")
        marks = input(f"Enter the mark of a student: ")
        file8.write(name + " "+ marks + "\n")
    file8.seek(0)
    print(file8.read())
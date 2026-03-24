#Write a program to take user input (like a sentence) and save it into a file. Then read the file and print its contents.
'''sentence = input("Enter a sentence: ")
with open('D:/python daily practice/Day_9/text.txt', 'w+') as file1:
    file1.write(sentence)
    file1.seek(0)
    print(file1.read())

#Read a text file and count:Number of lines, Number of words, Number of characters
with open('D:/python daily practice/Day_9/text.txt', 'r') as file2:
    line_count = 0
    word_count = 0
    character_count = 0
    for line in file2:
        line_count += 1

        character_count += len(line)

        word = line.split()
        word_count += len(word)
    print("Lines in a file: ", line_count)
    print("Words in a file: ", word_count)
    print("Characters in a file: ", character_count)

#Read content from one file and write it into another file.
with open('D:/python daily practice/Day_9/text.txt', 'r+') as file3:
    content = file3.read()
    print(content)

with open('D:/python daily practice/Day_9/text1.txt', 'r+') as file3_1:
    file3_1.write(content)
'''
#Input a word and check if it exists in the file. Print the line number(s) where it appears.
word = input("Enter a word you want to search: ")
with open('D:/python daily practice/Day_9/text.txt', 'r') as file4:
    lines = file4.readlines()

for index, line in enumerate(lines, start= 1):
    if word in line:
        print(f"Word found in line{index}: {line}")
    else:
        print("The word is not found in this file")

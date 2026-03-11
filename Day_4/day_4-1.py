#Input a string and count how many vowels (a, e, i, o, u) it has.
# Method 1
a = input("Enter a string: ")
vowel = 0
for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel += 1
    
print(vowel)

#Method 2
a1 = input("Enter a string: ")
vowels1 = "aeiouAEIOU"
count1 = 0

for j in vowels1:
    count1 += a1.count(j)
print("Number of vowels in a given string is", count1)

#Input a string and check if it reads the same forwards and backwards.
b = input("Enter a string: ")
rev_b = b[: : -1]
if b == rev_b:
    print("Original string: ", b)
    print("Reversed string: ", rev_b,"\n", "Both are same")
else:
    print("Original string and reversed string are not same")

#Input a sentence and count how many times each word appears.
sentence = input("Enter a sentence: ")
word = sentence.split()
word_count = {}

for r in word:
    if r in word_count:
        word_count[r] += 1
    else:
        word_count[r] = 1
print("word count is", )

for r, count in word_count.items():
    print(r, ":", count)

#Input a string and remove all spaces.
sentence1 = input("Enter a sentence to remove spaces: ")
print(sentence1.replace(" ", ""))

#Input a sentence and print the longest word.
sentence2 = input("Enter a sentence: ")
words = sentence2.split()

longest_word = ""
max_len = 0

for k in words:
    if len(k) > max_len:
        max_len = len(k)
        longest_word = k

print("The longest word is", longest_word)
print("length is", max_len)
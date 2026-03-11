# Input a range (e.g., 10–50). Use a loop with break to stop once the first prime is found.
import math
def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(math.sqrt(n))+1):
        if n % j == 0:
            return False
    return n
    
n1 = int(input("Enter the value for n1: "))
n2 = int(input("Enter the value for n2: "))

for i in range(n1, n2 + 2):
    if is_prime(i):
        prime_num = i
        break
if prime_num:
    print("First prime in range: ",prime_num)
else:
    print("No prime found in the given range")

# Print numbers from 1–20, but skip multiples of 3 using continue.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# Write a loop that iterates through a list of names. If the name is "Admin", just pass (do nothing), else print the name.
lst = ["Jayaveeraraman", "Anbukarasi", "Roshni", "Baskar", "Admin", "Dhoni", "Yuvaraj", "Bravo", "Jadeja"]
for i in lst:
    if i == "Admin":
        pass
    else:
        print(i)
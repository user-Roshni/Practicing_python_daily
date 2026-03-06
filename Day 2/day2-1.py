#Input a number and reverse it using a while loop.Example: 123 → 321.
number = int(input("Enter a number:"))
reversed_num = 0
while number != 0:
    digit = number % 10
    reversed_num = (reversed_num*10) + digit
    number = number // 10
print(reversed_num)

#Input a number and check if it’s prime using a for loop.
import math
num = int(input("Enter a number:"))
if num <= 1:
    print("Not a prime")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % 2 == 0:
            print("It's not a prime")
        else:
            print("It's a prime number")

#Print the first n terms of the Fibonacci series using a loop.
n = int(input("Enter a number:"))
a, b = 0,1
if n == 1:
    print(a)
elif n >= 2:
    print(a)
    print(b)
    for i in range(2, n):
        c = a+b
        print(c)
        a = b
        b = c
else:
    print("Invalid")
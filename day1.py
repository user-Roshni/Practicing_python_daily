#Input two numbers and print results of addition, subtraction, multiplication, division, modulus, floor division, and exponentiation.
a = int(input("Enter the value for a:"))
b = int(input("Enter the value for b:"))
print("Addition of a and b:" + str(a+b))
print("Subtraction:", a-b)
Multiplication = a * b
print("Multiplication:" + str(Multiplication))
print("Division:", a/b)
print("Modulus:", a%b)
print("Floor division:" + str(a//b))


#Input a number and check if it’s even or odd using %
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The given number", num, "is even")
else:
    print("The given number " + str(num) + " is odd") # concatenation

#Input three numbers and print the largest
a1 = int(input("Enter the first number:"))
b1 = int(input("Enter the second number:"))
c1 = int(input("Enter the third number:"))
if a1 == b1 == c1:
    print("Three numbers are same")
elif a1 == b1:
    print("value of a1 and b1 are same")
    if a1 > c1:
        print("a1 is greater")
    else:
        print("c1 is greater")
elif a1 == c1:
    if c1 > b1:
        print("c1 is greater")
    else:
        print("b1 is greater")
elif b1 == c1:
    if b1 > a1:
        print("b1 is greater")
    else:
        print("a1 is greater")
elif a1 >= b1 and a1 >= c1:
    print("a1 is the greatest and the value of a1 is", a1)
elif b1 >= a1 and b1 >= c1:
    print("b1 is the greatest and the value of b1 is " + str(b1))
else:
    print("c1 is the greatest and the value of c1 is", c1)

#Input a year and check if it’s a leap year.
year = int(input("Enter a year: "))
if year %4 == 0 and year % 100 != 0:
    print("It is a leap year")
elif year % 400 == 0 and year % 100 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")

'''Input marks for 3 subjects, calculate average, and assign grade:

≥90 → A

≥75 → B

≥50 → C

Else → Fail '''

m1 = int(input("Enter a mark for subject1: "))
m2 = int(input("Enter a mark for subject2: "))
m3 = int(input("Enter a mark for subject3: "))
avg = (m1 + m2 + m3)/3
print("The average marks are:", avg)
if avg >= 90:
    print("You passes in A grade")
elif avg >= 75:
    print("You passed in B grade")
elif avg >= 50:
    print("You passed in C grade")
else:
    print("You failed")

#Input a number and calculate the sum of its digits
number = (input("Enter a number:"))
Sum_of_digit = 0
for i in number:
    Sum_of_digit = Sum_of_digit + int(i)
print(Sum_of_digit)
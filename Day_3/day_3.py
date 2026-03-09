#Write a function square(num) that returns the square of a number.
def square(num):
    num = num ** 2
    return num

a = int(input("Enter a value: "))
square_val = square(a)
print(square_val)

#Write a function is_even() that returns True if the number is even, else False
def is_even():
    if b % 2 == 0:
        return "True"
    else:
        return "False"
    
b = int(input("Enter a value: "))
number = is_even()
print(number)    

#Write a function factorial(n) that returns the factorial of a number using a loop.
def factorial(n):
    fact = 1
    i = c
    if n >= 1:
        while i > 0:
            fact *= i
            i -= 1
        return fact
    else:
        return "Invalid"

c = int(input("Enter the value of c:"))
fact_num = factorial(c)
print(fact_num)
        
#Write a function greatest(a, b, c) that returns the largest of three numbers
def greatest(a, b, c):
    if a != b != c:
        if a > b and a > c:
            return a, "is greatest"
        elif b > a and b > c:
            return b, "is greatest"
        else:
            return c, "is greatest"
    elif a == b and b > c:
        return "a and b are equal but b is greater than that"
    elif a == b and c > b:
        return "a and b are equal but c is greater than that"
    elif a == c and b > c:
        return "a and c are equal but b is greater than that"
    elif a == c and c > b:
        return "a and c are equal but c is greater than that"
    elif b == c and a > c:
        return "b and c are equal but a is greater than that"
    elif b == c and c > a:
        return "b and c are equal but c is greater than that"
    else:
        return "All are same"
    
n1 = int(input("Enter the valuue for n1: "))
n2 = int(input("Enter the valuue for n2: "))
n3 = int(input("Enter the valuue for n3: "))
great_num = greatest(n1, n2, n3)
print(great_num)    

#Write a function is_palindrome(s) that returns True if the string is a palindrome, else False.
def is_palindrome(s):
    str_palindrome = s[::-1]
    if str_palindrome == s:
        return "True"
    else:
        return "False"
    
string = input("Enter a word: ")
palindrome = is_palindrome(string)
print(palindrome)
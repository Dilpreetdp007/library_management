# TASK 1
'''Practice questions

Q1.
s = "Python"
Print:
P
n
t using negative indexing


Q2.
numbers = [10, 20, 30, 40, 50]
Print:
First element
Last element
Second last element


Q3.
word = "Programming"
Print:
g
r using negative indexing
o


Q4.
s = "PythonProgramming"
Print:
Python
Programming




Q5.
numbers = [10,20,30,40,50,60,70]
Print:
[20,30,40]
[50,60,70]


Q6.
text = "ABCDEFGHIJ"
Print:
ACEGI using step size
BDFH
(Using both positive and negative indexing)


Q7.
student = {"name":"Rahul","age":20,"marks":75}
Change marks from 75 to 85.'''
# TASK 2
'''Question 1
text = "PYTHONPROGRAM"
Write a Python program to print every 2nd character from the string using slicing.

Question 2
text = "ABCDEFGHIJK"
Using slicing, print the characters C to H.

Question 3
text = "PROGRAMMING"
Write a program to reverse the string using slicing.

Question 4
numbers = [10, 20, 30, 40, 50, 60, 70]
Using slicing, print:
The first 4 elements


The last 3 elements



Question 5
text = "PYTHONDEVELOPER"
Using slicing with negative step size, print the string in reverse order skipping one character each time.'''
# TASK 3
'''PART 1:
BASIC LEVEL :
Take a number and print “Positive” if it is greater than 0.
Take a number and print “Even” if it is divisible by 2.
Take age and print “Eligible for voting” if age ≥ 18.
Take a number and print it only if it is greater than 100.
Take a character and print “Vowel” if it is a vowel.
Take a number and print “Multiple of 5” if divisible by 5.
Take a number and print “Negative” if it is less than 0.
Take marks and print “Pass” if marks ≥ 40.
Take a number and print its square if it is less than 10.
Take the temperature and print “Hot” if the temperature > 30.

MID LEVEL :
Take a number and print “Two-digit number” .
Take a number and print “Ends with 5” if the last digit is 5.
Take a number and print “Perfect square” if its square root is an integer.
Take a number and print “Palindrome candidate” if the first and last half are the same.
Take a number and print “Special number” if it is divisible by both 3 and 7.
Take a string and print “Starts with capital letter” if the first character is uppercase.
Take a number and print “Contains 0” if any digit is zero.'''
#TASK 4 
'''BASIC LEVEL :
Check if a number is Even or Odd.
Check if a number is Positive or Negative or Equal to Zero.
Check if a person is Minor or Adult (age 18).
Find the greater of two numbers.
Check if a number is divisible by 10 or not.

MID LEVEL :
Take 5 subject marks ,calculate average and print:
≥90% → Grade A
≥75% → Grade B
≥50% → Grade C
else Fail
Find the largest of three numbers.
Check if a year is Leap year or not.
Create a simple calculator (+, -, *, / based on user input).
Check if a number is:
divisible by 3 → “Fizz”
divisible by 5 → “Buzz”
both → “FizzBuzz”
      6. Take a number and check:
if even → divide by 2
if odd → multiply by 3 and add 1
 (Print result )
       7. Electricity bill calculation:
First 100 units → ₹5/unit
Next 100 → ₹7/unit
Above → ₹10/unit'''
# TASK 5 
'''WAP to print series of numbers from 3 to 39.
WAP to print series of numbers from 15 to 5.
WAP to print numbers divisible by 7 in range 1 to 21.
WAP to print the numbers which are divisible by both 3 and 5 from 5 to 13.
WAP to print divisor of 24 from 3 to 12.
WAP to count total no .of divisor of the given number.
WAP to check that count of the divisor of a given number is equal to 2 . If it is equal print prime number else print not a prime number.
WAP to print sum of the numbers present from 3 to 9.
WAP to print sum of the digits present in a number.
WAP to print sum of the odd digit present in a number.'''




# ANSWERS OF TASK 1
# A1
'''s = "Python"

print(s[-6])  # P
print(s[-1])  # n
print(s[-4])  # t
#A2
num = [10, 20, 30, 40, 50]
print(" first element",num[0])
print("last element",num[-1])
print("second last element",num[3])
#A3
word="programming"
print(word[3])
print(word[-7])
print(word[2])
#A4
s="PythonProgramming"
print(s[0:6])
print(s[6:])
#A5
numbers = [10,20,30,40,50,60,70]
print(numbers[1:4])
print(numbers[4:])
#A6
text = "ABCDEFGHIJ"
print(text[::2])
print(text[-2:-2])
#A7
student = {"name":"Rahul","age":20,"marks":75}
student["marks"]=85
print(student)



#TASK 2 ANSWERS
#A1

text = "PYTHONPROGRAM"
print(text[::2])
#A2
text = "ABCDEFGHIJK"
print(text[2:8])

#A3
text = "PROGRAMMING"
print(text[::-1])
#A4
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[0:4])
print(numbers[4:])
#A5
text = "PYTHONDEVELOPER"
print(text[: :-1])
 #TASK 3  ANSWERS
 #A1
n = int(input("Enter number: "))
if n > 0:
    print("Positive")
    #A2
n = int(input("Enter number: "))
if n % 2 == 0:
    print("Even")
    #A3
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible for voting")
    #A4
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible for voting")
    #A5
ch = input("Enter character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
    #A6
n = int(input("Enter number: "))
if n % 5 == 0:
    print("Multiple of 5")
    #A7
n = int(input("Enter number: "))
if n < 0:
    print("Negative")
    #A8
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
    #A9
n = int(input("Enter number: "))
if n < 10:
    print(n*n)
    #A10
temp = int(input("Enter temperature: "))
if temp > 30:
    print("Hot")
    #A11
n = int(input("Enter number: "))
if 10 <= n <= 99:
    print("Two-digit number")
    #A12
n = int(input("Enter number: "))
if n % 10 == 5:
    print("Ends with 5")
    #A13
n = int(input("Enter number: "))
if int(n**0.5) * int(n**0.5) == n:
    print("Perfect square")
    #A14
n = input("Enter number: ")
mid = len(n)//2
if n[:mid] == n[-mid:]:
    print("Palindrome candidate")
    #A15
n = int(input("Enter number: "))
if n % 3 == 0 and n % 7 == 0:
    print("Special number")
    #A16
s = input("Enter string: ")
if s[0].isupper():
    print("Starts with capital letter")
    #A17
n = input("Enter number: ")
if "0" in n:
    print("Contains 0")
    #TASK 4 ANSWERS
    #BASIC LEVEL
    #A1
n = int(input("Enter number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
    #A2
n = int(input("Enter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")    
    #A3
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")
    #A4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater:", a)
else:
    print("Greater:", b)
    #A5
n = int(input("Enter number: "))
if n % 10 == 0:
    print("Divisible by 10")
else:
    print("Not divisible by 10")
    #MID LEVEL
    #A1
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
m4 = int(input("Enter marks 4: "))
m5 = int(input("Enter marks 5: "))

avg = (m1 + m2 + m3 + m4 + m5) / 5

if avg >= 90:
    print("Grade A")
elif avg >= 75:
    print("Grade B")
elif avg >= 50:
    print("Grade C")
else:
    print("Fail")
    #A2
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
    #A3
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
    #A4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")
    #A5
n = int(input("Enter number: "))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
    #A6
n = int(input("Enter number: "))

if n % 2 == 0:
    print(n / 2)
else:
    print(n * 3 + 1)
    #A7
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Total bill:", bill)
#TASK 5 ANSWERS
#A1
for i in range(3, 40):
    print(i)
    #A2
for i in range(15, 4, -1):
    print(i)
    #A3
for i in range(1, 22):
    if i % 7 == 0:
        print(i)
   #A4
for i in range(5, 14):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
#A5
for i in range(3, 13):
    if 24 % i == 0:
        print(i)
#A6
n = int(input("Enter number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

print("Total divisors:", count)
#A7
n = int(input("Enter number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")
#A8
sum = 0

for i in range(3, 10):
    sum += i

print("Sum:", sum)
#A9
n = int(input("Enter number: "))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10

print("Sum of digits:", sum)
#A10
n = int(input("Enter number: "))
sum = 0

while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        sum += digit
    n = n // 10

print("Sum of odd digits:", sum)'''
# WHILE LOOP QUESTIONS 
''' Number Based
1. Print numbers from 1 to 20 using while loop
2. Print all odd numbers between 1 to 50
3. Find sum of first N natural numbers
4. Reverse a number (e.g., 123 → 321)
5. Count digits in a number
6. Find sum of digits of a number
7. Check if a number is palindrome
8. Print multiplication table of a number
9. Find factorial of a number
10. Check if a number is prime
STRING
1. Print each character of a string using while loop
2. Count number of vowels in a string
3. Count number of consonants
4. Reverse a string using while loop
5. Check if string is palindrome
6. Count occurrence of a specific character
7. Convert lowercase to uppercase manually (without built-in)
8. Find length of string without using len()
9. Remove spaces from a string
10. Count number of words in a string
LIST
1. Print all elements of a list using while loop
2. Find sum of all elements
3. Find maximum element in list
4. Find minimum element
5. Count even and odd numbers
6. Search an element in list (linear search)
7. Reverse a list using while loop
8. Count occurrence of a given element
9. Create a new list with only even numbers
10. Remove duplicates from list
MIXED
1. Take number input and store digits in list
2. Merge two lists using while loop
3. Find common elements in two lists
4. Check if two strings are anagrams
5. Convert number to string without using str()
6. Find second largest element in list
7. Check if list is palindrome
8. Count frequency of each character in string
9. Create list of squares from 1 to N
10. Remove all vowels from string 
 '''
# more questions
'''  Write a Python program to check whether a given number is even or odd.
● Write a Python program to find the sum of numbers between m and n.
● Write a Python program to find the product of numbers between m and n.
● Write a Python program to count the numbers from m to n.
● Write a Python program to swap two numbers using a third variable.
● Write a Python program to swap two numbers without using a third variable.
● Write a Python program to find the square of a given number.
● Write a Python program to find the cube of a given number.
● Write a Python program to find the factorial of a given number.
● Write a Python program to find the factors of a given number.
● Write a Python program to print the Fibonacci series up to a given number.
● Write a Python program to compute the exponential value for a given base and
power (xⁿ).
● Write a Python program to extract digits of a number in reverse order and print them.
● Write a Python program to count the digits of a given number.
● Write a Python program to find the sum of digits of a given number.
● Write a Python program to find the product of digits of a given number.
● Write a Python program to reverse a given number.
● Write a Python program to print a solid square of stars of size n (e.g., 5×5).
● Write a Python program to print a hollow square of stars of size n.
● Write a Python program to print a square with diagonal elements as '*' and rest as
space for size n.
● Write a Python program to print a right‑angled triangle of stars of height n.
● Write a Python program to print an inverted right‑angled triangle of stars of height n.
● Write a Python program to print a full pyramid of stars of height n.
● Write a Python program to print an inverted full pyramid of stars of height n.
● Write a Python program to print a diamond pattern of stars of size n.
● Write a Python program to print all elements in an array.
● Write a Python program to count the number of elements in an array.
● Write a Python program to print the elements of an array in reverse order.
● Write a Python program to print all elements at even indices in an array.
● Write a Python program to calculate the sum of all elements in an array.
● Write a Python program to print all duplicate elements in an array.
● Write a Python program to sort an array without using predefined methods.
● Write a Python program to merge two arrays.
● Write a Python program to print the largest element in a given array.
● Write a Python program to print the smallest element in a given array.
● Write a Python program to find the frequency of each element in an array.
● Write a Python program to copy all elements from one array to another array.
● Write a Python program to extract all characters from a given string.
● Write a Python program to print only alphabets from a given string.
● Write a Python program to print only digits from a given string.
● Write a Python program to print only special characters from a given string.
● Write a Python program to reverse a given string.
● Write a Python program to extract all duplicate characters from a given string.
● Write a Python program to extract all words from a given string.
● Write a Python program to print the multiplication table of a given number.
● Write a Python program to check whether a given number is prime or not.
● Write a Python program to print the sum of prime numbers between m and n.
● Write a Python program to print the product of prime numbers between m and n.
● Write a Python program to print the sum of the factors of a given number.
● Write a Python program to print the product of the factors of a given number.
● Write a Python program to print the sum of even and odd factors in a given number.
● Write a Python program to print the product of even and odd factors in a given
number.
● Write a Python program to count the digits in a given number.
● Write a Python program to print the even digits in a given number.
● Write a Python program to print the odd digits in a given number.
● Write a Python program to print the sum of digits in a given number.
● Write a Python program to print the product of digits in a given number.
● Write a Python program to print the sum of even digits in a given number.
● Write a Python program to print the sum of prime digits in a given number.
● Write a Python program to print the product of prime digits in a given number.
● Write a Python program to print the factorial of each digit in a given number.
● Write a Python program to print the sum of factorial of each digit in a given number.
● Write a Python program to print the factorial of even digits in a given number.
● Write a Python program to print the factorial of odd digits in a given number.
● Write a Python program to print the power of each digit raised to the number of digits
in the given number.
● Write a Python program to print the sum of powers of each digit raised to the number
of digits in the given number.
● Write a Python program to print the sum of powers of even digits raised to the
number of digits in the given number.
● Write a Python program to print the sum of powers of odd digits raised to the number
of digits in the given number.
● Write a Python program to print the nth prime number.
● Write a Python program to print the next prime number for a given number.
● Write a Python program to print the nth Fibonacci number.
● Write a Python program to check if a given number is a Fibonacci number.
● Write a Python program to find the largest digit in a given number.
● Write a Python program to find the smallest digit in a given number.
● Write a Python program to find the nth largest digit in a given number.
● Write a Python program to find the nth smallest digit in a given number.
● Write a Python program to find the sum of the smallest and largest digits in a given
number.
● Write a Python program to find the sum of the nth smallest and nth largest digits in a
given number.
● Write a Python program to find the binary representation of a decimal number.
● Write a Python program to find the decimal representation of a binary number.
● Write a Python program to find the GCD (HCF) of two numbers.
● Write a Python program to find the LCM of two numbers.
● Write a Python program to print a square number pattern where each row contains
the same number from 1 to n.
● Write a Python program to print a hollow square with numbers at the border and
space inside for size n.
● Write a Python program to print a square pattern with alternating 1s and 0s like a
chessboard of size n.
● Write a Python program to print a square where each cell contains the sum of row
and column indices (starting from 0) for size n.
● Write a Python program to print a number triangle with increasing numbers in each
row for height n.
● Write a Python program to print an inverted number triangle with decreasing numbers
in each row for height n.
● Write a Python program to print Floyd's triangle with continuous numbers for height n.
● Write a Python program to print a centred number pyramid of increasing numbers for
height n.
● Write a Python program to print an inverted number pyramid with decreasing width
for height n.
● Write a Python program to print a centred pyramid with alphabets increasing in each
row for height n.
● Write a Python program to print an inverted pyramid with alphabets decreasing in
each row for height n.
● Write a Python program to print a pyramid where each row contains increasing odd
numbers for height n.
● Write a Python program to print a pyramid where each row contains increasing even
numbers for height n.
● Write a Python program to print a diamond pattern using numbers increasing by 1 on
each line for size n.
● Write a Python program to print a diamond pattern using alphabets increasing
row‑wise (A to E) for size n.
● Write a Python program to print a diamond pattern where each row contains
consecutive alphabets for size n.
● Write a Python program to calculate the sum of all even elements in an array.
● Write a Python program to calculate the sum of all odd elements in an array.
● Write a Python program to calculate the sum of the first and last elements in an array.
● Write a Python program to calculate the sum of the last two elements in an array.
● Write a Python program to calculate the sum of all prime numbers in a given array.
● Write a Python program to calculate the product of all elements in an array.
● Write a Python program to calculate the product of all even elements in an array.
● Write a Python program to calculate the product of all prime numbers in a given
array.
● Write a Python program to calculate the average of all elements in a given array.
● Write a Python program to check if the product of the last two elements in an array is
even.
● Write a Python program to find the frequency of each element in an array.
● Write a Python program to remove the most repeated elements from an array.
● Write a Python program to remove the most repeated even elements from an array.
● Write a Python program to remove duplicates from a sorted array.
● Write a Python program to print duplicate elements at even indices in an array.
● Write a Python program to merge two arrays and find duplicate elements in the
merged array.
● Write a Python program to calculate the sum of duplicate elements in a given array.
● Write a Python program to sort only the positive elements in a given array.
● Write a Python program to sort only the even elements in a given array.
● Write a Python program to sort only the prime elements in a given array.
● Write a Python program to merge two arrays and sort the merged elements.
● Write a Python program to sort only the first two and last two elements in a given
array.
● Write a Python program to print the second largest element in an array.
● Write a Python program to print the second smallest element in an array.
● Write a Python program to print the nth largest element in a given array.
● Write a Python program to print the nth smallest element in a given array.
● Write a Python program to print the largest even element in a given array.
● Write a Python program to print the smallest odd element in a given array.
● Write a Python program to print the largest prime number in a given array.
● Write a Python program to calculate the sum of the largest and smallest elements in
an array.
● Write a Python program to calculate the product of the largest and smallest elements
in an array.
● Write a Python program to calculate the average of the largest and smallest elements
in an array.
● Write a Python program to calculate the difference between the largest and smallest
elements in an array.
● Write a Python program to merge only the even elements from two arrays into a
single array and print it in reverse order.
● Write a Python program to sort two arrays in ascending order, merge them, and print
only the even numbers.
● Write a Python program to sort the prime numbers from two arrays and merge them
into a single array.
● Write a Python program to merge the largest and smallest elements from two arrays
into a single array.
● Write a Python program to print all prime numbers in an array.
● Write a Python program to calculate the sum of the last four even numbers in an
array.
● Write a Python program to rotate an array to the left by a given number of steps.
● Write a Python program to rotate an array to the right by a given number of steps.
● Write a Python program to find the first non‑repeating element in an array.
● Write a Python program to check if an array is a palindrome.
● Write a Python program to remove an element from an array at a specific position.
● Write a Python program to check if two arrays are equal or not.
● Write a Python program to count the number of elements in an array without using
the len() function.
● Write a Python program to find the maximum product of two integers in an array.
● Write a Python program to calculate the prefix sum array.
● Write a Python program to find pairs in an array with a given sum.
● Write a Python program to reverse a string while maintaining the position of spaces.
● Write a Python program to check if a string is a palindrome.
● Write a Python program to count the frequency of each character in a string.
● Write a Python program to find the first non‑repeated character in a string.
● Write a Python program to find the second most frequent character in a string.
● Write a Python program to find the first repeating character in a string.
● Write a Python program to reverse only the digits present in a string.
● Write a Python program to replace duplicate characters with '*'.
● Write a Python program to remove a specific character from a string.
● Write a Python program to check if a string is made up of unique characters.
● Write a Python program to find the longest palindrome in a string.
● Write a Python program to find the smallest palindrome in a string.
● Write a Python program to find the smallest and largest words in a string.
● Write a Python program to find the frequency of each word in a string.
● Write a Python program to reverse each word in a string individually.
● Write a Python program to replace all spaces in a string with '%20'.
● Write a Python program to check if two strings are rotations of each other.
● Write a Python program to implement your own substring method.
● Write a Python program to implement your own split method for a string.
● Write a Python program to implement your own indexOf method for strings.
● Write a Python program to implement your own trim method for strings.
● Write a Python program to implement your own toLowerCase and toUpperCase
methods.
● Write a Python program to convert a string to its ASCII representation.
● Write a Python program to convert a string to its equivalent integer representation.
● Write a Python program to replace all vowels in a string with a given character.
● Write a Python program to check whether a given number is a Twisted Prime number
or not.
● Write a Python program to check whether a given number is a Mega Prime number
or not.
● Write a Python program to check whether a given number is a Palindrome number or
not.
● Write a Python program to check whether a given number is a SPY number or not.
● Write a Python program to check whether a given number is a Perfect number or not.
● Write a Python program to check whether a given number is a Strong number or not.
● Write a Python program to check whether a given number is a Neon number or not.
● Write a Python program to check whether a given number is an Armstrong number or
not.
● Write a Python program to check whether a given number is a Sunny number or not.
● Write a Python program to check whether a given number is an Automorphic number
or not.
● Write a Python program to check whether a given number is a Magic number or not.
● Write a Python program to check whether a given number is a Tech number or not.
● Write a Python program to check whether a given number is a Harshad (Niven)
number or not.
● Write a Python program to print the Twisted Prime numbers in the range from m to n.
● Write a Python program to print the Mega Prime numbers in the range from m to n.
● Write a Python program to print the Palindrome numbers in the range from m to n.
● Write a Python program to print the SPY numbers in the range from m to n.
● Write a Python program to print the Perfect numbers in the range from m to n.
● Write a Python program to print the Strong numbers in the range from m to n.
● Write a Python program to print the Neon numbers in the range from m to n.
● Write a Python program to print the Armstrong numbers in the range from m to n.
● Write a Python program to print the Sunny numbers in the range from m to n.
● Write a Python program to print the Automorphic numbers in the range from m to n.
● Write a Python program to print the Magic numbers in the range from m to n.
● Write a Python program to print the Tech numbers in the range from m to n.
● Write a Python program to print the Harshad (Niven) numbers in the range from m to
n.
● Write a Python program to print the nth Prime number.
● Write a Python program to print the nth Twisted Prime number.
● Write a Python program to print the nth Mega Prime number.
● Write a Python program to print the nth Palindrome number.
● Write a Python program to print the nth Sunny number.
● Write a Python program to print the nth Automorphic number.
● Write a Python program to print the nth Magic number.
● Write a Python program to print the nth Harshad (Niven) number.
● Write a Python program to print the Lucas series up to n terms.
● Write a Python program to print the factorial series up to n terms.
● Write a Python program to generate the Collatz sequence for a given number.
● Write a Python program to find the GCD or HCF of three numbers.
● Write a Python program to generate the first n terms of a Tribonacci sequence.
● Write a Python program to print a zigzag number pattern in a square of size n.
● Write a Python program to print Pascal's triangle up to n rows.
● Write a Python program to print a palindromic number triangle of height n.
● Write a Python program to print an alphabet palindromic pyramid of height n.
● Write a Python program to print a number mirror pyramid of height n.
● Write a Python program to print an alternating character pyramid of height n.
● Write a Python program to print a hollow number pyramid of height n.
● Write a Python program to print a zig‑zag alphabet pyramid of height n.
● Write a Python program to print an alphabet full diamond of size n.
● Write a Python program to print a hollow diamond with alphabets of size n.
● Write a Python program to print a double‑sided number diamond of size n.
● Write a Python program to print a number hourglass pattern of size n.
● Write a Python program to print an alphabet hourglass pattern of size n.
● Write a Python program to print a hollow hourglass with alphabets of size n.
● Write a Python program to check if the sum of all array elements is an Armstrong
number.
● Write a Python program to check if the product of all array elements is a palindrome.
● Write a Python program to check if the sum of all even elements in an array is a
strong number.
● Write a Python program to check if the sum of all odd elements in an array is an
Armstrong number.
● Write a Python program to implement the MergeSort algorithm to sort an array in
ascending order.
● Write a Python program to implement the QuickSort algorithm to sort an array in
ascending order.
● Write a Python program to replace every element in an array with the next greatest
element (from the right side), replacing the last element with -1.
● Write a Python program to rearrange an array with alternate high and low elements.
● Write a Python program to find the missing element in an array containing integers
from 1 to n with one element missing.
● Write a Python program to find the majority element in an array (element that
appears more than n/2 times) using Boyer‑Moore algorithm.
● Write a Python program to check if an array can be made strictly increasing by
removing at most one element.
● Write a Python program to find a peak element in an array (element strictly greater
than its neighbors) in O(log n) time.
● Write a Python program to remove consecutive duplicate characters from a string.
● Write a Python program to implement your own strstr() function to find the first
occurrence of a substring.
● Write a Python program to remove all characters from the first string that appear in
the second string.
● Write a Python program to check if two strings are isomorphic.
● Write a Python program to perform run‑length encoding on a string.
● Write a Python program to capitalize the first letter of each word in a string.
● Write a Python program to find all substrings of a given string.
● Write a Python program to check if one string is a permutation of another.
● Write a Python program to check if a string is a valid palindrome ignoring
non‑alphanumeric characters and case.
● Write a Python program to find the minimum window substring in a string s that
contains all characters of another string t.
● Write a Python program to check if a pattern matches a string (word pattern).
● Write a Python program to find the length of the longest substring without repeating
characters.
● Write a Python program to decode an encoded string where patterns are in the form
k[encoded_string] (nested encoding).
● Write a Python program to reverse a string without affecting special characters.
● Write a Python program to check if two strings are one edit away (insert, remove,
replace).
● Write a Python program to find the longest palindromic subsequence in a string.
● Write a Python program to remove duplicate letters from a string to get the
lexicographically smallest result.
● Write a Python program to find the minimum number of insertions required to make a
string a palindrome.
● Write a Python program to find the smallest substring in a given string that contains
all characters of another string.
● Write a Python program to check if two strings are anagrams.
● Write a Python program to group all anagrams together from a given list of strings.
● Write a Python program to check if two strings are k‑anagrams (can be made
anagrams by changing at most k characters).
● Write a Python program to find all starting indices of substrings in a string that are
anagrams of a given pattern.
● Write a Python program to check if one string is a rotation and also an anagram of
another string '''
# WHILE loop answwers
#A1



















"""
Maeve O'Toole

lab2.py

This program demonstrates the arithmetic side of Python
We will develop Python programs that do input, produce output,
and do arithmetic while using the Python math library.

This assignment is entirely my own work.

"""
import math

#Sum of Threes

def sum_of_threes():
    acc = 0
    y = eval(input("Enter your upper bound: "))
    for x in range(0, y + 1, 3):
        acc = acc + x
    print(acc)
sum_of_threes()
        # range function takes three arguements (start, end (which is 1 plus your wanted end, and step)
        # make sure you add one if your end is a variable
        # acc accumulates all of your numbers together

#Multiplication Table

def multiplication_table():
    # h (height) x l (length) to make it a table
    for h in range(1, 11): #vertical movement
        for l in range(1, 11): #horizontal movement
            print((h * l), end=" ")
        print()
multiplication_table()

#Computing the Area of a Triangle

def triangle_area():
    a = eval(input("Enter the length of side a:"))
    b = eval(input("Enter the length of side b:"))
    c = eval(input("Enter the length of side c:"))
    s = (a + b + c)/2
    x = s*(s-a)*(s-b)*(s-c)
    A = math.sqrt(x)
    print(A)
triangle_area()

def sumSquares():
    acc = 0
    start = eval(input("Enter the number you would like your range to begin with: "))
    end = eval(input("Enter the number you would like your range to end with: "))
    for x in range( start, end + 1 ):
        acc = acc + ( x ** 2 )
    print(acc)
sumSquares()

def power():
    acc = 1
    base = eval(input("Enter your base value: "))
    exponent = eval(input("Enter your exponent value: "))
    for x in range(exponent): # range(0, exponent, 1)
        acc = acc * base
    print(base, "^", exponent, "=", acc)
power()





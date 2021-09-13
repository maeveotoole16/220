"""
Maeve O'Toole

lab3.py

This program is aimed to develop a simple Python program
that asks for inputs, produce outputs, and does arithmetic
using loops.

This assignment is entirely my own work.

"""

def average():
    num = eval(input("Enter the number of homework assignments here: "))
    acc = 0
    for i in range(1, num + 1):
        grade = eval(input("Enter your grade on homework" + str(i)))
        acc = acc + grade
    print("Your average grade is ", (acc / num), "%")
average()

def tip_jar():
    acc = 0
    for i in range(5):
        donation = eval(input("How much was placed in the tip jar?"))
        acc = acc + donation
    print("The total amount in the jar is $", acc)
tip_jar()

def newton():
    num = eval(input("Enter the number you would like to approximate the square root of: "))
    ref = eval(input("How many times would you like to refine?"))
    approx = num / 2
    for i in range(ref):
        approx = (approx + ( num / approx )) / 2
    print(approx)
newton()

def sequence():
    x = eval(input("How many terms are in the series?"))
    for i in range(1, x + 1):
        c = 1 + (i // 2 * 2)
        print(c)
sequence()

def pi():
    n = eval(input("Enter the number of terms in the series here: "))
    acc = 1
    for i in range(n):
        num = 2 + (i // 2 * 2)
        denom = 1 + ((i + 1) // 2 * 2)
        acc = (num / denom) * acc
    print("The approximation of pi is", acc)
pi()


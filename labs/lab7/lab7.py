"""
Maeve O'Toole

lab7.py

This lab uses Python text files to practice writing function that accept
arguments, return values, and modify an object in an parameter.

This assignment is entirely my own work.

"""

import math

def cash_conversion():
    dollar = eval(input("Enter the integer dollar amount here: "))
    print('${:.2f}'.format(dollar))

def encode():
    message = input("Enter the message to be encoded: ")
    key = eval(input("Enter how far you want to shift your message: "))
    acc = " "
    for x in message:
        i = ord(x)
        i = i + key
        new = chr(i)
        acc = acc + new
    print(acc)

def sphere_area(radius):

    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area

def sphere_volume(radius):

    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
        total = acc
    return total

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + (i ** 3)
        total = acc
    return total

def encode_better():

    message1 = input("Enter your first string here: ")
    message2 = input("Enter your second string here: ")
    acc = ""
    for i in range(len(message1)):
        c = ord(message1[i])
        key = ord(message2[i])
        new_message = (c + key) - 97
        acc = acc + chr(new_message)
    print(acc)


def main():

    cash_conversion()
    encode()
    sphere_area()
    sphere_volume()
    sum_n()
    sum_n_cubes()
    encode_better()

if __name__ == '__main__':
    main()

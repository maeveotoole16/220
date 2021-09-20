"""
Maeve O'Toole

mean.py

This program is aimed to help me create a Python program on my own,
develop a simply program that asks for the input, does arithmetic,
and also provides an output. This program will help practice definite
loops as well as apply the software development process that we have
been practicing implementing when we code.

This assignment is entirely my own work.

"""

# Apply the Software Development Process

#1 What will this program do?
# This program will write a Python program to output the root-mean-square
# average of a series of numbers, the Harmonic Mean and the Geometric Mean.
# These represent three different methods for calculating a mean of a set of
# numbers.

#2 What will be the inputs and outputs?
# The input will ask the user to enter a number in which they want to know
# the rms average, the harmonic average, and the geometric mean of.
# The output will give you, separately, the rms average, harmonic average,
# and geometric mean of the users specified input value.

#3 What is a step-by-step list of what the program must do, aka an algorithm?
# ask user for the input of values they want to calculate the mean of
# calculate the rms average
# calculate the harmonic average
# calculate the geometric mean
# return the values based on the users input in the console below

import math

def main():

    num = eval(input("Enter the values to be entered: "))

    rmsacc = 0
    harmacc = 0
    geoacc = 1

    for i in range(1, num + 1):

        value = eval(input("Enter value " + str(i)))
        rmsacc = rmsacc + (value ** 2)
        harmacc = harmacc + (1/value)
        geoacc = geoacc * value

    print(round(math.sqrt( rmsacc / num ), 3))
    print(round( num / harmacc, 3))
    print(round((geoacc ** ( 1 / num )), 3))

if __name__ == '__main__':
    main()

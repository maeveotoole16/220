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
# ask user for the input of values
# calculate the rms average
# calculate the harmonic average
# calculate the geometric mean
# return the values based on the users input in the console

import math

def main():
    print("This program calculates the RMS Average, the Harmonic Mean, and the Geometric Mean")
    n = eval(input("Enter the numbers you would like to evaluate here: "))
    rms_ave = math.sqrt(((math.fsum(1, n+1)) * x ** 2) / n ))
    har_mean =

if __name__ == '__main__':
    main()



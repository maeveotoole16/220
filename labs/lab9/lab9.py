"""
Maeve O'Toole

lab9.py

This program is my lab9 functions.

This assignment is entirely my own work.

"""

def addTen(nums):

    for i in range(len(nums)):
        nums[i] = nums[i] + 10

def squareEach(nums):

    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):

    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc

def toNumbers(strList):

    for i in range(len(strList)):
        strList[i] = float(strList[i])

def writeSumOfSquares():

    in_file = input("Enter the file name here: ")
    out_file = input("Enter the file you want to write into here: ")

    # create infile

    infile = open(in_file, 'r')
    outfile = open(out_file, 'w+')

    for line in infile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        outfile.write("Sum of squares = " + str(summation))

def starter():

    weight = eval(input("Enter weight value here: "))
    wins = eval(input("Enter the number of wins the player has had here: "))

    if (weight >= 150 and weight < 160) and (wins >= 5):
        print("This player is a starter")
    elif (weight > 199) or (wins > 10):
        print("This player is a starter")
    else:
        print("This player is NOT a starter")

def leapYear(year):

    if (year % 100 != 0 or year % 400 == 0) and (year % 4 == 0):
        return True
    else:
        return False

from graphics import *
import math

def circleOverlap():

    win = GraphWin("Circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, radius)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, radius2)
    c2.draw(win)

    total_radius = radius + radius2
    dist = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)

    if total_radius >= dist:
        text1 = Text(Point(200, 50), "Your Circles Overlap!")
        text1.draw(win)
    else:
        if total_radius < dist:
            text2 = Text(Point(200, 50), "Your Circles do NOT Overlap!")
            text2.draw(win)

    win.getMouse()
    win.close()

def main():

    addTen()
    squareEach()
    sumList()
    toNumbers()
    writeSumOfSquares()
    starter()
    leapYear()
    circleOverlap()

if __name__ == '__main__':
    main()

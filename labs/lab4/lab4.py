"""
Maeve O'Toole

lab4.py

This lab is aimed to use Python graphics and the author-supplied graphics
package to practice accumulating sequence.

This assignment is entirely my own work.

"""

from graphics import *

import math

def squares():

    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move the square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("pink")
    shape.setFill("pink")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        user_click = win.getMouse()

        shape = Rectangle(Point(user_click.getX() - 10, user_click.getY() - 10), Point(user_click.getX() + 10, user_click.getY() + 10))
        shape.setOutline("pink")
        shape.setFill("pink")
        shape.draw(win)

    inst_pt = Point(width / 2, height - 25)
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)

    win.getMouse()  # waits to close until you click
    win.close()

def rectangle():

    width = 400
    height = 400
    win = GraphWin("Draw a Rectangle", width, height)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    rectangle = Rectangle(p1, p2)
    rectangle.setFill("pink")
    rectangle.setOutline("black")
    rectangle.draw(win)

    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getY() - p1.getY())
    area = length * width
    perimeter = 2 * (length * width)

    text1 = Text(Point(200, height - 40), "The area is " + str(area))
    text2 = Text(Point(200, height - 25), "The perimeter is " + str(perimeter))

    text1.draw(win)
    text2.draw(win)

    win.getMouse()
    win.close()

def circle():
    width = 400
    height = 400
    win = GraphWin("Draw a Circle", width, height)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p2.getY()
    y2 = p2.getY()

    r = math.sqrt(((x2 - x1)**2) - ((y2 - y1)**2))

    circle = Circle(p1, r)
    circle.draw(win)
    circle.setFill("blue")

    text = Text(Point(200, height - 40), "The radius is " + str(r))
    text.draw(win)

    inst_pt = Point(200, height - 25)
    instructions = Text(inst_pt, "Click again to end the program")
    instructions.draw(win)

    win.getMouse()
    win.close()

def pi2():
    acc = 0
    n = eval(input("Enter number of terms: "))
    for i in range(n):
        num = 4
        denom = 1 + 2 * i
        fraction = ((num / denom) * ((-1)**i))
        acc = acc + fraction

    print(acc)
    print(math.pi - acc)

def main():

    squares()
    rectangle()
    circle()
    pi2()

if __name__ == '__main__':
    main()

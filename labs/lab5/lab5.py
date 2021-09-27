"""
Maeve O'Toole

lab5.py

This lab aims to help learn to use Python graphics.

This assignment is entirely my own work.

"""

from graphics import *
import math

def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    p1.draw(win)
    p2.draw(win)
    p3.draw(win)

    s1 = Line(p1, p2)
    s2 = Line(p2, p3)
    s3 = Line(p1, p3)
    s1.draw(win)
    s2.draw(win)
    s3.draw(win)

    l1 = math.sqrt((p1.getX() ** 2) + (p2.getY() ** 2))
    l2 = math.sqrt((p2.getX() ** 2) + (p3.getY() ** 2))
    l3 = math.sqrt((p1.getX() ** 2) + (p3.getY() ** 2))

    # and display its area in the graphics window.
    perimeter = l1 + l2 + l3
    perimeter_text = Text(Point(250, 100), "The perimeter = " + str(perimeter))
    perimeter_text.draw(win)

    s = (l1 + l2 + l3) / 2
    area = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))
    area_text = Text(Point(250, 50), "The area = " + str(area))
    area_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 20, win_height / 2 + 40)
    r = Entry(Point(win_width / 1.8, win_height / 2 + 40), 5)
    r.draw(win)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    g = Entry(Point(win_width / 1.8, win_height / 2 + 70), 5)
    g.draw(win)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    b1 = Entry(Point( win_width / 1.8, win_height / 2 + 100), 5)
    b1.draw(win)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    for i in range(5):
        red = int(r.getText())
        green = int(g.getText())
        blue = int(b1.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
        win.getMouse()


    win.close()

def process_string():
    inp = input("Enter a string here: ")

    first = inp[0]
    print(first)

    last = inp[-1]
    print(last)

    pos25 = inp[2:6]
    print(pos25)

    conc = inp[0] + inp[-1]
    print(conc)

    first3 = inp[0:3] * 10
    print(first3)

    for i in inp:
        print(i)

    length = len(inp)
    print(length)

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)

    x = values[0] + values[2]
    print(x)

    x = values[1] * 5
    print(x)

    x = [ values[2], values[3], pt ]
    print(x)

    x = [ values[2], values[3], values[0]]
    print(x)

    x = [values[2], values[0], float(values[-1])]
    print(x)

    x = values[0] + values[2] + float(values[-1])
    print(x)

    x = len(values)
    print(x)

def another_series():
    num = eval(input("Enter the number of terms: "))
    acc = 0

    for x in range(num):
        y = 2 + (2 * (x % 3))
        print(y, end=" ")
        acc = acc + y
    print()
    print("sum =", acc)

def main():

    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()

if __name__ == '__main__':
    main()

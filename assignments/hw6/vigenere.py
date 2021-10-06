"""
Maeve O'Toole

vigenere.py

This program will implement the Vigenere cipher.
It is aimed to practice processing string data as
well as function development using the author's
graphics package.

This assignment is entirely my own work.

"""

from graphics import *

def main():

    win = GraphWin("Vigenere Cipher", 500, 500)
    win.setCoords(0, 0, 10, 10)

    message = Text(Point(3.8, 8.5), "Message to Code: ")
    message.draw(win)

    input1 = Entry(Point(6, 8.5), 15)
    input1.draw(win)

    keyword = Text(Point(3.8, 7.5), "Enter Keyword: ")
    keyword.draw(win)

    input2 = Entry(Point(6, 7.5), 15)
    input2.draw(win)

    output_text = Text(Point(3, 2.5), " Resulting Message: ")
    output_text.draw(win)

    button_text = Text(Point(5, 5), "Encode!")
    button_outline = Rectangle(Point(3, 6), Point(7, 4))
    button_text.draw(win)
    button_outline.draw(win)

    # process input

    win.getMouse()
    message2 = Text(Point(5, .5), "Click anywhere to close!")
    message2.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
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

def code(message, keyword):

    coded_phrase = ""
    keyword = keyword.upper()
    message = message.upper()
    message = message.replace(" ", "")

    for i in range(len(message)):
        ordinal = ord(message[i])
        ordinal = (((ordinal - 65) + (ord(keyword[i % len(keyword)]) - 65)) % 26) + 65
        coded_phrase = coded_phrase + chr(ordinal)

    return coded_phrase

def box():

    win = GraphWin("Vigenere", 500, 500)
    win.setCoords(0, 0, 10, 10)

    message_text = Text(Point(3.8, 8.5), "Message to Code: ")
    message_text.draw(win)

    keyword_text = Text(Point(3.8, 7.5), "Enter Keyword: ")
    keyword_text.draw(win)

    input2 = Entry(Point(6, 7.5), 18)
    input2.draw(win)

    input1 = Entry(Point(6, 8.5), 17)
    input1.draw(win)

    button_text = Text(Point(5, 5), "Encode!")
    button_outline = Rectangle(Point(3, 6), Point(7, 4))
    button_text.draw(win)
    button_outline.draw(win)

    win.getMouse()

    message = input1.getText()
    keyword = input2.getText()

    button_outline.undraw()
    button_text.undraw()

    output_val = Text(Point(5, 5), " Resulting Message: " + code(message, keyword))
    output_val.draw(win)

    message2 = Text(Point(5, .5), "Click anywhere to close!")
    message2.draw(win)
    win.getMouse()
    win.close()

def main():

    box()

if __name__ == '__main__':
    main()

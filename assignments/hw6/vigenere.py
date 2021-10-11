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
    encrypted = ""
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    i = 0
    for letter in message:
        if letter in alphabets:
            if (i == len(keyword)):
                i = 0
            letterIndex = alphabets.index(letter)
            keyIndex = alphabets.index(keyword[i])
            newIndex = letterIndex + keyIndex
            if (newIndex > 25):
                newIndex = newIndex % 26

            encrypted = encrypted + alphabets[newIndex]
            i = i + 1
        else:
            encrypted = encrypted + letter
    return encrypted

    message1 = input("Enter your first string here: ")
    message2 = input("Enter your second string here: ")
    acc = ""
    for i in range(len(message1)):
        c = ord(message1[i])
        key = ord(message2[i])
        new_message = (c + key) - 97
        acc = acc + chr(new_message)
    print(acc)

def box():

    win = GraphWin("Vigenere Cipher", 500, 500)
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

    output_val = Text(Point(3, 5), " Resulting Message: " + code(message, keyword))
    output_val.draw(win)

    message2 = Text(Point(5, .5), "Click anywhere to close!")
    message2.draw(win)
    win.getMouse()
    win.close()

def main():

    box()

if __name__ == '__main__':
    main()

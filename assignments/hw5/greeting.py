"""
Maeve O'Toole

greeting.py

This program displays a heart using the graphics library
with an arrow that shoots through the heart to make a festive
Valentine's Day greeting card.

This assignment is entirely my work.

"""

from graphics import GraphWin
from graphics import Image
from graphics import Text
from graphics import Point

def main():

    win = GraphWin("Greeting Card", 600, 600)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("pink")

    message = Text(Point(5, 9.5), "HAPPY VALENTINES DAY!")
    message.setTextColor("white")
    message.setFace("courier")
    message.setStyle("bold")
    message.setSize(18)
    message.draw(win)

    heart = Image(Point(5, 5), "heart.gif")
    heart.draw(win)

    win.getMouse()
    arrow = Image(Point(0, .01), "pinkarrow.gif")
    arrow.draw(win)
    for _ in range(1000):
        arrow.move(.1, .0001)

    message2 = Text(Point(5, .5), "Click anywhere to close!")
    message2.setTextColor("white")
    message2.setFace("courier")
    message2.setStyle("bold")
    message2.setSize(12)
    message2.draw(win)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

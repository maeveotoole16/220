"""

Maeve O'Toole

three_door_game.py

This program will draw three buttons, being three labeled doors,
in a graphics window and randomly select one of the buttons as the
secret door. If you click on the right door, you win!

This assignment is entirely my own work.

"""

from random import randrange
from graphics import GraphWin
from graphics import Point
from graphics import Text
from graphics import Rectangle
from button import Button


def main():
    win = GraphWin("Three Door Game", 500, 500)
    win.setBackground('beige')
    win.setCoords(10, 10, 0, 0)

    message1 = Text(Point(5, 2), "I have a secret door...")
    message1.setTextColor('pink')
    message1.setStyle('bold')
    message1.setSize(20)
    message1.draw(win)

    message2 = Text(Point(5, 8), "Click to choose my door...")
    message2.setTextColor('pink')
    message2.setStyle('bold')
    message2.setSize(18)
    message2.draw(win)

    button1 = Button(Rectangle(Point(9, 4), Point(7, 7)), 'Door 1')
    button1.text.setTextColor('pink')
    button1.text.setStyle('bold')
    button1.draw(win)

    button2 = Button(Rectangle(Point(6, 4), Point(4, 7)), 'Door 2')
    button2.text.setTextColor('pink')
    button1.text.setStyle('bold')
    button2.draw(win)

    button3 = Button(Rectangle(Point(3, 4), Point(1, 7)), 'Door 3')
    button3.text.setTextColor('pink')
    button1.text.setStyle('bold')
    button3.draw(win)

    point = win.getMouse()
    message1.undraw()
    message2.undraw()

    answer = randrange(3)
    for button in [button1, button2, button3]:
        if button.is_clicked(point) and button == [button1, button2, button3][answer]:
            button.color_button('green')
            message3 = Text(Point(5, 2), "You win!")
            message3.setSize(18)
            message3.setTextColor('green')
            message3.draw(win)
            break
        if button.is_clicked(point):
            button.color_button("red")
            message4 = Text(Point(5, 2), "You lose!")
            message4.setSize(18)
            message4.setTextColor('red')
            message4.draw(win)
            break

    message5 = Text(Point(5, 8), "Click to Quit")
    message5.setSize(14)
    message5.setTextColor('pink')
    message5.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()

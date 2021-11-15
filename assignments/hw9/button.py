"""

Maeve O'Toole

button.py

This program encapsulates all the data needed for a button shown in a GUI.

This assignment is entirely my own work.

"""

from graphics import Text

class Button:
    def __init__(self, shape, label):

        self.shape = shape
        self.label = label
        self.text = Text(self.shape.getCenter(), label)

    def get_label(self):
        return self.label

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        xclick = point.getX()
        yclick = point.getY()
        x_p = self.shape.getP1().getX()
        x_p2 = self.shape.getP2().getX()
        y_p = self.shape.getP1().getY()
        y_p2 = self.shape.getP2().getY()
        return (xclick >= x_p) and (xclick <= x_p2) and (yclick >= y_p) and (yclick <= y_p2)

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)

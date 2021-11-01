"""

Maeve O'Toole

bumper.py

This program will develop a Python program that uses the graphics package
while also practicing decision statements.

This assignment is entirely my own work.

"""

import time
from random import randint
from graphics import Circle
from graphics import Point
from graphics import GraphWin
from graphics import color_rgb

def get_random(move_amount):

    return randint(-move_amount, move_amount)

def did_collide(ball, ball2):

    ball_center = ball.getCenter()
    ball2_center = ball2.getCenter()
    ball_x_pos = ball_center.getX()
    ball_y_pos = ball_center.getY()
    ball2_x_pos = ball2_center.getX()
    ball2_y_pos = ball2_center.getY()
    ball_radius = ball.getRadius()
    ball2_radius = ball2.getRadius()

    distance = (((ball2_x_pos - ball_x_pos) ** 2) + ((ball2_y_pos - ball_y_pos) ** 2)) ** (1/2)
    radius = ball_radius + ball2_radius

    if distance <= radius:
        answer = True
        get_random_color(ball)
        get_random_color(ball2)
    else:
        answer = False
    return answer

def hit_vertical(ball, win):

    ball_center = ball.getCenter()
    ball_x_pos = ball_center.getX()
    radius = ball.getRadius()
    width = win.getWidth()

    if (ball_x_pos <= radius) or (ball_x_pos >= (width - radius)):
        answer = True
        get_random_color(ball)
    else:
        answer = False
    return answer

def hit_horizontal(ball, win):

    ball_y_pos = ball.getCenter().getY()
    radius = ball.getRadius()
    height = win.getHeight()

    if ball_y_pos <= radius or ball_y_pos >= height - radius:
        answer = True
        get_random_color(ball)
    else:
        answer = False
    return answer

def get_random_color(ball):

    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    ball.setFill(color_rgb(red, green, blue))

def main():

    win = GraphWin("JoyRide Bumper Cars", 600, 600)
    width = win.getWidth()
    height = win.getHeight()

    radius = 20
    car1 = Circle(Point(radius + 30, height / 2), radius)
    car2 = Circle(Point(width - (radius - 30), height / 2), radius)

    get_random_color(car1)
    get_random_color(car2)
    car1.draw(win)
    car2.draw(win)

    c1x = get_random(80)
    c2x = get_random(80)
    c1y = get_random(80)
    c2y = get_random(80)

    while True:
        car1.move(c1x, c1y)
        if hit_horizontal(car1, win):
            c1y = -c1y
        if hit_vertical(car1, win):
            c1x = -c1x

        car2.move(c2x, c2y)
        if hit_horizontal(car2, win):
            c2y = -c2y
        if hit_vertical(car2, win):
            c2x = -c2x

        if did_collide(car1, car2):
            c1x = -c1x
            c2x = -c2x
            c1y = -c1y
            c2y = -c2y

        time.sleep(.1)

    win.getMouse()

if __name__ == '__main__':
    main()

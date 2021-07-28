"""
Project Number Eighteen - The Hirst Painting
Super basic program using the turtle module
"""

import random
from turtle import Turtle, Screen
import colorgram as cg

cg_colours = cg.extract("C:/Users/User/Pictures/sunset painting.jpg", 10)
list_colours = []

for i in range(len(cg_colours)):
    temp = cg_colours[i].rgb
    list_colours.append(temp)


def get_colours():
    return random.choice(list_colours)


timmy = Turtle()
timmy.shape('turtle')
timmy.color('blue')
timmy.speed(0)
timmy.pensize(3)
screen = Screen()
screen.colormode(255)
timmy.penup()
timmy.backward(200)
timmy.right(90)
timmy.forward(200)
timmy.left(90)


for _ in range(10):
    for _ in range(10):
        timmy.dot(25, get_colours())
        timmy.forward(50)
    timmy.backward(500)
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)






















screen.exitonclick()
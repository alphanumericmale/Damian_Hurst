import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
t = Turtle()
t.pensize(20)

t.hideturtle()

colours = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
           (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
           (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
           (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.penup()
t.setx(-300)
t.sety(300)


def make_dot():
    t.dot(20, random.choice(colours))


def draw_spiral(side_length):
    for _ in range(side_length - 1):
        make_dot()
        t.forward(50)
        x = side_length
    t.right(90)
    while x > 0:
        for _ in range(2):
            for _ in range(x - 1):
                make_dot()
                t.forward(50)
            t.right(90)
        x -= 1
    make_dot()


draw_spiral(12)
# make_dot()
s = Screen()
s.exitonclick()

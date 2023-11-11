import turtle
from turtle import Turtle, Screen
import random
color_list = [  (202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102),]

turtle.colormode(255)


tim = Turtle()

def go_to_initial_pos():
    tim.color("white")
    tim.pu()
    tim.seth(225)
    tim.forward(500)
    tim.seth(0)
    tim.pd()


def go_one_step_up():
    tim.color("white")
    tim.seth(90)
    tim.forward(50)
    tim.seth(180)
    tim.forward(500)
    tim.seth(0)

def get_one_line():
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.pu()
        tim.forward(50)

tim.shape("triangle")
tim.speed(0)
go_to_initial_pos()
for _ in range(10):
    get_one_line()
    go_one_step_up()
    








screen = Screen()
screen.exitonclick()
import turtle
import math


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()  # faz a tela nao sumir


def poligon(t, n, length):
    angle = 360 / n
    polyline(t, n , length, angle)
    turtle.mainloop()  # faz a tela nao sumir


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_lenght = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_lenght, step_angle)
    turtle.mainloop()  # faz a tela nao sumir


def circle(t, r):
    arc(t, r, 360)


bob = turtle.Turtle()
circle(bob, 100)

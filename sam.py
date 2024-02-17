from turtle import *

wop = Screen()
wop.screensize(800, 800)

wop.tracer(0)

# For the message
texts = Turtle()
texts.speed(10)
texts.hideturtle()

# Balloons
bal = Turtle()
bal.penup()
bal.hideturtle()

dy = 0
y = 0

def key1():
    global dy
    dy = 0.2


def small_curve():
    speed(0)
    for t in range(45):
        right(5)
        forward(1)

def small_hearts(x, y):
    penup()
    goto(x, y)
    pendown()
    pensize(0)
    color('white', 'red')
    begin_fill()
    left(140)
    forward(25)
    small_curve()

    left(160)
    small_curve()
    forward(25)
    end_fill()
    hideturtle()
    left(150)

def curve():
    speed(0)
    for j in range(320):
        right(0.7)
        forward(1)

def hearts(x, y):
    penup()
    goto(x, y)
    pendown()
    pensize(4)
    color('white', 'red')
    begin_fill()
    left(150)
    forward(145)
    curve()

    left(150)
    curve()
    forward(145)
    end_fill()
    hideturtle()
    left(150)

wop.listen()
wop.onkeypress(key1, 'Up')

onscreenclick(hearts, 1)
onscreenclick(small_hearts, 3)

while True:
    y += dy
    y %= 600

    bal.goto(320, y)
    bal.stamp()

    bal.goto(320, y - 800)
    bal.stamp()

    wop.update()
    bal.clear()
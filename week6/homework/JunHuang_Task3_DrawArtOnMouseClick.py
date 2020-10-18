import turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'light green', 'blue', 'purple', 'white', 'gold']

turtle.hideturtle()
turtle.bgcolor('black')

SCT = turtle.Turtle()
SCT.hideturtle()
SCT.speed('fastest')


def draw_SC(pensize, pencolor, size, color):
    SCT.pensize(pensize)
    SCT.pencolor(pencolor)

    SCT.fillcolor(color)
    SCT.begin_fill()

    for _ in range(90):
        SCT.forward(size)
        SCT.left(89)
        SCT.forward(size)
        SCT.forward(10)

    SCT.end_fill()


def draw_random_SC_in_position(x, y):
    pensize = random.randint(1, 8)
    pencolor = random.choice(colors)
    angle = random.randint(0, 180)
    SCsize = random.randint(5, 60)
    SCcolor = random.choice(colors)

    SCT.penup()
    SCT.goto(x, y)
    SCT.pendown()

    SCT.setheading(angle)
    draw_SC(pensize, pencolor, SCsize, SCcolor)


turtle.getscreen().onclick(draw_random_SC_in_position)
turtle.done()

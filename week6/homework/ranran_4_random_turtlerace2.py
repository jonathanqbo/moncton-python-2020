import turtle
import random

colors = ['blue', 'orange', 'green', 'yellow', 'cyan', 'chocolate', 'pink', 'magenta']


def set_turtle():
    turtlename.color(random.choice(colors))
    turtlename.shapesize(random.randint(2, 4))
    turtlename.penup()
    turtlename.setposition(-300, random.randint(-360, 360))


def turtle_movement():
    while True:
        turtlename.forward(random.randint(10, 20))
        if turtlename.xcor() >= 300:
            break


def finish_line():
    turtle22 = turtle.Turtle()
    turtle22.hideturtle()
    turtle22.pensize(30)
    turtle22.pencolor('red')
    turtle22.penup()
    turtle22.setposition(300, 1000)
    turtle22.setheading(180)
    turtle22.pendown()
    turtle22.goto(300, -1000)


set_turtle()
finish_line()
turtle_movement()
turtle.done()

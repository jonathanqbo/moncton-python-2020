import turtle
import random

turtlecircledrawer = turtle.Turtle()
turtlecircledrawer.hideturtle()
turtlecircledrawer.speed('fastest')
turtle.bgcolor('black')
colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow']


def drawing_line_random(x, y):
    turtlecircledrawer.penup()
    turtlecircledrawer.goto(x, y)

    circle_color = random.choice(colors)
    circle_size = random.randint(30, 100)
    turtle_color = random.choice(colors)

    turtlecircledrawer.fillcolor()
    turtlecircledrawer.color(turtle_color)
    turtlecircledrawer.begin_fill()
    turtlecircledrawer.pencolor(circle_color)
    turtlecircledrawer.pensize(random.randint(3, 7))
    turtlecircledrawer.pendown()
    turtlecircledrawer.setheading(random.randint(0, 360))
    turtlecircledrawer.circle(circle_size)
    turtlecircledrawer.end_fill()


turtle.getscreen().onclick(drawing_line_random)

turtle.done()

import turtle
import random

colors = ['yellow', 'green', 'blue', 'purple', 'orange', 'red', 'white', 'silver', 'brown']

turtle.hideturtle()
turtle.bgcolor('black')

star_turtle = turtle.Turtle()
star_turtle.hideturtle()
star_turtle.speed('fastest')


def draw_star(pensize, pencolor, size, color):
    star_turtle.pensize(pensize)
    star_turtle.pencolor(pencolor)

    star_turtle.fillcolor(color)
    star_turtle.begin_fill()

    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)
        star_turtle.forward(size)
        star_turtle.left(72)

    star_turtle.end_fill()


def draw_random_star_in_position(x, y):
    pensize = random.randint(1, 8)
    pencolor = random.choice(colors)
    angle = random.randint(0, 180)
    starsize = random.randint(5, 60)
    starcolor = random.choice(colors)

    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()

    star_turtle.setheading(angle)
    draw_star(pensize, pencolor, starsize, starcolor)


turtle.getscreen().onclick(draw_random_star_in_position)
turtle.done()



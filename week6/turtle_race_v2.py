"""
NOTE: for reference only.
"""
import random
import turtle


def create_turtle(color, size, x, y, pensize, hide):
    race_turtle = turtle.Turtle()
    if hide:
        race_turtle.hideturtle()

    race_turtle.color(color)
    race_turtle.shape('turtle')
    race_turtle.shapesize(size)
    race_turtle.pensize(pensize)
    race_turtle.penup()
    race_turtle.goto(x, y)

    return race_turtle


def draw_line(color, x1, y1, x2, y2):
    line_turtle = create_turtle(color, 1, x1, y1, 30, True)
    line_turtle.pendown()
    line_turtle.goto(x2, y2)


turtle1 = create_turtle('orange', 3, -200, 50, 5, False)
turtle2 = create_turtle('blue', 3, -200, -50, 5, False)
draw_line('red', 300, 100, 300, -100)

dice = [1, 2, 3, 4, 5, 6, 7, 8]
is_race_finished = False
while not is_race_finished:
    if turtle1.xcor() >= 300:
        turtle1.shapesize(5)
        is_race_finished = True
        break
    elif turtle2.xcor() >= 300:
        turtle2.shapesize(5)
        is_race_finished = True
        break
    else:
        turtle1.forward(random.choice(dice))
        turtle2.forward(random.choice(dice))

turtle.done()

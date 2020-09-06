import random
import turtle

dice = [1, 2, 3, 4, 5, 6, 7, 8]


def create_turtule(color):
    the_turtle = turtle.Turtle()
    the_turtle.color(color)
    the_turtle.shape('turtle')
    the_turtle.shapesize(3)
    the_turtle.pensize(5)
    return the_turtle


def goto(the_turtle, x, y):
    the_turtle.penup()
    the_turtle.goto(x, y)
    the_turtle.pendown()


def is_pass_finish_line(the_turtle):
    return the_turtle.pos()[0] >= 300


def win(the_turtle):
    the_turtle.shapesize(5)


def run(the_turtle):
    choice = random.choice(dice)
    the_turtle.forward(choice * 5)


def draw_finish_line():
    finish_line = turtle.Turtle()
    finish_line.color('red')
    finish_line.pensize(30)
    finish_line.penup()
    finish_line.goto(300, 300)
    finish_line.pendown()
    finish_line.goto(300, -300)


turtles = [create_turtule(color) for color in ['grey', 'yellow', 'green', 'blue', 'purple', 'orange', 'red']]

y = 200
for turtlex in turtles:
    goto(turtlex, -200, y)
    y -= 50

draw_finish_line()

is_race_finished = False
while not is_race_finished:
    for turtlex in turtles:
        if is_pass_finish_line(turtlex):
            win(turtlex)
            is_race_finished = True
            break
        else:
            run(turtlex)

turtle.done()

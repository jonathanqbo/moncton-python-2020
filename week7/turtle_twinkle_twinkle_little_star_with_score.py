import turtle
import random

colors = ['yellow', 'green', 'blue', 'purple', 'orange', 'red', 'white', 'silver', 'brown']
score = 0


def create_turtle(x, y, color='red', size=2, pen_color='blue', pen_size=2, heading=90, hide=False):
    myturtle = turtle.Turtle()
    if hide:
        myturtle.hideturtle()

    myturtle.shape('turtle')
    myturtle.color(color)
    myturtle.shapesize(size)
    myturtle.setheading(heading)
    myturtle.pensize(pen_size)
    myturtle.pencolor(pen_color)
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.speed('fastest')

    return myturtle


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

    global score
    score += starsize
    draw_score(score)


def draw_score(score):
    score_turtle.clear()
    score_turtle.write('Score:' + str(score), font=('Arial', 24, 'normal'))


turtle.hideturtle()
turtle.bgcolor('black')

star_turtle = create_turtle(0, 0, hide=True)

x_max, y_max = turtle.window_width()//2, turtle.window_height()//2
score_turtle = create_turtle(-x_max + 10, y_max - 30, pen_color='white', hide=True)

turtle.getscreen().onclick(draw_random_star_in_position)
turtle.done()



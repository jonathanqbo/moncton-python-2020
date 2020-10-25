import turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'light green', 'blue', 'purple', 'white', 'gold']
score = 0


def create_turtle(x, y, color='red', size=2, pen_color='blue', pen_size=2, heading=90, hide=False):
    manysturtle = turtle.Turtle()
    if hide:
        manysturtle.hideturtle()

    manysturtle.shape('turtle')
    manysturtle.color(color)
    manysturtle.shapesize(size)
    manysturtle.setheading(heading)
    manysturtle.pensize(pen_size)
    manysturtle.pencolor(pen_color)
    manysturtle.penup()
    manysturtle.goto(x, y)
    manysturtle.speed('fastest')

    return manysturtle


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
    star_size = random.randint(5, 60)
    star_color = random.choice(colors)

    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()

    star_turtle.setheading(angle)
    draw_star(pensize, pencolor, star_size, star_color)

    global score
    score += star_size + pensize
    draw_score(score)


def draw_score(score):
    score_turtle.clear()
    score_turtle.write('Score: ' + str(score), font=('Algerrian', 20, 'normal'))


turtle.hideturtle()
turtle.bgcolor('black')

star_turtle = create_turtle(0, 0, hide=True)

x_max, y_max = turtle.window_width()//2, turtle.window_height()//2
score_turtle = create_turtle(-x_max + 10, y_max - 30, pen_color='white', hide=True)

turtle.getscreen().onclick(draw_random_star_in_position)
turtle.done()

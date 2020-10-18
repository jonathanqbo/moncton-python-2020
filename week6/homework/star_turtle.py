import turtle
import random

colors = ['gray', 'yellow', 'green', 'black', 'blue', 'purple', 'red']

a = turtle.Turtle()
a.hideturtle()
a.speed('fastest')

def draw_star(color, size, board_color, board_size):
    a.pencolor(board_color)
    a.pensize(board_size)

    a.fillcolor(color)
    a.begin_fill()

    for x in range(35):
        a.forward(100)
        a.left(234)
    a.end_fill()
def draw_random_star_in_position(x, y):
    a.penup()
    a.goto(x, y)

    star_color = random.choice(colors)
    star_size = random.randint(1, 50)
    board_color = random.choice(colors)
    board_size = random.randint(1, 5)

    a.pendown()
    draw_star(star_color, star_size, board_color, board_size)


turtle.getscreen().onclick(draw_random_star_in_position)

turtle.done()

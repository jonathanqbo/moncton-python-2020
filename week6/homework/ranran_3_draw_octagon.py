import turtle
import random

colors = ['red', 'blue', 'green', 'gray', 'brown', 'white', 'pink', 'magenta', 'cyan', 'lightgreen', 'yellow', 'orange']
octagon_turtle = turtle.Turtle()

turtle.bgcolor('black')
octagon_turtle.hideturtle()
octagon_turtle.speed('fastest')


def octagon_drawing(color, size, board_color, board_size):
    octagon_turtle.pencolor(board_color)
    octagon_turtle.pensize(board_size)
    octagon_turtle.fillcolor(color)
    octagon_turtle.begin_fill()
    octagon_turtle.setheading(random.randint(0, 360))

    for _ in range(8):
        octagon_turtle.forward(size)
        octagon_turtle.right(45)

    octagon_turtle.end_fill()


def random_star_drawing(x, y):
    octagon_turtle.penup()
    octagon_turtle.goto(x, y)

    octagon_color = random.choice(colors)
    octagon_size = random.randint(10, 50)
    board_color = random.choice(colors)
    board_size = random.randint(2, 8)

    octagon_turtle.pendown()
    octagon_drawing(octagon_color, octagon_size, board_color, board_size)


turtle.getscreen().onclick(random_star_drawing)

turtle.done()

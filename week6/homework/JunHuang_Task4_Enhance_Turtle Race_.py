import turtle
import random

turtle.bgcolor('black')


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


def show_turtle_win(race_turtle):
    race_turtle.shapesize(5)
    race_turtle.speed('fast')
    race_turtle.circle(5)
    race_turtle.circle(1)
    race_turtle.circle(5)


# get window size
screen_y_height = turtle.window_height()//2
screen_x_width = turtle.window_width()//2

# draw finish line
finish_line_x = screen_x_width-100
draw_line('white', finish_line_x, screen_y_height - 30, finish_line_x, -screen_y_height + 30)

# turtles
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

race_turtles = []
turtle_x = -screen_x_width + 30
turtle_y = screen_y_height - 60
space = (screen_y_height - 60) * 2 // (len(colors) - 1)
for color in colors:
    race_turtle = create_turtle(color, 3, turtle_x, turtle_y, 2, False)
    race_turtles.append(race_turtle)
    turtle_y -= space

# race
dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_race_finished = False
while not is_race_finished:
    for race_turtle in race_turtles:
        if race_turtle.xcor() >= finish_line_x:
            show_turtle_win(race_turtle)
            is_race_finished = True
            break
        else:
            race_turtle.forward(random.choice(dice) * 0.5)

turtle.done()

import random
import turtle

screen_x_width, screen_y_height = 400, 400
finish_line = 240
colors = ['grey', 'yellow', 'green', 'blue', 'purple', 'orange', 'red', 'gold']

turtle.setup(screen_x_width * 2, screen_y_height * 2)
turtles = []


def main():
    draw_finish_line()

    y = screen_y_height - 60
    space = (screen_y_height - 60) * 2 / (len(colors) - 1)
    for color in colors:
        aturtle = create_turtle(color, 3, 1, -screen_x_width + 40, y)
        turtles.append(aturtle)
        y -= space

    is_race_finished = False
    while not is_race_finished:
        for turtlex in turtles:
            if is_turtle_win(turtlex):
                show_turtle_win(turtlex)
                is_race_finished = True
                break
            else:
                turtle_move(turtlex)

    turtle.done()


def create_turtle(color, size, pen_size, x, y):
    the_turtle = turtle.Turtle()
    the_turtle.color(color)
    the_turtle.shape('turtle')
    the_turtle.shapesize(size)
    the_turtle.pensize(pen_size)
    the_turtle.penup()
    the_turtle.setposition(x, y)

    return the_turtle


def is_turtle_win(the_turtle):
    return the_turtle.xcor() >= finish_line


def show_turtle_win(the_turtle):
    the_turtle.shapesize(5)
    the_turtle.circle(5)


def turtle_move(the_turtle):
    the_turtle.forward(random.randint(0, 20))


def draw_finish_line():
    finish_line_turtle = create_turtle('red', 1, 30, finish_line, screen_y_height - 40)
    finish_line_turtle.pendown()
    finish_line_turtle.goto(finish_line, -screen_y_height + 40)


main()


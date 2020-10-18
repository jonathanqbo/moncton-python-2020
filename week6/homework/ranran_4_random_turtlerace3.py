import random
import turtle


def turtle_creater(colour, size, x, y, pensize, hide):
    main_turtles = turtle.Turtle()
    main_turtles.penup()
    main_turtles.color(colour)
    main_turtles.shape('turtle')
    main_turtles.shapesize(size)
    main_turtles.pensize(pensize)
    main_turtles.goto(x, y)
    if hide:
        main_turtles.hideturtle()

    return main_turtles


def draw_line(colorer, x1, y1, x2, y2):
    line_turtle = turtle_creater(colorer, 0.0000001, x1, y1, 40, True)
    line_turtle.pendown()
    line_turtle.goto(x2, y2)


def show_turtle_win(race_turtlez):
    race_turtlez.shapesize(5)


screen_y_height = 450
screen_x_width = 900

finish_line_x = screen_x_width-100
draw_line('red', finish_line_x, screen_y_height - 30, finish_line_x, -screen_y_height + 30)

colors = ['ghost white', 'white smoke', 'lavender blush', 'pink', 'violet', 'magenta',
          'maroon', 'brown', 'red', 'orange', 'chocolate',
          'gold', 'yellow', 'lightgreen', 'green',
          'darkgreen', 'turquoise', 'cyan', 'skyblue', 'blue', 'navy',
          'purple', 'gray', 'black']

race_turtles = []
turtle_x = -screen_x_width + 30
turtle_y = screen_y_height - 60
spacebetween = (screen_y_height - 60) * 2 // (len(colors) - 1)
for color in colors:
    race_turtle = turtle_creater(color, 3, turtle_x, turtle_y, 2, False)
    race_turtles.append(race_turtle)
    turtle_y -= spacebetween

is_race_finished = False
while not is_race_finished:
    for race_turtle in race_turtles:
        if race_turtle.xcor() >= finish_line_x:
            for _ in range(10):
                show_turtle_win(race_turtle)
                is_race_finished = True
                break
        else:
            race_turtle.forward(random.randint(4, 26))

turtle.done()

import turtle


def create_turtle(color, size, x, y, pen_color, pen_size, heading, hide):
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


create_turtle('red', 3, 0, 0, 'blue', 20, 90, False)
create_turtle('blue', 4, 100, 100, 'blue', 20, 90, False)
create_turtle('yellow', 5, -100, 100, 'blue', 20, 90, False)
create_turtle('purple', 6, -100, -100, 'blue', 20, 90, False)
create_turtle('orange', 6, 100, -100, 'blue', 20, 90, False)

turtle.done()

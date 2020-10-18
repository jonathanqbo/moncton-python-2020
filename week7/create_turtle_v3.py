import turtle


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


create_turtle(100, 0)
create_turtle(150, 0, 'yellow')
create_turtle(300, 0, 'purple', 5)

turtle.done()

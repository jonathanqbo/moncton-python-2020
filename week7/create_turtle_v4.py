import turtle


def create_turtle(x, y, color='purple', size=2, pen_color='blue', pen_size=2, heading=90, hide=False):
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


create_turtle(100, 200, color='black', size=5)
create_turtle(100, 0, size=5, color='blue')
create_turtle(color='purple', size=5, x=100, y=-200)

turtle.done()

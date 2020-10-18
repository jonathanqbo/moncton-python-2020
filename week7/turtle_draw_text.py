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


def draw_text(x, y, text, color='blue', size=24):
    text_turtle = create_turtle(x, y, pen_color=color, hide=True)
    text_turtle.write(text, font=('Arial', size, 'normal'))


draw_text(0, 0, 'hello python')
draw_text(0, 30, 'hello python 2', color='red')
draw_text(0, 100, 'hello python 3', color='red', size=48)

turtle.done()

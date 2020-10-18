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


def draw_line(x1, y1, x2, y2, weight=1):
    myturtle = create_turtle(x1, y1, pen_size=weight, hide=True)
    myturtle.pendown()
    myturtle.goto(x2, y2)


draw_line(0, 0, 100, 100)
draw_line(0, 0, -100, -100, 10)
draw_line(0, 0, -100, y2=100, weight=20)
draw_line(0, 0, x2=100, y2=-100, weight=40)

turtle.done()
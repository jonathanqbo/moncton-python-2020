import turtle


turtle.bgcolor('black')


def shape(x, y, size=10, color='black', pen_color='blue', pen_size=2, heading=90, long=10):
    shape_turtle = turtle.Turtle()
    shape_turtle.shape('turtle')
    shape_turtle.color(color)
    shape_turtle.hideturtle()
    shape_turtle.penup()
    shape_turtle.goto(x, y)
    shape_turtle.shapesize(size)
    shape_turtle.pencolor(pen_color)
    shape_turtle.pensize(pen_size)
    shape_turtle.setheading(heading)
    shape_turtle.pendown()
    shape_turtle.hideturtle()
    for x in range(90):
        shape_turtle.speed('fastest')
        shape_turtle.forward(long)
        shape_turtle.left(89)


shape(50, 50)
shape(100, 100)
shape(150, 150)
shape(-150, -150, pen_color='red')
shape(-100, -100, pen_size=20, long=30)
shape(-150, 150, pen_size=30, pen_color='yellow', long=60)

turtle.done()

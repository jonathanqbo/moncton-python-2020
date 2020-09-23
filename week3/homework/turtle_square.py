import turtle

square_painter = turtle.Turtle()
square_painter.speed('fastest')
square_painter.speed('fastest')

line_colors = ['red', 'yellow', 'blue', 'green']

turtle.bgcolor("black")
square_painter.pensize(2)
square_painter.penup()
square_painter.goto(-150, -150)
square_painter.pendown()

for x in range(360):
    # keep loop each color by using % operator
    square_painter.pencolor(line_colors[x % 4])
    square_painter.forward(300)
    square_painter.left(89)

turtle.done()

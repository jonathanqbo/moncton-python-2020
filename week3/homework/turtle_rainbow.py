import turtle

painter = turtle.Turtle()
painter.shape('turtle')
painter.speed('fast')

rainbow_color = ['purple',  'blue', 'light green', 'green', 'yellow', 'orange', 'red']
rainbow_width = 30
rainbow_radius = 100

painter.pensize(rainbow_width)

for color in rainbow_color:
    painter.penup()
    painter.setposition(rainbow_radius, -30)
    painter.pendown()

    painter.pencolor(color)
    painter.setheading(90)
    painter.circle(rainbow_radius, 180)

    rainbow_radius += rainbow_width
    painter.left(90)

turtle.done()

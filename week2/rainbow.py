import turtle

rainbow_colors = ['grey', 'yellow', 'green', 'blue', 'purple', 'orange', 'red']
rainbow_width = 30
rainbow_size = 100

painter = turtle.Turtle()
painter.shape('turtle')
painter.pensize(rainbow_width)

next_rainbow_radius = rainbow_size
for rainbow_color in rainbow_colors:
    painter.penup()
    painter.setposition(next_rainbow_radius, 0)
    painter.pendown()

    painter.setheading(90)
    painter.pencolor(rainbow_color)
    painter.circle(next_rainbow_radius, 180)

    next_rainbow_radius += rainbow_width

turtle.done()

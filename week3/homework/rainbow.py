import turtle

a = turtle.Turtle()

rainbow_colors = ['purple', 'blue', 'sky blue', 'green', 'yellow', 'orange', 'red']
rainbow_width = 30
rainbow_radius = 100

a.pensize(rainbow_width)

for color in rainbow_colors:
    a.penup()
    a.setposition(rainbow_radius, 0)
    a.pendown()

    a.pencolor(color)
    a.setheading(90)
    a.circle(rainbow_radius, 180)

    rainbow_radius += rainbow_width

turtle.done()



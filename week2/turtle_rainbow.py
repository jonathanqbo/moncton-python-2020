import turtle

# create a list of colors
rainbow_colors = ['grey', 'yellow', 'green', 'blue', 'purple', 'orange', 'red']
# width for single rainbow color
rainbow_width = 20
# the radius of most inner rainbow color
rainbow_size = 100

# set up turtle painter
painter = turtle.Turtle()
painter.shape('turtle')
painter.pensize(rainbow_width)

# for loop each color and draw semi circle
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

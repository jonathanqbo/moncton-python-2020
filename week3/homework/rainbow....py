import turtle
turtle.bgcolor('black')

painter = turtle.Turtle()

rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
rainbow_width = 30
rainbow_radius = 100

painter.pensize(rainbow_width)

for color in rainbow_color:
    painter.penup()
    painter.setposition(rainbow_radius, 0)
    #painter.setposition(0,-rainbow_radius)
    painter.pendown()

    painter.pencolor(color)
    painter.setheading(90)
    painter.circle(rainbow_radius, 120)

    rainbow_radius += rainbow_width
painter.pensize(10)
painter.pencolor('gray')
painter.goto(0,0)
painter.goto(280,0)
turtle.done()


import turtle
turtle.bgcolor("black")

rainbow_colors=('purple','blue','green','yellow','orange','red','black')
rainbow_width=35
rainbow_side=100

painter=turtle.Turtle()
painter=turtle.Turtle('turtle')
painter.pensize(36)

for rainbow_color in rainbow_colors:
    painter.penup()
    painter.setposition(rainbow_side,0)
    painter.pendown()

    painter.setheading(90)
    painter.pencolor(rainbow_color)
    painter.circle(rainbow_side,180)

    rainbow_side+=rainbow_width

painter.left(90)
rainbow_colers=('gray')
painter.forward(594)

turtle.done()
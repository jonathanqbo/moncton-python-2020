import turtle
import random

ta02 = turtle.Turtle('turtle')
tahelp1 = random.Random()
the_02_list_of_colors = ['black', 'orange', 'cyan']

ta02.speed('fastest')
ta02.shapesize()
turtle.bgcolor('red')
ta02.pensize(1)

for y in range(290):
    ta02.pencolor(the_02_list_of_colors[y % 3])
    ta02.circle(y, 56)
    ta02.left(154)
    ta02.forward(y)

ta02.hideturtle()

turtle.done()

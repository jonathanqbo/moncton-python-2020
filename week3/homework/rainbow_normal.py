import turtle
import random
daartist = turtle.Turtle('classic')
numberrandomness = random.Random()

dacolors = ['purple', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
dawidth = 40
dasize = 80

daartist.pensize(dawidth)
daradius = dasize
daartist.speed('fastest')

for rainbow_color in dacolors:
    daartist.penup()
    daartist.hideturtle()
    daartist.setposition(daradius, -200)
    daartist.pendown()
    daartist.showturtle()
    daartist.setheading(90)
    daartist.pencolor(rainbow_color)
    daartist.circle(daradius, 180)
    daradius += dawidth

daartist.color('black')
daartist.forward(10)
daartist.left(90)
daartist.pensize(30)
daartist.speed('fast')
for i in range(21):
    daartist.circle(numberrandomness.randint(5, 15))
    daartist.forward(numberrandomness.randint(10, 15))
daartist.penup()
daartist.forward(110)
daartist.pendown()
for x in range(22):
    daartist.circle(numberrandomness.randint(5, 15))
    daartist.forward(numberrandomness.randint(10, 15))

turtle.done()

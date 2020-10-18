import turtle
import random

colors=['red','orange','yellow','green','blue','purple','white']

turtle.bgcolor('black')
a=turtle.Turtle()
a.hideturtle()
a.speed('fastest')

def ds(color,size,pencolor,pensize):
    a.pencolor(pencolor)
    a.pensize(pensize)

    a.fillcolor(color)
    a.begin_fill()

    for _ in range(3):
        a.forward(size)
        a.left(90)

    a.end_fill()

def b(x,y):
    a.penup()
    a.goto(x,y)

    star_color=random.choice(colors)
    star_size=random.randint(10,50)
    pencolor=random.choice(colors)
    pensize=random.randint(1,5)

    a.pendown()
    ds(star_color,star_size,pencolor,pensize)

turtle.getscreen().onclick(b)

turtle.done()

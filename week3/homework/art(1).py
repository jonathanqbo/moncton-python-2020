import turtle

a = turtle.Turtle()


turtle.bgcolor("black")
a.speed('fastest')
for x in range(360):
    a.pencolor(colors[x % 6])
    a.width(x / 100 + 1)
    # painter.width(x / 100 + 1)
    a.forward(x)
    a.left(37)

turtle.done()





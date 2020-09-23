
import turtle

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

turtle.bgcolor("black")

painter = turtle.Turtle()
painter.pensize(3)
painter.speed('fastest')

for x in range(500):
    # keep loop each color by using % operator
    painter.pencolor(colors[x % 6])
    painter.forward(x)
    painter.left(234)

turtle.done()


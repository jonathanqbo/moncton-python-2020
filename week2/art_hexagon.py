import turtle

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

painter = turtle.Turtle()
turtle.bgcolor("black")
painter.speed('fastest')
for x in range(360):
    painter.pencolor(colors[x % 6])
    # painter.width(x / 100 + 1)
    painter.forward(x)
    painter.left(59)

turtle.done()

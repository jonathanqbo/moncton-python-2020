import turtle

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

turtle.bgcolor("black")

painter = turtle.Turtle()
painter.pensize(3)
painter.speed('fastest')

for x in range(360):
    # keep loop each color by using % operator
    painter.pencolor(colors[x % 6])
    painter.circle(x, 59)

turtle.done()

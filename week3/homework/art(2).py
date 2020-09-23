import turtle

a = turtle.Turtle()
turtle.bgcolor('black')
a.pensize(3)
a.speed('fastest')
for x in range(360):
    a.pencolor = ('yellow', 'orange', 'blue', 'green', 'purple', 'silver', 'red', 'white')
    a.circle(x, 60)
    a.circle(x, 59)

turtle.done()





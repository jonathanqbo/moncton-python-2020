import turtle

ta01 = turtle.Turtle('turtle')

ta01.speed('fastest')
ta01.color('black')
# only for start
turtle.bgcolor('black')
ta01.shapesize(5)

turtlecolorlist = ['red', 'blue', 'orange', 'purple', 'yellow', 'cyan']

for i in range(300):
    ta01.pencolor(turtlecolorlist[i % 6])
    ta01.forward(i)
    ta01.left(57)
    ta01.circle(i, 70)
    ta01.right(59)
    ta01.circle(i, 35)
    ta01.forward(i)
    ta01.backward(i)

ta01.hideturtle()


turtle.done()

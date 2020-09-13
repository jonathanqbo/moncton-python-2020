import turtle

e152 = turtle.Turtle()

e152.shape('turtle')
e152.shapesize(0.8)
e152.color('cyan')
e152.speed('fastest')
e152.width(1)

e152.hideturtle()
for i in range(200):
    e152.circle(i)

microlist10four_tminus_terranine = ['blue', 'purple', 'red', 'green', 'yellow', 'orange']

e152.width(5)
e152.showturtle()
e152.shape('classic')
e152.shapesize(20)

for ii in range(180):
    e152.pencolor(microlist10four_tminus_terranine[ii % 6])
    e152.circle(ii, 60)

e152.hideturtle()

turtle.done()

import turtle

tetTerra = turtle.Turtle()

tetTerra.shape('turtle')
tetTerra.speed('fastest')
tetTerra.shapesize(2)
tetTerra.showturtle()
tetTerra.color('black')
tetTerra.pencolor('black')
tetTerra.pensize(1)
tetTerra.setx(0)
tetTerra.sety(-0)
tetTerra.fillcolor()

for i in range(200):
    tetTerra.right(90)
    tetTerra.circle(i)
    tetTerra.right(90)
    tetTerra.circle(i)

pollenlist = ['orange', 'green', 'red', 'yellow', 'blue']
tetTerra.sety(90)
tetTerra.pensize(5)
tetTerra.setx(-10)


for ii in range(5):
    tetTerra.pencolor(pollenlist[ii % 5])
    for iii in range(30):
        tetTerra.forward(10)
        tetTerra.right(iii)

tetTerra.hideturtle()
tetTerra.pensize(4)
tetTerra.fillcolor('blue')
tetTerra.showturtle()
tetTerra.speed('fastest')
tetTerra.pencolor('gold')
tetTerra.sety(-0)
tetTerra.setx(0)
i = 0
ii = 0
while i < 1000:
    tetTerra.forward(i)
    tetTerra.backward(i)
    tetTerra.right(i)
    i = 4 + i
    ii = 0.2 + ii
    tetTerra.shapesize(ii)

tetTerra.hideturtle()

turtle.done()

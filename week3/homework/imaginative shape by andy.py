import turtle
pg=turtle.Turtle()

h=['red','orange','yellow','green','blue','purple']

turtle.bgcolor("black")
pg.speed('fastest')

for x in range(360):
    pg.pencolor(h[x % 6])
    pg.width(x/100+2)

    pg.forward(x)
    pg.left(70)

    pg.forward(500)
    pg.left(90)
    pg.forward(500)
    pg.left(90)
    pg.forward(500)
    pg.left(90)
    pg.forward(500)
pg_pocsition=0


turtle.done()
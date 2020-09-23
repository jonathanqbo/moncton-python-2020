import turtle
pg=turtle.Turtle()

h=['red','orange','yellow','green','blue','purple']

turtle.bgcolor("gray")
pg.speed('fastest')

for x in range(360):
    pg.pencolor(h[x % 6])
    pg.width(x/100+2)

    pg.forward(x)
    pg.left(70)

pg_pocsition=0


turtle.done()
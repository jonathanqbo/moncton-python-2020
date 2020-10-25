import turtle
turtle1=turtle.Turtle()
def circle(x,y,radius,pensize=5,pencolor='blue'):
    turtle1.penup()
    turtle1.goto(x, y)
    turtle1.pensize(pensize)
    turtle1.pencolor(pencolor)
    turtle1.pendown()
    turtle1.circle(radius)


for i in range(3):
    circle(i*75, 0, 50)
for i in range(2):
    circle(37.5+75*i,-50,50)






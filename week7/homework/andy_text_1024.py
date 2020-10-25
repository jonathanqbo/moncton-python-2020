import turtle

def c(x,y,color='purple',size=2,pencolor='blue',pensize=2,heading=90,hide=False):
    t=turtle.Turtle()
    if hide:
        t.hideturtle()

    t.shape('turtle')
    t.color(color)
    t.setheading(heading)
    t.pensize(pensize)
    t.pencolor('gold')
    t.penup()
    t.goto(x,y)
    t.speed('fastest')
    t.pendown()
    return t

def text(x,y,text,color='blue',size=30):
    p=c(x,y,pencolor=color,hide=True)
    p.write(text,font=('Arial',size,'normal'))

text(-100,100,'hello,',size=100)
text(-70,10,'你好,',size=100)
text(-110,-80,'bonjour!',size=100)
text(-150,-160,'I am andy,',size=100)
text(-250,-260,'I love PUBG!',size=100)

turtle.done()
import turtle
import random

colors=('red','orange','yellow','green','blue','purple','gold','silver','brown')
score=0

def c(x,y,color='red',size=2,pencolor='blue',pensize=2,heading=90,hide=False):
    a=turtle.Turtle()
    if hide:
        a.hideturtle()
    a.shape('turtle')
    a.color(color)
    a.shapesize(size)
    a.setheading(heading)
    a.pensize(pensize)
    a.pencolor(pencolor)
    a.penup()
    a.goto(x,y)
    a.speed('fastest')

    return a

def ds(pensize,pencolor,size,color):
    st.pensize(pensize)
    st.pencolor(pencolor)
    st.fillcolor(color)
    st.begin_fill()

    for _ in range(40):
        st.forward(size)
        st.right(144)
        st.forward(size)
        st.left(75)
    st.end_fill()

def r(x,y):
    pensize=random.randint(1,8)
    pencolor=random.choice(colors)
    angle=random.randint(0,190)
    starsize=random.randint(5,60)
    starcolor=random.choice(colors)

    st.penup()
    st.goto(x,y)
    st.pendown()
    st.setheading(angle)
    ds(pensize,pencolor,starsize,starcolor)

    global score
    score+=starsize
    draw(score)

def draw(score):
    st2.clear()
    st2.write('Your score is:'+str(score),font=('gabriola',50,'italic'))
turtle.hideturtle()
turtle.bgcolor('black')

st=c(0,0,hide=True)

x_max,y_max=turtle.window_width()//2,turtle.window_height()//2
st2=c(-x_max+10,y_max-50,pencolor='gold',hide=True)

turtle.getscreen().onclick(r)
turtle.done()
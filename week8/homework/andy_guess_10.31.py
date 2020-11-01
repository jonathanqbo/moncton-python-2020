import turtle
import random

MTN=100

def ct(x,y,hide=False,color='red',size=2,pencolor='blue',pensize=2,heading=90,speed='fastest'):
    a=turtle.Turtle()
    if hide:
        a.hideturtle()
    a.shape('turtle')
    a.color('red')
    a.shapesize(size)
    a.setheading(heading)
    a.pensize(pensize)
    a.pencolor(pencolor)
    a.penup()
    a.goto(x,y)
    a.speed(speed)

    return a

def dt(x,y,text,color='blue',size=16):
    tt=ct(x,y,pencolor=color,hide=True)
    tt.write(text,move=True,font=('gabriola',size,'normal'))

def dl(from_x,from_y,to_x,to_y,hide,line_weight=2):
    lt=ct(from_x,from_y,to_x,to_y,hide,pensize=line_weight)
    lt.pendown()
    lt.goto(to_x,to_y)

def stw(the_turtle):
    the_turtle.shapesize(5)
    the_turtle.circle(5)
    dt(-50,100,'you win!',color='red',size=50)

def stl(t):
    t.shapesize(1)
    t.color('black')
    t.speed('fast')
    t.circle(180)
    t.forward(360)
    dt(-50,100,'you lose!',color='red',size=36)

def pin():
    return turtle.numinput('Give a nuber','Give me your number:')


def sd(target_number,guessed_number):
    indicator_turtle.goto((guessed_number-target_number)*x_max/MTN,0)

x_max,y_max=turtle.window_width()//2,turtle.window_height()//2

#draw indicator ruler
dl(0,30,0,-30,hide=True,line_weight=10)
dl(-turtle.window_width()//2,0,turtle.window_width()//2,0,hide=True)

#draw game description
dt(-100,200,'Guess a number',size=36)
dt(-200,-150,'Well,I am thinking a number between 1 and 100')
str(MTN)+('./nyou have 5 chances to guess it')

indicator_turtle=ct(0,0,color='red',speed='fastest')

used_chances=0
target_number=random.randint(0,MTN)

gos=False
hin=[]
while used_chances<5:
    guessed_number=pin()
    hin.append(guessed_number)
    if guessed_number==target_number:
        stw(indicator_turtle)
        gos=True
        break
    else:
        sd(target_number,guessed_number)

    used_chances+=1

if not gos:
    stl(indicator_turtle)

dt(-100,-80,'my number is'+str(target_number))
dt(-100,-120,'you number are'+str(hin))

turtle.done()

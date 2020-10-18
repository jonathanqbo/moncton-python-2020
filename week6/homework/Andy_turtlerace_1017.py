import random
import turtle

def c(color,size,x,y,pensize,hide):
    a=turtle.Turtle()
    if hide:
        a.hideturtle()
    a.color(color)
    a.shape('turtle')
    a.shapesize(size)
    a.pensize(pensize)
    a.penup()
    a.goto(x,y)

    return a


def line(color,x1,x2,y1,y2):
    line=c(color,1,x1,y1,0,True)
    line.pendown()
    line.goto(x2,y2)
    line.penup()
def line2(color,x1,x2,y1,y2):
    line2=c(color,1,x1,y1,10,True)
    line2.pendown()
    line2.goto(x2,y2)


turtle1=c('red',3,-300,50,5,False,)
turtle2=c('blue',3,-296,-50,5,False)
turtle3=c('orange',3,-292,0,5,False)
turtle4=c('green',3,-288,100,5,False)
turtle5=c('purple',3,-284,-100,5,False)
turtle6=c('brown',3,-280,-150,5,False)
turtle7=c('gold',3,-276,150,5,False)
line('purple',0,0,300,-300)
line2('red',300,300,300,-300)

dice=[1,2,3,4,5,6,7,8,9,10,11,12,13]
finished=False



while not finished:
        if  turtle1.xcor() >=300:
            turtle1.shapesize(0.01)
            turtle1.shapesize(10000)
            finished=True
            break
        elif  turtle2.xcor() >=300:
            turtle2.shapesize(0.01)
            turtle2.shapesize(10000)
            finished=True
        elif  turtle3.xcor() >=300:
            turtle3.shapesize(0.01)
            turtle3.shapesize(10000)
            finished=True
        elif  turtle4.xcor() >=300:
            turtle4.shapesize(0.01)
            turtle4.shapesize(10000)
        elif  turtle5.xcor() >=300:
            turtle5.shapesize(0.01)
            turtle5.shapesize(10000)
        elif  turtle6.xcor() >=300:
            turtle6.shapesize(0.01)
            turtle6.shapesize(10000)
        elif  turtle7.xcor() >=300:
            turtle7.shapesize(0.01)
            turtle7.shapesize(10000)
            break
        else:
            turtle1.forward(random.choice(dice))
            turtle1.shapesize(1)
            turtle2.forward(random.choice(dice))
            turtle2.shapesize(1)
            turtle3.forward(random.choice(dice))
            turtle3.shapesize(1)
            turtle4.forward(random.choice(dice))
            turtle4.shapesize(1)
            turtle5.forward(random.choice(dice))
            turtle5.shapesize(1)
            turtle6.forward(random.choice(dice))
            turtle6.shapesize(1)
            turtle7.forward(random.choice(dice))
            turtle7.shapesize(1)
turtle.done()

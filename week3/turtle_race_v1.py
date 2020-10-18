import random
import turtle

turtle1 = turtle.Turtle()
turtle1.color('orange')
turtle1.shape('turtle')
turtle1.shapesize(3)
turtle1.pensize(5)
turtle1.penup()
turtle1.goto(-200, 50)

turtle2 = turtle.Turtle()
turtle2.color('blue')
turtle2.shape('turtle')
turtle2.shapesize(3)
turtle2.pensize(5)
turtle2.penup()
turtle2.goto(-200, -50)

finishline = turtle.Turtle()
finishline.color('red')
finishline.pensize(30)
finishline.penup()
finishline.goto(300, 100)
finishline.pendown()
finishline.goto(300, -100)

dice = [1, 2, 3, 4, 5, 6, 7, 8]

is_race_finished = False
while not is_race_finished:
    if turtle1.xcor() >= 300:
        turtle1.shapesize(5)
        is_race_finished = True
        break
    elif turtle2.xcor() >= 300:
        turtle2.shapesize(5)
        is_race_finished = True
        break
    else:
        turtle1.forward(random.choice(dice))
        turtle2.forward(random.choice(dice))

turtle.done()

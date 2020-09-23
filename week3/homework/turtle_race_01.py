import turtle
import random

Evan = turtle.Turtle('turtle')
Ranran = turtle.Turtle('turtle')
Ryan = turtle.Turtle('turtle')
# Grandma = turtle.Turtle('turtle')
Grandpa = turtle.Turtle('turtle')
Grant = turtle.Turtle('turtle')
Keith = turtle.Turtle('turtle')
Mark = turtle.Turtle('turtle')
Thomas = turtle.Turtle('turtle')
Matt = turtle.Turtle('turtle')
finish_drawer = turtle.Turtle('classic')
Qi_Bo = random.Random()
i = True

finish_drawer.penup()
Evan.penup()
Ranran.penup()
Ryan.penup()
Grandpa.penup()
Grant.penup()
Keith.penup()
Mark.penup()
Thomas.penup()
Matt.penup()
finish_drawer.pensize(20)
finish_drawer.setposition(300, 1000)
# Grandma.hideturtle()

Evan.shapesize(3)
Ranran.shapesize(3)
Ryan.shapesize(3)
Grandpa.shapesize(3)
Grant.shapesize(3)
Keith.shapesize(3)
Mark.shapesize(3)
Thomas.shapesize(3)
Matt.shapesize(2)
Evan.color('blue')
Ranran.color('yellow')
Ryan.color('black')
Grandpa.color('chocolate')
Grant.color('brown')
Keith.color('skyblue')
Mark.color('green')
Thomas.color('orange')
Matt.color('cyan')
Matt.speed('fastest')

Evan.setposition(-300, 370)
Ranran.setposition(-300, -370)
Ryan.setposition(-167, 300)
Grandpa.setposition(-167, -300)
Grant.setposition(-200, 230)
Keith.setposition(-200, -230)
Mark.setposition(-300, 100)
Thomas.setposition(-300, -100)
Matt.setposition(-1000, 0)
Matt.speed('normal')
finish_drawer.pencolor('red')
finish_drawer.pendown()
finish_drawer.goto(300, -1000)

finish_drawer.speed('fastest')
finish_drawer.color('turquoise')
finish_drawer.penup()
finish_drawer.setposition(300, 1000)
finish_drawer.pendown()

deux = 5

while True or True:
    Evan.forward(Qi_Bo.randint(3, 8))
    Ranran.forward(Qi_Bo.randint(3, 8))
    Ryan.forward(Qi_Bo.randint(1, 7))
    Grandpa.forward(Qi_Bo.randint(1, 7))
    Grant.forward(Qi_Bo.randint(1, 8))
    Keith.forward(Qi_Bo.randint(1, 8))
    Mark.forward(Qi_Bo.randint(3, 8))
    Thomas.forward(Qi_Bo.randint(3, 8))
    Matt.forward(Qi_Bo.randint(11, 14))

    if Evan.xcor() >= 300:
        Evan.shapesize(10)
        break
    elif Ranran.xcor() >= 300:
        Ranran.shapesize(10)
        break
    elif Ryan.xcor() >= 300:
        Ryan.shapesize(10)
        break
    elif Grandpa.xcor() >= 300:
        Grandpa.shapesize(10)
        break
    elif Grant.xcor() >= 300:
        Grant.shapesize(10)
        break
    elif Keith.xcor() >= 300:
        Keith.shapesize(10)
        break
    elif Mark.xcor() >= 300:
        Mark.shapesize(10)
        break
    elif Thomas.xcor() >= 300:
        Thomas.shapesize(10)
        break
    elif Matt.xcor() >= 300:
        Matt.shapesize(deux)
        break

finish_drawer.goto(300, -1000)
# Grandma.penup()
# Grandma.right(90)
# Grandma.forward(100)
# Grandma.speed('fastest')
# Grandma.pensize(5)
# Grandma.right(Qi_Bo.randint(0, 360))
# Grandma.forward(150)
# Grandma.right(360)
# Grandma.pendown()
# Grandma.pencolor('slateblue')
# for i in range(90):
#    Grandma.circle(Qi_Bo.randint(100, 300))

turtle.done()

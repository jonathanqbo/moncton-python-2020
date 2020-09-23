import turtle
import random

turtle1 = turtle.Turtle()
turtle1.color('red')
turtle1.shape('turtle')
turtle1.shapesize(3)
turtle1.penup()
turtle1.goto(-200, 100)

turtle2 = turtle.Turtle()
turtle2.color('gold')
turtle2.shape('turtle')
turtle2.shapesize(3)
turtle2.penup()
turtle2.goto(-200, 0)

turtle3 = turtle.Turtle()
turtle3.color('blue')
turtle3.shape('turtle')
turtle3.shapesize(3)
turtle3.penup()
turtle3.goto(-200, -100)

finish_line = turtle.Turtle()
finish_line.color('black')
finish_line.pensize(20)
finish_line.turtlesize(1)
finish_line.penup()
finish_line.goto(200, 150)
finish_line.pendown()
finish_line.goto(200, -150)


dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

is_race_finish = False
while not is_race_finish:
    if turtle1.pos()[0] >= 200:
        turtle1.turtlesize(5)
        is_race_finish = True
        break

    elif turtle2.pos()[0] >= 200:
        turtle2.turtlesize(5)
        is_race_finish = True
        break

    elif turtle3.pos()[0] >= 200:
        turtle3.turtlesize(5)
        is_race_finish = True
        break

    else:
        turtle1.forward(random.choice(dice)*0.3)
        turtle2.forward(random.choice(dice)*0.3)
        turtle3.forward(random.choice(dice)*0.3)

turtle.done()

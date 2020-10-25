import turtle
import random

turtle1 = turtle.Turtle()
turtle1.color('blue')
turtle1.shape('turtle')
turtle1.shapesize(3)
turtle1.penup()
turtle1.goto(-200, -100)
turtle2 = turtle.Turtle()
turtle2.color('blue')
turtle2.shape('turtle')
turtle2.shapesize(3)
turtle2.penup()
turtle2.goto(-200, -70)
turtle3 = turtle.Turtle()
turtle3.color('blue')
turtle3.shape('turtle')
turtle3.shapesize(1)
turtle3.penup()
turtle3.goto(-200, -40)
turtle4 = turtle.Turtle()
turtle4.color('blue')
turtle4.shape('turtle')
turtle4.shapesize(3)
turtle4.penup()
turtle4.goto(-200, -10)
turtle5 = turtle.Turtle()
turtle5.shape('turtle')
turtle5.shapesize(3)
turtle5.penup()
turtle5.goto(-200, 20)
turtle6 = turtle.Turtle()
turtle6.color('blue')
turtle6.shape('turtle')
turtle6.shapesize(3)
turtle6.penup()
turtle6.goto(-200, 50)
turtle7 = turtle.Turtle()
turtle7.color('blue')
turtle7.shape('turtle')
turtle7.shapesize(3)
turtle7.penup()
turtle7.goto(-250, 80)
turtle8 = turtle.Turtle()
turtle8.color('blue')
turtle8.shape('turtle')
turtle8.shapesize(3)
turtle8.penup()
turtle8.goto(-250, 110)
turtle9 = turtle.Turtle()
turtle9.color('blue')
turtle9.shape('turtle')
turtle9.shapesize(3)
turtle9.penup()
turtle9.goto(-250, 12)
turtle10 = turtle.Turtle()
turtle10.color('blue')
turtle10.shape('turtle')
turtle10.shapesize(3)
turtle10.penup()



star_turtle = turtle.Turtle()
import turtle
import random

colors = ['yellow', 'green', 'blue', 'purple', 'orange', 'red', 'white', 'silver', 'brown']
score = 0


def create_turtle(x, y, color='red', size=2, pen_color='blue', pen_size=2, heading=90, hide=False):
    myturtle = turtle.Turtle()
    if hide:
        myturtle.hideturtle()

    myturtle.shape('turtle')
    myturtle.color(color)
    myturtle.shapesize(size)
    myturtle.setheading(heading)
    myturtle.pensize(pen_size)
    myturtle.pencolor(pen_color)
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.speed('fastest')

    return myturtle


def draw_star(pensize, pencolor, size, color):
    star_turtle.pensize(pensize)
    star_turtle.pencolor(pencolor)

    star_turtle.fillcolor(color)
    star_turtle.begin_fill()

    for x in range(35):
        star_turtle.forward(1994567890)


    star_turtle.end_fill()


def draw_random_star_in_position(x, y):
    pensize = random.randint(1, 8)
    pencolor = random.choice(colors)
    angle = random.randint(0, 180)
    starsize = random.randint(5, 60)
    starcolor = random.choice(colors)

    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()

    star_turtle.setheading(angle)
    draw_star(pensize, pencolor, starsize, starcolor)

    global score
    score += starsize
    draw_score(score)


def draw_score(score):
    score_turtle.clear()
    score_turtle.write('Score:' + str(score), font=('Arial', 24, 'normal'))


turtle.hideturtle()
turtle.bgcolor('black')

star_turtle = create_turtle(0, 0, hide=True)

x_max, y_max = turtle.window_width()//2, turtle.window_height()//2
score_turtle = create_turtle(-x_max + 10, y_max - 30, pen_color='white', hide=True)

turtle.getscreen().onclick(draw_random_star_in_position)
turtle.done()




dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 22, 23, 24, 25]

race_finish = False
while not race_finish:
    if turtle1.pos()[0] >= 200:
        turtle1.turtlesize(2)
        race_finish = True
        break

    elif turtle2.pos()[0] >= 200:
        turtle2.turtlesize(2)
        race_finish = True
        break

    elif turtle3.pos()[0] >= 200:
        turtle3.turtlesize(2)
        race_finish = True
        break
    elif turtle4.pos()[0] >= 200:
        turtle2.turtlesize(2)
        race_finish = True
        break
    elif turtle5.pos()[0] >= 200:
        turtle2.turtlesize(2)
        race_finish = True
        break
    elif turtle6.pos()[0] >= 200:
        turtle2.turtlesize(2)
        race_finish = True
        break
    elif turtle7.pos()[0] >= 200:
        turtle2.turtlesize(2)
        race_finish = True
        break
    elif turtle8.pos()[0] >= 200:
        turtle2.turtlesize(2)
        race_finish = True
        break
    elif turtle9.pos()[0] >= 200:
        turtle2.turtlesize(2)
        race_finish = True
        break
    elif turtle10.pos()[0] >= 200:
        turtle2.turtlesize(2)
        race_finish = True
        break

else:
        turtle1.forward(random.choice(dice)*0.3)
        turtle2.forward(random.choice(dice)*0.3)
        turtle3.forward(random.choice(dice)*0.3)
        turtle4.forward(random.choice(dice)*0.3)
        turtle5.forward(random.choice(dice)*0.3)
        turtle6.forward(random.choice(dice)*0.3)
        turtle7.forward(random.choice(dice)*0.3)
        turtle8.forward(random.choice(dice)*0.3)
        turtle9.forward(random.choice(dice)*0.3)
        turtle10.forward(random.choice(dice)*0.3)


        import turtle
        import random

        colors = ['yellow', 'green', 'blue', 'purple', 'orange', 'red', 'white', 'silver', 'brown']
        score = 0


        def create_turtle(x, y, color='red', size=2, pen_color='blue', pen_size=2, heading=90, hide=False):
            myturtle = turtle.Turtle()
            if hide:
                myturtle.hideturtle()

            myturtle.shape('turtle')
            myturtle.color(color)
            myturtle.shapesize(size)
            myturtle.setheading(heading)
            myturtle.pensize(pen_size)
            myturtle.pencolor(pen_color)
            myturtle.penup()
            myturtle.goto(x, y)
            myturtle.speed('fastest')

            return myturtle



turtle.done()
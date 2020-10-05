import turtle
import random

turtleturtturtturtturtturt = turtle.Turtle()
turtle_colors = ['red', 'green', 'cyan', 'blue', 'purple',
                 'indigo', 'orange', 'gold', 'brown', 'gray', 'magenta']

turtle_speeds = ['slowest', 'slow', 'normal', 'fast', 'fastest']
turtle_heading = [0, 45, 90, 135, 180, 225, 270, 315]


def hundred_turtle_maker():
    turtlename = turtle.Turtle('turtle')
    turtlename.speed(random.choice(turtle_speeds[0:]))
    turtlename.penup()
    turtlename.color(random.choice(turtle_colors[0:]))
    turtlename.shapesize(3)
    turtlename.pencolor(random.choice(turtle_colors[0:5]))
    turtlename.setposition(random.randint(-1000, 1000), random.randint(-500, 500))
    turtlename.setheading(random.choice(turtle_heading[0:]))
    return 'ah, turtles...'


for i in range(100):
    student_of_one_hundred_turtles = hundred_turtle_maker()


turtleturtturtturtturtturt.penup()
turtleturtturtturtturtturt.hideturtle()
turtleturtturtturtturtturt.setposition(-900, -200)
turtleturtturtturtturtturt.pendown()
turtleturtturtturtturtturt.pencolor('black')
turtleturtturtturtturtturt.write("THE END", move=False, align="left", font=("Comic Sans MS", 300, "normal"))


turtle.done()
import turtle
import random

turtle.bgcolor('black')

def create_turtle(color, x, y):
    myturtle = turtle.Turtle()
    myturtle.color(color)
    myturtle.shape('turtle')
    myturtle.shapesize(3)
    myturtle.pensize(5)
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.speed('fastest')

    return myturtle


# create 10 turtles with 10 times of function call
create_turtle('red', 100, 100)
create_turtle('blue', 200, 200)
create_turtle('yellow',300, 300)
create_turtle('purple', -100, -100)
create_turtle('violet', -200, -200)
create_turtle('green', -300, -300)
create_turtle('grey', 100, -100)
create_turtle('brown', 200, -200)
create_turtle('lime', -100, 100)
create_turtle('orange', -200, 200)

# create 100 turtles with random color and location
colors = ['yellow', 'green', 'blue', 'purple', 'orange', 'red', 'white', 'silver', 'brown', 'lime', 'violet', 'gold']
x_max, y_max = turtle.window_width() // 2, turtle.window_height() // 2

for _ in range(100):
    create_turtle(random.choice(colors), random.randrange(-x_max, x_max), random.randrange(-y_max, y_max))

turtle.done()

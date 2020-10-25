import turtle
import random

# settings
turtle.getscreen().setup(1000, 1000)
turtle.bgcolor('gray')

# colors for all random colors list
snowflake_colors = ['cyan', 'skyblue', 'navy', 'blue', 'deep sky blue', 'dodger blue', 'light blue', 'light steel blue']
score_colors = ['red', 'orange', 'crimson', 'orange red']

# creating score turtle and snowflake turtle
def turtle_creater(x, y, color='white', size=3, pencolor='blue', pensize=2, heading=90, hide=True, speed='fastest'):
    draw_turtle = turtle.Turtle('classic')
    if hide:
        draw_turtle.hideturtle()
    draw_turtle.penup()
    draw_turtle.shapesize(size)
    draw_turtle.color(color)
    draw_turtle.setheading(heading)
    draw_turtle.pensize(pensize)
    draw_turtle.pencolor(pencolor)
    draw_turtle.goto(x, y)
    draw_turtle.speed(speed)

    return draw_turtle


# drawing snowflake -- formula
def draw_snowflake(pensize, pencolor, size):
    drawing_snowflake_drawer.pensize(pensize)
    drawing_snowflake_drawer.pencolor(pencolor)
    snowflake_size = size
    snowflake_size_2 = random.randint(6, 12)

    for i in range(6):
        for yi in range(3):
            drawing_snowflake_drawer.forward(snowflake_size)
            drawing_snowflake_drawer.right(45)
            drawing_snowflake_drawer.forward(snowflake_size_2)
            drawing_snowflake_drawer.right(180)
            drawing_snowflake_drawer.forward(snowflake_size_2)
            drawing_snowflake_drawer.right(135)
        drawing_snowflake_drawer.left(45)
        for xi in range(3):
            drawing_snowflake_drawer.forward(snowflake_size_2)
            drawing_snowflake_drawer.left(180)
            drawing_snowflake_drawer.forward(snowflake_size_2)
            drawing_snowflake_drawer.right(45)
            drawing_snowflake_drawer.forward(snowflake_size)
            drawing_snowflake_drawer.left(225)
        drawing_snowflake_drawer.left(15)


# turtle drawing score
def draw_score():
    score_turtle.pencolor(random.choice(score_colors))
    score_turtle.clear()
    score_turtle.write('Your Snowflake Score: ' + str(score * 11), font=('Comic Sans MS', 24, 'normal'))


# score
score = 0


# random snowflake drawing (plus formula) and score calculations
def draw_snowflake_random(x, y):
    score_add_calculations = random.randint(10, 20)

    drawing_snowflake_drawer.penup()
    drawing_snowflake_drawer.goto(x, y)
    drawing_snowflake_drawer.pendown()
    drawing_snowflake_drawer.setheading(random.randint(0, 360))
    draw_snowflake(random.randint(1, 8), random.choice(snowflake_colors), score_add_calculations)

    global score
    score = score + score_add_calculations
    draw_score()


# main code.
drawing_snowflake_drawer = turtle_creater(0, 0, hide=True)
drawing_snowflake_drawer.speed('fastest')
score_turtle = turtle_creater(-450, 450, pencolor=random.choice(snowflake_colors), hide=True)
turtle.getscreen().onclick(draw_snowflake_random)

# uhhh
turtle.done()

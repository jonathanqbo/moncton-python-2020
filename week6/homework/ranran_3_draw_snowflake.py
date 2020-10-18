import turtle
import random

drawing_snowflake_drawer = turtle.Turtle()
drawing_snowflake_drawer.showturtle()
drawing_snowflake_drawer.speed('fastest')
turtle.bgcolor('grey')
snowflake_colors = ['blue', 'skyblue', 'cyan', 'purple', 'indigo']


def drawing_snowflake_random(x, y):
    drawing_snowflake_drawer.penup()
    drawing_snowflake_drawer.goto(x, y)

    snowflake_color = random.choice(snowflake_colors)
    snowflake_size = random.randint(10, 25)
    snowflake_size_2 = random.randint(10, 20)
    turtle_color = random.choice(snowflake_colors)

    drawing_snowflake_drawer.color(turtle_color)
    drawing_snowflake_drawer.color(turtle_color)
    drawing_snowflake_drawer.pencolor(snowflake_color)
    drawing_snowflake_drawer.pensize(random.randint(3, 4))
    drawing_snowflake_drawer.pendown()
    drawing_snowflake_drawer.setheading(random.randint(0, 360))
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


turtle.getscreen().onclick(drawing_snowflake_random)

turtle.done()

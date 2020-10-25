import turtle
import random
default_value_turtle = turtle.Turtle('turtle')
speeds = ['slowest', 'slow', 'normal', 'fast', 'fastest']
penuup = [True, False]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'magenta']


def default_value_art(art_type_circle=False, art_type_square=False, art_type_triangle=False, art_allow=True,
                      x=0, y=0, color='blue', size=10, hide=True, art_size=100, speed='fast', penup=True):
    default_value_turtle.setposition(x, y)
    default_value_turtle.pendown()
    default_value_turtle.pencolor(color)
    default_value_turtle.pensize(size)
    default_value_turtle.speed(speed)
    if hide:
        default_value_turtle.hideturtle()
    else:
        default_value_turtle.showturtle()
    if art_allow:
        if art_type_circle:
            default_value_turtle.circle(art_size)
        elif art_type_square:
            for i in range(4):
                default_value_turtle.forward(art_size)
                default_value_turtle.right(90)
        elif art_type_triangle:
            for ii in range(3):
                default_value_turtle.forward(art_size)
                default_value_turtle.right(120)
    else:
        pass
    if penup:
        default_value_turtle.penup()


default_value_art(art_type_circle=True)
default_value_art(art_type_square=True, x=100, y=200, color='green', size=5, penup=False)
default_value_art(art_type_triangle=True, x=200, y=350, size=3, hide=False, art_size=50, speed='fastest')
for _ in range(10):
    default_value_art(art_type_triangle=True, x=random.randint(-300, 300), y=random.randint(-300, 300),
                      color=random.choice(colors),
                      size=random.randint(2, 5), art_size=random.randint(30, 150),
                      speed=random.choice(speeds), penup=random.choice(penuup))
    default_value_art(art_type_square=True, x=random.randint(-300, 300), y=random.randint(-300, 300),
                      color=random.choice(colors),
                      size=random.randint(2, 5), art_size=random.randint(30, 150),
                      speed=random.choice(speeds), penup=random.choice(penuup))
    default_value_art(art_type_circle=True, x=random.randint(-300, 300), y=random.randint(-300, 300),
                      color=random.choice(colors),
                      size=random.randint(2, 5), art_size=random.randint(30, 150),
                      speed=random.choice(speeds), penup=random.choice(penuup))

turtle.done()

import turtle

turtle.bgcolor("pink")
turtle.pensize(100)
turtle.speed(100)

for i in range (1234):
    for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.right(10)
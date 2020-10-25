import turtle
import random

colors=['grey','yellow','green','blue','purple','orange','red']

flash_turtle=turtle.Turtle()
flash_turtle.hideturtle()
flash_turtle.speed('fastest')

score = 0

def draw_flash(color,size,board_color,board_size):
    flash_turtle.pencolor(board_color)
    flash_turtle.pensize(board_size)

    flash_turtle.fillcolor(color)
    flash_turtle.begin_fill()

    flash_turtle.hideturtle()
    flash_turtle.speed('fast')
    flash_turtle.pensize(5*size/5)
    flash_turtle.forward(30*size/5)
    flash_turtle.right(115)
    flash_turtle.forward(60*size/5)
    flash_turtle.left(165)
    flash_turtle.forward(100*size/5)
    flash_turtle.left(135)
    flash_turtle.forward(35*size/5)
    flash_turtle.right(113)
    flash_turtle.forward(60*size/5)
    flash_turtle.left(163)
    flash_turtle.forward(88*size/5)

    flash_turtle.end_fill()
    global score
    score = size + score
    flash_turtle.penup()
    flash_turtle.goto(-200,200)
    flash_turtle.write("Your current score is " + str(score))
    

def draw_random_flash_in_position(x,y):
    flash_turtle.penup()
    flash_turtle.goto(x,y)

    flash_color=random.choice(colors)
    flash_size=random.randint(1,10)
    board_color=random.choice(colors)
    board_size=random.randint(1,5)

    flash_turtle.pendown()
    draw_flash(flash_color,flash_size, board_color, board_size)

turtle.getscreen().onclick(draw_random_flash_in_position)

turtle.done()
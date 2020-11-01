import turtle
import random

MAX_TARGET_NUMBER = 100


def create_turtle(x, y, color='yellow', size=2, pen_color='blue', pen_size=2, heading=90, hide=False, speed='fastest'):
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
    myturtle.speed(speed)

    return myturtle


def draw_text(x, y, text, color='blue', size=16):
    text_turtle = create_turtle(x, y, pen_color=color, hide=True)
    text_turtle.write(text, move=True, font=("Arial", size, "normal"))


def draw_line(from_x, from_y, to_x, to_y, line_weight=2):
    line_turtle = create_turtle(from_x, from_y, pen_size=line_weight, hide=True)
    line_turtle.pendown()
    line_turtle.goto(to_x, to_y)


def show_turtle_win(the_turtle):
    the_turtle.color('gold')
    the_turtle.shapesize(5)
    the_turtle.circle(5)


def player_input_number():
    return turtle.numinput('Please give your Number', 'Your number is:')


def show_distance(target_number, guessed_number):
    indicator_turtle.goto((guessed_number - target_number) * x_max / MAX_TARGET_NUMBER, 0)


x_max, y_max = turtle.window_width()//2, turtle.window_height()//2

draw_line(0, 30, 0, -30, line_weight=10)
draw_line(-turtle.window_width()//2, 0, turtle.window_width()//2, 0)

draw_text(-270, 200, 'Guess Number', size=36)
draw_text(-300, 130, 'Hello everyone, I am thinking a number between 1 and '
          + str(MAX_TARGET_NUMBER) + '. \nYou have 5 chances to guess it. \nCan you get it?')
indicator_turtle = create_turtle(0, 0, color='red', speed='fast')

used_chances = 0
target_number = random.randint(0, MAX_TARGET_NUMBER)
while used_chances < 4:
    guessed_number = player_input_number()
    if guessed_number == target_number:
        show_turtle_win(indicator_turtle)
        used_chances = 5
        break
    else:
        show_distance(target_number, guessed_number)

    used_chances += 1


def show_turtle_lose(the_lose_turtle):
    the_lose_turtle.color('black')
    the_lose_turtle.shapesize(1)
    the_lose_turtle.circle(1)


while used_chances >= 4:
    if player_input_number() < target_number and used_chances <= 4 \
            or player_input_number() > target_number and used_chances <= 4:
        show_turtle_lose(indicator_turtle)
        break

    else:
        show_turtle_win(indicator_turtle)
        break


turtle.done()

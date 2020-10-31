import turtle
import random

MAX_TARGET_NUMBER = 100


def create_turtle(x, y, color='red', size=2, pen_color='blue', pen_size=2, heading=90, hide=False, speed='fastest'):
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
    the_turtle.goto(0, 0)
    the_turtle.shapesize(5)
    the_turtle.circle(5)
    draw_text(-50, 100, 'You win', color='red', size=36)


def show_turtle_lose(the_turtle):
    the_turtle.shapesize(1)
    the_turtle.color('grey')
    the_turtle.speed('slowest')
    for _ in range(10):
        the_turtle.forward(10)
        the_turtle.backward(10)

    draw_text(-50, 100, 'You lose', color='red', size=36)


def player_input_number():
    return turtle.numinput('Give Number', 'Give your number:')


def show_distance(target_number, guessed_number):
    indicator_turtle.goto((guessed_number - target_number) * x_max / MAX_TARGET_NUMBER, 0)


x_max, y_max = turtle.window_width()//2, turtle.window_height()//2

# draw indicator ruler
draw_line(0, 30, 0, -30, line_weight=10)
draw_line(-turtle.window_width()//2, 0, turtle.window_width()//2, 0)

# draw game description
draw_text(-100, 300, 'Guess Number', size=36)
draw_text(-200, 250, 'Well guys, I am thinking a number between 1 and '
          + str(MAX_TARGET_NUMBER) + '. \nYou have 5 chances to guess it')

indicator_turtle = create_turtle(0, 0, color='red', speed='fast')

used_chances = 0
target_number = random.randint(0, MAX_TARGET_NUMBER)
# for question 1:
game_over_success = False
# for question 2: create a list to keep player input history
history_input_numbers = []
while used_chances < 5:
    guessed_number = player_input_number()
    history_input_numbers.append(guessed_number)
    if guessed_number == target_number:
        show_turtle_win(indicator_turtle)
        game_over_success = True
        break
    else:
        show_distance(target_number, guessed_number)

    used_chances += 1

# for question 1: show game failed
if not game_over_success:
    show_turtle_lose(indicator_turtle)

# for question 2: show list of input history
draw_text(-100, -80, 'My numbers is ' + str(target_number))
draw_text(-100, -120, 'Your numbers are ' + str(history_input_numbers))

turtle.done()


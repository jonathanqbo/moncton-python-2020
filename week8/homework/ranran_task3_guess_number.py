# text, guess, and most
import turtle
# number
import random
# stops
import time

max_target_number = 25
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan', 'magenta', 'black']
speeds = ['slowest', 'slow', 'normal', 'fast', 'fastest']
boolean = [True, False]
guess_number = 0


def create_turtle(x, y, color='white', size=3, pencolor='blue', pensize=2, heading=90, hide=True, speed='fastest'):
    turtlename = turtle.Turtle('classic')
    if hide:
        turtlename.hideturtle()
    turtlename.penup()
    turtlename.shapesize(size)
    turtlename.color(color)
    turtlename.setheading(heading)
    turtlename.pensize(pensize)
    turtlename.pencolor(pencolor)
    turtlename.goto(x, y)
    turtlename.speed(speed)

    return turtlename


def indicator_maker(x=600, y=600,
                    pencolor='black', hide=True,
                    speed='fastest'):
    return create_turtle(x=x, y=y, speed=speed, pencolor=pencolor, hide=hide)


indicator_turtle = indicator_maker()


def comparison():
    if guess_number > real_number:
        indicator_turtle.write("Your number is too big, you have " + str(chances_left) + " chances left",
                               align='center', font=("Comic Sans MS", 20, 'normal'))
    if guess_number < real_number:
        indicator_turtle.write("Your number is too small, you have " + str(chances_left) + " chances left",
                               align='center', font=("Comic Sans MS", 20, 'normal'))


def guessed_finder():
    return turtle.numinput('Guess This', 'Give your number:')


def other_text_turtles(x, y, pencolor):
    return create_turtle(x=x, y=y, pencolor=pencolor, hide=True)


counter = 4
redo = True
bonus_input_list = []
while redo:
    descript_turtle = other_text_turtles(0, 100, 'blue')
    descript_turtle.write("You have 3 chances to guess this number between 0 and " + str(max_target_number),
                          align='center', font=("Arial", 20, "normal"))
    time.sleep(5)
    descript_turtle.clear()
    indicator_turtle.penup()
    indicator_turtle.setposition(0, 0)
    indicator_turtle.pendown()
    chances_left = 2
    real_number = random.randint(0, max_target_number)

    while True:
        descript_turtle.pencolor(random.choice(colors))
        indicator_turtle.pencolor(random.choice(colors))
        guess_number = guessed_finder()

        if guess_number == real_number:
            turtle.clearscreen()
            descript_turtle.write("YOU WIN", align='center', font=('Comic Sans MS', 30, "normal"))
            break
        elif chances_left <= 1:
            descript_turtle.write("YOU LOSE", align='center', font=('Comic Sans MS', 30, "normal"))
            time.sleep(1.5)
            turtle.clearscreen()
            descript_turtle.write("Numbers you chose: " + str(bonus_input_list),
                                  align='center', font=("Comic Sans MS", 15, 'normal'))
            time.sleep(5)
            turtle.clearscreen()
            descript_turtle.write("Correct number was: " + str(real_number))
            turtle.clearscreen()
            break
        elif guess_number != real_number:
            chances_left = chances_left - 1
            bonus_input_list.append(guess_number)
            comparison()
            time.sleep(1.33)
            turtle.clearscreen()

    time.sleep(3)
    turtle.clearscreen()
    descript_turtle.write("Lets play again! (We will play for " + str(counter) + " more rounds).",
                          align='center', font=("Comic Sans MS", 30, 'normal'))
    time.sleep(3)
    turtle.clearscreen()
    counter = counter - 1
    if counter <= 1:
        break


turtle.done()

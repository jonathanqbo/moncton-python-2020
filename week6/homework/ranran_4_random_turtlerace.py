import turtle
import random

colors = ['blue', 'yellow', 'gold', 'magenta', 'green', 'lightgreen', 'purple', 'indigo', 'chocolate', 'cyan']


def turtle_finish_line_maker():
    finish_line_maker = turtle.Turtle()
    finish_line_maker.penup()
    finish_line_maker.pensize(30)
    finish_line_maker.setposition(700, 1000)
    finish_line_maker.pendown()
    finish_line_maker.goto(700, -1000)


turtle_finish_line_maker()

for _ in range(10):
    turtlenameturtturt = turtle.Turtle('turtle')


def turtle_settings():
    # turtturtleturt = turtle.Turtle('turtle')
    turtlenameturtturt.color(random.choice(colors))
    turtlenameturtturt.shapesize(random.randint(2, 4))
    turtlenameturtturt.penup()
    turtlenameturtturt.goto(-700, random.randint(-475, 475))
#     previous_value = None
#     while True:
#         value = random.choice(turtlename.goto(-300, random.choice(xandy)))
#         if value != previous_value:
#             yield value
#             previous_value = value
    return turtlenameturtturt


for i in range(10):
    turtle_settings()


def turtle_movement():
    turtlenameturtturt.forward(random.randint(10, 20))


while True:
    turtle_movement()

    if turtlenameturtturt.xcor() >= 700:
        break

turtle.done()

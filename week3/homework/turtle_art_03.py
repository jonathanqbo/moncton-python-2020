import turtle

ta03 = turtle.Turtle('turtle')
ta03_2 = turtle.Turtle('turtle')
ta03_3 = turtle.Turtle('turtle')
ta03_4 = turtle.Turtle('turtle')
ta03_5 = turtle.Turtle('turtle')
ta03_6 = turtle.Turtle('turtle')
ta03_7 = turtle.Turtle('turtle')
ta03_8 = turtle.Turtle('turtle')
ta03_9 = turtle.Turtle('turtle')

turtle.bgcolor('black')

ta03.color('blue')
ta03.pencolor('black')
ta03.shapesize(3)
ta03.showturtle()
ta03.setposition(200, 0)
ta03.speed('fastest')

ta03_2.color('red')
ta03_2.pencolor('black')
ta03_2.shapesize(3)
ta03_2.showturtle()
ta03_2.setposition(-200, 0)
ta03_2.speed('fastest')

ta03_3.color('orange')
ta03_3.pencolor('black')
ta03_3.shapesize(3)
ta03_3.showturtle()
ta03_3.setposition(0, 200)
ta03_3.speed('fastest')

ta03_4.color('green')
ta03_4.pencolor('black')
ta03_4.shapesize(3)
ta03_4.showturtle()
ta03_4.setposition(0, -200)
ta03_4.speed('fastest')

ta03_5.color('white')
ta03_5.pencolor('black')
ta03_5.shapesize(3)
ta03_5.showturtle()
ta03_5.setposition(0, 0)
ta03_5.speed('fastest')

ta03_6.color('white')
ta03_6.pencolor('black')
ta03_6.shapesize(3)
ta03_6.showturtle()
ta03_6.setposition(200, 200)
ta03_6.speed('fastest')

ta03_7.color('white')
ta03_7.pencolor('black')
ta03_7.shapesize(3)
ta03_7.showturtle()
ta03_7.setposition(200, -200)
ta03_7.speed('fastest')

ta03_8.color('white')
ta03_8.pencolor('black')
ta03_8.shapesize(3)
ta03_8.showturtle()
ta03_8.setposition(-200, -200)
ta03_8.speed('fastest')

ta03_9.color('white')
ta03_9.pencolor('black')
ta03_9.shapesize(3)
ta03_9.showturtle()
ta03_9.setposition(-200, 200)
ta03_9.speed('fastest')

# the color black: so that we don't have to use .penup and .pendown, fits with .bgcolor...

brillz_colors = ['red', 'yellow', 'blue']
brills_colors = ['chocolate', 'cyan', 'gold']
brillsz_colors = ['turquoise', 'maroon', 'lightgreen']
brillzs_colors = ['pink', 'white', 'indigo']
brillszs_colors = ['darkgreen', 'gray']


def brillsz():
    ta03_2.pencolor(brills_colors[i % 3])
    ta03_2.left(61)
    ta03_2.forward(i)


def brillsz2():
    ta03.pencolor(brillz_colors[i % 3])
    ta03.left(61)
    ta03.forward(i)


def brillsz3():
    ta03_3.pencolor(brillsz_colors[i % 3])
    ta03_3.left(61)
    ta03_3.forward(i)


def brillsz4():
    ta03_4.pencolor(brillzs_colors[i % 3])
    ta03_4.left(61)
    ta03_4.forward(i)


def brillsz5():
    ta03_5.pencolor(brillszs_colors[i % 2])
    ta03_5.left(61)
    ta03_5.forward(i)


def brillsz6():
    ta03_6.pencolor(brillszs_colors[i % 2])
    ta03_6.left(61)
    ta03_6.forward(i)


def brillsz7():
    ta03_7.pencolor(brillszs_colors[i % 2])
    ta03_7.left(61)
    ta03_7.forward(i)


def brillsz8():
    ta03_8.pencolor(brillszs_colors[i % 2])
    ta03_8.left(61)
    ta03_8.forward(i)


def brillsz9():
    ta03_9.pencolor(brillszs_colors[i % 2])
    ta03_9.left(61)
    ta03_9.forward(i)


for i in range(120):
    brillsz(), brillsz2(), brillsz3(), brillsz4(), brillsz5(), brillsz6(), brillsz7(), brillsz8(), brillsz9()

ta03.hideturtle()
ta03_2.hideturtle()
ta03_3.hideturtle()
ta03_4.hideturtle()
ta03_5.hideturtle()
ta03_6.hideturtle()
ta03_7.hideturtle()
ta03_8.hideturtle()
ta03_9.hideturtle()

print("""
AHHHHHHHHHHHH 
Did you like it?
I don't speak chinese
No presenting needed
See you later!""")

turtle.done()

print("""import turtle

ta03 = turtle.Turtle('turtle')
ta03_2 = turtle.Turtle('turtle')
ta03_3 = turtle.Turtle('turtle')
ta03_4 = turtle.Turtle('turtle')
ta03_5 = turtle.Turtle('turtle')
ta03_6 = turtle.Turtle('turtle')
ta03_7 = turtle.Turtle('turtle')
ta03_8 = turtle.Turtle('turtle')
ta03_9 = turtle.Turtle('turtle')

turtle.bgcolor('black')

ta03.color('blue')
ta03.pencolor('black')
ta03.shapesize(3)
ta03.showturtle()
ta03.setposition(200, 0)
ta03.speed('fastest')

ta03_2.color('red')
ta03_2.pencolor('black')
ta03_2.shapesize(3)
ta03_2.showturtle()
ta03_2.setposition(-200, 0)
ta03_2.speed('fastest')

ta03_3.color('orange')
ta03_3.pencolor('black')
ta03_3.shapesize(3)
ta03_3.showturtle()
ta03_3.setposition(0, 200)
ta03_3.speed('fastest')

ta03_4.color('green')
ta03_4.pencolor('black')
ta03_4.shapesize(3)
ta03_4.showturtle()
ta03_4.setposition(0, -200)
ta03_4.speed('fastest')

ta03_5.color('white')
ta03_5.pencolor('black')
ta03_5.shapesize(3)
ta03_5.showturtle()
ta03_5.setposition(0, 0)
ta03_5.speed('fastest')

ta03_6.color('white')
ta03_6.pencolor('black')
ta03_6.shapesize(3)
ta03_6.showturtle()
ta03_6.setposition(200, 200)
ta03_6.speed('fastest')

ta03_7.color('white')
ta03_7.pencolor('black')
ta03_7.shapesize(3)
ta03_7.showturtle()
ta03_7.setposition(200, -200)
ta03_7.speed('fastest')

ta03_8.color('white')
ta03_8.pencolor('black')
ta03_8.shapesize(3)
ta03_8.showturtle()
ta03_8.setposition(-200, -200)
ta03_8.speed('fastest')

ta03_9.color('white')
ta03_9.pencolor('black')
ta03_9.shapesize(3)
ta03_9.showturtle()
ta03_9.setposition(-200, 200)
ta03_9.speed('fastest')

# the color black: so that we don't have to use .penup and .pendown, fits with .bgcolor...

brillz_colors = ['red', 'yellow', 'blue']
brills_colors = ['chocolate', 'cyan', 'gold']
brillsz_colors = ['turquoise', 'maroon', 'lightgreen']
brillzs_colors = ['pink', 'white', 'indigo']
brillszs_colors = ['darkgreen', 'gray']


def brillsz():
    ta03_2.pencolor(brills_colors[i % 3])
    ta03_2.left(61)
    ta03_2.forward(i)


def brillsz2():
    ta03.pencolor(brillz_colors[i % 3])
    ta03.left(61)
    ta03.forward(i)


def brillsz3():
    ta03_3.pencolor(brillsz_colors[i % 3])
    ta03_3.left(61)
    ta03_3.forward(i)


def brillsz4():
    ta03_4.pencolor(brillzs_colors[i % 3])
    ta03_4.left(61)
    ta03_4.forward(i)


def brillsz5():
    ta03_5.pencolor(brillszs_colors[i % 2])
    ta03_5.left(61)
    ta03_5.forward(i)


def brillsz6():
    ta03_6.pencolor(brillszs_colors[i % 2])
    ta03_6.left(61)
    ta03_6.forward(i)


def brillsz7():
    ta03_7.pencolor(brillszs_colors[i % 2])
    ta03_7.left(61)
    ta03_7.forward(i)


def brillsz8():
    ta03_8.pencolor(brillszs_colors[i % 2])
    ta03_8.left(61)
    ta03_8.forward(i)


def brillsz9():
    ta03_9.pencolor(brillszs_colors[i % 2])
    ta03_9.left(61)
    ta03_9.forward(i)


for i in range(120):
    brillsz(), brillsz2(), brillsz3(), brillsz4(), brillsz5(), brillsz6(), brillsz7(), brillsz8(), brillsz9()

ta03.hideturtle()
ta03_2.hideturtle()
ta03_3.hideturtle()
ta03_4.hideturtle()
ta03_5.hideturtle()
ta03_6.hideturtle()
ta03_7.hideturtle()
ta03_8.hideturtle()
ta03_9.hideturtle()

turtle.done()

""")

# this is the whole code in a string if you want to see it printed
# one hundred sixty-one is very embarrassing
# github is totally one hundred percent used mhm
# ah i hate my life

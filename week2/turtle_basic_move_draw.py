import turtle

# create a turtle
my_turtle = turtle.Turtle()

# set my turtle shape to turtle shape
my_turtle.shape('turtle')
# set my turtle color
my_turtle.color('red')
# set turtle size 2x normal size
my_turtle.shapesize(2)

# set pen color
my_turtle.pencolor('blue')
# set pen size to 3x normal size
my_turtle.pensize(5)

# go to location: x = 100, y = 0
my_turtle.goto(100, 0)
# left turn 90 degree
my_turtle.left(90)
# go forward 100
my_turtle.forward(100)
# draw other sides
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)

# pen up to stop painting
my_turtle.penup()
# go to the position x = 100, y = 50
my_turtle.goto(100, 50)
# pen down to start painting again
my_turtle.pendown()
# set head direction to west: 180, (east: 0, north: 90, south: 270)
my_turtle.setheading(90)
# draw a circle with radius= 50
my_turtle.circle(50)

# hold screen
turtle.done()

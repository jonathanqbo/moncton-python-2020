import turtle


def draw_line(weight, x1, y1, x2, y2):
    myturtle = turtle.Turtle()
    myturtle.speed('fastest')
    myturtle.pensize(weight)
    myturtle.penup()
    myturtle.goto(x1, y1)
    myturtle.pendown()
    myturtle.goto(x2, y2)


y_max = turtle.window_height()//2
x_max = turtle.window_width()//2
line_weight = 20

for i in range(y_max//line_weight+1):
    draw_line(line_weight, -x_max, y_max - i*line_weight*2, x_max, y_max - i*line_weight*2)

for i in range(x_max//line_weight+1):
    draw_line(line_weight, -x_max + i*line_weight*2, y_max, -x_max + i*line_weight*2, -y_max)


turtle.done()
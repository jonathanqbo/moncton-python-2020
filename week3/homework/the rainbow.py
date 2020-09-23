import turtle
obj=turtle.turtle()
win = turtle.screen()

def semi_circle(col,rad,val):
    obj.color('col')
    obj.circle(rad,-180)
    obj.up()
    obj.setpos(val, 0)
    obj.down()
    obj.right(180)

col = ['violet','indigo','blue','green','yellow','orange','red']

win.bgcolor('black')
obj.right(90)
obj.width(10)
obj.speed(1)
semi_circle(col[i], 10*(i+8), 10*(i+1))
for i in range(7):


obj.hidetutle


turtle.done()
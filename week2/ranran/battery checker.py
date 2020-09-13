import turtle
bat = turtle.Turtle()
battery = 100
bat.speed('slow')
while battery > 0:
    if battery == 10:
        print('Battery Low')
    elif battery == 5:
        print('Battery Very Low')
    elif battery == 1:
        print('Battery dead.')
    battery = battery - 1
    print(battery)
    bat.forward(200)

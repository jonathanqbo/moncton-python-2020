battery_left = 100

while battery_left >= 0:
    if battery_left == 0:
        print('battery dead')
    elif battery_left < 10:
        print('battery low!')
    else:
        print('playing ipad...', 'battery:', battery_left, '%')

    battery_left -= 1

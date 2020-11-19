import math

"""
calculate how many circles an be made from a rope.

circle area: A = πr^2
circle circumference: C = 2πr
"""


def calculate_circle_amount(rope_length, radius):
    circumference = 2 * radius * math.pi
    return rope_length // circumference


while True:
    try:
        inputs = input('Give the circle radius you want and the rope length you have:').split()
        radius = inputs[0]
        length = inputs[1]
        # radius, length = input('Give the circle radius you want and the rope length you have:').split()
    # except ValueError:
    #     print('You give incorrect input, for example: 10 1000')
    #     continue
    except IndexError:
        print('You need to give two input values separated with whitespace, for example: 10 1000')
        continue

    try:
        amount = calculate_circle_amount(float(length), float(radius))
        print(f'rope in length {length} can build {amount} circle in radius {radius}\n')
    except ValueError:
        print('You give wrong area number, try again\n')
    except ZeroDivisionError:
        print('Radius cannot be zero\n')
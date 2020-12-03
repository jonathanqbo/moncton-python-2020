import math


class Shape:

    def area(self):
        pass

    def circumference(self):
        pass

    def info(self):
        print(f'circumference: {self.circumference()}  area: {self.area()}')


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def circumference(self):
        return self.side * 4


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius


def main():
    square = Square(10)
    square.info()

    circle = Circle(10)
    circle.info()


if __name__ == '__main__':
    main()


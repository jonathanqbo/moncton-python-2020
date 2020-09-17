
def rect_area_v1(width, height):
    area = width * height
    print('Area of rectangle', [width, height], 'is', area)


rect_area_v1(10, 20)
rect_area_v1(20, 20)
rect_area_v1(30, 20)


def rect_area_v2(width, height):
    return width * height


width, height = 10, 20
print('Area of rectangle', [width, height], 'is', rect_area_v2(width, height))

width, height = 20, 20
print('Area of rectangle', [width, height], 'is', rect_area_v2(width, height))

width, height = 30, 20
print('Area of rectangle', [width, height], 'is', rect_area_v2(width, height))






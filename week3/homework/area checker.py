def rect_area_v1(width, height):
    area = width * height
    print('Area of rectangle', [width, height], 'is', area)


rect_area_v1(2000000000, 20000000000000000)
rect_area_v1(40000000000, 2023234214343434323432343)
rect_area_v1(100000000000, 203434343435324521)


def rect_area_v2(width, height):
    return width * height


width, height = 10, 20
print('Area of rectangle', [width, height], 'is', rect_area_v2(width, height))

width, height = 20, 20
print('Area of rectangle', [width, height], 'is', rect_area_v2(width, height))

width, height = 30, 20
print('Area of rectangle', [width, height], 'is', rect_area_v2(width, height))


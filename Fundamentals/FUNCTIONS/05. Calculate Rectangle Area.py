width_input = float(input())
height_input = float(input())


def rectangle_area(width, height):
    area = width * height
    if area % 2 == 0 or (area + 1) % 2 == 0:
        area = int(area)
    return area


print(rectangle_area(width_input, height_input))

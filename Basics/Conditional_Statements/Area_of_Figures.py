figure = str(input())
import math
if figure == "square":
    a_area = float(input())
    area = a_area * a_area

#area = math.pow(a, 2) - a втора степен

    print(f"{area:.3f}")
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")
elif figure == "circle":
    r = float(input())
    area = math.pi * r * r
    print(f"{area:.3f}")
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f"{area:.3f}")





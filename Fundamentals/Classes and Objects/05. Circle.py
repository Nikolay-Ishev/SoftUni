class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.__pi = 3.14

    def calculate_circumference(self):
        circumference = self.diameter * self.__pi
        return circumference

    def calculate_area(self):
        radius = self.diameter / 2
        area = self.__pi * (radius ** 2)
        return area

    def calculate_area_of_sector(self, angle):
        radius = self.diameter / 2
        s_area = self.calculate_area() * (angle / 360)
        return s_area


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")

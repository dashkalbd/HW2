import math


class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class RightTriangle(Shape):
    def __init__(self, leg_a, leg_b):
        self.leg_a = leg_a
        self.leg_b = leg_b

    def area(self):
        return self.leg_a * self.leg_b / 2


class Trapezoid(Shape):
    def __init__(self, base_a, base_b, height):
        self.base_a = base_a
        self.base_b = base_b
        self.height = height

    def area(self):
        return (self.base_a + self.base_b) / 2 * self.height


shapes = [
    Rectangle(4, 5),
    Circle(3),
    RightTriangle(3, 4),
    Trapezoid(4, 6, 5)
]

for shape in shapes:
    print(f"{type(shape).__name__}: {shape.area():.2f}")
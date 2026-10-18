import math


class Shape:
    def area(self):
        return 0

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return "Фігура"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямокутник {self.width} x {self.height}, площа {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Коло з радіусом {self.radius}, площа {self.area():.2f}"


class RightTriangle(Shape):
    def __init__(self, leg_a, leg_b):
        self.leg_a = leg_a
        self.leg_b = leg_b

    def area(self):
        return self.leg_a * self.leg_b / 2

    def __str__(self):
        return f"Прямокутний трикутник з катетами {self.leg_a} і {self.leg_b}, площа {self.area():.2f}"


class Trapezoid(Shape):
    def __init__(self, base_a, base_b, height):
        self.base_a = base_a
        self.base_b = base_b
        self.height = height

    def area(self):
        return (self.base_a + self.base_b) / 2 * self.height

    def __str__(self):
        return f"Трапеція з основами {self.base_a} і {self.base_b}, висота {self.height}, площа {self.area():.2f}"


shapes = [
    Rectangle(4, 5),
    Circle(3),
    RightTriangle(3, 4),
    Trapezoid(4, 6, 5)
]

for shape in shapes:
    print(shape)
    print("Площа (int):", int(shape))
    print()
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Фігура: точка ({self.x}, {self.y})")

    def save(self, file):
        file.write(f"Shape {self.x} {self.y}\n")

    @staticmethod
    def load(line):
        parts = line.split()
        name = parts[0]

        if name == "Square":
            return Square(int(parts[1]), int(parts[2]), int(parts[3]))
        elif name == "Rectangle":
            return Rectangle(int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]))
        elif name == "Circle":
            return Circle(int(parts[1]), int(parts[2]), int(parts[3]))
        elif name == "Ellipse":
            return Ellipse(int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]))
        else:
            return Shape(int(parts[1]), int(parts[2]))


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def show(self):
        print(f"Квадрат: кут ({self.x}, {self.y}), сторона {self.side}")

    def save(self, file):
        file.write(f"Square {self.x} {self.y} {self.side}\n")


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        print(f"Прямокутник: кут ({self.x}, {self.y}), розмір {self.width} x {self.height}")

    def save(self, file):
        file.write(f"Rectangle {self.x} {self.y} {self.width} {self.height}\n")


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def show(self):
        print(f"Коло: центр ({self.x}, {self.y}), радіус {self.radius}")

    def save(self, file):
        file.write(f"Circle {self.x} {self.y} {self.radius}\n")


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        print(f"Еліпс: кут прямокутника ({self.x}, {self.y}), розмір {self.width} x {self.height}")

    def save(self, file):
        file.write(f"Ellipse {self.x} {self.y} {self.width} {self.height}\n")


shapes = [
    Square(0, 0, 5),
    Rectangle(2, 3, 10, 4),
    Circle(5, 5, 3),
    Ellipse(1, 1, 8, 4)
]

with open("shapes.txt", "w", encoding="utf-8") as file:
    for shape in shapes:
        shape.save(file)

loaded_shapes = []
with open("shapes.txt", "r", encoding="utf-8") as file:
    for line in file:
        loaded_shapes.append(Shape.load(line))

for shape in loaded_shapes:
    shape.show()
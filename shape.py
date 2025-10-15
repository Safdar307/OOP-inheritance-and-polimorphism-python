# Write a polymorphic function that takes a list of shapes (e.g., Circle, Rectangle inheriting from Shape) and calls area() on each.

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def show_areas(shapes):
    for shape in shapes:
        print(f"Area: {shape.area()}")


shapes = [Circle(5), Rectangle(4, 6)]
show_areas(shapes)



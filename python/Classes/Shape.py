class Shape:
    def __init__(self):
        self.name = "I am a shape!"

    def __str__(self):
        return self.name

class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = "I am a rectangle"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.name = "I am a Circle"


shape = Shape()
rect = Rectangle(2, 3)
circle = Circle(4)

print shape
print rect, "with", "length =", rect.x, "width =", rect.y
print circle

print isinstance(shape, Shape)
print isinstance(rect, Shape)
print isinstance(circle, Rectangle)


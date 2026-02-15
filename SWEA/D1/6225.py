class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


N = Rectangle(4, 5)
print(f"사각형의 면적: {N.area()}")
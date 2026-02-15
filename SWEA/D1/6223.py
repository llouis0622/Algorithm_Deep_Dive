class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


N = Circle(2)
print(f"원의 면적: {N.area()}")
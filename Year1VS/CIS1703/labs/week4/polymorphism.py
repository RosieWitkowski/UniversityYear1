class Shape():
    def __init__(self, height, length, name):
        self.height = height
        self.length = length
        self.name = name

    def calculate_area(self):
        return self.height * self.length
    
    def print_dimensions(self):
        print(f"{self.height}x{self.length} {self.name}")

class Triangle(Shape):
    def calculate_area(self):
        return .5 * self.height * self.length

square1 = Shape(2, 5, "square room")
triangle1 = Triangle(2, 5, "triangular wedge")

print(square1.calculate_area())
square1.print_dimensions()

print(triangle1.calculate_area())
triangle1.print_dimensions()

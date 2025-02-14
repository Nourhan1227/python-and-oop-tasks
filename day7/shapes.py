class Shape:
    count = 0

    def __init__(self, shapename, *dim):
        self.shapename = shapename
        self.dim = dim
        Shape.count += 1

    def area(self):
        pass 
    #     if self.shapename == "Square":
    #         return self.dim[0] ** 2
    #     elif self.shapename == "Triangle":
    #         return 0.5 * self.dim[0] * self.dim[1]
    #     elif self.shapename == "Parallelogram":
    #         return self.dim[0] * self.dim[1]
    #     elif self.shapename == "Circle":
    #         return 3.14 * (self.dim[0] ** 2)
    #     elif self.shapename == "Rectangle":
    #         return self.dim[0] * self.dim[1]
    #     else:
    #         return "Unknown shape "


class Circle(Shape):
    count = 0

    def __init__(self, radius):
        super().__init__("Circle", radius)
        self.radius = radius
        Circle.count += 1

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    count = 0

    def __init__(self, length, width):
        super().__init__("Rectangle", length, width)
        self.length = length
        self.width = width
        Rectangle.count += 1

    def area(self):
        return self.length * self.width

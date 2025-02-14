# demo.py
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    count = 0
    
    def __init__(self, name, d1, d2=0):
        self.name = name
        self.d1 = d1
        self.d2 = d2
        Shape.count += 1
    
    @abstractmethod
    def calcarea(self):
        pass  

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Line from {self.p1} to {self.p2}"

    def __len__(self):
        return int(math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2))

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle", base, height)

    def calcarea(self):
        return 0.5 * self.d1 * self.d2

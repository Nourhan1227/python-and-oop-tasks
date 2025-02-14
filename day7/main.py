from shapes import Shape, Circle, Rectangle  

shape1 = Shape("Square", 4)  
print("Square Area:", shape1.area())  

shape2 = Shape("Triangle", 6, 3)  
print("Triangle Area:", shape2.area())  

shape3 = Shape("Parallelogram", 5, 4)  
print("Parallelogram Area:", shape3.area())  

print("Total Shapes:", Shape.count)  




circle1 = Circle(5) 
circle2 = Circle(3)  
print("Circle Area:", circle1.area())  
print("Total Circles:", Circle.count)  




rect1 = Rectangle(6, 3)  
print("Rectangle Area:", rect1.area())  
print("Total Rectangles:", Rectangle.count)  

# main.py
from demo import Point, Line, Triangle

# Creating Points
p1 = Point(1, 2)
p2 = Point(4, 6)

# Create Line
line = Line(p1, p2)

# Create Triangle
triangle = Triangle(10, 5)

# Display Outputs
print(p1)             
print(p2)            
print(line)          
print(len(line))      
print(triangle.calcarea()) 

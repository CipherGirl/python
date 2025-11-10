# Classes should be open for extension but closed for modification.

"""Bad Example
class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2
"""

# Correct Way

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return 3.1416 * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2
    
"""
Note: The example above and some examples in the next sections use 
Python’s ABCs to provide what’s called interface inheritance. 
In this type of inheritance, subclasses inherit interfaces rather than functionality. 
In contrast, when classes inherit functionality, then you’re presented with implementation inheritance.
"""

    
circle = Circle(3)
rect = Rectangle(4, 5)
square = Square(4)

print(circle.calculate_area())
print(rect.calculate_area())
print(square.calculate_area())

"""
💡 Simple Explanation:

“Now I don’t touch existing code to add a new discount type — I just create a new subclass. 
That means the system is open for extension but closed for modification.”
"""
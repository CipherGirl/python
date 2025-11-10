"""
Polymorphism Types:
    1. Compile-Time Polymorphism: 
        It allows methods or operators with the same name to behave differently based on their input parameters or usage.
        Achieved through method overloading but it's not directly supported in Python
        In Python:
        - True compile-time polymorphism is not supported.
        - Instead, Python mimics it using default arguments or *args/**kwargs.
        - Operator overloading can also be seen as part of polymorphism, though it is implemented at runtime in Python.

    2. Run-Time Polymorphism:
        a. Method Overriding: A subclass redefines a method from its parent class.
        b. Duck Typing: If an object implements the required method, it works regardless of its type.
        c. Operator Overloading: Special methods (__add__, __sub__, etc.) redefine how operators behave for user-defined objects.
"""


# Compile-Time Polymorphism Example
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(5, 10))       # Two arguments
print(calc.add(5, 10, 15))   # Three arguments
print(calc.add(1, 2, 3, 4))  # Any number of arguments

# Run Time Polymorphism Example
from abc import abstractmethod
class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    # Method Overriding
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, width):
        self.width = width
    # Method Overriding
    def area(self):
        return self.width * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    # Method Overriding
    def area(self):
        return self.base * self.height

class Pizza(Circle):
    def __init__(self, toppings, radius):
        # Runtime polymorphism through inheritance
        super().__init__(radius)
        self.toppings = toppings

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Pepperoni", 10)]

# for shape in shapes:
    # print(f"{shape.area()} cm^2")


# Simple example of method overriding (duck typing as well)
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    # Override the parent method
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
def make_animal_speak(animal):
    # This function works for both Dog and Cat because they both have a 'speak' method.
    return animal.speak()

print(make_animal_speak(Cat()))
print(make_animal_speak(Dog()))

# Same method, different behavior
animals = [Dog(), Cat(), Animal()]

# for a in animals:
    # print(a.speak())


# Operator Overloading
# We create a simple class that customizes the '+' operator.

"""
Special methods in Python are methods with double underscores before and after the name (__method__).

They allow you to customize the behavior of built-in operations for your objects.

Examples: __init__, __str__, __len__, __getitem__, __add__, __repr__, etc.
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # This special method defines the behavior of the '+' operator.
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(v3)
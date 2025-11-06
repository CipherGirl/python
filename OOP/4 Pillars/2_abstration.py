# # Abstract Class = A class that cannot be instantiated on its own; Meant to be subclassed.
# #                  They can contain abtract methods, which are declared but have no implementations
# #                  Abstract class benefits:
# #                  1. Prevents instantiation of the class itself
# #                  2. Requires children to use inherited abtract methods
# # Partial Abstraction: Abstract class contains both abstract and concrete methods.
# # Full Abstraction: Abstract class contains only abstract methods (like interfaces).


from abc import ABC, abstractmethod
# ================
# Full Abstraction
# ================
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# vehicle = Vehicle()

class Car(Vehicle):
    def go(self):
        print("Driving the car")

    def stop(self):
        print("Stopped the car")

car = Car()

car.go()
car.stop()

class Motorcycle(Vehicle):
    def go(self):
        print("Riding the motorcycle")

    def stop(self):
        print("Stopped the motorcycle")


motorcycle = Motorcycle()

motorcycle.go()
motorcycle.stop()


# ===================
# Partial Abstraction
# ===================
class ElectricVehicle(ABC):

    @abstractmethod
    def charge(self):
        pass

    def dock_at_station(self):
        print("Charging the vehicle...")

class ElectricCar(ElectricVehicle):
    def charge(self):
        return super().dock_at_station()

electricCar = ElectricCar()

electricCar.charge()
# electricCar.go()
# electricCar.stop()


"""
Rafsun Bhai live session - Practice Abstract Class and Interface Class
"""
class Abs0(ABC):
    def test0(self):
        pass

    def test(self):
        print("Test from Abs0")
# Example of a Interface
class Abs1(ABC):
    def test1(self):
        pass

    
    def test(self):
        print("Test from Abs1")

class Abs2(ABC):
    @abstractmethod
    def test3(self):
        pass

    @abstractmethod
    def test4(self):
        pass

class Abs3(ABC):
    @abstractmethod
    def test6(self):
        pass

    @abstractmethod
    def test7(self):
        pass

class Xyz(Abs1, Abs0):
    # def test(self):
    #     print("Test")
    def test5(self):
        print("Test 5")
    
    print("Hello from Xyz")

class Xyz_1(Abs2, Abs3):
    def test3(self):
        print("Test 3")
    def test4(self):
        print("Test 4")
    def test6(self):
        print("Test 6")
    def test7(self):
        print("Test 7")
    print("Hello from Instance")

xyz = Xyz()
xyz_1 = Xyz_1()

xyz.test()


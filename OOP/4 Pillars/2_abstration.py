# Abstract Class = A class that cannot be instantiated on its own; Meant to be subclassed.
#                  They can contain abtract methods, which are declared but have no implementations
#                  Abstract class benefits:
#                  1. Prevents instantiation of the class itself
#                  2. Requires children to use inherited abtract methods
# Partial Abstraction: Abstract class contains both abstract and concrete methods.
# Full Abstraction: Abstract class contains only abstract methods (like interfaces).


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

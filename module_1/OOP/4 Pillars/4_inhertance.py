# Mutiple Inheritance = Inherit from more than one parent
#                       C(A, B)

# Multilevel Inheritance = Inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A 

class Animal:
    def __init__(self, name):
         self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# Single Inheritance
class Prey(Animal): 
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

# Multilevel Inheritence
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# Multiple and Multilevel Inheritence
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Maui")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()

# fish has both of the chacter of feeling and hunting 
# which is inherited from the Prey and Preditor parent classes

fish.flee()
fish.hunt()

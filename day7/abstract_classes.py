# Astract class = A class that cannot be instantiated on its own; Meant to be subclassed.
#                 They can contain abstract methods, which are declared but have no implementation.
#                 Abstract classes benefits:
#                 1. Prevents instantiations of the class itself
#                 2. Requires children to use inherited abstract methods

# abc - Abstract Base Classes
from abc import ABC, abstractmethod 


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def brake(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def brake(self):
        print("You brake the car")

class Motorbike(Vehicle):
    def go(self):
        print("You drive the motorbike")

    def brake(self):
        print("You brake the motorbike")


car = Car()
moto = Motorbike()

car.go()
car.brake()

moto.go()
moto.brake()

"""
Class is a blueprint for creating objects. 

Object is an instance of the class with unique attributes but the same structure. 

Class is a reusable component. Any amount aof instances might be created 
and all of them are maid with the same Car() class. 
To prevent assignment a  value from the car_bmw = Car() to the car_volvo = Car() 
self is used as a reference to the particular instance like bmw or volvo.

Without self, attributes would belong to the class itself, 
meaning all objects could accidentally overwrite each other’s values.

With self, each object gets its own memory space, 
preventing accidental modification from another instance like car_bmw affecting car_volvo.
"""
from car import Car

bmw_car = Car("M5", 2018, "Black", True)
print(bmw_car)          # Prints memory address
print(bmw_car.model)    # . stands for Attribute Access Operator

bmw_car.drive()

# Polymorphism = Greek word that means to "have mony forms or faces"
#                Poly = Many
#                Morphe = Form


#                TWO WAYS TO ACHIVE POLYMORPHISM
#                1. Inheritance - An object could be treated of the same type as a parent class
#                2. "Duck typing" - Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:
    # abstract method; requres ABC from abc and abstractmethod
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self. side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


# circle is an instance of the Circle which inherits from Shape
# hence, the circel has TWO FORMS (of the Circle and the Shape)
# but circle is not a triangle or square
circle = Circle(4)

shapes = [Circle(radius=4), Square(side=5), Triangle(base=7, height=8), Pizza(topping="pepperoni", radius=28)]

for shape in shapes:
    print(shape.area())

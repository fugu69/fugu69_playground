# super() = Function used in a child class to call methods from a paren (super) class. 
#           Allow you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, name, color, is_filled):
        self.name = name
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"{self.name} is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    # to inherit from the superclass we need to call its constructor inside the child constructor
    # and pass in required arguments
    def __init__(self, name, color, filled, radius):
        
        # self.color = color        # the code repeats itself
        # self. filled = filled

        super().__init__(name, color, filled)
        self.radius = radius 

    def describe(self):
        super().describe()
        print(f"It has a radius of  {self.radius}cm  and area of {3.14 * self.radius**2}cm^2.")

class Square(Shape):
    def __init__(self, name, color, is_filled, width):
        # self.color = color        # the code repeats itself
        # self. filled = filled

        super().__init__(name, color, is_filled)
        self.width = width 

    def describe(self):
        super().describe()
        print(f"It has an area of {self.width**2}cm^2.")

class Triangle(Shape):
    def __init__(self, name, color, is_filled, width, height):
        # self.color = color        # the code repeats itself
        # self. filled = filled

        super().__init__(name, color, is_filled) 
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It has an area of {self.width * self.height / 2}cm^2.")

circle = Circle(name = "Circle", color="red", filled=True, radius=28)
square = Square("Square", "blue", False, 10)
triangle = Triangle("Triangle", "purple", False, 8, 15)

# despite the argument called filled when we call the parent's constructor, the attribute has parent's name is_filled
# print(f"The circle has {circle.color} color, radius of {circle.radius} cm. Is it filled? {circle.is_filled}")
# print(f"The square has {square.color} color, width of {square.width} cm. Is it filled? {square.is_filled}")
# print(f"The triangle has {triangle.color} color, width of {triangle.width} cm and height of {triangle.height} cm. Is it filled? {triangle.is_filled}")

circle.describe()
square.describe()
triangle.describe()

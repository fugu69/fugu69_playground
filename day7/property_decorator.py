# @property = Decorator used to define a method as a property (it can be accessed like an attribut)
#             Benefit: Add functional logic when read, write or delete attributes
#             Gives getter, setter and deleter methods

class Rectangle:
    def __init__(self, width, height):
        self._width = width     # _name = _ stands for private
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter
    def width(self, new_width):
        self._width = new_width if new_width > 0 else print("error")

    @height.setter
    def height(self, new_height):
        self._height = new_height if new_height > 0 else print("error")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3, 4)

print(rectangle.width)
print(rectangle.height)
rectangle.width = 8
rectangle.width = 9
print(rectangle.width)
print(rectangle.height)
del rectangle.width
del rectangle.height


# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    # instance method
    def get_inf0(self):
        return f"{self.name} is {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Seller", "Seller", "Janitor"]
        # return True if position in valid_positions else False
        return position in valid_positions

print(Employee.is_valid_position("Manager"))

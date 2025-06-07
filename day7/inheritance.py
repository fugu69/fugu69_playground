# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extesdibility
#               Syntax: class Child(Parent)

# __init__(self) constructor is only needed when a class has attributes. In other cases it's optional.
# super() call is only needed to call a parent's constructor if we need it's attributes. In other cases it's optional.
# best prcatice is to call them explicitly for extensibility of the code

class Animal():
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print("Woof")

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print("Meow")

dog_pit = Dog("Pit")
cat_tom = Cat("Tom")

print(dog_pit.name)
print(dog_pit.is_alive)
dog_pit.eat()
dog_pit.bark()
cat_tom.sleep()
cat_tom.meow()

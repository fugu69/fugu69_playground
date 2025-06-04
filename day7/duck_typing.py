# "Duck typing" = Another way to achive polimorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                 If it meats minimum requirements, it's considerend as another type of object
#                 "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:

    alive = True

    def speak(self):
        print("BEEP!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

# multiple inheritance = Inherit from more than one parent calss
#                        Syntax class A(B, C)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          Syntax: class C(B) <- class B(A) <- class A

# Python automatically applies inherited constructors when no override exists
# super().__init__() is only needed when overriding the constructor in the child class
# Multiple inheritance works using MRO, so Fish correctly inherits from both Prey and Predator

class Animal:

    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")

class Prey(Animal):

    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):

    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator): 
    pass

class Fish(Prey, Predator):
    def __init__(self, name, species):
        super().__init__(name)          # ✅ Explicitly calling the parent constructor

        self.species = species          # ✅ New attribute

    def eat(self):                      # ✅ Override method to include species
        print(f"{self.name} the {self.species} is eating")

    def flee(self):                     # ✅ Override method to include species
        print(f"{self.name} the {self.species} is fleeing")

    def hunt(self):                     # ✅ Override method to include species
        print(f"{self.name} the {self.species} is hunting")
        

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo", "Clownfish")

print("Rabbit:")
rabbit.flee()
rabbit.eat()
print("Hawk:")
hawk.hunt()
hawk.eat()
print("Fish:")
fish.flee()
fish.hunt()
fish.eat()

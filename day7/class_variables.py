# class variables = Shared among all instances of a class
#                   Defined outside the constuctor
#                   Allow you to share data among all objects created from that class

import gc

class Student:

    graduate_year = 2024
    classes = ['Biology', 'Geography', 'Chemistry', 'History']
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

std1 = Student("Joseph", 19)
std2 = Student("Nikol", 17)

print(std1.name, std1.classes)
print(std2.name, std2.classes)

print(Student.num_students)


# print(gc.get_objects())

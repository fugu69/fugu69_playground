# Nested class = A class defined within another class
#                class Outer:
#                   class Inner:

# Benefits =     Allows you to logically group classes that are closely related
#                Encapsulates privates details that aren't relevant outside of the outer class
#                Keeps the namespace clean; reduces the possibility of naming conflicts

"""
class Employee:
    print("This is the first class")

class Employee: #naming conflict
    print("This is the second class")

class Company:
    class Employee:
        print("First class")

class Nonprofit:
    class Employee:
        print("Second class")
"""

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} is {self.position}"

    # Company scope
    # Not an Employee scope
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        self.employees.append(self.Employee(name, position))

    def list_employees(self):
        # return [employee.get_details() for employee in self.employees]
        return [f"{employee.name} is {employee.position}" for employee in self.employees]

company = Company("Dickheads")
big_bang_company = Company("Big Bang")

manager = company.add_employee("Joseph", "Head Manager")
seller = company.add_employee("Alex", "Seller")
head = company.add_employee("Eugene", "Head of The Office")

sheldon = big_bang_company.add_employee("Sheldon Cooper", "Theoretical Phisicist")
leonard = big_bang_company.add_employee("Leonard Hofstadter", "Experimental Phisicist")

print("The Office personell:")
for employee in company.list_employees():
    print(employee)

print("Caltech personell:")
for employee in big_bang_company.list_employees():
    print(employee)



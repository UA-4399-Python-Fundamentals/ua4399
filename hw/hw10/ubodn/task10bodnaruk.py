# Task 1

class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(sides=4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(length=10, width=5)
print(f"Number of sides: {rectangle.sides}")
print(f"Area of rectangle: {rectangle.area()}")


# Task 2

class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species_information(cls):
        return f"Species: {cls.species}"

    @staticmethod
    def general_message():
        return "Cats are better than Humans!"    

person = Human("Vasia")

person.welcome()
print(Human.species_information())
print(Human.general_message())


# Task 3

class Employee:
    """ A Class that represents the name and the salary of employees."""

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total_employees(cls):
        print(f"Total Employees: {cls.employee_count}")

emp1 = Employee("Ivan", 120000)
emp2 = Employee("Marichka", 180000)

emp1.display_info()
emp2.display_info()

Employee.total_employees()

print("Base:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)

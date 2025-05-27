# Task 1
class Polygon:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Polygon):
    def area(self):
        return self.width * self.height

# Task 2
class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"Species: {cls.species}"

    @staticmethod
    def random_message():
        return "Be kind, stay human!"


# Task 3
class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def total_employees(cls):
        return f"Total employees: {cls.count}"

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

# Test 

# Task 1 Test
print("Task 1")
rect = Rectangle(4, 6)
print("Area of rectangle:", rect.area())

# Task 2 Test
print("\nTask 2")
person = Human("Dmytro")
person.greet()
print(Human.get_species())
print(Human.random_message())

# Task 3 Test
print("\nTask 3")
emp1 = Employee("John", 45000)
emp2 = Employee("Jane", 30000)

print(emp1.display_info())
print(emp2.display_info())
print(Employee.total_employees())

# Meta Info
print("\nClass Meta Information")
print("Base classes:", Employee.__bases__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
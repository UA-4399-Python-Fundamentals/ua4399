# Task 1: Polygon and Rectangle Classes
class Polygon:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Polygon):
    def area(self):
        return self.width * self.height

# Task 2: Human Class
class Human:
    species = "Homosapiens"
    
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"This is a species of {cls.species}."

    @staticmethod
    def arbitrary_message():
        return "Humans are social beings."

# Task 3: Employee Class
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

# --- Test section ---

# Task 1 Test
print("=== Task 1 ===")
rect = Rectangle(5, 10)
print("Area of rectangle:", rect.area())

# Task 2 Test
print("\n=== Task 2 ===")
person = Human("Alice")
person.welcome()
print(Human.get_species())
print(Human.arbitrary_message())

# Task 3 Test
print("\n=== Task 3 ===")
emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)

print(emp1.display_info())
print(emp2.display_info())
print(Employee.total_employees())

# Meta Info
print("\n--- Class Meta Information ---")
print("Base classes:", Employee.__bases__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)

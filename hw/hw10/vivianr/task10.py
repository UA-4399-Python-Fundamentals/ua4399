#task 10.1
class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, length):
        super().__init__(4)
        self.width = width
        self.length = length
    def square(self):
        return self.width * self.length
    
#task 10.2
# creating a class with class and static methods
class Human:
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return f"Hello, Name: {self.name}!"
    @classmethod
    def get_species(cls):
        return f"This is a species of {cls.species}."
    @staticmethod
    def message():
        return "This is a static method."

#task10.3
class Employee:
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.__class__.count += 1
    def display(self):
        return f"Name: {self.name}, Salary: {self.salary}"
    
    @classmethod
    def get_number_of_employees(cls):
        return f"Number of employees: {cls.count}"

print("Base classes:", Employee.__bases__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)
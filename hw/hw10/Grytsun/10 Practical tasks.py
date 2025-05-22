# Task 1: Polygon and Rectangle Classes
class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)  # A rectangle has 4 sides
        self.width = width
        self.height = height

    def get_area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height


# Example usage
rectangle = Rectangle(2, 16)
print(f"Rectangle Area: {rectangle.get_area()}")  # Output: Rectangle Area: 32

# Task 2: Human Class
class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        """Displays a welcome message to the person."""
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        """Returns the species of the human."""
        return f"Species: {cls.species}"

    @staticmethod
    def arbitrary_message():
        """Returns an arbitrary message."""
        return "Humans are amazing creatures!"


# Example usage
person = Human("John")
print(person.welcome_message())  # Output: Welcome, John!
print(Human.get_species())       # Output: Species: Homosapiens
print(Human.arbitrary_message()) # Output: Humans are amazing creatures!

# Task 3: Employee Class
class Employee:
    total_employees = 0  # Class variable to count total employees

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def get_total_employees(cls):
        """Prints the total number of employees."""
        return f"Total Employees: {cls.total_employees}"

    def display_info(self):
        """Displays information about the employee."""
        return f"Name: {self.name}, Salary: {self.salary}"


# Example usage
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

print(employee1.display_info())  # Output: Name: Alice, Salary: 50000
print(employee2.display_info())  # Output: Name: Bob, Salary: 60000
print(Employee.get_total_employees())  # Output: Total Employees: 2

# Display class information
print(f"Base Classes: {Employee.__base__}")  # Output: <class 'object'>
print(f"Namespace: {Employee.__dict__}")    # Output: Class attributes and methods
print(f"Class Name: {Employee.__name__}")  # Output: Employee
print(f"Module Name: {Employee.__module__}")  # Output: __main__
print(f"Documentation: {Employee.__doc__}")  # Output: None (unless docstring is added)
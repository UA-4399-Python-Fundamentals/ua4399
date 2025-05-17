# Task1
class Polygon:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Rectangle(Polygon):

    def area(self):
        return self.length * self.width


def main():
    r = Rectangle(length=4, width=5)
    print(f"This is the are of a rectangle: {r.area()}")


main()


# Task2
class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello and Welcome, {self.name}")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def get_message():
        return "Arbitrary message!"


# Task3
class Employee:
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def counter_of_employees(cls):
        return Employee.counter

    def employee_profile(self):
        return f"Name: {self.name}, Salary: {self.salary}"


print(f"Class base: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Class module: {Employee.__module__}")
print(f"Class doc: {Employee.__doc__}")

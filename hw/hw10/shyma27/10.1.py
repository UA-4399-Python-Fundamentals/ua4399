#======task 1======
class Polygon():
    def square(self):
        return self.a * self.b

class Rectangle(Polygon):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
r = Rectangle(10, 10)
print(f"Square: {r.square()}\n")

#======task 2 =======
class Human():
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(f"Hello, {self.name}")
    
    @classmethod
    def species(cls):
        return f"Homosapiens"
    
    @staticmethod
    def lorem():
        return f"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"

h = Human("Anton")
h.print_name()
print(Human.species())
print(Human.lorem())

#======task 3======
class Employee():
    '''Employee class'''
    emp_count = 0
    
    def __init__(self, name, salary:int):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1
    
    def emp_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")
    
    @classmethod
    def total_emp(cls):
        print(f"Total employees: {Employee.emp_count}") 

    @staticmethod
    def inheritance():
        print(f"Inherited: {Employee.__base__}\nNamespace: {Employee.__dict__}\nName: {Employee.__name__}\nModule: {Employee.__module__}\nDocs: {Employee.__doc__}\n")

e = Employee("Dido", 10000)
e.emp_info()
Employee.total_emp()
Employee.inheritance()
e2 = Employee("Baba", 11000)
e2.emp_info()
Employee.total_emp()
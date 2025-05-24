# Homework Lesson 10

# ///////////////////////////////////////////////////////////////////
# 3 - Create an Employee class
print("Subtask 3")

class Employee:
    '''This class describes the employee of a company.'''
    counter = 0

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary
        
        Employee.counter += 1

    def information(self):
        return f"Employee - {self.name}, salary - {self.salary}"

    @classmethod
    def total_employees(cls):
        return Employee.counter


bobby = Employee("Bob", 1000)
print(bobby.information())

billy = Employee("Bill", 2000)
print(billy.information())

print(Employee.total_employees())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

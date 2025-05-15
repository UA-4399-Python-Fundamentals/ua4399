class Employee():
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count +=1

    @classmethod
    def total_employee(cls):
        return f"Total employees: {cls.count}"

    def info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

print("Base classes:", Employee.__bases__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)
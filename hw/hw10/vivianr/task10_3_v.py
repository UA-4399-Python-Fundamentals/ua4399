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
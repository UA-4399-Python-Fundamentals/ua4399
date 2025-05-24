import pandas as pd

class Employee:

    _employee_count = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        Employee._employee_count += 1

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @classmethod
    def total_employees(cls):
        return f"Total employees: {cls._employee_count}"

    def display_info(self):
        return f"Name: {self.__name}, Salary: {self.__salary}"

    @staticmethod
    def load_from_excel(file_path):
        """Loading a list of employees from an Excel file."""
        df = pd.read_excel(file_path)
        employees = [Employee(row["Name"], row["Salary"]) for _, row in df.iterrows()]
        return employees

# Var1
emp1 = Employee("Alex", 2500)
emp2 = Employee("Sara", 3500)

print(emp1.display_info())
print(emp2.display_info())
print(Employee.total_employees())

# +Var2
file_path = "Employee.xlsx"
employees = Employee.load_from_excel(file_path)

print("\nEmployees loaded from Excel:")
for emp in employees:
    print(emp.display_info())
print(Employee.total_employees())

print("\nClass metadata:")
print("Base classes:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)

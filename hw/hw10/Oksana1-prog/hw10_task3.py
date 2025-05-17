#Task 3 Create an employee class.
class Employee:
    employee_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")
    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp1.display_employee_info()
emp2.display_employee_info()
Employee.display_total_employees()
print("\nClass Introspection Details:")
print("Base classes:", Employee.__base__)
print("Class namespace (__dict__):", dict(Employee.__dict__))
print("Class name (__name__):", Employee.__name__)
print("Module name (__module__):", Employee.__module__)
print("Documentation (__doc__):", Employee.__doc__)
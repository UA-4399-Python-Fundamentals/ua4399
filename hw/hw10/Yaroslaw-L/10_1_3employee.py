class Employee:
    """A class to represent an employee with name and salary."""
    total_emp = 0
    def __init__(self, name_emp, salary):
        self.name_emp = name_emp
        self.salary = salary
        Employee.total_emp +=1
    def disp_particular(self):
        print(f"Name: {self.name_emp}, Salary: {self.salary}")
    @classmethod   
    def display_all(all):
        print(f"Number of employees: {all.total_emp}")

employees = [Employee("Jane", 1200),
             Employee("Boby", 1500)]
for emp in employees:
    emp.disp_particular()

Employee.display_all
print("Additional Info: ")
print("Base class: ", Employee.__base__)
print("Class namespace (__dict__):", Employee.__dict__)
print("Class name (__name__):", Employee.__name__)
print("Module_name (__module):", Employee.__module__)
print("Class documentation (__doc__):", Employee.__doc__)
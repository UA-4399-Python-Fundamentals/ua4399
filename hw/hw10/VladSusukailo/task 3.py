class Employee:
    count = 0
    employees = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
        Employee.employees.append(self)

    @classmethod
    def total_employees(cls):
        return cls.count

    @classmethod
    def show_all_employees(cls):
        for emp in cls.employees:
            print(emp.name, emp.salary)

e1 = Employee("John", 3000)
e2 = Employee("Jane", 4000)

print(Employee.total_employees())
Employee.show_all_employees()

print(Employee.__bases__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
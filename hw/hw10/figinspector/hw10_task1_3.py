class Employee:
    """ base class employee """

    total_employees = 0
    
    def __init__(self, name, salary):
        Employee.total_employees += 1
        self.name = name
        self.salary = salary
    
    def about(self):
        return f"{self.name} earns ${self.salary}"

    @classmethod
    def total_staff(cls):
        return cls.total_employees
    
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

employee_id_01 = Employee('Dawn', 3_600)
employee_id_02 = Employee('Cali', 2_400)
employee_id_03 = Employee('Paige', 4_004)

print(employee_id_01.about())
print(employee_id_02.about())
print(employee_id_03.about())

print(Employee.total_staff())
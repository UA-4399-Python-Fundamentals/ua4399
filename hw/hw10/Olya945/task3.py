class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def info(self):
        return f"Ім'я: {self.name}, Зарплата: {self.salary}"
    
    @classmethod
    def total_employees(cls):
        return f"Загальна кількість працівників: {cls.employee_count}"
    
    def class_info(self):
        return f"""
Інформація про клас:
Базові класи: {Employee.__bases__}
Простір імен класу: {Employee.__dict__}
Ім'я класу: {Employee.__name__}
Модуль класу: {Employee.__module__}
Документація: {Employee.__doc__}
"""
    
employee1 = Employee("Оля", 25000)
employee2 = Employee("Іван", 30000)
employee3 = Employee("Марія", 28000)
print(employee1.info())
print(employee2.info())
print(employee3.info())
print(Employee.total_employees())
print(employee1.class_info())

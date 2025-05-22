class Employee:
    count_employees = 0  

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count_employees += 1

    def total_employees(self):
        return f"Total Employees: {Employee.count_employees}"

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"
    
employee1 = Employee("Kate", 62300)
employee2 = Employee("Mike", 56000)

print(employee1.display_info())   
print(employee2.display_info())  
print(Employee.total_employees(Employee))  

print(f"Base - {Employee.__base__}")  
print(f"Dict - {Employee.__dict__}")  
print(f"Name - {Employee.__name__}")  
print(f"Mod - {Employee.__module__}")  
print(f"Doc - {Employee.__doc__}")  
class Employee:
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
    
    def __del__(self):
        Employee.counter -= 1
    
    @classmethod
    def show_counter(cls):
        print(Employee.counter)
    
    def display_info(self):
        print(f"Employee info: name is {self.name}, salary is {self.salary}")

Volodymyr = Employee("Volodymyr", 1000)
Volodymyr.display_info()
Employee.show_counter()

Vitaliy = Employee("Vitaliy", 500)
Vitaliy.display_info()
Employee.show_counter()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
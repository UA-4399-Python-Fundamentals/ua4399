class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self):
        print(f"Name : {self.name} , Salary = {self.salary}")

    @classmethod
    def display_total_empl(cls):
        print(f"employee_count =  {cls.employee_count}")

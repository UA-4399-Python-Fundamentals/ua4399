#task1
class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Rectangle(Polygon):
    def area(self):
        return self.length * self.width


def rectangle_square(l,w):
    return f"Square area of a rectangle is: {Rectangle(l,w).area()}"

print(rectangle_square(4,5))

#task2
class Human:
    def __init__(self,name):
        self.name = name

    def greeting(self):
        return f"Welcome, {self.name}"

    @classmethod
    def species_info(cls):
        return f"{cls.__name__} is a species of Homosapiens."

    @staticmethod
    def get_message():
        return "Hello, I am a Human!"

h1 = Human("George")


#task3
class Employee(Human):
    '''
    Class represents an Employee
    Attributes:
        name(str): Employee name (inherited from Human)
        salary(int): Employees salary
    '''

    employees_amount = 0
    employees_dict = {}

    def __init__(self,name,salary: int):
        super().__init__(name)
        self.salary = salary
        Employee.employees_amount += 1
        Employee.employees_dict[self.name]=self.salary


    @staticmethod
    def get_employees_number():
        return f"There are {Employee.employees_amount} employees"

    @staticmethod
    def get_employees_info():
        result = ""
        for key,value in Employee.employees_dict.items():
            result += f"Employee {key} has salary of {value} \n"
        return result



e1 = Employee("George",123)
e2 = Employee("Alice",456)
print(Employee.get_employees_number())
print(e1.get_employees_info())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)





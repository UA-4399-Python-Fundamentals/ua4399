############################################################################## 1 ##############################################################################

# class Polygon:
#     def __init__(self, sides: int):
#         self.sides = sides

# class Rectangle(Polygon):
#     def __init__(self, side_a: int, side_b: int):
#         super().__init__(4)
#         self.side_a = side_a
#         self.side_b = side_b

#     def rectangle_area(self):
#         return self.side_a * self.side_b
    

# print(Rectangle.__mro__)    

# rect_side_a = int(input("Enter lenght side a: "))
# rect_side_b = int(input("Enter lenght side b: "))
# rect = Rectangle(rect_side_a, rect_side_b)
# print(rect.rectangle_area())


############################################################################## 2 ##############################################################################

# class Human:
#     def __init__(self, name: str):
#         self.name = name

#     def welcome_message(self):
#         print(f"Hola amigo, {self.name}!")

#     @classmethod
#     def species(cls):
#         print('Homosapiens')

#     @staticmethod
#     def message():
#         print(f"Keep calm!")
    


# call_name = input("Call your name: ")
# name = Human(call_name)
# name.welcome_message()
# name.species()
# name.message()


############################################################################## 3 ##############################################################################

# class Employee:
#     workers = 0
#     def __init__(self, name: str, salary: int):
#         self.name = name
#         self.salary = salary
#         self.__class__.workers +=1

#     @classmethod
#     def current_employees(cls):
#         return cls.workers
    
#     def name_salary(self):
#         return f"{self.name}: {self.salary}"
    

# first = Employee('Den', 4000)
# second = Employee('Karl', 5000)
# third = Employee('Zak', 6000)
# print(Employee.workers)
# print(Employee.__base__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__doc__)
# print(Employee.current_employees())

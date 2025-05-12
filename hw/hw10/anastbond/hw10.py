#TASK1
class Polygon:
  def __init__(self):
    self.a = float(input('Enter a in cm'))
    self.b = float(input('Enter b in cm'))

class Rectangle(Polygon):
  def __init__(self):
    super().__init__()
  def square(self):
    return self.a*self.b

#TASK2
class Human:
  def __init__(self, name):
    self.name = name
  def greet(self):
    return f"Welcome,{self.name}!"
  
  @classmethod
  def ishomosapiens(cls):
    return 'Is homosapiens'

#TASK3
class Employee:
  counter = 0
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.counter += 1
  
  def show_empl(self):
    return f"{self.name} earns {self.salary} "
  @classmethod
  def show_total(cls):
    return cls.counter

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")

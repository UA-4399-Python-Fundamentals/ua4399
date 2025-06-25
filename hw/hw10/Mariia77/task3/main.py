from Employee import Employee

emp1 = Employee("Mariia", 4000)

emp2 = Employee("Sasha", 5000)

emp1.display_info()
emp2.display_info()
Employee.display_total_empl()

print("__base__" , Employee.__base__)
print("__dict__" , Employee.__dict__)
print("__name__" , Employee.__name__)
print("__module__" , Employee.__module__)
print("__doc__" , Employee.__doc__)


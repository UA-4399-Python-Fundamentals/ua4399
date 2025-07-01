class Employee:
    __employees_count = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = float(salary)
        Employee.__employees_count += 1

    def info(self):
        return f"{self.__name}  {self.__salary}"

    @classmethod
    def employees_counter(cls):
        return cls.__employees_count

    @staticmethod
    def class_info():
        print(f"Base classes: {Employee.__bases__}")
        print(f"Class namespace (__dict__): {Employee.__dict__}")
        print(f"Class name (__name__): {Employee.__name__}")
        print(f"Module name (__module__): {Employee.__module__}")
        print(f"Documentation (__doc__): {Employee.__doc__}")
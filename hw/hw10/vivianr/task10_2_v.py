# creating a class with class and static methods
class Human:
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return f"Hello, Name: {self.name}!"
    @classmethod
    def get_species(cls):
        return f"This is a species of {cls.species}."
    @staticmethod
    def message():
        return "This is a static method."

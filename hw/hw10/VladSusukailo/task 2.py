class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def random_message():
        return "Stay curious!"

h = Human("Alice")
print(h.greet())
print(Human.species())
print(Human.random_message())
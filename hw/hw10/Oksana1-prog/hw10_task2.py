#Task 2. Create a class Human, everyone has a name, create a method in the
#class that displays a welcome message to each person. Create a class method
#in the class that returns information that it is a species of "Homosapiens". And
#in the class create a static method that returns an arbitrary message.

class Human:
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name
    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"This species is {cls.species}."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message from the Human class."
person1 = Human("Alice")
person1.welcome()
print(Human.get_species())
print(Human.arbitrary_message())
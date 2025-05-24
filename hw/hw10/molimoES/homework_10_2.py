# Homework Lesson 10

# ///////////////////////////////////////////////////////////////////
# 2 - Create the Human's class
print("Subtask 2")

class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello, {self.name}!"

    @classmethod
    def species(cls):
        return "You are a \"Homosapiens\"!"

    @staticmethod
    def arbitrary_message():
        return "Hello, World!"


h = Human("Eugen")
print(h.welcome_message())
print(Human.species())
print(Human.arbitrary_message())

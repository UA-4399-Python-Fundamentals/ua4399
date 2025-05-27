class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species(cls, name):
        return f"{name} is a homosapien."

    @staticmethod
    def arbitrary_message(name):
        return f"Have a nice day, {name}!"


everyone = ["Oksana", "Yurii", "Dasha"]
for person in everyone:
    human = Human(person)
    print(human.welcome_message())
    print(Human.species(person))
    print(Human.arbitrary_message(person))
    print()

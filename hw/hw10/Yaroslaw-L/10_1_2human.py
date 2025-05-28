class Human:
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name
    def welcome(self):
        print(f"Hello, {self.name}!")
    @classmethod
    def return_inf(inf):
        return f"Humans are {inf.species}"
    @staticmethod
    def arbitrary(msg):
        return f"{msg.species} are only survived of Homo"
user_1=Human("Boby")
user_1.welcome()
print(Human.return_inf())
print(Human.arbitrary(Human))
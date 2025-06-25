class Human:
    def __init__(self, name):
        self.name = name

    def inputName(self):
        self.name = input("Enter the name of Human -> ")

    def dispHuman(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def isHomosapiens(cls):
        return "This Human is Homosapiens"

    @staticmethod
    def staticmethod():
        return "This method is static"

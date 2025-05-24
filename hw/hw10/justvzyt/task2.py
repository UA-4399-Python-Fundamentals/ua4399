class Human:
    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):
        print(f"Welcome, {self.name}!")
    
    def homosapiens(self):
        return "Homosapiens"
    
    @staticmethod
    def static_method():
        return "This is a static method"


Volodymyr = Human("Volodymyr")
Volodymyr.welcome_message()
print(f"Volodymyr is {Volodymyr.homosapiens()}")
print(Human.static_method())
print(Volodymyr.static_method())
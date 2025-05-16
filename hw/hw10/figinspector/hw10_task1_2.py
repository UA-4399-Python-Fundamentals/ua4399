class Human:
    """base class for human"""

    object_class = "Homosapiens"
    
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"{self.name} say hello!"
    
    @classmethod
    def info(cls):
        return cls.object_class

    @staticmethod
    def about():
        return f"Hi from base class"


human_1 = Human('Abel')

print(human_1.say_hello())
print(human_1.info())
print(human_1.about())

print(Human.info())
print(Human.about())
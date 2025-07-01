class Human:
    def __init__(self, name):
        self.__name = name

    def hello(self):
        return f"Hello {self.__name}!"

    @classmethod
    def species(cls):
        return "Homosapiens"
    
    @staticmethod
    def motto():
        return "I love python"
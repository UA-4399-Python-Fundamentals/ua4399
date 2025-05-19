class Human:
    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):
        return f"Привіт, {self.name}!"
    
    @classmethod
    def info(cls):
        return "Це клас людина."
    
    @staticmethod
    def static_info():
        return "Довільне повідомлення."
man = Human("Оля")
print(man.welcome_message())
print(Human.info())
print(Human.static_info())

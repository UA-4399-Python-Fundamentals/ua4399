class Person:
    def __init__(self, name:str, age:int):
        self.info=f"{name}s age is {age}"
    def getInfo(self):
        return self.info
class Human:
    def __init__(self, name):
        self.name = name
                
    def greet(self):
        return (f"Hello, my name is {self.name}")
    
    def Homo_sapiens(self):
        return (f"{self.name}, Homo sapiens")
               
    @staticmethod
    def arbitrary_message():
        return (f"What's alse?")
        
human = Human(input('name:'))

print (f"{human.greet()}. {human.Homo_sapiens()}. {human.arbitrary_message()}")


        

        



    
 
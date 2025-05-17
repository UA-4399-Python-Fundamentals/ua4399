import random
class Ghost(object):
    def __init__(self):
        x = random.randint(1, 4)
        if x == 1:
            self.color = "white"
        elif x == 2:
            self.color = "yellow"
        elif x == 3:
            self.color = "purple"
        else:
            self.color = "red"
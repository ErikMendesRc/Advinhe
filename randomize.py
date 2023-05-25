import random


class Randomize:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def randomize(self):
        randomNumber = random.randint(self.a, self.b)
        return randomNumber

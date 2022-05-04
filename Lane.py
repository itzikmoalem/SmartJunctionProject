from random import randint


class Lane:
    def __init__(self, n):
        self.name = n
        self.greenTimer = randint(5, 15)
        self.someChange = 1



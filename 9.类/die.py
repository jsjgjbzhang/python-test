from random import randint


class Die():
    """docstring for Die"""

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, times):
        for x in range(1, times + 1):
            print(randint(1, self.sides))

from random import randint

class DiceService(object):

    def roll(self):
        return randint(1, 6)
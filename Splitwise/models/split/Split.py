from abc import ABC, abstractmethod

class Split(ABC):
    def __init__(self, user, amount):
        self.user =  user
        self.amount = amount

    def setUser(self, user):
        self.user = user

    def getUser(self):
        return self.user

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount
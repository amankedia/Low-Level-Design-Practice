import uuid

class Player(object):

    def __init__(self, name):
        self.name = name
        self.id = str(uuid.uuid4())

    def getName(self):
        return self.name

    def getID(self):
        return self.id
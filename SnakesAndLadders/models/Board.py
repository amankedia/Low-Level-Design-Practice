class Board(object):

    snakes = []
    ladders = []
    playerPieces = {}

    def __init__(self, size):
        self.size = size

    def setSnakes(self, snakes):
        self.snakes = snakes

    def setLadders(self, ladders):
        self.ladders = ladders

    def setPlayerPieces(self, playerPieces):
        self.playerPieces = playerPieces

    def getSnakes(self):
        return self.snakes

    def getLadders(self):
        return self.ladders

    def getSize(self):
        return self.size

    def getPlayerPieces(self):
        return self.playerPieces

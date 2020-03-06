from SnakesAndLadders.models.Board import Board
from SnakesAndLadders.services.DiceService import DiceService
from collections import deque

class SnakeAndLadderService(object):

    DEFAULT_BOARD_SIZE = 100
    DEFAULT_NO_OF_DICES = 1
    players = deque()
    playerPieces = {}

    def __init__(self, boardSize):
        self.snakeAndLadderBoard = Board(boardSize)
        self.noOfDices = self.DEFAULT_NO_OF_DICES
        self.diceService = DiceService()

    def setPlayers(self, players):
        self.initialNumberOfPlayers = len(players)
        for player in players:
            self.players.append(player)
            self.playerPieces[player.getID()] = 0
        self.snakeAndLadderBoard.setPlayerPieces(self.playerPieces)

    def setNoOfDices(self, noOfDices):
        self.noOfDices = noOfDices

    def setSnakes(self, snakes):
        self.snakeAndLadderBoard.setSnakes(snakes)

    def setLadders(self, ladders):
        self.snakeAndLadderBoard.setLadders(ladders)

    def getNewPositionAfterGoingThroughSnakesAndLadders(self, newPosition):
        while(True):
            previousPosition = newPosition
            for snake in self.snakeAndLadderBoard.getSnakes():
                if snake.getStart() == newPosition:
                    newPosition = snake.getEnd()
            for ladder in self.snakeAndLadderBoard.getLadders():
                if ladder.getStart() == newPosition:
                    newPosition = ladder.getEnd()
            if newPosition == previousPosition:
                break
        return newPosition

    def movePlayer(self, player, positions):
        oldPosition = self.snakeAndLadderBoard.getPlayerPieces()[player.getID()]
        newPosition = oldPosition + positions
        boardSize = self.snakeAndLadderBoard.getSize()

        if newPosition > boardSize:
            newPosition = oldPosition
        else:
            newPosition = self.getNewPositionAfterGoingThroughSnakesAndLadders(newPosition)
        self.snakeAndLadderBoard.getPlayerPieces()[player.getID()] = newPosition
        print(player.getName() + " rolled a " + str(positions) + " and moved to " + str(newPosition))

    def getDiceRollValue(self):
        return self.diceService.roll()

    def hasPlayerWon(self, player):
        playerPosition = self.snakeAndLadderBoard.getPlayerPieces()[player.getID()]
        boardSize = self.snakeAndLadderBoard.getSize()
        return boardSize == playerPosition

    def isGameComplete(self):
        currentNumberOfPlayers = len(self.players)
        return currentNumberOfPlayers < self.initialNumberOfPlayers

    def startGame(self):
        while not self.isGameComplete():
            diceValue = self.getDiceRollValue()
            currentPlayer = self.players.popleft()
            self.movePlayer(currentPlayer, diceValue)
            if self.hasPlayerWon(currentPlayer):
                print("Player " + currentPlayer.getName() + " has won")
                del self.snakeAndLadderBoard.getPlayerPieces()[currentPlayer.getID()]
            else:
                self.players.append(currentPlayer)
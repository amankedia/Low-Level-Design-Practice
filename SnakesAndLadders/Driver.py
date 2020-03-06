from models.Snake import Snake
from models.Ladder import Ladder
from models.Player import Player
from services.SnakeAndLadderService import SnakeAndLadderService

class Driver(object):

    snakes = []
    ladders = []
    players = []

    def main(self):

        numberOfSnakes = input("Enter number of snakes: ")
        numberOfSnakes = int(numberOfSnakes)

        for i in range(numberOfSnakes):
            start = input("Enter start position of snake " + str(i+1) + " : ")
            end = input("Enter end position of snake " + str(i+1) + " : ")
            self.snakes.append(Snake(int(start), int(end)))

        numberOfLadders = int(input("Enter number of ladders: "))

        for i in range(numberOfLadders):
            start = input("Enter start position of ladder " + str(i + 1) + " : ")
            end = input("Enter end position of ladder " + str(i + 1) + " : ")
            self.ladders.append(Ladder(int(start), int(end)))

        numberOfPlayers = int(input("Enter number of players: "))

        for i in range(numberOfPlayers):
            name = input("Enter name of player " + str(i+1) + " : ")
            self.players.append(Player(name))


        snakeAndLadderService = SnakeAndLadderService(100)

        snakeAndLadderService.setPlayers(self.players)
        snakeAndLadderService.setSnakes(self.snakes)
        snakeAndLadderService.setLadders(self.ladders)

        snakeAndLadderService.startGame()





if __name__ == "__main__":
    driver = Driver()
    driver.main()

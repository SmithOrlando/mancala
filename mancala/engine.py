from loguru import logger
from player import Player
import os

class Engine:
    def __init__(self):
        """
        :param player1:  a player class instance
        :param player2:  a player class instance
        """
        self.player1 = Player()
        self.player2 = Player()
        
    def switch(self, switch, player):
        for mvt in range(switch):
            player.board[str(mvt + 1)] += 1
        pass
    
    def rewind(self):
        pass
    
    def show(self):
        print("player1\t\t\tplayer2")
        print("   {}\t\t\t   {}".format(self.player1.points, self.player2.points))
        print('\n')
        for item in self.player2.board:
            print("   {}\t\t\t   {}".format(self.player1.board[item], self.player2.board[item]))
    
    def run(self):
        # print("player you can move between 1 - 6")
        # print("palyer1 first move")
        # print(self.player1.move(int(input())))
        while True:
            self.show()
            next_move1 = int(input("\nplayer1 what's your next move ?"))
            if next_move1 in range(1, self.player1.get_border() + 1):
                switch = self.player1.move(next_move1)
                if switch > 0:
                    self.switch(switch, self.player2)
            else:
                print('\nImpossible move')
                
            os.system('clear')
            self.show()

            next_move2 = int(input("\nplayer2 what's your next move ?"))
            if next_move2 in range(1, self.player2.get_border() + 1):
                switch = self.player2.move(next_move2)
                if switch > 0:
                    self.switch(switch, self.player1)
            else:
                print('\nImpossible move')
            os.system('clear')


def run():
    engine = Engine()
    engine.run()


if __name__ == '__main__':
    run()

from loguru import logger


class Player:
    def __init__(self):
        self.board = {
            '1': 4,
            '2': 4,
            '3': 4,
            '4': 4,
            '5': 4,
            '6': 4,
        }
        self.points = 0
    
    def show(self):
        for holes in self.board:
            print(self.board[holes])
            
    def get_border(self):
        return len(self.board)
    
    def get_values(self, hole):
        return self.board[str(hole)]
    
    def update(self, hole):
        self.board[str(hole)] -= self.board[str(hole)]
    
    def move(self, hole):
        beans = self.get_values(hole)
        if beans > 0:
            self.update(hole)
            index = hole
            length = self.get_border()
            for mvnt in range(beans):
                if index < length:
                    self.board[str(index + 1)] += 1
                    index += 1
                elif index == length:
                    self.points += 1
                    index += 1
                else:
                    print('\n')
                    # self.show()
                    print("you've acumulated {} points".format(self.points))
                    logger.info("to the next player")
                    return beans - mvnt
            # print('\n')
            # self.show()
            # print("you've acumulated {} points".format(self.points))
            return 0
        else:
            print('empty cave !')
            return 0
            
    def sumUp(self):
        for cave in self.board:
            self.points += self.board[cave]
            self.board[cave] = 0
        return self.points

    
def main():
    player1 = Player()
    print("player1 you can move between 1 - 6")
    print("first move")
    print(player1.move(int(input())))
    while True:
        next_move = int(input("what's your next move ?"))
        if next_move in range(1, player1.get_border() + 1):
            print(player1.move(next_move))
        else:
            print('Impossible move')
            

if __name__ == '__main__':
    main()

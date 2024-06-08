from figures import *


class Cell:
    def __init__():
        pass


class GameBoard:
    def __init__(self):
        self.board = [[" "] * 8 for _ in range(8)]

        # white
        color = "white"
        for y in range(8):
            self.board[1][y] = Peshka((1, y), color)
        self.board[0][0] = Ladiya((0, 0), color)
        self.board[0][7] = Ladiya((0, 7), color)
        self.board[0][1] = Kon((0, 1), color)
        self.board[0][6] = Kon((0, 6), color)
        self.board[0][2] = Slon((0, 2), color)
        self.board[0][5] = Slon((0, 5), color)
        self.board[0][3] = King((0, 3), color)
        self.board[0][4] = Queen((0, 4), color)

        # black
        color = "black"
        for y in range(8):
            self.board[6][y] = Peshka((6, y), color)
        self.board[7][0] = Ladiya((7, 0), color)
        self.board[7][7] = Ladiya((7, 7), color)
        self.board[7][1] = Kon((7, 1), color)
        self.board[7][6] = Kon((7, 6), color)
        self.board[7][2] = Slon((7, 2), color)
        self.board[7][5] = Slon((7, 5), color)
        self.board[7][3] = King((7, 3), color)
        self.board[7][4] = Queen((7, 4), color)

    def choose_step(self):
        pass

    def win(self):
        pass

    def __str__(self):

        return "\n".join(map(lambda x: " ".join(map(lambda y: str(y), x)), self.board))

from figures import *


class GameBoard:
    def __init__(self, povorot_doski: bool = False):
        self.povorot_doski = povorot_doski
        self.board = [[" "] * 8 for _ in range(8)]

        # white
        color = "БЕЛЫЕ"
        for y in range(8):
            self.board[1][y] = Peshka(1, y, color)
        self.board[0][0] = Ladiya(0, 0, color)
        self.board[0][7] = Ladiya(0, 7, color)
        self.board[0][1] = Kon(0, 1, color)
        self.board[0][6] = Kon(0, 6, color)
        self.board[0][2] = Slon(0, 2, color)
        self.board[0][5] = Slon(0, 5, color)
        self.board[0][3] = King(0, 3, color)
        self.board[0][4] = Queen(0, 4, color)

        # black
        color = "ЧЕРНЫЕ"
        for y in range(8):
            self.board[6][y] = Peshka(6, y, color)
        self.board[7][0] = Ladiya(7, 0, color)
        self.board[7][7] = Ladiya(7, 7, color)
        self.board[7][1] = Kon(7, 1, color)
        self.board[7][6] = Kon(7, 6, color)
        self.board[7][2] = Slon(7, 2, color)
        self.board[7][5] = Slon(7, 5, color)
        self.board[7][3] = King(7, 3, color)
        self.board[7][4] = Queen(7, 4, color)

    def win(self):
        return False

    def check_koordinates(self, x, y, step):
        try:
            if self.board[x][y] == " ":
                return False
            if self.board[x][y].color != step:
                # print(self.board[koords[0]][koords[1]].color != step, self.board[koords[0]][koords[1]].color, step)
                return False
            return True
        except:
            return False

    def move_to(self, x, y, x_new, y_new):
        self.board[x_new][y_new], self.board[x][y] = self.board[x][y], " "
        self.board[x_new][y_new].x = x_new
        self.board[x_new][y_new].y = y_new

        # проверка на переход пешки в ферзя
        if isinstance(self.board[x_new][y_new], Peshka) and (
            x_new == (7 if self.board[x_new][y_new].color == "БЕЛЫЕ" else 0)
        ):
            self.board[x_new][y_new] = Queen(
                x_new, y_new, self.board[x_new][y_new].color
            )

        # проверка того, что король ходит правильно
        if isinstance(self.board[x_new][y_new], King):
            king = self.board[x_new][y_new]
            alive_enemies = []
            for i in range(8):
                for j in range(8):
                    if not isinstance(self.board[i][j], str) and self.board[i][j].color != king.color:
                        alive_enemies.append(self.board[i][j])
            
            banned_moves = set()
            for enemy in alive_enemies:
                banned_moves |= set(enemy.can_move_to(self))    
            
            if (x_new, y_new) in banned_moves:
                print('КОРОЛЮ НЕЛЬЗЯ ХОДИТЬ НА АТАКОВАННЫЕ ПОЛЯ!!!')
                self.board[x][y], self.board[x_new][y_new] = self.board[x_new][y_new], " "
                self.board[x][y].x = x
                self.board[x][y].y = y

                while (x_new, y_new) in banned_moves:
                    x_new, y_new = input('Выберите другое место для короля! : ')
                    x_new, y_new = int(x_new) - 1, ord(y_new) - 97
                
                self.board[x_new][y_new], self.board[x][y] = self.board[x][y], " "
                self.board[x_new][y_new].x = x_new
                self.board[x_new][y_new].y = y_new
            






    def __str__(self):
        board_str = [None] * 17
        board_str[0] = "   a  b  c  d  e  f  g  h "
        board_str[1] = "  ------------------------"
        for i in range(2, 17):
            if i % 2 == 0:
                # fmt: off
                board_str[i] = "|".join(map(lambda x: str(x).ljust(2), [(i-2) // 2 + 1] + self.board[(i - 2) // 2]))
                # fmt: on
            else:
                board_str[i] = "  ------------------------"
        return "\n".join(board_str if self.povorot_doski else reversed(board_str))

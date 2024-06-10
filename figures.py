from abc import ABC, abstractmethod
from typing import Tuple


class Figure(ABC):

    # @abstractmethod
    def check_step():
        pass

    # fmt: off
    @abstractmethod
    def __init__(self, x, y, color: str,):
        self.x = x
        self.y = y
        self.color = color
    # fmt: on

    # @abstractmethod
    def can_move_to(self, new_koords: Tuple[int, str]):
        pass

    # @abstractmethod
    def eat(self):
        pass

    def __str__(self) -> str:
        return self.symbol


class Peshka(Figure):
    def __init__(self, x, y, color: str):
        super().__init__(x, y, color)
        self.symbol = chr(9823 if self.color == "БЕЛЫЕ" else 9817)

    def can_move_to(self, board):
        # return True
        step = 1 if self.color == "БЕЛЫЕ" else -1
        moves = []

        # на две вперед, если начальная позиция
        start_y = (6, 1)[(step + 1) // 2]
        if (
            self.x == start_y
            and board.board[self.x + 2 * step][self.y] == " "
            and board.board[self.x + step][self.y] == " "
        ):
            moves.append((self.x + 2 * step, self.y))
        # обычный ход вперед
        # вот тут можно реализовать переход в ферзя
        if board.board[self.x + step][self.y] == " ":
            moves.append((self.x + step, self.y))
        # перемещение во время поедания
        if 0 <= self.y - 1 <= 7:
            if (
                hasattr(board.board[self.x + step][self.y - 1], "color")
                and board.board[self.x + step][self.y - 1].color != self.color
            ):
                moves.append((self.x + step, self.y - 1))

        if 0 <= self.y + 1 <= 7:
            if (
                hasattr(board.board[self.x + step][self.y + 1], "color")
                and board.board[self.x + step][self.y + 1].color != self.color
            ):
                moves.append((self.x + step, self.y + 1))
        # перемещение на базу врага и получение ферзя
        
        return moves


class Slon(Figure):
    def __init__(self, x, y, color: str):
        super().__init__(x, y, color)
        self.symbol = chr(9821 if self.color == "БЕЛЫЕ" else 9815)


class Kon(Figure):
    def __init__(self, x, y, color: str):
        super().__init__(x, y, color)
        self.symbol = chr(9822 if self.color == "БЕЛЫЕ" else 9816)


class Ladiya(Figure):
    def __init__(self, x, y, color: str):
        super().__init__(x, y, color)
        self.symbol = chr(9820 if self.color == "БЕЛЫЕ" else 9814)


class Queen(Figure):
    def __init__(self, x, y, color: str):
        super().__init__(x, y, color)
        self.symbol = chr(9819 if self.color == "БЕЛЫЕ" else 9813)


class King(Figure):
    def __init__(self, x, y, color: str):
        super().__init__(x, y, color)
        self.symbol = chr(9818 if self.color == "БЕЛЫЕ" else 9812)

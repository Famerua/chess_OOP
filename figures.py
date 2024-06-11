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

    @abstractmethod
    def can_move_to(self, board, dX, dY):
        moves = set()

        dx = dX
        dy = dY
        while (
            0 <= self.x + dx <= 7
            and 0 <= self.y + dy <= 7
            and isinstance(board.board[self.x + dx][self.y + dy], str)
        ):
            moves.add((self.x + dx, self.y + dy))
            if 0 <= self.x + dx + dX <= 7 and 0 <= self.y + dy + dY <= 7:
                dx += dX
                dy += dY
            else:
                break
        else:
            if 0 <= self.x + dx <= 7 and 0 <= self.y + dy <= 7:
                if board.board[self.x + dx][self.y + dy].color != self.color:
                    moves.add((self.x + dx, self.y + dy))
        return moves

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

    def can_move_to(self, board):
        moves = (
            super().can_move_to(board, 1, 1)
            | super().can_move_to(board, -1, -1)
            | super().can_move_to(board, -1, 1)
            | super().can_move_to(board, 1, -1)
        )
        return moves


class Kon(Figure):
    def __init__(self, x, y, color: str):
        super().__init__(x, y, color)
        self.symbol = chr(9822 if self.color == "БЕЛЫЕ" else 9816)

    def can_move_to(self, board):
        temp = set()
        for i in range(8):
            for j in range(8):
                if (self.x - i) ** 2 + (self.y - j) ** 2 == 5:
                    temp.add((i, j))

        # moves = set(filter(lambda x: not isinstance(board.board[x[0]][x[1]], str) and board.board[x[0]][x[1]].color != self.color, moves))
        moves = set()
        for move in temp:
            cell = board.board[move[0]][move[1]]
            if isinstance(cell, str) or (
                not isinstance(cell, str) and cell.color != self.color
            ):
                moves.add(move)

        return moves


class Ladiya(Figure):
    def __init__(self, x, y, color: str):
        super().__init__(x, y, color)
        self.symbol = chr(9820 if self.color == "БЕЛЫЕ" else 9814)

    def can_move_to(self, board):
        moves = (
            super().can_move_to(board, 1, 0)
            | super().can_move_to(board, -1, 0)
            | super().can_move_to(board, 0, 1)
            | super().can_move_to(board, 0, -1)
        )
        return moves


class Queen(Figure):
    def __init__(self, x, y, color: str):
        super().__init__(x, y, color)
        self.symbol = chr(9819 if self.color == "БЕЛЫЕ" else 9813)

    def can_move_to(self, board):
        moves = (
            super().can_move_to(board, 1, 0)
            | super().can_move_to(board, -1, 0)
            | super().can_move_to(board, 0, 1)
            | super().can_move_to(board, 0, -1)
            | super().can_move_to(board, 1, 1)
            | super().can_move_to(board, -1, -1)
            | super().can_move_to(board, -1, 1)
            | super().can_move_to(board, 1, -1)
        )
        return moves


class King(Figure):
    def __init__(self, x, y, color: str):
        super().__init__(x, y, color)
        self.symbol = chr(9818 if self.color == "БЕЛЫЕ" else 9812)

    def can_move_to(self, board, dX, dY):
        return super().can_move_to(board, dX, dY)

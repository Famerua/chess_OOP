from abc import ABC, abstractmethod
from typing import Tuple


class Figure(ABC):

    # @abstractmethod
    def check_step():
        pass

    # fmt: off
    @abstractmethod
    def __init__(self, koords: Tuple[int, str], color: str,):
        self.koords = koords
        self.color = color
    # fmt: on

    #@abstractmethod
    def move(self, new_koords: Tuple[int, str]):
        pass

    # @abstractmethod
    def eat(self):
        pass

    def __str__(self) -> str:
        return self.symbol


class Peshka(Figure):
    def __init__(self, koords: Tuple[int | str], color: str):
        super().__init__(koords, color)
        self.symbol = chr(9823 if self.color == "white" else 9817)

    # def __str__(self) -> str:
    #     return self.symbol


class Slon(Figure):
    def __init__(self, koords: Tuple[int | str], color: str):
        super().__init__(koords, color)
        self.symbol = chr(9821 if self.color == "white" else 9815)


class Kon(Figure):
    def __init__(self, koords: Tuple[int | str], color: str):
        super().__init__(koords, color)
        self.symbol = chr(9822 if self.color == "white" else 9816)


class Ladiya(Figure):
    def __init__(self, koords: Tuple[int | str], color: str):
        super().__init__(koords, color)
        self.symbol = chr(9820 if self.color == "white" else 9814)


class Queen(Figure):
    def __init__(self, koords: Tuple[int | str], color: str):
        super().__init__(koords, color)
        self.symbol = chr(9819 if self.color == "white" else 9813)


class King(Figure):
    def __init__(self, koords: Tuple[int | str], color: str):
        super().__init__(koords, color)
        self.symbol = chr(9818 if self.color == "white" else 9812)

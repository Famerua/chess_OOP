import gameboard
from itertools import cycle


def main():
    Board = gameboard.GameBoard()
    print(Board)

    steps = cycle(("БЕЛЫЕ", "ЧЕРНЫЕ"))
    while not Board.win():
        step = next(steps)
        x, y = input(
            f"Ходят {step}. Введите координаты фигуры, которой хотите пойти, через пробел.\n"
        )
        x, y = int(x) - 1, ord(y) - 97  # переводим в индексы двумерного списка
        #Проверка 1
        while not Board.check_koordinates(x, y, step):
            print(
                "Вы ввели неверные координаты!\nЛибо вы выбрали пустую клетку,\nлибо фигуру не вашего цвета,\nлибо формат координат неверный!"
            )
            x, y = input("Введите координаты снова! Пример: 1a. --- ")
            x, y = int(x) - 1, ord(y) - 97
        while not Board.board[x][y].can_move_to(Board):
            print("Неточные координаты! У фигуры нет свободных ходов.")
            x, y = input("Выберите другую фигуру!\n")
            x, y = int(x) - 1, ord(y) - 97
        # Здесь можно выводить возможные ходы на доске

        x_new, y_new = input("Выберите координаты куда пойти:\n")
        x_new, y_new = int(x_new) - 1, ord(y_new) - 97
        while (x_new, y_new) not in Board.board[x][y].can_move_to(Board):
            print("Ваша фигура не может сюда пойти!")
            x_new, y_new = input("Введите координаты снова! Пример: 1a. --- ")
            x_new, y_new = int(x_new) - 1, ord(y_new) - 97

        Board.move_to(x, y, x_new, y_new)
        print(Board)


if __name__ == "__main__":
    main()

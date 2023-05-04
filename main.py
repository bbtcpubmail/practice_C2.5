from typing import Union, Any


class Ship:
    def __init__(self, x, y, size, vector):
        self.x = x
        self.y = y
        self.size = size
        self.vector = vector
        self.healf = size



# Класс игрового поля
class GameDesk:
    def __init__(self, size):
        self.size = size
        self.desk = [['O'] * self.size for i in range(self.size)]

    # метод для очистки игрового поля
    def clear(self):
        self.desk = [['O'] * self.size for i in range(self.size)]

    # метод для расстановки кораблей
    def set_ship(self, ship):
        # не выходят ли координаты x и y за пределы игрового поля?
        if ship.x < 1 or ship.x > self.size or ship.y < 1 or ship.y > self.size:
            return False
        # не выходит ли корабль за пределы игрового поля
        if (ship.vector == 'R' and ship.y + ship.size - 1 > self.size
                or ship.vector == 'D' and ship.x + ship.size - 1 > self.size):
            return False

        # не заняты ли клетки
        # рассчитываем координаты "пятна" поиска
        if ship.vector == 'D':
            start_x = ship.x if ship.x == 1 else ship.x - 1
            stop_x = self.size if ship.x + ship.size - 1 == self.size else ship.x + ship.size
            start_y = ship.y if ship.y == 1 else ship.y - 1
            stop_y = ship.y if ship.y == self.size else ship.y + 1
        else:
            # ship.vector == 'R'
            start_x = ship.x if ship.x == 1 else ship.x - 1
            stop_x = ship.x if ship.x == self.size else ship.x + 1
            start_y = ship.y if ship.y == 1 else ship.y - 1
            stop_y = self.size if ship.y + ship.size - 1 == self.size else ship.y + ship.size

        for i in range(start_x - 1, stop_x):
            for j in range(start_y - 1, stop_y):
                if not self.desk[i][j] == 'O':
                    return False

        # заполняем клетки символами корабля

        for n in range(ship.size):
            if ship.vector == 'D':
                self.desk[ship.x - 1 + n][ship.y - 1] = '■'

            else:
                self.desk[ship.x - 1][ship.y - 1 + n] = '■'

        return True


def show_desk(desk):
    print()
    print("    | 1 | 2 | 3 | 4 | 5 | 6 | ")
    print("  --------------------------- ")
    for i, row in enumerate(desk):
        row_str = f"  {i + 1} | {' | '.join(row)} | "
        print(row_str)
    print()


s_1 = Ship(3, 2, 3, 'D')
s_2 = Ship(3, 1, 2, 'R')
s_3 = Ship(1, 5, 2, 'R')
s_4 = Ship(6, 6, 1, 'D')
s_5 = Ship(6, 1, 1, 'D')
s_6 = Ship(4, 4, 1, 'D')
s_7 = Ship(4, 6, 1, 'D')
d_1 = GameDesk(6)
d_1.set_ship(s_1)
d_1.set_ship(s_2)
d_1.set_ship(s_3)
d_1.set_ship(s_4)
d_1.set_ship(s_5)
d_1.set_ship(s_6)
d_1.set_ship(s_7)

show_desk(d_1.desk)

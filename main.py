from typing import Union, Any


class Ship:
    def __init__(self, x, y, size, vector):
        self.x = x
        self.y = y
        self.size = size
        self.vector = vector
        self.healf = size
        self.body = ['⬜️'] * self.size


# Класс игрового поля
class GameDesk:
    def __init__(self, size):
        self.size = size
        self.desk = [["O"] * self.size] * self.size

    # метод для очистки игрового поля
    def clear(self):
        self.desk = [["O"] * self.size] * self.size

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
            pass
            start_x = ship.x if ship.x == 1 else ship.x - 1
            stop_x = self.size if ship.x + ship.size - 1 == self.size else ship.x + ship.size
            start_y = ship.y if ship.y == 1 else ship.y - 1
            stop_y = ship.y if ship.y == self.size else ship.y + 1
        else:
            pass
            # ship.vector == 'R'
            start_x = ship.x if ship.x == 1 else ship.x - 1
            stop_x = ship.x if ship.x == self.size else ship.x + 1
            start_y = ship.y if ship.y == 1 else ship.y - 1
            stop_y = self.size if ship.y + ship.size - 1 == self.size else ship.y + ship.size

        for i in range(start_x, stop_x):
            for j in range(start_y, stop_y):
                if not self.desk[i][j] == "O":
                    return False

        # заполняем клетки символами корабля
        for i in range(ship.size):
            pass
            if ship.vector == 'D':
                self.desk[i][ship.y - 1] = '⬜️'
            else:
                self.desk[ship.x - 1][i] = '⬜️'

        return True


s_1 = Ship(3, 2, 3, 'D')
d_1 = GameDesk(6)
print(s_1.size)
print(d_1)
d_1.set_ship(s_1)
print(d_1.desk)

class Ship:
    def __init__(self, x, y, size, vector):
        self.x = x
        self.y = y
        self.size = size
        self.vector = vector
        self.health = size



    # метод повреждения корабля, возвращает 0 если "потопил"
    def strike(self):
        self.health -= 1
        return self.health


# Класс игрового поля
class GameDesk:
    def __init__(self, size):
        self.size = size
        self.desk = [['O'] * self.size for i in range(self.size)]

    # метод для очистки игрового поля
    def clear(self):
        self.desk = [['O'] * self.size for i in range(self.size)]

    # метод проверки выхода координат за пределы игрового поля
    def out_of_range(self, x, y):
        if x < 1 or x > self.size or y < 1 or y > self.size:
            return True
        return False

    # метод получения значения ячейки
    def get_cell(self, x, y):
        return self.desk[x-1][y-1]

    # метод установки значения ячейки
    def set_cell(self, x, y, char_):
        self.desk[x-1][y-1] = char_

    # метод проверки занятости ячейки
    def cell_is_free(self, x, y):
        return True if self.desk[x-1][y-1] == 'O' else False

    # метод для расстановки кораблей
    def set_ship(self, ship):
        # не выходят ли координаты x и y за пределы игрового поля?
        if self.out_of_range(ship.x, ship.y):
            raise Exception("Out of range.")
        # не выходит ли корабль за пределы игрового поля?
        if (ship.vector == 'R' and ship.y + ship.size - 1 > self.size
                or ship.vector == 'D' and ship.x + ship.size - 1 > self.size):
            raise Exception("Out of range.")

        # не заняты ли клетки?
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

        # ищем в пятне поиска что-нибудь отличное от 'O'
        for i in range(start_x - 1, stop_x):
            for j in range(start_y - 1, stop_y):
                if not self.desk[i][j] == 'O':
                    raise Exception("The Cell isn't free.")

        # все хорошо
        # заполняем клетки символами id корабля
        id_ = str(id(ship))
        for n in range(ship.size):
            if ship.vector == 'D':
                self.desk[ship.x - 1 + n][ship.y - 1] = id_
            else:
                self.desk[ship.x - 1][ship.y - 1 + n] = id_
        return True

    # метод выстрела
    def fire(self, x, y):
        # хотя бы в поле попали, уже хорошо :)
        if self.out_of_range(x, y):
            raise Exception("Out of range.")
        # в клетке уже что-то есть?
        cell = self.get_cell(x, y)
        if cell == 'T' or cell == 'X':
            raise Exception("The Cell on Fire already.")
        elif cell == 'O':
            self.set_cell(x, y, 'T')
            return 'T'
        else:  # cell is 'ship.id_'
            self.set_cell(x, y, 'X')
            return cell

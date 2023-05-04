class Ship:
    def __init__(self, x, y, size, vector):
        self.x = x
        self.y = y
        self.size = size
        self.vector = vector
        self.healf = size
        self.body = [["O"] * self.size] * self.size


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
        if (ship.vector == "h" and ship.y + ship.size - 1 > self.size
            or ship.vector == "v" and ship.x + ship.size - 1 > self.size):
            return False

        # не заняты ли клетки под кораблем
        if ship.vector == "v":
            for i in range(ship.size):
                if not self.desk[ship.x + i][ship.y] == "O":
                    return False


        if ship.vector == "H" and ship.x == 1:



d_1 = GameDesk(6)
s_1 = Ship(3,5,3,3)
print(s_1.size)




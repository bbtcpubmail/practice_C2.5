# sea batеle game for SkillFactory С2.5
import os
import re
from random import randint
from classes import Ship, GameDesk

DESK_SIZE = 6

helloText = """
***********************************************************************************************
*                                                                                             *
*      * * *    * * *      *           * * *       *     * * * *  * * * *  *      * * *       *
*     *         *         * *          *    *     * *       *        *     *      *           *
*      * * *    * * *    * * *         * * *     * * *      *        *     *      * * *       *
*           *   *       *     *        *    *   *     *     *        *     *      *           *
*      * * *    * * *  *       *       * * *   *       *    *        *     * * *  * * *       *
*                                                                                             *
***********************************************************************************************"""
gameRulesText = """
    Правила игры:
    Игра с компьютером (ИИ). Поле размером 6 х 6 клеток. В начале игры требуется расставить
    на игровом поле корабли так, чтобы между ними оставалась хотябы одна пустая клетка. Всего
    кораблей 7. Один размером в 3 клетки, два - 2 клетки, четыре - 1 клетка. Чтобы установить
    корабль на место, необходимо задать коордниаты его начальной точки X, Y(строка - столбец),
    его размер и направление (вниз - 'D', вправо - 'R'). Для выстрела игрок указывает коорди-
    наты клетки. В случае попадания клетка помечается знаком - 'Х', в случае промоха - 'T'.
    Для победы необходимо первым уничтожить все корабли соперника.
    
    """

# количество и типы кораблей
ships = [(3, 1), (2, 2), (1, 4)]
user_ships = {}
ai_ships = {}

# функция отрисовки игрового поля
def show_desk(desk, hide):
    print()
    ship_symbol = 'O' if hide else '■'
    row_str = ""
    for i in range(1, len(desk) + 1):
        row_str = row_str + '' + str(i) + ' | '
    print(f"    | {row_str}")
    # print("    | 1 | 2 | 3 | 4 | 5 | 6 | ")
    print("  ---" + "----" * len(desk))
    for i, row in enumerate(desk):
        # прячем id_ кораблей от пользователя

        row_str = f"  {i + 1} | {' | '.join(row)} | "
        row_str = re.sub('\| [0-9]+', '| ' + ship_symbol, row_str)
        # print(row_str)
        print(row_str)
    print()

# функция получения случайных координат
def get_rnd_coord(desk_size):
    x = randint(1, desk_size)
    y = randint(1, desk_size)
    v = 'D' if randint(0, 1) else 'R'
    print(x,y,v)
    return x, y, v

# выводим приветствие и правила игры
print(helloText)
print(gameRulesText)
input("                 Нажмите 'Enter' чтобы продолжить ")
print()

# создаем объекты игровых полей игрока и ИИ
player_desk = GameDesk(DESK_SIZE)
ai_desk = GameDesk(DESK_SIZE)

# получаем от игрока в цикле координаты кораблей и отображаем их на игровом поле
for size, count in ships:
    for i in range(1, count + 1):
        os.system('cls||clear')
        print("    " * int(DESK_SIZE // 2) + "Игрок")
        show_desk(player_desk.desk, False)
        show_desk(ai_desk.desk, False)
        input_str = input(
            f"    Введите координаты (X, Y) и направление "
            f" вниз - 'D', вправо - 'R' (по умолчанию 'R') корабля длиной {size} клетки ").replace(" ", "")

        x = input_str[0]
        y = input_str[1]
        v = input_str[2].upper() if len(input_str) == 3 else 'R'

        # создаем объекты кораблей
        ship = Ship(int(x), int(y), size, v, str(i))
        # расставляем корабли на игровом поле
        player_desk.set_ship(ship)
        # и помещаем их в словарь, чтобы обращаться к ним по ключу
        user_ships[str(i)] = ship
        # заодно сразу рандомно расставим корабли ИИ
        while 1:
            x, y, v = get_rnd_coord(DESK_SIZE)
            ship = Ship(x, y, size, v, str(i))
            if ai_desk.set_ship(ship):
                ai_ships[str(i)] = ship
                break
            del ship


# начинаем игру
while 1:
    os.system('cls||clear')
    print()
    print("    " * int(DESK_SIZE // 2) + "Игрок")
    show_desk(player_desk.desk, False)
    # print(player_desk.desk)
    print("    " * int(DESK_SIZE // 2) + "ИИ")
    show_desk(ai_desk.desk, False)
    print()
    print("   Стреляет игрок")
    input_str = input("    Введите координаты (X, Y) выстрела  ").replace(" ", "")
    cell = ai_desk.fire(int(input_str[0]), int(input_str[1]))
    if cell == 'T':
        print("      Мимо!")
    elif not cell:
        print("      Повторный выстрел")
    else:
        # попали в корабль, надо проверить жив ли он еще
        if ai_ships[cell].strike():
            print("     Ранил!")
        else:
            print("     Потопил!")
            ai_ships.pop(cell)
            if not len(ai_ships):
                print("Победил игрок")
                break






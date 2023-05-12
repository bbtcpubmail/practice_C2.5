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
player_ships = {}
ai_ships = {}

# функция получения случайных координат
def get_rnd_coord(desk_size):
    x = randint(1, desk_size)
    y = randint(1, desk_size)
    v = 'D' if randint(0, 1) else 'R'
    #print(x,y,v)
    return x, y, v

def check_result(cell, ship_list):
    if cell == 'T':
            print("      Мимо!")
    elif not cell:
            print("      Повторный выстрел")

    else:
    # похоже попали в корабль, надо проверить жив ли он еще
        if ship_list[cell].strike():
            print("     Ранил!")
        else:
            print("     Потопил!")
            ship_list.pop(cell)
            if not len(ship_list):
                winner = 'Человек' if ship_list is ai_ships else 'ИИ'
                os.system('cls||clear')
                print(f"""\n\n\n\n       
                *****************************
                *                           *
                       Победил {winner}      
                *                           *
                *****************************
                """)
                return False
    return True

# функция отрисовки игрового поля
def print_desk(pdesk, adesk):
    row_str = ""
    print('\n\n\n')
    print('         ' + '    ' * (DESK_SIZE // 2) + 'Человек' + '    ' + '    ' * DESK_SIZE + 'ИИ\n')
    for i in range(1, DESK_SIZE + 1):
        row_str = row_str + ('' + str(i) + ' | ')
    print(f"           | {row_str}          | {row_str}")
    # print("    | 1 | 2 | 3 | 4 | 5 | 6 | ")
    print('         ---' + '----' * DESK_SIZE + '         ' + '---' + '----' * DESK_SIZE)
    for i, row in enumerate(pdesk):
        row_str = f"         {i + 1} | {' | '.join(row)} |"
        # прячем id_ кораблей от пользователя
        row_str = re.sub('\| [0-9]+', '| ' + '■', row_str)
        print(row_str, end='')
        row_str = f"         {i + 1} | {' | '.join(adesk[i])} | "
        # то же самое для кораблей ИИ
        row_str = re.sub('\| [0-9]+', '| ' + 'O', row_str)
        print(row_str)
        print()
    print('\n\n')

# выводим приветствие и правила игры
os.system('cls||clear')
print(helloText)
print(gameRulesText)
input("                 Нажмите 'Enter' чтобы продолжить...")
print()

# создаем объекты игровых полей игрока и ИИ
player_desk = GameDesk(DESK_SIZE)
ai_desk = GameDesk(DESK_SIZE)
os.system('cls||clear')
print_desk(player_desk.desk, ai_desk.desk)

# получаем от игрока в цикле координаты кораблей и отображаем их на игровом поле
for size, count in ships:
    for i in range(1, count + 1):
        print(f"    Введите координаты (X, Y) и направление вниз - 'D', вправо - 'R' "
        f"(по умолчанию 'R') корабля длиной {size} ячейки(-а).\n")
        while 1:
            input_str = input("    (X, Y, D or R) >>>  ").split()
            # x = input_str[0]
            # y = input_str[1]
            # v = input_str[2].upper() if len(input_str) == 3 else 'R'
            try:
                x = int(input_str[0])
                y = int(input_str[1])
                v = input_str[2].upper() if len(input_str) == 3 else 'R'
            except Exception:
                print("Некорректный ввод! X и Y должны быть целыми числами, а направление - символом 'D' - вниз или"
                        " 'R' - вправо. Все координаты должны разделяться пробелами. Попробуйте еще раз.")
                print()
            else:
                break

        # создаем объекты кораблей
        ship = Ship(x, y, size, v)
        # расставляем корабли на игровом поле
        player_desk.set_ship(ship)
        # и помещаем их в словарь, чтобы обращаться к ним по ключу
        player_ships[str(id(ship))] = ship
        # заодно сразу рандомно расставим корабли ИИ.
        # дадим ему на это не более 30 циклов т.к. возможна тупиковая ситуация (поле 6х6 слишком мало)
        for j in range(30):
            x, y, v = get_rnd_coord(DESK_SIZE)
            ship = Ship(x, y, size, v)
            if ai_desk.set_ship(ship):
                ai_ships[str(id(ship))] = ship
                break
            del ship
        os.system('cls||clear')
        print_desk(player_desk.desk, ai_desk.desk)


# начинаем игру
while 1:
    print("\n    Стреляет игрок. ", end='')
    print("Введите координаты выстрела.\n")
    try:
        x, y = map(int, input("    (X, Y) >>>  ").split())
    except Exception:
        print("Некорректный ввод! X и Y должны быть целыми числами и должны разделяться пробелом. Попробуйте еще раз.")
        continue

    cell = ai_desk.fire(x, y)
    os.system('cls||clear')
    print_desk(player_desk.desk, ai_desk.desk)
    print(f'    Координаты вашего выстрела = {x}, {y}. ', end='')
    if not check_result(cell, ai_ships):
        break
    print("\n    Стреляет ИИ. ", end='')
    input("Нажмите 'Enter' чтобы продолжить...")
    x, y, v = get_rnd_coord(DESK_SIZE)
    cell = player_desk.fire(x, y)
    os.system('cls||clear')
    print_desk(player_desk.desk, ai_desk.desk)
    print(f'    Координаты выстрела ИИ = {x}, {y}. ', end='')
    if not check_result(cell, player_ships):
        break








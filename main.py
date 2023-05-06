from typing import Union, Any
import re

DESK_SIZE = 6




# функция отрисовки игрового поля
def show_desk(desk, repl):
    print()
    row_str = ""
    for i in range(1, len(desk) + 1):
        row_str = row_str + '' + str(i) + ' | '
    print(f"    | {row_str}")
    # print("    | 1 | 2 | 3 | 4 | 5 | 6 | ")
    print("  ---" + "----" * len(desk))
    for i, row in enumerate(desk):
        row_str = f"  {i + 1} | {' | '.join(row)} | "
        print(re.sub('\| [0-9]+', '| ' + repl, row_str))
    print()


s_1 = Ship(3, 2, 3, 'D', '1')
s_2 = Ship(3, 1, 2, 'R', '2')
s_3 = Ship(1, 5, 2, 'R', '3')
s_4 = Ship(6, 6, 1, 'D', '4')
s_5 = Ship(6, 1, 1, 'D', '5')
s_6 = Ship(4, 4, 1, 'D', '6')
s_7 = Ship(4, 6, 1, 'D', '7')
ships = {1: s_1, 2: s_2, 3: s_3, 4: s_4}
d_1 = GameDesk(DESK_SIZE)
d_2 = GameDesk(DESK_SIZE)
d_1.set_ship(s_1)
d_1.set_ship(s_2)
d_1.set_ship(s_3)
d_1.set_ship(s_4)
d_1.set_ship(s_5)
d_1.set_ship(s_6)
d_1.set_ship(s_7)

print()
print("    " * int(DESK_SIZE // 2) + "Игрок")
show_desk(d_1.desk, '■')
print("    " * int(DESK_SIZE // 2) + "ИИ")
show_desk(d_2.desk, 'O')

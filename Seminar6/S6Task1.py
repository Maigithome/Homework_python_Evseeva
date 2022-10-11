# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

field = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]


victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def print_field(field):
    print(field[0], end = " ")
    print(field[1], end = " ")
    print(field[2])
 
    print(field[3], end = " ")
    print(field[4], end = " ")
    print(field[5])
 
    print(field[6], end = " ")
    print(field[7], end = " ")
    print(field[8])   


def step_field(step,symbol):
    ind = field.index(step)
    field[ind] = symbol


# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "Игрок 'X'"
        elif field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win = "Игрок 'O'"

    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    print_field(field)

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок Х, ваш ход, укажите номер ячейки: "))
    else:
        symbol = "O"
        step = int(input("Игрок О, ваш ход, укажите номер ячейки: "))
 
    step_field(step,symbol) # делаем ход в указанную ячейку

    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_field(field)
print("Победил", win)

# def pole(size):
#     cells = [[i * size + j + 1 for j in range(size)] for i in range(size)]
#     print(cells)
#     return cells
#
#
# def draw_pole(cells, size):
#     w = len(str(size * size))
#     for line in cells:
#         for cell in line:
#             if cell == line[-1]:
#                 print(f'{cell:{w}}')
#             else:
#                 print(f'{cell:{w}}', end='|')
#         if line != cells[-1]:
#             print(('_' * w + '+') * (size - 1) + '_' * w)
#
def pole(size):
    cells = [i for i in range(1, size * size + 1)]
    return cells


def draw_pole(cells, size):
    w = len(str(cells[-1]))
    print(cells[0: size])
    print(cells[size: size * 2])
    print(cells[size * 2: size * 3])



def change_player(current_player):
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    return current_player


# ввод значений
def player_step(current_player, cells, size):
    steps = {'X': [], 'O': []}     # Ходы игроков
    try:
        print('Игрок', current_player, '. Куда ходить?  ', end="")
        step = int(input())
        if step < 1 or step > (size * size):
            print('Неподходящее значение, попробуй снова')
        if cells[step - 1] == 'X' or cells[step - 1] == 'O':
            print('Ячейка занята, попробуй снова')
        cells[step - 1] = current_player  # Добавление значений в игровое поле
      # добавление ходов игроков
    except ValueError:
        print('Неподходящее значение, попробуй снова')

    steps[current_player].append(step)
    print(steps)
    return steps


def who_winner(steps, current_player, size):
    winner_combinetion = []
    for i in range(size):
        winner_combinetion.append([(n + size * i) for n in range(1, size + 1)])

    for i in range(1, size + 1):
        winner_combinetion.append([(i + size * n) for n in range(size)])
    winner_combinetion.append([(i + size * (i - 1)) for i in range(1, size + 1)])
    winner_combinetion.append([(i * (size + 1) - i) for i in range(1, size + 1)]) # Вторая диагональ не настроена

    for i in winner_combinetion:
        if steps[current_player] in i:  # могут же быть лишние ходы
            return print(f'Выиграли: {current_player}')
        else:
            # return False
            continue


def game():
    print('Добро пожаловать!')
    print('Вас приветствует игра "крестики х нолики"')
    size = int(input('Введите размер стороны поля:  '))
    current_player = input('Кто будет ходить первым? X или 0?  ')
    current_player = current_player.upper()
    current_pole = pole(size)
    draw_pole(current_pole, size)
    count_steps = 0
    while count_steps <= size * size:
        steps = player_step(current_player, current_pole, size)
        draw_pole(current_pole, size)
        count_steps += 1
        who_winner(steps, current_player, size)
        current_player = change_player(current_player)
        if count_steps == size * size:
            return print('Ничья')


game()

def pole(size):       # Создает поле
    cells = [i for i in range(1, size * size + 1)]
    return cells


def draw_pole(cells, size):   # Отрисовывает поле
    w = len(str(size * size)) + 2
    print()
    for i in range(size):
        line = cells[size*i:size*(i+1)]
        for j in line:
            if j == line[-1]:
                print(f'{j:^{w}}', end='')
            else:
                print(f'{j:^{w}}', end='|')
        print()
        if line != cells[size*(size - 1):size*size]:
            print(('_' * w + '+') * (size - 1) + '_' * w)
    print()


def change_player(current_player):    # Меняет текущего игрока
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    return current_player


def player_step(current_player, cells, steps, size):   # Прописывает ходы игры
    try:
        print('Игрок', current_player, '. В какую ячейку походить?  ', end="")
        step = int(input())
        if step < 1 or step > (size * size):
            print('Неподходящее значение, попробуй снова')
        if cells[step - 1] == 'X' or cells[step - 1] == 'O':
            print('Ячейка занята, попробуй снова')
        cells[step - 1] = current_player   # Добавление значений в игровое поле
        steps[current_player].append(step)  # Добавление ходов игроков
    except ValueError:
        print('Неподходящее значение, попробуй снова')

    return steps


def who_winner(steps, current_player, size):
    winner_combinetion = []   # Создаем выигрышные комбинации
    for i in range(size):
        winner_combinetion.append([(n + size * i) for n in range(1, size + 1)])
    for i in range(1, size + 1):
        winner_combinetion.append([(i + size * n) for n in range(size)])
    winner_combinetion.append([(i + size * (i - 1)) for i in range(1, size + 1)])
    winner_combinetion.append([((size - i) + (i * size)) for i in range(size)])
# Определяем победителя
    for i in winner_combinetion:
        if all(j in steps[current_player] for j in i):
            return 'winner'


def check_size():    # Проверка ввода размера поля
    while True:
        size = input('Введите размер стороны поля:  ')
        if not size.isdigit():
            print('Это не число, введите число')
            continue
        return int(size)


def check_current_player():    # Проверка ввода игрока
    while True:
        current_player = input('Кто будет ходить первым? X или 0?  ').upper()
        if ord('А') <= ord(current_player) <= ord('я'):
            print("Пожалуйста, введите латинскую букву!")
            continue
        if current_player == 'X' or current_player == 'O':
            return current_player
        else:
            print('Неподходящее значение для игрока, попробуй снова')
            continue


def game():
    print('Добро пожаловать! \nВас приветствует игра "крестики х нолики"')

    size = check_size()
    current_player = check_current_player()
    current_pole = pole(size)
    draw_pole(current_pole, size)
    count_steps = 0             # Количество ходов
    steps = {'X': [], 'O': []}  # Ходы игроков
    while True:
        player_step(current_player, current_pole, steps, size)
        draw_pole(current_pole, size)
        who_winner(steps, current_player, size)
        count_steps += 1
        if who_winner(steps, current_player, size) == 'winner':
            print(f'Выиграли: {current_player}')
            break
        if count_steps == size * size:
            print('Ничья')
            break
        current_player = change_player(current_player)


if __name__ == "__main__":
    game()

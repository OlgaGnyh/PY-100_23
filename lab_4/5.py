import random


def get_random_password() -> str:
    # TODO написать функцию генерации случайных паролей
    znaki = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    random_password_list = random.sample(znaki, 8)
    random_password = ''.join(random_password_list)
    return str(random_password)


print(get_random_password())

# TODO написать функцию, которая выдает трехзначное число
import random


def random_num():
    random_num_list = [str(random.randint(0, 9)) for i in range(3)]
    random_num = ''.join(random_num_list)
    return int(random_num)


print(random_num())

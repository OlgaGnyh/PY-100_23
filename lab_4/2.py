import random

def get_unique_list_numbers() -> list[int]:
    # TODO написать функцию для получения списка уникальных целых чисел
    unique_list_numbers = []
    len_ = len(unique_list_numbers)
    while len_ < 15:
        num = random.randint(-10, 10)
        if num not in unique_list_numbers:
            unique_list_numbers.append(num)
            len_ = len(unique_list_numbers)
        if len_ == 15:
            break
    return unique_list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

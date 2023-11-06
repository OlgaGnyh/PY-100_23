import random
from random import choice
from collections import Counter

EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке
list_ = []
for count in counts:
    list_ = [random.choice(coin) for i in range(count)]
    list_count = Counter(list_)
    frequency = min(list_count.values()) / max(list_count.values())
    list_freq.append(frequency)

    # TODO подсчитать количество выпаданий орлов и решек
    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат

print(list_freq)

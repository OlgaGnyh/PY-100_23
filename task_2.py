# TODO решите задачу
import json

in_data = 'input.json'


def task() -> float:
    with open(in_data) as file:
        data = json.load(file)

    result = sum([dic["score"] * dic['weight'] for dic in data])
    return round(result, 3)


print(task())

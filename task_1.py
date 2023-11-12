# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
     # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as file:
        data = [line for line in csv.DictReader(file)]

      # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as out_f:
        json_data = json.dumps(data, indent=4)
    return print(json_data, end='')


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

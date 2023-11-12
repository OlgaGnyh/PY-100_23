import os

OUTPUT_FILE = "output.csv"


# TODO реализовать функцию to_csv_file

def to_csv_file(filename: str, headers: list, rows: list, delimiter=',', new_line='\n'):
    with open(filename, 'w', ) as f:
        f.write(delimiter.join(headers) + new_line)
        for line in rows:
            f.write(delimiter.join(line) + new_line)
    return f.read

if __name__ == '__main__':

    headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
    data = [
        ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
        ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
        ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
        ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
    ]

    # TODO Вызовете функцию to_csv_file и запишите данные в файл
    to_csv_file(OUTPUT_FILE, headers_list, data, ',', '\n')

    # Нужно для проверки задания
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE) as output_f:
            for line in output_f:
                print(line, end="")

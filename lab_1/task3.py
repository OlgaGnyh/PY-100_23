volume_disk_Mb = 1.44                               # объем дискеты в Мб
volume_disk_byte = volume_disk_Mb * 1024 * 1024     # объем дискеты в байтах
symbol = 4                                          # объем одного символа в байтах
line = symbol * 25                                  # объем строки
page = line * 50                                    # объем страницы
book = page * 100                                   # объем кники
books = int(volume_disk_byte / book)                # количество книг на дискете

print("Количество книг, помещающихся на дискету:", books)

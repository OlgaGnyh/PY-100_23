users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

visiting = {"Общее количество":0, "Уникальные посещения":0}

count_visiting = len(users)                 # размеру списка с посещениями
unique_count_visiting = len(set(users))     # равное количеству уникальных посещений

visiting["Общее количество"] = count_visiting
visiting["Уникальные посещения"] = unique_count_visiting

print(visiting)

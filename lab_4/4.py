# TODO написать функцию remove
# def remove(list_: list, val) -> list:
#     if val in list_:
#         index_ = list_[::-1].index(val)
#         list_remove = list_[::-1][:index_] + list_[::-1][(index_ + 1):]
#         return list_remove[::-1]
#     else:
#         return 'ValueError'

def remove(list_: list, val: any) -> list:
    if val in list_:
        indexes = [i for i in range(0, len(list_)) if list_[i] == val]
        list_remove = list_[:indexes[-1]] + list_[(indexes[-1] + 1):]
        return list_remove
    else:
        raise ValueError('ValueError')


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]

from functools import *

list_input = open('input.txt', 'r').read().split('\n')

numbers = [int(el) for el in list_input[0].split(',')]

@lru_cache(maxsize=None)
def rec_nb(nb, level=0, son_nb=0):
    count = 0
    if level >= 256:
        return 1
    if nb == 0:
        count += rec_nb(6, level + 1, son_nb + 1)
        count += rec_nb(8, level + 1, 0)
    else:
        count += rec_nb(nb - 1, level + 1, son_nb)

    return count

count = 0
for el in numbers:
    count += rec_nb(el)
print(count)
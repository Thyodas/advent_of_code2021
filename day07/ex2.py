list_input = open('input.txt', 'r').read().split('\n')

numbers = [int(el) for el in list_input[0].split(',')]

def find_min(nb_list, nb_min, nb_max):
    min_sum = -1
    min_pos = 0
    for pos in range(nb_min, nb_max + 1):
        nb_sum = 0
        for nb in nb_list:
            diff = abs(nb - pos)
            nb_sum += (diff * (diff + 1)) // 2
        if (nb_sum < min_sum or min_sum == -1):
            min_sum = nb_sum
            min_pos = pos
    return min_sum, min_pos

print(find_min(numbers, min(numbers), max(numbers)))
import re

list_input = open('input.txt', 'r').read().split('\n')

list_eval = [eval(line) for line in list_input]

def add_first_left(input_list, value, first=True):
    if first:
        if type(input_list[0]) == int:
            input_list[0] += value
            return True
        return add_first_left(input_list[0], value, False)
    if type(input_list[1]) == int:
        input_list[1] += value
        return True
    if add_first_left(input_list[1], value, False):
        return True
    if type(input_list[0]) == int:
        input_list[0] += value
        return True
    return add_first_left(input_list[0], value, False)

def add_first_right(input_list, value, first=True):
    if first:
        if type(input_list[0]) == int:
            input_list[0] += value
            return True
        return add_first_right(input_list[0], value, False)
    if type(input_list[0]) == int:
        input_list[0] += value
        return True
    if add_first_right(input_list[0], value, False):
        return True
    if type(input_list[1]) == int:
        input_list[1] += value
        return True
    return add_first_right(input_list[1], value, False)

def rec_explode(input_list, level=0):
    add_left = 0
    add_right = 0
    if level == 0:
        rec_explode.found_explode = False
    if type(input_list) == int:
        return [input_list, 0, 0]
    if level == 4 and not rec_explode.found_explode:
        rec_explode.found_explode = True
        return [0, input_list[0], input_list[1]]
    left = rec_explode(input_list[0], level + 1)
    right = rec_explode(input_list[1], level + 1)
    if left[1] or left[2]:
        if left[2] and not add_first_right(right, left[2]):
            add_right = left[2]
        add_left = left[1]
    elif right[1] or right[2]:
        if right[1] and not add_first_left(left, right[1]):
            add_left = right[1]
        add_right = right[2]
    return [[left[0], right[0]], add_left, add_right]

def rec_split(input_list):
    if type(input_list[0]) == int:
        if input_list[0] >= 10:
            divide = input_list[0] // 2
            input_list[0] = [divide, divide if input_list[0] % 2 == 0 else divide + 1]
            return True
    elif rec_split(input_list[0]):
        return True
    if type(input_list[1]) == int:
        if input_list[1] >= 10:
            divide = input_list[1] // 2
            input_list[1] = [divide, divide if input_list[1] % 2 == 0 else divide + 1]
            return True
    elif rec_split(input_list[1]):
        return True
    return False

def execute_tests(input_list):
    while True:
        input_list = rec_explode(input_list)[0]
        while rec_explode.found_explode:
            input_list = rec_explode(input_list)[0]
        splitted = rec_split(input_list)
        if not rec_explode.found_explode and not splitted:
            break
    return input_list

def add(list_a, list_b):
    new = [list_a, list_b]
    return execute_tests(new)

def calc_magnitude(input_list):
    if type(input_list) == int:
        return input_list
    left = calc_magnitude(input_list[0]) * 3
    right = calc_magnitude(input_list[1]) * 2
    return left + right

current_list = list_eval.pop(0)
for line in list_eval:
    current_list = add(current_list, line)

print(current_list)
print(calc_magnitude(current_list))
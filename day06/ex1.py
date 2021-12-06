list_input = open('input.txt', 'r').read().split('\n')

numbers = [int(el) for el in list_input[0].split(',')]

for i in range(80):
    add_list = []
    for i, nb in enumerate(numbers):
        if nb == 0:
            numbers[i] = 6
            add_list.append(8)
        else:
            numbers[i] -= 1
    for el in add_list:
        numbers.append(el)

print(len(numbers))
list_input = open('input.txt', 'r').read().split('\n')

def check(map, x, y):
    nb = int(map[y][x])
    if y + 1 < len(map):
        if int(map[y + 1][x]) <= nb:
            return False
    if y - 1 >= 0:
        if int(map[y - 1][x]) <= nb:
            return False
    if x + 1 < len(map[0]):
        if int(map[y][x + 1]) <= nb:
            return False
    if x - 1 >= 0:
        if int(map[y][x - 1]) <= nb:
            return False
    return True

count = 0
for y in range(len(list_input)):
    for x in range(len(list_input[0])):
        if check(list_input, x, y):
            count += int(list_input[y][x]) + 1

print(count)

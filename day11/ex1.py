list_input = open('input.txt', 'r').read().split('\n')

map = [[int(c) for c in line] for line in list_input]

def check(map, already, x, y):
    if map[y][x] == 0 and already[y][x] == 1:
        return 0
    map[y][x] += 1
    if map[y][x] <= 9 or already[y][x] == 1:
        return 0
    sum = 0
    already[y][x] = 1
    map[y][x] = 0
    if y + 1 < len(map):
        sum += check(map, already, x, y + 1)
        if x + 1 < len(map[0]):
            sum += check(map, already, x + 1, y + 1)
        if x - 1 >= 0:
            sum += check(map, already, x - 1, y + 1)
    if y - 1 >= 0:
        sum += check(map, already, x, y - 1)
        if x + 1 < len(map[0]):
            sum += check(map, already, x + 1, y - 1)
        if x - 1 >= 0:
            sum += check(map, already, x - 1, y - 1)
    if x + 1 < len(map[0]):
        sum += check(map, already, x + 1, y)
    if x - 1 >= 0:
        sum += check(map, already, x - 1, y)
    return 1 + sum

count = 0
for i in range(100):
    already = [[0 for c in line] for line in list_input]
    for y in range(len(map)):
        for x in range(len(map[0])):
            count += check(map, already, x, y)

print(count)
